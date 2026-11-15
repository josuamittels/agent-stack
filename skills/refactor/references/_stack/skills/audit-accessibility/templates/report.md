# Accessibility audit: {{artifact name}}

<!-- Fill this template for the actual request. Keep the common core. Select,
combine, rename, extend, or remove optional medium modules below. Remove these
authoring notes and all placeholder rows from the delivered report. The common
score-table machine labels stay stable; surrounding prose can be translated. -->

## Assessment summary

{{State what works, principal barriers, access needs/tasks affected, and the most valuable next actions. State whether this is a static design review, selected-criteria assessment, or broader implemented-product review.}}

{{Show open critical/high barriers and important unverified scope prominently. This is a scoped audit; the descriptive scores do not establish conformance.}}

## Scope and assessment basis

| Item | Details |
| --- | --- |
| Artifact/version/date | {{Identify the actual reviewed version and audit date.}} |
| Purpose and intended audience | {{Task/message and known access needs.}} |
| Medium and delivery | {{UI, infographic, publication, media, mixed, other; delivery channel.}} |
| Target and sources | {{Standards, versions/levels, platform/format mapping, local guideline sections.}} |
| Inventory selection | {{Full baseline or justified selected criteria; distinguish required and advisory.}} |
| Evaluated scope/sample | {{Pages/regions/states/journeys/files/languages and sampling rationale.}} |
| Environments and methods | {{Actual tools, devices, OS/browser/AT versions, viewports, zoom/settings.}} |
| Exclusions and unavailable evidence | {{What was not inspected and which conclusions it prevents.}} |
| Assumptions | {{Consequential assumptions and their sources.}} |

## Results and descriptive scores

{{P fulfilled; F not fulfilled; U unknown; N not applicable. Required criteria only. Assessed fulfillment = 100 × P / (P + F). Assessment coverage = 100 × (P + F) / (P + F + U). Show denominators and advisory results separately. Zero denominator = not assessed.}}

| Metric | Value |
| --- | ---: |
| fulfilled | {{P}} |
| not_fulfilled | {{F}} |
| unknown | {{U}} |
| not_applicable | {{N}} |
| assessed_fulfillment_pct | {{number to one decimal or not assessed}} |
| assessment_coverage_pct | {{number to one decimal or not assessed}} |

{{Explain the scores together. State the unknown coverage and any confirmed blockers. These are scoped bookkeeping metrics, not percent compliance or a user-success score.}}

## Criterion assessment register

{{Use one row per selected criterion with the criterion source/level and exact condition available through the linked source or notes. Full web AA baseline retains all 55 A/AA rows. Group by principle/category, or place a long register in an appendix. Keep advisory practices separate. Every fulfilled and N/A row needs evidence/rationale too.}}

{{Where applicable, include hierarchy/structure and reading sequence, descriptive headings/labels/instructions, and consistent identification/navigation. Record exact wording or compared instances and the evidence needed for semantic or behavioral judgments. Keep language or brand preferences outside required scores unless the full applicable criterion is unmet.}}

| ID and source/level | Required/advisory | Outcome | Evidence and rationale | Finding or next check |
| --- | --- | --- | --- | --- |
| {{criterion ID, source link, level}} | {{basis}} | {{Fulfilled / Not fulfilled / Unknown / Not applicable}} | {{evidence IDs, conditions/exceptions, observed result}} | {{finding IDs or specific verification}} |

## Findings and actions

### {{Finding ID: concise barrier description}}

| Item | Detail |
| --- | --- |
| Severity | {{Critical / High / Medium / Low, with impact justification.}} |
| Location and evidence | {{Artifact, region/component/state and evidence IDs.}} |
| Requirement | {{Criterion IDs, source, actual condition/exception.}} |
| Observed barrier and impact | {{Observed facts, affected access/task, distinguished from hypotheses.}} |
| Action | {{Concrete change and shared cause/affected instances where known.}} |
| Verification | {{Reproduction, expected outcome, environment and complete-task retest.}} |

{{Repeat for distinct findings. Keep verification gaps and optional improvements distinct from confirmed barriers.}}

## Prioritized action list

| Order | Type | Related IDs | Concrete action | Dependency/owner role if useful | Completion/retest evidence |
| --- | --- | --- | --- | --- | --- |
| {{rank}} | {{Remediation / Verification / Advisory}} | {{finding/criterion IDs}} | {{change or next test}} | {{dependency or suggested role, not an invented assignment}} | {{observable outcome and method}} |

## Accessible decisions to preserve

{{Specific fulfilled criteria and successful access routes, with evidence. Identify what later changes should retain.}}

<!-- OPTIONAL MODULE: retain for visual content where detailed measurement helps. -->
## Visual and contrast measurements

| Element/region/state | Source foreground/background | Size/weight or role | Criterion/threshold/exception | Unrounded ratio and displayed result | Evidence/limits |
| --- | --- | --- | --- | --- | --- |
| {{element}} | {{values, compositing and source}} | {{actual metrics or unknown}} | {{applicable rule}} | {{calculated value and outcome, or unknown}} | {{evidence IDs and delivery conditions}} |

<!-- OPTIONAL MODULE: interface controls or behavior only. -->
## Interface operation and adaptation

{{Record tested journeys, keyboard/focus, semantics/AT, forms/errors, input alternatives, dynamic state, scaling/reflow/preferences and unsupported states as relevant. Link criterion/finding/evidence IDs. A static mockup may leave these unknown; do not invent a test run.}}

<!-- OPTIONAL MODULE: charts, maps, diagrams or infographics. -->
## Infographic and information access

{{Assess labels/legends, colour-independent encoding, meaningful graphical contrast, sequence/relationships, and the actual equivalent summary/data representation. State whether delivery context and alternatives were inspectable. Add interface testing only for actual interactive features.}}

<!-- OPTIONAL MODULE: documents, slides, emails, print and publication. -->
## Document and publication access

{{Assess relevant structure/tags, reading order, language, text, tables, images, links, enlargement, export/distribution or physical delivery conditions. State what requires the actual file, intended-size sample or accessible alternative.}}

<!-- OPTIONAL MODULE: audio, video, animation and timing. -->
## Media, motion and timing

{{Assess relevant captions/transcript/audio description, player operation, controls, timing, reduced motion and flashing. Record actual playback evidence and unavailable checks.}}

<!-- OPTIONAL MODULE: native, physical, mixed or unanticipated formats. -->
## {{Medium-specific access assessment}}

{{Name the format/platform, applicable criteria, methods, results and specialist evidence gaps. Add or combine sections as needed.}}

## Evidence and remaining limits

| Evidence ID | Artifact/location/state | Method and conditions | Observation or attachment |
| --- | --- | --- | --- |
| {{E-ID}} | {{locator}} | {{actual method/environment}} | {{observed result or evidence path}} |

{{List untested scope and concrete next checks. For a re-audit, explain baseline/scope changes and distinguish fixes from retested results. Link the accompanying audit.json register.}}
