from __future__ import annotations

from pathlib import Path


def _result(status: str, step: str, aspect: str, observed, expected, evidence: list[str]):
    return {
        "status": status,
        "step": step,
        "aspect": aspect,
        "observed": observed,
        "expected": expected,
        "evidence": evidence,
    }


def check_cv_layout_fonts(record):
    item = record.get("evidence", {}).get("cv_validation")
    pointers = ["/evidence/cv_validation"]
    if not isinstance(item, dict):
        return _result("unverified", "PDF validation", "CV layout and fonts", item, "machine-readable CV build report", pointers)

    required = {"ok", "layout", "pdf_fonts", "all_pdf_fonts_embedded"}
    missing = sorted(required - item.keys())
    if missing:
        return _result("unverified", "PDF validation", "CV layout and fonts", {"missing": missing}, "ok, layout, pdf_fonts, and all_pdf_fonts_embedded fields", pointers)

    fonts = item.get("pdf_fonts")
    if not isinstance(fonts, list) or not fonts:
        return _result("unverified", "PDF validation", "CV layout and fonts", fonts, "non-empty list of embedded EBGaramond-* font resources", pointers)
    valid_fonts = all(isinstance(font, str) and font.startswith("EBGaramond-") for font in fonts)
    passed = item.get("ok") is True and item.get("layout") == "cv" and item.get("all_pdf_fonts_embedded") is True and valid_fonts
    observed = {
        "ok": item.get("ok"),
        "layout": item.get("layout"),
        "pdf_fonts": fonts,
        "all_pdf_fonts_embedded": item.get("all_pdf_fonts_embedded"),
    }
    expected = "ok=true; layout=cv; all PDF fonts embedded; every font begins EBGaramond-"
    return _result("pass" if passed else "fail", "PDF validation", "CV layout and fonts", observed, expected, pointers)


def check_intact_experience_blocks(record):
    item = record.get("evidence", {}).get("cv_validation")
    pointer = "/evidence/cv_validation/experience_blocks_intact"
    if not isinstance(item, dict) or "experience_blocks_intact" not in item:
        return _result("unverified", "PDF validation", "experience pagination", None, "experience_blocks_intact=true", [pointer])
    observed = item.get("experience_blocks_intact")
    return _result("pass" if observed is True else "fail", "PDF validation", "experience pagination", observed, True, [pointer])


def check_cv_section_order(record):
    import sys
    scripts = Path(__file__).resolve().parents[2] / "skills" / "create-cv" / "scripts"
    if str(scripts) not in sys.path:
        sys.path.insert(0, str(scripts))
    from cv_support import active_sections, validate_inputs
    evidence = record.get("evidence", {})
    headings = evidence.get("cv_validation", {}).get("section_headings")
    profile, content = evidence.get("cv_profile"), evidence.get("cv_content")
    pointers = ["/evidence/cv_validation/section_headings", "/evidence/cv_profile", "/evidence/cv_content"]
    if not isinstance(profile, dict) or not isinstance(content, dict) or not isinstance(headings, list):
        return _result("unverified", "PDF text extraction", "CV section order", headings, "profile, content and localized build headings", pointers)
    try:
        validate_inputs(profile, content)
        expected = active_sections(profile, content)
    except (ValueError, TypeError, KeyError, AttributeError) as exc:
        return _result("unverified", "PDF text extraction", "CV section order", str(exc), "valid CV source inputs", pointers)
    return _result("pass" if headings == expected else "fail", "PDF text extraction", "CV section order", headings, expected, pointers)


def check_job_description_archive(record):
    import sys
    from pathlib import Path
    scripts = Path(__file__).resolve().parents[2] / "skills" / "compose-career-profile" / "scripts"
    if str(scripts) not in sys.path:
        sys.path.insert(0, str(scripts))
    from career_workspace import archive_result
    return archive_result(record)
