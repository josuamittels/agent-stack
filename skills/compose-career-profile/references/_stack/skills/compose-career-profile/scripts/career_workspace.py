#!/usr/bin/env python3
"""Manage explicit career workspaces without accessing external personal systems."""
from __future__ import annotations
import argparse
from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import unicodedata


def require_working_directory(path):
    """Reject draft/QA writes in final application trees, including path aliases."""
    path = Path(path).expanduser()
    for candidate in (Path(os.path.abspath(path)), path.resolve()):
        for ancestor in (candidate, *candidate.parents):
            if ancestor.name.casefold() == "applications" or (ancestor / "job.md").is_file():
                raise ValueError(
                    "Drafts and QA must stay outside application folders. "
                    "Use the career workspace's work/ directory, a staple working folder, "
                    "or a temporary directory; deliver only the reviewed final PDF."
                )
    return path.resolve()


def digest(data):
    return hashlib.sha256(data).hexdigest()


def within(root, relative):
    root = root.resolve()
    candidate = root / relative
    if candidate.is_symlink() or any(p.is_symlink() for p in candidate.parents if p != root.parent):
        raise ValueError("Workspace paths must not use symlinks")
    resolved = candidate.resolve()
    if not resolved.is_relative_to(root):
        raise ValueError("Path escapes the selected workspace")
    return resolved


def atomic_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(data, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


@contextmanager
def locked(root):
    lock = within(root, "references/.career-lock")
    lock.mkdir()  # Fail immediately if another operation owns this workspace.
    try:
        yield
    finally:
        lock.rmdir()


def initialize(root, agents_template):
    root = Path(root).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    template = Path(agents_template).read_bytes()
    for name in ("applications", "references", "staples", "work"):
        within(root, name).mkdir(exist_ok=True)
    agents = within(root, "AGENTS.md")
    existed = agents.exists()
    if not existed:
        with agents.open("xb") as stream:
            stream.write(template)
    return {"project_root": str(root), "agents_preserved": existed}


def slug(text):
    value = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")[:70]
    return value or "unnamed"


def application(root, application_id, company, role, source=None):
    root = Path(root).expanduser().resolve()
    if not (root / "AGENTS.md").is_file():
        raise ValueError("Select an initialized career workspace")
    for name in ("applications", "references", "work"):
        if not within(root, name).is_dir():
            raise ValueError("Missing workspace directory: " + name)
    if not all(isinstance(x, str) and x.strip() for x in (application_id, company, role)):
        raise ValueError("Application id, company and role are required")
    source_text = Path(source).read_text(encoding="utf-8") if source else None
    if source_text is not None and not source_text.strip():
        raise ValueError("The full posting must not be empty")
    with locked(root):
        registry_path = within(root, "references/applications.json")
        registry = json.loads(registry_path.read_text()) if registry_path.exists() else {"schema_version": 1, "next_number": 1, "applications": {}}
        if not isinstance(registry, dict) or registry.get("schema_version") != 1 or not isinstance(registry.get("applications"), dict) or type(registry.get("next_number")) is not int or registry["next_number"] < 1:
            raise ValueError("Invalid application registry; preserve and repair it before allocating numbers")
        records = registry["applications"]
        item = records.get(application_id)
        if item is None:
            existing = [int(m.group(1)) for f in (root / "applications").iterdir() if (m := re.search(r"_(\d{3,})$", f.name))]
            number = max([registry["next_number"], *(n + 1 for n in existing)])
            folder = f"{slug(company)}_{slug(role)}_{number:03d}"
            item = {"folder": folder, "company": company, "role": role, "number": number}
            records[application_id] = item
            registry["next_number"] = number + 1
            # Reserve the number before creating files; failed attempts never recycle it.
            atomic_json(registry_path, registry)
        elif item.get("company") != company or item.get("role") != role:
            raise ValueError("Application id already belongs to a different company or role")
        if not isinstance(item, dict) or not isinstance(item.get("folder"), str) or not re.fullmatch(r".+_.+_\d{3,}", item["folder"]):
            raise ValueError("Invalid registered application folder")
        folder = within(root, "applications/" + item["folder"])
        folder.mkdir(exist_ok=True)
        work = within(root, "work/" + item["folder"])
        work.mkdir(exist_ok=True)
        job = within(root, "applications/" + item["folder"] + "/job.md")
        if source_text is not None:
            if job.exists():
                if job.read_text(encoding="utf-8") != source_text:
                    raise FileExistsError("Existing job.md differs; preserve it and obtain replacement approval")
            else:
                with job.open("x", encoding="utf-8", newline="\n") as stream:
                    stream.write(source_text)
        return {"application_folder": str(folder), "working_folder": str(work), "job_md_path": str(job), "applicable": source_text is not None, "source_text": source_text}


def deliver(source, destination, approved_sha256, validation):
    source, destination = Path(source).expanduser().resolve(), Path(destination).expanduser().absolute()
    if source.suffix.lower() != ".pdf" or destination.suffix.lower() != ".pdf":
        raise ValueError("Delivery requires PDF source and destination")
    data = source.read_bytes()
    if digest(data) != approved_sha256:
        raise ValueError("PDF changed since review; obtain approval of the current artifact")
    report = json.loads(Path(validation).read_text(encoding="utf-8"))
    if report.get("ok") is not True or report.get("pdf_sha256") != digest(data):
        raise ValueError("Missing or stale successful PDF validation")
    for key in ("content", "profile", "input"):
        if key + "_sha256" in report:
            name = report.get(key)
            if not isinstance(name, str) or Path(name).name != name:
                raise ValueError("Validation must identify a sibling " + key + " source")
            if digest((source.parent / name).read_bytes()) != report[key + "_sha256"]:
                raise ValueError("Source changed after PDF validation: " + key)
    destination.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with destination.open("xb") as stream:
            created = True
            stream.write(data)
    except Exception:
        if created:
            destination.unlink(missing_ok=True)
        raise
    return {"pdf": str(destination), "sha256": digest(data)}


def archive_result(record):
    """Check actual disk contents as well as supplied output; never infer a saved archive."""
    pointer = "/evidence/job_description_archive"
    item = record.get("evidence", {}).get("job_description_archive")
    def result(status, observed):
        return {"status": status, "step": "Application archive", "aspect": "job.md", "observed": observed,
                "expected": "actual numbered application job.md equals the complete source and supplied output", "evidence": [pointer, "/outputs/job_md"]}
    if not isinstance(item, dict):
        return result("unverified", "Missing archive evidence")
    if item.get("applicable") is False:
        return result("not_applicable", False)
    if item.get("applicable") is not True:
        return result("unverified", "Missing applicability")
    source, output = item.get("source_text"), record.get("outputs", {}).get("job_md")
    folder, path = item.get("application_folder"), item.get("job_md_path")
    if not all(isinstance(x, str) and x.strip() for x in (source, output, folder, path)):
        return result("unverified", "Missing source, output or path")
    folder, path = Path(folder), Path(path)
    if not folder.is_absolute() or not path.is_absolute() or folder.parent.name != "applications" or not re.fullmatch(r".+_.+_\d{3,}", folder.name) or path != folder / "job.md":
        return result("fail", "Incorrect archive path")
    try:
        saved = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        return result("unverified", str(exc))
    return result("pass" if saved == source == output else "fail", {"saved_matches_source": saved == source, "saved_matches_output": saved == output})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init")
    init.add_argument("--workspace", required=True, type=Path)
    init.add_argument("--agents-template", required=True, type=Path)
    app = commands.add_parser("application")
    app.add_argument("--workspace", required=True, type=Path)
    app.add_argument("--id", required=True)
    app.add_argument("--company", required=True)
    app.add_argument("--role", required=True)
    app.add_argument("--source", type=Path, help="Complete posting as canonical plain Markdown; never a role summary")
    copy = commands.add_parser("deliver")
    copy.add_argument("--source", type=Path, required=True)
    copy.add_argument("--destination", type=Path, required=True)
    copy.add_argument("--approved-sha256", required=True)
    copy.add_argument("--validation", required=True, type=Path, help="Current successful QA report bound to the reviewed sources")
    args = parser.parse_args()
    try:
        if args.command == "init":
            value = initialize(args.workspace, args.agents_template)
        elif args.command == "application":
            value = application(args.workspace, args.id, args.company, args.role, args.source)
        else:
            value = deliver(args.source, args.destination, args.approved_sha256, args.validation)
        print(json.dumps(value, ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        parser.exit(2, f"Error: {exc}\n")


if __name__ == "__main__":
    main()
