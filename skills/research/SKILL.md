---
name: "research"
description: "Produce source-grounded research reports and literature reviews through repeatable stages, journal-filtered discovery, academic writing, deterministic citations, and Markdown, LaTeX, PDF or Word export."
version: "0.13.0"
created: "2026-10-26"
updated: "2026-10-31"
author:
  - "Josua Mittelstaedt"
references:
  - "Federico De Ponte"
  - "Pandoc"
  - "PRISMA"
  - "Cochrane"
  - "Joanna Briggs Institute"
  - "ALLEA"
type: "skill"
status: "experimental"
---

# Research

Produce a source-grounded research report or literature review through a fixed, caller-run process. Research Literature owns scholarly discovery. Research owns reading, appraisal, synthesis and acceptance. Natural Writing owns drafting and polishing prose. Offline scripts own scaffolding, assembly, citation formatting and conversion; they never call a model or a network service.

## Scope

Support `research-report` and `literature-review`, with the fixed structures defined in [the workflow reference](references/workflow.md). Do not invent a manuscript, thesis or systematic-review template. Named formal review methods require the appropriate conduct and reporting standards; a report type or depth alone does not establish them. Primary records, official data, books and suitable grey literature may supplement scholarly sources when they answer the question.

### Boundaries

Do not invent evidence, methods, data, findings, locators, research steps or review results. Preserve contrary evidence and important uncertainty. Journal eligibility and multi-database identity agreement do not establish study quality or claim support. Keep the Research Literature journal rules in force across discovery routes, including its deep-only overlapping backward-reference exception. Providers without usable journal restrictions otherwise serve verification only while the filter is active. Do not obtain credentials, install dependencies or publish outputs as an automatic fallback.

## Evaluation contract

Evaluate a completed real use only. Helper regression tests exercise scripts, not research quality or this authored skill. For standalone reports, run the existing objective package at step 9. As a helper, return the report, cited-source inventory, receipts and unresolved limits to the owning workflow without a nested evaluation. Explicit instructions to skip evaluation take precedence and must be reported. Conversion or completeness checks are not scientific validation.

## Inputs

Use the topic or question, intended audience and use, requested deliverable or format, language, any supplied sources or constraints, and desired research depth. Select `research-report` unless the user requests `literature-review`. These are the only supported document templates. Select chat unless another format is requested; also support md, latex, pdf and docx. The same required sections and working artifacts apply at every depth. Ask through [ask-user-question](../ask-user-question/SKILL.md) only for a missing choice that would materially change what evidence can answer the question. First use [think-harder](../think-harder/SKILL.md) if context or evidence might resolve the choice; otherwise state a reasonable assumption and proceed.

Accept a depth of **quick**, **normal**, or **deep**. If the user gives a word count, source range, deadline, field, date range, geography, population, or source preference, honor it and note any resulting coverage limit. Default to **normal** depth when no depth is specified.

Accept **lenient**, **default**, or **strict** journal selection independently of depth. Journal selection defaults to **default**. Tell the user they can request **lenient** for broader venue coverage or **strict** for a narrower selection, then proceed with the default unless they specify otherwise. Use [Research Literature's journal-selection rules](../research-literature/SKILL.md#journal-selection) as the authoritative cutoffs and override policy. Honor requests for more lenient or stricter journal selection, explicit numeric thresholds, or disabling the filter. Keep the selection throughout follow-up searches. In deep research, also permit the bounded overlapping-reference exception defined by Research Literature; identify its evidence separately from explicitly requested exceptions.

The journal filter governs journal articles and reviews. Continue to use suitable primary records, official sources, books, and grey literature according to the question and stated inclusion criteria. Label their discovery separately. Journal eligibility does not establish individual study quality or replace the appraisal below.

Invoke [Natural Writing](../natural-writing/SKILL.md) as a writing helper with an academic writing focus. Pass the report language, audience, field, citation style, format, and depth; it owns language guidance and returns here without a separate evaluation. Use the field's established reporting guidance when the report type calls for it; consult a reporting checklist as a reporting aid, not proof that the underlying research was systematic or complete.

### Depth choices

Depth changes research effort and report scale. It does not change standards for source verification, fair representation, citation accuracy, or stating uncertainty.

| Depth | Search and inspection | Synthesis and report |
| --- | --- | --- |
| **Quick** | Simple crawl: focused initial searches, record verification and screening, with no second-round citation expansion. Aim for 8–12 substantive cited sources. | 800–1,600 words: a concise answer, key findings, disagreements and limitations, with methods and references. |
| **Normal** | Simple crawl across relevant databases, record verification and screening, with no second-round citation expansion. Inspect full text for sources carrying central claims. Aim for 16–24 substantive cited sources. | 2,000–4,000 words: a developed report with transparent methods, synthesis, source appraisal and competing explanations. This is the default depth. |
| **Deep** | Broader initial discovery plus the one-hop backward-reference round, screening overlaps first. Inspect full texts and compare methods, contexts and counterevidence. Aim for 32–64 substantive cited sources across both rounds. | At least 6,000 words, with no default maximum: detailed synthesis, evidence comparisons, uncertainty and limitations. |

Plan source discovery toward the upper source bound; be satisfied with the lower bound when no further helpful qualifying work is available. Research Literature's gate counts verified qualifying discoveries; Research's report evaluator separately counts substantive works actually cited. Do not add weak sources or filler text to meet either target.

The source and word ranges are default evaluation bounds when a user has not supplied a different numeric limit. A request-specific bound takes precedence. Do not add weak sources or pad prose to meet a bound; when the evidence or access cannot support it, report that limit and expect the corresponding objective check to fail or remain unverified. If the user asks for a formal systematic, scoping, or other named review, use its field-appropriate conduct and reporting standards; a depth label alone does not make a report systematic.

Accept optional citations, source papers (DOIs or other identifiers, URLs, titles, or full references), and authors the user wants considered. Preserve them verbatim as `brief.source_requests` with stable IDs and kind `work` or `author`. Use repeatable `init --source` and `--author` arguments, or populate that same field explicitly when completing the brief. With no supplied inputs, leave the list empty and proceed as usual.

Pass every entry to Research Literature for explicit lookup or targeted author search alongside normal topic discovery. Carry its per-input outcomes into `sources.search_receipt.requested_inputs`; a sufficient source count does not excuse ignoring an entry. Include resolved eligible papers in the appraisal pool. Use them in the report when relevant and supported by inspection; do not attach citations to unsupported claims just to satisfy a request. For an eligible requested work ultimately not cited, record the appraisal/selection reason and report it in the caller handoff. Likewise explain requested authors with no eligible relevant work, exclusions, inaccessible sources and unresolved identities. Preserve the journal filter and other criteria unless the user explicitly overrides them; a supplied citation alone is not an override.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/SKILL.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/SKILL.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

Use [the workflow and handoff reference](references/workflow.md) for fixed section purposes, phase completion and repair ownership. Before editing a working record, read [artifact contracts](references/artifacts.md) for required fields and templates. Read [CLI operations](references/cli.md) before running a helper. All Markdown references have metadata headers; machine-readable templates keep their native JSON/CSL formats.

### 1. Initialize the brief and project

Use the CLI `init` command to create a new task-local project from templates. Pass the original request, topic, type, depth, language, requested formats and selected journal preset. Use the requested output location or a new project folder in the task workspace. Never reuse a nonempty directory silently. `--resume` checks the existing topic/type and preserves its files.

Complete brief.json with a bounded question, scope, audience, field, actual research method and constraints with request/default provenance. Keep research depth independent of journal selection. Preserve explicit numeric overrides, category restrictions and exceptions. Default citation style is the bundled APA 7 style; a different style requires an explicit local CSL file. Record consequential assumptions instead of asking for settled preferences again.

Invoke [Think Deeper](../think-deeper/SKILL.md) to select appropriate primary evidence, search/appraisal methods and a practical outside check that could challenge the synthesis. Choose PICO or another framework only if it fits the question. Record the method and planned outside check in the brief. Mark the brief complete and run `validate --phase brief` before discovery.

### 2. Discover and screen sources

Invoke [Research Literature](../research-literature/SKILL.md) with the research depth, original question/context, concepts, every `brief.source_requests` entry (preserving IDs and original inputs), other seed references, criteria, result target, journal rules and explicit overrides. Request the source fields in sources.json's contract, including original provider records/provenance, search receipt, journal eligibility, identity checks, abstracts and access links. Preserve source IDs and reported limits. Request initial discovery only in this first handoff at every depth. Research Literature runs its pool-phase gate and returns verified working records; defer the final source-count retry decision until Research has combined any planned separately retrieved sources. Research coordinates the secondary handoff for deep runs after that combination. The discipline's records are discovery inputs, not evidence that full papers were read.

Add field-appropriate primary/official/grey sources separately when useful and record how each was actually retrieved. Screen against the question and inclusion criteria. Distinguish discovered, screened, included and full-text-inspected sources. Check version, date and retraction/correction notices where relevant. Record exclusions and access gaps. Preserve journal filters on scholarly discovery, and report blocked providers without calling them empty searches. For deep depth, combine the initial literature results with any separately retrieved primary/official sources, then invoke Research Literature for the secondary pass with those raw records and existing search/seed receipts. Run its anchor-phase gate to select qualified initial works. Retrieve reference lists for those works into the raw ledger, preserving unavailable/partial coverage and resolved or unresolved identities, and rerun the anchor gate to refresh anchor-sources.json after those input changes. Freeze seeds by running `rank-references --project <directory> --inventory <directory>/anchor-sources.json` before screening candidates, then review overlapping references before single-paper references. Save dispositions in citation-candidates.json, add eligible new works as secondary discoveries, and record the graph-backed journal exception only for overlap counts of at least two distinct initial works. Do not expand another hop. Follow [the secondary-round procedure](../research-literature/references/secondary-discovery.md) and [artifact fields](references/artifacts.md#secondary-discovery-records). Quick/normal runs leave the candidate scaffold pending and add no automatic citation discoveries.

Before accepting the completed discovery handoff, run [Research Literature's final gate](../research-literature/references/qualification-gate.md) against retrieved-sources.json and literature-contract.json, plus citation-candidates.json for deep runs. The helper writes sources.json, sources.md, excluded-sources.json, qualified-expansion.json and source-gate.json; preserve raw records. If below the minimum, Research Literature conducts one top-up and reruns the gate, then returns an honest shortfall if necessary. Top-up results never change frozen seeds. Do not proceed until the gate is handoff-ready.

Appraise secondary additions using the same evidence standards as initial sources. Describe both search rounds, the overlap exception and coverage limits in the methods and caller handoff. Run `validate --phase discovery`.

### 3. Appraise evidence and register claims

Read the full text of sources that carry central claims when accessible. Verify each key interpretation against the source itself. Extract the question, context, design or argument, data or materials, analysis, findings, limitations, and relevant funding or conflicts. Separate the authors' claims from the evidence and from your interpretation.

Assess sources against criteria appropriate to their role:

- For empirical studies, examine design fit, sampling or selection, measures, confounding, missing data, analysis, robustness, and whether the conclusion exceeds the results.
- For qualitative or interpretive work, examine context, material or participant selection, analytic process, positionality where relevant, and the connection between evidence and interpretation.
- For theory, assess definitions, assumptions, internal logic, explanatory reach, and engagement with serious alternatives.
- For historical, legal, policy, or technical primary sources, assess provenance, version, authorship, scope, and context; distinguish the source's text from its practical effect or later interpretation.
- For reviews and syntheses, inspect their search and inclusion methods, appraisal approach, synthesis, and date of coverage. A reporting checklist can reveal omissions but cannot validate conduct by itself.

Use a validated, design-specific appraisal tool when one applies and the report depth warrants it. Explain important judgments and uncertainty; do not convert a checklist score, journal label, or single composite rating into a substitute for reasoning. Do not infer a study's quality from abstract-only evidence.

Read only the gate-qualified sources.json as the included source pool; retain retrieved-sources.json and exclusion reasons for audit. A discovery shortfall after one top-up is a coverage limit, not permission to cite unverified works.

Save appraisals.json using the appraisal/finding templates. Record the actual inspection basis, findings and source locators. Metadata-only records cannot support extracted findings. Keep authors' claims, evidence and your interpretation distinguishable. An abstract-only proxy must retain that limitation.

Build claims.json with stable claim IDs, precise propositions, supporting and contrary finding references, qualifications and supported/qualified status. Remove unsupported claims or return to discovery/appraisal. Explain whether disagreements arise from definitions, methods, populations, timing or genuine uncertainty. Conduct quantitative pooling only when evidence and method justify it; otherwise state why narrative synthesis is appropriate. Run `validate --phase evidence`.

### 4. Structure the report

Complete outline.json's prescribed sections without changing their IDs, order or top-level headings. Assign each section its purpose, source IDs, claim IDs, inclusive word budget and neighboring context. Topic-specific subsections belong inside the synthesis sections. Use the selected depth's overall report bounds; do not pad sections or add weak sources to meet them. Reference-list words remain part of the existing complete-report word count.

Run `citations --prepare` to create bibliography.json and citation-keys.json from verified source metadata. Use those keys rather than constructing citation strings or guessing author-date disambiguation. The key builder preserves literal author names and supports DOI-less records. Run `validate --phase outline` before drafting.

### 5. Draft prescribed sections with Natural Writing

For each section, invoke [Natural Writing](../natural-writing/SKILL.md) in the current context. Pass the brief, document type, output language, academic style, section purpose, source/claim assignments, actual appraisal excerpts and locators, citation-key map, required terminology, word budget, neighboring context and unresolved restrictions. It owns loading the language guidance and returns prose to Research without a separate evaluation.

Write only to the assigned numbered section file while drafting. Preserve its required heading and use Pandoc citation keys at the supported claim, including checked locators and groups where appropriate. Use `[@MISSING]` for unresolved source support in a working draft; it blocks citation compilation and must be resolved or removed. Keep generated references out of hand-written prose. Findings, methods and locators must come from actual inspected evidence, not from a source title or assumed study design.

Return new evidence needs to Research. Retrieve and appraise additional sources under the same journal rules, update claims/outline, and regenerate keys with deliberate `--replace`. Draft the report summary provisionally; refresh it after the body is settled. Do not create placeholder research to fill a template.

### 6. Assemble and challenge the canonical draft

Run `assemble` to combine exactly the manifest's sections into draft.md. It rejects missing/duplicate/out-of-order sections, unfilled templates and unexpected top-level structure. After assembly, draft.md is the sole manuscript editing target. Section files remain drafting inputs. Reassembly requires explicit `--replace` and deliberately replaces later canonical edits.

Perform separate argument and citation reviews using the fixed argument-review.json and citation-review.json records. The argument review checks the answer, claim strength, counterevidence, cross-section consistency and outside check. The citation review checks source identity, claim support, quotations/numbers, locators and bibliography accuracy. Record findings with passage, severity, problem and actual correction, or record completed checks with concrete evidence. Never pre-mark them successful.

Apply at most two substantive repair passes. Resolve critical/major issues within scope or report the document as blocked/provisional with its remaining limitations. Do not simulate independent peer review or report model review as independent validation.

### 7. Polish without changing evidence

Invoke Natural Writing for the canonical draft with the settled outline, academic language guidance, review findings, terminology, citation map and protected numbers/qualifications. Improve coherence, paragraph development and transitions while preserving evidence and attribution. Refresh the summary and title against the finished body. Do not add unsupported results or strengthen novelty or causal claims during polishing.

Recheck every materially changed claim, number, quotation and citation. Complete both review records against the current draft SHA-256 and record the outside check's actual result. The validator rejects stale review hashes and unresolved blockers. Run `validate --phase review` before compilation.

### 8. Compile citations and export

Run `citations --replace` to compile report.md and cited-sources.json using Pandoc's cite processor and the selected local CSL style. It rejects unknown keys and emits a hash-linked citation receipt. The processor formats citations and only cited references; it does not establish claim support. Changes to draft or sources invalidate the receipt and require recompilation and any affected review.

For chat, use compiled report.md without another prose-generation pass. For requested files, read [export requirements](references/export.md) and run the export command. Markdown, standalone LaTeX and Word use Pandoc. PDF uses the fixed Markdown → DOCX → bundled LibreOffice route; obtain the bundled executable through the host's dependency lookup and pass it explicitly. Never silently choose an installed desktop LibreOffice or a different PDF backend.

Keep local assets available and preserve tables, equations, citations and references. Unsupported raw markup or missing assets must fail explicitly. Review rendered Word/PDF pages for all requested binary outputs, fix layout defects and re-export. Record visual-review evidence in exports.json without calling it a mechanical guarantee. Run `validate --phase final`. Deliver only requested outputs and material limits; keep all working records for repeatability.

### 9. Validate implementation

When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../spawn-evals/SKILL.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `evals/research/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

The private invocation record must use schema version 1, set skill to research, provide a unique non-empty invocation_id, include the original non-empty request, and map the saved report path under output_files.report. Its top-level structure is:

```json
{
  "schema_version": 1,
  "skill": "research",
  "invocation_id": "unique-id",
  "request": "the original user request",
  "constraints": {},
  "output_files": {"report": "/absolute/path/to/project/report.md"},
  "evidence": {"sources": []}
}
```

When invoked as a helper, return the report and its structured source inventory to the owning workflow without a separate check. Otherwise save the complete report as UTF-8 and create a private invocation record for Spawn Evals. Include the original request and these resolved constraints, each as `{"value": ..., "source": "request"|"skill_default"}`:

- `word_count_min` and `word_count_max`, using the selected depth's defaults unless the request supplies a bound. The checker counts whitespace-delimited words across the complete report, including citations and references. For deep depth, the default word maximum is `null` because the documented range says “or more.”
- `source_count_min` and `source_count_max`, using the selected depth's defaults unless the request supplies a bound. The checker counts `evidence.sources` entries; include one entry per substantive cited source.
- `journal_preset`, `journal_article_influence_min`, `journal_influence_percentile_min`, `journal_combination`, `journal_filter_disabled`, `journal_category`, and `journal_exceptions`. Use the documented inclusive preset thresholds by default: lenient `1.0` or `60`, default `2.5` or `80`, strict `5.0` or `90`. Use `or` by default. Record request overrides on the specific values they changed. If the request disables the filter, set the preset to `disabled`, both thresholds to `null`, and `journal_filter_disabled` to `true`. Use `null` for an unrestricted `journal_category` and an empty list for no exceptions. Exceptions are a list of exact `source_id` values and must be request-sourced.

Each `evidence.sources` record must include `source_id`, `publication_type`, and `title`. Use `publication_type: "journal_article"` or `"review"` for journal works; include `journal_title`, an `issns` list (empty when unavailable), and `article_url` for these items. Give other substantive source types an explicit non-empty publication type. Keep search and inspection notes available as evidence. Use only entries from cited-sources.json for this inventory. The citation consistency check compares these IDs with the current citation receipt, manuscript citation keys and compiled report hash. Neither citation bookkeeping nor journal and link checks judge findings, writing or research quality.

The literature-gate check validates the current discovered pool, rendered source list and bounded retry history through `evidence.project_dir`. It counts qualifying discoveries separately from cited report sources. The citation-expansion check reads brief.json, sources.json, retrieved-sources.json and qualified-expansion.json through the same directory; the original citation-candidates.json remains bound into the gate receipt. Preserve discovery annotations on cited records. Keep the frozen full initial pool and edge evidence even when some initial works are not cited; the cited-only inventory cannot establish overlap counts. Automatic overlap exceptions stay separate from request-sourced `journal_exceptions`.

Also include `requested_formats` as a resolved constraint with its provenance. Under `evidence`, include `project_dir` as the absolute project directory and `exports` as the entries from exports.json. Keep binary exports out of output_files, which accepts UTF-8 text only. The citation checker reads current draft.md, sources.json, bibliography.json, citation-receipt.json and report.md from that project. The requested-format checker compares the compiled report hash with conversion receipts and checks actual DOCX/PDF/LaTeX signatures and content structures. Missing dependencies or evidence remain unverified.

Run the prepared objective package through the Research wrapper:

```sh
python skills/research/scripts/complete.py --record /private/tmp/research-invocation.json
```

The configured package may check report length and source count against the resolved bounds, compare cited journal identities and scores with the selected preset, and test article-link reachability. A reachable link does not establish the identity or findings of the linked article. Use the wrapper's structured result as the evaluation record: distinguish a completed check, an unverified check, a top-level invocation error, and a missing package. A checker exception is not evidence that the package is missing. Network-blocked link checks should remain unverified; do not call links broken when the environment could not reach them. If no package exists, report NOT PASSED — UNVERIFIED and still deliver the completed report with that status; do not create a package during the invocation.

Do not evaluate nested Natural Writing output separately. Include the concise objective result with the report. Never describe the mechanical checks as proof that research findings are correct.

## Output

Return the compiled report in chat or the requested Markdown, LaTeX, PDF or Word files. Include the concise methods/limits note, actual citations and references, selected depth and journal rules, and standalone objective-check status with failed or unverified checks. As a helper, return the canonical report, cited-source inventory, project/receipt paths and remaining gaps to the owner. Keep internal working records out of the user-facing report unless requested. Do not expose private chain-of-thought or claim scientific correctness from script success.
