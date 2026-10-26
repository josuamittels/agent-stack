"""Deterministic checks for a completed Research skill invocation."""
import csv
import math
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "disciplines" / "spawn-evals" / "scripts"))
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
    return value.strip().casefold().replace("-", "_").replace(" ", "_")


def _title_key(value):
    return " ".join(re.findall(r"\w+", value.casefold())) if isinstance(value, str) else ""


def _load_journal_rows():
    path = ROOT / "disciplines" / "research-literature" / "references" / "journals.csv"
    with path.open(encoding="utf-8-sig", newline="") as source:
        return list(csv.DictReader(source))


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
