"""Build and publish an authorized static documentation site over explicit FTPS.

Credentials stay in the local profile. Only exported files and a public hash
manifest are uploaded. No remote files are deleted; unrelated files are kept.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import ftplib
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import ssl
import subprocess
import sys
import time
import urllib.request
import uuid


MANIFEST = ".agent-stack-docs-manifest.json"


def read_profile(path):
    values = {}
    for line in path.read_text().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition("=")
        if not sep:
            raise ValueError("Invalid deployment profile line")
        # Literal values; no shell evaluation or environment substitution.
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key.strip()] = value
    for key in ("HOST", "USER", "PASSWORD", "REMOTE_DIR", "URL", "SOURCE", "SITE_ID"):
        if not values.get("DOCS_DEPLOY_" + key):
            raise ValueError("Missing DOCS_DEPLOY_" + key)
    if values.get("DOCS_DEPLOY_PROTOCOL", "ftps") != "ftps":
        raise ValueError("This publisher supports explicit FTPS; configure ftps on port 21")
    return values


class SessionFTP(ftplib.FTP_TLS):
    """Reuse the verified control TLS session for hosts that require it."""

    def ntransfercmd(self, cmd, rest=None):
        conn, size = ftplib.FTP.ntransfercmd(self, cmd, rest)
        if self._prot_p:
            conn = self.context.wrap_socket(
                conn, server_hostname=self.host, session=self.sock.session
            )
        return conn, size


def connect(profile):
    ftp = SessionFTP(context=ssl.create_default_context(), timeout=45)
    ftp.connect(profile["DOCS_DEPLOY_HOST"], int(profile.get("DOCS_DEPLOY_PORT") or 21))
    ftp.login(profile["DOCS_DEPLOY_USER"], profile["DOCS_DEPLOY_PASSWORD"])
    ftp.prot_p()
    ftp.cwd(profile["DOCS_DEPLOY_REMOTE_DIR"])
    ftp._known_directories = set()
    return ftp


def safe_name(name):
    path = PurePosixPath(name)
    return bool(name) and not path.is_absolute() and ".." not in path.parts and "\\" not in name


def inventory(root):
    if not (root / "index.html").is_file() or not (root / "_pagefind/pagefind.js").is_file():
        raise ValueError("Static export must contain index.html and the built Pagefind index")
    output = {}
    for file in sorted(root.rglob("*")):
        if file.is_symlink():
            raise ValueError("Export contains a symlink")
        if not file.is_file():
            continue
        relative = file.relative_to(root).as_posix()
        if any(part.startswith(".env") or part in {"node_modules", ".git"} for part in file.relative_to(root).parts):
            raise ValueError("Nonpublic file found in export")
        body = file.read_bytes()
        output[relative] = {"sha256": hashlib.sha256(body).hexdigest(), "size": len(body)}
    return output


def remote_manifest(ftp, site_id):
    buffer = io.BytesIO()
    try:
        ftp.retrbinary("RETR " + MANIFEST, buffer.write)
    except ftplib.error_perm as error:
        if not str(error).startswith("550"):
            raise
        return {"schema_version": 1, "site_id": site_id, "files": {}}
    data = json.loads(buffer.getvalue())
    if data.get("schema_version") != 1 or data.get("site_id") != site_id:
        raise ValueError("Remote manifest belongs to a different deployment profile")
    if not isinstance(data.get("files"), dict) or not all(safe_name(x) for x in data["files"]):
        raise ValueError("Invalid remote deployment manifest")
    return data


def ensure_parent(ftp, relative):
    current = ""
    for part in PurePosixPath(relative).parent.parts:
        if part == ".":
            continue
        current = part if not current else current + "/" + part
        if current in ftp._known_directories:
            continue
        try:
            ftp.mkd(current)
        except ftplib.error_perm as error:
            if not str(error).startswith("550"):
                raise
        ftp._known_directories.add(current)


def atomic_upload(ftp, relative, body):
    ensure_parent(ftp, relative)
    temporary = relative + ".upload-" + uuid.uuid4().hex
    ftp.storbinary("STOR " + temporary, io.BytesIO(body), blocksize=128 * 1024)
    if ftp.size(temporary) != len(body):
        raise ValueError("Uploaded size mismatch for " + relative)
    ftp.rename(temporary, relative)


def publish(profile, root, files, workers, adopt, backup):
    with connect(profile) as ftp:
        previous = remote_manifest(ftp, profile["DOCS_DEPLOY_SITE_ID"])
        changed = [name for name in files if previous["files"].get(name) != files[name]]
        # A missing manifest never grants permission to overwrite an unrelated file.
        print(json.dumps({"preflight": "checking destination", "changed_files": len(changed)}), flush=True)
        for number, name in enumerate(changed, 1):
            if number % 100 == 0:
                print(json.dumps({"preflight_checked": number, "changed_files": len(changed)}), flush=True)
            if name in previous["files"]:
                continue
            try:
                ftp.voidcmd("TYPE I")
                existing_size = ftp.size(name)
            except ftplib.error_perm as error:
                if not str(error).startswith("550"):
                    raise
                continue
            if existing_size is not None:
                existing = io.BytesIO()
                ftp.retrbinary("RETR " + name, existing.write)
                if hashlib.sha256(existing.getvalue()).hexdigest() == files[name]["sha256"]:
                    continue
                if name not in adopt:
                    raise ValueError("Unmanaged remote file collision: " + name)
                saved = backup / name
                saved.parent.mkdir(parents=True, exist_ok=True)
                saved.write_bytes(existing.getvalue())
    groups = [
        [x for x in changed if not x.endswith(".html")],
        [x for x in changed if x.endswith(".html") and x != "index.html"],
        [x for x in changed if x == "index.html"],
    ]

    def upload_group(names):
        batches = [names[n::workers] for n in range(workers)]

        def worker(batch):
            if not batch:
                return 0
            with connect(profile) as ftp:
                ftp.voidcmd("TYPE I")
                for number, name in enumerate(batch, 1):
                    atomic_upload(ftp, name, (root / name).read_bytes())
                    if number % 50 == 0:
                        print(json.dumps({"worker_uploaded": number, "worker_files": len(batch)}), flush=True)
            return len(batch)

        with ThreadPoolExecutor(max_workers=workers) as pool:
            return sum(result.result() for result in as_completed(pool.submit(worker, b) for b in batches))

    total = 0
    for names in groups:
        total += upload_group(names)
        print(json.dumps({"uploaded": total, "changed_files": len(changed)}), flush=True)
    new_manifest = {"schema_version": 1, "site_id": profile["DOCS_DEPLOY_SITE_ID"], "files": files}
    body = (json.dumps(new_manifest, sort_keys=True) + "\n").encode()
    with connect(profile) as ftp:
        ftp.voidcmd("TYPE I")
        atomic_upload(ftp, MANIFEST, body)
    return {
        "url": profile["DOCS_DEPLOY_URL"], "uploaded": total,
        "unchanged": len(files) - total, "files": len(files),
        "retained_obsolete_files": len(set(previous["files"]) - set(files)),
    }


def verify_public(profile, root, files):
    """Check representative live bytes; interactive search remains a browser check."""
    pages = sorted(name for name in files if name.endswith("/index.html") and "_not-found" not in name and not name.startswith("404/"))
    samples = ["index.html", *pages[:2], "_pagefind/pagefind.js", "sitemap.xml", "robots.txt"]
    assets = sorted(name for name in files if name.startswith("_next/") and name.endswith(".js"))
    if assets:
        samples.append(assets[0])
    verified = []
    for name in samples:
        relative = name[:-len("index.html")] if name.endswith("index.html") else name
        url = profile["DOCS_DEPLOY_URL"].rstrip("/") + "/" + relative
        request = urllib.request.Request(url, headers={"Cache-Control": "no-cache", "Accept-Encoding": "identity"})
        with urllib.request.urlopen(request, timeout=45, context=ssl.create_default_context()) as response:
            body = response.read()
            if response.status != 200 or hashlib.sha256(body).hexdigest() != files[name]["sha256"]:
                raise ValueError("Live content differs from export: " + relative)
        verified.append(relative or "/")
    return verified


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=Path.cwd())
    parser.add_argument("--env-file", type=Path, default=Path(__file__).resolve().parents[1] / ".env.local")
    parser.add_argument("--probe", action="store_true", help="Read connection and destination listing only")
    parser.add_argument("--plan", action="store_true", help="Build and inspect local output without uploading")
    parser.add_argument("--workers", type=int, choices=range(1, 5), default=3)
    parser.add_argument("--adopt-existing", nargs="*", default=[], help="Exact inspected initial files to back up locally and replace")
    args = parser.parse_args()
    profile = read_profile(args.env_file.resolve())
    if args.probe:
        with connect(profile) as ftp:
            print(json.dumps({"protocol": "explicit-ftps", "remote_directory": ftp.pwd(), "entries": ftp.nlst()}))
        return
    project = args.project_root.resolve()
    environment = dict(os.environ, DOCS_SITE_URL=profile["DOCS_DEPLOY_URL"])
    subprocess.run(["npm", "run", "build"], cwd=project / "docs", check=True, env=environment)
    root = (project / profile["DOCS_DEPLOY_SOURCE"]).resolve()
    if not root.is_relative_to(project / "docs"):
        raise ValueError("Publish source must be an export inside this project's docs directory")
    files = inventory(root)
    print(json.dumps({"exported_files": len(files), "bytes": sum(x["size"] for x in files.values())}), flush=True)
    if args.plan:
        return
    started = time.time()
    if not all(safe_name(name) for name in args.adopt_existing):
        raise ValueError("Adoption names must be relative exported file paths")
    backup = project / ".local/docs-deploy" / ("backup-" + uuid.uuid4().hex)
    result = publish(profile, root, files, args.workers, set(args.adopt_existing), backup)
    result["live_verified_paths"] = verify_public(profile, root, files)
    if backup.exists():
        result["initial_backup"] = str(backup)
    result["elapsed_seconds"] = round(time.time() - started, 1)
    state = project / ".local/docs-deploy"
    state.mkdir(parents=True, exist_ok=True)
    (state / "last-deployment.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        # Never echo profile values in a traceback or command log.
        message = str(error)
        try:
            for arg in (Path(__file__).resolve().parents[1] / ".env.local",):
                if arg.exists():
                    message = message.replace(read_profile(arg)["DOCS_DEPLOY_PASSWORD"], "[redacted]")
        except Exception:
            pass
        print("Documentation deployment failed: " + message, file=sys.stderr)
        sys.exit(1)
