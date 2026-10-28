---
name: "technical-documentation"
description: "Standards for structuring, writing, verifying, and maintaining technical documentation for applications and software projects. Consult when assessing a repository, selecting documentation components, or creating and improving project docs."
version: "0.1.0"
created: "2026-10-24"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Divio"
  - "Daniele Procida"
  - "Google"
  - "Eric Holscher and the Write the Docs community"
  - "GitHub"
  - "Peter Hruschka"
  - "Gernot Starke"
type: "reference"
status: "experimental"
---

# Technical documentation

Good documentation helps a particular reader learn, complete a task, look up a dependable fact, or understand a system. Organize it around those needs. A repository's directory tree is evidence about the software, but it is rarely a useful outline for the entire documentation set.

Use this reference for applications, services, libraries, command-line tools, and their supporting projects. It defines content and quality conventions for people and repository-to-documentation tools. It does not prescribe a documentation framework, hosting provider, or execution workflow for an authoring skill.

Default to the smallest documentation set that supports the project's real readers and important tasks. Preserve useful existing content, stable links, and working tooling. Expand when a reader need justifies it.

## Contents

- [Identify readers and outcomes](#identify-readers-and-outcomes)
- [Ground documentation in evidence](#ground-documentation-in-evidence)
- [Separate the four documentation modes](#separate-the-four-documentation-modes)
- [Structure the documentation set](#structure-the-documentation-set)
- [Choose components for the project](#choose-components-for-the-project)
- [Compose pages from useful elements](#compose-pages-from-useful-elements)
- [Write dependable instructions and examples](#write-dependable-instructions-and-examples)
- [Combine generated and authored documentation](#combine-generated-and-authored-documentation)
- [Maintain documentation with the product](#maintain-documentation-with-the-product)
- [Decide whether the documentation is ready](#decide-whether-the-documentation-is-ready)

## Identify readers and outcomes

Name the primary reader, their starting knowledge, and what they need to accomplish before choosing pages. One person may need different modes at different times. An experienced developer learning an unfamiliar library still needs a tutorial.

| Reader | Typical needs | Avoid assuming |
| --- | --- | --- |
| App user | Access the app, perform core tasks, understand permissions, recover from errors. | They can clone a repository or run a terminal. |
| Integrator | Authenticate, make an initial request, use contracts correctly, handle failures. | They understand the internal architecture. |
| Contributor | Run locally, test, locate relevant code, follow contribution rules. | Existing team knowledge or a preconfigured laptop. |
| Operator or administrator | Configure, deploy, observe, upgrade, recover, and manage access. | A development server is suitable for production. |
| Maintainer | Understand boundaries, compatibility, design decisions, and release responsibilities. | The current code reveals why a decision was made. |

Express coverage as reader outcomes, such as "A contributor can start the app with local test data" or "An administrator can restore a backup and confirm the restored records." File counts and documented-symbol counts do not establish that coverage.

Separate public product documentation from internal operational material when access differs. A public guide must not depend on private instructions for an essential step without explaining the access requirement. Internal documentation still needs clear navigation and verified procedures.

For an unfamiliar repository, distinguish observed audiences from inferred audiences. A command-line entry point establishes a tool interface. It does not establish its intended customers, support commitments, or commercial positioning.

## Ground documentation in evidence

Describe the system at an identifiable revision or release. Inspect the evidence relevant to the intended pages, including existing docs, manifests and lockfiles, entry points, public interfaces, configuration loaders, tests, build scripts, deployment definitions, and release records. Inspect representative behavior deeply enough to explain the main reader journey. Avoid turning every file into a page.

Use evidence according to what it can establish.

| Evidence | Useful for | Limit |
| --- | --- | --- |
| Implementation and configuration loaders | Current behavior, defaults, precedence, validation, interfaces. | May contain defects or unfinished paths. |
| Schemas and declared public contracts | Expected input/output shapes and supported interfaces. | May disagree with runtime behavior. |
| Tests and reproducible execution | Checked scenarios, observable results, example validation. | Establish only the scenarios and environment actually checked. |
| Manifests, scripts, and CI definitions | Toolchain choices, available commands, build and test workflow. | Declared steps may fail or require unavailable services. |
| Infrastructure and deployment definitions | Intended infrastructure and configured deployment steps. | Do not prove what is currently deployed or operational. |
| Existing docs and accepted decision records | Terminology, intent, rationale, compatibility promises. | Can be stale. Compare with the described revision. |

When sources disagree, investigate rather than choosing whichever is easiest to quote. A test can encode an obsolete expectation. An implementation can violate a public contract. Describe observed behavior and the discrepancy explicitly when unresolved. Do not silently convert a bug into a supported guarantee.

Keep a lightweight authoring record that maps consequential claims to repository paths, symbols, schemas, or checks. Record the target revision and material verification limits. Reader-facing pages need source links only where they help readers inspect or maintain the subject. Keep process logs out of the published prose.

Do not infer production readiness from a deployment file, security guarantees from an authentication dependency, or platform support from a package's transitive dependencies. Do not invent rate limits, service-level commitments, license terms, recovery guarantees, product plans, or historical rationale.

If evidence is missing, omit an optional claim or identify the precise gap. For a required task, state what remains unverified and what evidence or access would resolve it. Avoid filling a public guide with speculative TODOs. Track unfinished authoring work separately unless the limitation itself matters to users.

## Separate the four documentation modes

Give each page one dominant purpose. Choose its mode from the reader's immediate need, then use the corresponding structure. A short definition or warning can support a procedure without turning it into a mixed-purpose manual. Move substantial secondary material to its own page and link to it.

| Mode | Reader's question | Purpose | Example title |
| --- | --- | --- | --- |
| Tutorial | "Help me learn by doing." | Build practical familiarity through a guided experience. | Build your first report |
| How-to guide | "How do I achieve this result?" | Complete a real task from a defined starting point. | Export a report as CSV |
| Reference | "What exactly does this accept or do?" | Find precise facts about an interface or behavior. | Export API |
| Explanation | "Why does it work this way?" | Develop understanding of a bounded subject. | How report snapshots preserve consistency |

Tutorials and how-to guides both contain actions. The distinction is whether the author chooses a learning experience or the reader brings a task. Reference and explanation both communicate knowledge. Reference supplies facts needed during work. Explanation connects ideas and reasons.

### Tutorials

Choose a small, meaningful project with one supported path and an observable result. State the required knowledge, environment, and access. Make choices for the learner so they can concentrate on the new skill.

Use this page order by default:

1. Outcome and a concrete picture of what the learner will make.
2. Prerequisites and starting state.
3. Guided actions with visible checkpoints.
4. Final verification and cleanup when resources were created.
5. A brief recap and links for independent work or deeper understanding.

Introduce concepts when the learner encounters them. Keep explanations short enough to preserve momentum. Avoid branching into every provider, configuration option, or implementation detail. Repeat the experience from a clean starting state before describing it as tested.

A quickstart for an experienced integrator may instead be a short how-to. Label it by what it actually provides. Installation alone is not necessarily a meaningful first success.

### How-to guides

Name a specific outcome and the assumed starting point. Include the decisions needed to adapt the procedure to the reader's situation. Keep background discussions elsewhere.

Use this page order by default:

1. Goal, applicability, and constraints.
2. Prerequisites, permissions, and required inputs.
3. Ordered actions, with conditional branches where they affect the task.
4. Verification of the resulting state.
5. Relevant recovery, cleanup, or next action.

Use titles such as "Rotate an API token" or "Restore a backup." Distinct environments can have separate sections or pages when their procedures materially differ. Give one recommended path when alternatives add no useful choice.

### Reference

Organize reference around the interface readers use, such as commands, resources, configuration keys, events, or public modules. Match the system's terminology and grouping. Do not mirror private folders merely because they exist.

Use a consistent entry structure across comparable items. Start with the name and purpose, then exact syntax or shape, inputs, outputs, behavior, constraints, and relevant errors. Include a compact example when it clarifies usage. Document all supported items within the declared scope. Explicitly separate experimental and internal interfaces.

A reference should let someone find a default, return value, or error condition without reading a tutorial. Links can connect an entry to a task guide or explanation.

### Explanation

Choose a bounded question, such as consistency, authorization, synchronization, or deployment topology. Establish the context, introduce the mental model, connect its parts, and explain consequences and tradeoffs. Include alternatives or history when evidence exists and they clarify the current design.

Use diagrams and examples to make relationships concrete. Keep executable procedures and exhaustive option lists in their own modes. Separate an observed mechanism from a documented reason for choosing it. If no decision record exists, describe how the mechanism works without inventing the team's intent.

### Resolve mixed material

An "Authentication" page can contain four different reader needs. Split it when those needs obstruct each other:

| Material | Home |
| --- | --- |
| Create a test account and make a first authenticated request. | Tutorial |
| Rotate credentials for an existing integration. | How-to guide |
| Header format, token lifetime, permission scopes, and error responses. | Reference |
| Trust boundaries and reasons for the authorization model. | Explanation |

Keep an essential limitation beside the affected fact or action even if it appears elsewhere. Separation must not make a reader follow several links to discover a prerequisite.

## Structure the documentation set

Separate three decisions. Content mode determines how a page works. Navigation determines how readers find it. Storage determines where maintainers edit it. These decisions can align without having identical hierarchies.

### Entry points and navigation

Use the repository README as a compact entry point. Default to this order, omitting inapplicable sections:

1. Project name and a concrete description of its purpose and audience.
2. Relevant status, compatibility, or access limitations.
3. The shortest supported path to a first useful result, or a prominent link to it.
4. Links to task guides, reference, and conceptual documentation.
5. Contribution, help, security-reporting, and license links when established.

Avoid repeating the full manual in the README. A package README can provide package-specific context and link to shared guidance.

A documentation landing page should help readers choose a route. State what the docs cover, show the main audience or task entry points, and expose the major content groups. An index that only repeats directory names adds little value.

Default navigation order is orientation, first success, common tasks, reference, and explanation. Place troubleshooting and upgrade help where affected readers can find them quickly. This is a navigation convention, not a requirement to read the site in sequence.

Use four visible mode groups when they help readers. For a product with distinct audiences, groups such as "Use the app," "Develop integrations," and "Operate the service" may be clearer. Keep the page modes distinct within those groups. Avoid duplicating the same page under each audience.

### File organization

Default to plain Markdown in an existing docs directory when no documentation stack exists. Preserve an established format or generator when it works. Add a site generator only when publishing, navigation, search, versioning, or interactive examples justify its maintenance cost.

The following tree illustrates a growing service with developer and operator needs. It is not a scaffold to create in every repository. Every named page must earn its place through useful content.

```text
README.md
CONTRIBUTING.md
CHANGELOG.md
docs/
  index.md
  tutorials/
    first-report.md
  how-to/
    run-locally.md
    export-report.md
    deploy-service.md
    restore-backup.md
  reference/
    api.md
    configuration.md
    errors.md
  explanation/
    architecture.md
    report-consistency.md
    decisions/
      0001-snapshot-storage.md
```

For a small tool, a README and a few linked pages can be enough. Do not create empty mode directories, placeholder landing pages, or unneeded policy files. A repository with extensive existing docs generally benefits from incremental repairs rather than a wholesale rearrangement.

For a monorepo, document shared concepts and workflows centrally. Put independently versioned interfaces and package-specific setup near their owning package or in clearly scoped site sections. State the working directory for commands and link package docs from the central entry point.

Use stable, descriptive, lowercase hyphenated slugs unless the project has another established convention. Preserve established URLs. When a page moves, update incoming links and use redirects where the publishing system supports them.

### Reading order and authoring order

Reading order follows the task. A newcomer needs an initial success path. An operator handling a failure needs recovery instructions immediately. A reference reader may arrive directly from search and needs local context.

Authoring order follows evidence and risk. Establish the supported setup and interfaces, verify a representative path, then complete the surrounding guidance. Default priorities for a new documentation set are:

1. Correct misleading instructions and missing prerequisites that block use or risk data loss.
2. Provide orientation and one meaningful first-success path for the primary reader.
3. Cover frequent or consequential tasks and the reference facts they depend on.
4. Explain the concepts needed to adapt, operate, or maintain the system.
5. Expand from observed gaps, support questions, and product changes.

Drafting reference facts early can prevent procedural mistakes. It does not mean publishing a reference-only manual and deferring every other reader need. These priorities guide bounded work, not a requirement to plan every future page before improving one.

## Choose components for the project

Use the following inventory to choose coverage. Components are subjects, not additional documentation modes. Each may require several modes, and a small project may cover a component in a single focused section.

| Component | Include when | Essential coverage |
| --- | --- | --- |
| Overview and access | A reader needs to identify or start using the project. | Purpose, audience, scope, access route, supported status, first-success link. |
| User workflows | People use an application interface. | Core outcomes, exact UI labels, permissions, saved state, validation, error recovery. |
| Installation and compatibility | Readers install software or an SDK. | Supported versions/platforms, prerequisites, install and verification, update/removal where relevant. |
| Local development | Contributors or self-hosters run the source. | Toolchain, package manager, dependency setup, environment, services, seed data, start/stop, test/build commands. |
| Configuration | Runtime behavior is configurable. | Keys, types, defaults, required conditions, sources, precedence, validation, reload/restart behavior. |
| API, SDK, CLI, or event contracts | Consumers integrate with a public interface. | Entry points, authentication, shapes, semantics, errors, limits, compatibility, examples. |
| Architecture and domain model | Readers must understand interactions or make changes safely. | System boundary, responsibilities, important flows, data ownership, external dependencies, constraints. |
| Deployment | Readers operate a supported deployment. | Environment assumptions, build artifacts, services, configuration, health verification, rollback limits. |
| Operations and recovery | The system has ongoing operational responsibilities. | Signals, diagnostics, routine tasks, backup/restore, failure recovery, escalation if established. |
| Data lifecycle | Data persists, moves, or is transformed. | Schema, migrations, import/export, compatibility, retention/deletion behavior, recovery implications. |
| Security and access | Readers configure access or handle sensitive data. | Roles, permission boundaries, credential handling, relevant limitations, established reporting route. |
| Troubleshooting | Failures require reader action. | Recognizable symptom, diagnostic evidence, likely causes, safe resolution, verification, escalation. |
| Upgrades and migrations | Existing installations or integrations must change. | Affected versions, breaking behavior, preparation, migration, verification, recovery constraints. |
| Contribution and maintenance | Others change or release the project. | Change workflow, relevant checks, review conventions, release process, documentation ownership. |
| Change history and glossary | Changes or domain terms need a durable lookup. | Curated user impact and upgrade links; definitions of genuinely unfamiliar terms. |

A hosted app's users may need sign-in instructions while its contributors need local setup. A native app may need device permissions, supported OS versions, signing requirements for contributors, and distribution-specific behavior. A library usually needs integration examples and public API reference. Do not force deployment and operations pages onto a library with no hosted component.

### Reference contracts

Use the fields relevant to each interface. Explicitly distinguish an omitted value from an empty or null value when behavior differs.

| Interface | Fields to cover |
| --- | --- |
| Configuration | Name, purpose, type, valid values, default or absence behavior, required condition, source/precedence, sensitivity, application timing. |
| HTTP API | Method/path, authorization, parameters/body, success response, error responses, pagination, ordering, idempotency, retry behavior, documented limits. |
| SDK or library | Import, signature, inputs/defaults, return type, exceptions, synchronous/asynchronous behavior, side effects, usage example. |
| CLI | Invocation, subcommands, arguments/options, defaults, environment, working directory, output channels/formats, exit codes, side effects. |
| Event or webhook | Name, schema/version, trigger, delivery/authentication, ordering, duplicates, retry and acknowledgement behavior. |

Include an item only if it exists, and identify important unsupported behavior. Do not invent a retry or delivery guarantee because it would be conventional. Generated signatures often need authored descriptions of semantics and constraints.

### Architecture and operations

Start architecture explanations with the system boundary and its external dependencies. Introduce major responsibilities before internal modules. Use a runtime example to show how a request, job, or event moves through the system. Show deployment boundaries when they differ from code boundaries. Document meaningful decisions, constraints, and known risks at the depth maintainers need.

An architecture decision record should identify its status, context, decision, and consequences. Link supporting evidence and superseding decisions when applicable. Preserve history rather than rewriting an old decision to pretend the new design was always intended.

Operational procedures need the environment, permission level, trigger, diagnostic checks, actions, completion condition, and relevant recovery limits. Distinguish a process health check from proof that the service completes its business function. A backup procedure alone does not establish that restoration works.

### Troubleshooting and upgrades

Organize troubleshooting by symptoms readers can recognize. Give the exact error text or code when stable, a diagnostic check, a supported cause, a resolution, and a way to verify recovery. Distinguish a hypothesis from a confirmed cause. Use an FAQ only for actual recurring questions, and move substantial answers into their proper pages.

An upgrade guide states source and target versions, affected readers, compatibility changes, preparation, ordered migration actions, verification, and rollback or recovery limits. If a migration is irreversible, say so before it begins. Keep release notes focused on what changed and link to the procedure.

## Compose pages from useful elements

Use elements that help readers act or understand. Do not require every page to contain every element.

| Element | Convention |
| --- | --- |
| Title | Identify the task, interface, or bounded concept. Use sentence case and the reader's terminology. |
| Opening | State the useful outcome or subject immediately. Add audience, scope, and applicability where they change interpretation. |
| Prerequisites | State necessary knowledge, tools, versions, permissions, accounts, data, and starting state before dependent actions. |
| Headings | Use one main heading and a logical hierarchy. Use verbs for tasks and noun phrases for reference or concepts. |
| Steps | Use numbered actions when order matters. Give each step one principal action and a relevant checkpoint. |
| Code and output | Name language and execution context. Separate input from expected output. Declare incomplete snippets. |
| Tables | Compare repeated fields or alternatives. Avoid wide tables filled with multi-paragraph procedures. |
| Notices | Highlight a relevant exception or risk sparingly. Keep required steps and prerequisites in the main flow. |
| Diagrams and screenshots | Clarify relationships or a difficult UI location. Include text equivalents and enough context to interpret them. |
| Verification | Describe the observable state that establishes success, beyond a command merely exiting. |
| Related links | Offer a useful next task, lookup, or explanation. Avoid an undifferentiated list of every nearby page. |
| Metadata | Use the project's existing fields for title, description, version applicability, owner, or review state when needed. |

A page should work when opened directly. Identify which product, package, version, environment, or role it concerns where ambiguity is possible. Do not rely on "the previous page" for an essential starting condition. Link the prerequisite by name.

Make link text describe its destination or purpose. Prefer repository-relative links for repository-local documents, and use the publishing system's supported link conventions for a site. Check the rendered target because a filesystem-valid link may still produce the wrong site URL.

Use a contents list on long pages when it improves navigation and the renderer does not already provide an effective equivalent. Split a page when its reader purpose changes or independent lookup becomes difficult. Word count alone is not a reason to split.

## Write dependable instructions and examples

State the location and conditions for an action before the action itself. Use imperative verbs, exact identifiers, and stable terminology. Mark optional steps explicitly. Put a risk and its consequence before the affected operation.

Avoid "just," "simply," and unsupported duration estimates. Do not send readers through unexplained setup commands. Explain an unfamiliar concept briefly when required, then link to its full explanation.

### Commands and code

Show the working directory, shell or execution environment, and required runtime where they affect the result. Use the package manager and version policy supported by the project. Do not offer interchangeable install commands unless they have been checked and are supported.

Use fenced code blocks with a language identifier. Keep runnable input free of prompt characters and output. Explain placeholders beside the example and make their boundaries clear. Follow the source language and project formatting, preserving meaningful indentation.

Make copied examples complete for their declared context. Include imports, configuration, authentication acquisition instructions, or surrounding code when required. If the snippet is partial, say where it belongs and mark omissions with language-appropriate comments. Do not present an abbreviated snippet as a complete runnable program.

Use synthetic data and nonfunctional credentials. Never publish real tokens, private hostnames, personal data, or sensitive logs. Mark a local-only shortcut clearly and explain the production requirement when known. Do not run destructive examples against a real environment merely to verify documentation.

Prefer examples stored in executable sample files or checked fixtures when the project can maintain them. Keep examples deterministic where practical. Label output as representative when IDs, timing, or other values vary.

The following fictional example illustrates a configuration entry. It does not describe this repository or establish a universal key name or default.

```markdown
### REPORT_TIMEOUT_MS

Maximum duration of a report request, in milliseconds.

| Property | Value |
| --- | --- |
| Type | Integer |
| Default when unset | `30000` |
| Valid values | `1000` through `120000`, inclusive |
| Source | Server process environment |
| Application timing | Process startup. Restart after changing the value. |

An invalid value prevents startup and reports a configuration error.
```

A real entry must derive the range, default, and validation behavior from the described implementation. An example becomes misleading when conventional-looking values are substituted for evidence.

### Visuals and accessibility

Use a diagram to clarify boundaries, relationships, sequences, or state changes that are harder to follow in prose. Label connections, define unfamiliar symbols, and distinguish logical structure from actual deployment. Prefer editable diagram sources when the repository supports them. Avoid generating large diagrams of every file.

Screenshots should show the relevant UI and identify the applicable version when it matters. Crop irrelevant material and remove sensitive data. Keep instructions in text so they remain searchable and usable when the image is unavailable.

Provide meaningful text alternatives and a prose description of essential diagram relationships. Do not encode meaning in color alone. Use accessible headings, descriptive links, readable tables, and keyboard-accessible controls. Avoid hiding required instructions in tabs or collapsed sections without a clear label. Check that copying a tab's code produces the complete intended example.

## Combine generated and authored documentation

Generate facts that have a reliable machine-readable source, such as signatures, schema fields, or command options. Author the context, task guidance, semantics, and tradeoffs that those sources do not supply.

Declare the source of truth for each generated artifact. Document the generation command, inputs, required tool version or lockfile, output location, and review expectations. Mark generated files so contributors know where to edit. Do not overwrite maintained prose during regeneration.

Keep one canonical home for each fact. Link to shared reference from procedures. Where a task needs a short repeated value or warning, keep the duplication deliberate and verifiable. Avoid copying the entire configuration table into multiple guides.

Generated coverage must match the public interface and intended audience. Exclude private symbols, secret defaults, internal-only endpoints, and accidental implementation details. A successful generator run does not establish semantic correctness or useful task coverage.

A repository-to-docs tool should preserve established custom sections and clearly distinguish proposed content, verified facts, and unresolved gaps. It should not change application behavior, install a docs stack, publish a site, or create support policies merely to make the documentation appear complete.

## Maintain documentation with the product

Keep docs in version control when the project supports it, review them with behavior changes, and assign ownership through existing contribution conventions. Prefer a reviewable diff over opaque regenerated output.

Update affected documentation when commands, defaults, permissions, schemas, workflows, or compatibility change. Choose checks that catch the likely drift, such as comparing generated reference, validating configuration samples, or exercising the documented setup path.

Distinguish docs for a released version from docs for an unreleased branch. State the version a page applies to when readers could otherwise combine incompatible instructions. Add versioned documentation when multiple supported releases materially differ. Avoid maintaining identical copies for every patch release.

For a continuously deployed service, describe the current supported behavior and identify feature availability constraints. A date alone cannot prove that the page matches a deployment. Review timestamps should record a real review rather than refresh automatically on every build.

Retain relevant historical migration paths and redirect retired URLs when possible. Mark deprecated interfaces with a replacement and known removal timing. Do not invent a deadline when none is established.

Use support questions, failed searches, issue reports, and task observations to identify the next useful improvement. Preserve useful docs through incremental changes. A documentation set can be appropriate for its current stage while still having a backlog.

## Decide whether the documentation is ready

Judge readiness against the chosen readers and outcomes. Use complementary checks and record what actually ran.

| Check | What to establish | What passing does not prove |
| --- | --- | --- |
| Structure and rendering | Docs build or render, navigation works, links and anchors resolve, assets load, code blocks are readable. | Commands work or explanations are accurate. |
| Interface agreement | Documented names, shapes, defaults, errors, and version scope agree with implementation and supported contracts. | Every possible runtime condition is covered. |
| Task execution | A representative reader path works from its stated prerequisites in an identified test environment. | All platforms and production environments behave identically. |
| Reader usability | A reader with the assumed knowledge can find the right page and recognize task completion. | All target readers succeed without assistance. |
| Maintenance | Canonical sources, generated boundaries, owners, and update triggers are clear enough to maintain the result. | The docs will remain current without future work. |

Before calling a documentation set complete for its scope, confirm these conditions:

- The primary audiences and important outcomes have useful entry points.
- Learning, task completion, lookup, and understanding are covered where needed, without empty framework sections.
- Each page has a clear purpose, applicability, and meaningful place in navigation.
- Procedures include their starting conditions, required permissions, relevant risks, and observable completion state.
- Consequential behavior claims are supported, and unresolved conflicts are visible to the author or affected reader.
- Examples match the declared version and context, and sensitive information is absent.
- Canonical information is discoverable without conflicting copies.
- Relevant verification has run, or its precise limits are reported.

When execution requires unavailable credentials, services, platforms, or destructive actions, use the strongest safe check available and state the untested boundary. Report "commands checked against scripts; end-to-end setup not run" when that is the evidence. Do not replace it with "verified documentation."

A documentation build and an internal read-through are useful checks. Neither establishes that an unfamiliar reader succeeds. If no reader validation occurred, keep that limitation explicit without blocking useful, accurately scoped improvements.
