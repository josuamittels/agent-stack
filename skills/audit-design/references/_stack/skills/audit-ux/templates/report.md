# UX audit: {{artifact or experience}}

<!-- Fill the shared core for this request. Keep only applicable optional modules,
combine or rename sections, and add medium/domain sections when useful. Remove
authoring notes and placeholder rows. This is a qualitative, task-centered audit,
not an invented usability percentage or a substitute for observed-user testing. -->

## Assessment summary

{{For whom and for which outcomes does the design work? Where does it obstruct the job? State the highest-impact changes, strengths and principal evidence limits. Mark a partial/provisional assessment clearly.}}

## Users, jobs and context

| User/context ID | Role and relevant needs/experience | Job or desired progress | Starting situation and constraints | What success means | Context source and unresolved facts |
| --- | --- | --- | --- | --- | --- |
| {{U-ID}} | {{Relevant facts only; distinguish end user from buyer/admin.}} | {{Outcome in the person's terms, not a feature name.}} | {{Trigger, environment, stakes, frequency where known.}} | {{Recognizable result.}} | {{Supplied / observed source / inferred / unresolved.}} |

{{Explain important expectations, existing workarounds, domain/platform conventions, group differences, and business/user goal conflicts. Include consequential questions and answers. Do not invent a persona to fill a gap.}}

## Review scope and evidence

| Item | Details |
| --- | --- |
| Artifact/version and review date | {{Actual reviewed material.}} |
| Medium, platform and delivery | {{Interface, prototype, document, infographic, mixed or other.}} |
| Evaluated units and journeys | {{Screens/pages/regions/states/roles/languages and sampling.}} |
| Methods and conditions | {{Actual inspection, walkthrough, interaction tests, supplied research and environments.}} |
| Principles and applicable modules | {{Chosen lenses with source/context.}} |
| Not inspected or unavailable | {{Scope/evidence gaps and resulting limits.}} |

| Evidence ID | Source/location/state | Method/conditions | Observation and scope limits |
| --- | --- | --- | --- |
| {{E-ID}} | {{Actual locator or source.}} | {{Method actually used; research provenance when applicable.}} | {{Artifact fact or user evidence, not an unmarked interpretation.}} |

## Tasks and outcome coverage

| Task ID | User/context | Trigger and starting information | Desired outcome and completion signal | Paths/conditions reviewed | Outcome and evidence |
| --- | --- | --- | --- | --- | --- |
| {{T-ID}} | {{U-ID}} | {{Starting state.}} | {{Required result and how it is recognized.}} | {{Main, recovery, interruption, other relevant paths.}} | {{Supported / Friction / Blocked / Unknown / Not applicable; evidence and limits.}} |

### {{Task ID: walkthrough or information-use sequence}}

| Step/region | What the person is trying to do or learn | Available cue/action and expected effect | Actual visible/reproduced response | UX interpretation and evidence strength | Finding or next check |
| --- | --- | --- | --- | --- | --- |
| {{step}} | {{Local goal linked to the larger job.}} | {{Notice, meaning and expected result.}} | {{Actual evidence or unknown.}} | {{Observation vs interpretation vs hypothesis.}} | {{IDs/action.}} |

{{Repeat for relevant tasks. For static content, follow comprehension/comparison/decision steps. Separate first-use learnability from repeat-use efficiency where both matter.}}

## Principle-based assessment

| Principle and source/convention | User/task relevance | Outcome | Supporting evidence and reasoning | Findings/unknowns |
| --- | --- | --- | --- | --- |
| {{Applicable lens.}} | {{U-ID/T-ID and why it matters.}} | {{Supported / Friction / Blocked / Unknown / Not applicable.}} | {{Evidence and interpretation.}} | {{IDs or verification.}} |

{{Include successful decisions and justify exclusions. Avoid mechanically adding every heuristic or treating an aesthetic preference as a usability defect.}}

## Accessibility sub-audit

| Item | Result |
| --- | --- |
| Helper invocation and artifacts | {{Actual invoked/applied Audit Accessibility workflow; link accessibility/report.md and accessibility/audit.json, or name the blocker.}} |
| Artifact/scope match | {{Reviewed version, medium, states and any coverage difference.}} |
| Leading barriers and task impacts | {{Preserve accessibility finding/criterion IDs and connect to UX task IDs.}} |
| Outcomes, metrics and limits | {{Summarize returned statuses/metrics in their own terms; do not convert into a UX score.}} |
| Required next actions | {{Repairs and verification, linked to the integrated list.}} |

{{Accessibility is a required component. If it could not finish, mark the UX report partial. Preserve unknowns and do not imply conformance.}}

## Detailed findings

### {{UX finding ID: concrete task problem}}

| Item | Detail |
| --- | --- |
| User, job, task and step | {{U-ID/T-ID and affected outcome.}} |
| Location and evidence | {{Artifact/state/region and E-IDs; cross-link accessibility IDs where relevant.}} |
| Principle or expectation | {{Named source/convention and its relevance.}} |
| Observed condition | {{What the material shows or actual execution demonstrated.}} |
| Consequence and evidence strength | {{Reasoned impact; supplied user evidence or hypothesis where appropriate.}} |
| Severity | {{Critical / High / Medium / Low, with task-based rationale.}} |
| Recommended action | {{Concrete change, preserved behavior, material tradeoff.}} |
| Verification | {{Reproduction/retest or neutral research task and what would support/challenge the claim.}} |

{{Repeat for distinct causes. Consolidate repeated symptoms while retaining affected locations. Keep uncertain behavioral concerns distinct from confirmed implementation defects.}}

## Integrated action plan

| Order | Type | UX/accessibility/task IDs | Action and intended user outcome | Dependencies/owner role if useful | Completion or validation evidence |
| --- | --- | --- | --- | --- | --- |
| {{rank}} | {{Repair / Design exploration / Verification / User research.}} | {{Linked IDs; avoid double-counting.}} | {{Concrete action.}} | {{Known dependency/suggested role.}} | {{Observable condition, method and relevant user/context.}} |

## What to preserve

{{Evidence-backed strengths, useful conventions, accessible behavior, successful task routes and intentional tradeoffs that recommendations should retain.}}

<!-- OPTIONAL MODULE: UI navigation, forms, controls and dynamic states. -->
## Interface behavior and continuity

{{Assess relevant orientation/navigation, input and commitment, state feedback, recovery, help, interruptions and return paths. Include unavailable states as unknown. Reference task/finding/evidence IDs rather than repeat all findings.}}

<!-- OPTIONAL MODULE: when learning or frequent/expert work changes the design. -->
## Learning and repeat use

{{Distinguish discoverability/onboarding, domain understanding, repeated effort, shortcuts/bulk work and habit. Explain how needs differ without assuming all users are novices or experts.}}

<!-- OPTIONAL MODULE: search, comparison, dashboards and information graphics. -->
## Finding and interpreting information

{{Assess information scent, labels/categories, comparison, definitions, mental model, context and decision support. For graphics, follow the reader's actual question and equivalent access. Do not substitute visual polish for comprehension or claim underlying data validity.}}

<!-- OPTIONAL MODULE: static documents, publications, slides or instructions. -->
## Reading, understanding and acting

{{Assess intended reading/decision task, necessary prior knowledge, sequence, clarity, navigation, actionable instructions and delivery context. Include only relevant medium concerns.}}

<!-- OPTIONAL MODULE: consequential decisions or multi-channel service journeys. -->
## Commitments, trust and service handoffs

{{Assess informed choice, costs/consequences, honest alternatives, cancellation/recovery, provider/offline handoffs and recognition of a confirmed result. Identify unavailable evidence.}}

<!-- OPTIONAL MODULE: actual device/platform context materially affects the job. -->
## Platform and environment fit

{{Assess relevant browser/native conventions, input conditions, mobility, interruptions, adaptation, languages and continuity. Cite the convention and actual context rather than impose a universal layout.}}

<!-- OPTIONAL MODULE: extend for another medium/domain. -->
## {{Specific domain or medium assessment}}

{{Name the relevant user question, principles, sources and evidence. Combine or add modules as needed.}}

## Open questions and validation plan

| Question or hypothesis | Affected decision/task | Evidence needed or question for the user | Suggested method/scenario | What result would change the recommendation |
| --- | --- | --- | --- | --- |
| {{Unknown.}} | {{T-ID/finding.}} | {{Specific missing context or behavior.}} | {{Neutral task/inspection; relevant participants if research is needed.}} | {{Falsifiable observation, with no invented target.}} |

{{State residual scope limits and any pending required handoff. For re-audits, record scope/version changes and distinguish proposed, implemented, reproduced and user-tested results.}}
