---
name: interaction-design
description: "Reference for UX/UI interaction decisions: task models, controls, input, focus, navigation, forms, feedback, asynchronous state, recovery, adaptation, specifications, and evaluation."
version: "0.2.0"
created: "2026-10-24"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Apple"
  - "World Wide Web Consortium"
  - "Justinmind"
  - "Talia Hartwell"
  - "Ramotion"
type: reference
status: experimental
---

# Interaction design

Interaction design defines what people can do, how they discover and perform an action, how the system responds, and how they continue or recover. Its unit is a complete exchange between a person and a product. A button's appearance is only one part of that exchange.

Use this guide when designing, specifying, implementing, or reviewing interfaces. It covers websites and applications, with web examples and explicit native-platform distinctions. Start from the task and its consequences; choose controls and visual treatment after the behavior is clear.

## Use this reference

This guide owns task and object models, control choice, state transitions, focus lifecycle, navigation, commitment, recovery, and feedback events. Apply the shared [framework](reference.md) for decision priorities, requirements language, and evidence.

For a new flow, start with [task and state modeling](#1-define-the-task-and-interaction-model), then the relevant [control and input patterns](#4-choose-controls-by-meaning). Use [specification and evaluation](#16-specify-the-interaction-contract) to complete the contract. [Accessibility](accessibility.md) owns access requirements and semantics; the shared framework identifies the owners of spatial and sensory expression.

## Contents

1. [Define the task and interaction model](#1-define-the-task-and-interaction-model)
2. [Make actions understandable](#2-make-actions-understandable)
3. [Model states and transitions](#3-model-states-and-transitions)
4. [Choose controls by meaning](#4-choose-controls-by-meaning)
5. [Support input and direct manipulation](#5-support-input-and-direct-manipulation)
6. [Design focus and selection](#6-design-focus-and-selection)
7. [Preserve orientation through navigation](#7-preserve-orientation-through-navigation)
8. [Choose disclosure and modality](#8-choose-disclosure-and-modality)
9. [Support data entry and commitment](#9-support-data-entry-and-commitment)
10. [Make search and collections manageable](#10-make-search-and-collections-manageable)
11. [Communicate response and progress](#11-communicate-response-and-progress)
12. [Keep asynchronous work trustworthy](#12-keep-asynchronous-work-trustworthy)
13. [Prevent errors and support recovery](#13-prevent-errors-and-support-recovery)
14. [Protect attention and informed choice](#14-protect-attention-and-informed-choice)
15. [Adapt behavior to context](#15-adapt-behavior-to-context)
16. [Specify the interaction contract](#16-specify-the-interaction-contract)
17. [Work through a complete example](#17-work-through-a-complete-example)
18. [Evaluate behavior in use](#18-evaluate-behavior-in-use)

## 1. Define the task and interaction model

Write the intended outcome in the person's terms: "Move these invoices into next month's budget" gives more direction than "Use the batch-edit toolbar." Establish the starting context, available information, successful result, and cost of a mistake. Observe existing work where possible; separate known behavior from assumptions to test.

A useful interaction brief identifies:

- Who performs the task, how often, with what experience, and under what physical or cognitive constraints.
- The objects people recognize, the actions they take, and the scope of each action.
- Entry points, dependencies, intermediate decisions, exit routes, and what survives interruption.
- The expected result, evidence of completion, and recovery when the result is unavailable or wrong.

Keep the product's conceptual model coherent. If a workspace contains projects and projects contain documents, use those relationships consistently in navigation, permissions, labels, and movement. Explain a meaningful distinction such as archive versus delete before asking people to choose.

Use five dimensions as a completeness prompt: words explain intent; visual representations identify objects and state; physical context determines feasible input; time determines response and continuity; behavior defines consequences. These dimensions work together. A clear label cannot compensate for an unpredictable effect.

Minimize unnecessary decisions and repeated entry. Do not minimize clicks at the expense of comprehension or control. A review step can be valuable before an expensive commitment; an extra confirmation for every reversible edit usually adds friction.

## 2. Make actions understandable

An affordance is a possible action; a signifier is the cue that communicates it. A draggable object needs both working drag behavior and a discoverable indication that it can move. Style alone does not establish operability.

Use familiar control shapes, placement, labels, and responses. Keep essential actions visible; reserve contextual menus for secondary actions that remain discoverable elsewhere when necessary. If decoration resembles a control, either make it operate as expected or remove the misleading cue.

Label actions with their result: "Save draft," "Send invitation," or "Delete project." Name the affected object when scope could be ambiguous. Use generic labels such as "Continue" when the next step is already clear, rather than inventing a specific result the button does not yet perform.

Map controls to effects through proximity, ordering, direction, and matching terminology. A row action affects that row; a collection action declares its selected scope. A slider identifies the quantity, direction, current value, and useful limits. Avoid modes in which the same action silently changes meaning. Make an active editing or selection mode visible and provide a clear exit.

Preserve a stable behavioral vocabulary across the product. The same symbol and label should produce the same kind of result. Brand expression can shape tone, material, and feedback; keep established activation, editing, scrolling, and dismissal conventions dependable.

## 3. Model states and transitions

Describe what the person sees and can do in each state, including transitions triggered by the system. Separate an object's persistent state from a control's temporary presentation and an operation's progress.

| State family | Distinction to preserve | Design consequence |
| --- | --- | --- |
| Control | Rest, hover, focus, pressed, unavailable | A focus indicator does not imply activation; a pressed appearance does not prove success. |
| Value or object | Selected, checked, expanded, edited, saved | Persistent state remains understandable after focus leaves. Several states can coexist. |
| Operation | Idle, pending, complete, failed, canceled, outcome unknown | Each meaningful transition needs truthful feedback and a supported next action. |
| Content | Loading, available, empty, no matches, partial, stale, unavailable | Explain why content is absent or limited and offer the appropriate route forward. |

Treat this as a set of dimensions, not one mutually exclusive list. A selected row can also be focused while a save is pending. Specify combined appearances and behavior so one state does not erase another.

For each consequential transition, identify the starting state, event, condition, resulting state, visible response, focus destination, persistence, and recovery. A condition might be permission, valid input, connectivity, or ownership. An unavailable action should explain its prerequisite where people can discover it.

Include repeated activation, rapid reversal, interruption, and competing updates. A state diagram helps when branches or concurrent operations become difficult to inspect in prose. A short table is sufficient for a simple control. Do not create diagrams that merely redraw a linear sequence without clarifying a decision.

## 4. Choose controls by meaning

Prefer a platform control that already expresses the required action. A custom component inherits the full responsibility for semantics, input, focus, state, and testing.

| Intent | Default control or pattern | Important boundary |
| --- | --- | --- |
| Go to a destination | Link on the web; platform navigation component in native apps | Web links preserve open-in-new-tab, copying, and browser history. |
| Perform an action | Button | A styled container is not a complete button implementation. |
| Choose independent values | Checkboxes | Show whether a group is partially selected when that state exists. |
| Choose one value from a set | Radio group or select; searchable picker for a large set | Radios expose a small comparison set; a picker saves space but hides alternatives. |
| Change an immediate on/off setting | Switch | Its label describes the setting. If a later Save commits it, make that form behavior explicit. |
| Reveal content | Disclosure button | Show expanded state and its relation to the revealed content. |
| Switch panels within one context | Tabs | A tab is not a substitute for every site navigation link. |
| Choose a bounded continuous quantity | Slider with readable value | Offer precise entry or step controls when accuracy matters. |
| Edit structured or long content | Appropriate text field or editor | Preserve native selection, caret movement, clipboard, and undo behavior. |

Apply [Accessibility’s native semantics and ARIA contract](accessibility.md#8-make-structure-and-meaning-programmatic). For a card with a destination and secondary actions, give each action a distinct target and accessible name.

Distinguish unavailable from hidden. Hide irrelevant actions when their absence does not conceal an expected capability. Keep unavailable actions visible when they explain the product model, but provide the reason and remedy outside a hover-only tooltip. Apply a coherent policy for whether unavailable custom actions remain keyboard-discoverable; native disabled controls normally leave the tab order.

## 5. Support input and direct manipulation

Design a complete route for each supported input method. Touch, pointer, keyboard, speech, switch access, and assistive technology can invoke the same task through different mechanics. Do not infer capabilities from viewport width: a tablet may have a keyboard and a desktop may have touch.

For pointer and touch activation, default to completion on release with a way to abandon the action before it commits. Press feedback can appear earlier. Starting a dangerous operation on pointer-down removes an important opportunity to cancel. Preserve platform exceptions for tasks whose function depends on continuous down-state input, such as drawing.

Apply [Accessibility’s target-size and pointer requirements](accessibility.md#support-pointer-touch-speech-and-switches). Use [Composition](composition.md#16-build-a-spatial-system) to allocate hit areas and separation without overlap, especially between destructive and frequently used actions.

Use [Accessibility’s hover/focus-content requirements](accessibility.md#tooltips-hover-content-and-touch) for tooltips. Choose [another disclosure pattern](#8-choose-disclosure-and-modality) when the content contains actions or belongs to the task rather than supplementary help.

For dragging, show the picked-up object, valid destinations, insertion position, constraints, and result. Define cancellation and invalid-drop behavior. Keep scrolling and dragging distinguishable, and preserve system edge gestures. Choose the alternative route using [Accessibility’s single-pointer and keyboard requirements](accessibility.md#support-pointer-touch-speech-and-switches).

Direct manipulation should track input without forcing people to wait for an ornamental transition. Preserve object identity and a predictable relationship between movement and effect. Specify [snapping, bounds, inertia, and interruption with Motion](motion.md#10-handle-gestures-inertia-and-constraints). Custom gestures supplement visible actions and require evidence that their learning cost serves the task.

## 6. Design focus and selection

### Keep the meanings separate

Keyboard focus identifies where keyboard input operates within the active interaction context. Selection identifies chosen content or a chosen value. Hover identifies a pointer target; press indicates activation in progress. A selected item can remain selected while focus moves elsewhere.

Use [Accessibility’s focus visibility, contrast, and geometry requirements](accessibility.md#make-focus-a-visible-meaningful-state). Keep focus, selection, error, and expanded states distinguishable when they coexist; the interaction contract determines which states coexist and where input goes.

### Define travel through the interface

Choose an established component pattern before assigning keys. Apply [Accessibility’s keyboard conventions and composite-control requirements](accessibility.md#9-support-keyboard-focus-and-alternative-input); this guide owns the task-dependent focus destinations below.

Allow selection to follow focus only when the consequence is immediate, predictable, and inexpensive. Use manual tab activation when changing panels starts slow loading. Exploring options must not commit a consequential action.

### Specify the focus lifecycle

| Event | Default focus behavior | Condition to handle |
| --- | --- | --- |
| Open a menu or picker | Enter the pattern's initial focus position | Editable comboboxes often retain input focus while identifying an active option. |
| Open a web modal dialog | Move inside and contain the tab sequence while open | Choose an input, introductory content, or safe action according to the task and content length. |
| Close a temporary surface | Return to its invoking control | If it disappeared or the task advanced, choose a logical continuation. |
| Navigate to a new application view | Establish orientation at a meaningful destination | Client-side web navigation needs a title update and a deliberate focus policy; ordinary document navigation uses browser behavior. |
| Update results or background status | Preserve the current interaction point | Announce a relevant result without moving focus just to make it noticeable. |
| Remove the focused web item | Move to the next meaningful item, previous item, or collection control | Keep identity stable through sorting and rendering; avoid dropping focus to the page body. |
| Reject a submitted form | Move to an actionable error summary or the first invalid field | Keep errors associated with their inputs and avoid repeatedly moving focus during correction. |

Move focus because the person's action or a necessary structural change demands it. Timers, promotional messages, and arriving data do not justify stealing focus. Autofocus is useful in a purpose-built entry task; on a general landing view it can skip introductory content and summon an unwanted mobile keyboard.

These web lifecycle defaults do not replace native focus systems. On iPadOS, native focus groups distinguish movement between regions from movement within a group. tvOS uses directional focus across actionable items and explicit activation for opening content. visionOS gaze hover is distinct from keyboard/controller focus. Use native framework behavior and verify the actual platform and access settings rather than reproducing web Tab rules everywhere.

## 7. Preserve orientation through navigation

Make the current location, available destinations, and route back understandable. Distinguish hierarchy, navigation history, and task progress: a breadcrumb, Back action, and step indicator answer different questions.

Keep primary destinations stable across views. Use the same names for the same places, and show the active destination without confusing it with transient focus. Preserve relevant filters, sort, selection, scroll position, and drafts when people inspect a detail view and return.

On the web, meaningful locations should support appropriate URLs, refresh, deep linking, and browser Back/Forward. Decide which changes enter history: a new destination usually does; every keystroke in a live search usually should not. Opening a deep link must establish enough surrounding context to continue.

Use disclosure controls for ordinary expanding website navigation. Application-style menus introduce a specialized keyboard model; a group of destination links does not need menu semantics merely because it is called a menu visually.

Separate leaving a view from canceling a transaction. Back may return to the previous screen while a background upload continues. Cancel may stop that upload without changing location. Name these effects accurately and protect unsaved work as described in section 13.

For multistep tasks, show progress when it helps planning, retain valid earlier answers, and allow review before commitment. Adapt later steps when earlier answers change, explaining any invalidated information. Do not require a linear wizard when people need frequent comparison or movement among independent settings.

## 8. Choose disclosure and modality

Reveal detail progressively when it reduces irrelevant complexity. Keep the next necessary action, decisive constraints, and consequences available before commitment. Advanced settings can be hidden behind a clear disclosure; unavoidable fees and destructive scope cannot.

Choose a container by the relationship between the task and its surrounding context.

| Situation | Default presentation | Tradeoff |
| --- | --- | --- |
| Explain or edit a small nearby detail | Inline expansion | Preserves context but increases page length. |
| Offer contextual actions | Menu or anchored popover | Compact; needs clear ownership and dismissal. |
| Inspect or edit while comparing with the main view | Nonmodal panel | Keeps both contexts available; requires a clear reading and focus order. |
| Complete a short, bounded task that must suspend the parent | Modal dialog or platform sheet | Focused, but interrupts access to the parent. |
| Perform a substantial task or visit a durable destination | Page, window, or appropriate full-screen task | Provides room and navigation at the cost of a context change. |

A backdrop does not establish modality by itself. A web modal must make the background inert, manage focus, expose its name and role, and provide an obvious dismissal control. Support Escape through the dialog's cancellation path. If dismissal would discard work, offer preservation or a clear decision before closing. Do not rely solely on clicking the backdrop or swiping.

Avoid stacking modal tasks. Finish, replace, or return from the current surface before opening another; reserve an additional alert for a necessary exceptional decision. Distinguish dismissing a local picker from closing the enclosing task. A nonmodal surface must permit deliberate movement between itself and the parent without trapping focus.

## 9. Support data entry and commitment

### Reduce entry without removing understanding

Ask for information only when it serves the task. Reuse known values when appropriate, show consequential defaults, and allow correction. Group related fields in a meaningful sequence. Explain required information, formats, limits, and why sensitive data is needed before submission.

Use persistent visible labels, suitable input types, mobile keyboards, and autocomplete metadata. Preserve paste, password managers, text selection, and international input composition. Names, addresses, phone numbers, and dates need formats appropriate to the people using the product. Do not treat a numeric-looking identifier as an arithmetic quantity.

Prefer visible choices when comparison matters and the set is small. Prefer search or filtering when a large choice set makes scanning expensive. Defaults should reduce effort without silently granting consent or making consequential decisions.

### Validate when a judgment is useful

Do not declare an incomplete value wrong while the person is still composing it. Default to format validation after leaving a completed field or attempting submission. Earlier feedback is useful for constraints that help during entry, such as remaining length or password requirements. After an error appears, update it as correction becomes valid.

Keep error messages beside their fields and explain how to correct the problem. On submission, provide a summary when errors span the form. Preserve all safe entered values. Separate field errors from connection failures and server-side business rules; a correct email address can still fail because an invitation already exists.

For ordinary web forms, default to allowing a submission attempt that reveals missing requirements. A permanently disabled primary action can conceal why progress is blocked. Disable repeated submission while the same operation is pending, or use a disabled control when the missing prerequisite is already explicit. Native flows may use platform-specific availability conventions; keep the reason understandable.

### Make the commit model explicit

| Model | Use when | Required behavior |
| --- | --- | --- |
| Immediate change | A reversible setting has an independent effect | Reflect the new state and explain failure or reversal. |
| Autosave | Continuous work benefits from persistence without repeated decisions | Distinguish edited, saving, saved, and failed; identify what is saved locally versus remotely. |
| Explicit Save or Apply | Related edits need review or atomic commitment | Show dirty state; define Cancel, navigation, and partial failure. |
| Review then commit | Money, publication, permissions, or another serious consequence needs verification | Summarize the actual effect and label the final action specifically. |

Do not mix commit models invisibly within one form. A preview is provisional until the declared commit point. "Done" should make clear whether it saves changes or only closes the surface. Offer reset only when useful, distinguish it from canceling edits, and state whether it restores defaults or previous values.

## 10. Make search and collections manageable

State the scope of search and whether results update during typing or after submission. Keep query entry responsive. If live results are delayed, show activity near the results and discard obsolete responses. Do not move focus out of the search field after each update.

Autocomplete needs a clear distinction between typed text, the active suggestion, and a committed choice. Define arrow navigation, selection, dismissal, and whether arbitrary text is allowed. Preserve ordinary text editing and do not submit an unfinished input-method composition. Explain no matches separately from loading or failure.

Show applied filters and provide a clear route to remove them. Specify whether a change applies immediately or requires Apply, and preserve that rule across the filter group. Show result counts and meaningful sort state without announcing every keystroke. A no-results state should help people broaden the query or remove constraints.

For collections, distinguish opening an item from selecting it for action. Display the selected count and exact batch scope, especially across pages: "Select this page" and "Select all matching results" have different consequences. Define what happens to selection after filtering, refreshing, or changing permissions. Report partial batch outcomes per affected item.

Choose pagination, explicit "Load more," or continuous loading by the task. Pagination supports bounded comparison and revisiting; continuous loading supports exploration but complicates position, footer access, and recovery. Preserve place when returning to the collection. Virtualized content must keep keyboard movement, active-item identity, and assistive-technology access coherent.

## 11. Communicate response and progress

Separate acknowledgment of input from evidence of completion. A button can respond immediately while the operation remains pending. A checkmark that means "saved" must reflect the declared persistence guarantee.

Use feedback near the affected object whenever practical. Match interruption to significance: a changed value can explain itself; a background status belongs inline; an important completed transaction needs persistent confirmation; a decision needed to avoid loss may justify an alert.

| Condition | Appropriate response |
| --- | --- |
| Direct, local effect | Show the changed object or value; avoid redundant success messages. |
| Noticeable waiting | Show activity and identify what is happening; keep unrelated work available. |
| Measurable progress | Show meaningful completed work or stages; do not fabricate a percentage. |
| Unknown duration | Use truthful activity feedback with recovery if progress stalls. |
| Empty starting state | Explain what belongs here and how to begin. |
| Partial or stale content | Identify what is available, what is missing or outdated, and how to refresh or recover. |
| Important completion | Provide a durable result, such as a receipt, destination link, or saved version. |

Choose indicator delays against measured response behavior to avoid flashing a loader for operations that finish immediately. Do not impose one universal duration. Skeletons can preserve expected layout; they should not imply data exists or hide a persistent error.

Status announcements should communicate meaningful changes without moving focus or flooding assistive technology. Use a transient toast for supplementary information, with persistent access to any essential action or result. An expiring message must not be the sole route to recovery.

Choose [Motion](motion.md#16-apply-interaction-patterns), [Sound](sound.md#11-design-product-sound-systems), or [Haptics](haptics.md#12-build-an-interaction-vocabulary) for sensory expression. Apply [Accessibility’s functional-needs model](accessibility.md#2-design-around-functional-needs) to preserve equivalent access.

## 12. Keep asynchronous work trustworthy

Default to retaining useful content while refreshing it, identifying stale or pending data when that affects a decision. Avoid blanking an entire interface because one region is updating. Keep the editable draft distinct from the last confirmed version.

Optimistic updates are suitable when success is likely, the effect is reversible, and failure can be repaired intelligibly. A favorite can appear selected immediately. A payment or newly granted permission needs confirmed evidence before the interface reports completion. If an optimistic change fails, restore the prior state or mark the unresolved change while preserving the person's work.

Specify ownership of results. An older search response must not overwrite a newer query. A save for an earlier draft must not label later edits as saved. Keep object identity stable while sorting, refreshing, or receiving collaboration updates.

Prevent duplicate consequences, not merely duplicate clicks. Disabling a pending button helps the interface, but the operation also needs a safe retry contract when repetition could create another order, invitation, or charge. If the connection fails after the server may have acted, show an unknown outcome and reconcile existing status before inviting another commitment.

Separate cancellation from rollback. Stopping a local wait may leave a remote job running; a sent message may be impossible to retract. State what the Cancel or Stop control actually guarantees. Long-running work should offer useful status, leaving and returning, and cancellation where supported.

For offline work, identify what remains available, what is queued, and when synchronization happens. Show conflicts without silently discarding either person's changes. Explain access changes or session expiry, preserve recoverable work securely, and resume at a meaningful point after reauthentication.

## 13. Prevent errors and support recovery

Use constraints, previews, clear scope, and safe defaults before adding confirmation dialogs. Prevent an impossible date or invalid destination where feasible, but explain the constraint. Do not silently substitute a consequential value.

Choose protection in proportion to reversibility and impact:

- For routine reversible edits, provide dependable undo rather than interrupting each action.
- For destructive work with recovery, explain the recovery location or interval and preserve a way to use it after a toast disappears.
- For irreversible or unusually consequential work, show the affected objects, scope, and consequence before a specifically labeled commitment.

Avoid placing initial focus or a default keyboard action on an irreversible destructive choice. Additional friction, such as typing an object's name, is justified only when it addresses a serious, demonstrated risk. Repetition without new information trains people to ignore warnings.

Define undo scope, grouping, persistence, and limits. "Undo move" is more informative than an unexplained "Undo." Keep editor text undo distinct from product-level operation history, and avoid allowing a global shortcut to reverse an unrelated action while someone is editing text. Make the effect of undo visible, including changes outside the current viewport.

Distinguish canceling a draft, stopping work, reverting committed changes, and navigating back. Each has a different effect. When leaving threatens unsaved work, offer preservation or an explicit decision through every relevant dismissal path. Prefer continuous recoverability over relying solely on a final browser warning.

An error message states what failed, what remains intact, and what the person can do. Offer the narrowest useful recovery: correct a field, retry a failed file, restore access, refresh conflicting data, or contact support with a safe reference. Retain completed work and do not make people restart a whole task because one part failed.

## 14. Protect attention and informed choice

Interrupt only when an immediate decision is needed or delay has a meaningful consequence. Put routine activity in a place people can consult. Deduplicate repeated notices, group related updates, and let people control nonessential notifications.

Ask for permission at the point its benefit is understandable. Explain the requested capability and provide a useful path after denial. Show whether an automated process is suggesting, preparing, or executing an action; obtain the required commitment before an external consequence and provide status and stopping controls appropriate to the operation.

Make choices honest and comparable. Present costs, recurrence, recipients, data exposure, and destructive scope before commitment. Keep declining, canceling, and changing a decision understandable. Do not use misleading urgency, preselected consent, disguised actions, or an obstructed cancellation path.

Respect people's time and stopping points. Preserve progress across ordinary interruptions. Where a session or task has a limit, explain it early, warn usefully, and support extension or recovery where possible. Help should be contextual and reachable without abandoning the work; forced onboarding should not substitute for understandable controls.

## 15. Adapt behavior to context

Responsive design changes how a task is performed, not just how its boxes fit. Preserve capability, state, and orientation when navigation collapses, panels move, or a dialog becomes a full-screen task. Do not silently lose entered values or focus when crossing a breakpoint.

Keep active controls reachable above an on-screen keyboard and usable with zoom, large text, long translations, and right-to-left layout. Preserve conventional scroll behavior and avoid layouts in which an unseen nested scroller traps the task. Test one-handed reach and coarse pointing where those contexts matter.

Support efficient expert routes through shortcuts, saved defaults, bulk actions, or command interfaces while retaining discoverable ordinary controls. Scope shortcuts to avoid conflicts with text entry, browsers, operating systems, and assistive technology. Make commands discoverable near their actions or in a searchable reference.

Native software should use the platform's navigation, focus, editing, menus, gestures, and window behavior. A web interface should retain browser expectations. Directional remote navigation, gaze targeting, stylus work, and wearable interactions require their own input-specific evaluation. Carry shared task semantics across platforms while allowing different mechanics.

## 16. Specify the interaction contract

A specification should let another person implement the behavior without guessing at hidden states. Use the smallest artifact that exposes the important decisions: a flow for routes, a transition table for state, a prototype for timing or manipulation, and annotated components for reusable behavior.

Record these fields for a consequential interaction:

| Field | What to specify |
| --- | --- |
| Purpose and scope | User outcome, affected objects, prerequisites, and permission. |
| Trigger and input | Supported activation routes, gestures, shortcuts, and cancellation before commitment. |
| State and transition | Starting state, conditions, resulting state, and repeated or competing events. |
| Feedback | Visible response, status announcements, sensory reinforcement, and reduced-motion behavior. |
| Focus and navigation | Entry, travel, activation, exit, restoration, history, and scroll policy. |
| Persistence | Commit point, local/remote guarantees, drafts, refresh, offline behavior, and conflicts. |
| Recovery | Validation, failure, unknown outcome, retry, undo, interruption, and partial completion. |
| Adaptation and verification | Platform differences, constrained layouts, realistic content, and observable acceptance criteria. |

Keep shared rules in the component or design system. A feature specification should reference those rules and describe its differences. A design system needs behavioral contracts and combined states as well as tokens and screenshots. Review changes to those contracts for every consuming pattern they affect.

## 17. Work through a complete example

Consider a project owner inviting a colleague. The task has a recipient, access level, external consequence, and a possible ambiguous network result. The following is an illustrative web design.

The owner activates "Invite member." A named modal opens, explains the invitation, and focuses the labeled email field. The access level defaults to the least privilege appropriate to the product and remains visible. The primary action says "Send invitation"; before submission, Cancel leaves without sending. Once submitted, Close dismisses the surface while status remains available in the member list. The dialog follows the focus lifecycle in section 6.

| Starting state and event | Result and feedback | Continuation and recovery |
| --- | --- | --- |
| Editing; incomplete submission | Inline errors and an actionable error summary; values retained | Correct the relevant fields. No invitation has been sent. |
| Valid draft; submit | Pending state identifies the recipient; repeated send is blocked | Close and Escape return to the member list, where the pending invitation remains visible. The request continues. |
| Pending; server confirms | Show the invitation as sent and identify its access level | Offer a durable invitation status and revocation action if supported. Closing returns focus to the trigger or the new member entry when that is the logical next task. |
| Pending; known rejection | Explain the actual issue, such as an existing membership | Retain the draft and offer the relevant route to manage access. |
| Pending; response lost | Show "Checking invitation status" rather than success or definite failure | Reconcile using the original operation identity before enabling another send. |
| Editing; attempted dismissal | Preserve the draft or ask whether to discard when useful work would be lost | Canceling dismissal returns to the draft; discarding restores focus to the invoker. |

Acceptance criteria include sending exactly one invitation through pointer and keyboard routes, correcting errors without re-entry, distinguishing sent from pending, and recovering after a lost response without a duplicate. A screenshot of the open dialog proves none of those behaviors by itself.

## 18. Evaluate behavior in use

Test the uncertainty that could invalidate the design. A paper flow can reveal a missing decision; a realistic interactive prototype can reveal confusion about commitment; a production implementation is needed to verify semantics, input handling, latency, persistence, and assistive-technology behavior. Choose fidelity accordingly.

Walk critical journeys in both directions, including entry from a deep link and return after interruption. Exercise realistic long content, empty data, invalid input, slow or lost connections, partial permissions, repeated activation, and competing updates. Test the input routes and platform settings the product claims to support.

Observe intended users attempting meaningful tasks without step-by-step coaching. Look for misread labels, hesitation, repeated actions, lost orientation, and incorrect beliefs about completion. Include disabled people and relevant assistive-technology use. A heuristic review or automated check can identify defects, but cannot establish that people understand the task.

Measure success and error recovery alongside effort and satisfaction. For asynchronous work, distinguish time to acknowledge input from time to a confirmed result. Interpret abandonment and interaction counts in context: fewer actions can reflect efficiency, an omitted safeguard, or an unfinished task. Do not optimize engagement at the expense of the person's outcome.

Before delivery, confirm that:

- A person can discover the task, predict its scope, complete it, and recognize the result.
- Supported input routes work throughout, with meaningful focus and no stranded or trapped state.
- Navigation, dismissal, waiting, and interruption preserve the promised work and continuity.
- Failure, uncertainty, and partial completion have truthful feedback and usable recovery.
- Responsive and platform adaptations preserve capability and respect user settings.

Record a defect with its starting state, input, expected result, observed result, and consequence. Fix task blockers and data-loss risks before ornamental refinements, then verify the affected transitions again. A design is ready when its contract holds under realistic use, including the recovery paths people are likely to need.
