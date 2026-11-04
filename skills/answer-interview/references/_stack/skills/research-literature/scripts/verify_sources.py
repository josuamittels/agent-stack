#!/usr/bin/env python3
"""Qualify a local scholarly inventory; no network or model calls."""
import argparse
import json
from pathlib import Path
import sys
from literature_common import LiteratureError
from literature_gate import run_gate


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise LiteratureError("invalid_arguments", message)


def main(argv=None):
    try:
        parser = Parser(description=__doc__)
        parser.add_argument("--contract", type=Path, required=True)
        parser.add_argument("--inventory", type=Path, required=True)
        parser.add_argument("--expansion", type=Path)
        parser.add_argument("--output-dir", type=Path, required=True)
        parser.add_argument("--attempt", choices=["initial", "top_up"], default="initial")
        parser.add_argument("--phase", choices=["pool", "anchors", "final"], default="final")
        parser.add_argument("--replace", action="store_true")
        result = run_gate(parser.parse_args(argv))
        print(json.dumps(result, ensure_ascii=False, allow_nan=False))
        return 0
    except (OSError, ValueError, TypeError, KeyError, AttributeError) as exc:
        print(json.dumps({"schema_version": 1, "status": "error", "error": {"code": getattr(exc, "code", "invalid_input"), "message": str(exc)}, "outputs": []}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    sys.exit(main())
