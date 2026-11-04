from __future__ import annotations


def _result(status, step, aspect, observed, expected, evidence):
    return {
        "status": status,
        "step": step,
        "aspect": aspect,
        "observed": observed,
        "expected": expected,
        "evidence": evidence,
    }


def _count(text, unit):
    if unit == "characters":
        return len(text)
    if unit == "words":
        return len(text.split())
    return None


def _active_limits(constraints):
    limits = []
    for key, unit in (("max_characters", "characters"), ("max_words", "words")):
        item = constraints.get(key)
        if item is None:
            continue
        if not isinstance(item, dict) or not isinstance(item.get("value"), int) or isinstance(item.get("value"), bool) or item["value"] < 0:
            return None
        limits.append((unit, item["value"]))
    return limits


def check_answer_within_limit(record):
    evidence = record.get("evidence", {})
    text = evidence.get("answer_text")
    constraints = record.get("constraints", {})
    limits = _active_limits(constraints)
    pointers = ["/constraints", "/evidence/answer_text"]

    if not isinstance(text, str):
        return _result("unverified", "Length check", "answer limit", text, "copy-ready answer text", ["/evidence/answer_text"])
    if limits is None:
        return _result("unverified", "Length check", "answer limit", constraints, "valid non-negative max_characters or max_words values", ["/constraints"])
    if not limits:
        return _result("not_applicable", "Length check", "answer limit", None, "an explicit maximum length", ["/constraints"])

    observed = {unit: _count(text, unit) for unit, _ in limits}
    failed = [(unit, limit, observed[unit]) for unit, limit in limits if observed[unit] > limit]
    expected = {limit_unit: limit for limit_unit, limit in limits}
    return _result("fail" if failed else "pass", "Length check", "answer limit", {"counts": observed, "exceeded": failed}, expected, pointers)


def check_reported_count(record):
    evidence = record.get("evidence", {})
    text = evidence.get("answer_text")
    reported = evidence.get("reported_counts")
    pointers = ["/evidence/answer_text", "/evidence/reported_counts"]

    if not isinstance(text, str) or not isinstance(reported, dict) or not reported:
        return _result("unverified", "Length check", "reported count", reported, "answer text and a non-empty map of reported counts", pointers)
    observed = {}
    for unit, value in reported.items():
        if unit not in {"characters", "words"} or not isinstance(value, int) or isinstance(value, bool):
            return _result("unverified", "Length check", "reported count", reported, "integer counts keyed by characters or words", pointers)
        observed[unit] = _count(text, unit)
    failed = {unit: {"reported": value, "actual": observed[unit]} for unit, value in reported.items() if value != observed[unit]}
    return _result("fail" if failed else "pass", "Length check", "reported count", {"reported": reported, "actual": observed, "mismatches": failed}, observed, pointers)
