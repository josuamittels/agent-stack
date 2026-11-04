"""Shared offline I/O and Pandoc contracts for Research's deterministic helpers."""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

SKILL = Path(__file__).resolve().parents[1]
TEMPLATES = SKILL / "templates"
APA = SKILL / "references/csl/apa.csl"
FORMATS = {"chat", "md", "latex", "pdf", "docx"}


class ResearchError(Exception):
    def __init__(self, code, message, unavailable=False):
        super().__init__(message)
        self.code = code
        self.unavailable = unavailable


def require(condition, message, code="invalid_input"):
    if not condition:
        raise ResearchError(code, message)


def load(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ResearchError("invalid_json", f"Cannot read JSON {path}: {exc}") from exc


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def digest(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode("utf-8")).hexdigest()


def file_hash(path):
    return digest(Path(path).read_bytes())


def template(name):
    return load(TEMPLATES / name)


def inside(project, relative):
    require(isinstance(relative, str) and relative, "Project path must be a nonempty string")
    target = (Path(project) / relative).resolve()
    require(target.is_relative_to(Path(project).resolve()), f"Path escapes project: {relative}")
    return target


def publish(files, replace=False):
    """Stage all bytes before replacing outputs; refuse overwrite by default."""
    targets = {Path(path).resolve(): value for path, value in files.items()}
    require(len(targets) == len(files), "Output paths must be distinct")
    for path in targets:
        require(not path.exists() or replace, f"Output exists: {path}; use --replace", "output_exists")
        require(not path.is_dir(), f"Output is a directory: {path}")
    staged = []
    try:
        for path, value in targets.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            fd, name = tempfile.mkstemp(prefix=".research-", dir=path.parent)
            staged.append((Path(name), path))
            with os.fdopen(fd, "wb") as out:
                out.write(value if isinstance(value, bytes) else value.encode("utf-8"))
        for temporary, target in staged:
            os.replace(temporary, target)
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)
    return [str(p) for p in targets]


def binary(name, override=None):
    value = str(override) if override else shutil.which(name)
    if not value or not Path(value).is_file() or not os.access(value, os.X_OK):
        raise ResearchError("missing_dependency", f"Executable unavailable: {override or name}", True)
    return value


def run(argv, data=None, cwd=None, timeout=120):
    try:
        result = subprocess.run([str(v) for v in argv], input=data, cwd=cwd,
                                text=True, capture_output=True, timeout=timeout)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ResearchError("process_unavailable", f"{Path(argv[0]).name}: {exc}", True) from exc
    if result.returncode:
        raise ResearchError("conversion_failed", f"{Path(argv[0]).name}: {result.stderr.strip() or result.stdout.strip()}")
    return result


def pandoc(data, args=(), executable=None, cwd=None):
    return run([binary("pandoc", executable), "--fail-if-warnings", *args], data, cwd)


def parse_markdown(text, executable=None):
    return json.loads(pandoc(text, ["-f", "markdown+citations", "-t", "json"], executable).stdout)


def walk(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def citation_ids(ast):
    return list(dict.fromkeys(c["citationId"] for n in walk(ast) if n.get("t") == "Cite"
                              for c in n["c"][0]))


def plain_inlines(inlines):
    parts = []
    for node in inlines:
        kind, value = node.get("t"), node.get("c")
        if kind == "Str":
            parts.append(value)
        elif kind in {"Space", "SoftBreak", "LineBreak"}:
            parts.append(" ")
        elif kind in {"Emph", "Strong", "Strikeout", "SmallCaps", "Superscript", "Subscript"}:
            parts.append(plain_inlines(value))
        elif kind in {"Code", "Math"}:
            parts.append(value[-1])
        elif kind in {"Span", "Link", "Image"}:
            parts.append(plain_inlines(value[1]))
    return "".join(parts)


def headers(ast):
    return [plain_inlines(n["c"][2]) for n in ast["blocks"]
            if n.get("t") == "Header" and n["c"][0] == 2]


def reject_pending(ast):
    for node in walk(ast):
        if node.get("t") in {"Code", "CodeBlock"}:
            continue
        content = node.get("c")
        if node.get("t") == "Str":
            require("RESEARCH_PENDING" not in content and "SOURCE_NEEDED" not in content,
                    "Unresolved Research placeholder", "unfinished_document")
        if node.get("t") in {"RawBlock", "RawInline"}:
            require("RESEARCH_PENDING" not in content[-1], "Unfilled section template", "unfinished_document")


def check_document(ast, root):
    """Check portable constructs and resolve local assets before conversion."""
    reject_pending(ast)
    forbidden_meta = {"bibliography", "references", "csl", "nocite", "suppress-bibliography", "include-in-header",
                      "header-includes", "include-before", "include-after"}
    require(not (set(ast.get("meta", {})) & forbidden_meta),
            "Bibliography/style/includes must use explicit CLI inputs, not manuscript metadata")
    assets = []
    for node in walk(ast):
        require(node.get("t") not in {"RawBlock", "RawInline"},
                "Raw HTML/TeX is not portable; use Markdown tables, math and local images", "unsupported_content")
        if node.get("t") == "Image":
            target = node["c"][2][0]
            require(not target.startswith(("http:", "https:", "//", "data:", "file:")),
                    f"Use a local image asset instead of {target}", "unsupported_asset")
            from urllib.parse import unquote
            path = (Path(root) / unquote(target)).resolve()
            require(path.is_file(), f"Missing local image: {path}", "missing_asset")
            require(path.suffix.lower() in {".png", ".jpg", ".jpeg"},
                    f"Portable exports require PNG/JPEG assets: {path}", "unsupported_asset")
            assets.append(path)
    return list(dict.fromkeys(assets))
