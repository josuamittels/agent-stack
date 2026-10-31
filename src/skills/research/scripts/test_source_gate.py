"""Qualification helper fixtures only; no live retrieval or authored-skill evaluation."""
from copy import deepcopy
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys
import tempfile
import subprocess
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "research-literature/scripts"))
from literature_common import dump, load, LiteratureError
from literature_gate import evaluate, validate_receipt, JOURNAL_KEYS
from literature_shared import graph
import verify_sources


def verified_fixture(source):
    source = deepcopy(source)
    source.setdefault("provenance", [{"provider": "fixture", "record_url": "https://example.test/record"}])
    source["provenance"] = [{**p, "record_url": p["record_url"] if p["record_url"].startswith("https://") else "https://example.test/" + source["source_id"]} for p in source["provenance"]]
    source.setdefault("authors", ["Fixture Author"])
    source.setdefault("year", 2020)
    source["relevance"] = {"status": "relevant", "basis": "abstract", "reason": "Helper fixture only", "criteria_status": "pass", "criteria_evidence": {}}
    source["verification"] = {"status": "multi_source_confirmed", "records": []}
    for provider in ("openalex", "crossref"):
        identifiers = deepcopy(source.get("identifiers", {}))
        if source.get("doi"):
            identifiers["doi"] = source["doi"]
        source["verification"]["records"].append({"provider": provider, "kind": "scholarly_database",
            "record_url": f"https://example.test/{provider}/{source['source_id']}", "retrieved_at": "2026-10-31",
            "match_status": "match", "metadata": {"title": source["title"], "authors": source["authors"], "year": source["year"], "identifiers": identifiers},
            "comparisons": {"title": "match", "authors": "match", "year": "match", "venue": "unavailable", "identifier": "match" if identifiers else "unavailable"}, "comparison_notes": {}})
    return source


def contract_fixture(brief=None):
    if brief is None:
        config = {"journal_preset": "default", "journal_article_influence_min": 2.5, "journal_influence_percentile_min": 80,
                  "journal_combination": "or", "journal_filter_disabled": False, "journal_category": None, "journal_exceptions": []}
        config = {k: {"value": v, "source": "skill_default"} for k, v in config.items()}
        depth, requests = "quick", []
    else:
        config = {k: deepcopy(brief["constraints"][k]) for k in JOURNAL_KEYS}
        depth, requests = brief["depth"], brief.get("source_requests", [])
    return {"schema_version": 1, "status": "complete", "depth": depth, "source_target": {"min": 2, "max": 4, "source": "request"},
            "constraints": config, "criteria": {}, "source_requests": requests, "search_passes": [
                {"pass_id": "initial", "status": "complete", "reason": "Helper fixture queries", "queries": [
                    {"provider": "fixture", "query": "first fixture query", "filters": {"journal": "eligible fixtures"}, "outcome": "retrieved", "retrieved_at": "2026-10-31"}]}]}


def refresh_project_gate(project, sources=None):
    brief = load(project / "brief.json")
    inventory = load(project / "sources.json") if sources is None else deepcopy(sources)
    inventory.setdefault("schema_version", 1)
    inventory.setdefault("search_receipt", {"status": "complete", "requested_inputs": []})
    inventory["sources"] = [verified_fixture(s) for s in inventory["sources"]]
    contract = contract_fixture(brief)
    (project / "literature-contract.json").write_text(dump(contract))
    (project / "retrieved-sources.json").write_text(dump(inventory))
    args = ["--contract", str(project / "literature-contract.json"), "--inventory", str(project / "retrieved-sources.json"), "--output-dir", str(project), "--replace"]
    if brief["depth"] == "deep":
        args += ["--expansion", str(project / "citation-candidates.json")]
    with redirect_stdout(io.StringIO()):
        code = verify_sources.main(args)
    if code != 0:
        raise AssertionError("Fixture gate setup failed")


class GateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="source-gate-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.out = self.root / "output"
        self.contract = contract_fixture()
        self.inventory = {"schema_version": 1, "search_receipt": {"status": "complete", "requested_inputs": []}, "sources": [self.source("a"), self.source("b")]}

    def source(self, sid):
        return verified_fixture({"source_id": sid, "title": "Fixture café " + sid, "publication_type": "book", "authors": ["Åse Fixture"], "year": 2020})

    def call(self, expected=0, attempt="initial", phase="final", replace=False):
        (self.root / "contract.json").write_text(dump(self.contract))
        (self.root / "retrieved.json").write_text(dump(self.inventory))
        args = ["--contract", str(self.root / "contract.json"), "--inventory", str(self.root / "retrieved.json"), "--output-dir", str(self.out), "--attempt", attempt, "--phase", phase]
        if replace:
            args.append("--replace")
        output = io.StringIO()
        with redirect_stdout(output):
            code = verify_sources.main(args)
        result = json.loads(output.getvalue())
        self.assertEqual(code, expected, result)
        return result

    def top_up(self):
        self.contract["search_passes"].append({"pass_id": "top_up", "status": "complete", "reason": "Address one missing fixture topic", "queries": [
            {"provider": "fixture", "query": "additional fixture query", "filters": {"journal": "eligible fixtures"}, "outcome": "zero_results", "retrieved_at": "2026-10-31"}]})

    def test_complete_list_and_receipt(self):
        result = self.call()
        self.assertEqual(result["qualified_count"], 2)
        self.assertTrue(result["handoff_ready"])
        validate_receipt(self.out / "source-gate.json")
        readable = (self.out / "sources.md").read_text()
        self.assertIn("café", readable)
        self.assertIn("Åse Fixture", readable)
        self.assertIn("Abstract: unavailable", readable)
        self.assertTrue((self.root / "retrieved.json").exists())

    def test_second_record_or_publisher_required(self):
        record = self.inventory["sources"][0]["verification"]["records"][1]
        record.update(provider="publisher:example.test", kind="primary_publication")
        self.inventory["sources"][0]["verification"]["status"] = "single_source"
        self.assertEqual(self.call()["qualified_count"], 2)
        self.inventory["sources"][1]["verification"]["records"] = self.inventory["sources"][1]["verification"]["records"][:1]
        result = self.call(replace=True)
        self.assertEqual(result["qualified_count"], 1)
        self.assertEqual(result["action"], "top_up_required")
        with self.assertRaises(LiteratureError):
            validate_receipt(self.out / "source-gate.json")

    def test_conflict_not_checked_duplicates_and_malformed_links(self):
        bad = self.source("c")
        bad["verification"]["records"][1]["match_status"] = "conflict"
        duplicate = deepcopy(self.inventory["sources"][0])
        duplicate["source_id"] = "duplicate"
        invalid = self.source("d")
        invalid["article_url"] = "not a URL"
        self.inventory["sources"] += [bad, duplicate, invalid]
        result = self.call()
        self.assertEqual(result["qualified_count"], 2)
        self.assertEqual(result["decisions"]["c"]["status"], "unresolved")
        self.assertIn("duplicate", result["decisions"]["duplicate"]["reason"])
        self.assertEqual(result["decisions"]["d"]["status"], "disqualified")

    def test_doi_less_and_unknown_sources(self):
        self.inventory["sources"][0]["identifiers"] = {"pmid": "123"}
        for record in self.inventory["sources"][0]["verification"]["records"]:
            record["metadata"]["identifiers"] = {"pmid": "123"}
            record["comparisons"]["identifier"] = "match"
        self.inventory["sources"][1]["verification"]["status"] = "not_checked"
        result = self.call()
        self.assertEqual(result["qualified_count"], 1)

    def test_journal_exclusion_explicit_override_and_other_criteria(self):
        journal = self.inventory["sources"][0]
        journal.update(publication_type="journal_article", journal_title="Unmatched fixture journal", issns=[])
        self.assertEqual(self.call()["qualified_count"], 1)
        self.contract["constraints"]["journal_exceptions"] = {"value": ["a"], "source": "request"}
        self.assertEqual(self.call(replace=True)["qualified_count"], 2)
        self.contract["criteria"] = {"year_min": 2021}
        for item in self.inventory["sources"]:
            item["relevance"]["criteria_evidence"] = {"year_min": "Fixture check"}
        self.assertEqual(self.call(replace=True)["qualified_count"], 0)

    def test_requested_inputs_reconciled_after_disqualification(self):
        self.contract["source_requests"] = [{"request_id": "r1", "kind": "work", "input": "Supplied fixture"}]
        self.call(expected=1)
        self.inventory["search_receipt"]["requested_inputs"] = [{"request_id": "r1", "status": "eligible", "source_ids": ["a"], "reason": "Fixture retrieval", "searches": ["fixture exact lookup"]}]
        self.inventory["sources"][0]["verification"]["records"] = []
        self.call()
        outcome = load(self.out / "sources.json")["search_receipt"]["requested_inputs"][0]
        self.assertEqual(outcome["status"], "unresolved")
        self.assertEqual(outcome["source_ids"], [])
        self.assertEqual(outcome["retrieved_source_ids"], ["a"])

    def test_requested_duplicate_maps_to_qualified_representative(self):
        duplicate = deepcopy(self.inventory["sources"][0])
        duplicate["source_id"] = "duplicate"
        self.inventory["sources"].append(duplicate)
        self.contract["source_requests"] = [{"request_id": "r1", "kind": "work", "input": "Fixture a"}]
        self.inventory["search_receipt"]["requested_inputs"] = [{"request_id": "r1", "status": "eligible", "source_ids": ["duplicate"], "reason": "Fixture match", "searches": ["Fixture exact lookup"]}]
        self.call()
        outcome = load(self.out / "sources.json")["search_receipt"]["requested_inputs"][0]
        self.assertEqual(outcome["source_ids"], ["a"])
        self.assertEqual(outcome["status"], "eligible")

    def test_exactly_one_top_up_and_persistent_shortfall(self):
        self.inventory["sources"] = self.inventory["sources"][:1]
        self.assertEqual(self.call()["action"], "top_up_required")
        self.top_up()
        result = self.call(attempt="top_up", replace=True)
        self.assertEqual(result["action"], "return_shortfall")
        self.assertTrue(result["handoff_ready"])
        validate_receipt(self.out / "source-gate.json")
        self.contract["search_passes"].append(deepcopy(self.contract["search_passes"][-1]))
        self.call(attempt="top_up", replace=True, expected=1)

    def test_top_up_addition_and_frozen_rules(self):
        self.inventory["sources"] = self.inventory["sources"][:1]
        self.call()
        self.top_up()
        added = self.source("new")
        added["search_pass"] = "top_up"
        self.inventory["sources"].append(added)
        self.assertEqual(self.call(attempt="top_up", replace=True)["qualified_count"], 2)
        self.contract["constraints"]["journal_filter_disabled"] = {"value": True, "source": "request"}
        self.call(attempt="top_up", replace=True, expected=1)

    def test_no_top_up_without_trigger_or_repeated_queries(self):
        self.top_up()
        self.call(attempt="top_up", expected=1)
        self.contract["search_passes"] = self.contract["search_passes"][:1]
        self.inventory["sources"] = self.inventory["sources"][:1]
        self.call()
        self.top_up()
        self.contract["search_passes"][-1]["queries"] = deepcopy(self.contract["search_passes"][0]["queries"])
        self.call(attempt="top_up", replace=True, expected=1)

    def test_overwrite_stale_receipt_and_formatting(self):
        self.call()
        self.call(expected=1)
        (self.out / "sources.md").write_text("different list")
        with self.assertRaises(LiteratureError):
            validate_receipt(self.out / "source-gate.json")
        self.call(replace=True)
        self.inventory["sources"][0]["title"] = "Altered raw input"
        (self.root / "retrieved.json").write_text(dump(self.inventory))
        with self.assertRaises(LiteratureError):
            validate_receipt(self.out / "source-gate.json")

    def deep_fixture(self):
        self.contract["depth"] = "deep"
        proof = [{"provider": "fixture", "record_url": "https://example.test/references", "retrieved_at": "2026-10-31"}]
        initial = []
        for sid in ("a", "b"):
            entry = self.source(sid)
            entry.update(doi="10.1234/" + sid, publication_type="journal_article", journal_title="Nature", issns=["0028-0836"])
            entry = verified_fixture(entry)
            entry["reference_list"] = {"status": "complete", "retrievals": deepcopy(proof), "limits": [], "references": [
                {"identity_status": "resolved", "identifiers": {"doi": "10.1234/target"}, "identity_evidence": deepcopy(proof)}]}
            initial.append(entry)
        expansion = graph(initial)
        expansion["status"] = "complete"
        expansion["candidates"][0]["disposition"] = {"status": "included", "source_id": "target", "reason": "Relevant fixture target"}
        target = self.source("target")
        target.update(doi="10.1234/target", publication_type="journal_article", journal_title="Unmatched fixture journal", issns=[], discovery_level="secondary",
                      secondary_discovery={"candidate_id": "doi:10.1234/target", "citing_source_ids": ["a", "b"], "overlap_count": 2,
                                           "journal_filter": "overlap_exempt", "relevance_reason": "Fixture relevance", "other_criteria_evidence": "Fixture screening"})
        target = verified_fixture(target)
        self.inventory["sources"] = initial + [target]
        return expansion

    def test_deep_overlap_recalculated_after_anchor_disqualification(self):
        expansion = self.deep_fixture()
        self.assertEqual(evaluate(self.contract, self.inventory, expansion, "initial", "final")[-1]["qualified_count"], 3)
        self.inventory["sources"][1]["verification"]["records"] = []
        output, excluded, normalized, _, receipt = evaluate(self.contract, self.inventory, expansion, "initial", "final")
        self.assertEqual([s["source_id"] for s in output["sources"]], ["a"])
        self.assertIn("exception lost", receipt["decisions"]["target"]["reason"])
        self.assertEqual(normalized["candidates"][0]["disposition"]["status"], "excluded")
        self.assertEqual(expansion["candidates"][0]["disposition"]["status"], "included")

    def test_deep_top_up_does_not_become_seed_or_start_next_hop(self):
        expansion = self.deep_fixture()
        self.contract["source_target"] = {"min": 4, "max": 6, "source": "request"}
        self.top_up()
        entry = self.source("top-up")
        entry["search_pass"] = "top_up"
        self.inventory["sources"].append(entry)
        output, _, normalized, _, receipt = evaluate(self.contract, self.inventory, expansion, "top_up", "final")
        self.assertEqual(receipt["qualified_count"], 4)
        self.assertEqual(normalized["initial_source_ids"], ["a", "b"])
        self.assertEqual(graph(self.inventory["sources"])["initial_source_ids"], ["a", "b"])
        self.assertEqual(next(s for s in output["sources"] if s["source_id"] == "target")["secondary_discovery"]["overlap_count"], 2)

    def test_deep_empty_anchor_pool_and_anchor_phase(self):
        self.contract["depth"] = "deep"
        self.inventory["sources"] = []
        empty = graph([])
        empty.update(status="partial", limits=["No qualifying anchors available"])
        self.assertEqual(evaluate(self.contract, self.inventory, empty, "initial", "final")[-1]["action"], "top_up_required")
        self.assertEqual(evaluate(self.contract, self.inventory, None, "initial", "anchors")[-1]["action"], "continue_expansion")

    def test_non_deep_cannot_accept_secondary_expansion(self):
        expansion = self.deep_fixture()
        self.contract["depth"] = "normal"
        with self.assertRaises(LiteratureError):
            evaluate(self.contract, self.inventory, expansion, "initial", "final")

    def test_top_up_history_cannot_be_reset_or_extended(self):
        self.inventory["sources"] = self.inventory["sources"][:1]
        self.call()
        self.top_up()
        self.call(attempt="top_up", replace=True)
        self.inventory["sources"].append(self.source("third-pass-candidate"))
        self.call(attempt="top_up", replace=True, expected=1)
        self.contract["search_passes"] = self.contract["search_passes"][:1]
        self.call(replace=True, expected=1)

    def test_unknown_work_types_cannot_bypass_journal_filter(self):
        self.inventory["sources"][0].update(publication_type="unknown", journal_title="Unmatched fixture journal")
        self.assertEqual(self.call()["qualified_count"], 1)
        self.inventory["sources"][0].update(csl={"type": "article-journal"}, journal_filter_applicable=False)
        self.assertEqual(self.call(replace=True)["qualified_count"], 1)
        self.inventory["sources"][0]["csl"] = {"type": "software"}
        self.assertEqual(self.call(replace=True)["qualified_count"], 2)

    def test_intermediate_pool_gate_defers_retry_until_combined(self):
        self.inventory["sources"] = self.inventory["sources"][:1]
        result = self.call(phase="pool")
        self.assertEqual(result["action"], "continue_collection")
        self.assertFalse(result["handoff_ready"])
        self.assertFalse((self.out / "source-gate.initial.json").exists())
        self.inventory["sources"].append(self.source("planned-primary"))
        result = self.call()
        self.assertEqual(result["action"], "return_qualified")
        self.assertFalse(result["top_up_used"])

    def test_standalone_cli_without_research_imports(self):
        (self.root / "contract.json").write_text(dump(self.contract))
        (self.root / "retrieved.json").write_text(dump(self.inventory))
        script = Path(__file__).resolve().parents[2] / "research-literature/scripts/verify_sources.py"
        result = subprocess.run([sys.executable, str(script), "--contract", str(self.root / "contract.json"),
                                 "--inventory", str(self.root / "retrieved.json"), "--output-dir", str(self.out)],
                                cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.assertTrue(json.loads(result.stdout)["handoff_ready"])

    def test_input_protection_even_with_replace(self):
        self.out.mkdir()
        contract_path = self.root / "contract.json"
        inventory_path = self.out / "sources.json"
        contract_path.write_text(dump(self.contract))
        original = dump(self.inventory)
        inventory_path.write_text(original)
        output = io.StringIO()
        with redirect_stdout(output):
            code = verify_sources.main(["--contract", str(contract_path), "--inventory", str(inventory_path),
                                        "--output-dir", str(self.out), "--replace"])
        self.assertEqual(code, 1)
        self.assertEqual(inventory_path.read_text(), original)
        self.assertFalse((self.out / "source-gate.json").exists())

    def test_upper_bound_is_target_not_reason_to_pad_or_disqualify(self):
        self.contract["source_target"] = {"min": 1, "max": 1, "source": "request"}
        result = self.call()
        self.assertEqual(result["target_status"], "above_target")
        self.assertEqual(result["qualified_count"], 2)
        self.assertEqual(result["action"], "return_qualified")


if __name__ == "__main__":
    unittest.main()
