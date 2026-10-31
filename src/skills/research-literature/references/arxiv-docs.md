---
name: "arxiv-docs"
description: "Operational reference for arXiv identity and version lookups, authorized searches, Atom records, and access limits."
version: "0.2.1"
created: "2026-10-30"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "arXiv"
type: "reference"
status: "experimental"
---

# arXiv search and lookup reference

Read for known-preprint identity/version lookup, or topic discovery when the caller explicitly permits it under the discipline's journal policy. Relevant API behavior was checked against the official manual on 2026-10-30.

## Access and role

Use HTTPS GET at `https://export.arxiv.org/api/query`. No key is needed. Space consecutive calls by at least three seconds and cache repeated lookups. Encode parameters through the client. Responses are Atom XML, including some error responses.

While the journal filter is active, arXiv is verification-only: it has no equivalent publishing-journal allowlist restriction. Its `jr` search field is free-text journal-reference metadata, not a substitute for that restriction. A deposited journal reference or DOI can help verify a known candidate but does not waive CSV eligibility. Do not start a broad topic search unless the caller permits broader discovery.

## Look up a known record

Use `id_list=<arxiv-id>` for an exact arXiv lookup. Preserve a version suffix when checking a particular version. Multiple IDs are comma-separated. For example, this is an illustrative known-paper lookup:

```sh
curl --get 'https://export.arxiv.org/api/query' \
  --data-urlencode 'id_list=1706.03762v1'
```

An unversioned ID returns the latest version. Keep both the base identifier and returned version. If only title/authors are known, use a narrow `search_query` such as `ti:"known paper title" AND au:known_surname`, inspect candidates, and compare identity. This verification lookup does not authorize adding unrelated search hits. Avoid sending both `id_list` and `search_query` unless the intended operation is to restrict those IDs by that query.

## Search and filter when discovery is authorized

| Parameter or field | Meaning |
| --- | --- |
| `search_query` | Query made from field terms, uppercase `AND`, `OR`, `ANDNOT`, parentheses and double-quoted phrases. |
| `ti:`, `abs:`, `au:` | Title, abstract and author terms. Author terms are not unique person identifiers. |
| `cat:` | arXiv category, such as `cat:cs.LG`, only when the requested subject scope warrants it. |
| `submittedDate:[202001010000 TO 202412312359]` | Inclusive submission-date range in UTC. It is not journal publication date. |
| `start` | Zero-based result offset. Start at 0. |
| `max_results` | Working page size, such as 100. Use slices no larger than 2000. The manual describes a 30,000-result retrieval ceiling. |
| `sortBy` | `relevance`, `submittedDate`, or `lastUpdatedDate`. |
| `sortOrder` | `ascending` or `descending`. |

An illustrative authorized topic request uses `search_query=(ti:"climate adaptation" OR abs:"climate adaptation")`, `start=0`, `max_results=100`, `sortBy=relevance`, and `sortOrder=descending`. Do not add date/category limits unless requested. Add exact-date criteria only after identifying which date the caller means.

Read `opensearch:totalResults` and actual entries separately. Advance `start` by entries retrieved while keeping the query, sort and filters unchanged. Stop at the observed total, empty page, caller's limit, or API ceiling. Record truncation and changing-result-set limitations. Do not interpret an Atom error entry as a paper.

## Extract identity, abstract and version evidence

Parse XML using these namespaces:

```text
atom       http://www.w3.org/2005/Atom
opensearch http://a9.com/-/spec/opensearch/1.1/
arxiv      http://arxiv.org/schemas/atom
```

Retain each Atom entry's `id`, `title`, all `author/name` values, `summary`, `published`, `updated`, `category`, and `link` values. `summary` is the abstract. Also retain `arxiv:doi`, `arxiv:journal_ref`, and `arxiv:primary_category` when present. Link attributes distinguish the abstract page, PDF and deposited DOI. Return full-text links without downloading the paper.

Resolve a deposited journal DOI in a scholarly database and compare title, authors and version before linking the preprint to a publication. Keep separate preprint and journal records. Missing journal metadata or an old submission date does not establish that a preprint is unreviewed, rejected or superseded. arXiv provides no reference/citation-list endpoint in this query API; use a supported scholarly graph for those edges.

## Errors and website fallback

Inspect HTTP status and Atom error entries. Correct invalid IDs or syntax after checking the error. Retry transient transport/5xx failures at most twice with backoff, maintaining request spacing. Stop on persistent access failures.

If the API is blocked, open `https://arxiv.org/abs/<known-id>` for the known candidate, inspect its version history and deposited DOI/journal reference, and record website access. For title-based verification, use the website's advanced title/author search and inspect actual record pages. It remains verification-only while the journal filter is active.

## Official fallback documentation

- [API query syntax, paging and Atom fields](https://info.arxiv.org/help/api/user-manual.html).
- [arXiv identifier and version conventions](https://info.arxiv.org/help/arxiv_identifier.html).


## Deep secondary discovery policy

When depth is deep, follow [the second-round procedure](secondary-discovery.md) for backward-reference overlap counting and known-target retrieval. A relevant target cited by at least two distinct initial works may bypass the CSV journal filter after identity resolution; a deposited identifier or journal reference alone does not establish this exception. Single-paper targets keep the ordinary journal rule. This never permits an unrestricted topic search or a second citation hop. Quick/normal runs do not automatically expand the pool through citations.
