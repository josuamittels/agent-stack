"""Report bookkeeping only. Does not decide accessibility or evidence adequacy."""
import json
import math
import re


# WCAG 2.2 A/AA index, excluding obsolete 4.1.1 Parsing.
WCAG_AA = {
    "1.1.1", "1.2.1", "1.2.2", "1.2.3", "1.2.4", "1.2.5",
    "1.3.1", "1.3.2", "1.3.3", "1.3.4", "1.3.5",
    "1.4.1", "1.4.2", "1.4.3", "1.4.4", "1.4.5", "1.4.10",
    "1.4.11", "1.4.12", "1.4.13", "2.1.1", "2.1.2", "2.1.4",
    "2.2.1", "2.2.2", "2.3.1", "2.4.1", "2.4.2", "2.4.3",
    "2.4.4", "2.4.5", "2.4.6", "2.4.7", "2.4.11", "2.5.1",
    "2.5.2", "2.5.3", "2.5.4", "2.5.7", "2.5.8", "3.1.1",
    "3.1.2", "3.2.1", "3.2.2", "3.2.3", "3.2.4", "3.2.6",
    "3.3.1", "3.3.2", "3.3.3", "3.3.4", "3.3.7", "3.3.8",
    "4.1.2", "4.1.3",
}
STATUSES = {"fulfilled", "not_fulfilled", "unknown", "not_applicable"}
BASES = {"required", "advisory"}
SEVERITIES = {"critical", "high", "medium", "low"}


def _result(status, aspect, observed, expected, evidence=None):
    return {
        "status": status, "step": "Accessibility report accounting",
        "aspect": aspect, "observed": observed, "expected": expected,
        "evidence": evidence or ["/outputs/audit"],
    }


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _ids(value):
    return isinstance(value, list) and all(_text(x) for x in value)


def _load(record):
    raw = record.get("outputs", {}).get("audit")
    if not isinstance(raw, str):
        raise ValueError("Missing full audit.json output")
    data = json.loads(raw)
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise ValueError("Expected audit.json schema_version 1")
    rows = data.get("criteria")
    if not isinstance(rows, list) or not rows:
        raise ValueError("Missing nonempty criteria register")
    for row in rows:
        if not isinstance(row, dict) or not _text(row.get("id")):
            raise ValueError("Each criterion needs an ID")
        if row.get("status") not in STATUSES or row.get("basis") not in BASES:
            raise ValueError("Criterion has invalid or absent status/basis")
    return data, rows


def check_inventory(record):
    expected = "Declared inventory preserved; full baseline retains 55 required A/AA criteria"
    pointers = ["/outputs/audit", "/evidence/selected_criterion_ids", "/constraints/baseline"]
    try:
        data, rows = _load(record)
        selected = record.get("evidence", {}).get("selected_criterion_ids")
        if not _ids(selected) or not selected:
            raise ValueError("Missing pre-assessment selected_criterion_ids")
        constraint = record.get("constraints", {}).get("baseline", {})
        baseline = constraint.get("value")
        if baseline not in {"wcag-2.2-aa", "selected-criteria"}:
            raise ValueError("Missing valid resolved baseline")
        if constraint.get("source") not in {"request", "skill_default"}:
            raise ValueError("Missing baseline provenance")
        ids = [row["id"] for row in rows]
        issues = []
        if len(set(ids)) != len(ids) or len(set(selected)) != len(selected):
            issues.append("Duplicate criterion IDs")
        if set(ids) != set(selected):
            issues.append({"missing": sorted(set(selected) - set(ids)), "added": sorted(set(ids) - set(selected))})
        if data.get("scope", {}).get("baseline") != baseline:
            issues.append("Register baseline differs from resolved baseline")
        if baseline == "wcag-2.2-aa":
            required = {row["id"] for row in rows if row["basis"] == "required"}
            missing = {"WCAG22:" + x for x in WCAG_AA} - required
            if missing:
                issues.append({"missing_required_wcag": sorted(missing)})
        return _result("fail" if issues else "pass", "criterion inventory", issues or {"criterion_count": len(ids)}, expected, pointers)
    except (ValueError, TypeError, AttributeError) as exc:
        return _result("unverified", "criterion inventory", str(exc), expected, pointers)


def check_scores(record):
    expected = "Required-only counts and percentages match register and visible report table"
    pointers = ["/outputs/audit", "/outputs/main"]
    try:
        data, rows = _load(record)
        scores = data.get("scores")
        report = record.get("outputs", {}).get("main")
        if not isinstance(scores, dict) or not isinstance(report, str):
            raise ValueError("Missing scores or full report")
        counts = {status: sum(row["basis"] == "required" and row["status"] == status for row in rows) for status in STATUSES}
        assessed = counts["fulfilled"] + counts["not_fulfilled"]
        potential = assessed + counts["unknown"]
        calculated = dict(counts)
        calculated["assessed_fulfillment_pct"] = round(100 * counts["fulfilled"] / assessed, 1) if assessed else None
        calculated["assessment_coverage_pct"] = round(100 * assessed / potential, 1) if potential else None
        if set(scores) != set(calculated):
            raise ValueError("Missing or extra summary score keys")
        issues = []
        for key, value in calculated.items():
            supplied = scores[key]
            numeric = type(supplied) in {int, float} and math.isfinite(supplied)
            if value is None:
                valid = supplied is None
            elif key in STATUSES:
                valid = type(supplied) is int and supplied == value
            else:
                valid = numeric and abs(supplied - value) < 1e-8
            if not valid:
                issues.append({"metric": key, "json": supplied, "expected": value})
            pattern = r"^\s*\|\s*`?" + re.escape(key) + r"`?\s*\|\s*([^|]+)\|\s*$"
            cells = re.findall(pattern, report, re.MULTILINE)
            if len(cells) != 1:
                issues.append({"metric": key, "report_rows": len(cells)})
                continue
            cell = cells[0].strip()
            if value is None:
                matches = cell == "not assessed"
            else:
                try:
                    matches = math.isfinite(float(cell)) and abs(float(cell) - value) < 1e-8
                except ValueError:
                    matches = False
            if not matches:
                issues.append({"metric": key, "report": cell, "expected": value})
        return _result("fail" if issues else "pass", "score arithmetic and report", issues or calculated, expected, pointers)
    except (ValueError, TypeError, AttributeError) as exc:
        return _result("unverified", "score arithmetic and report", str(exc), expected, pointers)


def check_traceability(record):
    expected = "Evidence IDs resolve; failed criteria link to actionable findings; unknowns have next checks"
    try:
        data, rows = _load(record)
        findings, evidence = data.get("findings"), data.get("evidence")
        if not isinstance(findings, list) or not isinstance(evidence, list):
            raise ValueError("Missing findings/evidence arrays")
        if any(not isinstance(x, dict) or not _text(x.get("id")) for x in findings + evidence):
            raise ValueError("Evidence and findings need IDs")
        f_by_id = {x["id"]: x for x in findings}
        c_by_id = {x["id"]: x for x in rows}
        e_ids = {x["id"] for x in evidence}
        issues = []
        if len(f_by_id) != len(findings) or len(e_ids) != len(evidence) or len(c_by_id) != len(rows):
            issues.append("Duplicate criterion, finding or evidence IDs")
        for item in evidence:
            if any(not _text(item.get(k)) for k in ("location", "method", "observation")):
                issues.append({"evidence": item["id"], "missing": "location/method/observation"})
        for row in rows:
            rid = row["id"]
            e_refs, f_refs = row.get("evidence_ids"), row.get("finding_ids")
            if not _ids(e_refs) or not _ids(f_refs):
                raise ValueError("Each criterion needs evidence_ids and finding_ids arrays")
            if not _text(row.get("rationale")) or not _text(row.get("source")):
                issues.append({"criterion": rid, "missing": "rationale/source"})
            if row["status"] != "unknown" and not e_refs:
                issues.append({"criterion": rid, "missing": "evidence for confirmed outcome"})
            if not set(e_refs) <= e_ids:
                issues.append({"criterion": rid, "unresolved_evidence": sorted(set(e_refs) - e_ids)})
            if row["status"] == "unknown" and not _text(row.get("next_check")):
                issues.append({"criterion": rid, "missing": "next_check"})
            if row["status"] == "not_fulfilled" and not f_refs:
                issues.append({"criterion": rid, "missing": "remediation finding"})
            for fid in f_refs:
                if fid not in f_by_id or rid not in f_by_id[fid].get("criterion_ids", []):
                    issues.append({"criterion": rid, "invalid_finding_link": fid})
        for finding in findings:
            refs = finding.get("criterion_ids")
            if not _ids(refs) or not refs:
                raise ValueError("Each finding needs criterion_ids")
            if finding.get("severity") not in SEVERITIES or any(not _text(finding.get(k)) for k in ("location", "impact", "action", "verification")):
                issues.append({"finding": finding["id"], "missing": "severity/location/impact/action/verification"})
            for cid in refs:
                if cid not in c_by_id or finding["id"] not in c_by_id[cid].get("finding_ids", []):
                    issues.append({"finding": finding["id"], "invalid_criterion_link": cid})
        return _result("fail" if issues else "pass", "barrier/action and evidence links", issues or {"criteria": len(rows), "findings": len(findings)}, expected)
    except (ValueError, TypeError, AttributeError) as exc:
        return _result("unverified", "barrier/action and evidence links", str(exc), expected)
