# Objective package setup

Use this reference only after Create Skill determines that the target skill has at least one meaningful, deterministic, task-specific check. If no such check is possible, Create Skill must skip Spawn Evals entirely, create no package, and omit all evaluator references and handoffs from the target skill. This step authors checks for future real invocations; it does not run them.

## Package files

Create only these files under `evals/<skill>/`:

- `rubric.json` declares `schema_version: 1`, the exact skill slug, and a non-empty `checks` array.
- `checks.py` defines one callable function named by each check's `handler` field. The runner calls each handler once with the invocation record.

Each rubric check has exactly `id`, `description`, `handler`, `mandatory`, and `required_inputs`. IDs are unique lowercase slugs. `required_inputs` contains JSON Pointers into the runtime object. `mandatory` is boolean. Descriptions state the measurable pass condition in plain language. Do not add weights, qualitative anchors, expected outputs, or test scenarios.

Each handler returns exactly `status`, `step`, `aspect`, `observed`, `expected`, and `evidence`. Status is `pass`, `fail`, `unverified`, or `not_applicable`. `step` and `aspect` are non-empty strings. `evidence` lists JSON Pointers to the supplied invocation record or its output/evidence fields. The runner ensures every declared check gets a result; never turn missing data into a pass.

Each check handler receives this object:

```json
{
  "schema_version": 1,
  "skill": "example-skill",
  "invocation_id": "unique-run-id",
  "request": "Original request text",
  "constraints": {
    "max_words": {"value": 600, "source": "request"},
    "depth": {"value": "standard", "source": "skill_default"}
  },
  "outputs": {"main": "Complete UTF-8 artifact text"},
  "evidence": {}
}
```

The source of each constraint is exactly `request` or `skill_default`. If the request explicitly overrides a default, pass the requested value and use `request`. Include only constraints that apply to this invocation. `output_files` in the input record maps artifact names to complete UTF-8 file paths; the runner loads their contents into `outputs`. Evidence must be structured JSON and may include source inventories, link lists, process counts, or other machine-verifiable records.

## Authoring checks

1. Map each meaningful objective criterion to an input field and a reproducible script condition. Exclude generic checks such as output existence when they do not measure the skill's intended outcome.
2. Use shared helpers from `disciplines/spawn-evals/scripts/checklib.py` for word counts, character counts, protected tokens, and URL reachability where they fit.
3. Treat timeouts, blocked requests, unavailable files, missing evidence, and ambiguous matches as unverified. A confirmed limit violation is a failure.
4. Keep request limits separate from skill defaults so the output can identify why a threshold applied.
5. Run `python disciplines/spawn-evals/scripts/runner.py --validate-package --skill <skill-slug>`. This checks rubric shape and checker syntax without calling handlers. Do not run the skill's checks or the completed authoring result here.

## Research example criteria

When a future Research package is prepared, its checks can use structured evidence to verify report word count, cited-source count, journal identity and supplied score thresholds, and whether cited article URLs resolve. The run record must include the selected depth, its configured ranges, any request overrides, a complete source inventory, and the journal score data revision. Reachability alone does not prove source identity or the truth of findings. Do not retain or recreate the old Research qualitative or claim-verification rubric.
