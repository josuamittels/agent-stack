"""Fixed project scaffolding, artifact validation and loss-aware assembly."""
from __future__ import annotations

from research_references import validate_expansion

from pathlib import Path
import re

from research_common import (FORMATS, TEMPLATES, dump, file_hash, headers, inside,
                             load, parse_markdown, publish, reject_pending, require, template)

DEPTHS = {"quick": (800, 1600, 8, 12), "normal": (2000, 4000, 16, 24),
          "deep": (6000, None, 32, 64)}
PRESETS = {"lenient": (1.0, 60), "default": (2.5, 80), "strict": (5.0, 90)}
REVIEW_CHECKS = {
    "argument": ["question_answered", "claim_strength", "counterevidence", "cross_section_consistency", "outside_check"],
    "citation": ["source_identity", "claim_support", "quotations_and_numbers", "locators", "bibliography"],
}
STAGES = ["brief", "discovery", "evidence", "outline", "draft", "review", "final"]


def structures(document_type):
    rows = template("structures.json")["types"]
    require(document_type in rows, f"Unsupported document type: {document_type}")
    return rows[document_type]


def constraint(value, source="skill_default"):
    return {"value": value, "source": source}


def init_project(args):
    project = args.project.resolve()
    require(args.topic.strip(), "Topic cannot be empty")
    formats = list(dict.fromkeys((args.formats or "chat").split(",")))
    require(set(formats) <= FORMATS and formats, "Formats must be chat,md,latex,pdf,docx")
    requested = [("work", value) for value in args.source] + [("author", value) for value in args.author]
    require(all(value.strip() for _, value in requested), "Source/author inputs cannot be empty")
    source_requests = [{"request_id": f"input-{index:03d}", "kind": kind, "input": value}
                       for index, (kind, value) in enumerate(requested, 1)]
    if args.resume:
        manifest = load(project / "manifest.json")
        brief = load(project / "brief.json")
        require(brief["topic"] == args.topic and brief["document_type"] == args.type,
                "Resume topic/type differs from existing project")
        require(not source_requests or brief.get("source_requests", []) == source_requests,
                "Resume source/author inputs differ; edit and reconcile the existing brief explicitly")
        for relative in manifest["artifacts"] + [s["path"] for s in manifest["sections"]]:
            require(inside(project, relative).is_file(), f"Resume artifact missing: {relative}")
        return {"project": str(project), "resumed": True, "outputs": []}
    require(not project.exists(), f"Project exists: {project}; use --resume", "output_exists")
    brief = template("brief.json")
    brief.update(document_type=args.type, topic=args.topic, request=args.request or args.topic,
                 question=args.topic, language=args.language, depth=args.depth,
                 formats=formats, citation_style=args.style if args.style in {"apa", "apa7"} else str(Path(args.style).expanduser().resolve()))
    brief["source_requests"] = source_requests
    bounds = DEPTHS[args.depth]
    names = ["word_count_min", "word_count_max", "source_count_min", "source_count_max"]
    brief["constraints"] = {n: constraint(v) for n, v in zip(names, bounds)}
    preset = args.journal_preset or "default"
    scores = PRESETS[preset]
    brief["constraints"].update({
        "journal_preset": constraint(preset, "request" if args.journal_preset else "skill_default"),
        "journal_article_influence_min": constraint(scores[0]),
        "journal_influence_percentile_min": constraint(scores[1]),
        "journal_combination": constraint("or"), "journal_filter_disabled": constraint(False),
        "journal_category": constraint(None), "journal_exceptions": constraint([]),
        "requested_formats": constraint(formats, "request" if args.formats is not None else "skill_default"),
    })
    manifest = template("manifest.json")
    manifest["document_type"] = args.type
    sections = []
    files = {project / name: dump(template(name))
             for name in ["sources.json", "appraisals.json", "claims.json", "citation-candidates.json"]}
    contract = load(TEMPLATES.parent.parent / "research-literature/templates/contract.json")
    contract.update(depth=args.depth, source_target={"min": bounds[2], "max": bounds[3], "source": "skill_default"},
                    constraints={k: v for k, v in brief["constraints"].items() if k.startswith("journal_")}, source_requests=source_requests)
    files[project / "literature-contract.json"] = dump(contract)
    files[project / "retrieved-sources.json"] = dump(template("sources.json"))
    files[project / "source-gate.json"] = dump(template("source-gate.json"))
    for index, row in enumerate(structures(args.type), 1):
        relative = f"sections/{index:02d}-{row['id']}.md"
        item = {**row, "path": relative, "source_ids": [], "claim_ids": [],
                "word_budget": {"min": None, "max": None}, "context": None}
        sections.append(item)
        files[project / relative] = (f"## {row['heading']}\n\n::: {{#refs}}\n:::\n"
                                    if row["id"] == "references" else
                                    (TEMPLATES / "section.md").read_text().replace("{{heading}}", row["heading"])
                                    .replace("{{purpose}}", row["purpose"]))
    manifest["sections"] = [{k: v for k, v in s.items() if k in {"id", "heading", "path"}} for s in sections]
    files.update({project / "brief.json": dump(brief), project / "manifest.json": dump(manifest),
                  project / "outline.json": dump({"schema_version": 1, "status": "pending", "sections": sections}),
                  project / "exports.json": dump({"schema_version": 1, "exports": []})})
    for kind in REVIEW_CHECKS:
        review = template("review.json")
        review.update(review_type=kind, checks={key: {"status": "pending", "evidence": []}
                                               for key in REVIEW_CHECKS[kind]})
        files[project / f"{kind}-review.json"] = dump(review)
    return {"project": str(project), "outputs": publish(files)}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def review_inputs(project):
    names = ["brief.json", "sources.json", "appraisals.json", "claims.json", "outline.json"]
    for name in ["citation-candidates.json", "source-gate.json", "literature-contract.json", "retrieved-sources.json", "qualified-expansion.json"]:
        if (project / name).exists():
            names.append(name)
    return {name: file_hash(project / name) for name in names}


def records(project):
    obj = load(project / "sources.json")
    require(obj.get("schema_version") == 1 and isinstance(obj.get("sources"), list), "sources.json requires schema_version 1 and sources[]")
    seen = set()
    for source in obj["sources"]:
        require(isinstance(source, dict), "Each source must be an object")
        sid = source.get("source_id")
        require(nonempty(sid) and sid not in seen, f"Missing or duplicate source_id: {sid}")
        seen.add(sid)
        require(nonempty(source.get("title")) and nonempty(source.get("publication_type")), f"Missing source title/type: {sid}")
        require(isinstance(source.get("provenance"), list) and source["provenance"], f"Missing retrieval provenance: {sid}")
        require(all(isinstance(p, dict) and nonempty(p.get("provider")) and nonempty(p.get("record_url"))
                    for p in source["provenance"]), f"Provenance needs provider and actual record_url: {sid}")
    return obj


def layout(project, brief):
    manifest = load(project / "manifest.json")
    outline = load(project / "outline.json")
    expected = structures(brief["document_type"])
    require(manifest.get("schema_version") == 1 and manifest.get("document_type") == brief["document_type"], "Manifest type/schema mismatch")
    require(isinstance(manifest.get("sections"), list) and len(manifest["sections"]) == len(expected), "Manifest section count changed")
    require(isinstance(outline.get("sections"), list) and len(outline["sections"]) == len(expected), "Outline section count changed")
    paths = set()
    for index, (actual, mapped, base) in enumerate(zip(outline["sections"], manifest["sections"], expected), 1):
        for item in [actual, mapped]:
            require(item.get("id") == base["id"] and item.get("heading") == base["heading"], "Section IDs, headings and order must match the selected template")
        require(actual.get("path") == mapped.get("path"), "Outline/manifest paths differ")
        require(mapped["path"] == f"sections/{index:02d}-{base['id']}.md", "Section paths must match the initialized template")
        path = inside(project, mapped["path"])
        require(path not in paths and path.is_file(), f"Missing/duplicate section path: {path}")
        paths.add(path)
    return outline


def accept_literature_gate(project, brief):
    """Accept only the current filtered pool under the Research caller's rules."""
    project = Path(project).resolve()
    from literature_gate import validate_receipt
    gate = validate_receipt(project / "source-gate.json", project / "literature-contract.json", project / "retrieved-sources.json",
                            project / "citation-candidates.json" if brief["depth"] == "deep" else None)
    require(gate["output_paths"]["inventory"] == str(project / "sources.json"), "Gate does not qualify this project's canonical inventory")
    contract = load(project / "literature-contract.json")
    require(contract["depth"] == brief["depth"] and contract["source_requests"] == brief.get("source_requests", [])
            and all(contract["constraints"][k] == v for k, v in brief["constraints"].items() if k.startswith("journal_")),
            "Literature contract differs from Research brief; reconcile and rerun gate")
    return gate


def validate_project(project, stage, executable=None):
    project = Path(project).resolve()
    require(stage in STAGES, "Unknown validation stage")
    level = STAGES.index(stage)
    brief = load(project / "brief.json")
    require(brief.get("schema_version") == 1 and brief.get("depth") in DEPTHS, "Invalid brief schema/depth")
    structures(brief.get("document_type"))
    for key in ["topic", "request", "question", "scope", "audience", "language", "method"]:
        require(nonempty(brief.get(key)), f"Complete brief.{key}", "incomplete_phase")
    require(brief.get("status") == "complete", "Brief is pending", "incomplete_phase")
    require(isinstance(brief.get("formats"), list) and brief["formats"] and set(brief["formats"]) <= FORMATS, "Invalid requested formats")
    for name in ["word_count_min", "word_count_max", "source_count_min", "source_count_max",
                 "journal_preset", "journal_article_influence_min", "journal_influence_percentile_min",
                 "journal_combination", "journal_filter_disabled", "journal_category", "journal_exceptions", "requested_formats"]:
        entry = brief.get("constraints", {}).get(name)
        require(isinstance(entry, dict) and set(entry) == {"value", "source"}
                and entry["source"] in {"request", "skill_default"}, f"Invalid/missing constraint provenance: {name}")
    for lower, upper in [("word_count_min", "word_count_max"), ("source_count_min", "source_count_max")]:
        lo, hi = [brief["constraints"][k]["value"] for k in (lower, upper)]
        require(type(lo) is int and lo >= 0 and (hi is None or type(hi) is int and hi >= lo), f"Invalid bounds: {lower}/{upper}")
    require(brief["constraints"]["requested_formats"]["value"] == brief["formats"], "Requested-format constraint differs from brief.formats")
    requests = brief.get("source_requests", [])
    require(isinstance(requests, list), "brief.source_requests must be an array")
    request_ids = set()
    for item in requests:
        require(isinstance(item, dict) and nonempty(item.get("request_id"))
                and item["request_id"] not in request_ids and item.get("kind") in {"work", "author"}
                and nonempty(item.get("input")), "Invalid/duplicate requested source or author")
        request_ids.add(item["request_id"])
    if level == 0:
        return {"stage": stage, "outputs": []}
    inventory = records(project)
    require(inventory.get("search_receipt", {}).get("status") in {"complete", "partial", "blocked"}, "Search receipt is pending")
    outcomes = inventory.get("search_receipt", {}).get("requested_inputs", [])
    require(isinstance(outcomes, list), "search_receipt.requested_inputs must be an array")
    outcome_ids = set()
    source_ids = {s["source_id"] for s in inventory["sources"]}
    for outcome in outcomes:
        require(isinstance(outcome, dict), "Requested-input outcome must be an object")
        rid = outcome.get("request_id")
        require(rid in request_ids and rid not in outcome_ids, "Unknown/duplicate requested-input outcome")
        outcome_ids.add(rid)
        require(outcome.get("status") in {"eligible", "excluded", "unresolved", "no_eligible_works"}
                and nonempty(outcome.get("reason")), f"Pending/missing requested-input disposition: {rid}")
        searches = outcome.get("searches")
        require(isinstance(searches, list) and searches and all(nonempty(s) for s in searches),
                f"Record actual lookup/search attempts for {rid}")
        matches = outcome.get("source_ids")
        require(isinstance(matches, list) and all(nonempty(s) and s in source_ids for s in matches)
                and len(matches) == len(set(matches)), f"Invalid requested-input source IDs: {rid}")
        require(outcome["status"] != "eligible" or matches, f"Eligible request requires retrieved sources: {rid}")
    require(outcome_ids == request_ids, "Account for every supplied paper/author in search_receipt.requested_inputs")
    require(inventory["sources"], "No retrieved source pool; report discovery limits instead of drafting")
    accept_literature_gate(project, brief)
    ids = {s["source_id"] for s in inventory["sources"]}
    if level == 1:
        return {"stage": stage, "source_count": len(ids), "outputs": []}
    appraisals, claims = load(project / "appraisals.json"), load(project / "claims.json")
    require(appraisals.get("schema_version") == claims.get("schema_version") == 1, "Appraisal/claim schema must be 1")
    require(appraisals.get("status") == claims.get("status") == "complete", "Complete appraisals and claims before structuring")
    found = set()
    reviewed = set()
    for item in appraisals.get("appraisals", []):
        sid = item.get("source_id")
        require(sid in ids and sid not in reviewed, f"Unknown/duplicate appraisal source: {sid}")
        reviewed.add(sid)
        require(item.get("inspection") in {"full_text", "abstract", "metadata"}, f"Invalid inspection basis: {sid}")
        require(isinstance(item.get("limitations"), list), f"Missing limitations list: {sid}")
        require(isinstance(item.get("findings"), list), f"Missing findings list: {sid}")
        for finding in item.get("findings", []):
            fid = finding.get("finding_id")
            require(nonempty(fid) and (sid, fid) not in found and nonempty(finding.get("text")) and nonempty(finding.get("locator")), f"Invalid/duplicate finding: {sid}/{fid}")
            require(item["inspection"] != "metadata", "Metadata-only inspection cannot support extracted findings")
            found.add((sid, fid))
    claim_ids = set()
    for claim in claims.get("claims", []):
        cid = claim.get("claim_id")
        require(nonempty(cid) and cid not in claim_ids and nonempty(claim.get("text")), "Invalid/duplicate claim")
        claim_ids.add(cid)
        require(claim.get("status") in {"supported", "qualified"} and claim.get("supports"), f"Claim needs evidence or removal: {cid}")
        require(claim["status"] != "qualified" or nonempty(claim.get("qualification")), f"Qualified claim needs its qualification: {cid}")
        for side in ["supports", "contradicts"]:
            require(isinstance(claim.get(side), list), f"Missing {side} list: {cid}")
            for ref in claim[side]:
                require((ref.get("source_id"), ref.get("finding_id")) in found, f"Unknown finding in claim {cid}")
    require(claim_ids, "Claims ledger is empty")
    if level == 2:
        return {"stage": stage, "claim_count": len(claim_ids), "outputs": []}
    outline = layout(project, brief)
    require(outline.get("schema_version") == 1 and outline.get("status") == "complete", "Outline schema invalid or pending")
    for row in outline["sections"]:
        require(nonempty(row.get("purpose")), "Section purpose missing")
        require(nonempty(row.get("context")), "Every section requires neighboring context or a stated standalone role")
        require(isinstance(row.get("source_ids"), list) and set(row["source_ids"]) <= ids, "Unknown outline source IDs")
        require(isinstance(row.get("claim_ids"), list) and set(row["claim_ids"]) <= claim_ids, "Unknown outline claim IDs")
        assigned = [c for c in claims["claims"] if c["claim_id"] in row["claim_ids"]]
        required_sources = {ref["source_id"] for c in assigned for side in ["supports", "contradicts"] for ref in c[side]}
        require(required_sources <= set(row["source_ids"]), "Section source assignments omit evidence for assigned claims")
        if row["id"] in {"findings", "synthesis"}:
            require(row["source_ids"] and row["claim_ids"], "Synthesis sections need explicit source and claim assignments")
        budget = row.get("word_budget", {})
        require(type(budget.get("min")) is int and budget["min"] >= 0 and type(budget.get("max")) is int and budget["max"] >= budget["min"], "Every section requires an inclusive integer word budget")
    if level == 3:
        return {"stage": stage, "outputs": []}
    draft = project / "draft.md"
    require(draft.is_file(), "Assemble draft.md first")
    ast = parse_markdown(draft.read_text(encoding="utf-8"), executable)
    reject_pending(ast)
    require(headers(ast) == [r["heading"] for r in structures(brief["document_type"])], "Draft top-level structure differs from selected template")
    if level == 4:
        return {"stage": stage, "draft_sha256": file_hash(draft), "inputs_sha256": review_inputs(project), "outputs": []}
    for kind, required_checks in REVIEW_CHECKS.items():
        review = load(project / f"{kind}-review.json")
        require(review.get("schema_version") == 1 and review.get("review_type") == kind and review.get("status") == "complete", f"Pending/invalid {kind} review")
        require(type(review.get("repair_passes")) is int and 0 <= review["repair_passes"] <= 2, "At most two substantive repair passes")
        require(review.get("draft_sha256") == file_hash(draft), f"Stale {kind} review; review the current draft")
        require(review.get("inputs_sha256") == review_inputs(project), f"Stale {kind} review evidence; recheck changed brief/sources/appraisals/claims/outline")
        for key in required_checks:
            check = review.get("checks", {}).get(key, {})
            require(check.get("status") in {"checked", "not_applicable"} and isinstance(check.get("evidence"), list)
                    and all(nonempty(e) for e in check["evidence"]) and check["evidence"], f"Review evidence missing for {kind}/{key}")
        for issue in review.get("issues", []):
            require(all(nonempty(issue.get(k)) for k in ["issue_id", "passage", "problem"]), "Review issues require ID, passage and problem")
            require(issue.get("severity") in {"critical", "major", "minor"} and issue.get("status") in {"open", "resolved"}, "Invalid review issue status/severity")
            require(issue["status"] == "resolved" or issue["severity"] == "minor", f"Unresolved blocker: {issue['issue_id']}")
            require(issue["status"] != "resolved" or nonempty(issue.get("correction")), "Resolved issues require an actual correction")
    require(nonempty(brief.get("outside_check", {}).get("observed")), "Record the outside check's observed result")
    if level == 5:
        return {"stage": stage, "outputs": []}
    receipt = load(project / "citation-receipt.json")
    require(receipt.get("schema_version") == 1 and receipt.get("status") == "ok"
            and isinstance(receipt.get("cited_source_ids"), list) and receipt["cited_source_ids"], "Incomplete citation receipt")
    cited_records = load(project / "cited-sources.json")
    require(isinstance(cited_records, list) and [s["source_id"] for s in cited_records] == receipt["cited_source_ids"], "Cited inventory differs from citation receipt")
    require(set(receipt.get("cited_source_ids", [])) <= reviewed, "Cited sources require an appraisal with actual inspection basis")
    require(receipt.get("draft_sha256") == file_hash(draft) and receipt.get("sources_sha256") == file_hash(project / "sources.json"), "Citations stale after draft/source changes")
    require(receipt.get("report_sha256") == file_hash(project / "report.md"), "Compiled report changed; recompile")
    export_list = load(project / "exports.json").get("exports", [])
    for fmt in brief["formats"]:
        if fmt in {"chat", "md"}:
            continue
        matches = [e for e in export_list if e.get("format") == fmt and e.get("input_sha256") == receipt["report_sha256"]]
        require(matches, f"Missing/current {fmt} export")
        output = Path(matches[-1]["output"])
        require(output.is_file() and file_hash(output) == matches[-1]["output_sha256"], f"Missing/changed export: {output}")
        for asset in matches[-1].get("asset_inputs", []) + matches[-1].get("asset_outputs", []):
            path = Path(asset["path"])
            require(path.is_file() and file_hash(path) == asset["sha256"], f"Missing/changed export asset: {path}")
        if fmt in {"docx", "pdf"}:
            require(matches[-1].get("visual_review") == "complete" and matches[-1].get("visual_review_evidence"), f"Record actual rendered page review for {fmt}")
    return {"stage": stage, "outputs": [], "draft_sha256": file_hash(draft)}


def assemble_project(args):
    project = args.project.resolve()
    validate_project(project, "outline", args.pandoc)
    brief = load(project / "brief.json")
    outline = layout(project, brief)
    chunks = []
    for row in outline["sections"]:
        text = inside(project, row["path"]).read_text(encoding="utf-8")
        ast = parse_markdown(text, args.pandoc)
        reject_pending(ast)
        require(headers(ast) == [row["heading"]], f"Wrong or duplicate section heading in {row['path']}")
        require(not any(n.get("t") == "Header" and n["c"][0] == 1 for n in ast["blocks"]), "Section files cannot redefine the report title")
        require(row["id"] == "references" or len(ast["blocks"]) > 1, f"Empty section: {row['id']}")
        chunks.append(text.strip())
    # Title is a single plain-text heading; do not let input inject Markdown structure.
    title = re.sub(r"([\\`*_{}\[\]<>#!])", r"\\\1", brief["topic"].replace("\n", " "))
    manuscript = "# " + title + "\n\n" + "\n\n".join(chunks) + "\n"
    output = project / "draft.md"
    outputs = publish({output: manuscript}, args.replace)
    return {"outputs": outputs, "draft_sha256": file_hash(output), "canonical": str(output)}
