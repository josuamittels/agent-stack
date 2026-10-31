"""Offline qualification, canonical list rendering, and one-top-up receipts."""
from __future__ import annotations
from copy import deepcopy
from pathlib import Path
import re
from urllib.parse import urlparse, quote

from literature_common import SKILL, digest, dump, file_hash, load, publish, require, LiteratureError
from literature_shared import aliases, graph, identifier, journal_applicable, journal_qualifies, text, validate_expansion

TARGETS = {"quick": (8, 12), "normal": (16, 24), "deep": (32, 64)}
JOURNAL_KEYS = ("journal_preset", "journal_article_influence_min", "journal_influence_percentile_min",
                "journal_combination", "journal_filter_disabled", "journal_category", "journal_exceptions")


def url(value):
    if not text(value):
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"https", "http"} and bool(parsed.netloc) and not parsed.username and not any(c.isspace() for c in value)


def key(value):
    return " ".join(re.findall(r"\w+", str(value).casefold()))


def contract_core(contract):
    return {k: v for k, v in contract.items() if k != "search_passes"}


def validate_contract(contract, attempt, phase):
    require(isinstance(contract, dict) and contract.get("schema_version") == 1 and contract.get("status") == "complete", "Complete the literature contract")
    require(contract.get("depth") in TARGETS, "Invalid literature depth")
    target = contract.get("source_target", {})
    require(isinstance(target, dict) and target.get("source") in {"request", "skill_default"}
            and type(target.get("min")) is int and target["min"] >= 0
            and (target.get("max") is None or type(target["max"]) is int and target["max"] >= target["min"]), "Invalid source target/provenance")
    if target["source"] == "skill_default":
        require((target["min"], target["max"]) == TARGETS[contract["depth"]], "Skill-default targets must match depth")
    config = contract.get("constraints", {})
    for name in JOURNAL_KEYS:
        row = config.get(name)
        require(isinstance(row, dict) and set(row) == {"value", "source"} and row["source"] in {"request", "skill_default"}, f"Missing journal rule/provenance: {name}")
    val = lambda name: config[name]["value"]
    require(val("journal_preset") in {"lenient", "default", "strict", "custom", "disabled"} and val("journal_combination") in {"or", "and"}, "Invalid journal selection")
    require(type(val("journal_filter_disabled")) is bool, "Journal filter flag must be boolean")
    require(val("journal_category") is None or text(val("journal_category")), "Invalid journal category")
    exceptions = val("journal_exceptions")
    require(isinstance(exceptions, list) and all(text(s) for s in exceptions) and len(set(exceptions)) == len(exceptions), "Invalid journal exception IDs")
    for name in ("journal_exceptions", "journal_category"):
        require(not val(name) or config[name]["source"] == "request", "Journal category/exceptions must be request-sourced")
    if val("journal_filter_disabled"):
        require(val("journal_preset") == "disabled" and config["journal_filter_disabled"]["source"] == "request"
                and config["journal_preset"]["source"] == "request"
                and val("journal_article_influence_min") is None and val("journal_influence_percentile_min") is None, "Disabled filter requires an explicit, consistent request override")
    else:
        require(val("journal_preset") != "disabled", "Disabled preset needs disabled filter")
        cutoffs = [val("journal_article_influence_min"), val("journal_influence_percentile_min")]
        import math
        require(any(v is not None for v in cutoffs) and all(v is None or type(v) in {int, float} and math.isfinite(v) and v >= 0 for v in cutoffs)
                and (cutoffs[1] is None or cutoffs[1] <= 100), "Invalid journal thresholds")
    require(isinstance(contract.get("criteria"), dict), "criteria must explicitly record additional inclusion requirements")
    criteria = contract["criteria"]
    for name in ("year_min", "year_max"):
        require(criteria.get(name) is None or type(criteria[name]) is int, f"Invalid criterion: {name}")
    require(criteria.get("year_min") is None or criteria.get("year_max") is None or criteria["year_min"] <= criteria["year_max"], "Invalid requested year range")
    require(criteria.get("language") is None or text(criteria["language"]), "Requested language must be a nonempty code")
    require(criteria.get("work_types") is None or isinstance(criteria["work_types"], list) and all(text(t) for t in criteria["work_types"]), "Invalid requested work types")
    preset = val("journal_preset")
    if not val("journal_filter_disabled") and preset in {"lenient", "default", "strict"}:
        scores = {"lenient": (1.0, 60), "default": (2.5, 80), "strict": (5.0, 90)}[preset]
        for name, expected in zip(("journal_article_influence_min", "journal_influence_percentile_min"), scores):
            require(config[name]["source"] != "skill_default" or val(name) == expected, "Journal defaults must match the selected preset; numeric overrides need request provenance")
    requests = contract.get("source_requests")
    require(isinstance(requests, list), "source_requests must be an array")
    request_ids = []
    for item in requests:
        require(isinstance(item, dict) and text(item.get("request_id")) and item.get("kind") in {"work", "author"} and text(item.get("input")), "Invalid requested paper/author")
        request_ids.append(item["request_id"])
    require(len(set(request_ids)) == len(request_ids), "Duplicate source request IDs")
    passes = contract.get("search_passes")
    expected = ["initial", "top_up"] if attempt == "top_up" else ["initial"]
    require(isinstance(passes, list) and [p.get("pass_id") for p in passes if isinstance(p, dict)] == expected, "Record exactly one initial pass and at most one top-up")
    seen = set()
    for row in passes:
        require(row.get("status") in {"complete", "blocked"} and isinstance(row.get("queries"), list) and row["queries"], "Record actual search attempts, including blocked searches")
        require(text(row.get("reason")), "Explain each search pass and any coverage limits")
        for query in row["queries"]:
            require(isinstance(query, dict) and text(query.get("provider")) and text(query.get("query")) and isinstance(query.get("filters"), dict)
                    and query.get("outcome") in {"retrieved", "zero_results", "blocked", "failed"} and text(query.get("retrieved_at")), "Search attempts require provider/query/filters/outcome/date")
            fingerprint = dump([query["provider"].casefold(), " ".join(query["query"].split()), query["filters"]])
            require(fingerprint not in seen, "Do not repeat identical exhausted searches in the top-up pass")
            seen.add(fingerprint)
    require(phase != "pool" or attempt == "initial", "Working-pool qualification precedes the final retry decision")
    require(phase != "anchors" or contract["depth"] == "deep" and attempt == "initial", "Anchor qualification is the first phase of deep discovery only")


def verification(source):
    state = source.get("verification")
    if not isinstance(state, dict) or state.get("status") not in {"multi_source_confirmed", "single_source"}:
        return False, "identity verification missing, unconfirmed or conflicting"
    records = state.get("records", [])
    if not isinstance(records, list):
        return False, "verification.records missing"
    matching = []
    source_keys = aliases(source)
    for record in records:
        if not isinstance(record, dict):
            return False, "invalid verification observation"
        if record.get("match_status") == "conflict":
            return False, "unresolved identity conflict"
        if record.get("match_status") != "match":
            continue
        provider = record.get("provider", "").strip().casefold()
        kind = record.get("kind")
        database = provider in {"openalex", "crossref", "semantic_scholar", "pubmed", "arxiv", "google_scholar"} or provider.startswith("database:")
        if not (text(record.get("retrieved_at")) and url(record.get("record_url"))
                and (kind == "scholarly_database" and database or kind == "primary_publication" and provider.startswith("publisher:"))):
            continue
        metadata = record.get("metadata", {})
        comparisons = record.get("comparisons", {})
        if not isinstance(metadata, dict) or not isinstance(comparisons, dict) or not text(metadata.get("title")):
            continue
        if any(comparisons.get(f) not in {"match", "unavailable"} for f in ("title", "authors", "year", "venue", "identifier")):
            continue
        if comparisons["title"] != "match":
            continue
        notes = record.get("comparison_notes", {})
        if not isinstance(notes, dict):
            continue
        if key(metadata["title"]) != key(source["title"]) and not text(notes.get("title")):
            continue
        record_keys = aliases(metadata)
        shared = source_keys & record_keys
        # A conflicting DOI is not repaired by a free-text comparison note.
        src_doi = {k for k in source_keys if k.startswith("doi:")}
        rec_doi = {k for k in record_keys if k.startswith("doi:")}
        if src_doi and rec_doi and not src_doi & rec_doi:
            return False, "conflicting DOI in retrieved identity records"
        if not shared and not (comparisons["authors"] == "match" and comparisons["year"] == "match"
                               and metadata.get("authors") and source.get("authors")
                               and metadata.get("year") is not None and source.get("year") is not None):
            continue
        if shared and comparisons["identifier"] != "match":
            continue
        valid = True
        for field in ("authors", "year"):
            if source.get(field) and metadata.get(field):
                if comparisons[field] != "match" or source[field] != metadata[field] and not text(notes.get(field)):
                    valid = False
        if valid:
            matching.append((provider, kind, record["record_url"]))
    for first in matching:
        for second in matching:
            if first[0] != second[0] and first[2] != second[2] and "scholarly_database" in {first[1], second[1]}:
                return True, "matching second scholarly database or primary publication record"
    return False, "no matching independent second record; link reachability alone does not qualify"


def screening(source, contract):
    relevant = source.get("relevance")
    if not isinstance(relevant, dict) or relevant.get("status") != "relevant" or relevant.get("criteria_status") != "pass":
        return False, "relevance or inclusion screening incomplete/non-compliant"
    if relevant.get("basis") not in {"abstract", "title_and_metadata", "full_text"} or not text(relevant.get("reason")):
        return False, "record actual relevance inspection and reason"
    notes = relevant.get("criteria_evidence")
    if not isinstance(notes, dict) or not all(text(notes.get(k)) for k, value in contract["criteria"].items() if value is not None and value != []):
        return False, "additional requested inclusion criteria lack screening evidence"
    criteria = contract["criteria"]
    for name, compare in (("year_min", lambda a, b: a >= b), ("year_max", lambda a, b: a <= b)):
        if criteria.get(name) is not None and (type(source.get("year")) is not int or not compare(source["year"], criteria[name])):
            return False, f"source violates {name}"
    if criteria.get("work_types") and source["publication_type"] not in criteria["work_types"]:
        return False, "source violates requested work types"
    if criteria.get("language") and source.get("language") != criteria["language"]:
        return False, "source violates requested language or language is unestablished"
    return True, "relevance and additional inclusion rules screened"


def normalize_requested(contract, inventory, qualified_ids, decisions):
    outcomes = inventory.get("search_receipt", {}).get("requested_inputs", [])
    require(isinstance(outcomes, list), "Requested input outcomes must be an array")
    requests = {r["request_id"] for r in contract["source_requests"]}
    seen, result = set(), []
    raw_ids = {s["source_id"] for s in inventory["sources"]}
    for outcome in outcomes:
        require(isinstance(outcome, dict), "Requested input outcome must be an object")
        rid = outcome.get("request_id")
        require(rid in requests and rid not in seen, "Unknown/duplicate requested input outcome")
        seen.add(rid)
        require(outcome.get("status") in {"eligible", "excluded", "unresolved", "no_eligible_works"} and text(outcome.get("reason")), "Requested input is unaccounted/pending")
        require(isinstance(outcome.get("searches"), list) and outcome["searches"] and all(text(s) for s in outcome["searches"]), "Record supplied-input lookup attempts")
        ids = outcome.get("source_ids")
        require(isinstance(ids, list) and all(isinstance(s, str) and s in raw_ids for s in ids) and len(set(ids)) == len(ids), "Requested input source IDs do not resolve")
        require(outcome["status"] != "eligible" or ids, "Eligible requested input needs retrieved source IDs")
        item = deepcopy(outcome)
        item["retrieved_source_ids"] = ids
        item["source_ids"] = list(dict.fromkeys(s if s in qualified_ids else decisions[s].get("representative_source_id")
                                               for s in ids if s in qualified_ids or decisions[s].get("representative_source_id") in qualified_ids))
        if outcome["status"] == "eligible" and not item["source_ids"]:
            item["status"] = "unresolved" if any(decisions[s]["status"] == "unresolved" for s in ids) else "excluded"
            item["reason"] = "Final gate: " + "; ".join(decisions[s]["reason"] for s in ids)
        result.append(item)
    require(seen == requests, "Account for every supplied paper/author before handoff")
    return result


def qualify(contract, inventory, expansion=None, phase="final"):
    require(isinstance(inventory, dict) and inventory.get("schema_version") == 1 and isinstance(inventory.get("sources"), list), "Inventory requires schema_version 1 and sources[]")
    require(isinstance(inventory.get("search_receipt"), dict), "Raw inventory needs its search receipt")
    considered = inventory["search_receipt"].get("considered_count")
    require(considered is None or type(considered) is int and considered >= 0, "considered_count must be measured integer or unavailable")
    raw = inventory["sources"]
    require(all(isinstance(s, dict) and text(s.get("source_id")) and not any(c.isspace() or ord(c) < 32 for c in s["source_id"]) for s in raw), "Each source needs a stable source_id without whitespace/control characters")
    require(len({s["source_id"] for s in raw}) == len(raw), "Duplicate source IDs; reconcile raw record identity first")
    decisions, copies = {}, {}
    allowed_passes = {p["pass_id"] for p in contract["search_passes"]}
    for source in sorted(raw, key=lambda s: s["source_id"]):
        sid = source["source_id"]
        reason, status = None, "disqualified"
        if not all(text(source.get(k)) for k in ("title", "publication_type")):
            reason = "required bibliographic fields missing"
        elif source.get("article_url") is not None and not url(source["article_url"]):
            reason = "malformed article URL"
        elif not isinstance(source.get("provenance"), list) or not source["provenance"] or not all(isinstance(p, dict) and text(p.get("provider")) and url(p.get("record_url")) for p in source["provenance"]):
            reason = "source retrieval provenance missing or malformed"
        elif source.get("csl") is not None and not isinstance(source["csl"], dict):
            reason = "CSL metadata must be an object or unavailable"
        elif source.get("year") is not None and type(source["year"]) is not int:
            reason = "year must be an integer or unavailable"
        elif source.get("abstract") is not None and not isinstance(source["abstract"], str):
            reason = "abstract must be text or unavailable"
        elif not isinstance(source.get("authors", []), list) or not all(text(a) if isinstance(a, str) else isinstance(a, dict) and any(text(a.get(k)) for k in ("literal", "given", "family")) for a in source.get("authors", [])):
            reason = "authors must be preserved as an array of display names or CSL name objects"
        elif source["publication_type"].strip().casefold().replace("-", "_").replace(" ", "_") not in {"journal_article", "review", "book", "book_chapter", "report", "webpage", "dataset", "preprint", "conference_paper"} and not (isinstance(source.get("csl"), dict) and text(source["csl"].get("type")) and type(source.get("journal_filter_applicable")) is bool):
            reason = "unclassified work type; normalize it or supply CSL type and explicit journal applicability"
        elif source.get("discovery_level", "initial") not in {"initial", "secondary"}:
            reason = "invalid discovery level"
        elif source.get("search_pass", "initial") not in allowed_passes:
            reason = "unrecorded search pass"
        elif source.get("search_pass") == "top_up" and source.get("discovery_level", "initial") != "initial":
            reason = "top-up results cannot be citation expansion additions"
        elif not (url(source.get("article_url")) or source.get("doi") or any(url(p.get("record_url")) for p in source.get("provenance", []) if isinstance(p, dict))):
            reason = "no valid work link"
        else:
            try:
                aliases(source)
                verified, note = verification(source)
                relevant, relevance_note = screening(source, contract)
                if not verified:
                    reason, status = note, "unresolved"
                elif not relevant:
                    reason = relevance_note
                else:
                    copies[sid] = deepcopy(source)
                    decisions[sid] = {"status": "provisional", "reason": note}
                    continue
            except (LiteratureError, TypeError, AttributeError) as exc:
                reason = "invalid identity/verification fields: " + str(exc)
        decisions[sid] = {"status": status, "reason": reason}
    normalized = deepcopy(expansion)
    if contract["depth"] != "deep" or phase != "final":
        require(expansion is None or expansion.get("status") == "pending", "Citation expansion is not allowed in this gate phase")
        for sid, source in list(copies.items()):
            if source.get("discovery_level", "initial") == "secondary":
                decisions[sid] = {"status": "disqualified", "reason": "secondary discovery is deep-final-only"}
                del copies[sid]
    # Initial candidates and top-up topic results always keep the ordinary journal rule.
    for sid, source in list(copies.items()):
        if source.get("discovery_level", "initial") == "initial" and not journal_qualifies(source, contract):
            decisions[sid] = {"status": "disqualified", "reason": "journal filter failed or journal eligibility unestablished"}
            del copies[sid]
    def deduplicate(initial_only=False):
        groups = []
        for sid, source in copies.items():
            if initial_only and source.get("discovery_level", "initial") != "initial":
                continue
            identities = aliases(source)
            if not identities:
                identities = {"metadata:" + dump([key(source["title"]), source.get("authors", []), source.get("year")])}
            matches = [i for i, (known, members) in enumerate(groups) if known & identities]
            members = {sid}
            for index in reversed(matches):
                known, previous = groups.pop(index)
                identities |= known
                members |= previous
            groups.append((identities, members))
        for _, members in groups:
            representative = min(members, key=lambda sid: (copies[sid].get("discovery_level", "initial") != "initial", copies[sid].get("search_pass", "initial") != "initial", sid))
            for sid in members - {representative}:
                decisions[sid] = {"status": "disqualified", "reason": "duplicate work identity; represented by " + representative, "representative_source_id": representative}
                del copies[sid]
    deduplicate(initial_only=True)
    if contract["depth"] == "deep" and phase == "final":
        require(isinstance(expansion, dict) and expansion.get("status") in {"complete", "partial"}, "Deep final gate requires completed or explicitly partial one-hop evidence")
        frozen = expansion.get("initial_source_ids", [])
        anchors = [s for s in raw if s["source_id"] in frozen]
        expected = graph(anchors)
        for field in ("schema_version", "initial_source_ids", "initial_inputs_sha256", "initial_work_groups", "coverage", "unresolved_references"):
            require(expansion.get(field) == expected[field], f"Stale raw citation graph: {field}")
        require(isinstance(expansion.get("candidates"), list) and len(expansion["candidates"]) == len(expected["candidates"]), "Raw citation candidates differ from reference lists")
        mapped = {}
        for item, derived in zip(expansion["candidates"], expected["candidates"]):
            require({k: v for k, v in item.items() if k != "disposition"} == {k: v for k, v in derived.items() if k != "disposition"}, "Raw citation graph edges/ranking changed")
            decision = item.get("disposition", {})
            if decision.get("status") == "included":
                sid = decision.get("source_id")
                require(sid not in mapped, "A source cannot fill multiple citation candidates")
                mapped[sid] = item
        for sid, source in list(copies.items()):
            if source.get("discovery_level", "initial") != "secondary":
                continue
            item = mapped.get(sid)
            if item is None or not aliases(source) & set(item["identity_keys"]):
                decisions[sid] = {"status": "disqualified", "reason": "secondary source lacks a matching frozen citation path"}
                del copies[sid]
                continue
            qualified_initial = {i for i, s in copies.items() if s.get("discovery_level", "initial") == "initial"}
            citing = sorted(min(set(members) & qualified_initial) for members in expected["initial_work_groups"].values()
                            if min(members) in item["citing_source_ids"] and set(members) & qualified_initial)
            ordinary = journal_qualifies(source, contract)
            if len(citing) < 2 and not ordinary:
                decisions[sid] = {"status": "disqualified", "reason": "journal exception lost: fewer than two qualified initial citing works"}
                del copies[sid]
                continue
            annotation = source.get("secondary_discovery")
            if not isinstance(annotation, dict) or not text(annotation.get("relevance_reason")) or not text(annotation.get("other_criteria_evidence")):
                decisions[sid] = {"status": "disqualified", "reason": "secondary screening annotations missing"}
                del copies[sid]
                continue
            annotation.update(candidate_id=item["candidate_id"], citing_source_ids=citing, overlap_count=len(citing),
                              journal_filter="ordinary" if ordinary else "overlap_exempt")
        deduplicate()
        for item in normalized["candidates"]:
            decision = item.get("disposition", {})
            if decision.get("status") == "included" and decision.get("source_id") not in copies:
                sid = decision.get("source_id")
                require(sid in decisions, "Included citation candidate missing from retrieved source inventory")
                item["disposition"] = {"status": "excluded", "source_id": None, "reason": "Final gate: " + decisions[sid]["reason"]}
        validate_expansion(contract, list(copies.values()), normalized, raw_sources=raw)
    deduplicate()
    for sid, source in copies.items():
        journal = "non_journal"
        if journal_applicable(source):
            journal = ("overlap_exempt" if isinstance(source.get("secondary_discovery"), dict) and source["secondary_discovery"].get("journal_filter") == "overlap_exempt"
                       else "disabled" if contract["constraints"]["journal_filter_disabled"]["value"]
                       else "explicit_exception" if sid in contract["constraints"]["journal_exceptions"]["value"] else "ordinary")
        source["qualification"] = {"mechanical_status": "qualified", "identity": "matching_second_record", "journal_basis": journal}
        decisions[sid] = {"status": "qualified", "reason": "identity, relevance, format and journal/exception checks passed"}
    output = {"schema_version": 1, "search_receipt": deepcopy(inventory.get("search_receipt", {})), "sources": list(copies.values())}
    output["search_receipt"]["requested_inputs"] = normalize_requested(contract, inventory, set(copies), decisions)
    output["search_receipt"]["status"] = "partial" if any(p["status"] == "blocked" or any(q["outcome"] in {"blocked", "failed"} for q in p["queries"]) for p in contract["search_passes"]) or inventory.get("search_receipt", {}).get("status") in {"partial", "blocked"} or len(copies) < contract["source_target"]["min"] or any(d["status"] == "unresolved" for d in decisions.values()) else "complete"
    rejected = [{"source": deepcopy(s), **decisions[s["source_id"]]} for s in raw if s["source_id"] not in copies]
    return output, rejected, normalized, decisions


def escape(value):
    return re.sub(r"([\\`*_{}\[\]<>#!|])", r"\\\1", str(value)).replace("\n", " ")


def display_author(value):
    if isinstance(value, dict):
        return value.get("literal") or " ".join(str(value[k]) for k in ("given", "family") if value.get(k))
    return str(value)


def render(inventory):
    rows = [f"# Qualified sources ({len(inventory['sources'])})", ""]
    for index, source in enumerate(inventory["sources"], 1):
        rows += [f"## {index}. {escape(source['title'])}", "",
                 f"- Source ID: {escape(source['source_id'])}",
                 "- Authors: " + escape("; ".join(display_author(a) for a in source.get("authors", [])) or "unavailable"),
                 "- Year: " + escape(source.get("year") if source.get("year") is not None else "unavailable"),
                 "- Venue: " + escape(source.get("journal_title") or source.get("publisher") or "unavailable"),
                 "- Work type: " + escape(source["publication_type"]),
                 "- Discovery level: " + escape(source.get("discovery_level", "initial")),
                 "- Verification: matching second record"]
        if source.get("discovery_level") == "secondary":
            rows.append("- Qualified initial citing works: " + str(source["secondary_discovery"]["overlap_count"]))
        link = source.get("article_url")
        if not url(link):
            link = next((p["record_url"] for p in source.get("verification", {}).get("records", []) if url(p.get("record_url"))), None)
        require(url(link), "Qualified source has no usable work record link")
        doi = source.get("doi") or source.get("identifiers", {}).get("doi")
        doi_link = "https://doi.org/" + identifier("doi", doi)[4:] if doi else None
        oa = source.get("open_access_url")
        rows += ["- DOI: " + ("[" + escape(identifier("doi", doi)[4:]) + "](" + quote(doi_link, safe=":/?#@!$&'*,;=%+") + ")" if doi else "unavailable"),
                 "- Work record: [link](" + quote(link, safe=":/?#@!$&'*,;=%+") + ")",
                 "- Open-access link: " + ("[reported link](" + quote(oa, safe=":/?#@!$&'*,;=%+") + ") — access not independently checked" if url(oa) else "unavailable"),
                 "- Journal decision: " + escape(source["qualification"]["journal_basis"]), "",
                 "Abstract: " + escape(source.get("abstract") or "unavailable"), ""]
    return "\n".join(rows)


def evaluate(contract, inventory, expansion, attempt, phase):
    validate_contract(contract, attempt, phase)
    qualified, rejected, normalized, decisions = qualify(contract, inventory, expansion, phase)
    count, target = len(qualified["sources"]), contract["source_target"]
    short = count < target["min"]
    action = "continue_collection" if phase == "pool" else "continue_expansion" if phase == "anchors" else "top_up_required" if short and attempt == "initial" else "return_shortfall" if short else "return_qualified"
    report = {"schema_version": 1, "status": "ok", "reference_sha256": {"journal_csv": file_hash(SKILL / "references/journals.csv")}, "phase": phase, "attempt": attempt, "action": action,
              "handoff_ready": phase == "final" and action != "top_up_required", "qualified_count": count,
              "target": target, "target_status": "below_minimum" if short else "above_target" if target["max"] is not None and count > target["max"] else "within_target",
              "shortfall": max(0, target["min"] - count), "top_up_used": attempt == "top_up", "decisions": decisions,
              "counts": {"considered": inventory.get("search_receipt", {}).get("considered_count"),
                         "candidate_records": len(inventory["sources"]),
                         "retrieved": sum(bool(s.get("provenance")) for s in inventory["sources"]), "qualified": count,
                         "disqualified": sum(d["status"] == "disqualified" for d in decisions.values()),
                         "unresolved": sum(d["status"] == "unresolved" for d in decisions.values())}}
    return qualified, rejected, normalized, render(qualified), report


def run_gate(args):
    contract, inventory = load(args.contract), load(args.inventory)
    if args.phase == "final" and args.attempt == "initial":
        require(not (args.output_dir / "source-gate.top_up.json").exists(), "Top-up already used; start a new invocation rather than resetting history")
    if args.attempt == "top_up" and (args.output_dir / "gate-input.top_up.json").exists():
        completed = load(args.output_dir / "gate-input.top_up.json")
        require(contract["search_passes"] == completed["contract"]["search_passes"]
                and {s["source_id"] for s in inventory["sources"]} == {s["source_id"] for s in completed["inventory"]["sources"]},
                "Top-up search/candidate set is frozen; replacement can repair metadata, not add another search pass")
    expansion = load(args.expansion) if args.expansion else None
    if args.attempt == "top_up":
        previous = load(args.output_dir / "source-gate.initial.json")
        snapshot = args.output_dir / "gate-input.initial.json"
        require(previous.get("phase") == "final" and previous.get("action") == "top_up_required"
                and previous.get("attempt") == "initial", "Top-up requires a recorded below-minimum first gate")
        require(previous.get("snapshot_sha256") == file_hash(snapshot), "First-attempt snapshot changed")
        first = load(snapshot)
        expected = evaluate(first["contract"], first["inventory"], first["expansion"], "initial", "final")[-1]
        require(all(previous.get(k) == v for k, v in expected.items()), "First-attempt receipt does not match its inputs")
        require(contract_core(contract) == contract_core(first["contract"]) and contract["search_passes"][0] == first["contract"]["search_passes"][0], "Top-up must preserve the original contract and initial search receipt")
        original_ids = {s["source_id"] for s in first["inventory"]["sources"]}
        require(original_ids <= {s["source_id"] for s in inventory["sources"]}, "Preserve every original raw candidate during top-up")
        require(all(s.get("search_pass") == "top_up" and s.get("discovery_level", "initial") == "initial" for s in inventory["sources"] if s["source_id"] not in original_ids),
                "New top-up records need initial discovery level and search_pass top_up")
    qualified, rejected, normalized, readable, receipt = evaluate(contract, inventory, expansion, args.attempt, args.phase)
    prefix = "pool-" if args.phase == "pool" else "anchor-" if args.phase == "anchors" else ""
    output = args.output_dir.resolve()
    paths = {"inventory": output / f"{prefix}sources.json", "excluded": output / f"{prefix}excluded-sources.json",
             "readable": output / f"{prefix}sources.md", "expansion": output / f"{prefix}qualified-expansion.json"}
    payloads = {paths["inventory"]: dump(qualified), paths["excluded"]: dump(rejected), paths["readable"]: readable,
                paths["expansion"]: dump(normalized)}
    receipt["input_sha256"] = {"contract": file_hash(args.contract), "inventory": file_hash(args.inventory), "expansion": file_hash(args.expansion) if args.expansion else None}
    receipt["input_paths"] = {"contract": str(args.contract.resolve()), "inventory": str(args.inventory.resolve()), "expansion": str(args.expansion.resolve()) if args.expansion else None}
    receipt["output_sha256"] = {k: digest(payloads[p]) for k, p in paths.items()}
    receipt["output_paths"] = {k: str(p) for k, p in paths.items()}
    snapshot = dump({"contract": contract, "inventory": inventory, "expansion": expansion})
    receipt["snapshot_sha256"] = digest(snapshot)
    name = "pool-gate.json" if args.phase == "pool" else "anchor-gate.json" if args.phase == "anchors" else "source-gate.json"
    payloads[output / name] = dump(receipt)
    if args.phase == "final":
        payloads[output / f"source-gate.{args.attempt}.json"] = dump(receipt)
        payloads[output / f"gate-input.{args.attempt}.json"] = snapshot
    protected = [args.contract, args.inventory] + ([args.expansion] if args.expansion else [])
    outputs = publish(payloads, args.replace, protected)
    return {**receipt, "outputs": outputs}


def validate_receipt(path, contract_path=None, inventory_path=None, expansion_path=None):
    receipt = load(path)
    require(isinstance(receipt, dict) and receipt.get("handoff_ready") is True, "Final literature gate is pending or requires its single top-up")
    paths = receipt["input_paths"]
    actual_paths = {"contract": contract_path, "inventory": inventory_path, "expansion": expansion_path}
    for name in ("contract", "inventory", "expansion"):
        saved = paths[name]
        require(actual_paths[name] is None or saved == str(Path(actual_paths[name]).resolve()), "Gate receipt points to unexpected project inputs")
        require((file_hash(saved) if saved else None) == receipt["input_sha256"][name], "Stale literature gate inputs")
    contract, inventory = load(paths["contract"]), load(paths["inventory"])
    expansion = load(paths["expansion"]) if paths["expansion"] else None
    snapshot = Path(path).parent / f"gate-input.{receipt['attempt']}.json"
    require(receipt.get("snapshot_sha256") == file_hash(snapshot)
            == digest(dump({"contract": contract, "inventory": inventory, "expansion": expansion})),
            "Current gate snapshot changed or differs from source inputs")
    expected = evaluate(contract, inventory, expansion, receipt["attempt"], receipt["phase"])
    report = expected[-1]
    require(all(receipt.get(k) == v for k, v in report.items()), "Gate receipt differs from qualified records")
    for name, data in zip(("inventory", "excluded", "expansion", "readable"), expected[:4]):
        content = data if name == "readable" else dump(data)
        require(digest(content) == receipt["output_sha256"][name] == file_hash(receipt["output_paths"][name]), "Stale or inconsistent final source list/data")
    if receipt["attempt"] == "top_up":
        first_path = Path(path).parent / "source-gate.initial.json"
        first = load(first_path)
        snap_path = Path(path).parent / "gate-input.initial.json"
        require(first.get("snapshot_sha256") == file_hash(snap_path) and first.get("action") == "top_up_required", "Top-up history missing/stale")
        initial = load(snap_path)
        original_ids = {s["source_id"] for s in initial["inventory"]["sources"]}
        require(original_ids <= {s["source_id"] for s in inventory["sources"]}
                and all(s.get("search_pass") == "top_up" and s.get("discovery_level", "initial") == "initial" for s in inventory["sources"] if s["source_id"] not in original_ids),
                "Top-up candidate provenance differs from recorded initial history")
        prior = evaluate(initial["contract"], initial["inventory"], initial["expansion"], "initial", "final")[-1]
        require(all(first.get(k) == v for k, v in prior.items()) and contract_core(contract) == contract_core(initial["contract"])
                and contract["search_passes"][0] == initial["contract"]["search_passes"][0], "Invalid top-up history/changed constraints")
    return receipt
