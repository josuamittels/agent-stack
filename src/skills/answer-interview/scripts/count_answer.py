#!/usr/bin/env python3
"""Count final UTF-8 answer text with explicit code-point and whitespace rules."""
import argparse
import json
from pathlib import Path


def counts(text):
    return {"characters": len(text), "words": len(text.split())}


def bounds(constraints):
    if not isinstance(constraints, dict):
        raise ValueError("constraints must be an object")
    result = {}
    for unit in ("characters", "words"):
        for prefix in ("min_", "max_"):
            key = prefix + unit
            if key in constraints:
                bound = constraints[key]
                if not isinstance(bound, dict) or type(bound.get("value")) is not int or bound["value"] < 0:
                    raise ValueError("Invalid explicit bound: " + key)
        low = constraints.get("min_" + unit, {}).get("value", 0)
        high = constraints.get("max_" + unit, {}).get("value")
        if type(low) is not int or low < 0 or (high is not None and (type(high) is not int or high < low)):
            raise ValueError("Invalid " + unit + " bounds")
        if "min_" + unit in constraints or "max_" + unit in constraints:
            result[unit] = (low, high)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("answer", type=Path, help="Exact answer only, including intentional line breaks")
    for unit in ("characters", "words"):
        parser.add_argument("--min-" + unit, type=int)
        parser.add_argument("--max-" + unit, type=int)
    args = parser.parse_args()
    constraints = {key: {"value": value} for key, value in vars(args).items() if key != "answer" and value is not None}
    try:
        limits = bounds(constraints)
        # read_bytes avoids silent newline conversion; CRLF counts as two code points.
        actual = counts(args.answer.read_bytes().decode("utf-8"))
        violations = [unit for unit, (low, high) in limits.items() if actual[unit] < low or (high is not None and actual[unit] > high)]
        print(json.dumps({"counts": actual, "within_limits": not violations, "violations": violations}))
        return 1 if violations else 0
    except (OSError, UnicodeError, ValueError, AttributeError) as exc:
        parser.exit(2, f"Error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
