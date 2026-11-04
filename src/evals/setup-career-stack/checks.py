"""Objective project-structure and routing checks for career workspace setup."""

from pathlib import Path


def _result(status, aspect, observed, expected, evidence):
    return {
        "status": status,
        "step": "career workspace setup",
        "aspect": aspect,
        "observed": observed,
        "expected": expected,
        "evidence": evidence,
    }


def check_workspace_structure(context):
    evidence = ["/evidence/project_root"]
    expected = "project root contains applications/, references/, staples/, and AGENTS.md"
    root = context.get("evidence", {}).get("project_root")
    if not isinstance(root, str) or not root.strip():
        return _result("unverified", "workspace structure", "project_root is unavailable", expected, evidence)
    path = Path(root).expanduser()
    required = ["applications", "references", "staples"]
    missing_dirs = [name for name in required if not (path / name).is_dir()]
    agents_exists = (path / "AGENTS.md").is_file()
    status = "fail" if missing_dirs or not agents_exists else "pass"
    return _result(status, "workspace structure",
                   {"missing_directories": missing_dirs, "AGENTS.md_exists": agents_exists},
                   expected, evidence)


def check_career_routing_instructions(context):
    evidence = ["/outputs/AGENTS.md"]
    expected = "AGENTS.md routes to compose-career-profile, create-cv, and draft-cover-letter, supports unnamed-skill requests, matches staples, and gives project-level letter voice priority"
    content = context.get("outputs", {}).get("AGENTS.md")
    if not isinstance(content, str) or not content.strip():
        return _result("unverified", "career routing instructions", "complete AGENTS.md is unavailable", expected, evidence)
    text = content.casefold()
    required = {
        "compose-career-profile": "compose-career-profile" in text,
        "create-cv": "create-cv" in text,
        "draft-cover-letter": "draft-cover-letter" in text,
        "automatic routing": "does not name a skill" in text or "without requiring a named skill" in text,
        "staple matching": "match" in text and "staple" in text,
        "project voice priority": "takes priority over the bundled profile" in text,
    }
    missing = [name for name, present in required.items() if not present]
    return _result("fail" if missing else "pass", "career routing instructions",
                   {"missing_requirements": missing}, expected, evidence)
