---
name: "qualification-gate"
description: "Mandatory final source qualification, fixed inventory/list format, independent identity observations, journal screening, and one-top-up receipts."
version: "0.1.0"
created: "2026-10-31"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "OpenAlex"
  - "Crossref"
  - "Allen Institute for AI"
type: "reference"
status: "experimental"
---

# Final source qualification gate

Read before returning a completed Research Literature source pool. The gate is an offline helper, not a search client or a model judge. It verifies recorded evidence and filters the handoff; Research Literature performs the searches, metadata comparisons and relevance judgments. Run it in direct and caller-run uses. A successful process exit does not mean the list is ready: inspect `handoff_ready` and `action`.

## Targets and attempts

| Depth | Qualified unique works | Search behavior |
| --- | --- | --- |
| quick | 8–12 | Simple crawl |
| normal, default | 16–24 | Simple crawl |
| deep | 32–64 combined across rounds | Initial discovery plus one backward-reference hop |

Plan search coverage toward the upper bound. Reaching the lower bound is enough when new searches find no additional helpful qualifying sources. These are targets for discoveries; a report's cited-source constraints are separate. Explicit numeric request/caller targets take precedence. A fixed count is min=max; a minimum-only request can use max=null. Do not include weak, irrelevant or unverified works to meet a number. A genuinely helpful qualifying work is not disqualified merely because the exploration target has already been exceeded.

Run the final gate after the planned searches and the deep backward-reference round where applicable. If the count is below minimum, `action=top_up_required` and `handoff_ready=false`. Perform exactly one targeted top-up pass using new queries/provider angles for recorded gaps, preserving all inclusion rules. Record blocked/failed attempts honestly. Reuse existing candidates, verify additions and run the gate with `--attempt top_up`. If still short, `action=return_shortfall` and `handoff_ready=true`; return the actual qualified remainder with its shortfall and limits. Zero qualifying works is an honest possible outcome. Do not automatically start another pass or another citation hop.

## Input contract

Copy [contract.json](../templates/contract.json) for standalone use; Research initializes literature-contract.json. Complete its pending fields from the actual request and searches. Use:

- `schema_version: 1`, `status: complete`, and depth quick/normal/deep.
- `source_target: {min, max, source}` where source is request or skill_default. Skill-default bounds must match the depth table.
- `constraints`: the resolved journal fields, each exactly `{value, source}` with request or skill_default provenance. Fields are journal_preset, journal_article_influence_min, journal_influence_percentile_min, journal_combination, journal_filter_disabled, journal_category and journal_exceptions. Use the discipline's authoritative preset table; category/exceptions and disabling the filter require explicit request provenance. The gate never loosens these rules.
- `criteria`: explicit additional inclusion criteria. Standard mechanically checked fields are year_min, year_max, language and work_types; keep other requested restrictions under clear keys. Every active key requires per-source screening evidence. Semantic criteria still need actual agent inspection; a nonempty note cannot prove scientific relevance.
- `source_requests`: the original requested paper/author entries with stable request_id, kind work/author, and verbatim input. Leave [] if none were supplied.
- `search_passes`: one initial pass, optionally followed by one top_up pass. Use the [pass](../templates/search-pass.json) and [query](../templates/search-query.json) templates. Each pass needs complete/blocked status, an actual reason/limit and nonempty queries. Queries require provider, query, actual filters, retrieved_at and outcome retrieved/zero_results/blocked/failed. A top-up may not repeat identical provider/query/filter requests already exhausted. Ordinary transient retries remain within the provider's bounded retry procedure, not another discovery pass.

Keep the raw inventory in retrieved-sources.json: schema_version 1, search_receipt, and sources[]. It must stay distinct from the generated sources.json. Retain raw candidate metadata, provider IDs and provenance, supplied-input outcomes, reference lists and conflicting observations. If a considered_count was actually measured, record it in search_receipt; otherwise leave it unavailable rather than inferring it from overlapping provider totals.

Each requested-input outcome must have the existing request_id/status/searches/source_ids/reason fields. All source_ids must resolve to raw records. The gate preserves those IDs as retrieved_source_ids and rewrites the qualified source_ids/status/reason when matches are disqualified or unresolved; it does not silently drop a supplied request. A duplicate requested record maps to its qualified canonical representative when the same work is included.

## Per-source qualification evidence

Each source needs a unique nonempty source_id, title, publication_type, authors array when available, integer year or null, and actual retrieval provenance with provider and HTTP(S) record_url. A non-null article_url must be a valid HTTP(S) URL. Use normalized publication_type journal_article, review, book, book_chapter, report, webpage, dataset, preprint or conference_paper. Other verified work types need an explicit CSL type and boolean journal_filter_applicable; unknown types cannot silently bypass journal screening. CSL article-journal always invokes the journal rule. Preserve full author names/CSL name objects, abstracts and additional provider fields. Qualified output records gain a derived qualification annotation with the second-record identity basis and ordinary/non-journal/explicit/disabled/overlap journal basis, separate from the preserved raw provider metadata. Missing year, venue or abstract remains explicit; it is not fabricated to fill the output template.

Use [verification.json](../templates/verification.json) and the [observation template](../templates/verification-record.json). `verification.status` retains the discipline's cross-database state: multi_source_confirmed or single_source can qualify with sufficient observations; identity_conflict, unconfirmed and not_checked cannot. A database plus a matching publisher record still has only one scholarly database, so it can remain single_source while passing the second-record gate.

Every current verification observation records:

- `provider`: openalex, crossref, semantic_scholar, pubmed, arxiv, google_scholar, database:<host> for another actually used scholarly database, or publisher:<host> for a primary publication record. Use the same provider ID for its API and website; two endpoints of one provider do not count twice.
- `kind`: scholarly_database or primary_publication; record_url and retrieved_at from the actual observation.
- `match_status`: match/conflict/unresolved/not_checked, plus observed `metadata` containing title, authors/year when available, identifiers and other useful fields.
- `comparisons`: title, authors, year, venue and identifier, each match/unavailable/conflict/unresolved as actually inspected. Counted observations must have a matching title and no outstanding conflicting/unresolved comparison.
- Optional `comparison_notes` keyed by title/authors/year for an inspected variation, such as an online-versus-issue date or verified author-name variant. These explain a resolved variation; they never override a conflicting DOI. Preserve historical disagreements separately after actual resolution rather than deleting their retrieval evidence.

At least two matching observations must have different provider IDs and different URLs, with at least one scholarly database. A reachable DOI or source URL alone does not count. Identifier matches use normalized exact IDs or evidenced crosswalks. Without a shared identifier, observed title, authors and year must match; DOI-less works are supported. Shared identifiers do not waive inspection of conflicting metadata. The helper cannot fetch the records to prove that observations were truthful; Research Literature owns that work. Bibliographic verification does not establish quality, peer review, full-text access or claim support.

Use [relevance.json](../templates/relevance.json): relevant status, actual inspection basis abstract/title_and_metadata (or caller-inspected full_text), a concrete reason, criteria_status pass and criteria_evidence keyed to active contract criteria. Pending, irrelevant and non-compliant records are not qualified. Additional criterion notes must describe actual checks; the helper directly enforces year/language/work-type constraints where requested.

Initial and topic-search top-up sources must pass the CSV journal rule or explicit request overrides. Non-compliant or unestablished eligibility disqualifies journal articles/reviews. Deep secondary additions may instead use the recorded overlap exception, but only after recalculation using qualified distinct initial works. Duplicate identities count once, using exact aliases or DOI-less bibliographic identity, not provider record count. Unconfirmed/conflicting works and other useful leads remain in excluded-sources.json with separate unresolved/disqualified states.

## CLI and generated artifacts

Run from the repository root with Python 3.10+; the helper uses only the standard library and its bundled journal CSV. No network, model, Pandoc, account or credential is involved.

```sh
python skills/research-literature/scripts/verify_sources.py --contract /absolute/project/literature-contract.json --inventory /absolute/project/retrieved-sources.json --output-dir /absolute/project
```

For a Research project, use `--replace` deliberately to fill the initialized pending generated files. The raw input paths are protected even with this flag. For deep final qualification add `--expansion /absolute/project/citation-candidates.json`.

After the first final receipt requests a top-up, complete exactly that query pass and append its candidates with search_pass top_up. Keep all previous candidates and raw evidence. Run:

```sh
python skills/research-literature/scripts/verify_sources.py --contract /absolute/project/literature-contract.json --inventory /absolute/project/retrieved-sources.json --output-dir /absolute/project --attempt top_up --replace
```

Include the same --expansion argument for deep mode. Initial and top-up rules/targets/requested inputs must agree. The first actual query pass remains unchanged. The helper requires the first below-minimum receipt and snapshot, freezes the completed top-up query/candidate set, and rejects attempts to reset history or extend it into another automatic search. Explicit replacement can repair metadata/formatting and rerun checks, not initiate a third pass. A newly authorized research invocation uses a new working directory.

The final outputs have fixed names:

| File | Content |
| --- | --- |
| sources.json | Qualified, deduplicated source records and reconciled search/requested-input receipt. |
| sources.md | Fixed readable list generated from exactly that inventory. |
| excluded-sources.json | Raw rejected records with unresolved/disqualified status and a reason. |
| qualified-expansion.json | Normalized deep graph with rejected additions excluded and qualified-anchor overlap annotations; null when no graph was supplied. |
| source-gate.json | Current receipt: action/handoff_ready, target/count/shortfall, per-source decisions, actual available count categories, and input/output paths and SHA-256 hashes, including the journal CSV reference hash. |
| source-gate.initial.json / gate-input.initial.json | First final-attempt receipt and exact local contract/inventory/graph snapshot. |
| source-gate.top_up.json / gate-input.top_up.json | Top-up receipt and snapshot, only when that pass ran. |

The Markdown list has a count heading and one numbered entry per qualified record, preserving title, stable ID, all authors, year, venue, work type, discovery level, verification basis, DOI, work-record link, reported open_access_url, journal decision and abstract or unavailable marker. Optional open-access links retain their reported/unconfirmed access status; identity verification does not establish full-text access. Secondary entries include the effective count of qualified initial citing works. Use this generated list without rewriting entries or counts. Excluded/unresolved leads are separate from the qualified source list.

All operations print JSON. Exit 0 means the offline operation completed, including when it requests the top-up; exit 1 means invalid inputs, stale history, overwrite refusal or failed qualification mechanics. Missing optional tools cannot block this standard-library helper. Publication is staged; preserve raw inputs on failures. Filesystem errors during final replacement can still require recovery from retained inputs.

## Coordinated initial-only handoff

When a caller explicitly coordinates initial discovery before combining planned official/primary sources, run `--phase pool` at any depth. It performs identity, format, journal and requested-input qualification, emitting pool-sources.json, pool-sources.md, pool-excluded-sources.json, pool-qualified-expansion.json and pool-gate.json. Action is continue_collection with handoff_ready false. Counts are provisional; this intermediate handoff does not spend the single top-up before the planned pool is combined. Keep the full raw ledger and original search receipt. Direct requests default to the final gate, not this intermediate phase.

## Deep anchor phase and Research acceptance

Before freezing deep seeds, run the same command with `--phase anchors`. It qualifies the initial pool and emits anchor-sources.json, anchor-sources.md, anchor-excluded-sources.json, anchor-qualified-expansion.json and anchor-gate.json. It returns action continue_expansion with handoff_ready false; counts do not trigger the top-up before the planned citation round. Use the anchor inventory for `research.py rank-references --project <project> --inventory <project>/anchor-sources.json`. Finish reference-list attempts on those qualified records in the raw ledger, then rerun the anchor gate with --replace so its output carries the updated reference lists before ranking. Retained raw records must carry the same identity/reference evidence for the final gate.

The frozen graph keeps original initial IDs/reference evidence. Final qualified lists may exclude failed anchors; only still-qualified members of each distinct initial work group earn an exemption. Raw graphs are preserved; normalized dispositions/overlap annotations go to qualified-expansion.json. A source losing its overlap exception can still qualify under the ordinary journal rule. An empty qualified anchor pool can yield an explicitly partial empty graph with a coverage limit.

Top-up topic results retain discovery_level initial and search_pass top_up; they never supply new seeds or another hop. If verification during the top-up newly qualifies a previously unqualified lead that was not frozen, annotate its admission as top_up. Do not relabel existing frozen anchors to alter their history.

Research's discovery validator requires the exact current receipt, contract, raw inventory, optional raw graph and generated files. It replays qualification and checks hashes/format consistency; any later change requires rerunning the gate and refreshing downstream reviews. It accepts an honest return_shortfall after the single top-up, while the report's cited-source objective bounds remain unchanged. No qualifying sources can support an authored report; return the discovery limit instead. Standalone Literature uses the same gate without calling Research.
