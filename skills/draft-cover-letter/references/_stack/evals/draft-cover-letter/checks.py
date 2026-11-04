from __future__ import annotations

from pathlib import Path
import re


def _result(status, step, aspect, observed, expected, evidence):
    return {
        "status": status,
        "step": step,
        "aspect": aspect,
        "observed": observed,
        "expected": expected,
        "evidence": evidence,
    }


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
