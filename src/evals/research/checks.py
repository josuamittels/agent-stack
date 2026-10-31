"""Deterministic checks for a completed Research skill invocation."""
import csv
import math
from pathlib import Path
import re
import sys
import json


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "skills" / "spawn-evals" / "scripts"))
import checklib  # noqa: E402


JOURNAL_WORK_TYPES = {"journal_article", "review"}


def _result(status, step, aspect, observed, expected, evidence):
    return {
        "status": status,
        "step": step,
        "aspect": aspect,
        "observed": observed,
        "expected": expected,
        "evidence": evidence,
    }


def _constraint(context, name):
    item = context.get("constraints", {}).get(name)
    if not isinstance(item, dict) or set(item) != {"value", "source"}:
        return None, None
    if item["source"] not in {"request", "skill_default"}:
        return None, None
    return item["value"], item["source"]


def _integer(value):
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _bounds(context, minimum_name, maximum_name):
    minimum, minimum_source = _constraint(context, minimum_name)
    maximum, maximum_source = _constraint(context, maximum_name)
    if not _integer(minimum) or (maximum is not None and not _integer(maximum)):
        return None
    if maximum is not None and maximum < minimum:
        return None
    return (minimum, maximum, minimum_source, maximum_source)


def _range_outcome(count, bounds):
    minimum, maximum = bounds[:2]
    return minimum <= count and (maximum is None or count <= maximum)


def check_report_word_range(context):
    bounds = _bounds(context, "word_count_min", "word_count_max")
    report = context.get("outputs", {}).get("report")
    if bounds is None or not isinstance(report, str):
        return _result("unverified", "report length", "word count input", None,
                       "word_count_min, word_count_max, and outputs.report with valid values",
                       ["/constraints/word_count_min", "/constraints/word_count_max", "/outputs/report"])
    count = checklib.word_count(report)
    minimum, maximum, minimum_source, maximum_source = bounds
    return _result(
        "pass" if _range_outcome(count, bounds) else "fail",
        "report length",
        "whitespace-delimited word count",
        {"count": count, "min_source": minimum_source, "max_source": maximum_source},
        {"min_inclusive": minimum, "max_inclusive": maximum},
        ["/outputs/report", "/constraints/word_count_min", "/constraints/word_count_max"],
    )


def check_cited_source_range(context):
    bounds = _bounds(context, "source_count_min", "source_count_max")
    sources = context.get("evidence", {}).get("sources")
    if bounds is None or not isinstance(sources, list):
        return _result("unverified", "source inventory", "cited-source count input", None,
                       "source_count_min, source_count_max, and evidence.sources with valid values",
                       ["/constraints/source_count_min", "/constraints/source_count_max", "/evidence/sources"])
    count = len(sources)
    minimum, maximum, minimum_source, maximum_source = bounds
    return _result(
        "pass" if _range_outcome(count, bounds) else "fail",
        "source inventory",
        "structured cited-source count",
        {"count": count, "min_source": minimum_source, "max_source": maximum_source},
        {"min_inclusive": minimum, "max_inclusive": maximum},
        ["/evidence/sources", "/constraints/source_count_min", "/constraints/source_count_max"],
    )


def _journal_config(context):
    names = {
        "preset": "journal_preset",
        "article_influence_min": "journal_article_influence_min",
        "influence_percentile_min": "journal_influence_percentile_min",
        "combination": "journal_combination",
        "filter_disabled": "journal_filter_disabled",
        "category": "journal_category",
        "exceptions": "journal_exceptions",
    }
    values, provenance = {}, {}
    for key, name in names.items():
        values[key], provenance[key] = _constraint(context, name)
        if name not in context.get("constraints", {}):
            return None, f"{name} constraint is missing"
        if provenance[key] is None:
            return None, f"{name} has invalid provenance"
    if values["preset"] not in {"lenient", "default", "strict", "custom", "disabled"}:
        return None, "journal-selection preset is invalid"
    if values["combination"] not in {"or", "and"} or type(values["filter_disabled"]) is not bool:
        return None, "journal-selection rule is invalid"
    if values["category"] is not None and not isinstance(values["category"], str):
        return None, "journal category must be a string or null"
    if values["category"] is not None and provenance["category"] != "request":
        return None, "journal category restrictions must come from an explicit request"
    exceptions = values["exceptions"]
    if not isinstance(exceptions, list) or any(not isinstance(item, str) or not item for item in exceptions):
        return None, "journal exceptions must be a list of source IDs"
    if len(exceptions) != len(set(exceptions)):
        return None, "journal exceptions contain duplicate source IDs"
    if exceptions and provenance["exceptions"] != "request":
        return None, "journal exceptions must come from an explicit request override"
    if values["filter_disabled"]:
        if provenance["filter_disabled"] != "request" or values["preset"] != "disabled" or provenance["preset"] != "request":
            return None, "disabling the journal filter must be an explicit request override"
        if values["article_influence_min"] is not None or values["influence_percentile_min"] is not None:
            return None, "disabled journal filtering cannot also define thresholds"
    else:
        if values["preset"] == "disabled":
            return None, "disabled preset requires filter_disabled true"
        if provenance["preset"] == "skill_default" and values["preset"] != "default":
            return None, "Research's default journal preset is default"
        if provenance["combination"] == "skill_default" and values["combination"] != "or":
            return None, "Research's default journal combination is or"
        if provenance["filter_disabled"] == "skill_default" and values["filter_disabled"] is not False:
            return None, "Research's default does not disable journal filtering"
        threshold_names = {
            "article_influence_min": ("journal_article_influence_min", None),
            "influence_percentile_min": ("journal_influence_percentile_min", 100),
        }
        for key, (name, maximum) in threshold_names.items():
            threshold = values[key]
            if threshold is not None:
                if isinstance(threshold, bool) or not isinstance(threshold, (int, float)):
                    return None, f"{key} must be numeric or null"
                if not math.isfinite(threshold) or threshold < 0 or (maximum is not None and threshold > maximum):
                    return None, f"{key} is outside its valid range"
        if values["article_influence_min"] is None and values["influence_percentile_min"] is None:
            return None, "at least one journal threshold is required"
        preset = checklib.JOURNAL_PRESETS.get(values["preset"])
        if values["preset"] in {"lenient", "default", "strict"} and preset is None:
            return None, "journal preset is unknown"
        for key, expected_value in (("article_influence_min", (preset or {}).get("article_influence")),
                                    ("influence_percentile_min", (preset or {}).get("influence_percentile"))):
            if provenance[key] == "skill_default" and values[key] != expected_value:
                return None, "skill-default threshold does not match the selected preset"
        if values["preset"] == "custom" and provenance["preset"] != "request":
            return None, "custom journal-selection rules must come from an explicit request"
    return {**values, "provenance": provenance}, None


def _sources(context):
    sources = context.get("evidence", {}).get("sources")
    if not isinstance(sources, list):
        return None, "evidence.sources must be a list"
    if any(not isinstance(source, dict) for source in sources):
        return None, "each source inventory entry must be an object"
    return sources, None


def _journal_type(source):
    value = source.get("publication_type")
    if not isinstance(value, str) or not value.strip():
        return None
    normalized = value.strip().casefold().replace("-", "_").replace(" ", "_")
    if source.get("journal_filter_applicable") is True or isinstance(source.get("csl"), dict) and source["csl"].get("type") == "article-journal":
        return "review" if normalized == "review" else "journal_article"
    return normalized


def _title_key(value):
    return " ".join(re.findall(r"\w+", value.casefold())) if isinstance(value, str) else ""


def _load_journal_rows():
    path = ROOT / "skills" / "research-literature" / "references" / "journals.csv"
    with path.open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


def _expansion_evidence(context):
    """Use the full frozen initial pool, never the cited-only inventory to count overlaps."""
    project = _project_evidence(context)
    if project is None:
        raise ValueError("project_dir is required for citation expansion evidence")
    sys.path.insert(0, str(ROOT / "skills/research/scripts"))
    from research_common import load
    from research_references import validate_expansion
    from research_project import accept_literature_gate
    brief = load(project / "brief.json")
    gate = accept_literature_gate(project, brief)
    if gate["output_paths"]["inventory"] != str((project / "sources.json").resolve()):
        raise ValueError("Gate inventory path differs from Research's canonical pool")
    brief = load(project / "brief.json")
    sources = load(project / "sources.json")["sources"]
    raw = load(project / "retrieved-sources.json")["sources"]
    path = project / "qualified-expansion.json"
    exemptions = validate_expansion(brief, sources, load(path) if path.exists() else None, raw_sources=raw)
    actual = {s["source_id"]: s for s in sources}
    for source in context.get("evidence", {}).get("sources", []):
        if actual.get(source.get("source_id")) != source:
            raise ValueError("Cited source differs from the current full project inventory")
    return exemptions


def check_literature_gate(context):
    evidence = ["/evidence/project_dir", "/evidence/sources"]
    project = _project_evidence(context)
    if project is None:
        return _result("unverified", "literature gate", "gate evidence", None,
                       "current, handoff-ready source qualification receipt", evidence)
    try:
        _expansion_evidence(context)
        from literature_common import load
        receipt = load(project / "source-gate.json")
        return _result("pass", "literature gate", "verified qualifying source pool",
                       {"qualified_count": receipt["qualified_count"], "action": receipt["action"], "shortfall": receipt["shortfall"]},
                       "qualified inventory and list match current inputs; any shortfall follows one top-up", evidence)
    except Exception as error:
        return _result("fail", "literature gate", "qualification/receipt consistency", str(error),
                       "current verified, journal-compliant inventory and bounded retry history", evidence)


def check_citation_expansion(context):
    evidence = ["/evidence/project_dir", "/evidence/sources"]
    if _project_evidence(context) is None:
        return _result("unverified", "citation expansion", "project evidence", None,
                       "full initial-pool citation graph and discovery depth", evidence)
    try:
        exemptions = _expansion_evidence(context)
        return _result("pass", "citation expansion", "frozen one-hop discovery",
                       {"overlap_exempt_source_ids": sorted(exemptions)},
                       "deep-only expansion with traced additions and distinct initial citing works", evidence)
    except Exception as error:
        return _result("fail", "citation expansion", "graph consistency", str(error),
                       "current, complete or explicitly partial citation expansion evidence", evidence)


def check_journal_selection(context):
    sources, issue = _sources(context)
    if issue:
        return _result("unverified", "journal selection", "source inventory", issue,
                       "evidence.sources list", ["/evidence/sources"])
    journal_sources = []
    unknown_types = []
    for index, source in enumerate(sources):
        kind = _journal_type(source)
        if kind is None:
            unknown_types.append(index)
        elif kind in JOURNAL_WORK_TYPES:
            journal_sources.append(source)
    if unknown_types:
        return _result("unverified", "journal selection", "publication type", unknown_types,
                       "publication_type for every source inventory entry", ["/evidence/sources"])
    if not journal_sources:
        return _result("not_applicable", "journal selection", "journal articles and reviews",
                       "no journal articles or reviews in the source inventory",
                       "applicable only to cited journal articles and reviews", ["/evidence/sources"])

    selection, issue = _journal_config(context)
    if issue:
        return _result("unverified", "journal selection", "resolved rule", issue,
                       "valid resolved journal-selection constraints", ["/constraints"])
    if selection["filter_disabled"]:
        return _result("pass", "journal selection", "explicitly disabled filter",
                       {"journal_sources": len(journal_sources), "provenance": selection["provenance"]},
                       "filter_disabled true from request", ["/constraints/journal_filter_disabled", "/evidence/sources"])

    try:
        rows = _load_journal_rows()
    except (OSError, csv.Error) as error:
        return _result("unverified", "journal selection", "score data availability",
                       type(error).__name__, "readable Research Literature journal CSV",
                       ["/constraints/journal_preset", "/evidence/sources"])

    exceptions = set(selection["exceptions"])
    results = []
    for index, item in enumerate(journal_sources):
        source_id = item.get("source_id")
        title = item.get("journal_title")
        issns = item.get("issns", [])
        if not isinstance(source_id, str) or not source_id:
            results.append({"status": "unverified", "source_index": index, "reason": "source_id missing"})
            continue
        if isinstance(item.get("secondary_discovery"), dict) and item["secondary_discovery"].get("journal_filter") == "overlap_exempt":
            try:
                exemption = _expansion_evidence(context).get(source_id)
                if exemption is None:
                    raise ValueError("No qualifying overlap exemption in frozen graph")
                results.append({"status": "pass", "source_id": source_id,
                                "reason": "deep backward-reference overlap exception",
                                "citing_source_ids": exemption["citing_source_ids"]})
            except Exception as error:
                results.append({"status": "fail", "source_id": source_id, "reason": str(error)})
            continue
        if source_id in exceptions:
            results.append({"status": "pass", "source_id": source_id, "reason": "explicit request exception"})
            continue
        if not isinstance(title, str) or not title.strip() or not isinstance(issns, list):
            results.append({"status": "unverified", "source_id": source_id, "reason": "journal identity missing"})
            continue
        matched = checklib.journal_rows(rows, title=title, issns=issns)
        if matched["status"] != "matched":
            results.append({"status": "unverified", "source_id": source_id,
                            "reason": "journal score row missing or ambiguous", "match_method": matched["method"]})
            continue
        if any(_title_key(row.get("journal", "")) != _title_key(title) for row in matched["rows"]):
            results.append({"status": "unverified", "source_id": source_id,
                            "reason": "ISSN match conflicts with supplied journal title", "match_method": matched["method"]})
            continue
        qualification = checklib.journal_qualification(
            matched["rows"],
            article_influence=selection["article_influence_min"],
            influence_percentile=selection["influence_percentile_min"],
            category=selection["category"],
            combination=selection["combination"],
        )
        results.append({
            "status": qualification["status"],
            "source_id": source_id,
            "journal_title": title,
            "match_method": matched["method"],
            "score_rows": matched["rows"],
            "qualification": qualification["reason"] if "reason" in qualification else qualification["branch"],
        })

    statuses = [item["status"] for item in results]
    status = "fail" if "fail" in statuses else "unverified" if "unverified" in statuses else "pass"
    expected = {
        "preset": selection["preset"],
        "article_influence_min": selection["article_influence_min"],
        "influence_percentile_min": selection["influence_percentile_min"],
        "combination": selection["combination"],
        "category": selection["category"],
        "inclusive": True,
        "provenance": selection["provenance"],
    }
    return _result(status, "journal selection", "cited journal eligibility",
                   results, expected, ["/constraints", "/evidence/sources"])


def check_article_links(context):
    sources, issue = _sources(context)
    if issue:
        return _result("unverified", "article link reachability", "source inventory", issue,
                       "evidence.sources list", ["/evidence/sources"])
    articles = []
    unknown_types = []
    for index, source in enumerate(sources):
        kind = _journal_type(source)
        if kind is None:
            unknown_types.append(index)
        elif kind in JOURNAL_WORK_TYPES:
            articles.append(source)
    if unknown_types:
        return _result("unverified", "article link reachability", "publication type", unknown_types,
                       "publication_type for every source inventory entry", ["/evidence/sources"])
    if not articles:
        return _result("not_applicable", "article link reachability", "journal article URLs",
                       "no journal articles or reviews in the source inventory",
                       "applicable only to cited journal articles and reviews", ["/evidence/sources"])
    results = []
    for index, article in enumerate(articles):
        source_id = article.get("source_id", f"source-index:{index}")
        url = article.get("article_url")
        if not isinstance(url, str) or not url.strip():
            results.append({"status": "unverified", "source_id": source_id, "reason": "article_url missing"})
            continue
        try:
            check = checklib.url_reachable(url)
        except Exception as error:  # Network and URL handlers can fail in environment-specific ways.
            results.append({"status": "unverified", "source_id": source_id,
                            "url": url, "reason": type(error).__name__})
            continue
        results.append({"status": check["status"], "source_id": source_id, "url": url,
                        "status_code": check.get("status_code"), "final_url": check.get("final_url"),
                        "reason": check.get("detail")})
    statuses = [item["status"] for item in results]
    status = "fail" if "fail" in statuses else "unverified" if "unverified" in statuses else "pass"
    return _result(status, "article link reachability", "cited journal article URLs", results,
                   "all journal article and review URLs resolve with HTTP 2xx or 3xx",
                   ["/evidence/sources"])


def _project_evidence(context):
    """Read current helper artifacts; missing old-style invocation evidence stays unverified."""
    value = context.get("evidence", {}).get("project_dir")
    if not isinstance(value, str) or not value:
        return None
    return Path(value)


def check_citation_inventory(context):
    evidence = ["/evidence/project_dir", "/evidence/sources", "/outputs/report"]
    project = _project_evidence(context)
    if project is None:
        return _result("unverified", "citation consistency", "project artifacts", None,
                       "current Research project evidence", evidence)
    sys.path.insert(0, str(ROOT / "skills/research/scripts"))
    try:
        from research_common import citation_ids, file_hash, load, parse_markdown, walk
        from research_render import bibliography, citation_key
        sources = load(project / "sources.json")["sources"]
        receipt = load(project / "citation-receipt.json")
        actual_keys = citation_ids(parse_markdown((project / "draft.md").read_text(encoding="utf-8")))
        cited = context.get("evidence", {}).get("sources")
        if not isinstance(cited, list) or not isinstance(context.get("outputs", {}).get("report"), str):
            return _result("unverified", "citation consistency", "cited inventory/report", None,
                           "cited source records and full report text", evidence)
        key_map = {s["source_id"]: citation_key(s["source_id"]) for s in sources}
        expected_ids = [s["source_id"] for s in sources if key_map[s["source_id"]] in actual_keys]
        compiled = (project / "report.md").read_text(encoding="utf-8")
        report_ast = parse_markdown(compiled)
        reference_keys = [n["c"][0][0][4:] for n in walk(report_ast)
                          if n.get("t") == "Div" and n["c"][0][0].startswith("ref-")]
        valid = (len(sources) == len(key_map) and bool(actual_keys)
                 and set(actual_keys) <= set(key_map.values())
                 and receipt.get("key_map") == key_map
                 and receipt.get("cited_keys") == actual_keys
                 and receipt.get("cited_source_ids") == expected_ids
                 and sorted(s["source_id"] for s in cited) == sorted(expected_ids)
                 and len(reference_keys) == len(actual_keys) and set(reference_keys) == set(actual_keys)
                 and receipt.get("draft_sha256") == file_hash(project / "draft.md")
                 and receipt.get("sources_sha256") == file_hash(project / "sources.json")
                 and receipt.get("report_sha256") == file_hash(project / "report.md")
                 and context["outputs"]["report"] == compiled
                 and load(project / "bibliography.json") == bibliography(sources)
                 and load(project / "cited-sources.json") == cited)
        return _result("pass" if valid else "fail", "citation consistency", "manuscript, bibliography and cited inventory",
                       {"cited_keys": actual_keys, "cited_source_ids": expected_ids, "reference_keys": reference_keys},
                       "one current bibliographic entry per cited key, matching inventory and hashes", evidence)
    except Exception as error:
        return _result("unverified", "citation consistency", "artifact parsing/dependency", type(error).__name__,
                       "readable current artifacts and available Pandoc", evidence)


def check_requested_formats(context):
    evidence = ["/constraints/requested_formats", "/evidence/project_dir", "/evidence/exports"]
    formats, provenance = _constraint(context, "requested_formats")
    project = _project_evidence(context)
    exports = context.get("evidence", {}).get("exports")
    if project is None or provenance is None or not isinstance(formats, list) or not formats or not isinstance(exports, list):
        return _result("unverified", "requested formats", "format constraints/conversion receipts", None,
                       "requested_formats with provenance and current project/export evidence", evidence)
    if any(f not in {"chat", "md", "latex", "pdf", "docx"} for f in formats):
        return _result("fail", "requested formats", "supported formats", formats,
                       "chat, md, latex, pdf, docx", evidence)
    sys.path.insert(0, str(ROOT / "skills/research/scripts"))
    results = []
    try:
        from research_common import file_hash, headers, load, parse_markdown, walk
        from research_render import docx_signature
        report = project / "report.md"
        ast = parse_markdown(report.read_text(encoding="utf-8"))
        counts = {kind: sum(n.get("t") == kind for n in walk(ast)) for kind in ["Table", "Math", "Image"]}
        for fmt in formats:
            if fmt in {"chat", "md"}:
                results.append({"format": fmt, "status": "pass" if context.get("outputs", {}).get("report") == report.read_text(encoding="utf-8") else "fail"})
                continue
            found = [e for e in exports if e.get("format") == fmt]
            if not found:
                results.append({"format": fmt, "status": "unverified", "reason": "conversion receipt missing"})
                continue
            item = found[-1]
            path = Path(item["output"])
            if not path.is_file():
                results.append({"format": fmt, "status": "unverified", "reason": "output inaccessible"})
                continue
            valid = (item.get("input_sha256") == file_hash(report)
                     and item.get("output_sha256") == file_hash(path) and item.get("features") == counts)
            for asset in item.get("asset_inputs", []):
                asset_path = Path(asset["path"])
                valid = valid and asset_path.is_file() and file_hash(asset_path) == asset["sha256"]
            if fmt == "docx":
                signature = docx_signature(path)
                valid = valid and signature["tables"] >= counts["Table"] and signature["math"] >= counts["Math"]
                valid = valid and signature["images"] >= counts["Image"]
                valid = valid and all(h in signature["text"] for h in headers(ast))
            elif fmt == "pdf":
                valid = valid and path.read_bytes().startswith(b"%PDF-") and item.get("backend") == "pandoc-docx+libreoffice"
                try:
                    from pypdf import PdfReader
                except ImportError:
                    results.append({"format": fmt, "status": "unverified", "reason": "pypdf unavailable for PDF page/text inspection"})
                    continue
                pdf = PdfReader(path)
                text = " ".join(" ".join((p.extract_text() or "").split()) for p in pdf.pages)
                # Some subset fonts expose corrupt text mappings despite correct visible glyphs.
                # Page/text presence is mechanical; layout/content fidelity still needs the recorded visual review.
                valid = valid and bool(pdf.pages) and bool(text.strip())
            else:
                text = path.read_text(encoding="utf-8")
                valid = valid and "\\begin{document}" in text and "\\end{document}" in text
                for asset in item.get("asset_outputs", []):
                    asset_path = Path(asset["path"])
                    valid = valid and asset_path.is_file() and file_hash(asset_path) == asset["sha256"]
            state = "pass" if valid else "fail"
            if valid and fmt in {"pdf", "docx"} and not (item.get("visual_review") == "complete" and item.get("visual_review_evidence")):
                state = "unverified"
            results.append({"format": fmt, "status": state})
    except Exception as error:
        return _result("unverified", "requested formats", "artifact inspection", type(error).__name__,
                       "readable current conversions and dependencies", evidence)
    statuses = [r["status"] for r in results]
    status = "fail" if "fail" in statuses else "unverified" if "unverified" in statuses else "pass"
    return _result(status, "requested formats", "report-to-export consistency", results,
                   "requested formats preserve current report revision and supported structures; binary layout review recorded", evidence)
