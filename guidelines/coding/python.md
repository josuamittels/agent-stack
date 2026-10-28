---
name: "python-best-practices"
description: "House standards for Python project structure, readability, typing, errors, testing, tooling, and review. Consult when creating or changing Python code."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Cursor"
  - "Affaan Mustafa"
  - "Python Software Foundation"
  - "Python Packaging Authority"
  - "pytest"
  - "Astral"
  - "Jesse Vincent"
type: "reference"
status: "experimental"
---

# Python best practices

Write Python whose behavior and boundaries are clear from its names, types, structure, and tests. Keep modules cohesive, validate external values when they enter the program, and make effects and failure behavior explicit. Follow the repository's supported Python versions, architecture, dependency manager, formatter, linter, type checker, and test runner first. These defaults apply where the repository leaves a choice.

## Contents

- [Code comments and docstrings](#code-comments-and-docstrings)
- [Project setup and tooling](#project-setup-and-tooling)
- [Project and module structure](#project-and-module-structure)
- [Names, formatting, and imports](#names-formatting-and-imports)
- [Types and data modeling](#types-and-data-modeling)
- [Functions, classes, and control flow](#functions-classes-and-control-flow)
- [Boundaries, errors, and resources](#boundaries-errors-and-resources)
- [Concurrency and performance](#concurrency-and-performance)
- [Tests and verification](#tests-and-verification)
- [Review checklist](#review-checklist)

## Code comments and docstrings

Do not put comments or docstrings in Python code. This applies to production modules, scripts, tests, examples, notebooks, and stubs. Do not add `#` comments, inline comments, type comments, `# noqa`, `# type: ignore`, formatter suppressions, TODO/FIXME/HACK markers, or docstrings. Remove such material in code you change instead of preserving or rewriting it. Markdown, API documentation, design notes, and change descriptions outside executable code are not covered by this ban.

Make the code explain itself. Use precise domain names, narrow functions, explicit types, clear exceptions, and tests that describe observable behavior. Keep complex algorithms understandable through small named steps and simple control flow. Put user and developer instructions in external documentation. If a static-analysis or formatter diagnostic appears to require an inline directive, fix the underlying design or configuration; isolate a verified interoperability issue at a boundary and record its rationale outside the code.

Where the repository can enforce this standard, enable a check in lint or CI that rejects source comments and docstrings, including tests and stubs. Ensure the check does not mistake `#` inside string literals, Markdown examples, or data fixtures for Python comments. Keep generated code under its generator's policy and report conflicts before modifying generated output.

## Project setup and tooling

Use the project's declared Python interpreter range. New projects should declare the minimum supported Python version and keep syntax, standard-library APIs, and dependency versions compatible with it. Prefer currently supported Python releases; do not imply a project supports every version that can parse its syntax.

For a new distributable package, use `pyproject.toml` for build-system and project metadata, with a maintained build backend. Keep runtime dependencies separate from development and optional dependencies. Pin or constrain dependencies according to the repository's reproducibility and release policy, and commit its lockfile when the selected manager expects one. Avoid maintaining the same metadata in several competing files.

Prefer a `src/` layout for a distributable package when import-shadowing risk or test/install fidelity matters:

```text
pyproject.toml
src/
  invoice_tool/
    __init__.py
    cli.py
    parsing.py
tests/
  test_parsing.py
```

A flat layout is reasonable for a small internal script, a simple application, or an established repository that already uses it. Choose the layout based on how the code is run and packaged; do not move a mature project just to match this example. Test packages through the same install path users receive when packaging behavior matters.

Use one project configuration as the source of truth for formatter, linter, type checker, test runner, and coverage settings where those tools support it. Use the installed toolchain and pinned versions in CI. Ruff is a suitable compact default for linting and formatting in a new project; Black, Flake8, isort, mypy, pyright, pytest, or unittest remain valid when they fit the project. Do not add a second tool that duplicates an existing check without a specific gap it closes.

Automate formatting, lint, type checking where configured, tests, and build or packaging checks in CI. Make local commands easy to discover in the project documentation or task runner. Run the narrowest relevant checks during development and the repository's full required suite before delivery. Do not claim an unavailable check passed.

## Project and module structure

Organize code around domain capabilities and reasons to change. Keep entrypoints and adapters for HTTP, CLI, files, databases, message queues, and third-party SDKs at the edges. Keep domain operations independent of those adapters where practical. A small project may keep this structure shallow; add folders only when they clarify ownership.

A service might use:

```text
src/
  billing/
    __init__.py
    domain.py
    service.py
    repository.py
  api/
    routes.py
  app.py
```

Here, `api.routes` translates transport input, `billing.service` coordinates a use case, and `billing.domain` owns domain rules. The repository adapter owns persistence. Let outer layers depend on inner domain code; avoid imports from domain modules back into frameworks or infrastructure. Avoid circular imports and imports that reach through another package's private implementation.

A module should have a focused purpose and a small public surface. Split it when it has unrelated responsibilities, independent reasons to change, or callers must understand unrelated behavior to use it. Keep cohesive types and functions together even if the file is not tiny. Prefer a direct function over a helper module, registry, or base class with one use. Add an abstraction when it names a stable concept, removes meaningful repetition, or isolates a volatile boundary.

Use `__init__.py` to define an intentional package API when needed. Do not re-export everything by default or create barrel modules that obscure where behavior lives. Keep internal names private by convention with a leading underscore; underscore naming is not a substitute for a clear package boundary.

Separate scripts from importable library code when both are present. Keep command-line argument parsing, environment reads, and process exit decisions in the entrypoint, then call ordinary functions that can be tested directly. Protect executable entrypoints with `if __name__ == "__main__":` when the file may also be imported.

## Names, formatting, and imports

Use PEP 8 naming: `snake_case` for modules, packages, functions, methods, and variables; `CapWords` for classes and exceptions; and `UPPER_SNAKE_CASE` for module constants. Use leading underscores for implementation details. Name values after their domain meaning or role, such as `invoice_total` or `retry_delay`, rather than generic labels like `data`, `value`, or `manager` when a useful name is available.

Use four spaces per indentation level. Let the project's formatter establish line wrapping, quotes, and whitespace. If no formatter exists, adopt a formatter and check its output instead of debating formatting in review. Follow PEP 8's import grouping: standard library, third-party packages, then local application imports, separated by blank lines. Import modules or specific names explicitly; avoid wildcard imports and import-time work.

Keep module-level code declarative. Define constants, types, and functions at import time, but do not open files, make network requests, parse large inputs, mutate global state, or start threads merely because a module is imported. Importing a module should be predictable and safe.

## Types and data modeling

Annotate public function parameters and return values, exported constants when inference is unclear, and internal boundaries where annotations make assumptions visible. Add local annotations when they prevent widening or make a non-obvious shape easier to understand. Let straightforward local values be inferred. Types support static analysis; Python does not enforce annotations at runtime.

Prefer built-in generics such as `list[str]`, `dict[str, int]`, and `str | None` when supported by the declared Python range. Use `collections.abc` types such as `Sequence`, `Mapping`, and `Iterable` for input contracts when callers need not provide a concrete mutable collection. Use `Any` only at an unavoidable untyped boundary, confine it there, and convert to a validated type immediately. Use `object` for opaque values, then narrow explicitly.

Represent data with the simplest structure that expresses its needs. Use a frozen dataclass for a value object with a fixed set of fields and behavior; a `TypedDict` for dictionary-shaped data with a known key contract; an enum for a closed set with meaningful named values; and a schema or parser for untrusted structured input. Use Pydantic or another validation library when the project already uses it or when its validation and serialization features justify the dependency. Do not create duplicate schemas that can drift from one source of truth.

Use a discriminated union or enum-backed state when several optional fields and booleans would permit contradictory combinations. Use `Protocol` when callers genuinely need structural substitution across implementations. Add generics when they preserve a relationship between input and output types. Avoid generic frameworks, deep inheritance, and elaborate type machinery that make a small operation harder to read.

Treat data from network responses, JSON, environment variables, CLI arguments, files, database drivers, IPC, and external libraries as untrusted until parsed. Validate once at the system boundary, then pass a named internal representation through the application. Do not repeatedly validate the same invariant in every layer or cast raw input to a type without checking it.

```python
def parse_port(value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("port must be an integer")
    if not 1 <= value <= 65_535:
        raise ValueError("port must be between 1 and 65535")
    return value
```

This parser accepts an opaque boundary value, checks the whole contract, and returns a value that downstream code can use as an `int`. It rejects `bool` explicitly because `bool` is a subclass of `int` in Python.

Use `None` only for meaningful absence. Avoid mutable default arguments; use `None` or a sentinel and create mutable values inside the function. Prefer immutable values for shared configuration and domain facts. If mutation is required, make ownership and mutation points clear.

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Invoice:
    subtotal_cents: int
    tax_cents: int

    @property
    def total_cents(self) -> int:
        return self.subtotal_cents + self.tax_cents
```

The frozen value object keeps its invariant simple, and the property names the domain operation without adding a service class for stateless arithmetic.

## Functions, classes, and control flow

Keep each function focused on a transformation, decision, or effect. Give it explicit inputs and a predictable return value. Use keyword-only parameters when a function has several options or when positional calls would be easy to misread. Positional parameters remain useful for short, obvious operations. Avoid boolean parameters that make call sites ambiguous; use named options or separate operations when behavior differs substantially.

Prefer a plain function for stateless behavior. Use a class when it owns state with a meaningful lifecycle, enforces an invariant across operations, or is required by an established framework. Do not turn a group of related functions into a class solely to collect them. Prefer composition over inheritance unless subtype behavior is a real part of the domain contract.

Use early returns for invalid or terminal cases when they make the normal path clear. Prefer explicit conditionals over nested conditional expressions, clever coercion, and side effects hidden inside comprehensions. Use comprehensions for simple construction or filtering; use a loop when it needs multiple decisions or would be harder to scan. Avoid mutable module-level state; pass dependencies or state through an object with a clear owner.

Use context managers for resources with cleanup requirements. Use `pathlib.Path` for filesystem paths and open files with an explicit encoding for text. Keep serialization format and timezone assumptions explicit. Avoid performing network, filesystem, database, or process effects deep inside a pure calculation.

## Boundaries, errors, and resources

Raise specific exceptions that describe the failure at the appropriate abstraction level. Define a custom exception when callers need to distinguish a domain failure or take a different action; otherwise use a suitable standard exception. Do not use exceptions for ordinary branching when a normal return type is clearer.

Catch only exceptions that the current layer can handle. Avoid bare `except` and broad catches that hide programming errors. When translating an error, preserve the cause with exception chaining. Do not silently discard failures. At a process, request, or job boundary, convert failures into actionable output and the correct status or retry behavior without exposing secrets or internal traces to end users.

```python
from pathlib import Path


class ConfigurationError(ValueError):
    pass


def read_configuration(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as error:
        raise ConfigurationError(f"cannot read configuration at {path}") from error
```

The boundary translates a filesystem failure into an actionable domain error while retaining the original cause for diagnostics.

Do not use `assert` to validate user or external input because optimized execution can remove assertions. Assertions are appropriate for internal invariants whose violation indicates a programming defect and is not part of normal input handling.

Use `with` or `async with` for files, locks, database transactions, and other managed resources. Close resources on both success and failure. Keep timeouts, cancellation, retries, and transaction boundaries explicit. Retry only failures that are transient and safe to repeat; use bounded attempts and backoff where retries could otherwise continue indefinitely.

Use environment variables or a configuration provider for deployment-specific settings. Parse and validate configuration once during startup, give missing or invalid settings clear errors, and avoid reading ambient process state throughout business logic. Never hard-code credentials or log secrets, personal data, or full sensitive payloads.

## Concurrency and performance

Choose concurrency based on the workload and the interfaces involved. Use synchronous code for ordinary sequential work. Use `asyncio` for high-concurrency I/O when the libraries and call chain support async; do not add `async` to CPU-bound work or mix blocking calls into an event loop. Use threads or processes only when their execution and shared-state costs are understood. Keep cancellation and task ownership explicit, and do not leave background tasks untracked.

Start with an algorithm and data structure suited to the expected input. Stream large inputs when practical instead of loading all data into memory. Avoid repeated work and unnecessary conversions, but do not sacrifice clarity for speculative micro-optimizations. Measure representative workloads before optimizing and retain a reproducible benchmark when performance is a requirement.

## Tests and verification

Test observable behavior, public contracts, and important boundary cases. Keep tests organized by feature or module, commonly under `tests/` with names such as `test_invoice_total.py`. Use the project's test runner; pytest is a reasonable default for new projects, while the standard-library `unittest` is appropriate when dependency constraints or existing conventions call for it.

Give tests descriptive names that state the behavior or condition. Cover normal outcomes, invalid inputs, missing values, boundary values, and meaningful failure paths. Use parametrization for related cases with the same assertion. Use fixtures for reusable setup and teardown, not as a hidden service locator or a way to obscure dependencies. Keep fixtures small and local in scope.

```python
def test_invoice_total_includes_tax() -> None:
    invoice = Invoice(subtotal_cents=1_250, tax_cents=100)

    assert invoice.total_cents == 1_350
```

This test checks the public result and stays independent of how the value object computes it.

Prefer tests that exercise real domain logic and parsers. Mock or fake true external boundaries such as network services, clocks, process execution, and expensive infrastructure. Avoid mocking internal functions just to follow the current call graph. Assert outcomes and externally visible effects rather than private call order unless order is part of the contract. Keep tests deterministic, independent, and explicit about temporary files, environment variables, and cleanup.

Add regression coverage for a defect when the change affects behavior and the repository workflow expects it. Use property-based tests for broad input spaces when invariants are clear and the added tooling is justified. Use integration tests where correctness depends on wiring, serialization, migrations, or an external protocol; keep unit tests fast enough for routine development.

For a change, run the repository's formatter check, linter, configured type checker, targeted tests, and any required packaging or integration checks. Expand verification when a change crosses boundaries or affects shared behavior. Report commands that could not run and the reason; do not imply unrun checks passed.

## Review checklist

- Does each module have a cohesive responsibility and a clear dependency direction?
- Are imports safe, and are runtime effects kept at explicit boundaries?
- Are external values validated before they become domain data?
- Do annotations clarify public contracts without spreading `Any` or unnecessary complexity?
- Are names, function signatures, and control flow clear without comments or docstrings?
- Are errors actionable, resources closed, and retries bounded?
- Do tests cover observable behavior, edge cases, and relevant failures without mirroring implementation details?
- Does the diff follow the repository's supported tools and conventions without inline comments, suppressions, or unrelated churn?
