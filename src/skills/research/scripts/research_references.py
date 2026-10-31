"""Research adapters for Literature-owned identity, journal and citation mechanics."""
from __future__ import annotations
from functools import wraps
from pathlib import Path
import sys

from research_common import ResearchError, dump, load, publish, require
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "research-literature/scripts"))
import literature_shared as shared
from literature_common import LiteratureError


def adapt(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except LiteratureError as exc:
            raise ResearchError(exc.code, str(exc)) from exc
    return wrapped


aliases = adapt(shared.aliases)
graph = adapt(shared.graph)
journal_qualifies = adapt(shared.journal_qualifies)
validate_expansion = adapt(shared.validate_expansion)


def rank_references(args):
    project = args.project.resolve()
    brief = load(project / "brief.json")
    require(isinstance(brief, dict) and brief.get("depth") == "deep", "Reference expansion is deep-only")
    ranked = graph(load(args.inventory or project / "sources.json")["sources"])
    path = project / "citation-candidates.json"
    if path.exists():
        previous = load(path)
        require(isinstance(previous, dict), "Citation candidate artifact must be an object")
        if previous.get("status") != "pending":
            require(previous.get("initial_source_ids") == ranked["initial_source_ids"], "Initial pool is frozen; do not add or relabel expansion seeds")
        else:
            # The initialized pending scaffold is the only implicit replacement.
            require(previous == {"schema_version": 1, "status": "pending", "initial_source_ids": [], "candidates": [], "limits": []}, "Modified pending ranking scaffold; use explicit replacement")
            return {"outputs": publish({path: dump(ranked)}, replace=True), "candidates": len(ranked["candidates"])}
    return {"outputs": publish({path: dump(ranked)}, replace=args.replace), "candidates": len(ranked["candidates"])}
