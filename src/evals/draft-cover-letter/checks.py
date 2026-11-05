from __future__ import annotations

from pathlib import Path


def _result(status, step, aspect, observed, expected, evidence):
    return {
        "status": status,
        "step": step,
        "aspect": aspect,
        "observed": observed,
        "expected": expected,
        "evidence": evidence,
    }



def check_job_description_archive(record):
    import sys
    from pathlib import Path
    scripts = Path(__file__).resolve().parents[2] / "skills" / "compose-career-profile" / "scripts"
    if str(scripts) not in sys.path:
        sys.path.insert(0, str(scripts))
    from career_workspace import archive_result
    return archive_result(record)


def check_letter_pdf(record):
    import hashlib
    import json
    item = record.get("evidence", {}).get("letter_pdf_qa")
    pointer = ["/evidence/letter_pdf_qa"]
    if isinstance(item, dict) and item.get("applicable") is False:
        return _result("not_applicable", "Letter PDF", "content and layout", False, "requested PDF output", pointer)
    if not isinstance(item, dict) or item.get("applicable") is not True:
        return _result("unverified", "Letter PDF", "content and layout", item, "explicit PDF applicability", pointer)
    try:
        pdf, source, report_path = (Path(item[k]) for k in ("pdf_path", "input_path", "validation_path"))
        report = json.loads(report_path.read_text())
        matches = report.get("pdf_sha256") == hashlib.sha256(pdf.read_bytes()).hexdigest() and report.get("input_sha256") == hashlib.sha256(source.read_bytes()).hexdigest()
    except (OSError, ValueError, TypeError, KeyError) as exc:
        return _result("unverified", "Letter PDF", "content and layout", str(exc), "available PDF, input and report", pointer)
    passed = matches and report.get("ok") is True and report.get("text_matches") is True and report.get("a4_portrait") is True and report.get("all_fonts_embedded") is True
    return _result("pass" if passed else "fail", "Letter PDF", "content and layout", {"current_hashes": matches, "report": report}, "current successful machine-readable PDF QA", pointer)
