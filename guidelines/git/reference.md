---
name: "git-best-practices"
description: "Reference for grouping file changes, ordering commits, writing commit messages, and using Git branches, worktrees, reviews, integration, and recovery. Consult when preparing or reviewing repository changes."
version: "0.1.0"
updated: "2026-10-25"
author:
  - "Josua Mittelstaedt"
references:
  - "Git"
  - "The Linux Kernel Organization"
  - "Conventional Commits"
  - "GitHub"
  - "conventional-changelog"
  - "Lubosky"
type: "reference"
status: "draft"
---

# Git best practices

Keep repository changes focused, reviewable, and recoverable. These conventions serve contributors and agents working in existing repositories. Follow explicit task instructions, repository policy, and host requirements first. The defaults below apply where those leave a choice.

Examples use `origin` as the remote, `main` as the integration branch, and illustrative paths. Substitute the repository's actual values. Commands that change history, publish work, or discard files require the authorization appropriate to the task. Reading this reference does not grant it.

## Contents

- [Inspect the starting state](#inspect-the-starting-state)
- [Choose a branch or worktree](#choose-a-branch-or-worktree)
- [Plan commit groups](#plan-commit-groups)
- [Order a commit series](#order-a-commit-series)
- [Stage and commit focused changes](#stage-and-commit-focused-changes)
- [Write commit messages](#write-commit-messages)
- [Synchronize and resolve conflicts](#synchronize-and-resolve-conflicts)
- [Prepare and integrate a pull request](#prepare-and-integrate-a-pull-request)
- [Undo and recover work](#undo-and-recover-work)
- [Manage repository content and releases](#manage-repository-content-and-releases)
- [Coordinate concurrent work](#coordinate-concurrent-work)

## Inspect the starting state

Before editing, identify the checkout, branch, existing changes, and any operation in progress. Inspect the relevant history and repository instructions. An empty branch name from `git branch --show-current` indicates detached HEAD.

```sh
git rev-parse --show-toplevel
git status --short --branch
git branch --show-current
git diff --stat
git diff --cached --stat
git log -5 --oneline
```

The working tree contains files being edited. The index is the staged snapshot for the next commit. `git diff` shows tracked changes between the working tree and index. `git diff --cached` shows changes between the index and `HEAD`. Untracked file contents appear in neither diff, so inspect files reported by status separately.

Preserve existing staged, unstaged, and untracked work. Attribute changes by inspecting their content and task context. File ownership alone is insufficient when several people or agents edit the same file. Resolve an unfinished merge or rebase before starting another history operation.

Check the remote and target branch before fetching or pushing. `git remote show origin` can query the remote's default branch. A locally recorded `origin/HEAD` may be absent or stale. Keep credentials and private remote URLs out of shared logs.

## Choose a branch or worktree

Use a short-lived topic branch for one reviewable outcome. Reuse a suitable task branch when continuing its work. Start an independent task from the intended integration branch, unless it explicitly depends on another change.

Use lowercase words separated by hyphens. Prefer a descriptive prefix and outcome, such as `fix/retry-empty-response` or `docs/git-guidelines`. Follow a required host prefix, such as `codex/git-guidelines`, and an explicitly requested branch name. Branch naming is a house convention rather than a Git requirement.

With a clean checkout and a verified `origin/main` target, a new independent branch can start directly from the fetched target:

```sh
git fetch origin
git switch --no-track -c docs/git-guidelines origin/main
```

This creates the topic branch without setting the integration branch as its upstream. After the first authorized push, set the upstream to the corresponding topic branch.

Use a worktree when an independent checkout avoids interrupting another task or disturbing local changes. Reuse a suitable existing checkout first. In a host that manages worktrees, use its creation, attachment, and cleanup tools. For a plain Git checkout, the equivalent is:

```sh
git worktree list
git worktree add -b docs/git-guidelines ../git-guidelines origin/main
```

The new worktree shares repository objects and ordinary branch refs, but has its own working files and index. Existing uncommitted changes are not copied. Worktrees isolate checkouts, not remote branches or all configuration. Let each active worktree use a distinct branch.

Remove a plain linked worktree with `git worktree remove ../git-guidelines` after confirming its work is preserved. Check ignored files before removal because they may contain needed local assets. A managed worktree follows its host's archive or cleanup procedure.

## Plan commit groups

Group changes by a single purpose that can be explained, reviewed, and reverted coherently. One commit may span many directories. One file may contribute different hunks to several commits. File extension, directory, authoring order, and file count do not determine the boundary.

Before staging a mixed change set, make a short ordered plan. For each group, identify its purpose, files or hunks, companion changes, dependencies on earlier groups, and proposed subject. Assign each intended change to one group. Leave unrelated existing work outside the plan. A simple fix with an obvious boundary needs no formal planning artifact.

Split a group when its parts have independent reasons to exist, independent review decisions, or independent rollback needs. Keep parts together when separating them would create an invalid or misleading intermediate state. A subject that needs to join two unrelated outcomes with "and" is a useful signal to reconsider the boundary. Prefer a larger coherent commit over several incomplete ones. Use no fixed file or line threshold.

### Which files belong together

| Changes | Grouping convention |
| --- | --- |
| Bug fix and regression test | Commit together, with fixtures and snapshots needed to demonstrate the corrected behavior. |
| Feature implementation across server, client, and shared types | Keep together when they form one usable behavior. Split independently usable prerequisites or increments. Do not split solely at frontend and backend directories. |
| Documentation and examples for changed behavior | Include with the implementation so its contract is accurate at that commit. Split an unrelated documentation correction or a standalone documentation improvement. |
| Package manifest and corresponding lockfile | Include together for the same dependency change. Include necessary compatibility edits and checks. Split unrelated dependency upgrades when they can be reviewed and rolled back independently. |
| Generated output and its source or generator change | Keep required checked-in generated files with the change that produces them. Separate unrelated regeneration churn. Follow repository policy about which generated files are tracked. |
| Rename or move | Keep deletion, addition, and required reference updates together. Separate a substantial behavior rewrite when the move alone is valid and the separation makes review clearer. |
| Refactoring and behavior change | Extract a useful behavior-preserving prerequisite into an earlier commit. Keep tiny local restructuring with the fix when separation adds little clarity or leaves unusable code. |
| Formatting, lint cleanup, and behavior change | Separate broad mechanical changes from logic edits. Include minimal formatting needed for changed lines. Keep formatter configuration with the reformat it requires when the repository checks require both together. |
| Configuration, migration, and implementation | Include changes required to make that commit work. Split a compatible preparatory migration or configuration addition when it is independently valid. Separate deployment steps still need a rollout plan. |
| Tests or CI only | Use a separate commit when improving existing coverage or automation independently. Keep test updates caused by a behavior change with that change. |
| Several fixes in one module | Split by root cause and independently verifiable outcome. A shared path does not make unrelated fixes one unit. |

Choose boundaries based on the actual dependency, not the row label alone. For example, a library upgrade and the compatibility fix it requires can belong together, while an optional second upgrade belongs elsewhere.

### Worked grouping example

Suppose a working tree adds invoice CSV export, extracts an existing invoice query, updates lint tooling, and corrects a spelling error in the README. The following file names and changes are illustrative:

| Commit | Files or hunks | Reason |
| --- | --- | --- |
| `refactor(invoices): extract invoice query` | Extraction hunks in `src/invoices/service.ts`, new `src/invoices/query.ts`, and adjusted existing tests | A behavior-preserving prerequisite that works without export. |
| `feat(invoices): add CSV export` | Export hunks in that same service, `src/routes/invoice-export.ts`, `src/ui/ExportButton.tsx`, export tests, fixtures, and `docs/invoices.md` | One usable feature with its validation and documented contract. |
| `build(lint): upgrade lint tooling` | The lint dependency entries in `package.json`, corresponding lockfile changes, and required lint configuration | An independent tooling change. Include required formatting here if its new checks demand it. |
| `docs: correct installation command spelling` | Only the unrelated README correction | A standalone correction that can be reviewed independently. |

The first two commits depend on each other in that order. The latter two are independent and may belong in separate pull requests. If the extraction has no clear value or cannot stand alone, include it in the feature commit. Do not create a separate "tests" commit for export or stage all of `service.ts` into the prerequisite.

## Order a commit series

Order commits by dependency and explanation. Put a valid prerequisite before its consumer, then introduce complete increments. Each retained commit should build and pass the checks applicable at that point. This makes regression isolation and selective reuse dependable. A green final branch does not justify broken commits in the middle.

A common sequence is a necessary behavior-preserving extraction, a complete feature or fix with its tests, then cleanup made possible by the new behavior. Use that sequence only when each step makes sense. An API transition may need an additive compatible interface first, updated callers second, and removal of the old interface last. Explain the dependency in the consuming commit's body when it is not obvious.

Write a failing regression test first during development if useful, then retain it with the fix in the final series. A separate test commit is appropriate when it already passes against existing behavior or establishes a deliberate test infrastructure prerequisite. Avoid ordering commits by a fixed list of types such as docs, tests, fixes, and features.

For schema or deployment changes, distinguish history order from runtime rollout order. Putting a migration before code in Git does not make incompatible deployments safe. Keep the necessary compatibility and rollout instructions with the relevant change.

Fold local follow-up corrections into the commit they complete before review when rewriting the unpublished topic is appropriate. Replace temporary "WIP" or "fix review" subjects with the lasting intent. Preserve published history when collaborators depend on it, following the rewrite rules below.

## Stage and commit focused changes

Stage explicit paths, or use `git add -p` when a file contains independent changes. Review the complete staged diff, including changes staged before the current task. A plain `git commit` records everything in the index.

```sh
git add -- guidelines/git/reference.md
git diff --cached --check
git diff --cached -- guidelines/git/reference.md
git diff --cached --stat
git status --short
git commit -m "docs(git): document collaboration and recovery"
```

Commit only after the whole staged snapshot belongs in that commit. Broad commands such as `git add .`, `git add -A`, and `git commit -a` require reviewing their full scope first. `git diff --cached --check` detects whitespace errors and conflict markers, but does not establish correctness.

Run the checks appropriate to the change. Test the behavior affected by code changes and inspect rendered output when layout matters. Keep test claims tied to the actual revision checked. If a required check cannot run, state the gap in the review description.

When one file spans groups, stage only the intended hunks and review both the staged result and what remains. Use `git add -p` in an interactive session. If the automation host cannot answer its prompts, use a carefully reviewed index patch or isolated checkout. Preserve the original working changes and existing staged intent. Do not force unrelated changes into a group because partial staging is inconvenient.

Verify the staged snapshot rather than assuming the working tree matches it. Unstaged changes can make a working-tree test pass even though the proposed commit is incomplete. For a complex partial commit, use an isolated checkout of the proposed snapshot or another repository-supported check. After each commit, inspect its file list and remaining status against the next planned group. Keep hooks enabled and address a rejected commit rather than bypassing them.

## Write commit messages

Read `CONTRIBUTING.md`, any commitlint or release configuration, and recent maintained history before choosing a format. Explicit repository rules take priority over examples in this reference. Preserve a consistent established plain-subject style. When choosing a format for a repository without one, use `type(scope): description`, with the scope optional. The typed examples below are house defaults based on Conventional Commits, not requirements imposed by Git.

### Subject, body, and footers

Name the concrete effect in the imperative, such as "preserve", "add", "reject", or "extract". Prefer "reject expired reset tokens" to "update auth files" or "fix issue". Use lowercase after a type prefix except for proper names and exact identifiers. Use an initial capital for an unprefixed subject. Omit a trailing period. Aim for roughly 50 characters and keep the full subject within 72 unless the project requires another limit. Clarity takes priority over shortening an essential identifier.

Use a blank line between the subject and body. For a nontrivial change, explain the triggering problem, why the chosen approach solves it, and material compatibility or migration consequences. Include a rejected alternative when it explains a consequential choice. A self-explanatory typo correction can use only a subject. Wrap prose body lines at about 72 characters, allowing long URLs and exact notation to remain intact.

Place issue references and required trailers after another blank line. Name the actual issue when known. Use a closing keyword only when the change resolves that issue and the hosting workflow supports it. Keep the message meaningful without opening the issue, reading a chat, or reconstructing the development session. Avoid file inventories, timestamps, "as discussed", and claims about tests that were not run.

```text
fix(auth): reject expired reset tokens

The reset endpoint accepts tokens after their expiry time. Check expiry
before updating the password so an old email cannot reset the account.

Include regression coverage for expired and still-valid tokens.

Closes: #418
```

The subject describes the outcome, the body preserves the reason, and the footer connects the illustrative issue. In a plain-subject repository, use `Reject expired reset tokens` with the same body.

### Types and scopes

Choose a type by the commit's primary purpose, including its companion tests and documentation. A feature commit stays `feat` when it also changes tests and a guide. Do not split a coherent commit merely to give each file category its own prefix.

| Type | Use | Illustrative subject |
| --- | --- | --- |
| `feat` | Add a capability | `feat(invoices): add CSV export` |
| `fix` | Correct behavior | `fix(auth): reject expired reset tokens` |
| `refactor` | Restructure while preserving behavior | `refactor(invoices): extract invoice query` |
| `perf` | Improve runtime performance | `perf(search): reuse compiled matchers` |
| `docs` | Change documentation independently | `docs(git): explain commit grouping` |
| `test` | Improve tests independently of a behavior change | `test(auth): cover existing expiry boundaries` |
| `style` | Change formatting without behavior changes | `style(parser): apply formatter` |
| `build` | Change dependencies, packaging, or build tooling | `build(deps): upgrade CSV parser` |
| `ci` | Change CI configuration | `ci: run checks on supported Node versions` |
| `chore` | Other maintenance with no more specific type | `chore: remove obsolete issue template` |
| `revert` | Reverse an earlier change | `revert: remove CSV export` |

Use the project's accepted type list. Release automation may assign meanings to types beyond this table, particularly dependency upgrades. Inspect that configuration rather than assuming `build`, `perf`, or `revert` has a particular version effect. A dependency or configuration change can still break a public contract.

Use a short, stable subsystem or package name for the scope, such as `auth`, `invoices`, or `cli`. Reuse an accepted scope rather than inventing a file path, task number, contributor name, or scope for every changed file. Omit it for a coherent change across the repository when no shared scope fits. A broad scope must not conceal unrelated purposes that should be separate commits.

### Breaking changes

When using Conventional Commits, mark an incompatible public change with `!` before the colon or a `BREAKING CHANGE:` footer. Prefer both when a migration explanation is useful. State what stops working and how consumers should adapt. A large diff is not automatically a breaking change, and a small default or runtime-support change can be one.

```text
feat(api)!: require cursor pagination

Replace page-number pagination to keep results stable while invoices
are added during traversal.

BREAKING CHANGE: The invoices endpoint no longer accepts page or limit.
Use cursor and page_size, and follow next_cursor from each response.
```

Use issue references, trailers, sign-off, and commit signing when the project requires them. Preserve correct authorship. Amend an unpublished task commit when that improves its coherence. Coordinate any amendment of published commits because it changes their identities.

## Synchronize and resolve conflicts

Fetch before choosing how to integrate remote work. Fetch normally updates remote-tracking refs without integrating those changes into the current branch. Inspect the difference, then choose the operation explicitly. `git pull` also integrates, so use it only with a known strategy.

For a topic branch targeting `origin/main`, inspect its divergence after fetching:

```sh
git fetch origin
git log --oneline --left-right HEAD...origin/main
git diff --stat origin/main...HEAD
```

The log shows commits unique to each side. The three-dot diff shows the topic's changes since the common ancestor. Review the final combined result as well when integration changes behavior.

| Situation | Default | Reason and exception |
| --- | --- | --- |
| Local integration branch is only behind its remote | `git merge --ff-only origin/main` | Advances without creating a merge commit. If it fails, inspect local divergence. |
| Unpublished topic needs a newer base | `git rebase origin/main` | Replays task commits on the new base. Preserve intentional merge topology when relevant. |
| Several contributors depend on published topic commits | `git merge origin/main` | Preserves existing commit identities. Rewrite only with their coordination. |
| An agreed published topic rewrite is necessary | Push with an explicit expected remote commit | Rejects the update if that branch moved unexpectedly. |

Start merge and rebase operations from a clean working state. Commit task work when appropriate, use a separate worktree, or deliberately stash work that you own. `git stash push -u -m "Pause Git guideline work"` includes untracked files and excludes ignored files. Inspect `git stash list` and the chosen entry before applying it. Prefer `git stash apply` and drop the entry after verifying recovery. Stashes are local and can conflict when restored.

### Conflict resolution

Use `git status` to identify conflicted paths. Read both intended changes and their common context, resolve the resulting behavior, and stage the resolved paths. During rebase, the meaning of "ours" and "theirs" differs from the intuitive topic-branch perspective, so inspect content before choosing either side.

After resolving a rebase conflict, continue with `git rebase --continue`. For a merge, use `git merge --continue`. Repeat the relevant checks after integration. A conflict-free merge can still introduce a behavioral defect.

Use `git rebase --abort` or `git merge --abort` to abandon the corresponding operation. A clean starting state makes restoration more dependable. Skip a rebased commit only after verifying its change is already present or intentionally unnecessary.

### Rewriting a remote topic branch

Keep shared integration and release history stable. When a published topic rewrite is specifically authorized, fetch and inspect its remote tip before rewriting. Record that full commit ID, then use it as the expected value in the lease.

For the illustrative branch `docs/git-guidelines`, capture the tip before the rewrite:

```sh
git fetch origin
git rev-parse refs/remotes/origin/docs/git-guidelines
```

After the agreed rewrite, replace `EXPECTED_COMMIT` below with that recorded full ID:

```sh
git push --force-with-lease=refs/heads/docs/git-guidelines:EXPECTED_COMMIT origin HEAD:refs/heads/docs/git-guidelines
```

If the lease fails, inspect the new remote work and coordinate the next step. A bare `--force-with-lease` relies on remote-tracking refs that background fetches may advance. An explicit expectation protects against that ambiguity. A lease checks the remote value, not whether the rewritten history includes every necessary change.

## Prepare and integrate a pull request

Keep a pull request focused on one outcome. Open a draft when early feedback helps or checks remain incomplete. Give it a title describing the final behavior and a description that explains the problem, change, relevant validation, and material limits. Include migration, rollout, and rollback details when the change needs them.

Before the first push, inspect the destination and outgoing commits. For the illustrative branch:

```sh
git log --oneline origin/main..HEAD
git diff --check origin/main...HEAD
git push --dry-run origin HEAD:refs/heads/docs/git-guidelines
git push -u origin HEAD:refs/heads/docs/git-guidelines
```

A dry run checks the proposed push without updating remote refs. It does not prove that remote checks or hooks will accept the real update. Push only the intended branch. Publish tags separately when needed.

Use the repository's required merge method. Where none is established, default to squash merging a topic pull request into one coherent integration commit. Preserve individual commits with a merge commit or rebase merge when their structure, attribution, or release process matters. A squash merge creates a new commit, so do not assume the original topic tip is an ancestor of the target afterward.

Merge after the required reviews and checks pass for the revision being integrated. Follow protected-branch rules. Update the title and description when scope changes, and report checks that remain unavailable. After integration, verify the target contains the intended result before deleting the topic branch. Branch deletion and worktree removal are separate operations.

## Undo and recover work

Choose an operation based on where the change exists. Inspect the target diff or commit first and preserve work that must survive.

| Intended result | Operation | Effect and boundary |
| --- | --- | --- |
| Remove a path from the next commit while keeping edits | `git restore --staged -- path/to/file` | Restores its index entry from `HEAD` and keeps the working file. Assumes an existing commit. |
| Discard unstaged tracked edits to one path | `git restore -- path/to/file` | Replaces the working file from the index. Unstaged content is lost. |
| Reverse an ordinary published commit | `git revert COMMIT` | Creates a new inverse commit and preserves existing history. May conflict. |
| Find a previous local branch position | `git reflog` | Shows recorded local reference updates. Recovery depends on retained objects and logs. |
| Preview removal of untracked files and directories | `git clean -nd` | Lists candidates without deleting them. Adding `-x` would include ignored files. |

Revert from a clean working state and review the inverse change. Reverting a merge requires selecting the correct mainline parent with `-m` and understanding how that affects later merges. A revert does not reverse external effects such as a database migration or published package.

To rescue a commit found through the reflog, inspect it with `git show COMMIT`, then retain it with `git branch rescue/topic COMMIT` using an unused branch name. Reflogs are local, can expire, and do not back up arbitrary uncommitted or untracked content.

Use `git reset --hard`, forced branch replacement, and actual `git clean` deletion only for a known target and specifically authorized discard. Preview cleanup candidates with the same scope and ignore options as the proposed deletion. Git generally cannot recover untracked files deleted by cleanup. Preserve needed ignored files before removing a checkout.

## Manage repository content and releases

Track source, required configuration, documentation, and the dependency lockfiles expected by the project. Follow repository policy for generated output and large assets. Use an established large-file store when ordinary Git history would become impractical.

Keep credentials, tokens, local environment values, and private runtime data out of commits. Put shared ignore rules in `.gitignore`, personal repository exclusions in `.git/info/exclude`, and machine-wide exclusions in the user's global ignore configuration. Ignore rules do not stop tracking a file already in the index. Removing it from tracking requires a deliberate index change, and its old contents remain in history.

When a credential enters history, revoke or rotate it promptly and follow the project's incident process. Deleting the current file or reverting its commit does not remove the secret from earlier commits. Coordinate any history cleanup across clones, branches, tags, and hosting caches.

Respect `.gitattributes` for text normalization and file handling. Keep bulk line-ending changes separate from substantive edits so the behavioral diff remains reviewable. Avoid changing global Git configuration to complete a single repository task.

Use the project's release naming and version policy. Prefer annotated tags for releases and signed tags when required. Tag the verified release commit and push the specific tag deliberately. Treat published release tags as stable references. Correct a release with a new version rather than silently moving its tag.

## Coordinate concurrent work

Assign separate branches and worktrees to independent active tasks. In a shared checkout, coordinate staging, commits, and branch changes because all participants share the index and working files. Re-read affected files before editing when another contributor may have changed them.

Preserve another contributor's edits even when they are incomplete. Resolve overlapping ownership before changing those lines or publishing a combined commit. Avoid switching branches, stashing the whole checkout, resetting files, or cleaning directories merely to obtain a clean status.

Hand off the branch or commit, changed paths, checks actually run, outstanding work, and relevant local state. Distinguish committed work from pushed work and reviewed work from merged work. Report unrelated remaining changes as context when they affect the next contributor's actions.
