# UX review lenses

Read when establishing user/task context, selecting report modules, and interpreting findings. These lenses organize the audit. Use the [Interaction guide](../../../guidelines/aesthetics/interaction.md) for behavioral rules and its delegated guidance for access and visual decisions. [Nielsen's usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) provide broad diagnostic principles, not a conformance standard or a replacement for user evidence.

## Resolve user context before judging fit

Record each important context claim as supplied, observed in source material, inferred, or unresolved. Name the source. Stakeholder descriptions establish intended users and goals; they do not establish observed behavior. Product context may make a task clear without resolving experience level or actual expectations.

Use these question areas only where the answer changes the audit:

| Unresolved context | What to establish | Why it changes a recommendation |
| --- | --- | --- |
| Who performs the job? | Actual user role, relevant expertise, distinction from buyer/admin/support, and materially different groups. | A domain term, default, or workflow useful to a practiced operator can obstruct first use. |
| What progress do they need? | Trigger, desired outcome, success condition, and current workaround. | Completing a feature flow may still fail to satisfy the real job. |
| What constrains the task? | Stakes, frequency, time pressure, interruptions, device/environment, language, access needs, privacy and resources where relevant. | Appropriate safeguards, density, input, continuity, and help depend on conditions. |
| What do they expect? | Familiar domain/platform patterns, existing tools, learned terminology and meaningful mental models. | A convention needs an identified reference. The reviewer's familiarity is not the user's expectation. |
| What evidence already exists? | Relevant research, task observations, support issues, analytics, known complaints and their scope. | Evidence may resolve a concern or reveal a different cause. Missing research remains a gap. |

Do not ask for demographics that do not affect the task. Do not fill missing facts with an invented persona. Ask about the real user and situation through the owning skill's question procedure. Follow [Government Digital Service's user-needs approach](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs) by framing needs around an outcome rather than a preferred feature.

## Common review principles

For each selected lens, connect the principle to the specific user, job, task, and evidence. Record supported design decisions as well as problems. Use additional domain guidance when it materially changes the result.

| Lens | Diagnostic questions | Applicable source or reading |
| --- | --- | --- |
| Need and job fit | Does the experience enable the required outcome, include the information/capability needed, and fit the real context? Does an essential service handoff fail outside the polished screen? | User evidence and brief first; Interaction section 1. Product-market fit cannot be established from a mockup. |
| Discoverability and learnability | Is the local goal understandable, the next action or information findable, its effect predictable, and progress recognizable? | Interaction sections 1–4 and 18; [cognitive walkthroughs](https://www.nngroup.com/articles/cognitive-walkthroughs/). |
| Language and conceptual model | Do names, categories, relationships, instructions, and labels match the user's understanding? Are distinctions meaningful before commitment? | Interaction sections 1–2; Nielsen's real-world match and recognition principles. |
| Orientation and information scent | Can the person identify location/state, find the relevant object, compare options, and return without losing context? | Interaction sections 7–8 and 10; Composition for hierarchy/grouping when needed. |
| Expectations and consistency | Do controls, labels, navigation, input and consequences follow relevant product/platform/domain conventions? Is a deviation justified by the task? | Interaction sections 2, 4, 7 and 15; actual platform/domain references. |
| Cognitive effort and repeat use | Does the task require avoidable recall, re-entry, irrelevant decisions, searching or context switches? Are expert routes available without hiding ordinary actions? | Interaction sections 8–10 and 15; Nielsen's recognition and efficiency principles. Click counts alone do not determine effort. |
| Feedback and truthful state | Is the system's actual state understandable during waiting, partial completion, errors and uncertainty? Can the person recognize a confirmed result? | Interaction sections 3 and 11–12. |
| Control and recovery | Can the person revise, back out, undo, resume and recover? Are protection and friction proportionate to consequences? | Interaction sections 9 and 13. |
| Informed choice and trust | Are costs, commitments, consent, privacy-relevant effects and cancellation clear at the point of decision? Are alternatives honestly presented? | Interaction section 14. This is a UX review, not a legal/privacy/security compliance audit. |
| Help and continuity | Is help available where needed without abandoning work? Do interruptions, access denial, handoffs and return visits preserve progress appropriately? | Interaction sections 7, 12–15. |
| Inclusive access | Can people with relevant access needs perceive, understand and operate the task? What remains unverified? | Required Audit Accessibility helper. Preserve its criterion findings and limits rather than duplicating its technical rubric. |

For interfaces, examine complete-task success and recovery as far as evidence allows. For information artifacts, success may mean finding, understanding, comparing or acting on the message. Do not add irrelevant interaction criteria to static material.

## Evidence and qualitative outcomes

Keep the design observation and the behavioral interpretation separate. A visible ambiguous action can support a reasoned concern; it does not demonstrate actual confusion. A reproducible implementation defect can establish what happened in that environment without proving prevalence among users.

Use these evidence labels with a source or locator:

- **Artifact observation:** directly inspected appearance, content, source, or reproduced behavior. State the method, state and environment.
- **User evidence:** supplied or actually obtained research/records. State whose behavior or report, method, population and relevant limits. A reported preference is not automatically observed task success.
- **Interpretation:** an explanation grounded in an observation and a named principle or convention. State which user/context assumption it depends on.
- **Hypothesis/open question:** plausible but unresolved need, belief or consequence. Name the research or additional evidence that could resolve it.

For a task, step or selected principle, use these qualitative outcomes:

| Outcome | Meaning |
| --- | --- |
| Supported | Inspected evidence supports the intended action/information route within the stated scope. This is not proof that intended users succeed. |
| Friction | An identifiable design condition introduces extra effort, ambiguity or recovery burden for the stated task. Explain the mechanism and evidence strength. |
| Blocked | Inspected evidence demonstrates that the scoped task cannot reach its required outcome through the evaluated route. If that is only predicted, label it a hypothesis instead. |
| Unknown | Missing context/evidence prevents a defensible outcome. Record what is missing and the next question/test. |
| Not applicable | The task/principle is outside the actual artifact or declared scope, with a reason. Missing evidence is not an exemption. |

These labels are judgments for a bounded review, not measurements or an additive score. Keep technical accessibility's own status labels in its subreport. Do not convert its percentage metrics into a UX rating.

## Impact and priority

| Severity | Anchor |
| --- | --- |
| Critical | Prevents an essential outcome without an effective alternative, or creates a serious harmful/irreversible consequence. |
| High | Substantially impedes an important task, invites a consequential error, or makes recovery impractical. |
| Medium | Adds material effort, ambiguity or interruption while a viable route remains. |
| Low | Localized inconvenience or refinement with limited task impact. |

Justify severity through the actual task and alternatives. Keep evidence strength separate from severity. A potentially critical hypothesis can need urgent testing without being reported as a confirmed blocker. Use known recurrence and affected scope where available; do not invent user counts or frequency. Explain different effects for different groups rather than averaging them away.

Prioritize demonstrated task blockage/harm and needed verification first, followed by shared causes and dependencies. Estimated implementation effort is provisional unless supported by project knowledge. A user-research action names the relevant audience/context, task, observation, and what evidence would support or challenge the proposed change. A cosmetic change without a task consequence belongs outside the main UX priorities.

## Modular depth

Keep a shared report core for user/jobs, scope/evidence, task walkthrough, principle outcomes, findings/actions, accessibility integration, preserved strengths, and open questions. Select optional modules for actual review decisions:

- Interface navigation, interaction, forms and state.
- First use/onboarding or expert/repeated work.
- Search, comparison, data and information comprehension.
- Documents, publications, infographics or instructions.
- Transactions, commitments, service handoffs or trust.
- Responsive/native/device context.
- Other domain or medium-specific needs, with named sources.

Combine modules when appropriate. Add a section for an unanticipated format rather than forcing it into a UI checklist. Limit category coverage when evidence is narrow and state the effect on the conclusions.
