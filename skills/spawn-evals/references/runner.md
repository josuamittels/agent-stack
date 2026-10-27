# Invocation runner contract

Use this reference whenever a skill calls Spawn Evals for a completed output. The runner invokes the configured Python checker directly in the current process; it does not create agents, contact a model, or persist input artifacts.

## Invocation record

Write one JSON object with exactly these fields:

```json
{
  "schema_version": 1,
  "skill": "example-skill",
  "invocation_id": "unique-run-id",
  "request": "Original user request",
  "constraints": {
    "depth": {"value": "standard", "source": "skill_default"}
  },
  "output_files": {"main": "/absolute/path/to/output.md"},
  "evidence": {}
}
```

`constraints` maps names to exact `{ "value": ..., "source": ... }` objects. `source` is `request` when the user supplied the value or `skill_default` when the skill selected it as its documented default. The skill passes the resolved value it used. `output_files` must identify complete UTF-8 outputs. `evidence` contains only structured data needed by the package checks.

Run from the repository root:

```sh
python skills/spawn-evals/scripts/runner.py --skill example-skill --record /absolute/path/to/record.json
```

The runner prints a JSON result with schema version, skill, invocation ID, overall status, and one result per package check. It exits 0 for pass, 1 for fail, and 2 for unverified or invalid inputs. A missing package produces `not_passed_unverified`; the runner does not create one.

## Result interpretation

- `pass`: every mandatory applicable check passed.
- `fail`: at least one mandatory check established a violation.
- `not_passed_unverified`: no mandatory failure was established, but a package, input, evidence item, or external check was unavailable.
- `not_applicable`: the check does not apply to this invocation and is excluded from the overall result.

Each result names its verification `step` and `aspect`, observed and expected values, and evidence locations. A script should distinguish a confirmed negative outcome from an inability to check. Do not add an aggregate percentage or qualitative language review.

## Privacy

The runner appends a compact record to `evals/.local/runs.jsonl`: UTC timestamp, skill slug, hashed invocation ID, package digest, overall status, and check IDs with statuses. It does not persist prompts, outputs, observed values, or source evidence. Callers may include the full check result with the completed artifact; do not persist the full request, output, or evidence in a shared log unless the user explicitly requests that storage.
