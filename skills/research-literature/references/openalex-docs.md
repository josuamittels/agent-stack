---
name: "openalex-docs"
description: "Operational reference for searching and filtering OpenAlex works and interpreting returned records."
version: "0.2.0"
created: "2026-10-25"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "OpenAlex"
type: "reference"
status: "experimental"
---

# OpenAlex Search and Filter Reference

Use this reference for routine literature searches through the OpenAlex API. Read the linked official pages only when a request fails, this reference does not cover a needed behavior, or observed behavior appears to have changed. This guide was checked against OpenAlex's official documentation on 2026-10-25.

## Request basics

- API base URL: `https://api.openalex.org`.
- Use `/works` to find publications, `/authors` to resolve researchers, and `/sources` to resolve journals and other sources. All return JSON.
- Basic metadata requests work without a key. A free API key is required to follow cursor pagination after its first page. Use only credentials already available in the environment; do not create, expose, or request credentials as part of a literature search.
- Pass request parameters through an HTTP client's parameter map so it encodes spaces, quotes, `|`, and other reserved characters.

OpenAlex also provides a website search for locating works and their OpenAlex IDs. Use the website as a fallback only when an available API route cannot reach the API. The website may not expose the API's filters, result totals, fields, or pagination; report those limits rather than inferring API behavior from the visible records. A web-search result that points to an OpenAlex page is not, by itself, a search performed in OpenAlex.
- OpenAlex returns its curated core works corpus by default. State when the `corpus` parameter was changed, because `corpus=all` includes a larger expansion set and changes result counts.

## Search modes

Use one search parameter per request:

| Parameter | Searches | Use |
| --- | --- | --- |
| `search.title_and_abstract` | Work title and abstract | Preferred for focused topic searches. |
| `search.title_abstract_keywords` | Title, abstract, and relevant OpenAlex keywords | Broader topical discovery. |
| `search` | Title, abstract, full text, and keywords | Broad discovery when full-text matching is useful. |
| `search.semantic` | Meaning of the work title and abstract | Find conceptually similar work when the query uses different terminology. |

Search supports uppercase `AND`, `OR`, and `NOT`. Quote a phrase for phrase matching. Terms without an operator are treated as `AND`; a leading minus sign does not exclude a term. Stemming and stop-word removal apply unless an `.exact` search parameter is used. The complete request URL is limited to about 4 KB. If a large Boolean expression exceeds it, split its `OR` alternatives across requests and union results by OpenAlex work ID.

Semantic search accepts up to 2,000 characters and returns at most 50 works per query. It permits filters and `select`, but it cannot be combined with another search parameter. It does not support the `cited_by_count` or `last_known_institutions.country_code` filters. Use it as a separate discovery query and deduplicate its results with other searches.

## Resolve named filters

Resolve people and journals before filtering. Names can be ambiguous, and OpenAlex filters should use identifiers.

1. Search `/authors?search=<name>` and confirm the candidate with available evidence such as ORCID, affiliation, and known works. Filter works with `authorships.author.id:<author-id>`.
2. Match a journal in `journals.csv` by ISSN or eISSN when that file is relevant. Resolve it through `/sources` and confirm the ISSN and title. Filter with `primary_location.source.id:<source-id>`. The source's ISSN can also be used under `primary_location.source.issn` where supported.
3. If identity remains ambiguous, report the candidates and continue without that filter rather than selecting one silently.

## Filters

Put work filters in the `filter` parameter. Commas combine different conditions with AND. Use `|` for OR values of one filter field, up to 100 values. OR cannot span different fields. Prefix a value with `!` to exclude it. Numeric fields support `<` and `>` comparisons. Filters are case-insensitive.

Useful work filters include:

| Filter | Example | Purpose |
| --- | --- | --- |
| `authorships.author.id` | `authorships.author.id:A123...` | Match a resolved author. |
| `primary_location.source.id` | `primary_location.source.id:S123...` | Match a resolved journal or source. |
| `publication_year` | `publication_year:2020-2024` | Limit publication years. |
| `from_publication_date`, `to_publication_date` | `from_publication_date:2020-01-01,to_publication_date:2024-12-31` | Set inclusive publication date bounds. |
| `type` | `type:article` | Limit the work type. |
| `topics.id` | `topics.id:T123...` | Filter by a resolved OpenAlex topic. |
| `language` | `language:en` | Filter metadata language. |
| `is_oa` | `is_oa:true` | Require an open-access location. |
| `has_fulltext` | `has_fulltext:true` | Require downloadable OpenAlex full text to be available. |
| `cited_by_count` | `cited_by_count:>10` | Apply a user-requested citation threshold. |

Combine filters only when the user intends all conditions together. Do not add citation, language, open-access, date, or type limits by default. Citation counts, search ranking, and journal scores are discovery context, not article-quality measures.

## Paging and returned fields

- `per_page` defaults to 25 and supports 1–100. Use 100 when paging through a result set.
- Basic `page` pagination can retrieve at most the first 10,000 results. Do not rely on legacy `per_page=200` behavior.
- Cursor paging starts with `cursor=*`; follow `meta.next_cursor` until it is `null`. A free API key is required after the first cursor page. Without one, use basic paging within its limit and report when results beyond that limit are inaccessible.
- Record `meta.count`, how many results were actually retrieved and inspected, and the exact query and filters. A total count is not the number reviewed.
- Use `select` to request only needed top-level fields. It cannot select nested paths. Select the containing object, then read its fields.
- Useful fields include `id`, `doi`, `title`, `publication_year`, `publication_date`, `type`, `authorships`, `primary_location`, `best_oa_location`, `open_access`, `abstract_inverted_index`, `topics`, `cited_by_count`, and `content_urls` when returned.

## Abstracts and full-text links

OpenAlex represents abstracts in `abstract_inverted_index`, a mapping from each word to one or more positions. Reconstruct plain text by placing each word at its recorded positions and joining the ordered words with spaces. If the field is null or absent, report the abstract as unavailable. Some reconstructed abstracts include trailing headings or keywords; flag obvious cases rather than silently editing the record.

Use `best_oa_location` or `open_access.oa_url` to return an available open-access landing page or PDF link. Include the location's version and license when available. `content_urls` are OpenAlex-hosted download URLs and require an API key to fetch. Return these only as links when useful. This discipline does not download or read full papers.

## Error handling

If a request fails, inspect the HTTP status and message before changing it. For `400`, check field names, values, query encoding, and URL length. For `401` or `403`, check whether the chosen endpoint or cursor page requires authentication. For `301`, follow the redirect to the merged entity. For `404`, verify the identifier. For `429`, slow down or stop if the available budget is exhausted; do not retry in a tight loop. Retry transient `500` responses with bounded backoff.

When the failure points to an undocumented or changed parameter, open the relevant official page below and update the request using that documentation. Do not guess a replacement field. If the issue persists, report the exact request shape, error, and remaining access limit.

## Official fallback documentation

- [API reference](https://help.openalex.org/api/) — endpoints, base URL, response envelope, and general request mechanics.
- [LLM Quick Reference](https://help.openalex.org/api/llm-quick-reference/) — concise HTTP patterns, common filter fields, and query limits.
- [Filter reference](https://help.openalex.org/api/filtering/) — filter syntax, logical operators, and related-entity filters.
- [Search reference](https://help.openalex.org/api/searching/) — searchable fields, Boolean and phrase syntax, URL-length behavior, and scoped search parameters.
- [Semantic Search](https://help.openalex.org/api/semantic-search/) — semantic-query behavior and limits.
- [Paging](https://help.openalex.org/api/paging/) — page and cursor rules, maximum page size, and key requirement for cursor continuation.
- [Select Fields](https://help.openalex.org/api/selecting-fields/) — top-level `select` behavior and limitations.
- [Work attributes](https://help.openalex.org/data/works/attributes/) — work fields, abstract representation, open-access locations, and full-text URLs.
- [Authorships](https://help.openalex.org/data/authorships/) — author identity and authorship-list limits.
- [Locations](https://help.openalex.org/data/locations/) — versions and source details for work locations.
- [Error handling](https://help.openalex.org/api/errors/) — status codes, common failures, and retry guidance.
