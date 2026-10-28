---
name: "versioning-best-practices"
description: "Versioning conventions for technical projects and standalone files. Consult when choosing initial versions, classifying changes, assigning lifecycle status, or preparing releases."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Tom Preston-Werner"
  - "npm"
  - "Keep a Changelog"
type: "reference"
status: "experimental"
---

# Versioning

Use `MAJOR.MINOR.PATCH` for released projects and independently maintained files. The number communicates compatibility. Record lifecycle status separately. The rules below apply SemVer to software and establish house conventions for documents and other files.

## Choose what receives a version

Version a unit that people adopt or release together, such as an application, package, schema, skill, or guideline. Files released only as part of an application inherit its version. Give a file its own version when readers use and update it independently. Independently released packages in one repository may have separate versions.

Define what consumers can rely on. For software, include supported APIs, commands, configuration, file formats, and runtime requirements. For a guideline or skill, include its required inputs, instructions, obligations, and outputs. A change is breaking when existing supported use requires adaptation.

## Start and increment

Use three non-negative integers without leading zeros. Count numerically, so `1.9.0` advances to `1.10.0`.

| Situation | Version |
| --- | --- |
| Empty scaffold or private placeholder | Optionally `0.0.0`. |
| First substantive development revision | `0.1.0`. Default for new standalone files. |
| First release with a supported compatibility contract | `1.0.0`. Start here directly if already ready. |

For versions from `1.0.0` onward:

| Change | Increment | Example |
| --- | --- | --- |
| Compatible correction | Patch | `1.4.2` → `1.4.3`. |
| Compatible addition or public API deprecation | Minor, reset patch | `1.4.2` → `1.5.0`. |
| Incompatible contract change | Major, reset minor and patch | `1.4.2` → `2.0.0`. |

Choose the largest required increment across the release. Judge consumer impact, rather than lines changed or effort. A one-line removal can be breaking. A large internal rewrite can preserve compatibility.

| Example | Classification |
| --- | --- |
| Correct a typo, repair an example without changing its rule, or fix behavior to match its documented contract | Patch. |
| Add an optional flag, backward-compatible operation, or optional workflow | Minor. |
| Rename a required field, remove a command, raise the minimum supported runtime, or make an optional review mandatory | Major. |
| Update a dependency or fix a security issue | Classify the resulting consumer impact. The dependency's own increment does not determine yours. |

For documents, these classifications are house policy. A clarification that changes what readers must do is a contract change, even if described as a correction.

During `0.y.z`, SemVer provides no stable compatibility promise. Our convention uses patch for compatible corrections and minor for additions or breaking changes, such as `0.3.2` → `0.4.0`. Explicitly identify breaking changes. Move to `1.0.0` once consumers should be able to rely on compatibility. Do not wait for feature completeness or a bug-free product.

## Record lifecycle status

These metadata labels are house definitions. Apply them to the specific artifact or release they describe.

| Status | Meaning and typical version |
| --- | --- |
| `draft` | In preparation or review. Usually `0.1.0` initially. Do not treat it as an approved standard. |
| `experimental` | Usable for trials. Design or behavior may change substantially. Usually `0.y.z` or a prerelease. |
| `stable` | Reviewed and supported for its stated use, with an explicit compatibility contract. Use `1.0.0` or later for new stable artifacts. |
| `deprecated` | Discouraged for new adoption. Identify the replacement and support or removal plan. Preserve its version history. |

Status changes require an explicit decision. A version number does not grant approval or certify quality. An older major release can remain stable while its successor is experimental. Retain existing version and status combinations until a deliberate migration.

Use optional prerelease suffixes for previews of a target release:

`1.0.0-alpha.1` → `1.0.0-beta.1` → `1.0.0-rc.1` → `1.0.0`

Our meanings are early trial, broader testing, and release candidate. A prerelease sorts below its matching final version. Optional build metadata such as `1.0.0+sha.a1b2c3` does not affect ordering. If a file requires exactly three numeric components, keep status in metadata instead.

## Identify and release revisions

Keep one authoritative version field, such as the package manifest or file frontmatter. Derive duplicate release labels from it. Keep tracked filenames stable, such as `reference.md`. Include the version in distributed exports when useful, such as `schema-1.2.0.json`. A tag may use `v1.2.0`, while the version field contains `1.2.0`.

Group working edits into a release or adopted file revision. Saves and commits need no individual version bump. Update the file's `updated` date when editing it. Reserve the version change for the revision being adopted or distributed.

Before release, compare against the previous released contract, verify affected behavior or examples, synchronize version labels, and record notable changes with a `YYYY-MM-DD` date. Include migration instructions for breaking changes. Keep pending notes under `Unreleased`.

Published version contents are immutable. Correct mistakes with a new release. Identify a withdrawn release and its replacement rather than reusing its number. For an individual file, preserve the previous revision in version control and publish the correction under its next version.
