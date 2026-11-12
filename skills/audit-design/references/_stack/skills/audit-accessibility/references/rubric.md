# Assessment rubric

Read before selecting criteria and filling the report. This file defines assessment mechanics, medium selection, and the machine-readable register. The [Accessibility guide](../../../guidelines/aesthetics/accessibility.md) owns domain requirements. Apply its full conditions, definitions, exceptions, and current source references.

## Criterion outcomes

| Display status | Machine value | Decision rule | Required support |
| --- | --- | --- | --- |
| Fulfilled | `fulfilled` | All necessary conditions pass across the declared evaluated cases. | Test method, observed result, and evidence IDs. A design annotation establishes intent only. |
| Not fulfilled | `not_fulfilled` | At least one evaluated case demonstrably fails the criterion. | Reproducible failing case, evidence IDs, and a remediation finding. Passing instances do not cancel it. |
| Unknown | `unknown` | No confirmed failure, but applicability or outcome cannot be settled with available evidence. Includes mixed passing and untested cases. | What is known, what remains untested, and the verification action needed. |
| Not applicable | `not_applicable` | The criterion's triggering condition is demonstrably absent from the declared scope, or its stated exception applies throughout that scope. | Scope evidence and the exact reason/exception. “Not shown” is insufficient. |

Use one aggregate row per unique criterion ID, with case-level results in the evidence notes or module. Distinct obligations from different sources can have distinct IDs. Do not duplicate the same requirement across modules to increase its score. Advisory observations remain separate from required results.

For an audit whose baseline is `wcag-2.2-aa`, retain all 55 criteria from Accessibility's section 26 as required rows with IDs `WCAG22:1.1.1`, and so on. Do not include obsolete 4.1.1. Unknowns and justified exclusions remain in the register. Additional contractual requirements can extend this set. For `selected-criteria`, declare the inventory and selection reasons explicitly and make no full-standard claim. Adding/removing criteria later needs a documented scope correction, not a silent denominator change.

## Scores and denominators

Score only rows with `basis: required`. Let P be fulfilled, F not fulfilled, U unknown, and N not applicable. Report all four counts. Advisory outcomes do not enter the denominators.

- **Assessed fulfillment** is `100 × P / (P + F)`. It describes tested criterion outcomes. If `P + F = 0`, report `not assessed` and store JSON `null`.
- **Assessment coverage** is `100 × (P + F) / (P + F + U)`. It describes how much of the potentially applicable inventory has a confirmed outcome. If its denominator is zero, report `not assessed` and store JSON `null`.

Round displayed percentages to one decimal place. Retain the underlying counts. Unknowns are excluded from fulfillment but remain in the coverage denominator, so the two metrics must always appear together. Neither is an accessibility percentage, a measure of disabled-user task success, or WCAG conformance. All applicable requirements and conformance conditions still matter individually. Show open critical/high barriers prominently even at 100% assessed fulfillment. A failed criterion is not fulfilled regardless of severity or effort.

Keep these six machine-readable summary labels and numeric values in the report's score table. Other text can be translated or reorganized. Use `not assessed` for a null percentage. Percent cells contain a plain number without `%` because the label supplies the unit.

| Metric | Value type |
| --- | --- |
| `fulfilled` | Integer P |
| `not_fulfilled` | Integer F |
| `unknown` | Integer U |
| `not_applicable` | Integer N |
| `assessed_fulfillment_pct` | One-decimal number or `not assessed` |
| `assessment_coverage_pct` | One-decimal number or `not assessed` |

Do not add a weighted composite, traffic-light overall rating, or letter grade by default. A user-requested additional rubric needs explicit definitions and a separate denominator. Preserve these common metrics so untested scope remains visible. Compare runs only when their inventory, scope, and methods are comparable.

## Barrier severity and action priority

Severity describes demonstrated impact, independently of the criterion's level or status. Assign it to findings, not to passes or unknowns.

| Severity | Anchor | Action order |
| --- | --- | --- |
| Critical | Blocks an essential task or essential information with no effective equivalent route, or presents an immediate serious access hazard. | Address first. Identify an interim accessible route where possible and retest the complete task. |
| High | Materially prevents or severely impedes an important task or information for an affected access need. | Prioritize next, including shared causes that spread across the artifact. |
| Medium | Creates substantial extra effort, confusion, or loss of access to secondary information while an effective route remains. | Repair after critical/high barriers, respecting dependencies. |
| Low | Limited localized access degradation or an advisory robustness improvement. | Refine after higher-impact issues. It remains a failure if it violates a requirement. |

Explain the affected task, available alternatives, recurrence, and scope for each severity. Do not infer affected population counts. A suspected critical issue with insufficient evidence remains unknown with an urgent verification action, rather than a confirmed failure.

## Medium modules and concrete checks

These are selection prompts, not an exhaustive replacement for the chosen standard. Instantiate multiple modules for mixed artifacts. Distinguish the visual artifact from its delivery mechanism.

| Module | Select when | Review questions and evidence |
| --- | --- | --- |
| Shared visual/content | Visible text, graphics, instructions, or meaning-bearing colours exist. | Actual text/graphic contrast and non-colour cues, readable content and relationships, instructions not reliant solely on sensory characteristics, and access to the intended message. Use Accessibility sections 6 and 15 plus the relevant type/colour/composition dependencies. |
| Interface | Controls, navigation, input, dynamic state, authentication, or transactions exist. | Keyboard access/no traps, visible and unobscured focus, names/roles/states, meaningful order, labels/errors, status announcements, predictable context, input alternatives, target size, complete tasks, zoom/reflow, preferences. Require live/source/AT evidence appropriate to each claim. Use sections 7–16, 20–23 and the full baseline index for a web AA audit. |
| Infographic/data | Charts, maps, diagrams, dashboards, or information graphics convey relationships. | Labels/legends, colour-independent distinctions, necessary graphical contrast, understandable sequence and relationships, text summaries and equivalent detailed data appropriate to the task. Verify the alternative's actual availability and usefulness. Add Interface for interactive filters/tooltips and keyboard routes. Use Accessibility section 18 and [Infographics](../../../guidelines/aesthetics/infographics.md), especially equivalent access. Do not audit statistical validity as accessibility. |
| Document/publication | PDFs, office documents, slides, emails, print, or exported publications. | Structure/tags and reading order where supported, headings, language, links/tables, image alternatives, selectable text, presentation order, enlargement/reflow where applicable, accessible export and distribution. For print, inspect intended size/conditions and the equivalent-access route. Use Accessibility sections 19–20 and format/platform guidance. A screenshot cannot establish PDF tags. |
| Audio/video/motion | Time-based content, animation, automatic playback, timed interactions, or flashing. | Captions, transcript, description of meaningful visuals, player operability, pause/stop/audio control, timing, reduced motion and flashing safety as applicable. Inspect actual media and controls. Use sections 16–17 plus Motion/Sound for delegated techniques. |
| Other/native/physical | Native software, kiosks, immersive/physical formats, or a medium outside the rows above. | Select actual platform/format requirements and test equivalent access under intended conditions. Record any WCAG2ICT mapping and unmet specialist/hardware evidence. Add a module with named criteria and methods, rather than forcing web controls into a static artifact. |

### Measurement anchors

Use the full local guide and actual criterion for decisions. These common anchors make the test plan concrete:

| Check | Baseline test and interpretation |
| --- | --- |
| Text contrast, WCAG 1.4.3 | At least 4.5:1, or 3:1 for qualifying large text. Large means at least 18 pt/24 CSS px regular or 14 pt/about 18.67 CSS px bold. Check scoped exceptions. Compare unrounded ratios. |
| Necessary graphic/control contrast, 1.4.11 | At least 3:1 against applicable adjacent colours. Identify the parts needed to understand or identify it. Decorative borders and state-to-state comparisons are not automatically the test. |
| Colour dependence, 1.4.1 | Information/actions/distinctions remain available through an additional cue. A simulation alone cannot establish the result. |
| Enlargement/reflow, 1.4.4/1.4.10 | Test text at 200% and applicable reflow at 320 CSS px width or 256 CSS px height, applying actual scope/exceptions. A narrow screenshot alone is insufficient. |
| Text-spacing override, 1.4.12 | Simultaneously apply line height 1.5×, paragraph spacing 2×, letter spacing 0.12×, and word spacing 0.16× where used by the script. Content/function must survive. These are test values, not mandated default typography. |
| Pointer targets, 2.5.8 | Test 24×24 CSS px or the actual spacing/equivalent/inline/user-agent/essential exception. Larger platform/product conventions are separate checks. |
| Focus, keyboard and semantics | Reproduce the relevant operation and observed result in named environments. A visible focus ring in one mockup does not prove keyboard reachability, absence of traps, correct order, or AT exposure. |

## `audit.json` contract

Save a JSON object with these fields. It is evidence bookkeeping, not a prescribed narrative structure. Use the same records to fill the report. Additional fields are allowed for module detail and re-audit comparisons.

- `schema_version`: integer `1`.
- `scope`: object containing `description`, `baseline` as `wcag-2.2-aa` or `selected-criteria`, `profiles` as a nonempty array of selected module names, and `sources` as an array naming versions/levels and source locations.
- `evidence`: array of objects with unique `id`, `location`, `method`, and `observation`. Add environment, state, settings, and attachments as needed.
- `criteria`: nonempty array with unique `id`, `source`, `basis` as `required` or `advisory`, `status` using the machine values above, `rationale`, `evidence_ids`, `finding_ids`, and `next_check`. Arrays contain IDs, not repeated prose. Evidence is required for fulfilled, not fulfilled, and N/A outcomes. Every unknown needs a nonempty `next_check`. Every not fulfilled row needs at least one linked finding. Record individual cases additionally when needed.
- `findings`: array with unique `id`, `criterion_ids`, `severity` as `critical`, `high`, `medium`, or `low`, `location`, `impact`, `action`, and `verification`. Criterion links must agree in both directions. Advisory findings may use this shape while staying outside the required score.
- `scores`: object with exactly the six metric keys above. Counts are integers; percentages are finite numbers from 0 to 100 or JSON `null` for undefined denominators.

The evaluation invocation supplies the pre-assessment inventory in `evidence.selected_criterion_ids` and the resolved baseline in `constraints.baseline`. The checker compares inventory, reported counts/percentages, and failure/action links. It cannot verify source truth, semantic adequacy, sampling representativeness, or whether evidence warrants a criterion decision.
