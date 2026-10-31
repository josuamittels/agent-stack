---
name: "research-literature"
description: "Search journal-filtered scholarly databases, cross-reference work identities and citation links, and return source-linked records, abstracts, and a caller-ready search receipt."
version: "0.14.0"
created: "2026-10-25"
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
  - "Clarivate"
  - "DORA"
type: "discipline"
status: "experimental"
---

# Research Literature

## Scope

Use this discipline to find academic works across suitable scholarly databases for a research topic, question, or set of search terms. Use OpenAlex, Crossref, Semantic Scholar, and relevant field-specific databases according to their coverage and journal-filtering support. Attempt the core providers independently so one provider's outage does not end discovery. Prefer open APIs. Use sources without usable journal restrictions for verification only while the journal filter is active, except exact-record retrieval for the deep-only overlapping-reference exception below.

This discipline returns bibliographic records, abstracts, search details, verification notes, and links to available full text. When used by another workflow, it supplies a traceable source pool for that caller to read and appraise. It does not read and appraise full papers, synthesize findings, assess study quality, or draft a literature review.

### Boundaries

Search eligible scholarly providers for records and abstracts, and cross-reference bibliographic identities across databases. Never use a general web search engine or general web-search results to discover, supplement, or replace scholarly database results. If a provider API is unavailable, try only that provider's own search website when it can enforce the active journal restrictions; otherwise record that discovery route as unavailable and continue through every other applicable eligible database. Return available full-text links without reading or evaluating whole papers. Do not infer missing metadata, peer-review status, journal reliability, or research conclusions. Do not treat journal classes, impact metrics, citation counts, or search ranking as substitutes for evaluating an individual study.

## Inputs

Use the supplied topic or question and any stated inclusion and exclusion criteria. Accept optional filters for authors, journals, publication dates or years, work types, fields, language, open access, citation count, and result size. Preserve explicit query terms and constraints.

When called by another workflow, carry forward its research purpose, focus or context, required subtopics, seed references, requested result size, and output contract. Use these to plan discovery rather than asking the user to repeat settled choices. Treat supplied references as leads, not independently verified records or automatic exceptions to the inclusion criteria. Record each required reference as retrieved and eligible, excluded with a reason, or unresolved. Reconcile that outcome again after the final gate; a retrieved requested work that fails verification does not count as qualified. Do not invent bibliographic fields to turn a supplied title or URL into a confirmed source.

Accept a caller-supplied or direct `depth` of `quick`, `normal`, or `deep`; use `normal` when unspecified. Only deep runs perform the backward-reference expansion in step 6. Depth does not alter the initial journal-selection rule. When Research coordinates staged discovery, honor its requested initial-only handoff first using the pool-phase qualification gate; return verified working records marked continue_collection, without spending the count-based retry. Run the final gate only after the caller supplies the combined planned pool, and perform the secondary pass first when deep. A secondary-only handoff preserves the existing query/seed receipts and runs step 6 without a new topic search. Direct requests and callers without a staged instruction complete both rounds when deep.

Depth sets the default target for distinct included works: **quick: 8–12**, **normal: 16–24**, **deep: 32–64** across the combined rounds. An explicit caller/user result target takes precedence. Plan exploration toward the upper bound, but accept the lower bound when further searches yield no helpful qualifying work. Count only distinct sources passing the final qualification gate; never pad a list or relax criteria to meet a target. Quick and normal use a simple crawl: initial topic/author/seed searches, record verification and screening, without automatically expanding citation-linked sources. Deep adds the single backward-reference round. Keep identity verification and journal standards at every depth; report insufficient eligible evidence rather than padding the list.

Accept optional specific citations, source papers (identifiers, URLs, titles or full references), and authors from the user or caller. Preserve each original input under a stable request ID, with kind `work` or `author`; do not omit a supplied entry because the general topic search found enough sources. Without these inputs, follow the usual discovery process.

For each supplied work, use exact identifier lookup first when available; otherwise search the title/full citation using the provider procedures and compare title, authors, year and venue. Unfiltered exact-record lookup is verification, not permission for unfiltered topic discovery. Include a resolved eligible work in the source pool even if the general query did not retrieve it. For each supplied author, resolve identity using ORCID, affiliation or known works where available; run a targeted author search combined with the question and active journal criteria. Keep namesake ambiguity explicit. Author suggestions add searches; apply an author-only restriction only when explicitly requested. Continue broader topic discovery and search for contrary evidence.

Account for every supplied input in `search_receipt.requested_inputs`, including in direct answers. Each outcome carries `request_id`, `status` (`eligible`, `excluded`, `unresolved`, or `no_eligible_works`), actual `searches` (provider and lookup/query text or an explicit blocked-attempt explanation), matched included `source_ids`, and a concrete `reason`. Retain original inputs alongside the receipt or in the caller's brief. Excluded/unresolved records can be returned separately without entering the eligible inventory. Report access limits and uncertain identity; never invent a successful lookup. Supplied papers and authors do not waive journal, topic or other inclusion rules. Explain any conflict and carry the outcome to the caller instead of silently dropping the request or broadening the filter.

Before selecting providers, read [database routes and cross-referencing](references/databases.md) for discovery eligibility and concrete provider procedures. Before using a provider, load its focused API or browser reference linked there for search syntax, journal restrictions, filters, paging, record fields, and identity/citation lookups. Use those local instructions for routine requests. Consult their official fallback documentation when a needed behavior is missing, a request errors, or observed behavior appears to have changed.

Use the [journal CSV](references/journals.csv) to select eligible journals. Its fields are `journal`, `issn_print`, `issn_online`, `category`, `area`, `inception`, `article_influence`, and `influence_percentile`. A journal may have multiple category rows. Treat these supplied metrics as venue-selection criteria, not proof of reliability or article quality.

### Journal selection

Accept **lenient**, **default**, or **strict** journal selection, independently of research depth. Use **default** when unspecified. Interpret "more lenient" as lenient and "stricter" as strict when no explicit preset or numeric cutoffs were supplied. Announce the selection and cutoffs, and proceed without asking the user to choose again.

| Selection | Minimum `article_influence` | Minimum `influence_percentile` |
| --- | --- | --- |
| Lenient | 1.0 | 60 |
| Default | 2.5 | 80 |
| Strict | 5.0 | 90 |

Accept a journal when `article_influence >= minimum OR influence_percentile >= minimum`. Boundaries are inclusive. Honor explicit numeric cutoffs or a request to disable the filter as overrides, rather than additional presets. If only one numeric cutoff is supplied, use only that metric unless the user also requests a preset for the other. Preserve the user's explicit combination rule if it differs from OR.

Read the [selection rationale](references/journal-selection.md) when explaining or reconsidering the presets. It supplies dated sources, CSV calibration counts, and provenance limits. The CSV does not specify the metric year or percentile calculation. Use its supplied percentile values without recomputing them or labeling them as JIF, CiteScore, or field-normalized percentiles.

Parse finite, nonnegative Article Influence scores and percentiles in 0–100. Compare without rounding. Zero is valid. Missing or invalid values fail only their own branch, so one available score can qualify a journal. If neither branch passes, exclude the journal from the eligible set. Record unknown scores or unmatched journals separately from measured below-threshold exclusions.

Match normalized print or electronic ISSNs first, ignoring hyphens and case, then confirm titles. Use title matching only when usable ISSNs are unavailable, and report ambiguous matches. Preserve category rows. For an explicit category restriction, test only matching category rows. Otherwise any qualifying category row suffices. Retain the qualifying row and metric branch in the search log rather than averaging or silently collapsing scores.

Apply this filter to journal articles and reviews. Search requested preprints, conference papers, books, and other source types separately and label them. Use the publishing journal to judge a journal article's eligibility, even when an accessible copy is hosted in a repository. An OA hosting location does not override the journal filter. The sole automatic journal exception is a relevant second-round reference cited by at least two distinct initial works during deep research; follow step 6 and record the supporting edges. All other scope and inclusion criteria still apply.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/SKILL.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/SKILL.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Frame the search

Identify the main concepts, population or setting, and outcome or relationship in the topic where applicable. Build a short concept list with relevant synonyms, spelling variants, and closely related terms. Prepare a few focused searches that cover those terms. Do not force a clinical or other field-specific framework onto a topic that does not fit it.

Choose search angles that serve the question, such as foundations, current work, methods, applications, or limitations. For an interdisciplinary question, cover the relevant domains with distinct queries. Resolve seed references in an appropriate scholarly database and use their verified terminology to refine queries. Seek reviews, foundational work, recent studies, or alternative perspectives when relevant and permitted by the criteria. Do not impose quotas, default date windows, language restrictions, or citation thresholds to create that range. Do not use a general web search engine to find candidate works, even if all scholarly providers are unavailable; report discovery as incomplete instead.

Keep the user's exact search string when supplied. Record the selected journal preset or override, query text, and filters used for every request. Use separate queries for distinct concepts when one long Boolean query would become difficult to inspect or exceed the selected provider's request limits.

### 2. Select providers and resolve filters

Build the eligible journal set once from the CSV, preserving the selected preset, category restrictions, and qualifying rows. For every run, attempt discovery independently through OpenAlex, Crossref, and Semantic Scholar; do not stop after one provider fails, returns zero matches, or supplies an adequate-looking pool. Also attempt PubMed for biomedical questions and any other relevant field-specific database with a usable journal restriction. Use the database reference to translate that eligible set into each provider's native journal identifiers or filters. Google Scholar may be used as a supplementary scholarly index only when its publication restriction can enforce the selected journals; it is not a general web-search fallback. Record each provider's role as discovery, verification only, or unavailable, with the observed outcome and reason.

While the journal filter is active, a discovery route must restrict the request to eligible journals before retrieving topic results. If a provider or chosen endpoint lacks that capability, use it only to verify already discovered candidates, identifiers, versions or citation relationships. Do not replace the restriction with an unfiltered topic search followed by CSV filtering. arXiv normally serves verification and version lookup because it does not offer an equivalent publishing-journal restriction. Known overlapping backward-reference targets in deep research may use exact-record retrieval under step 6's journal exception; this never permits unfiltered topic discovery. Any requested non-journal discovery requires explicit scope and suitable provider controls; do not treat it as an automatic bypass of the user's journal rule. An explicit request to disable the journal filter permits broader provider discovery.

Prefer an available open API over that provider's website. Use authorized existing credentials or an OpenAlex key supplied through the setup below. If an API request fails, classify the failure, follow only the documented bounded remedy, and try that provider's own website only when its visible controls can preserve the required restrictions. Regardless of that outcome, continue through every other applicable eligible database. Never switch to a general web search engine. Record successful zero results separately from failed, blocked, rate-limited, and authentication-required routes; zero results from one provider do not stand in for attempts at the others. Do not install clients, create accounts, obtain other credentials, purchase access or bypass restrictions.

#### Configure the optional OpenAlex key

Before the first OpenAlex request, check `OPENALEX_API_KEY` in the process environment, then in this skill's `references/.env`. Use the first nonempty value after trimming surrounding whitespace and optional matching quotes. Resolve these paths relative to this skill, not the caller's working directory. Read the file as environment data; do not execute or source it as shell code.

If neither location supplies a key, use [Ask User Question](../ask-user-question/SKILL.md) to offer two choices: provide an OpenAlex API key and save it locally for future searches, or research without a key. Explain that basic metadata searches work without one, while some operations require authentication. The user may enter the key directly in `references/.env` instead of sending it in chat. Wait for the choice before OpenAlex retrieval; continue independent provider work while waiting. Do not infer a choice from silence. Reuse an explicit keyless choice across staged calls in the same research task. If no user interaction is possible, report the pending choice to the caller and continue other providers.

When the user supplies a key for storage, create `references/.env` from [the environment template](references/.env.example) if the file is absent. Set `OPENALEX_API_KEY` in the existing file otherwise, preserving unrelated settings and comments. Save only the supplied value, with valid dotenv quoting, without shell interpolation. Restrict the file to owner read/write access where supported. Confirm that Git ignores it before writing a secret; do not modify the template with a real key. If storage is unavailable, report that the key was not saved and never claim future reuse is configured.

Pass the selected key through the HTTP client's `api_key` parameter only to `https://api.openalex.org`. Omit the parameter for keyless research. Never print the key, dump the environment file, or include credentials in search receipts, saved request URLs, logs, or reports; redact `api_key` from diagnostic URLs. Existing environment keys need no local copy. Record only whether requests used a key. If authentication rejects a key, report the failure without exposing or deleting it and offer replacement or keyless research once; a key cannot repair a DNS or transport failure.

#### OpenAlex filters and access

Follow [`references/openalex-docs.md`](references/openalex-docs.md) for supported parameters, filters, and limits.

- Resolve a named author through the OpenAlex Authors endpoint. Confirm the candidate using available identifiers such as ORCID, affiliation, and known works before filtering by author ID. Do not silently choose between people with similar names.
- Build the eligible journal set from the CSV using the journal-selection rules above. Intersect it with explicit journal and category restrictions. Resolve eligible journals by ISSN through the OpenAlex Sources endpoint, confirming titles and retaining all confirmed source IDs. Report ambiguous or unresolved venues rather than guessing. When the journal filter is disabled, resolve only requested journal constraints.
- Apply requested year bounds with publication-date filters and other requested constraints with supported work filters. Apply the stated default journal selection, but do not add further prestige, citation-count, open-access, language, or date cutoffs without a request.
- Combine multiple author IDs or source IDs with OpenAlex's OR syntax within that filter. Combine separate filter dimensions with AND only when the user intends all of them to apply together.

Use an available HTTP/API client to call `https://api.openalex.org`. Basic metadata queries can be made without an API key. Classify the result of a small read-only request before continuing:

- A valid OpenAlex response, including a successful response with zero matches, establishes API access. Record API errors separately from successful zero-result searches.
- A DNS, connection, TLS, or tool-access failure means the selected route could not reach the API. It does not establish that OpenAlex is down, that the query has zero matches, or that the API rejected the request. Do not repeat the same blocked route or broaden a query to compensate for transport failure.
- If direct API access is unavailable, use an available browser to search the OpenAlex website and inspect its work, author, or source records. Identify this as an OpenAlex website search, record the queries and which fields or result counts were visible, and mark filters or pagination that the interface could not verify. Do not present generic web-search results that merely mention OpenAlex as an OpenAlex search.
- If neither the API nor the OpenAlex website is available, stop that provider's retrieval, report the access gap, and continue other eligible providers. Do not install clients, configure proxies, or seek credentials to work around host restrictions.

If a requested value cannot be resolved or OpenAlex does not expose the needed filter, report the gap. Continue only where useful results can still honor the inclusion criteria. The CSV metrics are local criteria, not OpenAlex filter fields.

### 3. Search and retrieve records

Run provider-specific queries with the eligible journal restrictions in every discovery request. Keep the same topic, author, date and other constraints across journal batches. For Crossref, use eligible ISSNs with its works filter or journal-specific works endpoint. For Semantic Scholar, use a documented search endpoint with venue filtering and confirmed journal names. For PubMed, combine the topic with eligible ISSN or journal terms tagged `[ta]`. The [database reference](references/databases.md) supplies routes, metadata fields and access limits. Confirm each returned journal against the CSV as a final check, even when the provider enforced a journal restriction.

Retrieve provider IDs, DOI and other external IDs, title, complete available authors, publication dates, venue and ISSNs, type, abstract, citation count and access locations when available. Keep provider, query identifier, retrieval date, record URL and field provenance. Do not require a work to exist in OpenAlex to include it. Distinguish databases used for discovery from databases used only for confirmation, and label website versus API retrieval per provider.

#### OpenAlex retrieval

When API access is available, query the OpenAlex Works endpoint. Prefer `search.title_and_abstract` for targeted retrieval; use `search` when full-text terms or keywords are useful. Use semantic search when meaning-based retrieval could find useful terminology variants, subject to its documented limits. Use relevance ordering for discovery, but do not present its score as a measure of evidence quality. If a request errors or a needed field or behavior is unclear, consult the relevant official fallback link in the [`Openalex Documentation`](references/openalex-docs.md), correct the request, and record the change. When using the OpenAlex website fallback, follow its available search and record pages instead; do not claim API filters, counts, or pagination that the website did not expose.

Filter journal works by eligible `primary_location.source.id` values. Batch OR lists at no more than 100 source IDs per request, splitting further for the URL limit. Keep the topic, author, date, and other constraints on every batch. Merge results by stable work identifiers. For example, a focused request can use `search.title_and_abstract` with `filter=authorships.author.id:<author-id>,primary_location.source.id:<eligible-source-id>,from_publication_date:2020-01-01,to_publication_date:2024-12-31`. Omit unspecified optional filters. Let the HTTP client encode spaces, quotes, and the `|` OR separator. Follow the reference's paging rules, including the API-key requirement for cursor pages after the first.

If resolving the complete eligible journal set is impractical within access or resource limits, search only a confirmed subset of eligible journals with those restrictions applied. Identify the subset and its selection rule, and report partial venue coverage. If no usable restriction can be built, use that route for verification only. Retain the preset throughout follow-up searches. Empty results do not authorize relaxing the thresholds, dropping the filter, or including unknown venues.

Page through results when needed. If a Boolean query approaches OpenAlex's URL length limit, split its OR terms into smaller requests and merge the results by work ID. Record the total matching count and how many records were actually inspected or returned. If the result set is too large to inspect in full, state the selection rule and that the results are partial.

Review the yield across planned concepts before stopping. If a requested subtopic is poorly covered, refine terminology or try a relevant adjacent angle within the original scope. Preserve every inclusion rule across follow-up searches. Stop when the planned scope and requested result size are covered, further searches repeat the same eligible records, or a stated access or resource limit prevents useful retrieval. Report unmet targets and remaining search angles. Do not pad results or interpret a small retrieved set as proof that little literature exists.

For OpenAlex records, retrieve the bibliographic and access fields listed above, including the OpenAlex ID. Reconstruct an abstract from `abstract_inverted_index` by placing each word at its recorded position and joining the words in order. If no abstract is available, label it as missing rather than writing a summary in its place. OpenAlex notes that reconstructed abstracts can occasionally include text beyond the abstract; flag obvious cases without silently editing the record.

Use OpenAlex's `best_oa_location` to identify an available full-text page or PDF, and return its link and any known version or license. Return `content_urls` when available; downloading from OpenAlex's content API requires an API key. Do not download or analyze the paper as part of this search task. An open link does not by itself grant reuse rights.

### 4. Screen and deduplicate

Confirm journal eligibility before screening titles and available abstracts against the topic and other criteria. Exclude ineligible journal works and works clearly outside scope. Keep uncertain relevance matches among eligible works in a separate short list or mark why relevance is uncertain. When an abstract is absent, make clear that screening used title and metadata only.

Deduplicate by normalized DOI first, then confirmed external-ID crosswalks or matching native provider IDs. If no shared identifier exists, compare normalized titles, authors, publication dates, venue and version. A title/year match alone is a candidate match, not permission to merge. Keep the provider IDs and discovery provenance from every merged record. Preserve meaningful distinctions between a preprint, accepted manuscript, and version of record; do not imply they are identical versions when the records show otherwise.

Retain the journal match, qualifying category row, scores, and eligibility reason with screened records. When the filter is disabled, journal metadata remains optional context. Citation counts and journal metrics do not establish the quality or truth of an individual article.

Keep brief relevance notes separate from retrieved metadata and abstracts. Tie each note to the title or abstract actually inspected, and label its basis as `title_and_metadata` or `abstract`. Do not add inferred findings, methods, limitations, or peer-review status. Describe missing topics as gaps in the searched and screened set, with suggested refinements, rather than established gaps in the field.

### 5. Cross-reference and verify source records

For every retained candidate, attempt an identity lookup in at least one other appropriate scholarly database, subject to available access and the caller's budget. Prefer exact DOI lookups across Crossref, OpenAlex and Semantic Scholar. A retrieved finder counts once. Record other database lookups separately. For works without a DOI, use PMID, arXiv or another documented identifier crosswalk, or a carefully checked title-and-author match. Verification-only providers may retrieve metadata for known candidates. A new work enters the pool through journal-restricted discovery or the evidence-backed deep overlapping-reference exception in step 6.

Use `multi_source_confirmed` only when at least two distinct scholarly databases return matching identities. Use `single_source` for a work established by one database, `identity_conflict` for unresolved material disagreement, `unconfirmed` for a lead without a retrieved scholarly record, and `not_checked` when confirmation was not attempted. Report `found_by`, `confirming_sources`, `additional_confirmations`, `checked_sources`, `failed_sources`, `not_found_sources`, check dates and whether planned checks are complete. Preserve single-source works in the raw retrieval ledger with their limits. They enter the qualified final count only after matching another scholarly database record or the primary publication record, with actual dated observations. A single database plus matching publisher record may qualify while retaining `single_source` as its cross-database state; an unchecked single record does not qualify. A failed or rate-limited lookup is unknown, not evidence of absence.

Compare identifiers and available title, authors, venue, date and version before counting a match. Do not resolve conflicts by majority vote or title-token overlap alone. Crossref, OpenAlex and Semantic Scholar may share upstream metadata, so agreement corroborates indexing and identity, not independent replication, study quality or claim support. Follow the [cross-reference rules](references/databases.md#match-and-cross-reference-records) for matching, provenance and conflict handling.

Trace every included work to a retrieved scholarly database record or verified primary publication record. Preserve its identifiers, author display names and available author IDs, title, dates, source, and work type as returned. Keep missing fields explicit. Do not invent initials, split names into guessed components, impose an author-count cap, or discard a work merely because it lacks a DOI or abstract. Keep search-query or batch identifiers with each record so its discovery can be traced.

Check that the DOI and other returned links belong to the same work, using available record metadata. For a central seed reference, conflicting metadata, or a caller-requested identifier check, open the DOI or source landing page and compare title, authors, venue, and date where available. This is an identity check, not full-paper reading. Distinguish online publication dates, issue dates, and manuscript versions before treating differences as errors. Retain the observed values and provenance when a conflict cannot be resolved. Keep an unresolved identity out of the confirmed set and return it separately for caller review.

Record the verification basis and outcome precisely: retrieved provider records, cross-database confirmation, corroborating landing-page metadata if checked, identity conflict, or unresolved check. For a link check, distinguish reached, not found, and access or transport failure. Mark an unattempted check as not checked. Preserve an otherwise eligible scholarly record in the raw/unresolved ledger when corroboration is unavailable, with that check marked unresolved; exclude it from the qualified list and count. A failed request does not prove that a work does not exist, and a reachable DOI does not prove correct metadata, journal eligibility, peer review, study quality, or support for a claim. Do not apply one undifferentiated `verified` label to these separate questions.

Record abstract provenance by provider and record URL, identifying OpenAlex reconstruction, provider-supplied text, or missing, and state that full text was not read. An OA URL is a supplied access location until checked. Preserve its reported version and license without implying that access or reuse rights were independently confirmed. Carry these limits forward even when a record's identity is corroborated.

### 6. Run the deep backward-reference round

For quick/normal depth, do not automatically expand the source pool through citations. Identity and version checks may still use recorded relationships; they do not initiate another discovery round.

For deep depth, read [secondary discovery](references/secondary-discovery.md) before expanding. Run the [qualification gate](references/qualification-gate.md) in anchor phase, then freeze the deduplicated qualified initial pool and attempt backward-reference retrieval for every initial work. Preserve rejected retrievals separately. If no anchors qualify, retain an empty, explicitly partial expansion rather than inventing seeds. Preserve each reference list, identifiers, actual provider provenance and coverage limits. Resolve identities, then rank by the number of distinct initial works citing each target, descending, with stable identifier order for ties. Duplicate provider records and confirmed versions of one citing work count once.

Screen overlapping targets before single-paper references. A relevant target cited by at least two distinct initial works may bypass the CSV journal filter, including below-threshold and unmatched journals. Record `overlap_exempt` and the actual citation edges. Resolve such known targets through available scholarly records without requiring a journal-restricted discovery query. Single-paper references retain the ordinary journal rule and eligible retrieval route. Preserve all other inclusion criteria and identity verification in both cases. Overlap is a discovery signal, not quality, endorsement or claim support.

Add eligible new works with `discovery_level: secondary`, citing initial source IDs, overlap count, relevance basis and journal decision. Keep an already included work initial and attach its edges without another inventory entry. Expand one hop only; new additions never supply seeds or increase overlaps. Record exclusions, unresolved identities, unavailable lists, remaining candidates and resource limits. Return the ranked candidate data and reference lists to the caller. When using a Research project, its offline `rank-references` command computes the graph; it does no retrieval or screening. Research owns appraisal before using additions in prose.

Keep citation edges directed from citing to cited work, with provider, evidence URL and retrieval date. Label version and similarity relations separately. Forward citations are outside this automatic second round.

### 7. Qualify the final list before handoff

Read [the qualification-gate contract and CLI](references/qualification-gate.md) before compiling results. Preserve raw retrievals, complete the resolved search contract and per-source identity/relevance observations, and run the offline gate. It checks the fixed list format, distinct identities, requested-input outcomes, a matching second scholarly-database or primary-publication record, and actual journal eligibility or a supported exception. Link reachability alone is insufficient. Journal non-compliance and unestablished eligibility disqualify a work. Unconfirmed/conflicting records remain separate and do not count.

For deep runs, supply the frozen reference graph. Recalculate overlap exceptions using qualified initial citing works; a failed anchor cannot continue supplying an exemption. Top-up topic-search results use `search_pass: top_up`, retain initial discovery level and never become citation-expansion seeds.

If the first final gate reports `top_up_required`, perform one targeted additional search pass for recorded gaps, preserving journal and all other inclusion rules. Use genuinely new queries/provider angles rather than repeating exhausted identical searches. Re-verify all candidates and run the gate with `--attempt top_up`; its receipt and snapshot preserve the original trigger. This is one search pass, not another citation hop. If the count is still below the minimum, return only the qualifying remainder with its shortfall and access/coverage limits. Do not start another automatic top-up or inflate the list. Meeting the minimum is sufficient when further helpful sources cannot be found; the upper bound guides exploration.

Do not return the final list/data until the receipt has `handoff_ready: true`. A shortfall after the single top-up is an honest final handoff, including zero qualifying sources if that is the result. Use the generated sources.md and sources.json without a prose-generation pass that could change entries, metadata or counts. Keep excluded/unresolved records clearly separate. A staged initial-only handoff uses `--phase pool` at any depth and returns verified working data marked `continue_collection`; a staged deep anchor handoff uses `--phase anchors` and returns `continue_expansion`. Neither is a final public source list or spends the one count-based retry before the caller combines its planned sources.

### 8. Return the search results

Present the matching works with a DOI or native database record link, title, authors, year, journal, work type, abstract when available, and open-access link when available. Include relevant journal fields from the CSV only when they help interpret a requested filter or the result list. For deep results, show discovery level (`initial` or `secondary`) and the number of distinct initial works citing each addition. Explain that secondary level describes discovery, not study design. Include second-round coverage and its journal exception in the receipt. Name the actual databases searched and their roles. Do not imply that any one index, or the combined search, covers all relevant literature.

Alongside the results, report the search date, exact query strings, filters, total matched count, number returned or inspected, and any unresolved filters or truncation. Separate preprints and other work types where that distinction matters. Do not turn the list into a claim about what the literature collectively concludes.

Include the selected preset or override and numeric combination rule, CSV path and snapshot limitation, category rule, eligible and resolved journal counts, actual query batches, and retrieval mode per provider, distinguishing `API` from `website`. For retrieved records, distinguish inspected and included works, measured below-threshold exclusions, unknown journal matches or scores, and unresolved source IDs. Report counts actually observed in the chosen retrieval mode; mark counts unavailable when the website does not expose them. Do not sum overlapping batch totals as unique works or imply that source-filtered queries enumerated excluded works.

### 9. Pass the source pool to the caller

For a direct request, return the readable results and receipt in the conversation unless another format was requested. When used as a helper, also return a structured inventory in the caller's requested schema. If none was supplied, use a JSON object with `search_receipt`, `included_works`, `uncertain_works`, `unresolved_references`, `cross_references`, and, for deep runs, `citation_expansion` with the frozen initial pool, ranked candidates and coverage limits. Do not require fixed filenames or create a separate paper-writing pipeline.

Keep provider-derived bibliographic fields distinct from screening and verification annotations. Each inventory entry carries a stable local work key and all available provider IDs, DOI or other external IDs when available, bibliographic fields and links, abstract or explicit missing value, discovery-query identifiers, relevance basis, journal-selection evidence, cross-database confirmation status and supporting records, and verification notes. Use `null` for unavailable values and explain consequential missing data. Preserve all available authors and the abstract rather than shortening them silently for the handoff.

Before returning, validate the current gate receipt and reconcile its generated readable list and structured inventory by stable identifiers, qualified unique counts, titles, and years. Preserve the filtered inventory, excluded/unresolved ledger, search contract, both attempt receipts when applicable, and input snapshots for repeatability. Rebuild inconsistent bibliographic fields from retrieved records rather than editing them to match generated prose. Report any intentionally omitted records or truncated fields. Preserve the full inventory in the caller's authorized artifact location when one is supplied, and return its path with a concise summary.

Return the original question and constraints, source inventory, cross-reference edges, provider roles and outcomes, search and journal-selection receipt, seed-reference outcomes, unresolved identity or access checks, coverage limits, and suggested next searches. Distinguish completed retrieval, successful zero-result retrieval, and partial or blocked discovery. State what the pool is ready for and what remains: the caller owns full-text retrieval, appraisal, claim verification, synthesis, and any decision to broaden scope or change criteria. Resume the owning workflow without invoking later research or writing stages independently.

## Output

Return a concise, source-linked list of relevant academic works with abstracts where available and DOI, provider-record, and open-access links. Include the exact searches, journal-selection receipt, observed result counts, retrieval mode, record-verification basis, and screening or truncation notes. For a caller, include the reconciled structured inventory and remaining verification or coverage gaps. Name only databases actually searched, distinguish discovery from verification-only lookups, and report unavailable providers. Include cross-database confirmation states and citation/version relationships without treating them as claim verification. If all eligible discovery routes were unavailable, report incomplete discovery rather than an empty literature.
