---
name: "secondary-discovery"
description: "Deep-only backward-reference retrieval, overlap ranking, journal exceptions, and caller handoff."
version: "0.1.2"
created: "2026-10-31"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "OpenAlex"
  - "Crossref"
  - "Allen Institute for AI"
  - "National Library of Medicine"
type: "reference"
status: "experimental"
---

# Deep secondary discovery

Read for deep research only. This procedure expands one backward-citation hop from the initial included pool. Quick/normal research does not automatically expand citations. Secondary describes discovery level; a secondary-level addition may itself be a primary study.

## Retrieve reference lists

For a staged Research invocation, return initial results first, then resume this procedure when Research supplies the finished combined initial pool, including any separately retrieved official/grey sources. Preserve the existing topic searches and supplied-input outcomes rather than replacing them. Direct deep requests complete both rounds in one workflow.

Qualify initial candidates with the gate in anchor phase, then freeze only its deduplicated verified qualifying work IDs. Keep disqualified/unresolved candidates in the raw ledger. Preserve records for confirmed versions under a common identity; multiple database records or versions of one citing work count once. Explicitly supplied papers belong to this initial pool only if they passed initial inclusion. For a Research project, the first `rank-references --inventory anchor-sources.json` run freezes those source IDs; subsequent runs cannot introduce new initial seeds.

Attempt backward-reference retrieval for every initial work. Use the provider's local instructions for request fields, pagination, access restrictions and bounded retries:

| Provider | Backward-reference operation | Limits to preserve |
| --- | --- | --- |
| OpenAlex | Include `referenced_works` in the initial work `select`, or retrieve that work with this field. Resolve its returned work IDs using the [exact/batch lookup procedure](openalex-docs.md#identity-lookup-and-citation-links). | Matched index references may be incomplete; retain original IDs before fetching targets. |
| Crossref | Retrieve `/works/<doi>` and retain deposited `reference[]`, including DOI and unresolved citation text. Use [exact DOI or bibliographic matching](crossref-docs.md) to resolve identities. | Deposited references and DOIs can be absent. A bibliographic query is candidate matching; inspect the result before calling it resolved. |
| Semantic Scholar | Request `/paper/{paper_id}/references?fields=title,authors,year,venue,externalIds&limit=100`, following each returned `next` as `offset`. Follow the [reference endpoint instructions](semantic-scholar-docs.md#exact-records-and-citation-edges). | Fields are inside `citedPaper`; null targets remain unresolved. Preserve rate limits and unfinished pages. |
| PubMed | Use the documented `pubmed_pubmed_refs` ELink relation and retrieve target records through EFetch; follow the [link procedures](pubmed-docs.md#cross-reference-records-and-links). | This relation covers records linked to PMC, not every PubMed paper. |

Use another available graph when the first route lacks references. Preserve the union of retrieved references and its provider provenance, without counting duplicate edges. Do not claim a complete printed bibliography merely because an index response was exhausted. No initial work's unavailable reference list can be silently omitted.

Reference-list retrieval may reveal identifiers from any journal: it records known citation edges, not unrestricted topic discovery. Collect the edges first, resolve identities, and determine overlaps before applying target journal screening. Only exact known targets with a qualifying overlap may use the journal exception. Singletons require the ordinary eligible discovery route before inclusion.

## Resolve and rank

For each reference preserve identifiers, raw citation text where available, identity status, and dated provider evidence for the edge and identity resolution. Normalize DOI URLs/prefixes and case. Prefer exact identifiers and verified crosswalks; never combine references because title tokens or author names merely resemble each other. DOI-less works can use PMID, OpenAlex, Semantic Scholar or arXiv IDs. A verified bibliographic identity without these IDs can use an explicitly reconciled `work:` key with identity evidence. Unresolved identities remain separate and do not earn an overlap exemption.

Build the graph from frozen initial sources and their references only. Count unique citing works after confirmed version/record deduplication, not reference occurrences, providers, citation counts, or new additions. Sort by overlap descending and stable candidate ID ascending for ties. Screen overlapping references before single-paper references; deduplicate targets already in the initial pool without relabeling them.

When a Research project is present, populate its [reference template](../../research/templates/reference.json) and [source fields](../../research/references/artifacts.md#secondary-discovery-records), then run its offline `rank-references` command. The script computes groups and ordering from supplied evidence; Research Literature still performs retrieval, identity checking and relevance screening. Without that project, return the same graph fields under `citation_expansion` rather than requiring a separate project or tool dependency.

## Screen and hand off

For a relevant target cited by at least two distinct initial works, record `journal_filter: overlap_exempt` when using the exception. It may have a below-threshold or unmatched journal. Establish its bibliographic identity through known-record retrieval in available scholarly databases or a verified primary publication record. Preserve conflicting metadata and cross-database confirmation limits. Do not run unfiltered topic queries under this exception.

For a single-paper target, preserve the active journal filter, including category and score rules. Non-journal work types still require the existing scope and inclusion policy. Explicit user journal exceptions or disabling the filter remain ordinary request overrides. All candidates retain the topic, relevance, date, language, author-only restrictions when requested, work-type criteria, and identity checks. Citation overlap establishes neither quality nor claim support.

Record every candidate as included, excluded, unresolved, not inspected, or already initial, with reasons where applicable. A blocked identity/full-text route is an access limit, not scientific disproof. Mark additions `discovery_level: secondary` and retain citing initial IDs, overlap count, relevance basis and journal decision. Never crawl additions to create another round or increase overlap counts. Stop after screening the one-hop candidate set or at an actual access/resource limit; do not impose an invented default quota.

Return initial and secondary records, original reference lists, ranked candidate dispositions, citation-edge evidence, unresolved references and coverage limits. Show discovery level and overlap count in readable results. Use partial status for incomplete lists, unresolved candidates or uninspected remainder, explaining the limits. Research owns full-text appraisal, claim support and the final decision to cite each addition; methods and handoff must disclose the second round and its different journal rule.


## Final gate and top-up interaction

Read [the qualification gate](qualification-gate.md) before final handoff. It keeps the raw frozen graph, recalculates effective overlaps using qualified initial work groups, removes unsupported journal exemptions and writes qualified-expansion.json. If an anchor fails final verification, its stored edges remain auditable but cannot earn an overlap exception. A secondary addition may still pass the ordinary journal rule after losing its exception.

If too few qualified sources remain, perform one topic-search top-up with source search_pass top_up. Such records retain initial discovery level but never join the frozen anchor IDs or create another citation hop. If no initial works qualify, record an empty graph as partial with that limit; the one top-up can still yield ordinary qualifying sources. Preserve the first below-minimum receipt and its input snapshot.
