#!/usr/bin/env python3
"""Run Research's configured objective package against one invocation record."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'skills/spawn-evals/scripts'))
import runner


def complete(root, record_file):
    return runner.run(root, 'research', record_file)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--record', type=Path, required=True,
                        help='structured Research invocation record in JSON')
    args = parser.parse_args()
    result = complete(args.root, args.record)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(',', ':')))
    return {'pass': 0, 'fail': 1, 'not_passed_unverified': 2}[result['status']]


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(json.dumps({'schema_version': 1, 'skill': 'research',
                          'status': 'not_passed_unverified', 'checks': [],
                          'error': str(error) if isinstance(error, ValueError)
                          else 'checker-input-unavailable'}, sort_keys=True))
        sys.exit(2)
