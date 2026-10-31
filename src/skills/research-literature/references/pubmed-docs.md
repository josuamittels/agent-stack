---
name: "pubmed-docs"
description: "Operational reference for journal-restricted PubMed queries, ESearch, EFetch, identity checks, and supported record links."
version: "0.2.1"
created: "2026-10-30"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "National Library of Medicine"
type: "reference"
status: "experimental"
---

# PubMed search and lookup reference

Read for biomedical journal discovery, PMID/DOI confirmation, or PubMed record links. These relevant E-utilities operations and PubMed query rules were checked against NCBI documentation on 2026-10-30. Consult the official links below for missing operations, errors or changed behavior.

## Access and sequence

Base URL: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/`. Public requests need no key. Stay at or below three requests per second without a key, shared across the invocation's requests. Use an authorized existing key only if needed, with no more than its allowed rate. Identify the client with `tool` and an already authorized contact `email` where available. Do not invent a contact or obtain credentials.

1. Use `esearch.fcgi` with `db=pubmed`, `term`, `retmode=json`, `retstart=0`, and `retmax=100` to obtain PMIDs.
2. Read `esearchresult.count`, `idlist`, `querytranslation`, and any error/warning fields. Inspect the translated query before accepting its meaning.
3. Use `efetch.fcgi` with `db=pubmed`, `id=<comma-separated PMIDs>`, and `retmode=xml` for the actual bibliographic records and abstracts. Retrieve batches of 100 as a working size.
4. Preserve PMID, DOI, PMCID and the record URL `https://pubmed.ncbi.nlm.nih.gov/<pmid>/`. ESearch IDs alone are not full records or evidence that an abstract was inspected.

## Build the journal-restricted query

Use parentheses around each concept's synonyms, combine concepts with uppercase `AND`, and append an eligible-journal clause with `AND`. Use eligible ISSNs/eISSNs tagged `[ta]` first. Full journal names or abbreviations tagged `[ta]` are alternatives when confirmed. Combine eligible journals with `OR`. Batch large journal lists while keeping the topic and other constraints unchanged.

This illustrative query searches Nature by its print ISSN. Substitute the eligible ISSNs and planned terms:

```sh
curl --get 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi' \
  --data-urlencode 'db=pubmed' \
  --data-urlencode 'term=(climate[tiab] AND adaptation[tiab]) AND 0028-0836[ta]' \
  --data-urlencode 'retmode=json' \
  --data-urlencode 'retstart=0' \
  --data-urlencode 'retmax=100'
```

Use the returned PMID list in the next request:

```text
GET /efetch.fcgi
db=pubmed
id=<comma-separated PMIDs actually returned by ESearch>
retmode=xml
```

## Query fields and requested filters

| Requirement | Query syntax in `term` |
| --- | --- |
| Title/abstract concepts | `climate[tiab] AND adaptation[tiab]`. Quotes request a phrase; review warnings if PubMed cannot apply it as intended. |
| Eligible journals | `(0028-0836[ta] OR 1476-4687[ta])`. These are alternative ISSNs in an illustrative journal clause, not a new default journal set. |
| Requested author | `Smith J[au]` or a confirmed full name with `[fau]`. Confirm identity; names are ambiguous. |
| Inclusive dates | `("2020/01/01"[dp] : "2024/12/31"[dp])`. Do not substitute entry/indexing dates for publication dates. |
| Publication type | `Review[pt]` or another documented type when requested. |
| Language | `english[la]`, only when requested. |
| Known DOI | `<bare-doi>[aid]`, followed by record inspection and an exact DOI comparison. |
| Known PMID | Retrieve directly with EFetch; no topic search is needed. |

Unqualified terms can undergo Automatic Term Mapping to MeSH and other fields. Use explicit `[tiab]` terms for a reproducible title/abstract query; add confirmed `[mh]` terms when controlled-vocabulary expansion serves the question. Record `querytranslation` and material warnings. Do not silently broaden the query or remove the journal clause after zero results.

## Page and extract records

Advance `retstart` by the number of PMIDs returned, preserving `term` and `retmax`. Stop when the reported count is covered, the page is empty, or the caller's limit is reached. PubMed ESearch exposes only the first 10,000 matches. For a larger set, split by eligible journals or publication-date intervals that together preserve the original scope, then deduplicate PMIDs. Otherwise report truncation; increasing `retmax` or `retstart` cannot bypass the cap.

For a stable history-backed run, add `usehistory=y` to ESearch, retain the returned `WebEnv` and `querykey`, and pass `WebEnv` plus `query_key` to EFetch with `retstart` and `retmax`. Keep history values private to the invocation and do not report them as bibliographic identifiers.

Parse EFetch XML with an XML parser. For journal articles, retain `MedlineCitation/PMID`, `Article/ArticleTitle`, `Article/Abstract/AbstractText`, `Article/AuthorList`, `Article/Journal`, publication date fields, and `PubmedData/ArticleIdList/ArticleId` with its `IdType`. Preserve structured abstract section labels and inline text. Keep the journal ISSN and available linking ISSN. Confirm the publishing journal against the CSV. Missing abstract/date/name components remain explicit, and a PMID does not itself prove MEDLINE indexing or peer review.

## Cross-reference records and links

For a known DOI, ESearch the DOI with `[aid]`, EFetch each candidate, then compare its deposited DOI, title, authors and version. For a PMID, EFetch it directly. Do not treat multiple search hits as interchangeable.

For backward links, request `elink.fcgi?dbfrom=pubmed&db=pubmed&id=<pmid>&linkname=pubmed_pubmed_refs&cmd=neighbor`. This reference relation is available for PubMed records linked to PMC, not every PubMed record. Read IDs under the matching `LinkSetDb/Link` and retrieve their records with EFetch. `linkname=pubmed_pubmed` provides related articles, not citation edges.

The checked live PubMed link list does not expose a `pubmed_pubmed_citedin` relation. Use OpenAlex or Semantic Scholar for forward citations rather than inventing that request. To inspect current link support after a link-name error, call `einfo.fcgi?db=pubmed&retmode=json` and read `einforesult.dbinfo[].linklist`. Missing citation links indicate incomplete coverage. Route singleton candidates through journal-restricted discovery before inclusion. For a known target qualifying under the [deep overlap exception](secondary-discovery.md), identity retrieval need not restrict the journal; all other inclusion rules remain.

## Errors and website fallback

Check API-level error/warning fields even after HTTP 200. For 429, honor Retry-After and reduce request rate. Retry transient failures at most twice with backoff. A blocked API is not an empty search.

If the API is unavailable, open [PubMed](https://pubmed.ncbi.nlm.nih.gov/), paste the same tagged query, inspect Advanced → History and Search Details for translation, and open each inspected record's abstract page. Retain the journal clause on every query. Record visible totals, pages inspected and any inaccessible export/field information.

## Official fallback documentation

- [E-utilities operations and parameters](https://www.ncbi.nlm.nih.gov/books/NBK25499/).
- [NCBI E-utilities reference](https://eutilities.github.io/site/Reference_Guide/a_reference/).
- [PubMed search fields and translation](https://pubmed.ncbi.nlm.nih.gov/help/).
- [Entrez link names and meanings](https://www.ncbi.nlm.nih.gov/entrez/query/static/entrezlinks.html).
- [NCBI request-rate policy](https://support.nlm.nih.gov/kbArticle/?pn=KA-05510).
