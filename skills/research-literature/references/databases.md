---
name: "databases"
description: "Provider selection, journal-restricted search procedures, and bibliographic cross-referencing for Research Literature."
version: "0.4.0"
created: "2026-10-30"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "OpenAlex"
  - "Federico De Ponte"
  - "Crossref"
  - "Allen Institute for AI"
  - "National Library of Medicine"
  - "arXiv"
  - "Google Scholar"
type: "reference"
status: "experimental"
---

# Literature databases and cross-reference routes

Read this guide before selecting providers. It defines which request to run and which focused reference to load. Read only the reference for a provider actually used. Those references contain routine syntax, filters, pagination, response fields and identity/citation lookups. Consult their official documentation only for missing behavior, request errors or observed changes. Last checked 2026-10-30.

## Attempt all applicable scholarly providers

Attempt OpenAlex, Crossref, and Semantic Scholar independently for every topic-discovery run, using a journal-restricted query in each provider that supports it. Do not stop when one provider fails, returns zero matches, or the combined pool appears sufficient. Add PubMed for biomedical topics and relevant field-specific databases when their venue controls can enforce the active journal rule. Record each attempt, including a successful zero-result response, separately from a failed or blocked request. A provider outage is not evidence of no results and does not excuse skipping the remaining providers.

When a provider API is unavailable, use only that provider's own website if visible controls preserve the journal restriction. If the provider website cannot enforce the restriction, mark its discovery route unavailable and continue with the other eligible providers. Never use a general web search engine or its results as a fallback for scholarly discovery. If every applicable scholarly route is unavailable, return incomplete discovery with the exact provider failures; do not present an empty pool as evidence that no literature exists.

## Prepare the journal restrictions

Build the eligible journal set from `journals.csv` using the discipline's selected preset or explicit override. Retain qualifying rows and normalize print/electronic ISSNs for matching. API journal restrictions select that eligible set; they do not calculate Article Influence or percentile thresholds.

For every initial topic discovery request, restrict the query to eligible journals before retrieving topic matches. Recheck the returned publishing journal against the CSV. If a route cannot express or preserve the restriction, use that route for verification only. A known-work lookup may verify identifiers or metadata without a journal restriction, but its unrelated hits cannot enter the source pool. During deep secondary discovery only, an identified backward-reference target cited by at least two distinct initial works can enter under the [overlap exception](secondary-discovery.md), retaining all other inclusion criteria. This exception never permits an unfiltered topic query.

## Run the appropriate provider procedure

Use the API request below first for each selected API-backed provider. Encode query parameters through the client and classify the actual HTTP/API response. Use the documented website fallback only if the API is unavailable or lacks the needed operation. Keep each provider's role, executed query, journal restriction, retrieval mode, matched/inspected counts and access limits in the receipt. The examples in the provider references are illustrative, not preselected eligible journals or default topics.

### OpenAlex

Load [OpenAlex search and filter instructions](openalex-docs.md) before making requests.

1. Resolve eligible ISSNs through `/sources/issn:<issn>` or the Sources search route, confirm journal identity, and retain source IDs.
2. Call `GET https://api.openalex.org/works` with `search.title_and_abstract=<planned topic>` and `filter=primary_location.source.id:<eligible-source-id>`. Join confirmed alternative source IDs with `|`, up to 100 per batch and within the URL limit.
3. Add only requested date, author, work-type and other constraints. Keep them in every source batch. Read `results` and `meta.count`; page using the reference's key-aware controls.
4. Reconstruct available abstracts from `abstract_inverted_index`. For identity checks retrieve a known work ID or DOI. For backward links use `referenced_works`; for forward links use the `cites` filter as detailed in the reference.
5. If neither API nor website preserves the journal restriction, stop discovery through OpenAlex and continue other eligible providers.

### Crossref

Load [Crossref search, filters and DOI lookups](crossref-docs.md) before making requests.

1. Confirm an eligible ISSN through `GET https://api.crossref.org/journals/<issn>` when needed.
2. Search `GET /journals/<issn>/works` with `query=<planned topic>`, `rows=100` and `cursor=*`. The equivalent `/works` route requires `filter=issn:<eligible-issn>`.
3. Add requested dates/types through the reference's filter syntax. Repeat per eligible journal and query variant. Follow `message.next-cursor` with unchanged restrictions, reading records under `message.items`.
4. Confirm a known DOI with `/works/<doi>`. Resolve DOI-less citation candidates using `query.bibliographic` and compare the returned metadata. Read deposited `reference[]` for backward edges; use another graph for forward citation lists.

### Semantic Scholar

Load [Semantic Scholar search, fields and citation endpoints](semantic-scholar-docs.md) before making requests.

1. Map eligible journals to confirmed full venue names or ISO4 abbreviations.
2. Search `GET https://api.semanticscholar.org/graph/v1/paper/search/bulk` with the planned `query`, the eligible `venue` names, and explicit bibliographic `fields`. Use the reference's bulk-query grammar, not the plain-text relevance-search grammar.
3. Add requested year/date/type restrictions as documented. Follow `token` until exhausted or the inspection limit is reached. Bulk search has no `limit` or `offset`; do not invent them.
4. Confirm known work IDs through `/paper/DOI:<doi>`, `/paper/PMID:<pmid>` or `/paper/ARXIV:<id>`. Retrieve `/references` and `/citations` separately with their offset pagination.
5. If eligible journal names cannot be mapped or venue filtering is unavailable on the usable route, use the provider for identity/citation verification only.

### PubMed

Load [PubMed query tags, ESearch and EFetch](pubmed-docs.md) for biomedical discovery or known-record checks.

1. Build `(topic and synonym clauses) AND (eligible-issn[ta] OR eligible-issn[ta])`. Apply explicit title/abstract, author, date and other requested tags from the reference.
2. Call `GET https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi` with `db=pubmed`, `term=<tagged query>`, `retmode=json`, `retstart=0`, and `retmax=100`.
3. Inspect `esearchresult.querytranslation` and warnings. Retrieve returned PMIDs through `efetch.fcgi` with `db=pubmed`, `id=<returned PMID list>` and `retmode=xml`. Use ESearch paging or history-backed retrieval as documented; respect its 10,000-match limit.
4. Check XML journal ISSNs against the CSV and preserve PMID, PMCID and DOI separately. Use DOI `[aid]` searches plus EFetch for identity checks, and the documented ELink names for citation or similarity relations.

### arXiv

Load [arXiv ID lookup, Atom fields and authorized search](arxiv-docs.md) before making requests.

1. With the journal filter active, use arXiv for verification/version checks only. It has no equivalent publishing-journal restriction.
2. For a known candidate, call `GET https://export.arxiv.org/api/query` with `id_list=<known arxiv-id>`, retaining the version suffix if supplied. If no ID is known, use a narrow title-and-author verification query from the reference.
3. Parse Atom entries, abstracts, versioned IDs and deposited DOI/journal references. Confirm any journal publication through an eligible discovery route before inclusion, except when the known target qualifies for the deep overlapping-reference journal exception.
4. Only when the caller permits broader discovery, run the reference's fielded `search_query` procedure with `start` and `max_results`. Preserve the distinction between arXiv submission dates and journal publication dates.

### Google Scholar

Load [Google Scholar browser search steps](google-scholar-search.md) when supplementary website discovery or verification can add coverage. Do not invent a public search API.

1. Open `https://scholar.google.com/`, then the side menu's Advanced search.
2. Enter the planned topic terms and one confirmed eligible journal in **Return articles published in**. Set author/year controls only when requested and repeat per eligible journal.
3. Inspect actual publisher/repository/database records behind the results, retain the query URL and visible approximate counts, and record the pages inspected. If the publication restriction is unusable, switch to known-title/author verification only.
4. Use **Cited by**, **Related articles** and **All versions** with their distinct meanings from the reference. Stop on browser challenges or traffic blocks.

## Handle access and retrieval outcomes

Attempt OpenAlex, Crossref, and Semantic Scholar for core discovery on every run. Add PubMed for biomedical topics and other relevant field-specific providers when available. Google Scholar is supplementary scholarly-index discovery only when its visible publication control can enforce the active journal rule; arXiv remains verification-only under active journal filtering. Honor a caller's explicit provider restrictions. Explain any provider that is inapplicable or cannot be used, and record the actual attempt and outcome for each applicable provider.

Use authorized existing credentials or an OpenAlex key supplied through [the skill's optional-key setup](../SKILL.md#configure-the-optional-openalex-key). Do not create accounts, obtain other keys, install clients, purchase access or bypass restrictions. On 400, apply the selected reference's parameter correction. On 429 or transient failures, follow its bounded backoff. A successful response with zero results differs from an access failure. Record failed, blocked, rate-limited, and authentication-required routes without calling them empty searches. Never use general web search to replace a scholarly provider or supplement its results.

Preserve provider-native identifiers, dates, names, types and abstracts beside normalized fields. Keep query IDs and field provenance. Do not carry query syntax, journal IDs, filters or page controls between providers. Missing required metadata remains unresolved, not assumed to pass. Preserve the existing caller inventory and search-receipt contract.

## Match and cross-reference records

Normalize DOI URL prefixes, the `doi:` prefix and case for comparison, while retaining the original value. Preserve meaningful identifier punctuation. Match exact DOI or confirmed crosswalks between native identifiers first. A title search supplies candidates, not an identity guarantee. For DOI-less records compare normalized title, authors, date, venue and version. Resolve material differences against a publisher or repository record. Keep unresolved candidates separate instead of forcing a merge.

A matching DOI still needs a title and available author/version sanity check. Token overlap alone can incorrectly match short or generic titles. Keep conflicting source values with their URLs and retrieval dates, and document the chosen canonical field's provenance. Do not overwrite conflicts with a majority vote. Prefer primary publication metadata for the version of record when it resolves a discrepancy. Retain distinct preprint and journal versions with an explicit relationship when supported.

For identity confirmation, look up retained candidates in another appropriate database. Use exact DOI lookups across Crossref, OpenAlex and Semantic Scholar where available. For a PMID or arXiv-only work, use a documented external-ID lookup or a carefully matched title search in another relevant database. Absence from Crossref alone is not evidence that a DOI is invalid or that a work does not exist.

The default confirmation floor is two distinct scholarly databases holding matching records. Count the retrieved finder once and a second matching database once, regardless of API/website routes or repeated queries. Record the original finder separately from additional lookups. The same record copied to a web snippet does not add a database. OpenAlex and Semantic Scholar can ingest Crossref metadata, so cross-index agreement is not fully independent evidence or study replication.

Use these record statuses:

| Status | Meaning |
| --- | --- |
| `multi_source_confirmed` | At least two distinct scholarly databases returned identity-consistent records. |
| `single_source` | One database establishes the record in the inspected results. Additional checks found no match or remain incomplete, as separately recorded. |
| `identity_conflict` | Returned identifiers or metadata materially disagree and the work/version cannot yet be reconciled. |
| `unconfirmed` | A supplied or web-discovered lead has no confirmed scholarly record yet. |
| `not_checked` | Cross-database confirmation was not attempted. Explain the limit. |

Keep `found_by`, `confirming_sources`, `additional_confirmations`, `checked_sources`, `failed_sources`, `not_found_sources`, conflicts and check timestamps. `checked_sources` contains successful responses, including explicit no-match responses. Failed requests belong in `failed_sources`, not in absence counts. Mark whether planned checks are complete. Retain single-source works in the raw ledger with their limits. Before final handoff, the [qualification gate](qualification-gate.md) requires a matching second database or primary publication record; an unchecked single record stays unresolved and does not count. A database plus publisher confirmation can pass while retaining single_source as its database-confirmation state. Record shortfalls and follow the one-top-up rule.

## Follow citations within the search scope

Read [secondary discovery](secondary-discovery.md) when depth is deep. Retrieve backward references for all frozen initial works through the documented endpoints above, retain identifiers and coverage, and group resolved identities across citing works. Rank distinct initial-work overlaps before singleton references. At least two distinct initial citing works permit a recorded journal-filter exception for a relevant known target; exact-record retrieval may then establish its identity without an eligible-journal discovery query. Singletons retain the ordinary journal filter and discovery route. All other inclusion rules apply.

Expand one hop only and mark additions secondary. Quick/normal runs do not automatically expand through citations. Forward citations, related-article results and version links are not backward-reference overlap evidence. A citation edge points from citing to cited work and must carry provider, evidence URL/record ID and retrieval date. Missing or incomplete lists indicate coverage limits, not an empty bibliography. Citation links establish neither endorsement nor claim support.
