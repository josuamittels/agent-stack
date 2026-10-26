---
name: "research-literature"
description: "Search OpenAlex for academic works with lenient, default, or strict journal-influence selection and other requested filters, and return source-linked records and abstracts."
version: "0.4.0"
updated: "2026-10-26"
author:
  - "Josua Mittelstaedt"
references:
  - "OpenAlex"
  - "Clarivate"
  - "DORA"
type: "discipline"
status: "draft"
---

# Research Literature

## Scope

Use this discipline to find academic works in OpenAlex for a research topic, question, or set of search terms. It can narrow results by author, journal, publication year, work type, subject, open-access status, or other supported OpenAlex fields.

This discipline returns bibliographic records, abstracts, search details, and links to available full text. It does not read and appraise full papers, synthesize findings, assess study quality, or draft a literature review.

## Inputs

Use the supplied topic or question and any stated inclusion and exclusion criteria. Accept optional filters for authors, journals, publication dates or years, work types, fields, language, open access, citation count, and result size. Preserve explicit query terms and constraints.

Before searching, read [`references/openalex-docs.md`](references/openalex-docs.md) for OpenAlex endpoints, search syntax, filters, paging, and record fields. Consult the official documentation linked there only if an API request errors, this reference does not cover a needed behavior, or observed behavior appears to have changed.

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

Apply this filter to journal articles and reviews. Search requested preprints, conference papers, books, and other source types separately and label them. Use the publishing journal to judge a journal article's eligibility, even when an accessible copy is hosted in a repository. An OA hosting location does not override the journal filter.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Frame the search

Identify the main concepts, population or setting, and outcome or relationship in the topic where applicable. Build a short concept list with relevant synonyms, spelling variants, and closely related terms. Prepare a few focused searches that cover those terms. Do not force a clinical or other field-specific framework onto a topic that does not fit it.

Keep the user's exact search string when supplied. Record the selected journal preset or override, query text, and filters used for every request. Use separate queries for distinct concepts when one long Boolean query would become difficult to inspect or exceed OpenAlex's request URL limit.

### 2. Resolve filters to OpenAlex identifiers

Follow [`references/openalex-docs.md`](references/openalex-docs.md) for supported parameters, filters, and limits.

- Resolve a named author through the OpenAlex Authors endpoint. Confirm the candidate using available identifiers such as ORCID, affiliation, and known works before filtering by author ID. Do not silently choose between people with similar names.
- Build the eligible journal set from the CSV using the journal-selection rules above. Intersect it with explicit journal and category restrictions. Resolve eligible journals by ISSN through the OpenAlex Sources endpoint, confirming titles and retaining all confirmed source IDs. Report ambiguous or unresolved venues rather than guessing. When the journal filter is disabled, resolve only requested journal constraints.
- Apply requested year bounds with publication-date filters and other requested constraints with supported work filters. Apply the stated default journal selection, but do not add further prestige, citation-count, open-access, language, or date cutoffs without a request.
- Combine multiple author IDs or source IDs with OpenAlex's OR syntax within that filter. Combine separate filter dimensions with AND only when the user intends all of them to apply together.

Use an available HTTP/API client to call `https://api.openalex.org`. Basic metadata queries can be made without an API key. If direct HTTP access is unavailable, use an available browser route to inspect OpenAlex records and report any missing fields or paging limits. Do not install a client or expose credentials to work around missing access.

If a requested value cannot be resolved or OpenAlex does not expose the needed filter, report the gap. Continue only where useful results can still honor the inclusion criteria. The CSV metrics are local criteria, not OpenAlex filter fields.

### 3. Search and retrieve records

Query the OpenAlex Works endpoint. Prefer `search.title_and_abstract` for targeted retrieval; use `search` when full-text terms or keywords are useful. Use semantic search when meaning-based retrieval could find useful terminology variants, subject to its documented limits. Use relevance ordering for discovery, but do not present its score as a measure of evidence quality. If a request errors or a needed field or behavior is unclear, consult the relevant official fallback link in the [`Openalex Documentation`](references/openalex-docs.md), correct the request, and record the change.

Filter journal works by eligible `primary_location.source.id` values. Batch OR lists at no more than 100 source IDs per request, splitting further for the URL limit. Keep the topic, author, date, and other constraints on every batch. Merge results by stable work identifiers. For example, a focused request can use `search.title_and_abstract` with `filter=authorships.author.id:<author-id>,primary_location.source.id:<eligible-source-id>,from_publication_date:2020-01-01,to_publication_date:2024-12-31`. Omit unspecified optional filters. Let the HTTP client encode spaces, quotes, and the `|` OR separator. Follow the reference's paging rules, including the API-key requirement for cursor pages after the first.

If resolving the complete eligible journal set is impractical within access or resource limits, retrieve topic matches first and apply the same CSV eligibility check before relevance screening or inclusion. Label this as post-filtered, bounded retrieval and report its limits. Do not claim coverage of every eligible venue. Retain the preset throughout follow-up searches. Empty results do not authorize relaxing the thresholds, dropping the filter, or including unknown venues.

Page through results when needed. If a Boolean query approaches OpenAlex's URL length limit, split its OR terms into smaller requests and merge the results by work ID. Record the total matching count and how many records were actually inspected or returned. If the result set is too large to inspect in full, state the selection rule and that the results are partial.

Retrieve the title, authors, publication year, journal/source, type, DOI, OpenAlex ID, abstract, citation count, and open-access locations when available. Reconstruct an abstract from `abstract_inverted_index` by placing each word at its recorded position and joining the words in order. If no abstract is available, label it as missing rather than writing a summary in its place. OpenAlex notes that reconstructed abstracts can occasionally include text beyond the abstract; flag obvious cases without silently editing the record.

Use OpenAlex's `best_oa_location` to identify an available full-text page or PDF, and return its link and any known version or license. Return `content_urls` when available; downloading from OpenAlex's content API requires an API key. Do not download or analyze the paper as part of this search task. An open link does not by itself grant reuse rights.

### 4. Screen and deduplicate

Confirm journal eligibility before screening titles and available abstracts against the topic and other criteria. Exclude ineligible journal works and works clearly outside scope. Keep uncertain relevance matches among eligible works in a separate short list or mark why relevance is uncertain. When an abstract is absent, make clear that screening used title and metadata only.

Deduplicate by DOI first, then OpenAlex work ID. If neither is available, compare normalized titles and years. Preserve meaningful distinctions between a preprint, accepted manuscript, and version of record; do not imply they are identical versions when the records show otherwise.

Retain the journal match, qualifying category row, scores, and eligibility reason with screened records. When the filter is disabled, journal metadata remains optional context. Citation counts and journal metrics do not establish the quality or truth of an individual article.

### 5. Return the search results

Present the matching works with a DOI or OpenAlex record link, title, authors, year, journal, work type, abstract when available, and open-access link when available. Include relevant journal fields from the CSV only when they help interpret a requested filter or the result list. Describe the scope as an OpenAlex search; do not imply that one index covers all relevant literature.

Alongside the results, report the search date, exact query strings, filters, total matched count, number returned or inspected, and any unresolved filters or truncation. Separate preprints and other work types where that distinction matters. Do not turn the list into a claim about what the literature collectively concludes.

Include the selected preset or override and numeric combination rule, CSV path and snapshot limitation, category rule, eligible and resolved journal counts, actual query batches, and retrieval mode. For retrieved records, distinguish inspected and included works, measured below-threshold exclusions, unknown journal matches or scores, and unresolved source IDs. Report counts actually observed in the chosen retrieval mode. Do not sum overlapping batch totals as unique works or imply that source-filtered queries enumerated excluded works.

## Output

Return a concise, source-linked list of relevant academic works with abstracts where available and DOI, OpenAlex, and open-access links. Include the exact searches, journal-selection receipt, result counts, and screening or truncation notes. Identify the search as OpenAlex-only.

## Boundaries

Search OpenAlex for records and abstracts. Return available full-text links without reading or evaluating whole papers. Do not infer missing metadata, peer-review status, journal reliability, or research conclusions. Do not treat journal classes, impact metrics, citation counts, or search ranking as substitutes for evaluating an individual study.
