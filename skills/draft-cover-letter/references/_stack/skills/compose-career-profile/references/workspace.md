# Career workspace operations

Read when a career skill works in an explicitly selected career workspace. This reference owns application identity, numbering, archiving, working paths, and delivery. Use the bundled [workspace helper](../scripts/career_workspace.py); do not reimplement these operations in prose or a one-off script.

## Initialize

Setup Career Stack selects the root and supplies its bundled AGENTS template. Run:

```bash
python "$AGENT_STACK_ROOT/skills/compose-career-profile/scripts/career_workspace.py" init --workspace /path/to/career --agents-template /path/to/setup-career-stack/templates/AGENTS.md
```

The helper creates `applications/`, `references/`, `staples/`, and `work/` while preserving an existing AGENTS file. It does not restructure an existing project. Inspect meaningful existing contents first.

## Register and archive an application

Use the employer's requisition id or canonical vacancy URL as the application id. Without one, choose a stable label from the supplied role and reuse it. Distinct requisitions or deliberate reapplications use distinct ids; a repost of the same requisition reuses its id. Resolve ambiguous duplicates before allocation.

Extract the complete supplied posting into a UTF-8 plain Markdown source file in a working location. Exclude site navigation; preserve the posting's words and order. This canonical extracted source is the archive input and the evaluator's `source_text`. Do not pass a summary as a full posting. The helper copies this text exactly; it does not retrieve URLs or determine completeness.

```bash
python "$AGENT_STACK_ROOT/skills/compose-career-profile/scripts/career_workspace.py" application --workspace /path/to/career --id vacancy-id --company Example --role Analyst --source /path/to/full-posting.md
```

Without a complete posting, omit `--source`, record the archive as unavailable, and continue supported work. Ask for the full posting if needed; never invent a partial `job.md`. The same operation applies to CV, letter, and answer-only applications.

The JSON response supplies `application_folder`, `working_folder`, and archive evidence. Reuse those paths. The persistent `references/applications.json` reserves monotonically increasing numbers, including failed allocations and deleted application folders. Preserve this registry and withdrawn records. Existing numbered folders are included when allocating the next number. Duplicate ids reuse their paths; conflicting company/role details fail. Different existing job text is preserved. Obtain replacement approval and make the approved archive correction explicitly; the helper never replaces it silently.

Use a fresh revision directory inside `work/<application-folder>/` for tailored sources and QA. Keep reusable staple sources beside their staple. Final application folders contain only `job.md`, approved `CV.pdf`, and optional approved `Motivation_Letter.pdf`. Do not store durable sources only in temporary storage. Generation and QA helpers reject output inside `applications/`, or beneath a directory containing `job.md`, including resolved path aliases. Temporary QA outside those paths is allowed. Final delivery copies only the reviewed PDF.

Operations use a workspace lock. If another operation owns it, stop and retry after it finishes. Following a crash, inspect the registry and partial paths before removing a stale lock; do not reset the registry or reuse reserved numbers.

## Deliver the reviewed PDF

Generate and inspect a draft in its working directory. Obtain approval of the exact content and bind the reviewed artifact to its SHA-256 hash. For CVs, require the current validation report and matching PDF, content, and profile hashes before delivery. A hash identifies bytes; it does not prove approval or visual quality.

```bash
python "$AGENT_STACK_ROOT/skills/compose-career-profile/scripts/career_workspace.py" deliver --source /path/to/work/CV.pdf --destination /path/to/application/CV.pdf --approved-sha256 APPROVED_PDF_SHA256 --validation /path/to/work/qa/validation.json
```

This copies the reviewed bytes without regeneration and refuses changed sources or existing destinations. Use `Motivation_Letter.pdf` for a requested letter. For approved replacements, preserve the old final until replacement approval, then archive it under `work/` before delivering the new file. Outside a workspace, use only the user's explicit destination.
