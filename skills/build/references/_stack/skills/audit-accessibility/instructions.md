---
name: "audit-accessibility"
description: "Audit a supplied interface, design, infographic, document, or media artifact against applicable accessibility standards. Fill a modular report.md with evidenced criterion outcomes, transparent scores, and prioritized remediation and verification actions."
version: "0.1.1"
created: "2026-11-12"
updated: "2026-11-12"
author:
  - "Josua Mittelstaedt"
references:
  - "World Wide Web Consortium"
  - "Humbleteam"
type: "skill"
status: "experimental"
---

# Audit accessibility

Assess an existing artifact against the accessibility requirements that apply to its medium and delivery context. Produce an evidence-linked report of what is fulfilled, not fulfilled, unknown, and not applicable, with reproducible scores and concrete next actions.

## Scope

Use for accessibility reviews of screenshots, design files, prototypes, working interfaces, infographics, documents, presentations, media, and related artifacts. Match the review to the supplied material and requested scope. A single static graphic can receive a useful review without becoming an interface audit.

### Boundaries

An audit request authorizes inspection and reporting. Implementation, publication, external communications, and consequential live transactions require their own authorization. Use safe test states for forms and account flows. Record inaccessible states instead of activating consequential actions to obtain evidence.

Distinguish a scoped assessment from whole-product conformance, legal advice, certification, and user research. A scanner score, passing contrast pair, static mockup, or selected sample cannot establish complete accessibility. Report real failures and unknowns even when a score is high.

## Inputs

Require an identifiable artifact and access sufficient to inspect at least part of it. Use supplied purpose, audience needs, medium, delivery channel, platform, version, supported environments, journeys, standard/version/level, constraints, and output location. Infer ordinary context with a stated assumption. Ask only about consequential gaps the material cannot settle.

Read the [aesthetics framework](../../guidelines/aesthetics/reference.md), [Accessibility guide](../../guidelines/aesthetics/accessibility.md), and [assessment rubric](references/rubric.md) before assessing. Accessibility owns requirements and evidence standards. Read its target, relevant medium/domain sections, evaluation/remediation sections, and criterion coverage index as applicable. Follow decision-specific dependencies rather than loading every aesthetics guide.

### Default Procedures

When task input is needed from the user, route the question through [ask-user-question](../ask-user-question/instructions.md) for preparation, delivery, and interpretation. First invoke [think-harder](../think-harder/instructions.md) when ambiguity, missing information, or competing interpretations may be resolved from context, relevant guidance, evidence, or a reasonable default. Skip Think Harder for direct permission or approval gates, explicitly requested interviews, and facts or preferences only the user can supply. Ask only about consequential unresolved items. Continue independent work and preserve approval requirements.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Establish scope and the criterion inventory

Identify the artifact/version, purpose, pages or regions, states, delivery conditions, support combinations, and exclusions. Select medium profiles using the rubric. An interactive chart can need both UI and infographic modules. Keep the common report core and only relevant optional modules. Add a medium-specific section when needed.

Set the target before assigning results. Default web reviews to WCAG 2.2 AA plus separately identified stronger product conventions from Accessibility. Retain all 55 A/AA criteria in its coverage index for this baseline, including untestable criteria. For an explicitly focused review or non-web artifact, select a justified inventory from applicable standards and platform/format guidance. Label it a selected-criteria assessment. Consult relevant platform guidance and WCAG2ICT interpretation for non-web software/documents. For physical output, record actual size, environment, and accessible alternatives. Digital contrast alone does not establish print legibility.

Record selected IDs, sources/versions/levels, test conditions, declared scope, and required or advisory basis before evaluation. Explain selection and exclusions. Do not silently drop failing or unknown criteria later. Add access needs beyond WCAG as advisory unless a specified source makes them requirements. Verify normative wording, exceptions, and changing specifications when they affect a decision. Investigate legal applicability only when requested or necessary to settle the target, using current primary sources.

### 2. Inspect and preserve evidence

Open actual rendered evidence with available image/document/design/browser tools. Inspect it alongside source or annotations where useful. Give evidence stable IDs with artifact location, region/state, method, environment/settings, and observed result. Reject blank, wrong-state, loading, or unreadable captures as support for a judgment. Disclose sampling and retain case-level results.

Choose complementary methods the artifact supports: visual inspection, colour measurement, source/semantic inspection, automated rules, keyboard/pointer tests, zoom/reflow and spacing overrides, platform preferences, assistive technology, and complete-task checks. Record what ran and what was unavailable. An accessibility tree is not screen-reader testing. Claim disabled-user research only when it occurred.

A screenshot supports its visible state. It cannot establish hidden content, focus behavior, accessible names, keyboard operation, responsive adaptation, or alternatives elsewhere. Source inspection does not prove delivered rendering or AT behavior. Missing evidence is unknown, not an automatic failure or exemption. Unknown delivery context for an infographic can leave its text equivalent unverified while still permitting review of visible labels and colour dependence.

### 3. Assess the selected criteria

Apply the status and severity rubrics in [rubric.md](references/rubric.md). Keep observations, criterion interpretations, and user-impact hypotheses distinguishable. Evaluate the complete condition and its exceptions. Product preferences and advisory improvements do not become normative failures.

Include the access implications of unclear hierarchy, inconsistent identification/navigation, and ambiguous or misleading headings, labels and instructions when applicable. Use the owning guide to select the actual requirements for structure/relationships, meaningful sequence, descriptive text, consistent behavior and instructions; inspect semantics and operation when the decision depends on them. Visual emphasis alone does not establish semantic hierarchy. Tie a failure to the criterion's complete condition, and keep broader language or brand-tone concerns advisory unless an applicable requirement is demonstrably unmet.

Retain case-level evidence and assign one aggregate outcome per criterion over its declared scope. A confirmed failing case means not fulfilled even if other cases pass. Without a failure, incomplete required evidence means unknown. Fulfilled requires adequate evidence across scoped cases. Not applicable needs a supported scope reason, not absence from a crop. Do not count each passing instance as a separate criterion or average away a failure.

For reliable opaque foreground/background pairs, invoke [Check Colour Contrast](../check-colour-contrast/instructions.md) with the actual values and formats. Use [Colour's compositing/calculation guidance](../../guidelines/aesthetics/colour.md#calculate-srgb-contrast-correctly) for transparency, conversion, and variable backgrounds. Record element/state, source values, text size/weight or graphic role, applicable criterion/threshold, full-precision ratio, and result. Compare before rounding. Treat screenshot sampling and unknown scale as limited evidence. Do not infer exact CSS target sizes or font metrics from image pixels. Colour-vision simulation is supplementary evidence, not a criterion test.

### 4. Turn barriers and gaps into actions

Give each finding an ID, location/state, criterion IDs, observed evidence, affected access/task, severity, concrete remediation, and reproducible retest. Group repeated instances under a shared cause where justified while retaining their locations. Preserve verified accessible behavior.

Give unknowns verification actions with the input/environment/test needed. Separate these from confirmed repairs and optional improvements. Suggest owner roles when useful, without inventing assignments, deadlines, or effort certainty. Prioritize blocked essential tasks, serious barriers, shared causes, and dependencies. Do not lower impact merely because fewer people are affected.

### 5. Fill the modular report

Read and copy [templates/report.md](templates/report.md) for every invocation. Use a fresh audit directory at the requested destination, otherwise a writable project output location under `audits/accessibility/<artifact-slug>/<unique-run>/`. Preserve earlier reports. If persistent storage is unavailable, return the filled Markdown and state the saving limitation.

Fill common sections, instantiate applicable modules, and remove unused modules, authoring notes, and placeholder rows. Adapt titles, narrative, tables, and depth to the artifact. Use [Write](../write/instructions.md) for the output language. Keep machine fields and criterion IDs stable across translations.

Save `audit.json` beside `report.md` using the rubric's data contract. It is the reproducible assessment register. Calculate the raw counts and two descriptive scores exactly as specified. Show denominators, critical/high barriers, and unknown scope beside the scores. Keep advisory outcomes separate. A zero denominator is not a perfect result. Never call the metrics percent compliance or use them to declare conformance.

Use this register for criterion rows, findings, actions, and scores. Confirm every selected criterion is accounted for, failures lead to remediation, and unknowns lead to verification. For re-audits, retain comparable IDs and document scope changes. Distinguish fixed, retested, and verified in the delivered version.

### 6. Validate implementation

When invoked as a helper, return to the owning workflow without separate evaluation. For a skill with meaningful, deterministic, task-specific checks, invoke [Spawn Evals](../spawn-evals/instructions.md) once with a structured invocation record containing the original request, resolved constraints and their source, complete UTF-8 outputs, and machine-readable evidence. Its objective package in `src/evals/audit-accessibility/` defines only those checks. Report PASS, FAIL, or NOT PASSED — UNVERIFIED with the failing or unavailable verification steps. Do not use model judges, sub-agents, qualitative assessments, weighted scores, or synthetic scenarios. If no package exists for an objectively checkable skill, report NOT PASSED — UNVERIFIED; do not create one during an ordinary skill invocation. If no meaningful objective check is possible for this skill, omit this entire validation section and all Spawn Evals references from the skill.

Supply `output_files.main` for the full report and `output_files.audit` for `audit.json`. Include `evidence.selected_criterion_ids`, settled in step 1, and `constraints.baseline` with value `wcag-2.2-aa` or `selected-criteria` and provenance. Use Spawn Evals' runner contract. Checks cover criterion accounting, score arithmetic/report agreement, and failure/action traceability. Its result describes report mechanics, not the artifact's accessibility.

## Output

Return the filled `report.md` and matching `audit.json` with a short summary of fulfilled requirements, leading barriers, next actions, and evidence gaps. Include the target/scope, criterion outcomes with evidence, transparent scores, relevant medium modules, prioritized remediation/verification actions, and strengths to preserve.

As a helper, return these artifacts and open questions to the owning workflow without separate evaluation. Do not modify the reviewed artifact as part of reporting.
