"""Offline helper/checker fixtures, not authored Research invocation evaluations."""
from copy import deepcopy
from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

import research
from test_source_gate import refresh_project_gate
from research_common import ResearchError, dump, load
from research_references import graph, validate_expansion

EVIDENCE = [{"provider": "fixture", "record_url": "fixture:references", "retrieved_at": "2026-10-31"}]


def ref(doi=None, **extra):
    return {"identity_status": "resolved", "identifiers": {"doi": doi} if doi else {},
            "identity_evidence": deepcopy(EVIDENCE), **extra}


def source(sid, refs, **extra):
    return {"source_id": sid, "title": "Fixture " + sid, "publication_type": "journal_article",
            "doi": "10.1234/" + sid, "discovery_level": "initial", "provenance": deepcopy(EVIDENCE),
            "journal_title": "Nature", "issns": ["0028-0836"],
            "reference_list": {"status": "complete", "retrievals": deepcopy(EVIDENCE), "references": refs, "limits": []}, **extra}


class ReferenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="reference-helper-")
        self.addCleanup(self.tmp.cleanup)
        self.project = Path(self.tmp.name) / "project"
        self.call("init", "--project", self.project, "--topic", "Reference ranking fixture", "--depth", "deep")
        self.brief = load(self.project / "brief.json")
        self.sources = [source("a", [ref("10.1234/overlap"), ref("10.1234/single")]),
                        source("b", [ref("https://doi.org/10.1234/OVERLAP")])]

    def call(self, *args, expected=0):
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            code = research.main([str(a) for a in args])
        result = json.loads(stdout.getvalue())
        self.assertEqual(code, expected, result)
        return result

    def save(self, name, value):
        (self.project / name).write_text(dump(value), encoding="utf-8")

    def screened(self):
        artifact = graph(self.sources)
        artifact["status"] = "complete"
        for item in artifact["candidates"]:
            if not item["existing_source_ids"]:
                item["disposition"] = {"status": "excluded", "source_id": None, "reason": "Outside fixture question"}
        return artifact

    def addition(self, artifact, candidate=0, exempt=True):
        item = artifact["candidates"][candidate]
        added = {"source_id": "added", "doi": item["candidate_id"][4:], "title": "Fixture addition",
                 "publication_type": "journal_article", "journal_title": "Unmatched fixture journal", "issns": [],
                 "discovery_level": "secondary", "provenance": deepcopy(EVIDENCE),
                 "secondary_discovery": {"candidate_id": item["candidate_id"], "citing_source_ids": item["citing_source_ids"],
                     "overlap_count": item["overlap_count"], "journal_filter": "overlap_exempt" if exempt else "ordinary",
                     "relevance_reason": "Fixture topic match", "other_criteria_evidence": "Fixture constraints screened"}}
        item["disposition"] = {"status": "included", "source_id": "added", "reason": "Relevant fixture"}
        self.sources.append(added)
        return added

    def test_rank_normalizes_doi_and_deduplicates_edges(self):
        self.sources[0]["reference_list"]["references"].append(ref("doi:10.1234/OVERLAP"))
        artifact = graph(self.sources)
        self.assertEqual([c["overlap_count"] for c in artifact["candidates"]], [2, 1])
        self.assertEqual(len(artifact["candidates"][0]["edges"]), 3)
        self.assertEqual(artifact, graph(list(reversed(self.sources))))

    def test_doi_less_crosswalk_and_confirmed_versions(self):
        self.sources[0]["reference_list"]["references"] = [ref(identifiers={"pmid": "123"})]
        self.sources[1]["reference_list"]["references"] = [ref(identifiers={"openalex": "W123", "pmid": "123"})]
        candidate = graph(self.sources)["candidates"][0]
        self.assertEqual(candidate["overlap_count"], 2)
        for s in self.sources:
            s.update(canonical_id="work:same-confirmed-work", identity_evidence=deepcopy(EVIDENCE))
        candidate = graph(self.sources)["candidates"][0]
        self.assertEqual(candidate["overlap_count"], 1)
        self.assertEqual(candidate["citing_source_ids"], ["a"])

    def test_stable_ties_unresolved_and_missing_coverage(self):
        self.sources[0]["reference_list"]["references"] = [ref("10.1234/z"), ref("10.1234/a"), {"identity_status": "unresolved", "raw_citation": "Unknown reference"}]
        self.sources[1]["reference_list"].update(status="partial", limits=["Only page one available"], references=[])
        artifact = self.screened()
        self.assertEqual([c["candidate_id"] for c in artifact["candidates"]], ["doi:10.1234/a", "doi:10.1234/z"])
        with self.assertRaises(ResearchError):
            validate_expansion(self.brief, self.sources, artifact)
        artifact.update(status="partial", limits=["Incomplete coverage; unresolved citation"])
        validate_expansion(self.brief, self.sources, artifact)
        self.sources[1]["reference_list"]["status"] = "pending"
        with self.assertRaises(ResearchError):
            graph(self.sources)

    def test_existing_sources_stay_initial(self):
        self.sources[0]["reference_list"]["references"].append(ref("10.1234/b"))
        artifact = self.screened()
        existing = next(c for c in artifact["candidates"] if c["existing_source_ids"])
        existing["disposition"] = {"status": "already_initial", "source_id": None, "reason": None}
        self.assertEqual(existing["existing_source_ids"], ["b"])
        validate_expansion(self.brief, self.sources, artifact)

    def test_overlap_exception_and_one_hop_only(self):
        artifact = self.screened()
        added = self.addition(artifact)
        added["reference_list"] = {"status": "complete", "retrievals": deepcopy(EVIDENCE), "references": [ref("10.1234/recursive")], "limits": []}
        self.assertEqual(set(validate_expansion(self.brief, self.sources, artifact)), {"added"})
        self.assertFalse(any(c["candidate_id"].endswith("recursive") for c in graph(self.sources)["candidates"]))
        added["secondary_discovery"]["other_criteria_evidence"] = ""
        with self.assertRaises(ResearchError):
            validate_expansion(self.brief, self.sources, artifact)

    def test_singleton_cannot_bypass_journal_rule(self):
        artifact = self.screened()
        added = self.addition(artifact, candidate=1)
        with self.assertRaises(ResearchError):
            validate_expansion(self.brief, self.sources, artifact)
        added["secondary_discovery"]["journal_filter"] = "ordinary"
        with self.assertRaises(ResearchError):
            validate_expansion(self.brief, self.sources, artifact)
        added["publication_type"] = "book"
        validate_expansion(self.brief, self.sources, artifact)

    def test_ordinary_journal_csv_and_explicit_exceptions(self):
        artifact = self.screened()
        added = self.addition(artifact, candidate=1, exempt=False)
        added.update(journal_title="Nature", issns=["0028-0836"])
        validate_expansion(self.brief, self.sources, artifact)
        added.update(journal_title="Unmatched fixture journal", issns=[])
        self.brief["constraints"]["journal_exceptions"] = {"value": ["added"], "source": "request"}
        validate_expansion(self.brief, self.sources, artifact)

    def test_initial_anchors_keep_the_ordinary_journal_filter(self):
        artifact = self.screened()
        self.addition(artifact)
        self.sources[0].update(journal_title="Unmatched fixture journal", issns=[])
        with self.assertRaises(ResearchError):
            validate_expansion(self.brief, self.sources, artifact)

    def test_depth_gate_and_forged_graph(self):
        artifact = self.screened()
        self.addition(artifact)
        for depth in ("quick", "normal"):
            self.brief["depth"] = depth
            with self.assertRaises(ResearchError):
                validate_expansion(self.brief, self.sources, artifact)
        self.brief["depth"] = "deep"
        artifact["candidates"][0]["overlap_count"] = 3
        with self.assertRaises(ResearchError):
            validate_expansion(self.brief, self.sources, artifact)

    def test_ranking_overwrite_freeze_and_no_dependency(self):
        self.save("sources.json", {"sources": self.sources})
        self.call("rank-references", "--project", self.project)
        self.call("rank-references", "--project", self.project, expected=1)
        self.call("rank-references", "--project", self.project, "--replace")
        self.sources.append(source("new-seed", []))
        self.save("sources.json", {"sources": self.sources})
        self.call("rank-references", "--project", self.project, "--replace", expected=1)
        self.brief["depth"] = "normal"
        self.save("brief.json", self.brief)
        self.call("rank-references", "--project", self.project, expected=1)

    def test_uninspected_candidates_and_stale_input(self):
        artifact = self.screened()
        artifact["candidates"][0]["disposition"].update(status="not_inspected", reason="Resource limit")
        artifact.update(status="partial", limits=["Resource limit"])
        with self.assertRaises(ResearchError):
            validate_expansion(self.brief, self.sources, artifact)
        artifact["candidates"][1]["disposition"].update(status="not_inspected", reason="Resource limit")
        validate_expansion(self.brief, self.sources, artifact)
        self.sources[0]["reference_list"]["references"].append(ref("10.1234/new-reference"))
        with self.assertRaises(ResearchError):
            validate_expansion(self.brief, self.sources, artifact)

    def test_discovery_phase_integrates_ranking_and_review_hashes(self):
        from research_project import review_inputs
        self.brief.update(status="complete", scope="Helper fixture only", audience="Helper tests", method="Offline fixture")
        self.save("brief.json", self.brief)
        self.save("sources.json", {"schema_version": 1, "search_receipt": {"status": "complete"}, "sources": self.sources})
        self.call("validate", "--project", self.project, "--phase", "discovery", expected=1)
        self.call("rank-references", "--project", self.project)
        self.save("citation-candidates.json", self.screened())
        refresh_project_gate(self.project)
        self.call("validate", "--project", self.project, "--phase", "discovery")
        before = review_inputs(self.project)
        artifact = load(self.project / "citation-candidates.json")
        artifact["candidates"][0]["disposition"]["reason"] = "Updated fixture decision"
        self.save("citation-candidates.json", artifact)
        self.assertNotEqual(before["citation-candidates.json"], review_inputs(self.project)["citation-candidates.json"])

    def test_missing_blocked_lists_and_identity_evidence(self):
        self.sources[0]["reference_list"].update(status="blocked", references=[], limits=["Fixture traffic block"])
        artifact = self.screened()
        artifact.update(status="partial", limits=["One blocked initial list"])
        validate_expansion(self.brief, self.sources, artifact)
        del self.sources[1]["reference_list"]
        with self.assertRaises(ResearchError):
            graph(self.sources)
        self.sources = [source("a", [ref("10.1234/target", identity_evidence=[])])]
        with self.assertRaises(ResearchError):
            graph(self.sources)

    def test_secondary_cannot_bridge_conflicting_candidate_aliases(self):
        artifact = self.screened()
        added = self.addition(artifact)
        added.update(canonical_id="work:ambiguous", identity_evidence=deepcopy(EVIDENCE))
        self.sources[0]["reference_list"]["references"][1].update(canonical_id="work:ambiguous", identity_evidence=deepcopy(EVIDENCE))
        # Rebuild after an identity crosswalk on a different target, then map the addition incorrectly.
        artifact = self.screened()
        artifact["candidates"][0]["disposition"] = {"status": "included", "source_id": "added", "reason": "Fixture"}
        with self.assertRaises(ResearchError):
            validate_expansion(self.brief, self.sources, artifact)

    def test_objective_handler_accepts_only_evidenced_exception(self):
        artifact = self.screened()
        added = self.addition(artifact)
        self.save("brief.json", self.brief)
        self.save("sources.json", {"sources": self.sources})
        self.save("citation-candidates.json", artifact)
        refresh_project_gate(self.project)
        added = next(s for s in load(self.project / "sources.json")["sources"] if s["source_id"] == "added")
        path = Path(__file__).resolve().parents[3] / "evals/research/checks.py"
        spec = importlib.util.spec_from_file_location("research_fixture_checks", path)
        checks = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(checks)
        context = {"constraints": self.brief["constraints"], "evidence": {"project_dir": str(self.project), "sources": [added]}}
        self.assertEqual(checks.check_journal_selection(context)["status"], "pass")
        self.assertEqual(checks.check_citation_expansion(context)["status"], "pass")
        self.assertEqual(checks.check_literature_gate(context)["status"], "pass")
        artifact["candidates"][0]["overlap_count"] = 50
        self.save("citation-candidates.json", artifact)
        self.assertEqual(checks.check_journal_selection(context)["status"], "fail")
        self.assertEqual(checks.check_citation_expansion(context)["status"], "fail")
        self.assertEqual(checks.check_literature_gate(context)["status"], "fail")


if __name__ == "__main__":
    unittest.main()
