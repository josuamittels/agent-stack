---
name: "semantic-scholar-docs"
description: "Operational reference for Semantic Scholar search syntax, venue filters, pagination, identity lookups, and citation endpoints."
version: "0.3.0"
created: "2026-10-30"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "Allen Institute for AI"
type: "reference"
status: "experimental"
---

# Semantic Scholar search and lookup reference

Read when searching Semantic Scholar or checking identities and citation edges. The request contract below was checked against the official Academic Graph schema on 2026-10-30. Use the official schema for omitted fields, request errors or changed behavior.

## Access and endpoints

Base URL: `https://api.semanticscholar.org/graph/v1`. Use HTTPS GET and encode parameter values through the client. Try public access first. If an authorized API key already exists, send it in `x-api-key`. Do not acquire a key during literature discovery or expose it in logs. A 401/403 or persistent 429 means this route is unavailable under current access, not that the query is empty.

| Operation | Path | Response |
| --- | --- | --- |
| Journal-restricted topic search | `/paper/search/bulk` | `data[]`, estimated `total`, optional continuation `token`. |
| Plain-text candidate lookup | `/paper/search` | `data[]`, `total`, `offset`, optional `next`. |
| Exact identity lookup | `/paper/{paper_id}` | One paper record. |
| Backward citations | `/paper/{paper_id}/references` | `data[].citedPaper` and optional `next`. |
| Forward citations | `/paper/{paper_id}/citations` | `data[].citingPaper` and optional `next`. |

## Search eligible journals

1. Map the CSV-eligible journal to its confirmed full venue name or ISO4 abbreviation. The `venue` filter accepts names, not OpenAlex IDs or influence scores.
2. Call `/paper/search/bulk` with `query`, `venue` and `fields`. Use separate journal requests when a journal name contains a comma or its mapping is ambiguous. Otherwise a comma-separated venue list means OR.
3. Check returned `venue`, `journal` and available `publicationVenue` metadata against the CSV journal identity. A venue can be a conference, so its presence alone does not establish journal eligibility.
4. If the mapping or venue restriction cannot be enforced, mark the route verification-only. Do not switch to an unfiltered topic query.

This illustrative request uses Nature. Substitute an eligible confirmed venue and the planned topic:

```sh
curl --get 'https://api.semanticscholar.org/graph/v1/paper/search/bulk' \
  --data-urlencode 'query=climate + adaptation' \
  --data-urlencode 'venue=Nature' \
  --data-urlencode 'fields=title,authors,year,publicationDate,venue,journal,publicationVenue,externalIds,url,abstract,publicationTypes,citationCount,openAccessPdf'
```

Bulk search matches title/abstract terms with English stemming. Spaces require all terms by default. Use `+` for AND, `|` for OR, `-` to negate a term, double quotes for a phrase, parentheses for grouping, and `*` for a prefix. For example, `(adaptation | resilience) + climate` expresses alternatives plus a required concept. Encode the literal `+` through the client so it is not decoded as a space. Do not use OpenAlex's uppercase Boolean grammar as a substitute.

## Apply requested filters and page

| Requirement | Parameter |
| --- | --- |
| Journal restriction | `venue=Nature` or a comma-separated set of confirmed eligible names. |
| Inclusive years | `year=2020-2024`, `year=2020-`, or `year=-2024`. |
| Inclusive dates | `publicationDateOrYear=2020-01-01:2024-12-31`. Records with unknown exact dates are treated as January 1 of the known year, so verify strict day-level criteria separately. |
| Work types | `publicationTypes=JournalArticle,Review` includes either type when requested. |
| Subject | `fieldsOfStudy=Medicine,Biology` includes either named field when requested. |
| Minimum citations | `minCitationCount=<integer>`, only when requested. |
| Accessible PDF | `openAccessPdf` is a presence-only parameter, only when requested. It does not establish reuse rights. |

Bulk search returns up to 1000 records per call. It does not accept `limit` or `offset`. Repeat the same request with `token=<returned token>` until no token remains or the inspection limit is reached. The `total` is an estimate. Record actual retrieved/inspected counts. Do not request nested citation/reference lists in bulk search. Fetch those separately. Leave the stable default paper-ID order unless a different order is requested.

For a title/author verification search, `/paper/search?query=<plain citation terms>&limit=5&fields=<fields>` returns candidate records. Its query has no special Boolean syntax. Replace lexical hyphens with spaces if they prevent matching. It accepts the venue restriction too when used for discovery. Follow `next` as the next `offset`, preserving filters, with `limit` at most 100. This endpoint exposes at most 1000 relevance-ranked results. Do not present it as exhaustive retrieval. An author name in the query is not an author-ID filter; verify returned authors.

## Exact records and citation edges

Use a native `paperId` or a supported prefixed ID, such as `DOI:10.18653/v1/N18-3011`, `PMID:<pmid>`, or `ARXIV:<arxiv-id>`, in `/paper/{paper_id}`. Encode it as a path value. Request the bibliographic fields above and compare identity/version before counting a confirmation. Do not first run a relevance search when an exact external ID is available.

Request `/paper/{paper_id}/references?fields=title,authors,year,venue,externalIds&limit=100` for backward edges. Request the analogous `/citations` path for forward edges. Pass a returned `next` value as `offset` for the next page. The documented maximum `limit` is 1000. The paper fields appear inside `citedPaper` or `citingPaper`, not at the edge's top level. Keep unresolved/null targets separate and do not fabricate their metadata. Citation lists provide relationships, not evidence of endorsement.

Missing abstracts can reflect licensing limits even when the website displays text. Keep them missing or record a separately inspected abstract with its own provenance. Preserve author names and IDs, DOI case as returned, publication types and reported access/license metadata.

## Errors and website fallback

For 400, check fields against the chosen endpoint and check query/filter syntax. For 404 on an exact lookup, record no match in this database. For 429, honor Retry-After, retry at most twice with increasing delay, then stop the route. Treat transport/5xx failures as unresolved after bounded retries.

If API access remains unavailable, try [Semantic Scholar](https://www.semanticscholar.org/), search the topic and apply the visible publication venue filter to an eligible journal before inspecting results. If no usable venue control is exposed, mark Semantic Scholar unavailable for topic discovery and use exact DOI/title searches only for verification. Continue through OpenAlex, Crossref, and every other applicable scholarly provider. Never substitute a general web search or web-search results. Preserve visible counts and limitations; do not claim API pagination from website results.

## Official fallback documentation

- [Academic Graph API](https://api.semanticscholar.org/api-docs/graph).
- [Machine-readable schema linked by that page](https://api.semanticscholar.org/graph/v1/swagger.json).


## Deep secondary discovery policy

When depth is deep, follow [the second-round procedure](secondary-discovery.md) for backward-reference overlap counting and known-target retrieval. A relevant target cited by at least two distinct initial works may bypass the CSV journal filter after identity resolution; a deposited identifier or journal reference alone does not establish this exception. Single-paper targets keep the ordinary journal rule. This never permits an unrestricted topic search or a second citation hop. Quick/normal runs do not automatically expand the pool through citations.
