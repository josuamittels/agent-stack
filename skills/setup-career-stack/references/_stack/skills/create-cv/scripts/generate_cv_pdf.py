#!/usr/bin/env python3
"""Preflight bundled assets and run the standalone CV PDF generator."""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

from cv_support import require_working_directory


SKILL_ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = SKILL_ROOT / "assets"
REFERENCE_ROOT = SKILL_ROOT / "references"
SCRIPT_ROOT = SKILL_ROOT / "scripts"
REQUIRED_FONTS = (
    "EBGaramond-Regular.ttf",
    "EBGaramond-Bold.ttf",
    "EBGaramond-RegularItalic.ttf",
    "EBGaramond-BoldItalic.ttf",
)
FONT_LICENSE = "OFL-1.1.txt"
REQUIRED_MODULES = ("docx", "PIL", "pypdf", "pypdfium2")


def iter_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for child in value.values():
            yield from iter_strings(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_strings(child)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Run the standalone EB Garamond CV generator. The PDF and "
            "editable DOCX are written beside the content unless --output-root is supplied."
        )
    )
    parser.add_argument("--content", type=Path, required=True, help="UTF-8 role-specific cv-content.json")
    parser.add_argument(
        "--profile",
        type=Path,
        required=True,
        help="Candidate-specific fixed identity, education, interests, and languages JSON",
    )
    parser.add_argument("--output-root", type=Path, help="Folder for CV.docx, CV.pdf, and qa/ outputs; defaults to the content folder")
    parser.add_argument("--preflight-only", action="store_true", help="Check bundled resources and dependencies without generating files")
    return parser


def preflight(content_path: Path, profile_path: Path, output_root: Path) -> tuple[dict, list[str]]:
    output_root = require_working_directory(output_root)
    content = content_path.expanduser().resolve()
    profile = profile_path.expanduser().resolve()
    font_dir = ASSET_ROOT / "fonts"
    build_script = SCRIPT_ROOT / "build_cv.py"
    support = SCRIPT_ROOT / "cv_support.py"

    required_files = [
        content,
        profile,
        SKILL_ROOT / "templates" / "cv-profile.example.json",
        SKILL_ROOT / "templates" / "cv-content.example.json",
        REFERENCE_ROOT / "cv-layout.md",
        REFERENCE_ROOT / "export-and-qa.md",
        REFERENCE_ROOT / "font-usage.md",
        REFERENCE_ROOT / "source-of-truth.md",
        REFERENCE_ROOT / "cv-guidelines.md",
        REFERENCE_ROOT / "role-relevance.md",
        REFERENCE_ROOT / "ats-guidelines.md",
        build_script,
        support,
        SCRIPT_ROOT / "requirements.txt",
        font_dir / FONT_LICENSE,
        *(font_dir / name for name in REQUIRED_FONTS),
    ]
    missing = [str(path) for path in required_files if not path.is_file()]
    if missing:
        raise FileNotFoundError("Required standalone CV resources are missing:\n- " + "\n- ".join(missing))
    if content.parent != output_root.resolve() or profile.parent != output_root.resolve():
        raise ValueError("Keep cv-content.json and cv-profile.json in the working output folder for reproducible QA and delivery")
    existing_outputs = [output_root / name for name in ("CV.docx", "CV.pdf") if (output_root / name).exists()]
    if existing_outputs:
        raise FileExistsError("Refusing to overwrite existing CV output: " + ", ".join(path.name for path in existing_outputs))
    try:
        content_data = json.loads(content.read_text(encoding="utf-8"))
        profile_data = json.loads(profile.read_text(encoding="utf-8"))
        json.loads((SKILL_ROOT / "templates" / "cv-profile.example.json").read_text(encoding="utf-8"))
        json.loads((SKILL_ROOT / "templates" / "cv-content.example.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"Could not read valid UTF-8 JSON from a required CV file: {exc}") from exc
    if not isinstance(content_data, dict) or not isinstance(content_data.get("document"), dict):
        raise ValueError("cv-content.json must be an object containing a document object")
    profile_strings = list(iter_strings(profile_data))
    profile_placeholders = [value for value in profile_strings if re.search(r"\[[^\]]+\]", value)]
    profile_examples = ("candidate@example.com", "example.com", "20XX", "X/10", "tel:+12025550100")
    if profile_placeholders or any(marker in value for value in profile_strings for marker in profile_examples):
        raise ValueError("Replace all mock values in the candidate CV profile before PDF generation")
    content_strings = list(iter_strings(content_data))
    content_placeholders = [value for value in content_strings if re.search(r"\[[^\]]+\]", value)]
    content_dates = any(re.search(r"\b(?:MMM|20XX)\b", value) for value in content_strings)
    if content_placeholders or content_dates:
        raise ValueError("Replace all template placeholders in cv-content.json before PDF generation")

    office = shutil.which("soffice") or shutil.which("libreoffice")
    if not office:
        raise RuntimeError("LibreOffice/soffice is required for the CV PDF export")
    unavailable_modules = [name for name in REQUIRED_MODULES if importlib.util.find_spec(name) is None]
    if unavailable_modules:
        raise RuntimeError("Required Python modules are unavailable: " + ", ".join(unavailable_modules))

    report = {
        "ready": True,
        "content_file": content.name,
        "profile": profile.name,
        "profile_template": "templates/cv-profile.example.json",
        "content_template": "templates/cv-content.example.json",
        "layout_specification": "references/cv-layout.md",
        "export_and_qa_guide": "references/export-and-qa.md",
        "font_guide": "references/font-usage.md",
        "source_of_truth_guide": "references/source-of-truth.md",
        "cv_guidelines": "references/cv-guidelines.md",
        "role_relevance_guide": "references/role-relevance.md",
        "ats_guidelines": "references/ats-guidelines.md",
        "build_script": build_script.name,
        "support_module": support.name,
        "python_requirements": "scripts/requirements.txt",
        "font_files": list(REQUIRED_FONTS),
        "font_license": f"assets/fonts/{FONT_LICENSE}",
        "pdf_exporter_available": True,
        "python_modules": list(REQUIRED_MODULES),

    }
    return report, [str(build_script), str(profile)]


def main() -> int:
    args = build_parser().parse_args()
    content = args.content.expanduser().resolve()
    output_root = (args.output_root.expanduser().absolute() if args.output_root else args.content.expanduser().absolute().parent)
    try:
        report, build_args = preflight(content, args.profile, output_root)
    except (FileExistsError, FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"Preflight failed: {exc}", file=sys.stderr)
        return 2

    if args.preflight_only:
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0

    build_script, profile = build_args
    command = [
        sys.executable,
        build_script,
        str(content),
        "--profile",
        profile,
        "--output-root",
        str(output_root),
    ]
    print("Preflight passed; running the bundled build script.", flush=True)
    completed = subprocess.run(command, check=False)
    if completed.returncode:
        return completed.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
