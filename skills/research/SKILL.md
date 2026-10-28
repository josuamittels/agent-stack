---
name: "research"
description: "Produce source-grounded, critically appraised academic research reports at a user-selected depth with lenient, default, or strict journal selection. Use for researching a question or synthesizing literature."
version: "0.7.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "PRISMA"
  - "Cochrane"
  - "Joanna Briggs Institute"
  - "ALLEA"
type: "skill"
status: "experimental"
---

# Research

Produce an academically grounded report that answers a defined question, shows how the evidence was found and assessed, and makes the limits of the conclusions visible.

## Evaluation contract

Evaluate a completed real use only. There are no synthetic scenarios or qualitative assessments. For standalone reports, run the objective checks described in step 8 after producing the report. Evaluation does not attempt to verify whether a report's substantive findings are true. When invoked as a helper, return the report and structured source inventory to the owning workflow; the owner retains evaluation and delivery. Explicit user instructions to skip evaluation take precedence and must be reflected in the delivered status.

## Scope

Use for research reports, literature syntheses, evidence-based background briefs, and critical analyses of a topic. The output may draw on scholarly literature, primary materials, official data, and carefully selected grey literature, depending on the question.

Use [Research Literature](../research-literature/SKILL.md) to discover academic works in OpenAlex. This skill owns full-text retrieval where available, source appraisal, synthesis, and the report. Use [Think Deeper](../think-deeper/SKILL.md) to select the professional research methods, primary material, and an independent check for the specific question. A request to locate papers or return bibliographic records only belongs to Research Literature. A single-paper critique may use this skill when the user also needs it situated in relevant scholarship.

### Boundaries

Do not invent or alter research evidence, hide material counterevidence, or represent incomplete searching as comprehensive. Do not claim systematic-review status unless the conduct and documentation meet the relevant method. Do not imply that PRISMA or another reporting checklist alone establishes methodological quality. If the question calls for specialist interpretation beyond the accessible evidence or the source base cannot support a reliable answer, narrow the claim and state the limitation.

## Inputs

Use the topic or question, intended audience and use, requested deliverable or format, language, any supplied sources or constraints, and desired research depth. Ask only for a missing choice that would materially change what evidence can answer the question. Otherwise state a reasonable assumption and proceed.

Accept a depth of **light**, **default**, or **thorough**. If the user gives a word count, source range, deadline, field, date range, geography, population, or source preference, honor it and note any resulting coverage limit. Default to **default** depth when no depth is specified.

Accept **lenient**, **default**, or **strict** journal selection independently of depth. Journal selection defaults to **default**. Tell the user they can request **lenient** for broader venue coverage or **strict** for a narrower selection, then proceed with the default unless they specify otherwise. Use [Research Literature's journal-selection rules](../research-literature/SKILL.md#journal-selection) as the authoritative cutoffs and override policy. Honor requests for more lenient or stricter journal selection, explicit numeric thresholds, or disabling the filter. Keep the selection throughout follow-up searches and citation chasing, and identify any explicitly requested exceptions.

The journal filter governs journal articles and reviews. Continue to use suitable primary records, official sources, books, and grey literature according to the question and stated inclusion criteria. Label their discovery separately. Journal eligibility does not establish individual study quality or replace the appraisal below.

Invoke [Natural Writing](../natural-writing/SKILL.md) as a writing helper with an academic writing focus. Pass the report language, audience, field, citation style, format, and depth; it owns language guidance and returns here without a separate evaluation. Use the field's established reporting guidance when the report type calls for it; consult a reporting checklist as a reporting aid, not proof that the underlying research was systematic or complete.

### Depth choices

Depth changes research effort and report scale. It does not change standards for source verification, fair representation, citation accuracy, or stating uncertainty.

| Depth | Search and inspection | Synthesis and report |
| --- | --- | --- |
| **Light** | Focused searches across the most relevant discovery routes; inspect the strongest accessible sources and the foundational material needed to answer the question. Aim for roughly 5–8 substantive sources when the field supports that scope. | Roughly 800–1,500 words: a concise answer, a few connected themes, key disagreements or limitations, and a short methods and references section. Suitable for orientation, not a claim of comprehensive coverage. |
| **Default** | Search multiple relevant routes or databases, screen for fit, inspect full text for sources carrying central claims, and check references or citations where useful. Aim for roughly 10–20 substantive sources when the field supports that scope. | Roughly 2,000–4,000 words: a developed report with a transparent method, thematic synthesis, source-quality discussion, competing explanations, and actionable conclusions only where supported. |
| **thorough** | Broaden and document the search across suitable databases and primary or grey-literature sources; use backward and forward citation searching; inspect full texts and compare relevant theories, designs, contexts, and counterevidence. Aim for roughly 20–40 substantive sources when the question and evidence base justify it. | Roughly 5,000–10,000 words or more: a substantial report with an explicit research protocol, evidence map or comparison tables where useful, deeper theoretical integration, stronger treatment of heterogeneity and uncertainty, and detailed limitations. |

The source and word ranges are default evaluation bounds when a user has not supplied a different numeric limit. A request-specific bound takes precedence. Do not add weak sources or pad prose to meet a bound; when the evidence or access cannot support it, report that limit and expect the corresponding objective check to fail or remain unverified. If the user asks for a formal systematic, scoping, or other named review, use its field-appropriate conduct and reporting standards; a depth label alone does not make a report systematic.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Set the question and depth

Translate the topic into a bounded research question. Identify the phenomenon, population or material, context, time period, and relationship or claim at issue where they apply. Distinguish descriptive, explanatory, causal, comparative, interpretive, and predictive questions. Record research depth and journal selection separately, including numeric overrides, exceptions, and any assumptions that affect what counts as relevant evidence.

If scope is too broad for the selected depth, choose a focused angle that preserves the user's intent and state it. Ask a concise question only when the answer would materially change the report and cannot be inferred.

### 2. Choose and document a method

Invoke [Think Deeper](../think-deeper/SKILL.md) with the question, depth, intended reader, and known limits. Use its method to identify the most direct evidence, suitable search and appraisal approaches, and a practical check that could challenge the synthesis. Apply the recommendations within this workflow; do not substitute a vague instruction to “be rigorous.”

Choose methods that fit the field and question. Use a framework such as PICO only when it fits the question; use an interpretive, historical, theoretical, or other appropriate structure when it does not. Select reporting or appraisal standards for the actual study and review types. Do not apply one checklist to every source. Record the search date, each source or database consulted, material query terms and filters, inclusion and exclusion logic, and any access or language limits. This is a research report unless a named review method is actually followed.

### 3. Search and screen evidence

Invoke [Research Literature](../research-literature/SKILL.md) for scholarly discovery. Pass the question, concepts and synonyms, inclusion or exclusion criteria, depth, journal selection and any overrides or exceptions, date bounds if any, and relevant author or publication constraints. Retain its journal-eligibility and exclusion evidence, search details, returned records, abstracts, and open-access links. Apply the same journal criteria to other routes that discover journal articles. Its records and abstracts support discovery; they do not establish that a full paper was read or appraised.

Add field-appropriate searches for primary sources, official statistics, standards, books, or grey literature when those materials can answer the question directly. Prefer original studies, records, and authoritative documentation for claims about what was observed or what a policy or system says. Use review articles to locate and contextualize primary work. Check publication type, version, venue, date, retraction or correction notices when relevant, and conflicts of interest where disclosed. Citation counts, journal rank, search ranking, and institutional reputation may help locate sources but do not establish quality. If Research Literature cannot reach OpenAlex through its API or website, continue useful discovery through other available sources when that preserves the question and inclusion rules. Record the actual providers and queries, identify this as a non-OpenAlex fallback, and report that OpenAlex discovery was incomplete.

Screen results against the question and stated criteria. De-duplicate records. Distinguish discovered, screened, full-text inspected, and included sources; do not imply that all search results were read. Record important exclusions and reasons at a level proportionate to depth. If a central source is inaccessible, use a clearly identified abstract or secondary account only as a limited proxy, seek an accessible version where practical, and state what could not be verified.

### 4. Read and appraise the evidence

Read the full text of sources that carry central claims when accessible. Verify each key interpretation against the source itself. Extract the question, context, design or argument, data or materials, analysis, findings, limitations, and relevant funding or conflicts. Separate the authors' claims from the evidence and from your interpretation.

Assess sources against criteria appropriate to their role:

- For empirical studies, examine design fit, sampling or selection, measures, confounding, missing data, analysis, robustness, and whether the conclusion exceeds the results.
- For qualitative or interpretive work, examine context, material or participant selection, analytic process, positionality where relevant, and the connection between evidence and interpretation.
- For theory, assess definitions, assumptions, internal logic, explanatory reach, and engagement with serious alternatives.
- For historical, legal, policy, or technical primary sources, assess provenance, version, authorship, scope, and context; distinguish the source's text from its practical effect or later interpretation.
- For reviews and syntheses, inspect their search and inclusion methods, appraisal approach, synthesis, and date of coverage. A reporting checklist can reveal omissions but cannot validate conduct by itself.

Use a validated, design-specific appraisal tool when one applies and the report depth warrants it. Explain important judgments and uncertainty; do not convert a checklist score, journal label, or single composite rating into a substitute for reasoning. Do not infer a study's quality from abstract-only evidence.

### 5. Build a synthesis before drafting

Organize the evidence by themes, mechanisms, theories, methods, populations, time periods, or disagreements that answer the question. For each central claim, map the supporting and contrary evidence and note the source types and limitations. Compare findings rather than producing an author-by-author inventory.

Explain convergence and disagreement only where the sources support it. Check whether differences arise from methods, definitions, populations, context, timing, or genuine unresolved conflict. Identify the strongest counterevidence and plausible alternative explanations. Connect theories to findings without presenting theoretical coherence as empirical confirmation. State evidence gaps as gaps in the searched and inspected material, not as universal absence claims.

Use tables for evidence comparisons or claim-to-source traceability when they make the reasoning easier to inspect. Conduct quantitative synthesis only when the underlying data are sufficiently comparable and the method is suitable; otherwise synthesize narratively and explain why pooling was not justified.

### 6. Write the report

Apply Natural Writing with an academic writing focus while composing the report. Preserve verified findings, uncertainty, quotations, and attribution through prose revisions.

Lead with a direct, appropriately qualified answer. Adapt section names to the deliverable, but include the functions needed for the reader to assess the work:

1. Title and date of the evidence search.
2. Executive summary or abstract, when useful for the requested length.
3. Research question and scope.
4. Search and selection method, including sources, date, journal preset or override with its numeric rule, important exclusions, coverage limits, and any exceptions.
5. Thematic findings and critical comparison of evidence.
6. Interpretation, theoretical implications, or practical implications where warranted.
7. Limitations, remaining uncertainty, and conclusion.
8. References for cited works.

Cite claims close to the evidence supporting them. Verify that each citation points to the cited work and that bibliographic details, quotation text, page numbers, DOI, or URL are correct where used. Cite the version actually consulted. Never fabricate a citation, finding, quotation, page, statistic, or search step. Use quotation marks only for checked wording; otherwise paraphrase with a citation. Choose a consistent citation style suited to the field or user request; if no style is indicated for an interdisciplinary report, use APA 7 author-date.

Keep the report's claims proportional to evidence strength, relevance, directness, and consistency. Distinguish established findings, contested interpretations, plausible hypotheses, and recommendations. Avoid false balance: describe opposing positions according to the strength and relevance of their evidence. Do not overstate causation, novelty, consensus, generalizability, or practical impact.

### 7. Challenge and finalize

Apply the outside check selected through Think Deeper. Examples include verifying whether a known foundational source was retrieved, tracing a central claim to its primary evidence, checking an official statistic against its original release, or testing whether a conclusion remains sound under the strongest counterexample. State the check and observed result internally in the research notes or in the report when it affects confidence.

Check that the report answers the question, matches the selected depth, distinguishes searched from inspected material, cites every substantive evidence claim, represents contrary findings fairly, and records important uncertainty. If the check finds a material gap, correct the analysis within scope or report the limit. Do not present model self-review as independent validation.

### 8. Run objective checks

The private invocation record must use schema version 1, set skill to research, provide a unique non-empty invocation_id, include the original non-empty request, and map the saved report path under output_files.report. Its top-level structure is:

```json
{
  "schema_version": 1,
  "skill": "research",
  "invocation_id": "unique-id",
  "request": "the original user request",
  "constraints": {},
  "output_files": {"report": "/absolute/path/to/report.txt"},
  "evidence": {"sources": []}
}
```

When invoked as a helper, return the report and its structured source inventory to the owning workflow without a separate check. Otherwise save the complete report as UTF-8 and create a private invocation record for Spawn Evals. Include the original request and these resolved constraints, each as `{"value": ..., "source": "request"|"skill_default"}`:

- `word_count_min` and `word_count_max`, using the selected depth's defaults unless the request supplies a bound. The checker counts whitespace-delimited words across the complete report, including citations and references. For thorough depth, the default word maximum is `null` because the documented range says “or more.”
- `source_count_min` and `source_count_max`, using the selected depth's defaults unless the request supplies a bound. The checker counts `evidence.sources` entries; include one entry per substantive cited source.
- `journal_preset`, `journal_article_influence_min`, `journal_influence_percentile_min`, `journal_combination`, `journal_filter_disabled`, `journal_category`, and `journal_exceptions`. Use the documented inclusive preset thresholds by default: lenient `1.0` or `60`, default `2.5` or `80`, strict `5.0` or `90`. Use `or` by default. Record request overrides on the specific values they changed. If the request disables the filter, set the preset to `disabled`, both thresholds to `null`, and `journal_filter_disabled` to `true`. Use `null` for an unrestricted `journal_category` and an empty list for no exceptions. Exceptions are a list of exact `source_id` values and must be request-sourced.

Each `evidence.sources` record must include `source_id`, `publication_type`, and `title`. Use `publication_type: "journal_article"` or `"review"` for journal works; include `journal_title`, an `issns` list (empty when unavailable), and `article_url` for these items. Give other substantive source types an explicit non-empty publication type. Keep search and inspection notes available as evidence. The source-count check counts this inventory and does not prove that every entry appears in the report. The journal and link checks do not judge findings, writing, or research quality.

Run the prepared objective package through the Research wrapper:

```sh
python skills/research/scripts/complete.py --record /private/tmp/research-invocation.json
```

The configured package may check report length and source count against the resolved bounds, compare cited journal identities and scores with the selected preset, and test article-link reachability. A reachable link does not establish the identity or findings of the linked article. Use the wrapper's structured result as the evaluation record: distinguish a completed check, an unverified check, a top-level invocation error, and a missing package. A checker exception is not evidence that the package is missing. Network-blocked link checks should remain unverified; do not call links broken when the environment could not reach them. If no package exists, report NOT PASSED — UNVERIFIED and still deliver the completed report with that status; do not create a package during the invocation.

Do not evaluate nested Natural Writing output separately. Include the concise objective result with the report. Never describe the mechanical checks as proof that research findings are correct.

## Output

Return the requested report in the requested format or save it to the requested location. If neither is specified, deliver the report in the conversation. Include a concise methods note, in-text citations and a reference list, the selected depth and journal selection, and the objective evaluation result with failed or unverified checks. For a material access or search limit, identify what was inaccessible and how it affects the conclusion. Do not expose internal chain-of-thought; present the research decisions, evidence, and reasoning needed to audit the report.
