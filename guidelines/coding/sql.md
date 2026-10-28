---
name: "sql-best-practices"
description: "House standards for SQL structure, naming, correctness, security, schema design, performance, and migrations. Consult when writing or reviewing SQL source, embedded queries, schemas, indexes, or migrations."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Lauren Tan"
  - "Cursor"
  - "Supabase"
  - "Everything Claude Code"
type: "reference"
status: "experimental"
---

# SQL best practices

Write SQL so its data flow, assumptions, and effects are visible from the statement itself. Use explicit columns, named constraints, safe parameters, and measured query plans. Encode durable invariants in the schema. Keep each statement small enough to review, and follow the repository's engine, version, migration runner, formatter, and existing conventions wherever they define behavior.

These standards apply to SQL files, queries embedded in application code, migrations, schema definitions, stored routines, tests, and SQL examples. SQL dialects differ. Identify the actual engine and supported version before using engine-specific syntax or relying on operational behavior. Treat examples here as structural patterns; substitute the target engine's valid types and syntax.

## Contents

- [Code comments](#code-comments)
- [Project and dialect conventions](#project-and-dialect-conventions)
- [Formatting and statement structure](#formatting-and-statement-structure)
- [Names and aliases](#names-and-aliases)
- [Query composition](#query-composition)
- [Correctness and result shape](#correctness-and-result-shape)
- [Schema and data modeling](#schema-and-data-modeling)
- [Security and access control](#security-and-access-control)
- [Transactions and concurrency](#transactions-and-concurrency)
- [Indexes and performance](#indexes-and-performance)
- [Migrations and schema evolution](#migrations-and-schema-evolution)
- [Verification and review](#verification-and-review)

## Code comments

Do not write comments in SQL code. This is a strict rule for authored or modified SQL source, including standalone SQL files, embedded SQL, migrations, routines, tests, fixtures, and examples. Do not add line comments, block comments, end-of-line comments, commented-out statements, comment-based directives, or database object descriptions such as `COMMENT ON TABLE` and `COMMENT ON COLUMN`. Do not preserve an existing comment in a changed SQL scope because it looks useful or warns future maintainers.

Make SQL carry its own explanation. Choose specific names, separate distinct operations into named statements or CTEs, express rules as constraints, and make predicates and joins explicit. Put durable design rationale in external schema documentation, a design record, or the migration description. Put temporary rationale in the change description. If a comment claims a correctness or safety constraint, encode that constraint in the schema, query, test, or deployment check and remove the comment.

Do not replace comments with opaque naming, redundant CTEs, or artificial SQL constructs. If the behavior remains surprising after a reasonable structural rewrite, put the explanation outside the SQL source and link to it from the surrounding project documentation where the repository supports that practice.

## Project and dialect conventions

Use the SQL engine, version, migration tool, query builder, and lint or formatting setup already selected by the repository. Do not introduce a second style or formatter for one query. Before writing specialized SQL, identify the target engine and version and check whether the syntax, locking, transactional DDL, index behavior, and null semantics apply there.

Use portable SQL for ordinary operations when it stays clear and correct. Use engine-specific features when they materially improve correctness, security, or performance and the project supports them. Keep a specialized feature near the owning query or migration rather than disguising it behind a false portability claim.

Examples use positional parameter markers such as `$1` for readability. Replace them with the syntax supported by the repository's driver. Constructs such as row-value comparisons, `RETURNING`, partial indexes, row policies, and concurrent index creation are engine-specific; verify them before use.

Keep boundaries clear between query text and application behavior. Use the ORM or query builder already established in the codebase for routine operations. Use raw SQL when it gives needed control or clarity, and keep it parameterized. A query builder does not remove the need to understand the SQL it generates.

## Formatting and statement structure

Use uppercase SQL keywords and lowercase `snake_case` identifiers unless the repository consistently uses another formatter convention. Put each major clause on its own line. Put each selected expression, inserted row, assignment, grouping key, and ordering key on a separate line once a list has more than one item. Indent continuation lines consistently by two or four spaces according to repository style.

Prefer one logical statement per file section. End statements with semicolons in SQL files and migrations. Use explicit column lists for inserts and keep the column and value order aligned.

```sql
SELECT
    account_id,
    COUNT(*) AS open_invoice_count
FROM invoices
WHERE status = $1
GROUP BY account_id
HAVING COUNT(*) > $2
ORDER BY open_invoice_count DESC, account_id ASC;
```

In a multi-row insert, keep every tuple in the same column order. Use one `INSERT` with multiple `VALUES` rows or the engine's bulk-loading facility instead of a loop that submits one row at a time.

```sql
INSERT INTO account_settings (account_id, setting_key, setting_value)
VALUES
    ($1, $2, $3),
    ($4, $5, $6);
```

For data-changing statements, put the target and changed columns near the top, then make the source or filter easy to inspect. Use `RETURNING` only when the caller needs returned data and the engine supports it.

```sql
UPDATE subscriptions
SET
    status = $1,
    updated_at = $2
WHERE account_id = $3
  AND id = $4;
```

Do not combine unrelated data changes into a dense statement to save lines. A reader should be able to identify the target, changed values, and row scope quickly.

## Names and aliases

Use lowercase `snake_case` for tables, columns, constraints, indexes, views, and routines. Prefer descriptive singular or plural table names according to the repository's established convention; use one convention consistently. Avoid quoted mixed-case names, spaces, abbreviations without a stable domain meaning, and reserved words.

Name constraints for the invariant and table they own, such as `orders_account_id_fkey` or `users_email_key`. Name indexes for their table and leading access pattern, such as `orders_account_id_created_at_idx`. Follow the engine or migration framework's naming limits.

Qualify columns with table aliases in joins and in queries where more than one relation could supply the name. Use short, stable aliases for simple joins (`u`, `o`); use descriptive aliases when a query has several relations, self-joins, or repeated domain roles. Avoid aliases that obscure the source.

```sql
SELECT
    customers.id AS customer_id,
    orders.id AS order_id,
    orders.created_at
FROM customers
JOIN orders ON orders.customer_id = customers.id;
```

Use output aliases that describe the resulting value. Avoid `value`, `data`, or `result` when a domain name is available. Do not rely on a select-list alias in a clause where the target engine does not allow it.

## Query composition

Select only the columns the caller needs. Avoid `SELECT *` in application paths, views, reports with a stable contract, and production routines. An explicit projection prevents accidental data exposure and makes schema changes easier to review. `SELECT *` is acceptable for short-lived local exploration when the result is not saved or consumed by an application.

List joins explicitly. Use `JOIN ... ON` for relationships and `CROSS JOIN` only when the Cartesian product is intended. Do not use comma joins. Keep join predicates next to the join they constrain, and distinguish join conditions from row filters.

```sql
SELECT
    orders.id,
    customers.name AS customer_name
FROM orders
JOIN customers ON customers.id = orders.customer_id
WHERE orders.status = $1;
```

Choose join type from the required result. An inner join removes unmatched rows; a left join preserves the left side and produces nulls for missing right-side values. Moving a right-side filter between `ON` and `WHERE` can change a left join into effective inner-join behavior. Keep the filter in `ON` when unmatched left rows must remain.

Use a CTE when it names a meaningful intermediate result or separates a complicated operation into understandable phases. Do not wrap a simple expression in a CTE solely to add lines. Avoid long chains that rename the same data at every step. Check the target engine's CTE inlining and materialization behavior when performance depends on it.

```sql
WITH eligible_accounts AS (
    SELECT id
    FROM accounts
    WHERE state = $1
)
SELECT
    invoices.account_id,
    SUM(invoices.amount) AS outstanding_amount
FROM invoices
JOIN eligible_accounts ON eligible_accounts.id = invoices.account_id
WHERE invoices.paid_at IS NULL
GROUP BY invoices.account_id;
```

Use `UNION ALL` when duplicates should remain; use `UNION` only when removing duplicates is part of the result contract. The duplicate elimination in `UNION` has a cost and can conceal incorrect input cardinality.

## Correctness and result shape

Use `IS NULL` and `IS NOT NULL` for null checks. Ordinary comparisons with `NULL` produce an unknown result, not true or false. Do not treat `NULL` as an empty string, zero, or a default unless that is the domain meaning and the query handles it explicitly.

Write predicates so every condition and operator is visible. Parenthesize mixed `AND` and `OR` conditions according to the intended grouping, even when precedence technically settles the result. Use half-open time ranges for adjacent windows so a boundary row is not counted twice.

```sql
SELECT
    events.id,
    events.occurred_at
FROM events
WHERE events.occurred_at >= $1
  AND events.occurred_at < $2;
```

Do not rely on an implicit row order. Add `ORDER BY` anywhere a stable order matters, including pagination, a limited result, deterministic aggregation, or a test fixture. Add a unique tie-breaker to the ordering when the primary sort key can repeat.

Prefer keyset pagination for large or frequently changing result sets when the sort key is stable and indexed. Use a cursor containing the complete sort key, including its unique tie-breaker. `OFFSET` remains suitable for small results or interfaces that require direct page numbers, when its cost and shifting-page behavior are acceptable.

```sql
SELECT
    id,
    created_at,
    total
FROM orders
WHERE (created_at, id) < ($1, $2)
ORDER BY created_at DESC, id DESC
LIMIT $3;
```

Use `EXISTS` when the question is whether a matching row exists and duplicate joined rows are not wanted. Aggregate at the intended grain. Include the grouping key that defines one output row, and distinguish `COUNT(*)` from `COUNT(column)`, which ignores null values. Do not rely on engine-specific behavior that permits ungrouped selected columns.

Handle division by zero, empty input sets, and nullable aggregate results deliberately. Use `COALESCE` only when the replacement value matches the domain contract; do not use it to hide missing or invalid data.

Use explicit casts when they clarify the intended type or prevent ambiguous inference. Avoid implicit coercions that change comparison, precision, timezone, or index behavior. Preserve exact values for money and other exact quantities with an appropriate exact numeric type; use approximate floating-point types only when approximation is acceptable.

## Schema and data modeling

Model each table around one entity or relationship at a clear grain. Give each table a primary key unless the natural key is stable, compact, and genuinely unique for the row's lifetime. Choose the key type for the engine and workload; do not use a universal ID type without considering key distribution, index locality, interoperability, and whether IDs are exposed externally.

Use foreign keys to encode relationships and select `ON DELETE` and `ON UPDATE` behavior intentionally. Add indexes to foreign-key columns when joins, deletes, updates, or referential checks need them; verify whether the engine creates such indexes automatically. An index has storage and write costs, so choose it from actual access patterns.

Use `NOT NULL`, `UNIQUE`, `CHECK`, and foreign-key constraints to enforce durable invariants at the database boundary. Name constraints. Prefer a database constraint to an application-only check when all writers must obey the same rule. Account for each engine's treatment of nulls in unique constraints and checks.

Choose types from the domain and target engine. Use exact numerics for exact quantities, a boolean type for two-state flags, and an appropriate time type with a documented timezone convention. Distinguish an instant from a local calendar date or wall-clock time. Set and use UTC consistently for instants where that is the application convention. Use bounded string types only when the limit is a real domain constraint; do not add arbitrary length limits by habit.

Represent a small closed set of values with a constraint or engine-supported enum when the set is genuinely stable. Use a lookup table or reference relation when values need metadata, lifecycle, or independent administration. Do not duplicate the same invariant across application code, triggers, and constraints without a reason.

Store structured JSON only when its variable shape is part of the domain. Keep frequently filtered, joined, constrained, or aggregated values in typed columns. Add a JSON index only for queries that use its supported operators and have a measured need.

## Security and access control

Pass data values through the database driver's parameter binding or the repository's safe query-builder API. Never concatenate or interpolate external values into SQL, even after quoting, trimming, numeric conversion, or validation. Parameterization is the primary protection against SQL injection.

Parameters generally cannot stand for identifiers, operators, or sort directions. For dynamic query structure, choose from a small closed allowlist of known identifiers or query fragments. Reject unknown values before constructing the statement.

```sql
SELECT
    id,
    email
FROM users
WHERE tenant_id = $1
  AND email = $2;
```

Give application roles only the privileges required for their operations. Avoid broad grants. Separate migration-owner credentials from routine application credentials. Treat views, functions, triggers, and definer rights as security boundaries and review their effective privileges.

For multi-tenant or user-owned data, enforce row ownership in the database where the engine and platform support it. In PostgreSQL, use Row Level Security policies that bind the row's tenant or owner to a trusted identity context. Index policy columns when the policy predicate and workload require it. Verify access through the same role and request context the application uses; a privileged owner session can bypass policies and give false confidence.

Never put secrets, credentials, or unnecessary personal data in query text, SQL examples, stored routines, logs, or migration fixtures. Ensure errors and query logging do not expose bound sensitive values.

## Transactions and concurrency

Use a transaction when multiple statements must succeed or fail as one unit, or when the operation requires a consistent view. Keep transactions short. Do not wait for user input or call external services while holding a transaction open.

Acquire locks in a consistent order across code paths that touch the same rows. Lock only the rows and resources the operation needs. Select an isolation level based on the anomaly the business operation must prevent, and make retries safe when the engine reports serialization failures or deadlocks.

Use atomic updates, unique constraints, and conflict handling to enforce invariants under concurrent writers. Do not implement check-then-write logic as separate unprotected statements when two transactions could pass the check simultaneously.

Use `FOR UPDATE SKIP LOCKED` only for queue-like work where skipping rows currently claimed by another worker is correct. It can omit locked rows and is unsuitable for reads that promise a complete or consistent result. Make claim, transition, and completion behavior explicit, and ensure abandoned work can be recovered.

Batch bulk inserts and updates when that reduces round trips without creating an unbounded transaction or lock. For large backfills, use bounded batches, a stable progress key, resumability, and a clear stop condition. Measure lock impact against representative data.

## Indexes and performance

Start from the query shape and workload, then use the engine's plan tools to verify the access path. Do not add an index merely because a column appears in a predicate. Consider selectivity, table size, write rate, existing indexes, sort order, and the cost of maintaining each additional index.

Order composite index columns to match the actual filters and ordering. Equality predicates commonly precede range or ordering columns, but the correct order depends on leading-prefix use and the full workload. Use partial, expression, covering, or specialized indexes only when the target engine supports them and a real query benefits.

Index columns used by frequent joins, selective filters, and row-level access policies when plan evidence supports it. Check whether composite indexes already cover a foreign key's leading column before adding a duplicate. Keep indexes small enough that write amplification and storage remain acceptable.

Inspect plans for expensive scans, joins, sorts, row-estimate errors, and repeated work. A sequential scan is not inherently a defect; it may be cheapest for a small table or a query returning much of the data. Compare estimates with actual execution when safe and appropriate. `EXPLAIN ANALYZE` executes the statement, so do not use it on a modifying statement or expensive production query without understanding and controlling its effects.

Avoid N+1 query patterns by fetching related data in a bounded query or batch where appropriate. Avoid fetching more rows or columns than the caller uses. Use pagination for unbounded results. For analytic workloads, choose aggregates, materialized views, or summaries only when freshness, refresh cost, and storage fit the requirement.

## Migrations and schema evolution

Make every production schema change through the repository's versioned migration system. Do not change a live database manually and leave the migration history behind. Keep deployed migrations immutable; correct a deployed change with a new migration. Follow the project's forward-only production policy and describe any supported rollback procedure outside the SQL source.

Before authoring a migration, inspect the current schema, migration history, application readers and writers, data volume, engine version, and migration runner behavior. Identify lock duration, table rewrites, transaction support, and failure recovery for each operation. Syntax that works locally may behave differently on a large production table.

Keep schema changes and large data transformations in separate migrations or controlled jobs so each can be bounded, observed, and retried. For incompatible changes, use expand and contract: add the new representation, deploy code that can work across the transition, backfill in bounded batches, switch reads and writes, verify old usage has stopped, and remove the old representation later.

Make additions backward-compatible where practical. Add a nullable column or an engine-supported safe default first, then populate and constrain it in a later step when required by table size or deployment order. Do not assume a default is instant or lock-free across engines and versions. Add `NOT NULL` only after existing rows and all active writers satisfy the invariant.

Create indexes using the target engine's online or concurrent option when it reduces production blocking. Confirm whether that operation can run inside the migration transaction and how the migration tool handles retries or partial failure. A failed concurrent index build may leave an invalid index that needs cleanup.

Before removing a column, table, enum value, or constraint, remove dependent application and reporting usage and confirm deployed clients no longer rely on it. Before a backfill or destructive update, quantify the affected rows and define a recovery path. Never use an unbounded data-changing statement against a large production table without understanding transaction size, lock impact, and rollback cost.

Use migration files that clearly group one coherent schema transition. Keep statement order explicit and rerun behavior consistent with the migration system. Do not add defensive `IF EXISTS` or `IF NOT EXISTS` clauses reflexively; use them when the migration framework or recovery design needs idempotence and the clauses cannot conceal schema drift.

## Verification and review

Use the repository's SQL formatter, linter, migration checks, and database test setup. Validate syntax against the target engine and version. Test the migration from the prior schema state and verify the resulting schema and data invariants. Exercise relevant queries with representative data and realistic parameter values.

For behavior changes, cover empty results, duplicate rows, nulls, boundary timestamps, and concurrent writes where those conditions affect correctness. Test permissions through the actual application role. Confirm generated query plans for critical paths and measure before claiming an optimization.

### Review checklist

- Does the SQL match the repository's engine, supported version, and formatter?
- Is there any SQL source comment, commented-out statement, comment directive, or `COMMENT ON` statement?
- Are values parameterized, and are dynamic identifiers selected from an allowlist?
- Are selected columns explicit and join predicates unambiguous?
- Are nulls, duplicates, grouping grain, ordering, pagination, and boundary conditions handled intentionally?
- Do constraints enforce durable invariants, and do types match the domain?
- Are privileges and row policies limited to the intended data and role?
- Are transactions bounded, locks ordered, retries safe, and concurrent writers accounted for?
- Are indexes supported by query workload and plan evidence?
- Does the migration account for production volume, deployment order, locks, retries, and recovery?
- Were syntax, migration state, data behavior, and critical query plans verified with the available project tools?
