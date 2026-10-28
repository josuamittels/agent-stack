---
name: "typescript-best-practices"
description: "House standards for TypeScript code structure, type safety, naming, errors, async work, tests, and review. Consult when creating or changing .ts or .tsx files."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Cursor"
  - "TypeScript"
  - "typescript-eslint"
  - "Peter Steinberger"
  - "Garry Tan"
type: "reference"
status: "experimental"
---

# TypeScript best practices

Write TypeScript so that behavior and legal states are clear from code, types, and tests. Keep modules cohesive, validate untrusted values once at system boundaries, and let precise types carry those guarantees through the program. Follow the repository's documented runtime, framework, formatter, linter, and module conventions first. These defaults apply where the repository leaves a choice.

## Contents

- [Code comments](#code-comments)
- [Project configuration and tooling](#project-configuration-and-tooling)
- [Structure and module boundaries](#structure-and-module-boundaries)
- [Types and data modeling](#types-and-data-modeling)
- [Functions, names, and control flow](#functions-names-and-control-flow)
- [Errors and asynchronous work](#errors-and-asynchronous-work)
- [Imports and public APIs](#imports-and-public-apis)
- [Tests and verification](#tests-and-verification)
- [Review checklist](#review-checklist)

## Code comments

Do not write comments in code. This is a strict rule for all authored or modified TypeScript and TSX: no `//`, `/* ... */`, JSDoc/TSDoc, TODO/FIXME/HACK markers, suppression directives, or explanatory comments in production code, tests, fixtures, and examples. Do not preserve a comment merely because it looks useful or warns future maintainers.

Make the code carry its explanation. Choose domain-specific names, express constraints in types, move complex behavior into a well-named function, validate at the boundary, and assert behavior in a test. If a compiler or linter diagnostic seems to require a suppression, change the design, narrow the value, or isolate a verified interop limitation in the smallest possible adapter. Never silence a diagnostic with an inline directive. If a requirement cannot be encoded in code or tests, raise it in external documentation or the change description rather than leaving an in-code comment.

Where the repository can enforce this rule, configure its linter or CI checks to reject comments in TypeScript and TSX. Remove comments in the changed scope instead of replacing them with different comment syntax or disabling the check.

## Project configuration and tooling

Use the project's pinned TypeScript version, package manager, runtime, build tool, formatter, linter, and test runner. Do not introduce a competing tool or replace a repository convention to satisfy personal preference. Make one formatting and import-order style consistent within the project.

For new projects, enable `strict` and keep strict null checking. Add targeted compiler checks such as `noImplicitReturns`, `noFallthroughCasesInSwitch`, `noUncheckedIndexedAccess`, or `exactOptionalPropertyTypes` when compatible with the runtime and codebase. Understand each option before enabling it; do not loosen strictness to make a new implementation compile. For a mature project, improve strictness in bounded areas and avoid broad unrelated churn.

Keep the TypeScript compiler as a correctness gate. Run the repository's typecheck, lint, format check, and relevant tests for changed code. Resolve diagnostics at their source; do not use `any`, assertions, suppression directives, or broad tsconfig exclusions to hide them. If a check is not available or cannot be run, report that precisely.

## Structure and module boundaries

Organize files around cohesive behavior and domain concepts, not around arbitrary line counts or a universal folder template. Keep related types, validation, and core operations close together. Split a module when it has multiple independent reasons to change, unrelated responsibilities, or an API that forces readers to load unrelated concepts. Keep a small cohesive module intact even if it contains both types and functions.

A useful application shape separates adapters from domain work:

```text
src/
  domain/
    order.ts
  boundaries/
    parse-order.ts
  adapters/
    http-orders.ts
  main.ts
```

Use the repository's architecture when one already exists. Keep framework, transport, filesystem, database, and process details at the edges. Put business rules in functions that accept domain values and return domain results. Avoid pass-through layers, generic helpers with one caller, speculative abstractions, and circular module dependencies.

Make dependencies flow in one direction: entrypoints and adapters call domain operations; domain code does not import the web framework, command-line parser, or storage adapter. A module should expose the smallest surface its callers need. Export intentionally; keep implementation details private. Avoid barrel files that obscure ownership or create cycles.

Use one obvious source of truth for each shape or invariant. Derive types from the authoritative schema, generated protocol, or existing domain model rather than duplicating fields across interfaces. Separate wire, persistence, and UI representations only when their semantics or lifecycles actually differ.

## Types and data modeling

### Prefer inference and precise types

Let TypeScript infer local variables and straightforward return types. Add annotations where they clarify a public contract, constrain an evolving value, document a complex callback boundary through its signature, or prevent undesirable widening. Prefer `satisfies` to a type assertion when checking a configuration object while retaining its literal types.

Use `unknown` for values whose shape is not known. Avoid `any`: it disables checking and spreads through dependent expressions. If a third-party API exposes `any`, contain it in a small adapter and return a type that has been validated. Do not use `any` as a shortcut for unfinished types.

Use `T | undefined` or `T | null` to represent real absence; do not use optional fields to disguise incomplete initialization. Prefer readonly inputs and immutable bindings when mutation is not required. Use `readonly` fields or collections for values that must not change after construction.

Use `type` for unions, intersections, aliases, and mapped or conditional types. Use `interface` for an object contract that is intentionally open to extension or declaration merging, or when the surrounding project consistently uses interfaces for object shapes. Do not define the same object contract twice with both forms. Prefer string literal unions for closed sets; use enums only when the runtime representation or an established project API requires one. Add generics when they preserve a real relationship between inputs and outputs, not to make a simple helper appear reusable.

### Model valid states

Prefer discriminated unions to a collection of optional properties and booleans that allow contradictory combinations. Use a consistent literal discriminator such as `kind` for each union. Handle every variant and make switches exhaustive.

```ts
type LoadState<T> =
  | { kind: "loading" }
  | { kind: "ready"; value: T }
  | { kind: "failed"; message: string };

function valueOrMessage<T>(state: LoadState<T>): T | string {
  switch (state.kind) {
    case "loading":
      return "Loading";
    case "ready":
      return state.value;
    case "failed":
      return state.message;
    default: {
      const exhaustive: never = state;
      return exhaustive;
    }
  }
}
```

Represent constraints constructively when doing so simplifies callers: non-empty tuples for guaranteed elements, branded identifiers for semantically distinct primitives, and discriminated result types for distinct outcomes. Validate a brand at the boundary once and create it only after validation. Do not strengthen every simple type reflexively; use the least restrictive type that lets operations remain total and clear.

Use utility types such as `Pick`, `Omit`, `Parameters`, `ReturnType`, `Awaited`, and `typeof` when they express a real dependency on an existing contract. Prefer a small named domain type when a utility-type expression becomes harder to understand than the duplicated shape.

### Parse untrusted data at boundaries

Treat network responses, JSON, IPC, environment variables, CLI input, file contents, database rows, and browser messages as `unknown` until parsed. Validate at the point of entry and convert to a named internal type. Use the validation library already established in the project and infer the TypeScript type from its schema where possible. Do not add a new schema dependency for one check.

```ts
import { z } from "zod";

const AccountSchema = z.object({
  id: z.string().uuid(),
  plan: z.enum(["free", "team"]),
});

type Account = z.infer<typeof AccountSchema>;

function parseAccount(input: unknown): Account {
  return AccountSchema.parse(input);
}
```

If no schema library exists, use a small parser or type guard that checks every property it claims to validate. A type guard must prove its predicate. Do not cast parsed JSON directly to a desired type. After a boundary returns a validated domain value, trust that type internally instead of repeating the same checks down the call chain.

### Avoid unchecked assertions

Avoid `as` assertions, non-null assertions (`!`), and double assertions. They tell the compiler to trust an unproven claim and often move a crash to runtime. Prefer control-flow narrowing, discriminants, schema parsing, a safer signature, or a representation that makes the invalid state impossible.

A narrow assertion may be used only when a third-party or platform type is demonstrably incomplete and the value has already been validated. Keep it at the interop boundary, explain the proof through the code's checks and local naming, and do not let the asserted type hide unvalidated input. Never use an assertion to convert raw external data into a domain object. Use `as const` only when literal preservation is necessary and `satisfies` cannot express the intended check.

## Functions, names, and control flow

Name files and exported types using the repository's established casing. If no file convention exists, use lowercase kebab-case file names that describe the module's primary responsibility. Use `PascalCase` for types and classes, `camelCase` for values and functions, and `UPPER_SNAKE_CASE` for module-level constants only when project style uses it. Prefer names that describe domain meaning or observable behavior. Avoid vague names such as `data`, `item`, `result`, and `manager` when a domain name is available; short names remain fine for obvious local scopes.

Keep functions focused on one decision or transformation. Make inputs and outputs explicit. Return values rather than mutating shared state when practical. Use object-shaped arguments when a function has several related parameters or multiple adjacent parameters of the same primitive type; positional arguments are fine when the operation is simple and order is unambiguous, or in a measured hot path. Prefer functions for stateless transformations. Use a class when an object owns meaningful state or a lifecycle, or when a framework or external API requires one; do not wrap a handful of related functions in a class without a state or lifecycle reason.

Prefer early returns for invalid or terminal cases when they make the main path easier to follow. Use `if` and `switch` for meaningful branching. Avoid nested ternaries, boolean flags whose meaning changes by call site, and clever coercions that hide behavior. Use `const` by default; use `let` only when reassignment is needed and keep the mutable scope narrow.

Do not add abstractions before a second real use or a demonstrated complexity reduction. A helper should give a concept a clear name, remove meaningful duplication, or isolate an external effect. Remove dead branches, unused exports, and compatibility paths without a current contract.

## Errors and asynchronous work

Represent expected alternatives in return types when they are part of normal domain flow, for example `{ kind: "ok", value } | { kind: "error", reason }`. Throw for exceptional failures when that matches the surrounding API. Do not use exceptions for routine branching or return ambiguous magic strings. Preserve useful error context when translating an error across a boundary.

Treat caught errors as `unknown`. Narrow with `instanceof Error` or a validated error shape before reading properties. Do not discard an error silently. Handle it, add appropriate context, or propagate it. User-facing and machine-facing errors should be actionable without leaking secrets or internal implementation details.

Use `async`/`await` for readable sequencing. Await promises that must finish; do not leave accidental floating promises. Use `Promise.all` for independent work and sequential awaits when ordering, shared state, or resource limits require it. Keep cancellation and deadlines explicit when a caller or external operation can outlive its usefulness.

Close or release resources in `finally` or a structured disposal pattern, including files, sockets, servers, locks, and temporary directories. Ensure all completion paths settle listeners and timers. Avoid mutable module-level state; where shared state is needed, give it one owner and an explicit lifecycle.

## Imports and public APIs

Follow the repository's module system and runtime resolution rules. Use ES module syntax in modern TypeScript unless the project requires another format. Make type-only imports explicit with `import type` when the configured compiler or lint rules support it. Use stable aliases or relative paths according to the project; do not invent a second import convention.

Avoid importing a deep implementation detail from another module when that detail is not part of its supported surface. Keep exported APIs small, typed, and intentional. Prefer named exports in libraries and multi-symbol modules; use default exports when a framework or repository convention expects them. Avoid re-export-only barrels that make dependency direction hard to see.

## Tests and verification

Test externally observable behavior and important boundary cases, not private implementation details. Prefer real parsers, data structures, and test framework utilities when they are inexpensive and reliable. Use fakes or mocks at true external boundaries; avoid mocks that merely restate the implementation.

Give each test a descriptive behavior name. Cover valid, invalid, missing, and variant cases for parsers and state transitions. Add regression coverage for a fixed bug when the repository workflow calls for it. Keep test helpers simpler than the code they support and do not bury important assertions in custom wrappers.

For a change, use the project's typecheck, lint, formatter check, and targeted tests. Run broader checks when the change crosses module boundaries or modifies shared behavior. Verify generated output through its owning tool rather than editing generated files directly. Report any check that could not be run; never claim a check passed without running it.

## Review checklist

- Does each module have one cohesive responsibility and a clear owner for state?
- Are untrusted values parsed at entry and represented by domain types afterward?
- Do the types make invalid states and mismatched identifiers difficult to express?
- Are all union variants handled and all assertions justified at a verified interop boundary?
- Are names, signatures, and control flow clear without comments?
- Are async work and resource cleanup correct on success, failure, and cancellation paths?
- Are tests focused on behavior, boundaries, and regressions?
- Does the diff follow the repository's tools and conventions without suppressions or unrelated churn?
