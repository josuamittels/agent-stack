from __future__ import annotations


EXPECTED_SECTIONS = [
    "EDUCATION",
    "PROFESSIONAL EXPERIENCE",
    "PERSONAL EXPERIENCE",
    "HARD SKILLS",
    "PERSONAL INTERESTS",
    "LANGUAGE PROFICIENCY",
]


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
    headings = record.get("evidence", {}).get("section_headings")
    pointer = "/evidence/section_headings"
    if not isinstance(headings, list) or not all(isinstance(value, str) for value in headings):
        return _result("unverified", "PDF text extraction", "CV section order", headings, EXPECTED_SECTIONS, [pointer])
    observed = [value.strip().upper() for value in headings]
    return _result("pass" if observed == EXPECTED_SECTIONS else "fail", "PDF text extraction", "CV section order", observed, EXPECTED_SECTIONS, [pointer])
