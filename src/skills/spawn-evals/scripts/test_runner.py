import json
import tempfile
import unittest
from pathlib import Path

import runner


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.skill = 'demo-skill'
        self.package = self.root / 'evals' / self.skill
        self.package.mkdir(parents=True)
        self.output = self.root / 'output.txt'
        self.output.write_text('hello {{name}}', encoding='utf-8')
        self.record = self.root / 'record.json'
        self.write_record()
        self.write_package()

    def tearDown(self):
        self.temp.cleanup()

    def write_record(self, constraints=None):
        value = {'schema_version': 1, 'skill': self.skill, 'invocation_id': 'inv-1',
                 'request': 'Return a short greeting.',
                 'constraints': constraints if constraints is not None else {'max_chars': {'value': 14, 'source': 'skill_default'}},
                 'output_files': {'main': str(self.output)}, 'evidence': {}}
        self.record.write_text(json.dumps(value), encoding='utf-8')

    def write_package(self, source=None):
        rubric = {'schema_version': 1, 'skill': self.skill, 'checks': [
            {'id': 'length', 'description': 'Respect max_chars.', 'handler': 'check_length',
             'mandatory': True, 'required_inputs': ['/constraints/max_chars/value', '/outputs/main']},
            {'id': 'availability', 'description': 'A required external check.', 'handler': 'availability',
             'mandatory': True, 'required_inputs': []},
        ]}
        (self.package / 'rubric.json').write_text(json.dumps(rubric), encoding='utf-8')
        code = source or "\ndef check_length(record):\n    text = record['outputs']['main']\n    limit = record['constraints']['max_chars']['value']\n    return {'status':'pass' if len(text) <= limit else 'fail','step':'output length',\n            'aspect':'character limit','observed':len(text),'expected':limit,'evidence':['/outputs/main']}\n\ndef availability(record):\n    return {'status':'pass','step':'fixture','aspect':'availability',\n            'observed':True,'expected':True,'evidence':[]}\n"
        (self.package / 'checks.py').write_text(code, encoding='utf-8')

    def test_passes_at_boundary(self):
        result = runner.run(self.root, self.skill, self.record)
        self.assertEqual(result['status'], 'pass')
        self.assertEqual(result['checks'][0]['observed'], 14)

    def test_fails_over_limit(self):
        self.write_record({'max_chars': {'value': 13, 'source': 'request'}})
        result = runner.run(self.root, self.skill, self.record)
        self.assertEqual(result['status'], 'fail')
        self.assertEqual(result['checks'][0]['status'], 'fail')
        self.assertEqual(result['checks'][0]['step'], 'output length')

    def test_missing_package_is_unverified(self):
        value = json.loads(self.record.read_text(encoding='utf-8'))
        value['skill'] = 'missing-skill'
        self.record.write_text(json.dumps(value), encoding='utf-8')
        result = runner.run(self.root, 'missing-skill', self.record)
        self.assertEqual(result['status'], 'not_passed_unverified')

    def test_required_input_missing_is_unverified(self):
        self.write_record({})
        result = runner.run(self.root, self.skill, self.record)
        self.assertEqual(result['status'], 'not_passed_unverified')
        self.assertEqual(result['checks'][0]['aspect'], 'required input missing')

    def test_invalid_constraint_source_is_rejected(self):
        self.write_record({'max_chars': {'value': 20, 'source': 'guessed'}})
        with self.assertRaisesRegex(ValueError, 'constraint source'):
            runner.run(self.root, self.skill, self.record)

    def test_package_validation_does_not_execute_checks(self):
        marker = self.root / 'executed'
        source = (f"from pathlib import Path\nPath({str(marker)!r}).write_text('yes')\n"
                  "def check_length(record):\n    return {}\n"
                  "def availability(record):\n    return {}\n")
        self.write_package(source)
        result = runner.validate_package(self.root, self.skill)
        self.assertEqual(result['status'], 'valid')
        self.assertFalse(marker.exists())

    def test_history_keeps_only_compact_outcomes(self):
        result = runner.run(self.root, self.skill, self.record)
        history = (self.root / 'evals' / '.local' / 'runs.jsonl').read_text(encoding='utf-8')
        row = json.loads(history)
        self.assertEqual(row['status'], result['status'])
        self.assertEqual(row['checks'][0], {'id': 'length', 'status': 'pass'})
        self.assertNotIn('request', row)
        self.assertNotIn('output', row)


if __name__ == '__main__':
    unittest.main()
