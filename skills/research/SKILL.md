---
name: "research"
description: "Produce source-grounded, critically appraised academic research reports. Use for researching a topic, answering a research question, or synthesizing literature at a user-selected depth."
version: "0.1.0"
updated: "2026-10-25"
author:
  - "Josua Mittelstaedt"
references:
  - "PRISMA"
  - "Cochrane"
  - "Joanna Briggs Institute"
  - "ALLEA"
type: "skill"
status: "draft"
---

# Research

Produce an academically grounded report that answers a defined question, shows how the evidence was found and assessed, and makes the limits of the conclusions visible.

## Scope

Use for research reports, literature syntheses, evidence-based background briefs, and critical analyses of a topic. The output may draw on scholarly literature, primary materials, official data, and carefully selected grey literature, depending on the question.

Use [Research Literature](../../disciplines/research-literature/SKILL.md) to discover academic works in OpenAlex. This skill owns full-text retrieval where available, source appraisal, synthesis, and the report. Use [Think Deeper](../../disciplines/think-deeper/SKILL.md) to select the professional research methods, primary material, and an independent check for the specific question. A request to locate papers or return bibliographic records only belongs to Research Literature. A single-paper critique may use this skill when the user also needs it situated in relevant scholarship.

## Inputs

Use the topic or question, intended audience and use, requested deliverable or format, language, any supplied sources or constraints, and desired research depth. Ask only for a missing choice that would materially change what evidence can answer the question. Otherwise state a reasonable assumption and proceed.

Accept a depth of **light**, **default**, or **thorough**. If the user gives a word count, source range, deadline, field, date range, geography, population, or source preference, honor it and note any resulting coverage limit. Default to **default** depth when no depth is specified.

Read [English guidelines](../../guidelines/languages/english.md) for English reports, including its Academic section. For another requested language, read its matching language guideline. Use the field's established reporting guidance when the report type calls for it; consult a reporting checklist as a reporting aid, not proof that the underlying research was systematic or complete.

### Depth choices

Depth changes research effort and report scale. It does not change standards for source verification, fair representation, citation accuracy, or stating uncertainty.

| Depth | Search and inspection | Synthesis and report |
| --- | --- | --- |
| **Light** | Focused searches across the most relevant discovery routes; inspect the strongest accessible sources and the foundational material needed to answer the question. Aim for roughly 5–8 substantive sources when the field supports that scope. | Roughly 800–1,500 words: a concise answer, a few connected themes, key disagreements or limitations, and a short methods and references section. Suitable for orientation, not a claim of comprehensive coverage. |
| **Default** | Search multiple relevant routes or databases, screen for fit, inspect full text for sources carrying central claims, and check references or citations where useful. Aim for roughly 10–20 substantive sources when the field supports that scope. | Roughly 2,000–4,000 words: a developed report with a transparent method, thematic synthesis, source-quality discussion, competing explanations, and actionable conclusions only where supported. |
| **thorough** | Broaden and document the search across suitable databases and primary or grey-literature sources; use backward and forward citation searching; inspect full texts and compare relevant theories, designs, contexts, and counterevidence. Aim for roughly 20–40 substantive sources when the question and evidence base justify it. | Roughly 5,000–10,000 words or more: a substantial report with an explicit research protocol, evidence map or comparison tables where useful, deeper theoretical integration, stronger treatment of heterogeneity and uncertainty, and detailed limitations. |

The source and word ranges are planning guides, not quotas or evidence-quality thresholds. Follow a user-specified length when supplied. Stop when further searching yields diminishing relevant evidence or when the chosen scope has been reached. Say when the available literature is sparse, search access is limited, or a target range would add weakly relevant sources. Do not pad a bibliography or report to meet a number. If the user asks for a formal systematic, scoping, or other named review, use its field-appropriate conduct and reporting standards; a depth label alone does not make a report systematic.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../../disciplines/think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../../disciplines/ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Set the question and depth

Translate the topic into a bounded research question. Identify the phenomenon, population or material, context, time period, and relationship or claim at issue where they apply. Distinguish descriptive, explanatory, causal, comparative, interpretive, and predictive questions. Record the user's depth and any assumptions that affect what counts as relevant evidence.

If scope is too broad for the selected depth, choose a focused angle that preserves the user's intent and state it. Ask a concise question only when the answer would materially change the report and cannot be inferred.

### 2. Choose and document a method

Invoke [Think Deeper](../../disciplines/think-deeper/SKILL.md) with the question, depth, intended reader, and known limits. Use its method to identify the most direct evidence, suitable search and appraisal approaches, and a practical check that could challenge the synthesis. Apply the recommendations within this workflow; do not substitute a vague instruction to “be rigorous.”

Choose methods that fit the field and question. Use a framework such as PICO only when it fits the question; use an interpretive, historical, theoretical, or other appropriate structure when it does not. Select reporting or appraisal standards for the actual study and review types. Do not apply one checklist to every source. Record the search date, each source or database consulted, material query terms and filters, inclusion and exclusion logic, and any access or language limits. This is a research report unless a named review method is actually followed.

### 3. Search and screen evidence

Invoke [Research Literature](../../disciplines/research-literature/SKILL.md) for scholarly discovery. Pass the question, concepts and synonyms, inclusion or exclusion criteria, depth, date bounds if any, and any relevant author or publication constraints. Retain its search details, returned records, abstracts, and open-access links. Its records and abstracts support discovery; they do not establish that a full paper was read or appraised.

Add field-appropriate searches for primary sources, official statistics, standards, books, or grey literature when those materials can answer the question directly. Prefer original studies, records, and authoritative documentation for claims about what was observed or what a policy or system says. Use review articles to locate and contextualize primary work. Check publication type, version, venue, date, retraction or correction notices when relevant, and conflicts of interest where disclosed. Citation counts, journal rank, search ranking, and institutional reputation may help locate sources but do not establish quality.

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

Lead with a direct, appropriately qualified answer. Adapt section names to the deliverable, but include the functions needed for the reader to assess the work:

1. Title and date of the evidence search.
2. Executive summary or abstract, when useful for the requested length.
3. Research question and scope.
4. Search and selection method, including sources, date, and meaningful limits.
5. Thematic findings and critical comparison of evidence.
6. Interpretation, theoretical implications, or practical implications where warranted.
7. Limitations, remaining uncertainty, and conclusion.
8. References for cited works.

Cite claims close to the evidence supporting them. Verify that each citation points to the cited work and that bibliographic details, quotation text, page numbers, DOI, or URL are correct where used. Cite the version actually consulted. Never fabricate a citation, finding, quotation, page, statistic, or search step. Use quotation marks only for checked wording; otherwise paraphrase with a citation. Choose a consistent citation style suited to the field or user request; if no style is indicated for an interdisciplinary report, use APA 7 author-date.

Keep the report's claims proportional to evidence strength, relevance, directness, and consistency. Distinguish established findings, contested interpretations, plausible hypotheses, and recommendations. Avoid false balance: describe opposing positions according to the strength and relevance of their evidence. Do not overstate causation, novelty, consensus, generalizability, or practical impact.

### 7. Challenge and finalize

Apply the outside check selected through Think Deeper. Examples include verifying whether a known foundational source was retrieved, tracing a central claim to its primary evidence, checking an official statistic against its original release, or testing whether a conclusion remains sound under the strongest counterexample. State the check and observed result internally in the research notes or in the report when it affects confidence.

Check that the report answers the question, matches the selected depth, distinguishes searched from inspected material, cites every substantive evidence claim, represents contrary findings fairly, and records important uncertainty. If the check finds a material gap, correct the analysis within scope or report the limit. Do not present model self-review as independent validation.

### 8. Validate implementation

When invoked as a helper, return to the owning workflow without separate evaluation. Otherwise invoke [spawn-evals](../../disciplines/spawn-evals/SKILL.md). Pass the original requirements, necessary input context, completed output, observable evidence, and one evaluation ID bound to the request. Use live mode once for this completed result; keep domain-specific criteria in `evals/research/`. Do not evaluate callers or nested helpers, refresh suites, repair, or retry. Report good or not good and material gaps, then stop.

## Output

Return the requested report in the requested format or save it to the requested location. If neither is specified, deliver the report in the conversation. Include a concise methods note, in-text citations and a reference list, and the selected depth. For a material access or search limit, identify what was inaccessible and how it affects the conclusion. Do not expose internal chain-of-thought; present the research decisions, evidence, and reasoning needed to audit the report.

## Boundaries

Do not invent or alter research evidence, hide material counterevidence, or represent incomplete searching as comprehensive. Do not claim systematic-review status unless the conduct and documentation meet the relevant method. Do not imply that PRISMA or another reporting checklist alone establishes methodological quality. If the question calls for specialist interpretation beyond the accessible evidence or the source base cannot support a reliable answer, narrow the claim and state the limitation.
