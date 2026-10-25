# Evaluation package setup

Read at initialization and after a relevant skill/resource or requirement change. Use the target's real intent; invent realistic synthetic examples, not a fictional user preference. Clarify only gaps that materially prevent a defensible rubric. The target artifact should not dictate its own passing standard.

## Maintained package

Under `evals/<skill-name>/`, maintain:

- `suite.json`: schema version 1, skill slug, active rubric version, and the relevant resource paths used for the skill digest.
- `rubrics/v1.json` and later immutable versions: skill, version, and 3–6 criteria with weights totaling 100. Never overwrite an existing frozen version; increment the version and update the manifest.
- `cases.json`: three lightweight synthetic cases (normal, boundary, failure) with organic prompts, synthetic input, expected behaviors for the coordinator only, and known satisfactory/defective calibration artifacts. Extra regression cases may be retained when a demonstrated failure justifies them; ordinary grading never reruns the suite.
- `checks/` only when a real domain constraint benefits from an executable check. Use approved helpers directly, not arbitrary commands embedded in data.
- Local `runs.jsonl` and `.local/`: abstract outcomes, verdict cache, locks, and suite completion marker. Both are ignored by Git.

Use the checked-in packages as concrete examples. Criterion IDs use lowercase letters, digits, and single hyphens (no underscores). A criterion contains `id`, `description`, `weight`, `critical`, `kind` (`check` or `judge`), `anchors` with keys `0`, `1`, `2`, `category`, and `improvement_guidance`. Optional `applies_if` names a boolean task-context flag set before grading; omit it for unconditional criteria. Critical criteria may not be conditional. Evidence is required for every applicable criterion. Category is one of `intent`, `fidelity`, `structure`, `evidence`, `boundaries`, `evaluation`, `quality`, or `lifecycle`.

Make rubric descriptions, anchors, cases and repair guidance reusable and synthetic. Logs inherit static guidance from the rubric, so no real user text belongs there. Cover the outcome, important failure conditions, boundaries/handoffs, and necessary evidence. Prefer 3–6 measurable criteria over a broad generic checklist. Mechanical constraints belong in checks; judgment criteria need discriminating anchors rather than taste words. Domain branches can use an applicability flag; missing flags make evaluation incomplete.

## Initial calibration and suite

1. Validate package structure with the helper. Check coverage against skill purpose and current requirements; known good and defective artifacts must separate on the relevant criteria. If they do not, refine the rubric before freezing it.
2. Create neutral temporary producer copies and organic requests as specified in the Betabert contract. Spawn the three synthetic-case producers with display names **Apollo** (normal case), **Athena** (boundary case), and **Prometheus** (failure case), using task names `apollo`, `athena`, and `prometheus` respectively. If a task name is occupied, append `_<short-id>` while preserving its display name. Run each case in a fresh context with no rubric visibility; confine writes to temporary project locations. Never exercise external side effects just to populate a suite.
3. Grade actual outputs with the frozen rubric, using objective checks and a separate fresh Betabert. Also grade the known calibration artifacts without disclosing expected verdicts to the judge. Do not claim an authored expected outcome is an executed test.
4. Record abstract case outcomes through the helper with mode `suite` or `calibration`. Call `mark-suite` with their returned record fingerprints after the full suite and calibration completed acceptably. The marker binds those results to the skill/resource digest, active rubric, cases, checker bytes, and evaluator configuration. `status` reports whether this package needs its suite rerun. Do not mark it complete from manual inspection alone.

For a new skill created by create-skill, initialize this target package and run its synthetic suite. Separately validate create-skill's own finished authoring output as its actual invocation; these measure different things. If a domain's suite cannot run within authorized resources, report the setup as prepared with incomplete suite evidence; do not silently treat its outputs as acceptable.

## Revisions

Keep the user's quality bar and acceptance policy fixed. A skill change that does not change the bar still invalidates the suite marker through the resource digest. A changed bar needs a new rubric version. Preserve useful earlier regression cases. A bad case or ambiguous rubric is a measurement problem: explain the correction, revise it explicitly, and keep its new version distinct from a skill improvement. Never pool scores from different rubric versions into one trend without labeling that change.
