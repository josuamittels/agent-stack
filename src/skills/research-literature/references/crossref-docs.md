---
name: "crossref-docs"
description: "Operational reference for journal-restricted Crossref searches, filters, pagination, DOI lookups, and deposited references."
version: "0.3.0"
created: "2026-10-30"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "Crossref"
type: "reference"
status: "experimental"
---

# Crossref search and lookup reference

Read when searching Crossref or confirming a known DOI. This is the routine request contract, checked against Crossref's official documentation on 2026-10-30. Consult the official links below for an omitted operation, a request error, or changed behavior.

## Access and request format

Use HTTPS GET against `https://api.crossref.org`. Public metadata access needs no account or key. Encode query parameters with the HTTP client's parameter map or curl's `--data-urlencode`. Reuse cached responses within the invocation. Send an identifying User-Agent. Include `mailto` only when an authorized contact address is already supplied, never an invented address.

## Search eligible journals

1. Take eligible print/electronic ISSNs from `journals.csv` using the discipline's selected thresholds. Do not put influence scores into API parameters.
2. Request `GET /journals/{issn}` to check the deposited journal title and ISSNs when the mapping is unresolved.
3. For each confirmed eligible ISSN, request `GET /journals/{issn}/works` with `query=<topic terms>`. Alternatively use `GET /works` with `filter=issn:<issn>`. Retain that journal restriction on every page.
4. Run separate requests for distinct journals or query variants and merge by normalized DOI. Do not assume a list of ISSNs in one parameter means OR.
5. Check returned `container-title` and `ISSN` against the CSV again. Log unresolved journals separately.

This illustrative request searches Nature by its print ISSN. Use it only if that journal qualifies for the invocation, and replace the topic with the planned query:

```sh
curl --get 'https://api.crossref.org/journals/0028-0836/works' \
  --data-urlencode 'query=climate adaptation' \
  --data-urlencode 'rows=100' \
  --data-urlencode 'cursor=*'
```

`query` searches deposited metadata. For a known citation, `query.bibliographic` accepts title, author, year and other citation text. These are relevance queries, not exact identity matches. Do not pass OpenAlex Boolean syntax or invented `author:` operators. Use `query.author=<name>` for a requested author constraint, then confirm the person from returned metadata.

## Apply requested filters

| Requirement | Request parameter |
| --- | --- |
| Eligible journal on `/works` | `filter=issn:0028-0836` |
| Inclusive publication dates | Add `from-pub-date:2020-01-01,until-pub-date:2024-12-31` to `filter`. |
| Work type | Add a documented type such as `type:journal-article` when requested. Crossref types do not distinguish every study design or review subtype. |
| Author terms | `query.author=<name>` is a search, not a unique author identifier. Confirm the returned authors. |
| OA or language restrictions | Inspect deposited license/language metadata where available. Do not equate `has-license` or `has-full-text` with open access. Unverifiable criteria remain unresolved. |

Separate filters with commas to combine dimensions. On `/journals/{issn}/works`, the journal is already fixed by the path. Add only requested date, type or other constraints. Do not add an abstract-availability filter merely because abstracts are useful.

## Page and extract

Use `rows=100` as a working page size, up to the documented maximum of 1000. Start with `cursor=*`. Read `message.items`, `message.total-results` and `message.next-cursor`. Pass the returned cursor unchanged as the next request's `cursor`, preserving all queries and filters. Stop on a missing cursor, an empty/short page, or the caller's inspection limit. Record partial coverage. Detect a repeated cursor/page rather than looping indefinitely. For counts alone, `rows=0` returns the observed total without records.

Keep `DOI`, `URL`, `title`, `author`, `published`, `published-online`, `published-print`, `container-title`, `ISSN`, `type`, `abstract`, `link`, `license`, `reference`, and `is-referenced-by-count` when present. Preserve arrays and author objects. Dates may contain year only. Do not invent a month/day. Crossref abstracts may contain JATS XML. Extract readable text with an XML/HTML parser while retaining the original field and its provenance. Missing abstracts stay missing.

## Confirm identity and follow references

For a known DOI, request `GET /works/{doi}` with the DOI encoded as a path value. Read the single record under `message`. Compare DOI, title, authors, venue and version with the candidate. A 404 means no record at that Crossref lookup, not universal DOI invalidity. Other registration agencies exist. A transport or authentication error is not a no-match response.

For a DOI-less seed, use `/works?query.bibliographic=<known citation>&rows=5`, inspect every candidate, and confirm identity before adopting a DOI. This is verification-only lookup when the provider is not eligible for discovery.

`reference[]` contains deposited backward references. Resolve any reference DOI into a record before counting a match. A reference without a DOI is a lead requiring bibliographic matching. `is-referenced-by-count` is a count, not a forward citation list. Use OpenAlex or Semantic Scholar for forward traversal. Missing references mean unavailable metadata, not an empty bibliography.

## Errors and website fallback

For 400, check parameter names, encoding and the documented filter values. For 429, honor Retry-After and back off. Retry a transient 5xx at most twice with backoff. Stop the route on persistent failures and report it separately from zero results. Record observed rate-limit headers rather than assuming a fixed throughput.

If the API is blocked, try [Crossref Metadata Search](https://search.crossref.org/) only if its visible controls enforce the eligible journal restriction. If not, mark Crossref unavailable for topic discovery, continue through OpenAlex, Semantic Scholar, and all other applicable scholarly providers, and use Crossref only for exact-record verification. Never substitute general web search or web-search results for Crossref discovery.

## Official fallback documentation

- [REST API overview and endpoints](https://www.crossref.org/documentation/retrieve-metadata/rest-api/).
- [Filter definitions](https://www.crossref.org/documentation/retrieve-metadata/rest-api/rest-api-filters/).
- [Rows, cursors, field selection and request guidance](https://www.crossref.org/documentation/retrieve-metadata/rest-api/tips-for-using-the-crossref-rest-api/).


## Deep secondary discovery policy

When depth is deep, follow [the second-round procedure](secondary-discovery.md) for backward-reference overlap counting and known-target retrieval. A relevant target cited by at least two distinct initial works may bypass the CSV journal filter after identity resolution; a deposited identifier or journal reference alone does not establish this exception. Single-paper targets keep the ordinary journal rule. This never permits an unrestricted topic search or a second citation hop. Quick/normal runs do not automatically expand the pool through citations.
