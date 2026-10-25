#!/usr/bin/env python3
"""Deterministic scoring and abstract local records; model/tool orchestration stays with the skill."""
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import secrets
import sys
import tempfile
import os
import fcntl

SLUG = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
CATEGORIES = {'intent', 'fidelity', 'structure', 'evidence', 'boundaries', 'evaluation', 'quality', 'lifecycle'}
MODES = {'live', 'suite'}
ENGINE_DIR = Path(__file__).resolve().parent


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


def no_duplicates(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError('duplicate JSON field')
        out[key] = value
    return out


def parse(text):
    return json.loads(text, object_pairs_hook=no_duplicates,
                      parse_constant=lambda _: (_ for _ in ()).throw(ValueError('non-finite number')))


def load(path):
    return parse(Path(path).read_text())


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_rubric(rubric):
    require(isinstance(rubric, dict), 'rubric must be an object')
    require(isinstance(rubric.get('skill'), str) and bool(SLUG.fullmatch(rubric['skill'])), 'invalid skill slug')
    require(isinstance(rubric.get('version'), str) and bool(re.fullmatch(r'v[1-9][0-9]*', rubric['version'])), 'invalid rubric version')
    criteria = rubric.get('criteria')
    require(isinstance(criteria, list) and 3 <= len(criteria) <= 6, 'rubric needs 3–6 criteria')
    ids = set()
    for c in criteria:
        require(isinstance(c, dict), 'criterion must be an object')
        require(isinstance(c.get('id'), str) and bool(SLUG.fullmatch(c['id'])) and c['id'] not in ids, 'invalid or duplicate criterion ID')
        ids.add(c['id'])
        require(type(c.get('weight')) is int and c['weight'] > 0, 'weights must be positive integers')
        require(type(c.get('critical')) is bool and c.get('kind') in {'check', 'judge'}, 'invalid criterion type')
        require(c.get('category') in CATEGORIES, 'invalid failure category')
        for key in ['description', 'improvement_guidance']:
            require(isinstance(c.get(key), str) and bool(c[key].strip()), 'criterion text is required')
        a = c.get('anchors')
        require(isinstance(a, dict) and set(a) == {'0', '1', '2'} and all(isinstance(v, str) and v.strip() for v in a.values()), 'three explicit anchors required')
        if 'applies_if' in c:
            require(not c['critical'] and isinstance(c['applies_if'], str) and bool(SLUG.fullmatch(c['applies_if'])), 'critical criteria cannot be conditional')
    require(sum(c['weight'] for c in criteria) == 100, 'weights must total 100')
    return rubric


def applicability(rubric, flags):
    require(isinstance(flags, dict) and all(type(v) is bool for v in flags.values()), 'flags must be booleans')
    missing = [c['id'] for c in rubric['criteria'] if 'applies_if' in c and c['applies_if'] not in flags]
    active = [c for c in rubric['criteria'] if 'applies_if' not in c or flags.get(c['applies_if']) is True]
    return active, missing


def score(rubric, flags, checks, judgments, qualitative=True):
    """Only allowlisted criterion IDs and 0/1/2 outcomes affect arithmetic."""
    validate_rubric(rubric)
    active, missing = applicability(rubric, flags)
    skipped = {c['id'] for c in rubric['criteria'] if c['kind'] == 'judge'} if not qualitative else set()
    active = [c for c in active if c['id'] not in skipped]
    missing = [cid for cid in missing if cid not in skipped]
    invalid = bool(missing)
    results = {}
    for kind, values in [('check', checks), ('judge', judgments)]:
        if not isinstance(values, list):
            invalid = True
            continue
        expected = {c['id'] for c in active if c['kind'] == kind}
        seen = set()
        for item in values:
            if not isinstance(item, dict) or item.get('id') not in expected or item.get('id') in seen:
                invalid = True
                continue
            cid = item['id']
            seen.add(cid)
            valid = type(item.get('score')) is int and item['score'] in (0, 1, 2) and item.get('evidence') is True and not item.get('error')
            if not valid:
                invalid = True
            results[cid] = item['score'] if valid else None
        if seen != expected:
            invalid = True
    outcomes, failures = [], []
    for c in rubric['criteria']:
        if c['id'] in skipped:
            value, status = None, 'qualitative-skipped'
        elif c in active:
            value = results.get(c['id'])
            status = 'missing' if value is None else ('met' if value == 2 else 'gap')
        else:
            value, status = None, 'missing' if c['id'] in missing else 'not-applicable'
        outcomes.append({'id': c['id'], 'score': value, 'status': status})
        if status in {'missing', 'gap'}:
            failures.append({'criterion': c['id'], 'category': 'evidence' if status == 'missing' else c['category']})
    if invalid or not active:
        return {'score': None, 'verdict': 'incomplete', 'outcomes': outcomes, 'failures': failures,
                'process_gap': 'invalid-or-missing-evidence'}
    total = sum(Fraction(c['weight'] * results[c['id']], 2) for c in active)
    maximum = sum(c['weight'] for c in active)
    exact = 100 * total / maximum
    display = float((Decimal(exact.numerator) / Decimal(exact.denominator)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
    acceptable = exact >= 90 and all(results[c['id']] == 2 for c in active if c['critical'])
    return {'score': display, 'verdict': 'acceptable' if acceptable else 'unacceptable',
            'outcomes': outcomes, 'failures': failures}


def safe_file(root, relative):
    require(isinstance(relative, str) and not Path(relative).is_absolute(), 'resource path must be relative')
    p = (root / relative).resolve()
    require(p.is_relative_to(root) and p.is_file(), 'resource must be a file inside the stack')
    return p


def resource_digest(root, resources):
    require(isinstance(resources, list) and bool(resources), 'resource set is required')
    return digest({r: hashlib.sha256(safe_file(root, r).read_bytes()).hexdigest() for r in sorted(resources)})


def package(root, slug):
    root = root.resolve()
    require(bool(SLUG.fullmatch(slug)) and len(slug) <= 64, 'invalid package slug')
    path = (root / 'evals' / slug).resolve()
    require(path.is_relative_to(root / 'evals'), 'package escapes evals root')
    manifest = load(path / 'suite.json')
    require(manifest.get('schema_version') == 1 and manifest.get('skill') == slug, 'invalid suite manifest')
    version = manifest.get('active_rubric')
    require(isinstance(version, str) and bool(re.fullmatch(r'v[1-9][0-9]*', version)), 'invalid active rubric')
    rubric = validate_rubric(load(path / 'rubrics' / (version + '.json')))
    require(rubric['skill'] == slug and rubric['version'] == version, 'rubric identity mismatch')
    cases = load(path / 'cases.json')
    require(isinstance(cases, dict) and cases.get('skill') == slug, 'case identity mismatch')
    suite_cases = cases.get('cases')
    require(isinstance(suite_cases, list) and len(suite_cases) >= 3, 'three synthetic cases required')
    ids = set()
    for c in suite_cases:
        require(isinstance(c, dict) and isinstance(c.get('id'), str) and bool(SLUG.fullmatch(c['id'])) and c['id'] not in ids, 'invalid or duplicate case ID')
        ids.add(c['id'])
        require(c.get('expected_verdict') in {'acceptable', 'unacceptable'}, 'expected verdict required')
    extra = {}
    for p in sorted((path / 'checks').rglob('*')) if (path / 'checks').exists() else []:
        if p.is_file() and '__pycache__' not in p.parts:
            require(p.resolve().is_relative_to(path), 'checker escapes package')
            extra[str(p.relative_to(path))] = hashlib.sha256(p.read_bytes()).hexdigest()
    frozen_path = path / '.local' / 'rubrics.json'
    if frozen_path.exists():
        frozen = load(frozen_path)
        require(version not in frozen or frozen[version] == digest(rubric), 'frozen rubric changed; create a new rubric version')
    return path, rubric, cases, resource_digest(root, manifest['resources']), digest({'manifest': manifest, 'rubric': rubric, 'cases': cases, 'checks': extra})


def evaluator_digest(config):
    require(isinstance(config, dict) and isinstance(config.get('model'), str) and bool(config['model']), 'evaluator model is required')
    require(config.get('reasoning') == 'low', 'Betabert reasoning must be low')
    files = [ENGINE_DIR / 'engine.py', ENGINE_DIR.parent / 'SKILL.md'] + sorted((ENGINE_DIR.parent / 'references').glob('*.md'))
    return digest({'config': config, 'files': {str(p.relative_to(ENGINE_DIR.parent)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}})


def identity(root, slug, packet):
    allowed = {'input', 'output', 'evidence', 'flags', 'checks', 'evaluator', 'invocation_id', 'mode', 'case_id', 'qualitative_assessment', 'evaluation_id'}
    require(isinstance(packet, dict) and not set(packet) - allowed, 'unexpected packet fields')
    require('input' in packet and 'output' in packet and packet['output'] is not None, 'input and completed output required')
    require(packet.get('mode', 'live') in MODES, 'invalid evaluation mode')
    require(isinstance(packet.get('invocation_id'), str) and bool(packet['invocation_id']), 'invocation identity required')
    path, rubric, cases, revision, setup = package(root, slug)
    mode = packet.get('mode', 'live')
    if mode == 'suite':
        expected = cases['cases'][:3]
        require(packet.get('case_id') in {c['id'] for c in expected}, 'unknown synthetic case')
    else:
        require('case_id' not in packet, 'case ID only permitted for synthetic records')
    qualitative = packet.get('qualitative_assessment', True)
    require(type(qualitative) is bool, 'qualitative_assessment must be boolean')
    if not qualitative:
        require(mode == 'live' and target_status(root, slug) == 'stable', 'only stable live evaluations may skip Betabert')
        decision = path / '.local' / 'sampling' / (digest(packet['invocation_id']) + '.json')
        require(decision.exists(), 'prepare must select qualitative sampling before grading')
        saved = load(decision)
        require(saved == {'skill_revision': revision, 'qualitative_assessment': False}, 'sampling decision does not permit skipping Betabert')
    judge = evaluator_digest(packet.get('evaluator'))
    flags = packet.get('flags', {})
    applicability(rubric, flags)
    fingerprint = digest({'packet': {k: v for k, v in packet.items() if k not in {'invocation_id', 'evaluation_id'}}, 'skill_revision': revision, 'setup': setup, 'evaluator': judge})
    base = {'fingerprint': fingerprint, 'skill_revision': revision, 'setup_digest': setup, 'rubric_version': rubric['version'], 'evaluator_digest': judge, 'mode': mode, 'qualitative_assessment': qualitative, 'evaluation': digest(evaluation_id(packet))}
    if mode == 'suite':
        base['case_id'] = packet['case_id']
    return path, rubric, cases, base


@contextmanager
def locked(path):
    local = path / '.local'
    local.mkdir(parents=True, exist_ok=True)
    with (local / 'lock').open('a') as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield local
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def atomic_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix='.pending-')
    try:
        with os.fdopen(fd, 'w') as f:
            f.write(canonical(value) + '\n')
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def target_status(root, slug):
    # Read only the stack's simple top-level status field, not arbitrary YAML.
    root = root.resolve()
    manifest = load(root / 'evals' / slug / 'suite.json')
    candidates = [f'{folder}/{slug}/SKILL.md' for folder in ('skills', 'disciplines')]
    targets = [safe_file(root, p) for p in candidates if p in manifest['resources']]
    require(len(targets) == 1, 'one authoritative target SKILL.md must be listed in resources')
    text = targets[0].read_text()
    parts = text.split('---', 2)
    require(len(parts) == 3 and not parts[0].strip(), 'target frontmatter required for sampling')
    fields = re.findall(r'^status:[ \t]*(.*)$', parts[1], re.MULTILINE)
    require(len(fields) == 1, 'one target status required for sampling')
    value = fields[0].strip().strip('"\'')
    require(value in {'draft', 'experimental', 'stable', 'deprecated'}, 'unsupported target status')
    return value


def prepare(root, slug, packet):
    """Freeze one independent 5% draw per stable live invocation before lookup."""
    path, _, _, revision, _ = package(root, slug)
    require(isinstance(packet.get('invocation_id'), str) and bool(packet['invocation_id']), 'invocation identity required')
    qualitative = True
    if packet.get('mode', 'live') == 'live' and target_status(root, slug) == 'stable':
        with locked(path) as local:
            decision = local / 'sampling' / (digest(packet['invocation_id']) + '.json')
            if decision.exists():
                saved = load(decision)
                require(saved['skill_revision'] == revision, 'sampling request belongs to another revision; report and stop')
                qualitative = saved['qualitative_assessment']
            else:
                qualitative = secrets.randbelow(100) < 5
                atomic_json(decision, {'skill_revision': revision, 'qualitative_assessment': qualitative})
    prepared = {**packet, 'qualitative_assessment': qualitative}
    identity(root, slug, prepared)
    return prepared


def lookup(root, slug, packet):
    path, _, _, base = identity(root, slug, packet)
    cached = path / '.local' / 'cache' / (base['fingerprint'] + '.json')
    hit = cached.exists()
    return {'hit': hit, **base, **({'result': load(cached)} if hit else {})}


def suite_key(base):
    return {k: base[k] for k in ['skill_revision', 'setup_digest', 'evaluator_digest']}


def record(root, slug, packet, judgments):
    path, rubric, _, base = identity(root, slug, packet)
    invocation = digest(packet['invocation_id'])
    check_record_budget(root, slug, packet, base)
    with locked(path) as local:
        frozen_path = local / 'rubrics.json'
        frozen = load(frozen_path) if frozen_path.exists() else {}
        rubric_hash = digest(rubric)
        require(rubric['version'] not in frozen or frozen[rubric['version']] == rubric_hash, 'frozen rubric changed; create a new rubric version')
        if rubric['version'] not in frozen:
            frozen[rubric['version']] = rubric_hash
            atomic_json(frozen_path, frozen)
        previous = local / 'invocations' / (invocation + '.json')
        if previous.exists():
            old = load(previous)
            require(old['fingerprint'] == base['fingerprint'], 'invocation already recorded for different content; report and stop')
            return {**old, 'duplicate': True}
        cache = local / 'cache' / (base['fingerprint'] + '.json')
        reused = cache.exists()
        result = {**load(cache), **base} if reused else {**base, **score(rubric, packet.get('flags', {}), packet.get('checks', []), judgments, base['qualitative_assessment'])}
        result = {**result, 'decision': 'good' if result['verdict'] == 'acceptable' else 'not-good', 'timestamp': datetime.now(timezone.utc).isoformat(), 'cache_reused': reused}
        # Result is constructed above from fixed metadata, static guidance and numeric outcomes.
        with (path / 'runs.jsonl').open('a') as f:
            f.write(canonical(result) + '\n')
            f.flush()
            os.fsync(f.fileno())
        if result['verdict'] != 'incomplete' and not reused:
            atomic_json(cache, result)
        atomic_json(previous, result)
    finish_record(root, packet, result)
    return result


def mark_suite(root, slug, config, fingerprints):
    """Summarize exactly three recorded attempts; failure never requests a rerun."""
    path, _, cases, revision, setup = package(root, slug)
    key = {'skill_revision': revision, 'setup_digest': setup, 'evaluator_digest': evaluator_digest(config)}
    expected = {c['id'] for c in cases['cases'][:3]}
    require(len(fingerprints) == 3 and len(set(fingerprints)) == 3, 'exactly three scenario records are permitted')
    with locked(path) as local:
        rows = [parse(line) for line in (path / 'runs.jsonl').read_text().splitlines() if line]
        selected = {}
        for fp in fingerprints:
            require(isinstance(fp, str) and bool(re.fullmatch('[0-9a-f]{64}', fp)), 'invalid record fingerprint')
            matches = [r for r in rows if r['fingerprint'] == fp]
            require(bool(matches), 'scenario has not been recorded')
            r = matches[-1]
            require(suite_key(r) == key and r['mode'] == 'suite', 'scenario uses different resources, mode or evaluator')
            selected[r['case_id']] = r
        require(set(selected) == expected, 'only the three selected scenarios may be summarized')
        require(len({r['evaluation'] for r in selected.values()}) == 1, 'scenario records must belong to one evaluation')
        good = all(r['verdict'] == 'acceptable' for r in selected.values())
        result = {'key': key, 'records': sorted(fingerprints), 'decision': 'good' if good else 'not-good'}
        atomic_json(local / 'suite.json', result)
    return {'suite_complete': True, 'decision': result['decision'], **key}


def evaluation_id(packet):
    value = packet.get('evaluation_id', packet.get('invocation_id'))
    require(isinstance(value, str) and bool(value), 'evaluation identity required')
    return value


def budget_file(local, packet):
    return local / 'evaluations' / (digest(evaluation_id(packet)) + '.json')


def begin(root, slug, request):
    """Bind one authorized request to one target, mode and finite dispatch budget."""
    _, _, cases, revision, _ = package(root, slug)
    mode = request.get('mode', 'live')
    require(mode in MODES, 'only live or three-scenario evaluation is permitted')
    state = {'skill': slug, 'mode': mode, 'skill_revision': revision,
             'case_ids': [c['id'] for c in cases['cases'][:3]] if mode == 'suite' else [],
             'claims': [], 'recorded': {}, 'finished': False}
    with locked(root.resolve() / 'evals') as local:
        target = budget_file(local, request)
        if target.exists():
            old = load(target)
            require(all(old[k] == state[k] for k in ['skill', 'mode', 'skill_revision', 'case_ids']), 'evaluation is already bound; scope cannot expand')
            return old
        atomic_json(target, state)
    return state


def claim(root, slug, request):
    """Consume a dispatch slot before spawning; failed attempts are not refundable."""
    with locked(root.resolve() / 'evals') as local:
        target = budget_file(local, request)
        require(target.exists(), 'begin evaluation before dispatch')
        state = load(target)
        require(state['skill'] == slug and not state['finished'], 'evaluation scope is closed or belongs to another target')
        role = request.get('role')
        if role == 'producer':
            require(state['mode'] == 'suite' and request.get('case_id') in state['case_ids'], 'producer outside the three selected scenarios')
            slot = 'producer:' + request['case_id']
        else:
            require(role == 'judge', 'only producer or judge dispatch is permitted')
            require(state['mode'] == 'live' or all('producer:' + c in state['claims'] for c in state['case_ids']), 'consume the three producer attempts before the single judge')
            slot = 'judge'
        require(slot not in state['claims'], 'dispatch budget exhausted; report and stop')
        state['claims'].append(slot)
        atomic_json(target, state)
    return {'permitted': True, 'slot': slot}


def check_record_budget(root, slug, packet, base):
    with locked(root.resolve() / 'evals') as local:
        target = budget_file(local, packet)
        require(target.exists(), 'begin evaluation before recording')
        state = load(target)
        require(state['skill'] == slug and state['mode'] == base['mode'] and state['skill_revision'] == base['skill_revision'], 'record is outside the frozen evaluation scope')
        slot = packet.get('case_id', 'live')
        if state['mode'] == 'suite':
            require(slot in state['case_ids'] and 'producer:' + slot in state['claims'], 'scenario did not consume a producer slot')
        prior = state['recorded'].get(slot)
        require(not state['finished'] or prior is not None, 'evaluation is finished; report and stop')
        require(prior is None or (prior['invocation'] == digest(packet['invocation_id']) and prior['fingerprint'] == base['fingerprint']), 'scenario already recorded; no replacement attempt')
        cache = root / 'evals' / slug / '.local' / 'cache' / (base['fingerprint'] + '.json')
        require(not base['qualitative_assessment'] or 'judge' in state['claims'] or cache.exists(), 'claim the single judge attempt before recording')
        if prior is None:
            state['recorded'][slot] = {'invocation': digest(packet['invocation_id']), 'fingerprint': base['fingerprint'], 'pending': True}
            atomic_json(target, state)


def finish_record(root, packet, result):
    with locked(root.resolve() / 'evals') as local:
        target = budget_file(local, packet)
        state = load(target)
        slot = packet.get('case_id', 'live')
        state['recorded'][slot] = {'invocation': digest(packet['invocation_id']), 'fingerprint': result['fingerprint']}
        state['finished'] = state['mode'] == 'live' or (len(state['recorded']) == 3 and all(not r.get('pending') for r in state['recorded'].values()))
        atomic_json(target, state)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('command', choices=['validate', 'begin', 'claim', 'prepare', 'lookup', 'record', 'status', 'mark-suite'])
    ap.add_argument('--root', type=Path, default=Path.cwd())
    ap.add_argument('--skill', required=True)
    args = ap.parse_args()
    root = args.root.resolve()
    if args.command == 'validate':
        _, rubric, _, revision, setup = package(root, args.skill)
        result = {'valid': True, 'skill': args.skill, 'rubric_version': rubric['version'], 'skill_revision': revision, 'setup_digest': setup}
    else:
        request = parse(sys.stdin.read())
        if args.command == 'begin':
            result = begin(root, args.skill, request)
        elif args.command == 'claim':
            result = claim(root, args.skill, request)
        elif args.command == 'prepare':
            result = prepare(root, args.skill, request)
        elif args.command == 'lookup':
            result = lookup(root, args.skill, request)
        elif args.command == 'record':
            require(isinstance(request, dict) and set(request) <= {'packet', 'judgments'}, 'record expects packet and judgments')
            result = record(root, args.skill, request['packet'], request.get('judgments', []))
        elif args.command == 'mark-suite':
            result = mark_suite(root, args.skill, request['evaluator'], request['fingerprints'])
        else:
            path, _, _, revision, setup = package(root, args.skill)
            key = {'skill_revision': revision, 'setup_digest': setup, 'evaluator_digest': evaluator_digest(request['evaluator'])}
            marker = path / '.local' / 'suite.json'
            result = {'suite_required': False, 'suite_current': marker.exists() and load(marker).get('key') == key, **key}
    print(canonical(result))


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        # No packet contents or model responses are printed on failures.
        print(canonical({'decision': 'not-good', 'verdict': 'incomplete', 'error': type(error).__name__, 'message': str(error) if isinstance(error, ValueError) else 'invalid-or-unavailable-setup'}))
        sys.exit(2)
