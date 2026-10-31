"""Standalone offline I/O for literature qualification helpers."""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
import tempfile

SKILL = Path(__file__).resolve().parents[1]


class LiteratureError(ValueError):
    def __init__(self, code, message):
        super().__init__(message)
        self.code = code


def require(condition, message, code="invalid_input"):
    if not condition:
        raise LiteratureError(code, message)


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"


def digest(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode("utf-8")).hexdigest()


def file_hash(path):
    return digest(Path(path).read_bytes())


def load(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise LiteratureError("invalid_json", f"Cannot read JSON {path}: {exc}") from exc


def publish(files, replace=False, protected=()):
    targets = {Path(p).resolve(): value for p, value in files.items()}
    require(len(targets) == len(files), "Output paths must be distinct")
    protected = {Path(p).resolve() for p in protected}
    for path in targets:
        require(path not in protected, "Output would overwrite a source input")
        require(not path.exists() or replace, f"Output exists: {path}; use --replace", "output_exists")
        require(not path.is_dir(), f"Output is a directory: {path}")
    staged = []
    try:
        for path, value in targets.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            fd, name = tempfile.mkstemp(prefix=".literature-", dir=path.parent)
            staged.append((Path(name), path))
            with os.fdopen(fd, "wb") as out:
                out.write(value if isinstance(value, bytes) else value.encode("utf-8"))
        for temporary, target in staged:
            os.replace(temporary, target)
    finally:
        for temporary, _ in staged:
            temporary.unlink(missing_ok=True)
    return [str(p) for p in targets]
