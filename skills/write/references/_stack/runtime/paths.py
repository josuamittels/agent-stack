"""User-owned paths, independent of an installed Agent Stack package."""
import argparse
import json
import os
from pathlib import Path


def config_directory(override=None):
    return Path(override or os.environ.get('AGENT_STACK_CONFIG_DIR') or
                Path(os.environ.get('XDG_CONFIG_HOME', Path.home() / '.config')) / 'agent-stack').expanduser()


def state_directory(override=None):
    return Path(override or os.environ.get('AGENT_STACK_STATE_DIR') or
                Path(os.environ.get('XDG_STATE_HOME', Path.home() / '.local/state')) / 'agent-stack').expanduser()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config-dir')
    parser.add_argument('--state-dir')
    args = parser.parse_args()
    print(json.dumps({'config_dir': str(config_directory(args.config_dir)),
                      'state_dir': str(state_directory(args.state_dir)),
                      'openalex_env': str(config_directory(args.config_dir) / 'research-literature.env')}))
