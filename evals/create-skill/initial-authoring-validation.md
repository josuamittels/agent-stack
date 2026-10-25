# Initial validation record

Date: 2026-10-24. Skill: create-skill, 0.1.0, draft.

## Executed structural checks

- Ruby's standard YAML parser parsed create-skill, natural-writing, and translate. All three have the template's required fields, appropriate string/list types, matching valid slugs, one verbatim missing-information paragraph under Inputs, and no unfinished scaffold markers.
- Checked bundled references and document links in those skills. Cross-skill invocation contracts were reviewed as interfaces rather than evidence of runtime execution.
- Node parsed evals.json: 15 unique cases, each containing a prompt, fixtures, and observable expected outcomes. Read the rubric against those outcomes, including critical approval, naming, attribution, preservation, and lifecycle failures.
- Node checked map relationships: one affected node per identifier, no repeated explicit edges, and all six Create Skill relationships (templates, research-web, think-harder, ask-user-question, Mermaid, spawn-evals).
- Mermaid 11.17.2 parsed the complete saved map. A temporary localhost viewer rendered it in Chromium with @mermaid-js/layout-elk 0.2.0. Inspected the full screenshot: Create Skill and Spawn Evals appear in Admin Skills with the expected entry styling; the added connections and existing sections are visible without clipping. Some long connections remain in this existing large map; unrelated layout/configuration was preserved. Preview artifacts are temporary, outside the repository.
- Scoped git whitespace checks passed for the two modified tracked skill files. Reviewed the newly authored files separately. The full working-tree whitespace check also reports a pre-existing trailing blank line in plan.md; that unrelated file was left untouched.
- Verified sources/research_create-skill.md remains ignored by the existing sources/* rule. No ignore-rule change or force-add was performed.

## Manual scenario walkthrough

This is a review of the saved instructions against each fixture, not independent agent execution and not a behavioral suite pass.

| Scenario | Observed instruction path and conclusion |
| --- | --- |
| Named creation | Inputs accepts the supplied name; steps 1–4 establish the contract, research, and copy/fill the shared template. Initial version/status are explicit. |
| Unnamed creation | Inputs preserves naming as a user decision after reasoning; step 1 requires the name to be settled before authoring. |
| Invalid name | Inputs rejects an unsafe or malformed slug and asks for the user's replacement, avoiding traversal or silent normalization. |
| Duplicate name | Collision handling blocks an overwrite; the existing-skill branch requires a concrete approved proposal. |
| Research and attribution | Step 2 inspects original bodies and creates the per-source/combined record; step 4 attributes only verified meaningful influences. |
| Dynamic discovery | Step 2 explains the JavaScript-loaded directory and observed public endpoint alternative without interpreting empty static HTML as no matches. |
| Discipline fallback | Inputs names the three permitted direct fallbacks and requires disclosure; unresolved constraints persist into clarification. |
| Research blocked | Step 2 completes available investigation and asks before proceeding with an evidence-limited draft. |
| Edit before approval | Steps 1–3 inspect the failure and comparable approaches; step 3 withholds target/resource/map edits while presenting the proposal. |
| Edit after approval | Step 3 honors specific existing approval, and step 4 preserves unrelated behavior and metadata. |
| Map reuse | Step 5 requires the existing identifier, supported edges and styles, no duplicate nodes/edges, and preservation of unrelated changes. |
| Stable promotion | Step 5 requires explicit user approval, deletes only the matching research file, removes dangling pointers, and retains operational knowledge. |
| No automatic promotion | Draft is the creation default; passing validation alone does not authorize a status change or research deletion. |
| Evaluation handoff | Step 6 specifies spawn-evals inputs and expected returned criteria/rubric/tests, then reviews coverage and separates design from execution. |
| Adjacent task | Scope distinguishes standalone guidelines, disciplines, agents, and installation from skill creation; it preserves the requested destination. |

## Practical limits

No independent behavioral or runtime discovery evaluation was executed. The fixture suite and scoring rubric are prepared for evaluation. Manual walkthroughs support instruction coverage but do not establish how a fresh agent will behave. No claim is made that this draft is installed in a host discovery root or ready for stable promotion. The shared template and unrelated plan.md changes remain intact.
