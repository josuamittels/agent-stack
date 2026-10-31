"""Helper regression tests, not Research-skill invocations or research-quality evaluations."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest

import research
from research_common import dump, file_hash, load
from research_project import REVIEW_CHECKS, review_inputs
from research_render import citation_key, docx_signature
from test_source_gate import refresh_project_gate


class HelperTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="research-helper-test-")
        self.addCleanup(self.tmp.cleanup)
        self.project = Path(self.tmp.name) / "project"
        self.call("init", "--project", self.project, "--topic", "Converter fixture: café and α")

    def call(self, *argv, expected=0):
        output = io.StringIO()
        with redirect_stdout(output):
            code = research.main([str(v) for v in argv])
        result = json.loads(output.getvalue())
        self.assertEqual(code, expected, result)
        return result

    def save(self, name, data):
        (self.project / name).write_text(dump(data), encoding="utf-8")

    def ready(self):
        brief = load(self.project / "brief.json")
        brief.update(status="complete", scope="Only a converter test, not a research report.",
                     audience="Helper test", method="Inspect fixture artifacts.")
        brief["outside_check"]["observed"] = "Compared conversion fixture objects."
        self.save("brief.json", brief)
        source = {"source_id": "fixture-book", "title": "A Conversion Fixture", "publication_type": "book",
                  "authors": ["Åse Example"], "year": 2020, "provenance": [{"provider": "test fixture", "record_url": "fixture:book"}]}
        other = {**source, "source_id": "uncited-fixture", "title": "Uncited Conversion Fixture"}
        self.save("sources.json", {"schema_version": 1, "search_receipt": {"status": "complete", "searches": [], "limits": ["test data only"]}, "sources": [source, other]})
        refresh_project_gate(self.project)
        self.save("appraisals.json", {"schema_version": 1, "status": "complete", "appraisals": [{"source_id": "fixture-book", "inspection": "abstract", "limitations": ["test only"], "findings": [{"finding_id": "f1", "text": "Fixture finding", "locator": "fixture abstract"}]}]})
        self.save("claims.json", {"schema_version": 1, "status": "complete", "claims": [{"claim_id": "c1", "text": "Fixture claim", "status": "qualified", "supports": [{"source_id": "fixture-book", "finding_id": "f1"}], "contradicts": [], "qualification": "Converter test only"}]})
        outline = load(self.project / "outline.json")
        outline["status"] = "complete"
        for section in outline["sections"]:
            section.update(source_ids=["fixture-book"], claim_ids=["c1"], word_budget={"min": 0, "max": 200}, context="Independent converter-fixture section")
            if section["id"] != "references":
                (self.project / section["path"]).write_text(
                    f"## {section['heading']}\n\nUnicode café and α remain intact [@{citation_key('fixture-book')}, p. 3].\n", encoding="utf-8")
        self.save("outline.json", outline)

    def assembled(self):
        self.ready()
        self.call("assemble", "--project", self.project)

    def reviews(self):
        for kind, checks in REVIEW_CHECKS.items():
            review = load(self.project / f"{kind}-review.json")
            review.update(status="complete", draft_sha256=file_hash(self.project / "draft.md"), inputs_sha256=review_inputs(self.project), checks={k: {"status": "checked", "evidence": ["Converter fixture only"]} for k in checks})
            self.save(f"{kind}-review.json", review)

    def test_init_pending_resume_and_no_overwrite(self):
        self.assertEqual(load(self.project / "argument-review.json")["status"], "pending")
        self.assertFalse((self.project / "report.md").exists())
        self.assertEqual(load(self.project / "brief.json")["constraints"]["requested_formats"]["source"], "skill_default")
        self.call("init", "--project", self.project, "--topic", "Converter fixture: café and α", expected=1)
        before = file_hash(self.project / "brief.json")
        self.call("init", "--project", self.project, "--topic", "Converter fixture: café and α", "--resume")
        self.assertEqual(before, file_hash(self.project / "brief.json"))
        self.call("validate", "--project", self.project, "--phase", "brief", expected=1)

    def test_depth_names_bounds_and_independent_journal_default(self):
        brief = load(self.project / "brief.json")
        self.assertEqual(brief["depth"], "normal")
        self.assertEqual(brief["constraints"]["source_count_min"]["value"], 16)
        self.assertEqual(brief["constraints"]["source_count_max"]["value"], 24)
        for depth, bounds in {"quick": (800, 1600, 8, 12), "normal": (2000, 4000, 16, 24), "deep": (6000, None, 32, 64)}.items():
            target = Path(self.tmp.name) / ("depth-" + depth)
            self.call("init", "--project", target, "--topic", "Depth fixture", "--depth", depth)
            current = load(target / "brief.json")
            self.assertEqual(current["depth"], depth)
            self.assertEqual(tuple(current["constraints"][key]["value"] for key in
                                   ["word_count_min", "word_count_max", "source_count_min", "source_count_max"]), bounds)
            self.assertEqual(current["constraints"]["journal_preset"], {"value": "default", "source": "skill_default"})
            self.assertEqual(current["constraints"]["journal_article_influence_min"]["value"], 2.5)
            self.assertEqual(current["constraints"]["journal_influence_percentile_min"]["value"], 80)
        for legacy in ["light", "default", "thorough"]:
            self.call("init", "--project", Path(self.tmp.name) / legacy,
                      "--topic", "Depth fixture", "--depth", legacy, expected=1)

    def test_optional_requested_sources_are_preserved_and_accounted(self):
        target = Path(self.tmp.name) / "seeded"
        self.call("init", "--project", target, "--topic", "Fixture",
                  "--source", "10.1234/éxample", "--source", "A supplied citation",
                  "--author", "Åse Example (ORCID supplied)")
        requests = load(target / "brief.json")["source_requests"]
        self.assertEqual([r["kind"] for r in requests], ["work", "work", "author"])
        self.assertEqual(requests[0]["input"], "10.1234/éxample")
        self.call("init", "--project", target, "--topic", "Fixture", "--resume",
                  "--source", "different work", expected=1)
        self.ready()
        brief = load(self.project / "brief.json")
        brief["source_requests"] = requests
        self.save("brief.json", brief)
        self.call("validate", "--project", self.project, "--phase", "discovery", expected=1)
        sources = load(self.project / "sources.json")
        outcomes = [{"request_id": r["request_id"], "status": "unresolved",
                     "searches": ["Fixture lookup: blocked, test only"],
                     "source_ids": [], "reason": "Test fixture has no real lookup"} for r in requests]
        sources["search_receipt"]["requested_inputs"] = outcomes
        self.save("sources.json", sources)
        refresh_project_gate(self.project)
        self.call("validate", "--project", self.project, "--phase", "discovery")
        outcomes[0].update(status="eligible", source_ids=[])
        self.save("sources.json", sources)
        self.call("validate", "--project", self.project, "--phase", "discovery", expected=1)
        outcomes[0]["source_ids"] = ["fixture-book"]
        self.save("sources.json", sources)
        refresh_project_gate(self.project)
        self.call("validate", "--project", self.project, "--phase", "discovery")
        outcomes.append(outcomes[0])
        self.save("sources.json", sources)
        self.call("validate", "--project", self.project, "--phase", "discovery", expected=1)

    def test_literature_review_has_prescribed_extra_sections(self):
        target = Path(self.tmp.name) / "review"
        self.call("init", "--project", target, "--topic", "Fixture", "--type", "literature-review")
        names = [r["heading"] for r in load(target / "outline.json")["sections"]]
        self.assertEqual(len(names), 9)
        self.assertIn("Evidence overview", names)
        self.assertIn("Disagreements and evidence gaps", names)
        target2 = Path(self.tmp.name) / "explicit-chat"
        self.call("init", "--project", target2, "--topic", "Fixture", "--formats", "chat")
        self.assertEqual(load(target2 / "brief.json")["constraints"]["requested_formats"]["source"], "request")

    def test_manifest_order_missing_and_duplicate_sections(self):
        self.ready()
        manifest = load(self.project / "manifest.json")
        manifest["sections"].reverse()
        self.save("manifest.json", manifest)
        self.call("assemble", "--project", self.project, expected=1)
        manifest["sections"].reverse()
        self.save("manifest.json", manifest)
        target = self.project / manifest["sections"][0]["path"]
        target.unlink()
        self.call("assemble", "--project", self.project, expected=1)
        self.ready()
        manifest["sections"][1] = manifest["sections"][0]
        self.save("manifest.json", manifest)
        self.call("assemble", "--project", self.project, expected=1)

    def test_duplicates_and_unknown_evidence_ids(self):
        self.ready()
        inv = load(self.project / "sources.json")
        inv["sources"].append(inv["sources"][0])
        self.save("sources.json", inv)
        self.call("citations", "--project", self.project, "--prepare", expected=1)
        self.ready()
        claims = load(self.project / "claims.json")
        claims["claims"][0]["supports"][0]["finding_id"] = "absent"
        self.save("claims.json", claims)
        self.call("validate", "--project", self.project, "--phase", "evidence", expected=1)

    @unittest.skipUnless(shutil.which("pandoc"), "Pandoc required")
    def test_doi_less_citations_locators_and_uncited_exclusion(self):
        self.assembled()
        self.call("citations", "--project", self.project, "--prepare")
        result = self.call("citations", "--project", self.project, "--replace")
        self.assertEqual(result["cited_source_ids"], ["fixture-book"])
        report = (self.project / "report.md").read_text()
        self.assertIn("Åse Example", report)
        self.assertIn("p. 3", report)
        self.assertNotIn("Uncited Conversion Fixture", report)
        self.assertNotIn("[@", report)
        self.assertIn("café", report)
        before = file_hash(self.project / "report.md")
        self.call("citations", "--project", self.project, expected=1)
        self.assertEqual(before, file_hash(self.project / "report.md"))
        self.call("citations", "--project", self.project, "--replace")
        self.assertEqual(before, file_hash(self.project / "report.md"))

    @unittest.skipUnless(shutil.which("pandoc"), "Pandoc required")
    def test_unknown_citations_and_pending_placeholders_preserve_outputs(self):
        self.assembled()
        draft = self.project / "draft.md"
        draft.write_text(draft.read_text() + "\nUnknown [@MISSING].\n")
        self.call("citations", "--project", self.project, expected=1)
        self.assertFalse((self.project / "report.md").exists())
        self.ready()
        path = self.project / load(self.project / "outline.json")["sections"][0]["path"]
        path.write_text(path.read_text() + "\n<!-- RESEARCH_PENDING -->\n")
        self.call("assemble", "--project", self.project, "--replace", expected=1)

    @unittest.skipUnless(shutil.which("pandoc"), "Pandoc required")
    def test_review_hash_and_repair_limit(self):
        self.assembled()
        self.reviews()
        self.call("validate", "--project", self.project, "--phase", "review")
        draft = self.project / "draft.md"
        draft.write_text(draft.read_text() + "\nA later edit.\n")
        self.call("validate", "--project", self.project, "--phase", "review", expected=1)
        self.reviews()
        review = load(self.project / "argument-review.json")
        review["repair_passes"] = 3
        self.save("argument-review.json", review)
        self.call("validate", "--project", self.project, "--phase", "review", expected=1)

    @unittest.skipUnless(shutil.which("pandoc"), "Pandoc required")
    def test_citation_group_and_narrative(self):
        self.assembled()
        draft = self.project / "draft.md"
        draft.write_text(draft.read_text() + f"\n@{citation_key('fixture-book')} and others [@{citation_key('uncited-fixture')}, pp. 4-5].\n")
        result = self.call("citations", "--project", self.project)
        self.assertEqual(len(result["cited_keys"]), 2)
        self.assertIn("4", (self.project / "report.md").read_text())

    @unittest.skipUnless(shutil.which("pandoc"), "Pandoc required")
    def test_portable_exports_math_tables_assets_and_failures(self):
        # This tests converters, not an invented Research invocation.
        import base64
        image = Path(self.tmp.name) / "asset.png"
        image.write_bytes(base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+jRZkAAAAASUVORK5CYII="))
        source = Path(self.tmp.name) / "input.md"
        source.write_text("# Converter fixture\n\nUnicode café and α.\n\n$$E=mc^2$$\n\n| A | B |\n|---|---|\n| one | two |\n\n![Local fixture](asset.png)\n", encoding="utf-8")
        for fmt, suffix in [("md", "md"), ("latex", "tex"), ("docx", "docx")]:
            target = Path(self.tmp.name) / "exports" / ("report." + suffix)
            self.call("export", "--input", source, "--format", fmt, "--output", target)
            self.assertTrue(target.is_file())
            self.call("export", "--input", source, "--format", fmt, "--output", target, expected=1)
        signature = docx_signature(Path(self.tmp.name) / "exports/report.docx")
        self.assertEqual(signature["tables"], 1)
        self.assertEqual(signature["math"], 1)
        source.write_text("# Fixture\n\n![remote](https://example.com/image.png)\n")
        self.call("export", "--input", source, "--format", "docx", "--output", Path(self.tmp.name) / "blocked.docx", expected=1)
        source.write_text("# Fixture\n\n<img src='asset.png'>\n")
        self.call("export", "--input", source, "--format", "latex", "--output", Path(self.tmp.name) / "blocked.tex", expected=1)
        source.write_text("# Fixture\n\n![missing](absent.png)\n")
        self.call("export", "--input", source, "--format", "docx", "--output", Path(self.tmp.name) / "blocked.docx", expected=1)

    def test_missing_dependencies_and_bad_arguments_are_json(self):
        self.call("doctor", "--pandoc", "/no/such/executable", expected=2)
        self.call("export", "--format", "invalid", expected=1)

    @unittest.skipUnless(shutil.which("pandoc"), "Pandoc required")
    def test_final_requires_current_citations_and_reviewed_exports(self):
        self.assembled()
        brief = load(self.project / "brief.json")
        brief["formats"] = ["docx"]
        brief["constraints"]["requested_formats"] = {"value": ["docx"], "source": "request"}
        self.save("brief.json", brief)
        self.reviews()
        self.call("citations", "--project", self.project)
        self.call("export", "--project", self.project, "--input", self.project / "report.md", "--format", "md", "--output", self.project / "draft.md", "--replace", expected=1)
        self.call("validate", "--project", self.project, "--phase", "final", expected=1)
        self.call("export", "--project", self.project, "--input", self.project / "report.md", "--format", "docx", "--output", self.project / "output/report.docx")
        self.call("validate", "--project", self.project, "--phase", "final", expected=1)
        register = load(self.project / "exports.json")
        register["exports"][0].update(visual_review="complete", visual_review_evidence=["Unit fixture annotation; no research-quality claim"])
        self.save("exports.json", register)
        self.call("validate", "--project", self.project, "--phase", "final")
        report = self.project / "report.md"
        report.write_text(report.read_text() + "\nA later change.\n")
        self.call("validate", "--project", self.project, "--phase", "final", expected=1)

    @unittest.skipUnless(shutil.which("pandoc"), "Pandoc required")
    def test_changed_appraisal_invalidates_review(self):
        self.assembled()
        self.reviews()
        data = load(self.project / "appraisals.json")
        data["appraisals"][0]["notes"] = "Newly discovered context"
        self.save("appraisals.json", data)
        self.call("validate", "--project", self.project, "--phase", "review", expected=1)


if __name__ == "__main__":
    unittest.main()
