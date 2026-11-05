"""Mechanical answer bounds, complete count reporting, and archive verification."""
from pathlib import Path
import sys
scripts = Path(__file__).resolve().parents[2] / "skills" / "answer-interview" / "scripts"
if str(scripts) not in sys.path:
    sys.path.insert(0, str(scripts))
from count_answer import bounds, counts


def _result(status, aspect, observed, expected):
    return {"status": status, "step": "Answer length", "aspect": aspect, "observed": observed, "expected": expected, "evidence": ["/evidence", "/constraints"]}


def _answers(record):
    evidence = record.get("evidence", {})
    if "answers" in evidence:
        values = evidence["answers"]
        if not isinstance(values, list) or not values:
            raise ValueError("answers must be a non-empty list")
    else:
        values = [{"id": "answer", "text": evidence.get("answer_text"), "constraints": record.get("constraints", {}), "reported_counts": evidence.get("reported_counts")}]
    ids = set()
    for value in values:
        if not isinstance(value, dict) or not isinstance(value.get("id"), str) or not value["id"].strip() or value["id"] in ids:
            raise ValueError("Each answer needs a distinct id")
        ids.add(value["id"])
        if not isinstance(value.get("text"), str) or not isinstance(value.get("constraints"), dict):
            raise ValueError("Each answer needs text and resolved constraints")
    return values


def check_answer_within_limit(record):
    try:
        answers = _answers(record)
        observations, failures, applicable = [], [], False
        for answer in answers:
            limits = bounds(answer["constraints"])
            actual = counts(answer["text"])
            applicable = applicable or bool(limits)
            bad = [unit for unit, (low, high) in limits.items() if actual[unit] < low or (high is not None and actual[unit] > high)]
            observations.append({"id": answer["id"], "counts": actual, "bounds": limits, "violations": bad})
            failures.extend(bad)
        return _result("fail" if failures else "pass" if applicable else "not_applicable", "answer bounds", observations, "each answer meets every requested minimum and maximum")
    except (ValueError, TypeError, AttributeError) as exc:
        return _result("unverified", "answer bounds", str(exc), "complete answer records and valid bounds")


def check_reported_count(record):
    try:
        answers = _answers(record)
        observations, applicable, failed, missing = [], False, False, False
        for answer in answers:
            limits = bounds(answer["constraints"])
            if not limits:
                continue
            applicable = True
            reported = answer.get("reported_counts")
            if not isinstance(reported, dict) or any(unit not in reported for unit in limits):
                missing = True
                observations.append({"id": answer["id"], "missing_required_counts": sorted(limits.keys() - (reported or {}).keys()) if isinstance(reported, dict) else sorted(limits)})
                continue
            actual = counts(answer["text"])
            for unit in reported:
                if unit not in actual or type(reported[unit]) is not int:
                    missing = True
                elif reported[unit] != actual[unit]:
                    failed = True
            observations.append({"id": answer["id"], "actual": actual, "reported": reported})
        return _result("fail" if failed else "unverified" if missing else "pass" if applicable else "not_applicable", "reported counts", observations, "every applicable count is present and matches final text")
    except (ValueError, TypeError, AttributeError) as exc:
        return _result("unverified", "reported counts", str(exc), "complete answer records and bounds")

def check_job_description_archive(record):
    import sys
    from pathlib import Path
    scripts = Path(__file__).resolve().parents[2] / "skills" / "compose-career-profile" / "scripts"
    if str(scripts) not in sys.path:
        sys.path.insert(0, str(scripts))
    from career_workspace import archive_result
    return archive_result(record)
