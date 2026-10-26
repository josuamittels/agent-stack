#!/usr/bin/env python3
"""Run one skill's deterministic objective checks against a structured record."""
import argparse
import ast
from datetime import datetime, timezone
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import sys


SLUG = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
RECORD_KEYS = {'schema_version', 'skill', 'invocation_id', 'request', 'constraints', 'output_files', 'evidence'}
HANDLER_RESULT_KEYS = {'status', 'step', 'aspect', 'observed', 'expected', 'evidence'}
STATUSES = {'pass', 'fail', 'unverified', 'not_applicable'}


def load_json(path):
    def no_duplicates(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=no_duplicates,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError('invalid JSON number: ' + value)))


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':'))


def pointer(value, path):
    current = value
    if path in {'', '/'}:
        return current
    for token in path.lstrip('/').split('/'):
        token = token.replace('~1', '/').replace('~0', '~')
        if isinstance(current, list):
            current = current[int(token)]
        else:
            current = current[token]
    return current


def read_record(path, expected_skill):
    record = load_json(path)
    require(isinstance(record, dict) and set(record) == RECORD_KEYS, 'record fields do not match schema_version 1')
    require(record['schema_version'] == 1 and record['skill'] == expected_skill, 'record identity mismatch')
    require(isinstance(record['invocation_id'], str) and record['invocation_id'], 'invocation_id is required')
    require(isinstance(record['request'], str) and record['request'].strip(), 'original request is required')
    require(isinstance(record['constraints'], dict), 'constraints must be an object')
    for name, item in record['constraints'].items():
        require(isinstance(name, str) and isinstance(item, dict) and set(item) == {'value', 'source'},
                'each constraint must contain value and source')
        require(item['source'] in {'request', 'skill_default'}, 'constraint source must be request or skill_default')
    require(isinstance(record['output_files'], dict) and record['output_files'], 'at least one output file is required')
    outputs = {}
    for name, value in record['output_files'].items():
        require(isinstance(name, str) and isinstance(value, str), 'output_files must map names to paths')
        outputs[name] = Path(value).read_text(encoding='utf-8')
    require(isinstance(record['evidence'], dict), 'evidence must be an object')
    return record, outputs


def require(condition, message):
    if not condition:
        raise ValueError(message)


def missing_package(skill, invocation_id):
    return {
        'schema_version': 1,
        'skill': skill,
        'invocation_id': invocation_id,
        'status': 'not_passed_unverified',
        'checks': [],
        'summary': 'No objective evaluation package is configured for this skill.',
    }


def record_history(root, result, package):
    """Persist only invocation identity hashes, check states, and digests."""
    package_digest = None
    rubric_path, checks_path = package / 'rubric.json', package / 'checks.py'
    if rubric_path.is_file() and checks_path.is_file():
        digest = hashlib.sha256()
        digest.update(rubric_path.read_bytes())
        digest.update(checks_path.read_bytes())
        package_digest = digest.hexdigest()
    invocation_id = result.get('invocation_id')
    record = {
        'schema_version': 1,
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'skill': result['skill'],
        'invocation_sha256': hashlib.sha256(invocation_id.encode('utf-8')).hexdigest() if invocation_id else None,
        'package_sha256': package_digest,
        'status': result['status'],
        'checks': [{'id': item['id'], 'status': item['status']} for item in result.get('checks', [])],
    }
    directory = Path(root).resolve() / 'evals' / '.local'
    directory.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(directory, 0o700)
    descriptor = os.open(directory / 'runs.jsonl', os.O_CREAT | os.O_APPEND | os.O_WRONLY, 0o600)
    try:
        os.write(descriptor, (canonical(record) + '\n').encode('utf-8'))
    finally:
        os.close(descriptor)


def validate_package(root, skill):
    require(bool(SLUG.fullmatch(skill)) and len(skill) <= 64, 'invalid skill slug')
    package = Path(root).resolve() / 'evals' / skill
    rubric_path, checks_path = package / 'rubric.json', package / 'checks.py'
    require(rubric_path.is_file() and checks_path.is_file(), 'objective package files are missing')
    rubric = load_json(rubric_path)
    require(isinstance(rubric, dict) and set(rubric) == {'schema_version', 'skill', 'checks'}
            and rubric.get('schema_version') == 1 and rubric.get('skill') == skill,
            'invalid rubric identity')
    checks = rubric.get('checks')
    require(isinstance(checks, list) and checks, 'rubric must define checks')
    ids = []
    for spec in checks:
        require(isinstance(spec, dict) and set(spec) == {'id', 'description', 'handler', 'mandatory', 'required_inputs'},
                'invalid check specification')
        require(isinstance(spec['id'], str) and SLUG.fullmatch(spec['id']), 'invalid check id')
        require(isinstance(spec['description'], str) and spec['description'].strip(), 'check description is required')
        require(isinstance(spec['handler'], str) and spec['handler'].isidentifier(), 'invalid check handler')
        require(type(spec['mandatory']) is bool, 'mandatory must be boolean')
        require(isinstance(spec['required_inputs'], list)
                and all(isinstance(path, str) and path.startswith('/') for path in spec['required_inputs']),
                'required_inputs must be JSON Pointers')
        ids.append(spec['id'])
    require(len(ids) == len(set(ids)), 'duplicate check id')
    require(any(spec['mandatory'] for spec in checks), 'rubric must include a mandatory check')
    tree = ast.parse(checks_path.read_text(encoding='utf-8'), filename=str(checks_path))
    functions = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}
    require(all(spec['handler'] in functions for spec in checks), 'a rubric handler is missing from checks.py')
    return {'schema_version': 1, 'skill': skill, 'status': 'valid', 'check_ids': ids}


def run(root, skill, record_path):
    require(bool(SLUG.fullmatch(skill)) and len(skill) <= 64, 'invalid skill slug')
    record, outputs = read_record(record_path, skill)
    package = Path(root).resolve() / 'evals' / skill
    rubric_path, checks_path = package / 'rubric.json', package / 'checks.py'
    if not rubric_path.is_file() or not checks_path.is_file():
        result = missing_package(skill, record['invocation_id'])
        record_history(root, result, package)
        return result
    rubric = load_json(rubric_path)
    require(isinstance(rubric, dict) and set(rubric) == {'schema_version', 'skill', 'checks'}
            and rubric.get('schema_version') == 1 and rubric.get('skill') == skill,
            'invalid rubric identity')
    checks = rubric.get('checks')
    require(isinstance(checks, list) and checks, 'rubric must define checks')
    ids = []
    for spec in checks:
        require(isinstance(spec, dict) and set(spec) == {'id', 'description', 'handler', 'mandatory', 'required_inputs'},
                'invalid check specification')
        require(isinstance(spec['id'], str) and SLUG.fullmatch(spec['id']), 'invalid check id')
        require(isinstance(spec['description'], str) and spec['description'].strip(), 'check description is required')
        require(isinstance(spec['handler'], str) and spec['handler'], 'check handler is required')
        require(type(spec['mandatory']) is bool, 'mandatory must be boolean')
        require(isinstance(spec['required_inputs'], list) and all(isinstance(p, str) for p in spec['required_inputs']),
                'required_inputs must be JSON pointers')
        require(all(path.startswith('/') for path in spec['required_inputs']), 'required_inputs must be JSON Pointers')
        ids.append(spec['id'])
    require(len(ids) == len(set(ids)), 'duplicate check id')
    require(any(spec['mandatory'] for spec in checks), 'rubric must include a mandatory check')

    runtime = {'schema_version': 1, 'skill': skill, 'invocation_id': record['invocation_id'],
               'request': record['request'], 'constraints': record['constraints'], 'outputs': outputs,
               'evidence': record['evidence']}
    module_spec = importlib.util.spec_from_file_location('skill_objective_checks', checks_path)
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)
    final = []
    for spec in checks:
        missing = []
        for path in spec['required_inputs']:
            try:
                pointer(runtime, path)
            except (KeyError, IndexError, ValueError, TypeError):
                missing.append(path)
        handler = getattr(module, spec['handler'], None)
        require(callable(handler), 'rubric handler is missing or not callable: ' + spec['handler'])
        if missing:
            item = {'status': 'unverified', 'step': 'input validation',
                    'aspect': 'required input missing', 'observed': missing,
                    'expected': spec['required_inputs'], 'evidence': []}
        else:
            try:
                item = handler(runtime)
                require(isinstance(item, dict) and set(item) == HANDLER_RESULT_KEYS,
                        'handler result has invalid fields: ' + spec['id'])
                require(item['status'] in STATUSES, 'invalid check status: ' + spec['id'])
                require(all(isinstance(item[k], str) and item[k].strip() for k in ('step', 'aspect')),
                        'each check needs a verification step and aspect: ' + spec['id'])
                require(isinstance(item['evidence'], list),
                        'evidence must be a list of locations: ' + spec['id'])
                for location in item['evidence']:
                    require(isinstance(location, str) and location.startswith('/'),
                            'evidence locations must be JSON Pointers: ' + spec['id'])
                    try:
                        pointer(runtime, location)
                    except (KeyError, IndexError, ValueError, TypeError):
                        item = {'status': 'unverified', 'step': 'result validation',
                                'aspect': 'evidence location does not resolve', 'observed': location,
                                'expected': 'a JSON Pointer into the invocation record', 'evidence': []}
                        break
            except Exception as error:
                item = {'status': 'unverified', 'step': 'check execution',
                        'aspect': 'check handler failed or returned an invalid result',
                        'observed': {'error_type': type(error).__name__, 'message': str(error)},
                        'expected': 'handler returns a valid structured check result',
                        'evidence': []}
        item = {'id': spec['id'], **item}
        item['mandatory'] = spec['mandatory']
        final.append(item)
    mandatory = [item for item in final if item['mandatory'] and item['status'] != 'not_applicable']
    if any(item['status'] == 'fail' for item in mandatory):
        status = 'fail'
    elif any(item['status'] == 'unverified' for item in mandatory):
        status = 'not_passed_unverified'
    elif any(item['status'] == 'not_applicable' for item in final):
        status = 'pass'
    else:
        status = 'pass'
    result = {'schema_version': 1, 'skill': skill, 'invocation_id': record['invocation_id'],
              'status': status, 'checks': final}
    record_history(root, result, package)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument('--skill', required=True)
    parser.add_argument('--record', type=Path)
    parser.add_argument('--validate-package', action='store_true',
                        help='validate the package without executing check handlers')
    args = parser.parse_args()
    try:
        if args.validate_package:
            print(canonical(validate_package(args.root, args.skill)))
            return 0
        require(args.record is not None, '--record is required unless --validate-package is selected')
        result = run(args.root, args.skill, args.record)
        print(canonical(result))
        return {'pass': 0, 'fail': 1, 'not_passed_unverified': 2}[result['status']]
    except Exception as error:
        print(canonical({'schema_version': 1, 'skill': args.skill, 'status': 'not_passed_unverified',
                         'checks': [], 'error_type': type(error).__name__,
                         'error': str(error) if isinstance(error, ValueError) else 'checker-input-unavailable'}))
        return 2


if __name__ == '__main__':
    sys.exit(main())
