---
name: "research-cli"
description: "Offline CLI inputs, outputs, dependency checks, replacement rules, and phase validation commands for Research."
version: "0.3.2"
created: "2026-10-30"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "Pandoc"
type: "reference"
status: "experimental"
---

# Research CLI operations

Read before using [research.py](../scripts/research.py). Run with an available Python 3.10+ interpreter. Python helpers use the standard library; citation parsing/rendering and conversion additionally require Pandoc with built-in citeproc. Scripts never contact a model or network service. Do not install missing dependencies automatically.

## Standard sequence

Commands below run from the repository root. `/private/tmp/research-project` is an illustrative new task-local directory; replace it with the actual project path. The topic is illustrative, not a prefilled evidence claim. Omit `--formats` when chat is a skill default; passing it marks the value as request-sourced. Likewise, pass `--journal-preset` only for an explicit user choice. Preserve any caller-resolved provenance when completing brief.json.

```sh
python skills/research/scripts/research.py init --project /private/tmp/research-project --topic 'Question to research' --request 'Original request' --type research-report --depth normal --formats chat
python skills/research/scripts/research.py doctor --formats chat
python skills/research/scripts/research.py validate --project /private/tmp/research-project --phase brief
```

Complete records through the owning phase before validation. Continue with discovery, evidence and outline validation; they intentionally reject initialized pending records. When retrieved source metadata is ready, generate keys before writing:

```sh
python skills/research/scripts/research.py citations --project /private/tmp/research-project --prepare
python skills/research/scripts/research.py validate --project /private/tmp/research-project --phase outline
python skills/research/scripts/research.py assemble --project /private/tmp/research-project
python skills/research/scripts/research.py validate --project /private/tmp/research-project --phase draft
```

Review and polish draft.md, then run draft validation again to obtain its current `draft_sha256` and `inputs_sha256`. After actually rechecking the relevant claims, copy these into both completed review records and compile:

```sh
python skills/research/scripts/research.py validate --project /private/tmp/research-project --phase review
python skills/research/scripts/research.py citations --project /private/tmp/research-project --replace
python skills/research/scripts/research.py validate --project /private/tmp/research-project --phase final
```

Final validation also requires requested exports; run it after producing and inspecting those formats. Use `--replace` on citations after preparation because it deliberately regenerates bibliography.json and citation-keys.json. For other styles, pass `--style /absolute/path/style.csl` at initialization or citation compilation. Prefer recording the settled style in the brief. Only self-contained local CSL styles with citation and bibliography sections are accepted; no remote styles are fetched.

## Commands and results

| Command | Required inputs | Generated output |
| --- | --- | --- |
| init | `--project`, `--topic`; optional original request, type, depth, language, formats, style, journal preset | Manifest, pending records and prescribed numbered section files. |
| rank-references | `--project` with deep depth and completed initial reference-list attempts; optional `--replace` | Frozen ranked citation-candidates.json; no network/model calls or Pandoc dependency. |
| validate | `--project`, `--phase brief/discovery/evidence/outline/draft/review/final` | JSON completeness receipt on stdout; no fabricated review results or file writes. |
| assemble | `--project` and validated outline/sections | draft.md and its SHA-256 in stdout. |
| citations --prepare | `--project` with gate-qualified source metadata/provenance | bibliography.json and citation-keys.json. |
| citations | `--project` with draft/source metadata and style | Bibliography, key map, report.md, cited-sources.json, citation-receipt.json. |
| export | `--input`, `--format md/latex/pdf/docx`, `--output` with matching extension | Converted file, local assets for text formats, and `.receipt.json` companion. `--project` registers a canonical report export. |
| doctor | Optional requested `--formats`, `--pandoc`, `--soffice` | Tool paths/versions or precise missing prerequisites. |

Every operation prints a JSON object with schema_version 1, status, outputs, and command-specific data or an error code/message. Exit 0 means the requested mechanical operation succeeded, 1 means invalid inputs or failed conversion, and 2 means an unavailable dependency. `--help` is conventional human-readable CLI help. An output receipt does not certify factual or scientific quality.

`init` accepts repeatable `--source 'DOI, URL, title or full citation'` and `--author 'Name or ORCID, with identifying context'`. These preserve original values in `brief.source_requests`; they perform no retrieval. Research Literature resolves them and fills one `search_receipt.requested_inputs` outcome per request. Omit both options for normal topic discovery.

`init --resume` requires matching topic/type and existing standard artifacts; it never resets the project. The reference-ranking command fills only its exact untouched pending scaffold without `--replace`. Other generated outputs refuse overwrite unless `--replace` is supplied. Export cannot overwrite its input. All generated content is staged before publication; dependency or conversion failures leave existing outputs intact. Filesystem errors during the final publication can still require recovery from retained source inputs.

## Citation syntax

Use the generated key exactly. For example, if citation-keys.json maps a source to `r0123456789abcdef`, Pandoc forms are `[@r0123456789abcdef]`, `[@r0123456789abcdef, p. 3]`, and narrative `@r0123456789abcdef`. Multiple sources share a group separated by semicolons. Preserve locators from actual inspected sources. `[@MISSING]` and `SOURCE_NEEDED` are unfinished draft markers, not final citations.

The helper parses Pandoc's AST instead of applying regular-expression substitution to citations. Code examples and ordinary links are not citations. Manuscript metadata cannot inject bibliography, nocite, CSL or raw includes; pass bibliography/style through explicit CLI options. Unknown keys fail before publishing a report.

## Formats and dependencies

Use [export requirements](export.md) for exact format operations, content limits, bundled LibreOffice and visual inspection. Pandoc paths can be supplied with `--pandoc`. PDF always requires an explicit `--soffice` path resolved from the host's bundled dependency lookup. The CLI never falls back to an unrelated desktop installation or a TeX engine.

## Rank deep backward references

```bash
python skills/research/scripts/research.py rank-references --project /private/tmp/research-project
```

This operation requires deep depth and completed reference-list attempts on every initial source. It uses only local JSON and the standard library: no Pandoc, network or model. Inputs are brief.json and initial records/reference lists in sources.json. Output is citation-candidates.json plus a JSON receipt with candidate count and published path.

The first run fills the exact untouched pending scaffold created by init. Existing ranked/screened output requires `--replace`; altered pending scaffolds are rejected. Replacement re-derives the graph and resets candidate screening decisions, so rerank before recording dispositions. Frozen initial source IDs must remain unchanged; newly discovered sources use secondary level. Identity/reference changes require explicit reranking and fresh screening. Do not edit a hash to bypass this check.

Fill candidate dispositions and source annotations as defined in the [artifact contract](artifacts.md#secondary-discovery-records). Then run `validate --phase discovery`; it checks depth, the frozen graph, one-hop additions, overlap counts, recorded coverage and the singleton journal rule. The later review/final validators retain these checks.


## Depth names and defaults

`--depth` accepts quick, normal and deep; omitted depth selects normal. These names replace light, default and thorough as depth values. Journal presets remain lenient, default and strict, with default selected when omitted. Quick/normal use a simple crawl; `rank-references` is deep-only. Explicit numeric request bounds still override depth defaults.

For an existing project using an old depth value, deliberately map light to quick, default to normal or thorough to deep in brief.json before resuming. Reconcile skill-default numeric bounds against the current depth table while preserving request-sourced overrides. Revalidate discovery and regenerate stale reviews/compiled artifacts after changing the brief. Initialization/resume does not silently reset existing records.


## Qualify discovery before writing

Use [Research Literature's standalone qualification CLI](../../research-literature/references/qualification-gate.md) after collecting raw candidates into retrieved-sources.json and completing literature-contract.json. The final gate writes the canonical sources.json; use --replace deliberately for the pending project scaffold and later generated outputs. It preserves its input ledger. Run --phase anchors first for deep discovery, then rank-references with --inventory /absolute/project/anchor-sources.json. Freeze seeds before the backward-reference round. The final gate accepts --expansion /absolute/project/citation-candidates.json.

A top_up_required receipt blocks discovery acceptance. Conduct one additional query pass, append its receipt/candidates with search_pass top_up and rerun with --attempt top_up --replace. After that, return_shortfall is an honest usable pool limit. validate --phase discovery checks the bound receipts, generated list/inventory and retry history; source-count targets for the final cited report remain separate.
