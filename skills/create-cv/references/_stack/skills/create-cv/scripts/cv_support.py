"""Shared schema checks and bundled asset paths for the CV generator."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = SKILL_ROOT / "assets" / "fonts"
SEPARATOR_RAISE_HALF_POINTS = 5
SECTION_RULE_EIGHTH_POINTS = 14
BULLET_SIZE_HALF_POINTS = 20
ALLOWED_LANGUAGE_LABELS = (
    "native",
    "fluent",
    "prof. working",
    "lim. working",
    "A1",
    "A2",
    "B1",
    "B2",
    "C1",
    "C2",
    "basic",
)


def read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as stream:
        value = json.load(stream)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return value


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def all_strings(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from all_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from all_strings(child)


def require_keys(value: dict[str, Any], keys: tuple[str, ...], label: str, errors: list[str]) -> None:
    for key in keys:
        if key not in value:
            errors.append(f"{label}: missing `{key}`")


def validate_inputs(profile: dict[str, Any], content: dict[str, Any]) -> None:
    errors: list[str] = []
    if profile.get("schema_version") != 1 or content.get("schema_version") != 1:
        errors.append("Only schema_version 1 is supported")

    require_keys(profile, ("identity", "education", "language_policy", "interests"), "CV profile", errors)
    require_keys(
        content,
        ("document", "professional_experience", "personal_experience", "hard_skills"),
        "CV content",
        errors,
    )

    forbidden_overrides = {"identity", "education", "languages", "language_policy", "interests"}
    overrides = sorted(forbidden_overrides.intersection(content))
    if overrides:
        errors.append("CV content may not override fixed sections: " + ", ".join(overrides))

    document = content.get("document", {})
    if isinstance(document, dict):
        require_keys(document, ("company", "role"), "document", errors)
        max_pages = document.get("max_pages")
        if max_pages is not None and (isinstance(max_pages, bool) or not isinstance(max_pages, int) or max_pages < 1):
            errors.append("document.max_pages must be a positive integer or null")
    else:
        errors.append("document must be an object")

    for section_name, entry_keys in (
        ("professional_experience", ("employer", "role", "dates", "bullets")),
        ("personal_experience", ("title", "dates", "bullets")),
    ):
        entries = content.get(section_name, [])
        if not isinstance(entries, list) or not entries:
            errors.append(f"{section_name} must be a non-empty list")
            continue
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                errors.append(f"{section_name}[{index}] must be an object")
                continue
            require_keys(entry, entry_keys, f"{section_name}[{index}]", errors)
            bullets = entry.get("bullets")
            if not isinstance(bullets, list) or not bullets or not all(isinstance(x, str) and x.strip() for x in bullets):
                errors.append(f"{section_name}[{index}].bullets must be a non-empty string list")
            elif len(bullets) > 4:
                errors.append(f"{section_name}[{index}].bullets may contain at most 4 items")

    skills = content.get("hard_skills", [])
    if not isinstance(skills, list) or not skills:
        errors.append("hard_skills must be a non-empty list")
    else:
        for index, skill in enumerate(skills):
            if not isinstance(skill, dict):
                errors.append(f"hard_skills[{index}] must be an object")
                continue
            require_keys(skill, ("label", "details"), f"hard_skills[{index}]", errors)

    language_policy = profile.get("language_policy", {})
    configured_labels = language_policy.get("allowed_labels", []) if isinstance(language_policy, dict) else []
    allowed = set(configured_labels)
    languages = language_policy.get("languages", []) if isinstance(language_policy, dict) else []
    if configured_labels != list(ALLOWED_LANGUAGE_LABELS):
        errors.append("profile language_policy.allowed_labels must exactly match the locked vocabulary: " + ", ".join(ALLOWED_LANGUAGE_LABELS))
    for index, language in enumerate(languages):
        if not isinstance(language, dict) or language.get("level") not in allowed:
            errors.append(f"profile language[{index}] uses a label outside the allowed vocabulary")

    blocked_terms = profile.get("blocked_cv_terms", [])
    outward_values = {
        "identity": profile.get("identity"),
        "education": profile.get("education"),
        "languages": languages,
        "interests": profile.get("interests"),
        "content": content,
    }
    outward_text = "\n".join(all_strings(outward_values))
    for term in blocked_terms:
        if term and term in outward_text:
            errors.append(f"Blocked outward-facing term found: `{term}`")

    for education in profile.get("education", []):
        if not isinstance(education, dict):
            errors.append("Each education entry must be an object")
            continue
        require_keys(education, ("institution", "degree", "location", "dates", "details"), "education entry", errors)
        details = education.get("details", [])
        if not isinstance(details, list) or len(details) < 2:
            errors.append("Each education entry must include GPA and notable-course details")
            continue
        if not isinstance(details[0], str) or not details[0].startswith("GPA: "):
            errors.append(f"Education entry must begin with a `GPA: ` detail: `{education.get('institution', '')}`")
        if not any(isinstance(detail, str) and detail.startswith("Notable Courses: ") for detail in details):
            errors.append(f"Education entry lacks a `Notable Courses: ` detail: `{education.get('institution', '')}`")
        if any(isinstance(detail, str) and detail.startswith("Exchange Semester:") for detail in details):
            errors.append(f"Exchange semesters must be standalone education entries: `{education.get('institution', '')}`")
        for detail in details:
            if isinstance(detail, str) and re.search(r"\b\d+(?:\.\d+)?/\d+\b", detail) and not detail.startswith("GPA: "):
                errors.append(f"Academic average must start with `GPA: `: `{detail}`")

    if errors:
        raise ValueError("CV input validation failed:\n- " + "\n- ".join(errors))
