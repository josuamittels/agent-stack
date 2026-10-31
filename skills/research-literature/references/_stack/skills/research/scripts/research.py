#!/usr/bin/env python3
"""Deterministic Research project, citation and export CLI. No network/model calls."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import sys

from research_common import ResearchError, require
from research_project import DEPTHS, PRESETS, assemble_project, init_project, validate_project
from research_render import compile_project, export_document
from research_references import rank_references


class Parser(argparse.ArgumentParser):
    def error(self, message):
        raise ResearchError("invalid_arguments", message)


def parser():
    root = Parser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True, parser_class=Parser)
    init = commands.add_parser("init", help="Create the standard project without invented research")
    init.add_argument("--project", type=Path, required=True)
    init.add_argument("--topic", required=True)
    init.add_argument("--request", help="Original user request; defaults to the topic")
    init.add_argument("--type", choices=["research-report", "literature-review"], default="research-report")
    init.add_argument("--depth", choices=DEPTHS, default="normal")
    init.add_argument("--language", default="en")
    init.add_argument("--formats", help="Comma-separated chat,md,latex,pdf,docx; defaults to chat")
    init.add_argument("--style", default="apa", help="apa or an explicit local CSL path")
    init.add_argument("--source", action="append", default=[], help="Optional paper citation, title, identifier or URL; repeat for each work")
    init.add_argument("--author", action="append", default=[], help="Optional author name/ORCID with identifying context; repeat for each author")
    init.add_argument("--journal-preset", choices=PRESETS)
    init.add_argument("--resume", action="store_true", help="Check existing files without rewriting them")
    ranking = commands.add_parser("rank-references", help="Rank frozen initial-pool backward references; deep only")
    ranking.add_argument("--project", type=Path, required=True)
    ranking.add_argument("--inventory", type=Path, help="Qualified anchor inventory instead of sources.json")
    validation = commands.add_parser("validate", help="Check a completed phase's artifact requirements")
    validation.add_argument("--project", type=Path, required=True)
    validation.add_argument("--phase", choices=["brief", "discovery", "evidence", "outline", "draft", "review", "final"], required=True)
    assembly = commands.add_parser("assemble", help="Assemble exactly the prescribed sections")
    assembly.add_argument("--project", type=Path, required=True)
    citations = commands.add_parser("citations", help="Prepare citation keys or compile the final references")
    citations.add_argument("--project", type=Path, required=True)
    citations.add_argument("--prepare", action="store_true", help="Build keys and CSL data before drafting")
    citations.add_argument("--style", help="Override the brief's style with a local CSL path or apa")
    export = commands.add_parser("export", help="Convert Markdown without model calls")
    export.add_argument("--input", type=Path, required=True)
    export.add_argument("--format", choices=["md", "latex", "pdf", "docx"], required=True)
    export.add_argument("--output", type=Path, required=True)
    export.add_argument("--project", type=Path, help="Register an export of this project's report.md")
    export.add_argument("--bibliography", type=Path, help="Local CSL JSON array for unrendered citation keys")
    export.add_argument("--style", help="Local CSL path or apa")
    export.add_argument("--reference-doc", type=Path, help="Optional local Word styling document")
    export.add_argument("--soffice", help="Explicit host-resolved bundled LibreOffice executable for PDF")
    doctor = commands.add_parser("doctor", help="Read-only dependency checks")
    doctor.add_argument("--formats", default="chat")
    doctor.add_argument("--soffice", help="Explicit host-resolved bundled LibreOffice executable")
    for sub in [validation, assembly, citations, export, doctor]:
        sub.add_argument("--pandoc", help="Explicit executable instead of PATH resolution")
    for sub in [assembly, citations, export, ranking]:
        sub.add_argument("--replace", action="store_true", help="Explicitly replace generated outputs, never source input")
    return root


def doctor(args):
    from research_common import binary, run
    formats = set(args.formats.split(","))
    require(formats and formats <= {"chat", "md", "latex", "pdf", "docx"}, "Invalid requested formats")
    results = {}
    missing = []
    for name, override in [("pandoc", args.pandoc), *([("soffice", args.soffice)] if "pdf" in formats else [])]:
        if name == "soffice" and not override:
            results[name] = {"available": False, "reason": "Pass the host-resolved bundled path with --soffice"}
            missing.append(name)
            continue
        try:
            path = binary(name, override)
            results[name] = {"available": True, "path": path, "version": run([path, "--version"]).stdout.splitlines()[0]}
        except ResearchError as exc:
            results[name] = {"available": False, "reason": str(exc)}
            missing.append(name)
    if missing:
        return {"status": "unavailable", "dependencies": results, "missing": missing, "outputs": []}
    return {"dependencies": results, "outputs": []}


def main(argv=None):
    try:
        args = parser().parse_args(argv)
        if args.command == "init":
            result = init_project(args)
        elif args.command == "rank-references":
            result = rank_references(args)
        elif args.command == "validate":
            result = validate_project(args.project, args.phase, args.pandoc)
        elif args.command == "assemble":
            result = assemble_project(args)
        elif args.command == "citations":
            result = compile_project(args)
        elif args.command == "export":
            result = export_document(args)
        else:
            result = doctor(args)
        result = {"schema_version": 1, "status": "ok", "command": args.command, **result}
        print(json.dumps(result, ensure_ascii=False, allow_nan=False))
        return 2 if result["status"] == "unavailable" else 0
    except (ResearchError, OSError, ValueError, TypeError, KeyError) as exc:
        unavailable = isinstance(exc, ResearchError) and exc.unavailable
        print(json.dumps({"schema_version": 1, "status": "unavailable" if unavailable else "error",
                          "error": {"code": getattr(exc, "code", "invalid_input"), "message": str(exc)},
                          "outputs": []}, ensure_ascii=False))
        return 2 if unavailable else 1


if __name__ == "__main__":
    sys.exit(main())
