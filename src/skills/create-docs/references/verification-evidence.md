# Verification evidence

Use this contract after a real Create Docs invocation, when handing completed output to Spawn Evals. It checks navigation between supplied documentation pages and fragments targeting those pages. It does not establish prose quality, coverage, factual accuracy, all broken links, or command correctness.

Follow [the runner contract](../../spawn-evals/references/runner.md). Put the resolved mode under `constraints.mode`, with its explicit-request provenance. Include every authored UTF-8 documentation source in `output_files`. Also include complete rendered HTML snapshots from the actual Markdown renderer or Nextra preview, with a distinct output key per page. These are temporary verification artifacts, not published source pages.

Supply these evidence fields:

- `pages`: a nonempty array, with one object per documentation page. Each object has exactly `route`, `source_key`, and `html_key`. Both keys identify entries in `output_files`. Include maintained documentation pages participating in navigation as well as newly authored pages.
- `landing_route`: the route of the documentation landing page.

Use canonical absolute paths on one synthetic origin for `route`, for example `/index.md` and `/how-to/run-locally.md` for basic Markdown, or `/` and `/how-to/run-locally` for Nextra. Match the renderer's actual link resolution and URL prefix. The checker uses `https://docs.invalid` only as a normalization base and never contacts it. For basic output, keep `.md` hrefs in the rendered HTML when those are the links readers use in the repository. If the renderer rewrites links, use its rendered URL scheme consistently instead.

For Nextra, capture rendered DOM after navigation is available. Include full HTML with real anchor `href` values and element IDs, not screenshots, a model-authored link list, or a rewritten summary. For basic, render each complete page with the intended Markdown dialect. Preserve IDs and links. Put snapshots in `output_files` so the runner reads their complete text.

The page inventory must cover the complete agreed documentation set. The checker cannot discover an omitted page from the repository. Missing or unreadable rendered evidence is unverified. An orphaned page is a confirmed failure. It also checks nonempty fragments on links whose target is in the supplied page set. It ignores links outside that set, including external links, assets, implementation links, and unknown routes. Check those separately during the owning workflow's full link review.

The graph check traverses links from the landing page. Every supplied page must be reachable. Basic output also requires each page to reach the landing page, directly or through parent pages. Interactive output can use theme navigation for those links. If a page intentionally sits outside the docs set, settle its scope before constructing the inventory instead of excluding a failed page after the check.

Store invocation records and rendered snapshots outside published docs. Pass actual unavailable evidence as missing and report NOT PASSED — UNVERIFIED. Do not create synthetic pages to obtain a result.
