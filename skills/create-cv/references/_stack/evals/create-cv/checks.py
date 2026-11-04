from __future__ import annotations

from pathlib import Path
import re


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


def _markdown_text(text):
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"(?m)^\s{0,3}#{1,6}\s*", "", text)
    text = re.sub(r"(?m)^\s*(?:[-*+•]\s+|\d+[.)]\s+)", "", text)
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    text = re.sub(r"(?m)^\s*-{3,}\s*$", "", text)
    text = re.sub(r"(?<!\\)[*_`~]+", "", text)
    return " ".join(text.split())


def check_job_description_archive(record):
    evidence_path = "/evidence/job_description_archive"
    item = record.get("evidence", {}).get("job_description_archive")
    if not isinstance(item, dict):
        return _result("unverified", "Application archive", "job.md", item, "machine-readable archive status and source text", [evidence_path])
    if item.get("applicable") is False:
        return _result("not_applicable", "Application archive", "job.md", False, "specific Setup Career Stack application with a full job description", [evidence_path + "/applicable"])
    if item.get("applicable") is not True:
        return _result("unverified", "Application archive", "job.md", item.get("applicable"), "applicable=true or false", [evidence_path + "/applicable"])

    source = item.get("source_text")
    application_folder = item.get("application_folder")
    job_path = item.get("job_md_path")
    job_md = record.get("outputs", {}).get("job_md")
    pointers = [evidence_path + "/source_text", evidence_path + "/application_folder", evidence_path + "/job_md_path", "/outputs/job_md"]
    if not all(isinstance(value, str) and value.strip() for value in (source, application_folder, job_path, job_md)):
        return _result("unverified", "Application archive", "job.md", {"source_text_available": bool(source), "application_folder": application_folder, "job_md_path": job_path, "job_md_available": bool(job_md)}, "complete source posting, numbered application path, and saved job.md output", pointers)

    folder = Path(application_folder)
    expected_job_path = folder / "job.md"
    in_applications = folder.parent.name == "applications" and bool(re.search(r"_\d{3,}$", folder.name))
    path_matches = Path(job_path) == expected_job_path and in_applications
    source_matches = _markdown_text(source) == _markdown_text(job_md)
    observed = {"path_matches": path_matches, "source_matches": source_matches, "application_folder": application_folder, "job_md_path": job_path}
    expected = "job_md_path equals <applications>/<numbered-job-folder>/job.md and job.md preserves all source text without added wording"
    return _result("pass" if path_matches and source_matches else "fail", "Application archive", "job.md", observed, expected, pointers)
