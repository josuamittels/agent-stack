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


def require_working_directory(path):
    import sys
    scripts = Path(__file__).resolve().parents[2] / "compose-career-profile" / "scripts"
    if str(scripts) not in sys.path:
        sys.path.insert(0, str(scripts))
    from career_workspace import require_working_directory as check
    return check(path)


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


SECTION_KEYS = ("education", "professional_experience", "personal_experience", "hard_skills", "interests", "languages")
SECTION_LABELS = {
    "en": ("Education", "Professional Experience", "Personal Experience", "Hard Skills", "Personal Interests", "Language Proficiency"),
    "de": ("Ausbildung", "Berufserfahrung", "Eigene Projekte und Engagement", "Fachkenntnisse", "Interessen", "Sprachkenntnisse"),
    "nl": ("Opleiding", "Werkervaring", "Eigen projecten en nevenactiviteiten", "Vaardigheden", "Interesses", "Talenkennis"),
    "fr": ("Formation", "Expérience professionnelle", "Projets personnels et engagements", "Compétences techniques", "Centres d’intérêt", "Langues"),
}


def section_labels(content):
    document = content.get("document", {})
    if "section_labels" in document:
        return document["section_labels"]
    language = document.get("language", "en").split("-")[0].lower()
    if language not in SECTION_LABELS:
        raise ValueError("Supply document.section_labels for this output language")
    return dict(zip(SECTION_KEYS, SECTION_LABELS[language]))


def active_sections(profile, content):
    labels = section_labels(content)
    values = {"education": profile.get("education", []),
              "professional_experience": content.get("professional_experience", []),
              "personal_experience": content.get("personal_experience", []),
              "hard_skills": content.get("hard_skills", []),
              "interests": profile.get("interests", []),
              "languages": profile.get("language_policy", {}).get("languages", [])}
    return [labels[key].upper() for key in SECTION_KEYS if values[key]]


def validate_inputs(profile: dict[str, Any], content: dict[str, Any]) -> None:
    errors = []
    if profile.get("schema_version") != 1 or content.get("schema_version") != 1:
        errors.append("Only schema_version 1 is supported")
    identity = profile.get("identity")
    if not isinstance(identity, dict) or not isinstance(identity.get("name"), str) or not identity["name"].strip():
        errors.append("identity.name must be a non-empty string")
    elif any(key in identity and identity[key] is not None and not isinstance(identity[key], str) for key in ("location",)):
        errors.append("identity.location must be a string or omitted")
    if isinstance(identity, dict):
        for key in ("portfolio", "linkedin", "phone", "email"):
            item = identity.get(key)
            if item is not None and (not isinstance(item, dict) or any(not isinstance(item.get(k), str) or not item[k].strip() for k in ("label", "url"))):
                errors.append("identity." + key + " must have a label and URL or be omitted")
    overrides = {"identity", "education", "languages", "language_policy", "interests"}.intersection(content)
    if overrides:
        errors.append("CV content may not override fixed sections: " + ", ".join(sorted(overrides)))
    document = content.get("document")
    if not isinstance(document, dict):
        errors.append("document must be an object")
    else:
        for key in ("company", "role"):
            if not isinstance(document.get(key), str):
                errors.append("document." + key + " must be a string")
        maximum = document.get("max_pages")
        if maximum is not None and (type(maximum) is not int or maximum < 1):
            errors.append("document.max_pages must be positive or null")
        try:
            labels = section_labels(content)
            if not isinstance(labels, dict) or set(labels) != set(SECTION_KEYS) or not all(isinstance(x, str) and x.strip() for x in labels.values()):
                errors.append("section_labels must name every defined section")
            elif len({x.casefold() for x in labels.values()}) != len(SECTION_KEYS):
                errors.append("Section labels must be distinct")
        except (ValueError, AttributeError, TypeError) as exc:
            errors.append(str(exc))
    for owner, key in ((profile, "education"), (profile, "interests"), (content, "professional_experience"), (content, "personal_experience"), (content, "hard_skills")):
        if not isinstance(owner.get(key, []), list):
            errors.append(key + " must be a list; use [] for absent evidence")
    if errors:
        raise ValueError("CV input validation failed:\n- " + "\n- ".join(errors))
    for key, required in (("professional_experience", ("employer", "role", "dates")), ("personal_experience", ("title", "dates")), ("hard_skills", ("label", "details"))):
        for entry in content.get(key, []):
            if not isinstance(entry, dict) or any(not isinstance(entry.get(k), str) or not entry[k].strip() for k in required):
                errors.append(key + " entries require " + ", ".join(required))
                continue
            if key != "hard_skills":
                bullets = entry.get("bullets")
                if not isinstance(bullets, list) or not 1 <= len(bullets) <= 4 or not all(isinstance(x, str) and x.strip() for x in bullets):
                    errors.append(key + " bullets must contain 1–4 non-empty strings")
    for entry in profile.get("education", []):
        if not isinstance(entry, dict) or any(not isinstance(entry.get(k), str) or not entry[k].strip() for k in ("institution", "degree", "dates")):
            errors.append("Education requires institution, degree and dates")
            continue
        if not isinstance(entry.get("details", []), list) or not all(isinstance(x, str) and x.strip() for x in entry.get("details", [])):
            errors.append("Education details must be a string list; GPA and courses are optional")
    if not all(isinstance(x, str) and x.strip() for x in profile.get("interests", [])):
        errors.append("interests must contain non-empty strings")
    policy = profile.get("language_policy", {})
    if not isinstance(policy, dict) or not isinstance(policy.get("languages", []), list):
        errors.append("language_policy.languages must be a list")
    else:
        for language in policy.get("languages", []):
            if not isinstance(language, dict) or not isinstance(language.get("name"), str) or not language["name"].strip() or language.get("level") not in ALLOWED_LANGUAGE_LABELS:
                errors.append("Languages need a name and an allowed proficiency label")
    blocked = profile.get("blocked_cv_terms", [])
    if not isinstance(blocked, list) or not all(isinstance(x, str) for x in blocked):
        errors.append("blocked_cv_terms must be a string list")
    else:
        outward = "\n".join(all_strings({"identity": identity, "education": profile.get("education", []), "interests": profile.get("interests", []), "languages": policy.get("languages", []) if isinstance(policy, dict) else [], "content": content}))
        for term in blocked:
            if term and term in outward:
                errors.append("Blocked outward-facing term: " + term)
    if not any(profile.get(k) for k in ("education",)) and not any(content.get(k) for k in ("professional_experience", "personal_experience", "hard_skills")):
        errors.append("Supply at least one substantive education, experience or skill section")
    if errors:
        raise ValueError("CV input validation failed:\n- " + "\n- ".join(errors))
