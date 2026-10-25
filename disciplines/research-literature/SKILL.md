---
name: "research-literature"
description: "Search OpenAlex for relevant academic works, apply author, journal, date and other filters, and return source-linked records and abstracts."
version: "0.2.0"
updated: "2026-10-25"
author:
  - "Josua Mittelstaedt"
references:
  - "OpenAlex"
type: "discipline"
status: "draft"
---

# Research Literature

## Scope

Use this discipline to find academic works in OpenAlex for a research topic, question, or set of search terms. It can narrow results by author, journal, publication year, work type, subject, open-access status, or other supported OpenAlex fields.

This discipline returns bibliographic records, abstracts, search details, and links to available full text. It does not read and appraise full papers, synthesize findings, assess study quality, or draft a literature review.

## Inputs

Use the supplied topic or question and any stated inclusion and exclusion criteria. Accept optional filters for authors, journals, publication dates or years, work types, fields, language, open access, citation count, and result size. Preserve explicit query terms and constraints.

Before searching, read [`references/openalex_docs.md`](references/openalex_docs.md) for OpenAlex endpoints, search syntax, filters, paging, and record fields. Consult the official documentation linked there only if an API request errors, this reference does not cover a needed behavior, or observed behavior appears to have changed.

Use the [`Journals Database`](../references/journals.csv) when journal scores or ERIM journal classes are relevant. The file preserves the supplied ERIM workbook's categories and metrics. It can contain several rows for one journal because a journal may appear in multiple categories. Match by ISSN when possible, then confirm the journal title. Treat its scores and classes as user-provided context, not as proof of reliability or article quality.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Frame the search

Identify the main concepts, population or setting, and outcome or relationship in the topic where applicable. Build a short concept list with relevant synonyms, spelling variants, and closely related terms. Prepare a few focused searches that cover those terms. Do not force a clinical or other field-specific framework onto a topic that does not fit it.

Keep the user's exact search string when supplied. Otherwise, record the query text and the filters used for every request. Use separate queries for distinct concepts when one long Boolean query would become difficult to inspect or exceed OpenAlex's request URL limit.

### 2. Resolve filters to OpenAlex identifiers

Follow [`references/openalex_docs.md`](references/openalex_docs.md) for supported parameters, filters, and limits.

- Resolve a named author through the OpenAlex Authors endpoint. Confirm the candidate using available identifiers such as ORCID, affiliation, and known works before filtering by author ID. Do not silently choose between people with similar names.
- Resolve a journal through `references/journals.csv` by ISSN or eISSN when possible. Then resolve that ISSN through the OpenAlex Sources endpoint and filter works by the journal's source ID. Use the journal name only when no usable ISSN is available, and report ambiguous matches.
- Apply requested year bounds with publication-date filters, and apply other requested constraints with supported work filters. Do not silently add prestige, citation-count, open-access, language, or date cutoffs that the user did not request.
- Combine multiple author IDs or source IDs with OpenAlex's OR syntax within that filter. Combine separate filter dimensions with AND only when the user intends all of them to apply together.

Use an available HTTP/API client to call `https://api.openalex.org`. Basic metadata queries can be made without an API key. If direct HTTP access is unavailable, use an available browser route to inspect OpenAlex records and report any missing fields or paging limits. Do not install a client or expose credentials to work around missing access.

If a requested value cannot be resolved or OpenAlex does not expose the needed filter, report the gap and continue with the remaining constraints where that still produces useful results.

### 3. Search and retrieve records

Query the OpenAlex Works endpoint. Prefer `search.title_and_abstract` for targeted retrieval; use `search` when full-text terms or keywords are useful. Use semantic search when meaning-based retrieval could find useful terminology variants, subject to its documented limits. Use relevance ordering for discovery, but do not present its score as a measure of evidence quality. If a request errors or a needed field or behavior is unclear, consult the relevant official fallback link in the [`Openalex Documentation`](references/openalex_docs.md), correct the request, and record the change.

For example, a focused request can use `search.title_and_abstract` with `filter=authorships.author.id:<author-id>,primary_location.source.id:<source-id>,from_publication_date:2020-01-01,to_publication_date:2024-12-31`. Omit filters the user did not request. Let the HTTP client encode spaces, quotes, and the `|` OR separator. Follow the reference's paging rules, including the API-key requirement for cursor pages after the first.

Page through results when needed. If a Boolean query approaches OpenAlex's URL length limit, split its OR terms into smaller requests and merge the results by work ID. Record the total matching count and how many records were actually inspected or returned. If the result set is too large to inspect in full, state the selection rule and that the results are partial.

Retrieve the title, authors, publication year, journal/source, type, DOI, OpenAlex ID, abstract, citation count, and open-access locations when available. Reconstruct an abstract from `abstract_inverted_index` by placing each word at its recorded position and joining the words in order. If no abstract is available, label it as missing rather than writing a summary in its place. OpenAlex notes that reconstructed abstracts can occasionally include text beyond the abstract; flag obvious cases without silently editing the record.

Use OpenAlex's `best_oa_location` to identify an available full-text page or PDF, and return its link and any known version or license. Return `content_urls` when available; downloading from OpenAlex's content API requires an API key. Do not download or analyze the paper as part of this search task. An open link does not by itself grant reuse rights.

### 4. Screen and deduplicate

Compare titles and available abstracts against the topic and stated criteria. Exclude only works that are clearly outside scope. Keep uncertain matches in a separate short list or mark why relevance is uncertain. When an abstract is absent, make clear that screening used title and metadata only.

Deduplicate by DOI first, then OpenAlex work ID. If neither is available, compare normalized titles and years. Preserve meaningful distinctions between a preprint, accepted manuscript, and version of record; do not imply they are identical versions when the records show otherwise.

Use the journal CSV to add matching journal metadata when useful. Join by ISSN/eISSN before title. Retain category-specific rows and scores instead of collapsing them to one score. Do not use journal scores as an automatic inclusion rule unless the user explicitly requests that filter. Citation counts and journal classifications describe metadata; they do not establish the quality or truth of an individual article.

### 5. Return the search results

Present the matching works with a DOI or OpenAlex record link, title, authors, year, journal, work type, abstract when available, and open-access link when available. Include relevant journal fields from the CSV only when they help interpret a requested filter or the result list. Describe the scope as an OpenAlex search; do not imply that one index covers all relevant literature.

Alongside the results, report the search date, exact query strings, filters, total matched count, number returned or inspected, and any unresolved filters or truncation. Separate preprints and other work types where that distinction matters. Do not turn the list into a claim about what the literature collectively concludes.

## Output

Return a concise, source-linked list of relevant academic works with abstracts where available and DOI, OpenAlex, and open-access links. Include the exact searches and filters, result counts, screening or truncation notes, and journal-score context when requested. Identify the search as OpenAlex-only.

## Boundaries

Search OpenAlex for records and abstracts. Return available full-text links without reading or evaluating whole papers. Do not infer missing metadata, peer-review status, journal reliability, or research conclusions. Do not treat journal classes, impact metrics, citation counts, or search ranking as substitutes for evaluating an individual study.
