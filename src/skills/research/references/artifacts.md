---
name: "research-artifacts"
description: "Required project artifacts, JSON record fields, provenance, and completion states for repeatable Research runs."
version: "0.3.2"
created: "2026-10-30"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "Federico De Ponte"
  - "Pandoc"
type: "reference"
status: "experimental"
---

# Research artifact contracts

Read before completing project records. [Templates](../templates/brief.json) and the CLI validators define schema version 1. Do not invent a new record type or manuscript structure during an invocation. Keep missing data explicit as null or an empty list. Read [Research Literature's gate contract](../../research-literature/references/qualification-gate.md) before completing its verification/relevance observations or running the final source gate. A template is unfinished input, not evidence of completed research.

## Project records

| Artifact | Required content |
| --- | --- |
| brief.json | `schema_version`, pending/complete `status`, `document_type`, `topic`, original `request`, bounded `question`, `scope`, `audience`, optional `field`, `language`, `depth`, `citation_style`, `formats`, `terminology`, `constraints`, actual `method`, `outside_check` with planned/observed text, and `assumptions`. |
| manifest.json | Type, prescribed section IDs/headings/relative paths, working artifact inventory and generated artifact names. The initializer owns it. Paths must stay within the project. |
| sources.json | `schema_version`, `search_receipt` with status, actual searches and limits, and `sources`, with discovery-level and reference-list fields for deep runs. Use the [source template](../templates/source.json) for each retrieved work. |
| retrieved-sources.json | Raw retrieved candidates and original search/requested-input receipt; preserve this separately from the filtered pool. |
| literature-contract.json | Resolved discovery depth/targets/provenance, journal rules, additional criteria, requested inputs and actual search-pass history. |
| source-gate.json | Current qualification receipt with input/output hashes, count/shortfall, decisions and retry state; handoff_ready must be true. |
| citation-candidates.json | Frozen initial pool, resolved ranked backward-reference graph, screening dispositions and coverage limits; pending scaffold at other depths. See [secondary records](#secondary-discovery-records). |
| appraisals.json | `schema_version`, status and `appraisals` using the [appraisal](../templates/appraisal.json) and [finding](../templates/finding.json) templates. |
| claims.json | `schema_version`, status and `claims` using the [claim template](../templates/claim.json). |
| outline.json | `schema_version`, status and prescribed ordered sections. Each has `id`, `heading`, `path`, `purpose`, `source_ids`, `claim_ids`, inclusive `word_budget` with min/max, and neighboring `context`. |
| argument-review.json / citation-review.json | [Review template](../templates/review.json): type, status, reviewed draft SHA-256, `inputs_sha256` for the brief/sources/appraisals/claims/outline and citation-candidates artifacts, repair count, fixed checks and issues using the [issue template](../templates/issue.json). |
| exports.json | Schema version and an `exports` array of generated conversion receipts. After actual page inspection, set each Word/PDF entry's `visual_review` to `complete` and add `visual_review_evidence` with rendered page paths and observations. |

The CLI fills type, topic, question, original request, default constraints and pending checks. Research completes scope, method, evidence and actual judgments. Mark a phase complete only after doing the work. Do not edit a hash to make a stale review appear current; review the new text, then record its actual hash.

## Optional requested papers and authors

`brief.source_requests` defaults to `[]`. Each entry is `{"request_id":"input-001","kind":"work","input":"Original citation, identifier, URL or title"}`; kind may also be `author`, retaining the name/ORCID and any supplied identity context. IDs must be unique. These are additional search obligations, not automatic author-only filters or journal exceptions.

`search_receipt.requested_inputs` defaults to `[]` and must contain exactly one outcome per request ID before discovery passes validation. Each outcome has `request_id`, `status` (`eligible`, `excluded`, `unresolved`, `no_eligible_works`), nonempty `searches` containing actual provider/query or blocked-attempt details, `source_ids` referencing included inventory records, and a nonempty `reason`. Eligible outcomes need at least one source ID. Other outcomes may have an empty list; retain excluded/uncertain metadata separately. A blocked or unresolved result is an accounted limitation, not successful inclusion. Research must inspect eligible requested works and explain any later decision not to cite them in appraisal/selection notes and the handoff. Mechanical accounting cannot establish that the searches were adequate or the claims supported.

## Constraint provenance

Every constraint is exactly `{"value": ..., "source": "request" | "skill_default"}`. The complete-report word and cited-source bounds are:

| Depth | Words inclusive | Cited substantive sources inclusive |
| --- | --- | --- |
| quick | 800–1600 | 8–12 |
| normal | 2000–4000 | 16–24 |
| deep | At least 6000, no default ceiling | 32–64 |

The initializer records `word_count_min/max`, `source_count_min/max`, the existing `journal_*` fields, and `requested_formats`. For explicit numeric, journal, category or exception overrides, update the resolved constraint with request provenance and retain it in the standalone invocation record. When disabling the journal filter by request, use preset disabled, null thresholds and `journal_filter_disabled=true`. Do not change the journal CSV or its rule to meet a source target. `formats` must agree with `constraints.requested_formats.value`.

## Sources and bibliography metadata

Each source requires unique nonempty `source_id`, `title`, `publication_type`, and a nonempty `provenance` list of actual provider/primary record observations. Preserve original provider IDs, URLs, query IDs, metadata, journal eligibility, access and identity checks, and conflicting or missing fields. The source template does not replace Research Literature's evidence: keep its additional fields and search receipt.

Journal articles/reviews additionally carry `journal_title`, `issns`, and `article_url` for the existing objective package. Prefer source types `journal_article`, `review`, `book`, `book_chapter`, `report`, `webpage`, `dataset`, `preprint`, or `conference_paper`. Unknown source types can supply an explicit CSL type in `csl`.

Optional bibliographic fields include `authors`, integer `year`, `doi`, `volume`, `issue`, `pages` and `publisher`. Authors are display-name strings or explicit CSL name objects. Strings become CSL `literal` names; the helper never guesses surname/given-name boundaries. Supply explicit `family`/`given` values only from verified metadata. `csl` can preserve richer dates, editors, page ranges, publisher places and other verified CSL fields. Its title must match the source title, and an explicit ID must equal the generated citation key. Nulls remain missing, not invented publication values.

`citations --prepare` generates stable `r` plus 16 SHA-256 hex characters from each exact source_id. citation-keys.json maps original IDs to these keys; bibliography.json is the derived CSL JSON array. Never type or guess a generated key. Duplicate source IDs/DOIs require source-pool reconciliation. Distinct versions remain distinct only where their identities warrant it.

## Findings and claims

An appraisal has one source_id, an `inspection` of full_text, abstract or metadata, findings, limitations and notes. A finding requires finding_id, text and an actual locator such as a section/page, table or abstract. Metadata-only inspection cannot produce extracted findings. An absent finding is not a fabricated null result.

A claim has a unique claim_id, text, supported/qualified status, `supports` and `contradicts` arrays of `{"source_id": ..., "finding_id": ...}`, and a qualification where needed. Unsupported/pending claims block structuring until supported, qualified or removed. Links establish traceability; the script cannot judge whether a finding semantically supports a proposition.

## Reviews and generated results

Argument checks are question_answered, claim_strength, counterevidence, cross_section_consistency and outside_check. Citation checks are source_identity, claim_support, quotations_and_numbers, locators and bibliography. Each check has status pending/checked/not_applicable and evidence describing the actual check or reason it does not apply. Both completed reviews must match draft.md's current SHA-256 and the current input hashes, including citation-candidates.json when present. `validate --phase draft` returns these hashes after you perform the review.

Issues require issue_id, passage, severity critical/major/minor, status open/resolved, problem, and the actual correction for resolved issues. Open critical/major issues block finalization. `repair_passes` counts substantive repair rounds and cannot exceed two.

Generated artifacts are draft.md, bibliography.json, citation-keys.json, report.md, cited-sources.json and citation-receipt.json. The cited inventory contains original source records for actual citation keys only. Receipts bind draft, source inventory, style and compiled report by SHA-256. Export receipts add input/output hashes, format/backend, tool versions, detected feature counts and visual-review state. Scripts report bookkeeping and conversion outcomes, not scientific correctness.

## Secondary discovery records

Only deep projects populate citation-candidates.json; quick/normal projects leave its pending scaffold unchanged. Missing `discovery_level` on an older source means initial. New source templates set it explicitly. All initial sources in a deep project need a reference-list attempt before ranking, including a dated blocked/unavailable attempt when appropriate.

Use the [reference template](../templates/reference.json) for each reference. `reference_list` is an object with:

- `status`: pending, complete, partial, unavailable or blocked. Pending does not pass deep discovery validation.
- `retrievals`: nonempty provider evidence records with `provider`, actual `record_url` and `retrieved_at`; record attempted operation/error details for blocked routes. These establish the list's provenance, not a successful response in every case.
- `references`: resolved or unresolved reference records, retaining raw citation text and identifiers where available. `identity_status` is resolved or unresolved; resolved references require dated `identity_evidence` and an identifier. Optional per-reference `provenance` supplies edge evidence; otherwise the containing list's retrievals supply it.
- `limits`: strings describing coverage and unfinished paging. Required for partial, unavailable or blocked status. Complete means completed retrieval of available indexed references, not proof of a complete printed bibliography.

Both source and reference records accept `identifiers` with namespaces `doi`, `openalex`, `pmid`, `semantic_scholar`, and `arxiv`. Source-level `doi` is also read. DOI prefixes/URLs and case are normalized; OpenAlex work IDs may be bare or full URLs. arXiv version suffixes are grouped under the same work. An alias crosswalk must come from verified metadata; conflicts remain unresolved. To reconcile confirmed manuscript/published versions or DOI-less title-only identities, set the same `canonical_id: work:<stable-local-key>` and retain dated `identity_evidence` on each reconciled entry. No automatic title/author fuzzy matching occurs.

`rank-references` creates citation-candidates.json with `schema_version`, ranked status, frozen `initial_source_ids`, `initial_inputs_sha256`, `initial_work_groups`, `candidates`, `coverage`, `unresolved_references` and `limits`. The hash binds initial identities and reference lists. Grouped citing records use the lexically first source ID as their representative; edge records retain the original source IDs. Each candidate has `candidate_id`, resolved `identity_keys`, unique `citing_source_ids`, `overlap_count`, `edges` with from/to IDs, reference index and provenance, `existing_source_ids`, and a `disposition`. Ordering is overlap descending, then candidate ID ascending. Repeated edges retain evidence but increase the count only once per distinct initial work.

Complete candidate dispositions with `status` included/excluded/unresolved/not_inspected/already_initial, `source_id` for additions, and a nonempty `reason` for every non-initial candidate. Initial matches retain already_initial and do not become additions. The gate writes a normalized qualified-expansion.json that preserves frozen identity/reference evidence while excluding rejected additions and recalculating qualified-anchor overlap annotations. Stop at a resource limit by marking the remaining ranked suffix not_inspected; record an overall limit. The validator checks ordering and that higher-ranked candidates were not left uninspected while lower-ranked candidates were screened, but cannot establish the actual timing or adequacy of screening.

Set overall status complete after all candidates are screened with complete retrieval coverage; use partial for unresolved references, unresolved/uninspected candidates or partial/unavailable/blocked lists. Partial requires explanatory `limits`. Finalization may retain honest coverage limitations; pending/unaccounted work blocks phase completion.

Secondary sources use `discovery_level: secondary` and the [secondary-discovery template](../templates/secondary-discovery.json): `candidate_id`, representative `citing_source_ids`, `overlap_count`, `journal_filter` (overlap_exempt or ordinary), `relevance_reason`, and `other_criteria_evidence`. The latter describes actual screening of remaining inclusion rules; scripts do not judge scientific relevance. overlap_exempt needs two distinct initial citing works; ordinary applies the CSV rule or existing explicit request overrides. A singleton journal article cannot bypass that rule. New secondary reference lists do not participate in the graph. Every addition must match one included candidate; citing paths, counts and graph hashes are checked against current initial references.

Before freezing, the anchor gate applies the ordinary journal rule and second-record verification. Final overlap counts use only qualified initial works; rejected anchors stay in the raw ledger and frozen edge evidence but no longer earn exemptions. Topic-search top-ups carry `search_pass: top_up` and never become seeds. An empty qualified anchor pool produces an explicitly partial empty graph.

The graph joins the review-input hashes so later edits invalidate argument/citation reviews. Preserve the full graph for objective checks even when only a subset of the initial pool is eventually cited. Do not transfer automatic overlap exceptions into the explicit request `journal_exceptions` list.


## Qualified discovery artifacts

The Literature gate owns sources.json, sources.md, excluded-sources.json, qualified-expansion.json and source-gate.json. Preserve source-gate.initial.json and gate-input.initial.json; after a top-up also preserve source-gate.top_up.json and gate-input.top_up.json. Initial anchor qualification produces anchor-sources.json and anchor-gate.json. Every source retains search_pass (initial or top_up), verification observations, relevance/inclusion screening and original provenance. Templates for these observations live beside Research Literature.

Research's discovery validator requires a current handoff-ready gate receipt bound to the exact raw inventory, contract and optional raw graph, checks the contract against the brief, and verifies generated list/data hashes. The source target counts qualified discoveries, not citations. A return_shortfall receipt is acceptable after one top-up; zero sources cannot support drafting a research report. Gate, contract, raw inventory and normalized graph join review input hashes, so changed discovery evidence requires fresh reviews and citation/export checks.
