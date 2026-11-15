# Component decisions

Read during a component-library audit. These are decision procedures for the audit, applied under the target repositories' standards. Verify framework-specific details against the installed version. Record the evidence supporting each decision; there is no scientifically established universal component count, variant limit, or directory layout.

## Compare contracts before appearances

Compare user purpose, semantic role, keyboard and focus behavior, state transitions, accessible naming, data requirements, layout, tokens, and supported consumers. Two blue rectangles may be a navigation link and an action button. Preserve their different semantics even if they share styling. Two differently named action buttons with the same contract may belong to one canonical component.

| Evidence | Decision | Required migration detail |
| --- | --- | --- |
| Same purpose, behavior, and states; differences are accidental spacing, radius, naming, or color drift | Standardize one component and its tokens | Chosen design authority, before/after states, all copies and overrides removed |
| Same contract with a meaningful recurring visual emphasis, size, density, or placement need | Add or retain a named variant axis | Actual use cases, defaults, legal values, accessibility and supported combinations |
| Differences are content or optional substructure with stable interaction ownership | Compose through children, slots, or small subcomponents | Slot contract, ordering, semantics, state ownership, required content |
| Repeated domain-specific defaults or data orchestration around a general primitive | Keep a domain wrapper near its feature | Shared primitive imports, domain dependencies, no copied primitive styles |
| Different purpose, semantic role, state machine, focus model, or lifecycle | Split components, sharing lower-level primitives where useful | Separate contracts and tests; avoid a conditional mega-component |
| Uncertain reuse or coincidental resemblance | Retain locally pending evidence | State what evidence would justify extraction; avoid speculative shared APIs |
| A supported old consumer cannot migrate in the same delivery | Temporary adapter | Consumer/version, mapping, checks, owner, removal trigger |

## Evaluate variants

For every axis list current consumers and the user need it expresses. Retain an axis when the conceptual contract remains coherent and callers can predict its behavior. Prefer semantic names such as emphasis or tone where the established design system uses them. Avoid names tied to a page, campaign, or accidental hex value. A size prop is not automatically justified: show the supported density or placement need.

Merge aliases with identical meaning. Remove unused values only after checking supported public consumers. Reduce redundant booleans that encode one mutually exclusive choice to a closed union or equivalent language construct. Keep genuinely independent booleans when they describe independent capabilities. Loading and disabled are usually state/capability concerns; avoid multiplying unrelated visual variants to represent them.

Build a table of legal and illegal combinations. In TypeScript encode incompatible prop shapes through discriminated unions where useful; do not cast errors away. A growing collection of flags that selects unrelated DOM trees or state machines is evidence for composition or splitting. Independent visual axes may remain orthogonal without materializing every Cartesian combination as a separate component. Test meaningful interactions and risky boundaries; do not invent a numeric variant cap.

Example: primary and secondary submit actions may share a Button with an emphasis axis. A ProductCard with pricing and purchase orchestration can compose a shared Card surface inside its feature. A navigation menu and a select input need separate contracts even when their popovers look similar. These examples guide investigation and do not override the product's semantics.

## Choose ownership and package shape

Separate tokens, low-level primitives, reusable product-independent components, domain compositions, and page orchestration by ownership and dependency direction. These are conceptual roles, not mandatory directories or packages. Keep feature data fetching, routing policy, authentication, and business rules out of a general UI library. Keep reusable accessibility behavior in the appropriate primitive or component so apps do not reimplement it inconsistently.

Promote a component to the library when real consumers need one maintained contract and the library can own its API, testing, documentation, and release cost. A single local use may remain local. Do not extract merely because a file is long, or retain duplication merely because each copy is short. Keep public types beside their contract; derive from authoritative schemas when possible. Avoid a global types dumping ground and exporting implementation-only types.

Document each public component's purpose, import, props, defaults, supported states, variant rationale, accessibility responsibilities, and examples through the project's existing documentation or story system. Keep implementation, tests, stories, and styles close using existing conventions. Consumers should use supported package entrypoints and delivered styles/tokens. Prevent deep imports and app-specific CSS overrides from becoming a second undocumented API. Verify the production package, including declarations and assets, rather than relying on source aliases.

## Primary evidence and limits

- [React: Thinking in React](https://react.dev/learn/thinking-in-react) supplies hierarchy, responsibility, and state ownership guidance. It does not prescribe a universal folder layout.
- [GOV.UK contribution criteria](https://design-system.service.gov.uk/community/contribution-criteria/) requires useful, unique, usable, consistent, and versatile shared contributions. Its government service context is not a mandatory release process for every library.
- [TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html) explains discriminated unions and exhaustiveness. Types alone do not verify runtime accessibility or styling.
- [npm package.json](https://docs.npmjs.com/cli/v11/configuring-npm/package-json/) defines package entrypoints, files, and dependency metadata; use the target package manager's corresponding guidance.
- [Martin Fowler: Branch By Abstraction](https://martinfowler.com/bliki/BranchByAbstraction.html) supports gradual substitution. It does not justify indefinite adapters or require long-lived Git branches.

The decision table synthesizes these sources and the requested audit goals. Treat it as engineering judgment to substantiate against the codebase, rather than experimental proof that one architecture is always superior.
