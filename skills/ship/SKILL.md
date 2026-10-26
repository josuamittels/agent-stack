---
name: "ship"
description: "Ship a reviewed change by following the target repository's release, changelog, test, and Git workflow. Use when asked to ship, release, push, or create or update a pull request."
version: "0.2.0"
updated: "2026-10-26"
author:
  - "Josua Mittelstaedt"
references:
  - "Garry Tan"
  - "Peter Steinberger"
  - "Git"
  - "GitHub"
  - "GitLab"
type: "skill"
status: "draft"
---

# Ship

Prepare and deliver a requested change through the target repository's release workflow. Use the repository's own version source, changelog, checks, branch policy, and hosting platform. A request to ship authorizes only the delivery boundary the user asked for; it does not authorize an unrelated merge, tag, deployment, or publication.

## Scope

Use when the user asks to ship or release work, push changes, or create or update a pull request or merge request.

For a changelog-only request, use [Update Changelog](../../disciplines/update-changelog/SKILL.md). For Agent Stack repositories, read [Release Agent Stack](../../disciplines/release-agent-stack/SKILL.md) to apply its local version and delivery rules.

### Boundaries

- Do not assume a `VERSIONS.md`, `CHANGELOG.md`, SemVer, a GitHub remote, or a pull request workflow. Discover and follow the target repository's instructions.
- Do not overwrite or include unrelated staged, unstaged, or untracked work. Do not use broad staging commands without reviewing their full scope.
- Never force-push, silently change the requested target, or claim a pending or unavailable check passed.
- Do not merge, tag, deploy, or publish unless the user requested that action and the repository's policy permits it.
- A skill invocation does not grant host permissions or credentials. Stop at the first unavailable authorization or capability needed for the requested path.

## Inputs

Use the user’s requested change and delivery boundary, repository root, available worktree and Git state, repo instructions, release metadata, declared checks, and available host tools. Resolve the repository root before reading project-level release files.

Read the target repository’s `AGENTS.md` and relevant contribution, release, CI, branch, and pull-request instructions. Read this stack’s [Git guide](../../guidelines/git/reference.md) for branch, staging, commit, push, and recovery defaults; [Versioning guide](../../guidelines/versioning/reference.md) when a version change is relevant; and [Changelog guide](../../guidelines/changelog/reference.md) when maintaining release notes. Project instructions and the user’s explicit request take precedence.

### Default Procedures

If you miss relevant information, first invoke [think-harder](../../disciplines/think-harder/SKILL.md), passing all unresolved constraints and all available context, including references and guidelines, over. If `think-harder` leaves one or more constraints unresolved, use [ask-user-question](../../disciplines/ask-user-question/SKILL.md) to inquire the missing information.

If any discipline is unavailable, perform it directly and report the fallback. Carry unresolved constraints forward and do not invent answers or pretend the dependency ran.

## Workflow

### 1. Establish the repository and delivery request

Inspect the repository root, current branch, staged and unstaged changes, untracked paths, recent history, remotes, and any unfinished merge or rebase. Preserve all existing work. Stop if the repository has an unresolved merge or rebase, the current checkout cannot be identified safely, or the requested changes cannot be separated from unrelated work.

Read project instructions and detect the hosting platform and available authenticated CLI. Identify the requested destination: local commits, a topic-branch push, a direct push to an integration branch, or a pull/merge request. Follow the user’s explicit destination only when repository policy permits it. If the destination, base branch, or authorization is unclear and changes the required Git operation, ask before publishing.

For this Agent Stack repository only, require both the root `AGENTS.md` marker `agent-stack:entry` and the expected `VERSIONS.md`, `map.mmd`, `skills/`, `disciplines/`, and `guidelines/` paths before invoking the repository-specific discipline. If either identity check fails, do not apply Agent Stack release rules.

### 2. Inspect the change and project release sources

Define the exact change set from the request, current diffs, and relevant history. Do not treat every checkout change as in scope. Identify the authoritative version source and scheme, the canonical changelog and its release format, the target branch, and any repository release procedure. Do not assume commit messages alone establish user-facing change facts.

If the repository has a changelog and its policy or the requested release calls for an update, invoke [Update Changelog](../../disciplines/update-changelog/SKILL.md) with verified changes, the intended version or section, and the evidence for each entry. Do not create a changelog or invent a version when the repository has no such convention unless the user requests it or repository instructions require it.

When the Agent Stack identity checks pass, read and apply [Release Agent Stack](../../disciplines/release-agent-stack/SKILL.md). Pass the request, exact change set, Git state, and repository metadata. It returns any `VERSIONS.md` edits and the permitted delivery route. Do not repeat its stack version decision or apply its status gate to another repository.

### 3. Prepare release metadata

Change a project version only when the user requests a release or the repository's release procedure requires one. Keep the existing version source authoritative. Apply the project's documented scheme; use the linked Versioning guide only when SemVer or standalone-file policy applies. For other schemes, preserve their actual labels and rules.

If the version source is absent, contradictory, malformed, or does not establish the bump needed for the requested release, stop before changing it and ask for the missing decision. Do not silently select patch as a default. Update the release date only when the actual release date is known. Keep version, changelog heading, and tag aligned when the repository's procedure requires those values to agree.

### 4. Discover and run required checks

Inspect repository instructions, CI workflows, manifests, and test configuration to find declared build, test, lint, documentation, and generated-file checks that apply to the change. Run the relevant local checks against the final candidate after source and release-metadata edits. Use existing dependencies and documented commands; do not install tools or invent substitute checks without authorization.

Record each check’s exact command or host check name, result, and commit or content it covered. Treat results as `passed`, `failed`, `pending`, `skipped`, or `unavailable`. If a required check fails, repair only within the authorized change and rerun it. If it remains failed, stop before committing or publishing. If a required check cannot run, report the gap and stop before publishing unless the user explicitly accepts that specific gap. A repository with no applicable checks may proceed after recording that none were declared.

After creating or updating a hosted request, inspect its checks on the latest head commit. Report pending, failed, skipped, and unavailable checks as such. Do not claim successful delivery while a required check is failing or unknown.

### 5. Prepare and review commits

Use a topic branch for a review request. Reuse the appropriate working branch when it is already established. For direct integration-branch pushes, verify the exact branch and repository policy before proceeding. If the checkout is on the target branch and the requested work needs review, create a topic branch only when doing so preserves the current work safely; otherwise stop and report the blocker.

Group changes into coherent, ordered commits. Include tests and documentation with the behavior they support; keep release metadata with the release it describes. Stage explicit paths or hunks. Review the complete staged diff, `git diff --cached --check`, and staged file list before each commit. If unrelated staged work cannot be kept out of the commit, stop before committing and ask the user to separate the index. Never create an empty commit.

Use the project’s commit format. If none exists, default to `type(scope): description` with optional scope, as described in the Git guide. Report each created commit and its included paths.

### 6. Push or create the requested hosted request

Before pushing, inspect the destination remote, outgoing commits, complete base-to-head diff, and target branch. Use a dry-run push only if it is supported and has no hidden side effects; do not use a PR/MR dry-run as proof that no branch push can occur. Push only the intended ref, set upstream for a new topic branch, and never force-push.

For a direct branch push, push only when explicitly requested or required by the repository’s release procedure and permitted by its branch rules. If the push is rejected, do not rewrite history or switch destinations silently; inspect the reason and resolve it under repository policy.

For a pull request or merge request, confirm the host CLI and authentication before publishing. Check for an existing request from the branch and update it only as needed; otherwise create one with a concise title and a body that summarizes the change, checks, and known gaps. Do not let the host CLI perform an implicit push; push the reviewed ref explicitly, then create or update the request. If the request cannot be created after the branch push, report the pushed branch and failure without attempting destructive cleanup.

Stop at the user’s requested or repository-defined boundary. Do not merge or publish a release just because the PR is open or its checks are green.

### 7. Report the delivery

Report the repository and target, release version and changelog updates if applicable, checks with their actual results, commit IDs, pushed ref, PR/MR URL, and any unavailable or pending work. Distinguish local commits from pushed commits and a created request from a merged or published release.

Include a machine-readable evidence object in the completion record when it helps verify delivery or when repository policy requires it:

```json
{
  "repository": {
    "agent_stack_identity": false,
    "stack_status": "not_applicable"
  },
  "release": {
    "version_changed": false,
    "inventory_synced": false,
    "no_changes": false
  },
  "checks": [],
  "actions": []
}
```

Use the actual identity result and lifecycle status; list each check with `required`, `status`, `phase` (`prepublish` or `remote`), and covered `head_sha` where available. List completed Git or hosting actions as objects with an `action` field such as `commit`, `push`, `create_pr`, `update_pr`, `merge`, or `tag`. For Agent Stack releases, include `release.component_frontmatter` as the path/version/status values read from eligible component frontmatter, so the inventory can be independently compared. Set `release.no_changes` to true only when the requested change set is empty. Do not report an action that did not occur.

### 8. Validate the completed delivery

Ship performs these completion checks directly against the final candidate and delivery evidence before reporting success:

- Re-read the authoritative version source and changelog section. Confirm their version, date, and release notes agree wherever the project requires them to.
- Compare the requested change set with the final staged diff and committed diff. Confirm unrelated work was excluded and no empty commit was created.
- Confirm every required local check passed against the final candidate. If any source or metadata changed after a check, rerun that check. Keep skipped, unavailable, failed, and pending results distinct from passed results.
- For a hosted request, confirm its target and latest head commit. Check remote status against that exact head and report any pending, failed, skipped, or unavailable checks accurately.
- For Agent Stack, recheck that the identity gate was satisfied, the component inventory matches current frontmatter, and the completed Git actions match the lifecycle route returned by Release Agent Stack.
- Confirm the final state is the one requested: local commit, pushed branch, open PR/MR, merged change, or published release. Do not report a later state than the evidence supports.

If a mismatch appears, repair it within the authorized scope, rerun affected checks, and repeat this validation. If it cannot be resolved safely, stop and report the mismatch and current delivery state.

## Output

Return the completed commits and delivery state, version/changelog updates, applicable checks and their evidence, hosted request URL when created, and unresolved blockers. State whether work is local, pushed, under review, merged, or released. Never call a pending state complete.
