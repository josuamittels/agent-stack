"""Executable regression checks for the shared evaluator, using synthetic temporary packages."""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('engine', Path(__file__).with_name('engine.py'))
e = importlib.util.module_from_spec(spec)
spec.loader.exec_module(e)


def rubric():
    return {'skill': 'demo', 'version': 'v1', 'criteria': [
        {'id': id, 'weight': w, 'critical': critical, 'kind': kind, 'category': 'quality',
         'description': 'Synthetic reusable criterion.', 'anchors': {'0': 'Failed.', '1': 'Partial.', '2': 'Met.'},
         'improvement_guidance': 'Repair the synthetic quality gap.'}
        for id, w, critical, kind in [('core', 10, True, 'check'), ('quality', 70, False, 'judge'), ('finish', 20, False, 'judge')]]}


def outcome(id, score=2):
    return {'id': id, 'score': score, 'evidence': True}


class ScoringTests(unittest.TestCase):
    def test_full_score(self):
        r = e.score(rubric(), {}, [outcome('core')], [outcome('quality'), outcome('finish')])
        self.assertEqual((r['score'], r['verdict']), (100.0, 'acceptable'))

    def test_skip_normalizes_and_excludes_critical_judge(self):
        r = rubric(); r['criteria'][1]['critical'] = True
        result = e.score(r, {}, [outcome('core')], [], qualitative=False)
        self.assertEqual((result['score'], result['verdict']), (100.0, 'acceptable'))
        self.assertEqual(result['outcomes'][1]['status'], 'qualitative-skipped')
        self.assertEqual(result['failures'], [])
        self.assertEqual(e.score(r, {}, [outcome('core', 1)], [], qualitative=False)['verdict'], 'unacceptable')
        self.assertEqual(e.score(r, {}, [], [], qualitative=False)['verdict'], 'incomplete')

    def test_skip_requires_objective_weight_and_evidence(self):
        r = rubric(); r['criteria'][0]['kind'] = 'judge'
        self.assertEqual(e.score(r, {}, [], [], qualitative=False)['verdict'], 'incomplete')
        c = outcome('core'); c['evidence'] = False
        self.assertEqual(e.score(rubric(), {}, [c], [], qualitative=False)['verdict'], 'incomplete')
        self.assertEqual(e.score(rubric(), {}, [outcome('core')], [outcome('quality')], qualitative=False)['verdict'], 'incomplete')

    def test_skipped_judge_flags_do_not_mask_missing_objective_flags(self):
        r = rubric(); r['criteria'][2]['applies_if'] = 'long-output'
        self.assertEqual(e.score(r, {}, [outcome('core')], [], qualitative=False)['score'], 100)
        r['criteria'][0]['critical'] = False
        r['criteria'][0]['applies_if'] = 'objective-flag'
        self.assertEqual(e.score(r, {}, [], [], qualitative=False)['verdict'], 'incomplete')

    def test_exact_threshold(self):
        r = e.score(rubric(), {}, [outcome('core')], [outcome('quality'), outcome('finish', 1)])
        self.assertEqual((r['score'], r['verdict']), (90.0, 'acceptable'))

    def test_below_threshold(self):
        r = e.score(rubric(), {}, [outcome('core')], [outcome('quality', 1), outcome('finish')])
        self.assertEqual((r['score'], r['verdict']), (65.0, 'unacceptable'))

    def test_critical_gate_above_threshold(self):
        r = e.score(rubric(), {}, [outcome('core', 1)], [outcome('quality'), outcome('finish')])
        self.assertEqual((r['score'], r['verdict']), (95.0, 'unacceptable'))

    def test_missing_evidence(self):
        v = outcome('quality'); v['evidence'] = False
        r = e.score(rubric(), {}, [outcome('core')], [v, outcome('finish')])
        self.assertEqual((r['score'], r['verdict']), (None, 'incomplete'))

    def test_missing_criterion(self):
        self.assertEqual(e.score(rubric(), {}, [], [outcome('quality'), outcome('finish')])['verdict'], 'incomplete')

    def test_malformed_judgments(self):
        variants = [None, {}, [outcome('quality'), outcome('quality'), outcome('finish')],
                    [outcome('core'), outcome('quality'), outcome('finish')],
                    [outcome('unknown'), outcome('quality'), outcome('finish')]]
        for judgments in variants:
            with self.subTest(judgments=judgments):
                self.assertEqual(e.score(rubric(), {}, [outcome('core')], judgments)['verdict'], 'incomplete')

    def test_boolean_not_numeric_score(self):
        bad = outcome('quality', True)
        self.assertEqual(e.score(rubric(), {}, [outcome('core')], [bad, outcome('finish')])['verdict'], 'incomplete')

    def test_check_error(self):
        c = outcome('core'); c['error'] = 'temporary detail must not be stored'
        self.assertEqual(e.score(rubric(), {}, [c], [outcome('quality'), outcome('finish')])['verdict'], 'incomplete')

    def test_conditionals_and_missing_flag(self):
        r = rubric(); r['criteria'][2]['applies_if'] = 'long-output'
        self.assertEqual(e.score(r, {}, [outcome('core')], [outcome('quality')])['verdict'], 'incomplete')
        result = e.score(r, {'long-output': False}, [outcome('core')], [outcome('quality')])
        self.assertEqual(result['score'], 100)
        self.assertEqual(result['outcomes'][2]['status'], 'not-applicable')

    def test_critical_cannot_be_conditional(self):
        r = rubric(); r['criteria'][0]['applies_if'] = 'optional'
        with self.assertRaises(ValueError): e.validate_rubric(r)

    def test_weights_and_duplicate_ids(self):
        r = rubric(); r['criteria'][0]['weight'] = 11
        with self.assertRaises(ValueError): e.validate_rubric(r)
        r = rubric(); r['criteria'][1]['id'] = 'core'
        with self.assertRaises(ValueError): e.validate_rubric(r)

    def test_exact_repeat_and_canonical_order(self):
        a = e.score(rubric(), {}, [outcome('core')], [outcome('quality'), outcome('finish')])
        b = e.score(rubric(), {}, [outcome('core')], [outcome('finish'), outcome('quality')])
        self.assertEqual(a, b)
        self.assertEqual(e.digest({'b': 2, 'a': 1}), e.digest({'a': 1, 'b': 2}))

    def test_strict_json(self):
        for text in ['{"a":1,"a":2}', '{"a":NaN}']:
            with self.assertRaises(ValueError): e.parse(text)


class StorageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='quality-work-')
        self.root = Path(self.tmp.name)
        self.path = self.root / 'evals/demo'
        (self.path / 'rubrics').mkdir(parents=True)
        (self.root / 'skills/demo').mkdir(parents=True)
        (self.root / 'skills/demo/SKILL.md').write_text('Synthetic skill instructions.')
        self.write('suite.json', {'schema_version': 1, 'skill': 'demo', 'active_rubric': 'v1', 'resources': ['skills/demo/SKILL.md']})
        self.write('rubrics/v1.json', rubric())
        self.write('cases.json', {'skill': 'demo', 'cases': [{'id': n, 'expected_verdict': 'acceptable'} for n in ['normal', 'boundary', 'failure']],
                                  'calibrations': [{'id': 'known-good', 'expected_verdict': 'acceptable'}, {'id': 'known-bad', 'expected_verdict': 'unacceptable'}]})
        self.packet = {'invocation_id': 'run-a', 'mode': 'suite', 'case_id': 'normal',
                       'input': {'requirements': 'PRIVATE_INPUT_SENTINEL'}, 'output': 'PRIVATE_OUTPUT_SENTINEL',
                       'evidence': {'note': 'PRIVATE_EVIDENCE_SENTINEL'}, 'flags': {}, 'checks': [outcome('core')],
                       'evaluator': {'model': 'synthetic-model', 'reasoning': 'low'}}
        self.judgments = [dict(outcome('quality'), pointer='PRIVATE_JUDGE_SENTINEL'), outcome('finish')]

    def tearDown(self): self.tmp.cleanup()

    def write(self, p, value): (self.path / p).write_text(json.dumps(value))

    def live_packet(self, status='stable'):
        (self.root / 'skills/demo/SKILL.md').write_text(f'---\nstatus: "{status}"\n---\nSynthetic instructions.')
        p = dict(self.packet, mode='live'); p.pop('case_id')
        return p

    def ready(self, packet):
        base = e.lookup(self.root, 'demo', packet)
        e.atomic_json(self.path / '.local/suite.json', {'key': e.suite_key(base)})

    def test_sampling_exact_five_percent_and_retry_retention(self):
        p = self.live_packet()
        selected = []
        for draw in range(100):
            with patch.object(e.secrets, 'randbelow', return_value=draw) as random:
                prepared = e.prepare(self.root, 'demo', dict(p, invocation_id=f'draw-{draw}'))
                selected.append(prepared['qualitative_assessment'])
                random.assert_called_once_with(100)
            with patch.object(e.secrets, 'randbelow', side_effect=AssertionError('retry redrew')):
                self.assertEqual(e.prepare(self.root, 'demo', prepared), prepared)
        self.assertEqual(sum(selected), 5)

    def test_skip_record_and_cache_are_separate_from_judged_result(self):
        p = self.live_packet()
        with patch.object(e.secrets, 'randbelow', return_value=5):
            prepared = e.prepare(self.root, 'demo', p)
        self.ready(prepared)
        result = self.do_record(prepared, [])
        self.assertEqual((result['score'], result['verdict']), (100, 'acceptable'))
        self.assertFalse(result['qualitative_assessment'])
        self.assertTrue(e.lookup(self.root, 'demo', prepared)['hit'])
        self.assertFalse(e.lookup(self.root, 'demo', dict(prepared, qualitative_assessment=True))['hit'])
        self.assertEqual(self.do_record(prepared, [])['duplicate'], True)

    def test_sampling_does_not_bypass_suite_or_selected_judge(self):
        p = self.live_packet()
        with patch.object(e.secrets, 'randbelow', return_value=99):
            prepared = e.prepare(self.root, 'demo', p)
        self.assertEqual(self.do_record(prepared, [])['process_gap'], 'suite-required')
        with patch.object(e.secrets, 'randbelow', return_value=4):
            selected = e.prepare(self.root, 'demo', dict(p, invocation_id='selected'))
        self.ready(selected)
        self.assertEqual(self.do_record(selected, [])['verdict'], 'incomplete')
        with self.assertRaises(ValueError):
            self.do_record(dict(selected, qualitative_assessment=False), [])

    def test_skip_cannot_be_forged_or_used_in_other_modes(self):
        p = self.live_packet()
        with self.assertRaises(ValueError): self.do_record(dict(p, qualitative_assessment=False), [])
        for status in ['draft', 'experimental', 'deprecated']:
            p = self.live_packet(status)
            with patch.object(e.secrets, 'randbelow', side_effect=AssertionError('unexpected draw')):
                self.assertTrue(e.prepare(self.root, 'demo', p)['qualitative_assessment'])
            with self.assertRaises(ValueError): self.do_record(dict(p, qualitative_assessment=False), [])
        self.live_packet()
        with self.assertRaises(ValueError): self.do_record(dict(self.packet, qualitative_assessment=False), [])
        with patch.object(e.secrets, 'randbelow', side_effect=AssertionError('synthetic draw')):
            self.assertTrue(e.prepare(self.root, 'demo', self.packet)['qualitative_assessment'])

    def test_sampling_revision_change_requires_new_invocation(self):
        p = self.live_packet()
        with patch.object(e.secrets, 'randbelow', return_value=99): e.prepare(self.root, 'demo', p)
        (self.root / 'skills/demo/SKILL.md').write_text('---\nstatus: stable\n---\nRevised.')
        with self.assertRaises(ValueError): e.prepare(self.root, 'demo', p)

    def do_record(self, packet=None, judgments=None):
        return e.record(self.root, 'demo', packet or self.packet, self.judgments if judgments is None else judgments)

    def test_lookup_reuse_and_abstract_log(self):
        self.assertFalse(e.lookup(self.root, 'demo', self.packet)['hit'])
        first = self.do_record()
        self.assertTrue(e.lookup(self.root, 'demo', self.packet)['hit'])
        p = dict(self.packet, invocation_id='run-b')
        second = self.do_record(p, [])
        self.assertEqual(second['score'], first['score'])
        self.assertTrue(second['cache_reused'])
        all_saved = '\n'.join(f.read_text() for f in self.path.rglob('*') if f.is_file() and ('.local' in f.parts or f.name == 'runs.jsonl'))
        for sentinel in ['PRIVATE_INPUT_SENTINEL', 'PRIVATE_OUTPUT_SENTINEL', 'PRIVATE_EVIDENCE_SENTINEL', 'PRIVATE_JUDGE_SENTINEL']:
            self.assertNotIn(sentinel, all_saved)

    def test_invocation_deduplication(self):
        self.do_record()
        self.assertTrue(self.do_record()['duplicate'])
        self.assertEqual(len((self.path / 'runs.jsonl').read_text().splitlines()), 1)
        with self.assertRaises(ValueError): self.do_record(dict(self.packet, output='different'))

    def test_fingerprint_invalidation(self):
        first = e.lookup(self.root, 'demo', self.packet)['fingerprint']
        for key, val in [('input', {'requirements': 'other'}), ('output', 'other'), ('evidence', {'new': True}),
                         ('evaluator', {'model': 'other', 'reasoning': 'low'}), ('checks', [outcome('core', 1)])]:
            self.assertNotEqual(e.lookup(self.root, 'demo', dict(self.packet, **{key: val}))['fingerprint'], first)
        (self.root / 'skills/demo/SKILL.md').write_text('Changed instructions.')
        self.assertNotEqual(e.lookup(self.root, 'demo', self.packet)['fingerprint'], first)

    def test_rubric_and_checker_invalidation(self):
        first = e.lookup(self.root, 'demo', self.packet)['fingerprint']
        r = rubric(); r['criteria'][1]['anchors']['2'] = 'New evidence anchor.'
        self.write('rubrics/v1.json', r)
        second = e.lookup(self.root, 'demo', self.packet)['fingerprint']
        self.assertNotEqual(first, second)
        (self.path / 'checks').mkdir()
        (self.path / 'checks/check.py').write_text('print(1)')
        self.assertNotEqual(second, e.lookup(self.root, 'demo', self.packet)['fingerprint'])

    def test_frozen_rubric_requires_new_version(self):
        self.do_record()
        r = rubric(); r['criteria'][1]['anchors']['2'] = 'Revised quality anchor.'
        self.write('rubrics/v1.json', r)
        with self.assertRaises(ValueError): self.do_record(dict(self.packet, invocation_id='revised'))
        r['version'] = 'v2'; self.write('rubrics/v2.json', r)
        manifest = e.load(self.path / 'suite.json'); manifest['active_rubric'] = 'v2'
        self.write('suite.json', manifest)
        self.assertEqual(self.do_record(dict(self.packet, invocation_id='new-version'))['verdict'], 'acceptable')

    def test_live_requires_completed_suite(self):
        p = dict(self.packet, mode='live'); p.pop('case_id')
        result = self.do_record(p)
        self.assertEqual(result['verdict'], 'incomplete')
        self.assertEqual(result['process_gap'], 'suite-required')
        self.assertFalse(e.lookup(self.root, 'demo', p)['hit'])

    def test_suite_marker_requires_real_matching_records(self):
        with self.assertRaises(ValueError): e.mark_suite(self.root, 'demo', self.packet['evaluator'], [])
        fps = []
        for mode, ids in [('suite', ['normal', 'boundary', 'failure']), ('calibration', ['known-good', 'known-bad'])]:
            for cid in ids:
                p = dict(self.packet, mode=mode, case_id=cid, invocation_id=cid)
                judgments = [outcome('quality', 0), outcome('finish', 0)] if cid == 'known-bad' else self.judgments
                fps.append(self.do_record(p, judgments)['fingerprint'])
        self.assertTrue(e.mark_suite(self.root, 'demo', self.packet['evaluator'], fps)['suite_complete'])
        p = dict(self.packet, mode='live', invocation_id='live-ready'); p.pop('case_id')
        self.assertEqual(self.do_record(p)['verdict'], 'acceptable')
        (self.root / 'skills/demo/SKILL.md').write_text('New resource bytes.')
        p['invocation_id'] = 'live-changed'
        self.assertEqual(self.do_record(p)['verdict'], 'incomplete')

    def test_path_escape_and_meta_bypass(self):
        with self.assertRaises(ValueError): e.package(self.root, '../demo')
        p = dict(self.packet, mode='meta');p.pop('case_id')
        with self.assertRaises(ValueError): self.do_record(p)

    def test_unexpected_packet_fields(self):
        with self.assertRaises(ValueError): self.do_record(dict(self.packet, prior_score=100))


if __name__ == '__main__':
    unittest.main(verbosity=2)
