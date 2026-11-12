# Verification evidence

Read when assembling Build's final objective invocation record. Use the shared [runner contract](../../spawn-evals/references/runner.md) for record fields and execution. This reference supplies only Build's evidence shape.

## Scope of the objective check

The package checks Python comment tokens and module, class, and function docstrings in authored or rewritten units. It does not check other languages, test adequacy, runtime behavior, design quality, or the completeness of the producer's inventory. Keep those limits beside the result. A not-applicable result for a non-Python change does not establish that its code has no comments.

Use language-aware project tooling and engineering review for other languages. This package deliberately avoids a regular-expression scanner that would mistake strings for comments. A future language extension needs its own reliable parser and declared inputs.

## Required evidence

Supply `evidence.source_inventory` as an array covering every added or modified handwritten code file in the task. Each entry has these fields:

- `path`, the project-relative source path.
- `language`, with `python` for Python, including `.pyi`, and the actual language name otherwise.
- `output_key`, the key in `output_files` whose complete UTF-8 content is that file's final source.
- `ranges`, an array of inclusive `[start_line, end_line]` pairs covering authored or rewritten units in the final source. Use the whole file for a new file and the complete rewritten function, class, or block for an edit. Include comment-only edits. Do not restrict ranges to changed statement lines to evade nearby comments or docstrings.

Include all inventoried final sources in `output_files`. Deleted files have no final source and are omitted. Keep a separate deletion account in the implementation summary. Generated and vendor files are outside this handwritten-source inventory and remain governed by their generator or source policy. Required existing legal notices and executable headers should remain outside authored ranges when they are not being rewritten. A conflict inside a rewritten unit remains unresolved rather than receiving a silent exemption.

Missing inventory, unavailable content, invalid ranges, or Python that cannot be parsed is unverified. A detected comment token or docstring within an authored range fails. No Python entries makes this narrow check not applicable. An explicit empty inventory is appropriate only when the task changes no surviving handwritten code.

The checker reads provided source text only. It executes no project code and does not run tests or open browsers. Keep test commands, exit statuses, runtime evidence, and reviewer findings in the task's normal verification account, rather than inventing machine approval from those narrative claims.
