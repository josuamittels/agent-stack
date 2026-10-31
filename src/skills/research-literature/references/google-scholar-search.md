---
name: "google-scholar-search"
description: "Browser reference for journal-restricted Google Scholar searches, citation checks, version links, and access limits."
version: "0.2.1"
created: "2026-10-30"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "Google Scholar"
type: "reference"
status: "experimental"
---

# Google Scholar website search reference

Read only when using Google Scholar's authorized browser route. This workflow uses the website, not an assumed public search API or a scraping service. Relevant controls were checked against Google's search help on 2026-10-30.

## Search eligible journals

1. Open [Google Scholar](https://scholar.google.com/). Open the side menu and select **Advanced search**.
2. Put planned topic terms in **with all of the words**, alternatives in **with at least one of the words**, or a required phrase in **with the exact phrase**. Preserve the caller's concepts rather than copying another database's query grammar.
3. In **Return articles published in**, enter one confirmed CSV-eligible journal's full name. Run separate searches for other journals; do not assume OR syntax in that field. Set author and year fields only when requested.
4. Submit the query. Record the resulting URL, entered fields, date, visible approximate total and any active restrictions. Inspect publishing-journal identities on the actual linked records and apply the CSV rule again.
5. Move through the visible result pages until the planned inspection limit, no next page, or an access block. Record pages and records inspected. Do not describe an approximate total or capped result list as exhaustive coverage.

If the publication restriction is absent, cannot be retained, or produces ambiguous journal matches that cannot be resolved, mark Scholar verification-only. Do not replace it with unrestricted topic discovery. If a changed layout prevents identifying the required controls, report that route unavailable instead of guessing hidden query parameters.

## Verify a known citation

Search the exact title in double quotes. Add an author term if needed, using the documented `author:` operator, such as `author:"d knuth"`. Open the matched publisher, repository or scholarly database record and compare title, authors, year, DOI, venue and version. A Scholar snippet, citation export or title match alone is not confirmation of all bibliographic fields.

Use **All versions** to inspect alternate records and possible publication versions. Keep the actually inspected version and evidence URLs. Scholar and a second route to the same indexed source are not two additional scholarly databases. If the evidence comes only from a web/publisher page, preserve that provenance without counting it as another database confirmation.

## Cross-reference citations

From a confirmed seed, use **Cited by** for forward citation candidates. Use **Related articles** only as a similarity relation. **All versions** is a version grouping, not a citation edge. Record the seed, relationship, page URL, visible count and candidates inspected. Route newly linked works through journal-restricted discovery before inclusion. Do not read full papers merely to extract backward references under this discipline.

Do not substitute the result snippet for an abstract. Open an actual record containing an abstract and identify its source, or report the abstract missing. Return available full-text URLs without downloading or appraising the paper.

## Access limits

Stop at a CAPTCHA, unusual-traffic notice, sign-in requirement or persistent block. Do not bypass it, configure proxies, purchase third-party search access or claim a failed search returned zero works. Continue eligible API routes and report Scholar's limited availability.

## Official fallback documentation

- [Google Scholar search help](https://scholar.google.com/intl/en/scholar/help.html), including advanced search, citation links, versions and coverage limits.


## Deep secondary discovery policy

When depth is deep, follow [the second-round procedure](secondary-discovery.md) for backward-reference overlap counting and known-target retrieval. A relevant target cited by at least two distinct initial works may bypass the CSV journal filter after identity resolution; a deposited identifier or journal reference alone does not establish this exception. Single-paper targets keep the ordinary journal rule. This never permits an unrestricted topic search or a second citation hop. Quick/normal runs do not automatically expand the pool through citations.
