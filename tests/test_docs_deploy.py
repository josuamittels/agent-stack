"""Deployment regressions using an in-memory destination; no network or credentials."""
import contextlib
import ftplib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "docs_deploy", ROOT / "src/skills/create-docs/scripts/deploy_docs.py"
)
deploy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(deploy)


class MemoryFTP:
    def __init__(self, files):
        self.files = files
        self.writes = []
        self._known_directories = set()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def retrbinary(self, command, callback):
        name = command.removeprefix("RETR ")
        if name not in self.files:
            raise ftplib.error_perm("550 Missing file")
        callback(self.files[name])

    def size(self, name):
        if name not in self.files:
            raise ftplib.error_perm("550 Missing file")
        return len(self.files[name])

    def voidcmd(self, command):
        return "200 OK"

    def mkd(self, name):
        return name

    def storbinary(self, command, source, blocksize):
        self.files[command.removeprefix("STOR ")] = source.read()

    def rename(self, source, destination):
        self.files[destination] = self.files.pop(source)
        self.writes.append(destination)


class DeploymentTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "index.html").write_text("new homepage")
        (self.root / "_pagefind").mkdir()
        (self.root / "_pagefind/pagefind.js").write_text("search asset")

    def test_profile_preserves_literal_password_characters(self):
        profile = self.root / "profile"
        profile.write_text("\n".join([
            "DOCS_DEPLOY_HOST=example.invalid", "DOCS_DEPLOY_USER=example",
            "DOCS_DEPLOY_PASSWORD='a$b#c'", "DOCS_DEPLOY_REMOTE_DIR=/",
            "DOCS_DEPLOY_URL=https://example.invalid", "DOCS_DEPLOY_SOURCE=docs/out",
            "DOCS_DEPLOY_SITE_ID=test",
        ]))
        self.assertEqual(deploy.read_profile(profile)["DOCS_DEPLOY_PASSWORD"], "a$b#c")

    def test_inventory_rejects_private_files_and_symlinks(self):
        secret = self.root / ".env.local"
        secret.write_text("private sample")
        with self.assertRaisesRegex(ValueError, "Nonpublic"):
            deploy.inventory(self.root)
        secret.unlink()
        (self.root / "linked").symlink_to(self.root / "index.html")
        with self.assertRaisesRegex(ValueError, "symlink"):
            deploy.inventory(self.root)

    def test_unmanaged_collision_stops_before_writes(self):
        ftp = MemoryFTP({"index.html": b"unrelated existing page"})
        with patch.object(deploy, "connect", return_value=ftp), contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaisesRegex(ValueError, "Unmanaged remote file collision"):
                deploy.publish({"DOCS_DEPLOY_SITE_ID": "test"}, self.root,
                               deploy.inventory(self.root), 1, set(), self.root / "backup")
        self.assertEqual(ftp.files["index.html"], b"unrelated existing page")
        self.assertEqual(ftp.writes, [])

    def test_named_adoption_backs_up_original_and_publishes_manifest_last(self):
        ftp = MemoryFTP({"index.html": b"inspected placeholder", "unrelated.txt": b"keep"})
        files = deploy.inventory(self.root)
        with patch.object(deploy, "connect", return_value=ftp), contextlib.redirect_stdout(io.StringIO()):
            deploy.publish({"DOCS_DEPLOY_SITE_ID": "test", "DOCS_DEPLOY_URL": "https://example.invalid"}, self.root,
                           files, 1, {"index.html"}, self.root / "backup")
        self.assertEqual((self.root / "backup/index.html").read_bytes(), b"inspected placeholder")
        self.assertEqual(ftp.files["unrelated.txt"], b"keep")
        self.assertEqual(ftp.files["index.html"], b"new homepage")
        self.assertLess(ftp.writes.index("_pagefind/pagefind.js"), ftp.writes.index("index.html"))
        self.assertEqual(ftp.writes[-1], deploy.MANIFEST)

    def test_live_verification_rejects_different_content(self):
        response = io.BytesIO(b"stale homepage")
        response.status = 200
        with patch.object(deploy.urllib.request, "urlopen", return_value=response):
            with self.assertRaisesRegex(ValueError, "Live content differs"):
                deploy.verify_public({"DOCS_DEPLOY_URL": "https://example.invalid"},
                                     self.root, deploy.inventory(self.root))


if __name__ == "__main__":
    unittest.main()
