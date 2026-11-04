"""Offline, one-hop reference ranking and evidence-backed discovery validation."""
from __future__ import annotations

import csv
import math
from pathlib import Path
import re

from literature_common import SKILL, digest, dump, require


def text(value):
    return isinstance(value, str) and bool(value.strip())


def evidence(items):
    return (isinstance(items, list) and bool(items) and all(
        isinstance(p, dict) and all(text(p.get(k)) for k in ("provider", "record_url", "retrieved_at"))
        for p in items))


def identifier(kind, value):
    require(text(value), "Reference identifiers must be nonempty strings")
    value = value.strip()
    if kind == "doi":
        value = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:)", "", value, flags=re.I).lower()
        require(bool(re.fullmatch(r"10\.\d{4,9}/\S+", value)), "Malformed DOI in reference identity")
    elif kind == "openalex":
        value = re.sub(r"^https?://openalex\.org/", "", value, flags=re.I).upper()
        require(bool(re.fullmatch(r"W\d+", value)), "Malformed OpenAlex work ID")
    elif kind == "pmid":
        require(value.isdigit(), "Malformed PMID")
    elif kind == "arxiv":
        value = re.sub(r"^https?://arxiv\.org/abs/", "", value, flags=re.I)
        value = re.sub(r"v\d+$", "", value).lower()
        require(bool(re.fullmatch(r"(?:\d{4}\.\d{4,5}|[a-z.-]+/\d{7})", value)), "Malformed arXiv work ID")
    else:
        require(kind == "semantic_scholar", f"Unsupported identifier namespace: {kind}")
        value = value.lower()
    return f"{kind}:{value}"


def aliases(record):
    ids = record.get("identifiers", {})
    require(isinstance(ids, dict), "identifiers must be a namespace/value object")
    result = {identifier(k, v) for k, v in ids.items() if v is not None}
    if record.get("doi"):
        doi_key = identifier("doi", record["doi"])
        require(not ids.get("doi") or identifier("doi", ids["doi"]) == doi_key, "Conflicting source DOI fields; reconcile identity before ranking")
        result.add(doi_key)
    canonical = record.get("canonical_id")
    if canonical is not None:
        require(text(canonical) and canonical.startswith("work:") and evidence(record.get("identity_evidence")),
                "Manual work/version reconciliation requires work: canonical_id and dated identity_evidence")
        result.add(canonical)
    return result


def graph(sources):
    """Resolve only supplied, evidenced aliases; never fuzzy-match titles or authors."""
    require(isinstance(sources, list) and all(isinstance(s, dict) for s in sources), "Invalid sources array")
    source_ids = [s.get("source_id") for s in sources]
    require(all(text(s) for s in source_ids) and len(set(source_ids)) == len(source_ids), "Missing/duplicate source IDs")
    require(all(s.get("discovery_level", "initial") in {"initial", "secondary"} for s in sources), "Invalid discovery_level")
    initial = sorted((s for s in sources if s.get("discovery_level", "initial") == "initial" and s.get("search_pass", "initial") == "initial"), key=lambda s: s["source_id"])
    parent = {}

    def find(key):
        parent.setdefault(key, key)
        if parent[key] != key:
            parent[key] = find(parent[key])
        return parent[key]

    def union(keys):
        keys = sorted(keys)
        for key in keys:
            find(key)
        leader = min(find(key) for key in keys)
        for key in keys:
            parent[find(key)] = leader

    source_keys, links, coverage, unresolved = {}, [], [], []
    for source in initial:
        sid = source["source_id"]
        keys = aliases(source) | {"source:" + sid}
        union(keys)
        source_keys[sid] = keys
        listing = source.get("reference_list")
        require(isinstance(listing, dict), f"Record reference-list retrieval for {sid}")
        status = listing.get("status")
        require(status in {"complete", "partial", "unavailable", "blocked"}, f"Reference-list attempt pending for {sid}")
        require(evidence(listing.get("retrievals")), f"Record dated retrieval/blocked-attempt provenance for {sid}")
        limits = listing.get("limits")
        require(isinstance(limits, list) and all(text(l) for l in limits)
                and (status == "complete" or limits), f"Record reference coverage limits for {sid}")
        refs = listing.get("references")
        require(isinstance(refs, list), f"reference_list.references must be an array: {sid}")
        coverage.append({"source_id": sid, "status": status, "retrievals": listing["retrievals"], "limits": limits})
        for index, ref in enumerate(refs):
            require(isinstance(ref, dict) and ref.get("identity_status") in {"resolved", "unresolved"}, "Reference needs explicit identity_status")
            if ref["identity_status"] == "unresolved":
                unresolved.append({"source_id": sid, "reference_index": index, "reference": ref})
                continue
            require(evidence(ref.get("identity_evidence")), f"Resolved reference needs identity evidence: {sid}/{index}")
            keys = aliases(ref)
            require(keys, "Resolved reference needs an identifier or evidenced manual identity")
            union(keys)
            links.append((sid, index, keys, ref.get("provenance", listing["retrievals"])))
            require(evidence(links[-1][3]), "Citation edge requires dated provider provenance")
    groups = {}
    for key in parent:
        groups.setdefault(find(key), set()).add(key)
    # Prefer external bibliographic identities over local source labels.
    names = {root: min(keys, key=lambda k: (k.startswith(("source:", "work:")), k)) for root, keys in groups.items()}
    initial_groups = {}
    for sid, keys in source_keys.items():
        initial_groups.setdefault(names[find(next(iter(keys)))], []).append(sid)
    representatives = {sid: min(members) for members in initial_groups.values() for sid in members}
    candidates = {}
    for sid, index, keys, provenance in links:
        key = names[find(next(iter(keys)))]
        item = candidates.setdefault(key, {"candidate_id": key, "identity_keys": sorted(groups[find(next(iter(keys)))]),
                                          "citing_source_ids": [], "overlap_count": 0, "edges": [],
                                          "existing_source_ids": sorted(initial_groups.get(key, []))})
        item["citing_source_ids"].append(representatives[sid])
        item["edges"].append({"from_source_id": sid, "to_candidate_id": key, "reference_index": index, "provenance": provenance})
    for item in candidates.values():
        item["citing_source_ids"] = sorted(set(item["citing_source_ids"]))
        item["overlap_count"] = len(item["citing_source_ids"])
        item["disposition"] = {"status": "already_initial" if item["existing_source_ids"] else "pending", "source_id": None, "reason": None}
    ranked = sorted(candidates.values(), key=lambda c: (-c["overlap_count"], c["candidate_id"]))
    # Bind the graph to identity and reference inputs, but not later appraisal annotations.
    inputs = [{k: s.get(k) for k in ("source_id", "doi", "identifiers", "canonical_id", "identity_evidence", "reference_list")} for s in initial]
    return {"schema_version": 1, "status": "ranked", "initial_source_ids": [s["source_id"] for s in initial],
            "initial_inputs_sha256": digest(dump(inputs)), "initial_work_groups": initial_groups,
            "candidates": ranked, "coverage": coverage, "unresolved_references": unresolved, "limits": []}




def journal_applicable(source):
    kind = source.get("publication_type", "").strip().casefold().replace("-", "_").replace(" ", "_")
    csl = source.get("csl")
    return kind in {"journal_article", "review"} or isinstance(csl, dict) and csl.get("type") == "article-journal" or source.get("journal_filter_applicable") is True


def journal_qualifies(source, brief):
    """Use the same CSV thresholds for secondary singleton screening as initial discovery."""
    config = brief["constraints"]
    val = lambda key: config[key]["value"]
    if val("journal_filter_disabled"):
        return config["journal_filter_disabled"]["source"] == "request"
    if source["source_id"] in val("journal_exceptions"):
        return config["journal_exceptions"]["source"] == "request"
    if not journal_applicable(source):
        return True
    normalize = lambda s: re.sub(r"[^\w]", "", s.casefold())
    issns = {normalize(s) for s in source.get("issns", []) if text(s)}
    title = source.get("journal_title")
    with (SKILL / "references/journals.csv").open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream))
    if issns:
        rows = [r for r in rows if issns & {normalize(r.get(k, "")) for k in ("issn_print", "issn_online")}]
    else:
        rows = [r for r in rows if text(title) and normalize(r.get("journal", "")) == normalize(title)]
    if not rows or not text(title) or any(normalize(r["journal"]) != normalize(title) for r in rows):
        return False
    category = val("journal_category")
    require(category is None or isinstance(category, str), "Journal category must be a string or null")
    rows = [r for r in rows if category is None or r.get("category", "").casefold() == category.casefold()]
    thresholds = [("article_influence", val("journal_article_influence_min")), ("influence_percentile", val("journal_influence_percentile_min"))]
    for row in rows:
        branches = []
        for field, cutoff in thresholds:
            if cutoff is None:
                continue
            try:
                score = float(row[field])
                branches.append(math.isfinite(score) and score >= 0 and (field != "influence_percentile" or score <= 100) and score >= cutoff)
            except (ValueError, TypeError, KeyError):
                branches.append(False)
        if branches and (all(branches) if val("journal_combination") == "and" else any(branches)):
            return True
    return False


def validate_expansion(brief, sources, artifact, raw_sources=None):
    require(brief.get("depth") in {"quick", "normal", "deep"}, "Invalid discovery depth")
    require(artifact is None or isinstance(artifact, dict), "Citation expansion artifact must be an object")
    secondary = {s["source_id"]: s for s in sources if s.get("discovery_level", "initial") == "secondary"}
    require(all(s.get("discovery_level", "initial") in {"initial", "secondary"} for s in sources), "Invalid discovery_level")
    if brief.get("depth") != "deep":
        require(not secondary and (artifact is None or artifact.get("status") == "pending"), "Secondary discovery is deep-only")
        return {}
    require(isinstance(artifact, dict) and artifact.get("status") in {"complete", "partial"}, "Finish or explicitly limit deep reference screening")
    if raw_sources is not None:
        frozen = artifact.get("initial_source_ids", [])
        require(isinstance(frozen, list) and len(set(frozen)) == len(frozen), "Invalid frozen source IDs")
        anchors = [s for s in raw_sources if s["source_id"] in frozen]
        require({s["source_id"] for s in anchors} == set(frozen), "Frozen sources missing from raw inventory")
        require(all(s.get("search_pass", "initial") == "initial" and s.get("discovery_level", "initial") == "initial" for s in anchors),
                "Top-up or secondary sources cannot become frozen seeds")
        require(all(s["source_id"] in frozen or s.get("search_pass") == "top_up" for s in sources if s.get("discovery_level", "initial") == "initial"),
                "Additional initial sources require top-up annotations")
        expected = graph(anchors)
    else:
        expected = graph(sources)
    for initial in sources:
        if initial.get("discovery_level", "initial") == "initial":
            require(journal_qualifies(initial, brief), "Initial journal anchors must satisfy the ordinary rule or an explicit request override")
    for key in ("schema_version", "initial_source_ids", "initial_inputs_sha256", "initial_work_groups", "coverage", "unresolved_references"):
        require(artifact.get(key) == expected[key], f"Stale/invalid citation expansion: {key}")
    actual = artifact.get("candidates")
    require(isinstance(actual, list) and len(actual) == len(expected["candidates"]), "Citation candidate count differs from recorded reference lists")
    limits = artifact.get("limits")
    require(isinstance(limits, list) and all(text(l) for l in limits), "Expansion limits must be strings")
    require(artifact["status"] != "partial" or limits, "Partial expansion requires explicit limits")
    partial = bool(expected["unresolved_references"]) or any(c["status"] != "complete" for c in expected["coverage"])
    included, exemptions, previous_statuses = set(), {}, []
    for item, derived in zip(actual, expected["candidates"]):
        require(isinstance(item, dict) and {k: v for k, v in item.items() if k != "disposition"}
                == {k: v for k, v in derived.items() if k != "disposition"}, "Candidate order, identities or citation edges changed; rerank explicitly")
        decision = item.get("disposition", {})
        require(isinstance(decision, dict), "Candidate disposition must be an object")
        status = decision.get("status")
        require(status in {"included", "excluded", "unresolved", "not_inspected", "already_initial"}, "Pending citation candidate screening")
        if derived["existing_source_ids"]:
            require(status == "already_initial", "Initial works stay initial, without duplicate additions")
        else:
            require(status != "already_initial" and text(decision.get("reason")), "Record candidate selection/access reason")
        if status in {"unresolved", "not_inspected"}:
            partial = True
        if status not in {"not_inspected", "already_initial"}:
            require("not_inspected" not in previous_statuses, "Screen higher-ranked candidates before lower-ranked ones")
        previous_statuses.append(status)
        if status != "included":
            continue
        sid = decision.get("source_id")
        require(sid in secondary and sid not in included, "Included candidate must map to exactly one secondary source")
        source = secondary[sid]
        source_aliases = aliases(source)
        matches = [c["candidate_id"] for c in expected["candidates"] if source_aliases & set(c["identity_keys"])]
        require(matches == [item["candidate_id"]], "Secondary identity must match exactly one candidate; reconcile conflicting aliases before ranking")
        require(not any(source_aliases & aliases(initial) for initial in sources if initial.get("discovery_level", "initial") == "initial"),
                "Secondary source duplicates an initial identity; reconcile before ranking")
        citing_ids = item["citing_source_ids"]
        if raw_sources is not None:
            qualified_ids = {s["source_id"] for s in sources}
            citing_ids = sorted(min(set(members) & qualified_ids) for members in expected["initial_work_groups"].values()
                                if min(members) in item["citing_source_ids"] and set(members) & qualified_ids)
        annotation = source.get("secondary_discovery", {})
        require(isinstance(annotation, dict), "Secondary source needs secondary_discovery annotation")
        require(annotation.get("candidate_id") == item["candidate_id"] and annotation.get("citing_source_ids") == citing_ids
                and annotation.get("overlap_count") == len(citing_ids), "Secondary discovery annotation differs from frozen graph")
        require(text(annotation.get("relevance_reason")) and text(annotation.get("other_criteria_evidence")), "Record relevance and remaining inclusion-criteria screening")
        rule = annotation.get("journal_filter")
        if rule == "overlap_exempt":
            require(len(citing_ids) >= 2, "Journal overlap exception needs two distinct initial citing works")
            exemptions[sid] = {**item, "citing_source_ids": citing_ids, "overlap_count": len(citing_ids)}
        else:
            require(rule == "ordinary" and journal_qualifies(source, brief), "Non-exempt secondary source must pass the ordinary journal rule")
        included.add(sid)
    require(included == set(secondary), "Every secondary source needs a screened, recorded initial-pool citation path")
    require(not partial or artifact["status"] == "partial" and limits, "Incomplete coverage/screening needs partial status and explicit expansion limits")
    return exemptions
