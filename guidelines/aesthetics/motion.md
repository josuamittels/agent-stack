---
name: motion-design
description: "Comprehensive motion and animation reference for perception, timing, spacing, easing, springs, gesture physics, choreography, expressive identity, transitions, patterns, accessibility, motion systems, implementation, and evaluation."
version: "0.2.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Apple"
  - "World Wide Web Consortium"
  - "MDN contributors"
  - "Emil Kowalski"
  - "Enrico Tartarotti"
  - "Google Material Design"
  - "IBM Carbon Design System"
  - "Aviad Shahar - Tendler"
  - "Frank Thomas"
  - "Ollie Johnston"
  - "Micah Bowers"
  - "Ngoc Minh"
  - "Jeffrey Heer"
  - "George G. Robertson"
  - "Motion"
  - "Rachel Andrew"
  - "Paul Lewis"
  - "Sam Thorogood"
type: reference
status: experimental
---

# Motion design

Motion makes change perceptible. It can show what caused an event, where something went, how objects relate, what remains available, and whether a system responded. It also gives a composition temperament: hesitant, precise, buoyant, severe, restless, ceremonial. The same endpoints can communicate different things through the movement between them.

Design that movement as part of the experience. An animation has an audience, a purpose, a temporal structure, a physical suggestion, and a cost in attention and time. A beautiful sequence can still interrupt work, misrepresent a result, or make someone uncomfortable. A direct state change can be the most considered motion decision.

Use this guide for interfaces, websites, identities, explanatory graphics, presentations, character accents, and spatial experiences. Product interaction supplies many examples because it exposes difficult constraints: unpredictable input, repetition, asynchronous results, interruption, and access. Linear storytelling permits different pacing and exaggeration. Keep those contexts distinct.

## Use this reference

This guide owns temporal composition, timing, easing, springs, trajectories, choreography, and animation lifecycle. Apply the shared [framework](reference.md) for decision priorities, requirements language, and evidence.

For UI, start with [1–2](#1-understand-why-motion-matters), [7–13](#7-choose-duration-and-response), and [16–23](#16-apply-interaction-patterns); verify with [26–27](#26-work-through-complete-examples). Use [14–15](#14-create-feeling-and-expressive-identity) for expressive and narrative sequences. [Interaction](interaction.md) defines behavior and state truth; [Accessibility](accessibility.md) defines access and control requirements; [Composition](composition.md) defines spatial endpoints.

## Contents

1. [Understand why motion matters](#1-understand-why-motion-matters)
2. [Write the motion brief](#2-write-the-motion-brief)
3. [Design for perception and expectation](#3-design-for-perception-and-expectation)
4. [Know the facets of motion](#4-know-the-facets-of-motion)
5. [Adapt animation principles](#5-adapt-animation-principles)
6. [Separate timing from spacing](#6-separate-timing-from-spacing)
7. [Choose duration and response](#7-choose-duration-and-response)
8. [Shape easing and timing functions](#8-shape-easing-and-timing-functions)
9. [Design with springs](#9-design-with-springs)
10. [Handle gestures, inertia, and constraints](#10-handle-gestures-inertia-and-constraints)
11. [Establish spatial grammar](#11-establish-spatial-grammar)
12. [Choose a transition structure](#12-choose-a-transition-structure)
13. [Choreograph groups and sequences](#13-choreograph-groups-and-sequences)
14. [Create feeling and expressive identity](#14-create-feeling-and-expressive-identity)
15. [Compose narrative and illustrative motion](#15-compose-narrative-and-illustrative-motion)
16. [Apply interaction patterns](#16-apply-interaction-patterns)
17. [Design scrolling and environmental motion](#17-design-scrolling-and-environmental-motion)
18. [Animate typography, symbols, and data](#18-animate-typography-symbols-and-data)
19. [Provide access and control](#19-provide-access-and-control)
20. [Build a motion system](#20-build-a-motion-system)
21. [Keep state correct through interruption](#21-keep-state-correct-through-interruption)
22. [Choose implementation mechanisms](#22-choose-implementation-mechanisms)
23. [Protect rendering and responsiveness](#23-protect-rendering-and-responsiveness)
24. [Adapt to devices and platforms](#24-adapt-to-devices-and-platforms)
25. [Specify and hand off](#25-specify-and-hand-off)
26. [Work through complete examples](#26-work-through-complete-examples)
27. [Review and diagnose](#27-review-and-diagnose)

For a component, start with its brief, transition, pattern, accessibility behavior, and interruption contract. For a design system, read the mechanics before choosing tokens. For a film or identity sequence, concentrate on perception, choreography, expression, narrative, and delivery. Use the diagnostic table when an animation feels wrong but the cause is unclear.

## 1. Understand why motion matters

### Give change a readable structure

A menu that expands from its trigger can establish ownership. A selected card that becomes a detail view can preserve identity. A panel that moves aside can reveal that another surface was already behind it. Motion supplies intermediate evidence that a cut omits.

Use it when that evidence matters. People can miss brief changes, lose an object among moving peers, or infer a relationship that the design never intended. Moving an unrelated advertisement into a shopping basket would suggest an addition even if no item was added. Movement carries claims about the world of the product.

| Job | What motion can establish | What must remain available without it |
| --- | --- | --- |
| Feedback | Input was received; a control changed state | A discernible state and appropriate programmatic feedback |
| Orientation | A destination, hierarchy, or persistent location | Navigation labels, structure, and a recoverable place |
| Continuity | An entity persists while its presentation changes | Stable identity and understandable before/after states |
| Explanation | Order, process, dependency, or transformation | A replayable or static explanation when needed |
| Attention | Something changed and deserves notice | A persistent indicator or accessible notification |
| Expression | Character, rhythm, material, or emotional emphasis | The content and task, even if the expressive layer is removed |
| Temporal feedback | Work is pending, progressing, complete, or failed | Truthful status, recovery, and control |

### Budget attention, repetition, and trust

Motion competes with reading, decision-making, conversation, and other movement. An effect that works once in a portfolio can exhaust someone processing hundreds of records. Judge a whole session, including idle time and repeated actions.

Do not infer conversion, trust, learning, or reduced cognitive load from polish alone. Those are outcomes to investigate in the intended task. Persistent, truthful state often establishes confidence more effectively than an elaborate confirmation. Never prolong processing, fake progress, or obscure failure to make a product seem more sophisticated.

### Decide when to leave a state change immediate

Default to immediate changes for focus indication, typing, high-frequency selection, urgent information, and tasks where the intermediate path adds no useful meaning. Brief supporting animation may remain if it does not delay perception or operation.

Animate when a reader needs to track a meaningful transformation, a person is manipulating an object, a change would otherwise be difficult to locate, or the brief calls for a deliberate expressive moment. “Everything should animate” is not a direction.

## 2. Write the motion brief

Describe the event before selecting a preset. State what changes, why the viewer should notice, and what they should understand or feel afterward.

| Decision | Specify |
| --- | --- |
| Audience and situation | Expertise, input methods, viewing conditions, frequency, likely competing attention |
| Meaning | Cause, affected entity, relationship, and final truth |
| Primary role | Feedback, orientation, explanation, atmosphere, expression, or a combination with a clear priority |
| Character | Two or three qualities translated into observable behavior |
| Temporal context | User-driven, time-driven, scroll-driven, sensor-driven, or data-driven; one-shot or repeated |
| Spatial model | Origin, destination, axis, depth, anchor, path, and persistent landmarks |
| Mechanics | Animated properties, curve or simulation, duration or settling rule, and coordination |
| Control | Cancellation, reversal, retargeting, skipping, replay, and pause |
| Alternatives | Reduced motion, unsupported platform, slow device, failed asset, and static output |
| Evidence | What the prototype must prove and how to inspect it |

A useful brief: “When a person opens a project inspector, reveal that it belongs to the selected project and occupies the trailing side of the workspace. Keep the project title stable, accept input as soon as the inspector is ready, and let repeated activation reverse its current movement. Character: precise and composed; short travel, no overshoot, no child cascade. Reduced motion changes the inspector state immediately.”

An unhelpful brief: “Make the panel smooth, premium, and delightful.” It leaves geometry, semantics, control, and tradeoffs unresolved.

For redesigns, inventory existing motion before adding any. Capture entry, exit, loading, success, failure, hover, keyboard, gestures, idle effects, and reduced-motion behavior. Keep established spatial meanings unless there is a clear reason to change them.

## 3. Design for perception and expectation

### Preserve identity and common fate

People can perceive objects moving together as a group. Use a shared trajectory, onset, and stable relationship to show that a heading, icon, and actions belong to one surface. Independent lag can imply loose attachment; independent direction can imply separate ownership.

Keep a recognizable feature during a meaningful transformation: a thumbnail, title, silhouette, or anchor. If every feature changes simultaneously, the viewer may see replacement rather than continuity. If two different entities are morphed together, they may appear to be the same entity. Preserve actual identity, not just a pleasing visual match.

### Make causality credible

A response near an action and close to it in time can imply that the action caused the response. Large delays, unrelated intermediate movement, or responses far from the trigger weaken that relationship. Show immediate local acknowledgment while slower work proceeds.

Do not confuse acknowledgment with success. A depressed button means the input was received; it does not mean the payment, upload, or permission change succeeded. Show those outcomes from actual application state.

### Keep attention within capacity

A viewer cannot carefully follow every moving object in a dense scene. Similar objects crossing paths, occluding each other, or changing several visual properties are especially difficult to track. Simplify paths, group related movement, preserve landmarks, and highlight the entity that matters. Use labels and persistent comparison when tracking is insufficient.

A moving element in peripheral vision can attract attention even when it is small. Avoid repeated shimmers, drifting backgrounds, and bouncing badges beside sustained reading or precise work. The useful question is how much competition the movement creates in context.

### Use physical expectations selectively

Acceleration, inertia, contact, gravity, resistance, and occlusion can make behavior legible. They need internal consistency. A rigid panel that stops with a soft landing can feel coherent; a panel whose text stretches like rubber while its border behaves like steel may not.

Physical plausibility is a design resource. Interfaces can act instantly, disappear, resize without conserving volume, or map time to scroll. Choose the simplifications that clarify the action. There is no need to simulate a drawer's full mass before showing a menu.

Apparent heaviness comes from the relationship among size, acceleration, braking, deformation, contact, sound, and context. Size alone does not establish mass. In real free fall, mass alone does not make a body fall more slowly.

### Distinguish object movement from self-movement

Large-field translation, zoom, rotation, parallax, and camera movement can suggest that the viewer is moving. A visually stationary body receiving strong visual movement can experience discomfort. User initiation does not guarantee comfort.

Keep a stable reference where possible, reduce unnecessary field coverage, and offer an alternative without simulated travel. There is no universal safe amplitude, duration, or oscillation frequency for every person and display.

## 4. Know the facets of motion

Specify motion across connected dimensions. A duration field alone describes very little.

| Facet | Questions and consequences |
| --- | --- |
| Translation and trajectory | Where does the object go? Is the path straight, curved, segmented, or constrained? |
| Scale and shape | Does it grow, deform, morph, or reveal more content? What remains rigid? |
| Rotation and orientation | Around which pivot and axis? Does orientation follow the path? |
| Appearance | How do opacity, color, stroke, light, texture, and blur change? |
| Depth and occlusion | What passes in front, behind, through, or out of view? |
| Timing and spacing | When does each phase occur, and how much change occurs within equal time intervals? |
| Dynamics | How do acceleration, damping, momentum, constraints, and external input govern movement? |
| Choreography | Which events coincide, overlap, lead, follow, or repeat? |
| Viewpoint | Is the object moving, the camera moving, or both? |
| Interaction | How does the sequence respond to a person changing their mind? |
| Character | What behavior makes this feel specific to the product or story? |
| Accessibility and delivery | What survives without movement, sound, fast rendering, or a particular input? |

A **transition** connects states. An **animation** is a change over time and may include many transitions, holds, loops, or simulations. A **microinteraction** is a small interaction with trigger, behavior, feedback, and subsequent state; its motion is only one part. A **motion system** defines reusable behavioral choices and their conditions.

A **timeline** maps events to time. A **state machine** maps allowed states and transitions. A **simulation** evolves from state and forces. A **progress mapping** connects an input such as scroll position to an output. Choose the model that matches the source of change.

## 5. Adapt animation principles

Classical principles help make action readable and expressive. Adapt each to the task; an interface should not inherit the delays or exaggeration of a character performance by default.

| Principle | Useful application | Boundary |
| --- | --- | --- |
| Staging | Give the decisive action a clear focal point, silhouette, and surrounding space | Do not make every element compete for the lead |
| Anticipation | Prepare an audience for a major narrative movement; preview a drag destination | Do not delay a button's response with a wind-up |
| Squash and stretch | Suggest elasticity, effort, impact, or a playful character | Keep labels, controls, and data legible; deform a container separately when appropriate |
| Slow in and slow out | Shape acceleration and arrival | Not every response needs a slow beginning; continuous activity may need constant speed |
| Arcs | Make organic gestures and paths feel directed | Do not add curved detours to ordinary navigation without purpose |
| Follow-through | Let an attached feature settle after a main action | Bound the tail; avoid a control that remains visually unstable |
| Overlapping action | Offset related parts to suggest articulation or attachment | Excessive lag can imply independent objects or a broken layout |
| Secondary action | Support the primary gesture with a smaller event | Keep it subordinate and optional |
| Timing | Establish pace, weight, emphasis, and relationships | Duration cannot rescue an unclear action |
| Exaggeration | Make a narrative idea readable or establish identity | Avoid false state, alarming errors, or coercive rewards |
| Pose-to-pose and straight-ahead | Plan key states, then refine the transitions; explore fluid movement by successive iteration | Preserve a reliable final state and delivery constraints |
| Solid construction and appeal | Maintain convincing volume, perspective, balance, and a readable personality | Appeal depends on audience and intent; it is not synonymous with cuteness |

Use **holds** deliberately. A pause before a reveal can build expectation; a pause after a result can let it register. In a working interface, persistent state often provides that reading time while leaving the person free to act.

## 6. Separate timing from spacing

**Timing** describes when an action starts, how long it takes, and when meaningful beats occur. **Spacing** describes the amount of visual change between successive samples. At a fixed sampling rate, wider spacing means higher speed.

These illustrative positions all travel 100 units in the same total time. Samples occur at equal time intervals:

```text
Time             0%    20%   40%   60%   80%   100%
Constant speed    0     20    40    60    80    100
Accelerating      0      4    16    36    64    100
Decelerating      0     36    64    84    96    100
Smoothstep        0   10.4  35.2  64.8  89.6    100
```

The endpoints and duration cannot tell you which version feels responsive or heavy. Inspect the intermediate positions. The last row uses `E(u) = 3u² − 2u³`; it starts and finishes with zero velocity, but its acceleration does not match stationary acceleration at both joins.

For a scalar value interpolated between `a` and `b`:

```text
u = clamp((t − t₀) / T, 0, 1)
x(t) = a + (b − a) E(u)
v(t) = (b − a) E′(u) / T
acceleration(t) = (b − a) E″(u) / T²
```

Here `T` is duration in seconds, and `E` maps normalized time to progress. The same curve traversing twice the distance in the same duration has twice the velocity. Halving duration doubles velocity and quadruples acceleration for the same displacement and curve. This explains why shortening an animation can make it harsh even when the easing is unchanged.

A curve plot usually shows **progress versus time**, not the object's spatial path. Slope describes progress velocity. A flat section is a hold. A negative slope means reversal. A curve exceeding progress `1` overshoots the target. The actual speed along a curved path also depends on how path position is parameterized; equal parameter steps do not guarantee equal path distance.

Do not equate more frames with longer duration without fixing playback rate. Twelve frames last 500ms at 24fps and 200ms at 60fps. Increasing display refresh should improve sampling of the same real-time trajectory, not change its speed.

### Control smoothness beyond velocity

**Jerk** is the rate of change of acceleration. A trajectory can have continuous position and velocity yet feel forceful at a join because acceleration changes abruptly. For a deliberately gentle, fixed-duration movement between resting states, a quintic progress curve such as `E(u) = 10u³ − 15u⁴ + 6u⁵` provides zero velocity and acceleration at both endpoints. It does not provide zero endpoint jerk, preserve arbitrary incoming velocity, or establish that the movement suits the task.

Do not treat minimum-jerk models of some human reaching movements as a universal law for interfaces. They are useful mechanical references, alongside springs and authored curves. Contact, impact, a crisp cut, and a playful snap can require different treatment.

## 7. Choose duration and response

### Separate the clocks

A component has several relevant times:

- **Input latency:** time from action to perceptible acknowledgment.
- **Availability:** time until the person can use the result.
- **Visual duration:** time allocated to the main visible transition.
- **Settling:** time until residual motion falls below the implementation's stopping thresholds.
- **Dwell:** time information remains available to read.
- **Total sequence:** delays, staggers, movement, holds, and tails combined.

Do not make availability depend on a decorative settling tail. A search field can receive input while its surface finishes appearing. Conversely, a control that moves away under a pointer can be technically enabled yet practically unusable.

### Establish a small duration vocabulary

The following is a proposed starting scale for ordinary screen interfaces, not a platform specification or perceptual threshold. Use existing platform/component behavior when appropriate.

| Example role | Starting range | Typical decision |
| --- | --- | --- |
| Immediate | 0ms | Focus, typing, urgent state, repeated expert action |
| Brief feedback | 80–140ms | Small state tint or press response |
| Local transition | 140–220ms | Small popover, selection indicator, compact reveal |
| Surface transition | 220–340ms | Panel, sheet, meaningful expansion |
| Large relationship | 300–450ms | Large shared-element movement requiring tracking |
| Expressive phrase | Brief-specific | A logo, celebration, illustration, or explanatory beat |

Start near the shorter end for frequent tasks and small travel. Increase time when distance, scale, or tracking complexity requires it; first reduce unnecessary movement. A long expressive sequence can be appropriate when viewing it is the chosen activity and skip/replay behavior is provided.

Do not scale duration directly with every viewport pixel. If using distance-based duration, define a bounded policy such as `T = clamp(Tmin, Tbase + αd, Tmax)` with explicit units and tuned limits. It is a product convention, not a physical law. Reassess across screen sizes.

### Shape perceived response honestly

Immediate acknowledgment plus an early useful result often feels more responsive than a delayed, perfectly synchronized reveal. A decelerating entrance shows much of the movement early; a long near-static tail can still make it feel unfinished.

For pending work, show actual status. Avoid flashing a spinner for already-completed work; a short indicator-show delay can prevent flicker, while acknowledgment remains immediate. If work finishes during that delay, reveal the result immediately. Do not hold a completed task merely to complete a spinner cycle or satisfy a minimum display duration.

For determinate work, bind progress to a meaningful quantity and label what it measures. Bytes uploaded are different from processing complete. If progress cannot be estimated, use a truthful indeterminate state with recovery when necessary.

## 8. Shape easing and timing functions

### Choose the curve by the behavior

| Curve family | Starting use | Inspect for |
| --- | --- | --- |
| Linear | Continuous rotation, a clock-like scan, direct mapping of known progress | Abrupt start/stop when attached to a finite movement |
| Decelerating / ease-out | Prompt response and a controlled arrival | Excessive initial jump or lingering final tail |
| Accelerating / ease-in | Departure that gains speed out of view | Sluggish acknowledgment; abrupt stop if still visible |
| Ease-in-out | A visible object moving between resting positions | A beginning too slow for an immediate response |
| Overshoot / back | A deliberately elastic or anticipatory accent | Values outside valid domains; unwanted reversal |
| Elastic / spring-like curve | A repeatable authored recoil in a fixed timeline | Fake continuity when interrupted |
| Steps | Sprite frames, held drawings, mechanical increments | Accidental flicker, unreadable text, wrong frame indexing |

An exit need not be ease-in. Use it when speeding away supports the spatial model. A nearby drawer returning to rest off-screen may use a symmetric or decelerating curve. A quick fade can end a transient element without implying travel. Preserve the semantic relationship, then choose the curve.

### Read cubic Bézier curves correctly

`cubic-bezier(x1, y1, x2, y2)` has fixed endpoints `(0,0)` and `(1,1)`. Its horizontal axis is input progress and vertical axis is output progress. In CSS, both x control coordinates must lie within `[0,1]`; y control coordinates can lie outside that interval. Out-of-range y values can create anticipation or overshoot, subject to the animated property's value handling.

The curve's internal parameter is not elapsed time. Evaluation finds the curve point corresponding to the requested x value and returns its y value. Setting control-point x coordinates differently can change the acceleration even with the same y coordinates.

Use endpoint slopes to reason about joins. A position curve with zero slope at the end can meet a stationary state without a velocity jump. That does not guarantee continuous acceleration or natural movement through an interruption.

Example semantic curves, offered as an original starter set:

```css
:root {
	--motion-ease-arrive: cubic-bezier(0.16, 1, 0.3, 1);
	--motion-ease-move: cubic-bezier(0.4, 0, 0.2, 1);
	--motion-ease-depart: cubic-bezier(0.4, 0, 1, 1);
	--motion-ease-constant: linear;
}
```

Built-in CSS `ease`, `ease-in`, `ease-out`, and `ease-in-out` are valid choices with fixed definitions. Prefer a custom curve when it serves a documented system need. Custom syntax alone does not improve quality.

### Distinguish `linear` from `linear()`

The keyword `linear` maps input to output at a constant rate. The `linear()` function joins specified progress stops with straight segments. It can describe a hold, an irregular speed profile, or a sampled spring-like trajectory:

```css
/* Illustrative authored overshoot, not a live spring simulation. */
.accent {
	animation-timing-function:
		linear(0, 0.7 30%, 1.04 60%, 0.99 80%, 1);
}
```

More samples can approximate a smooth curve more closely. This remains a fixed progress mapping: it does not automatically incorporate a new target or release velocity. Check support for the actual function in target browsers and provide a simpler fallback.

### Use steps and keyframe intervals intentionally

`steps(n, jump-end)` holds the first state until the first interval ends; `jump-start` makes an initial jump. `jump-none` omits endpoint jumps and requires at least two steps. `jump-both` includes both endpoints and changes the number of held intervals. Inspect the exact sequence rather than guessing from the step count.

For a ten-frame horizontal sprite strip, `steps(10, end)` can work when the animated background distance covers ten frame widths and the final out-of-range endpoint is not displayed. A strip animated only from the first to the last frame's origin requires a different interval calculation. Verify first, last, repeat, and pause frames.

In CSS keyframe animation, easing generally applies between relevant keyframes for each property. A timing function declared on a keyframe governs the interval leading from that keyframe to the next relevant one; a function on the final keyframe has no following interval to affect. A complex animation with several keyframes does not necessarily apply one global ease across the entire sequence. In the Web Animations API (WAAPI), effect easing maps progress across an iteration, while keyframe easing shapes the following keyframe interval. Inspect both when mixing them.

## 9. Design with springs

### Treat a spring as evolving state

A spring models attraction toward a target with inertia and damping. It can start at the current position and velocity, including a gesture release or an interrupted animation. A bouncy fixed easing curve only resembles one recorded trajectory.

For a one-dimensional, linear, viscously damped spring with fixed target `x*`:

```text
m x″ + c x′ + k(x − x*) = 0
natural angular frequency: ωₙ = √(k/m)
damping ratio:             ζ = c / (2√(km))
```

`m` is mass, `k` is stiffness, `c` is damping coefficient, and time is in seconds. In coherent abstract units, `k` has units of mass/time² and `c` has units of mass/time. Interface libraries may normalize mass, use a damping ratio instead of a coefficient, or expose duration/bounce controls. A parameter named `damping` is not enough to identify its meaning.

The passive model assumes `m > 0`, `k > 0`, and `c ≥ 0`; positive damping dissipates energy. Invalid coefficients or an unstable numerical solver can produce growing oscillation. A negative damping coefficient actively adds energy and is unsuitable as an ordinary settling preset.

| Parameter change | With other raw parameters fixed | Design implication |
| --- | --- | --- |
| Increase stiffness `k` | Raises natural frequency and lowers damping ratio | Faster oscillatory tendency, potentially more overshoot |
| Increase damping `c` | Raises damping ratio | Can suppress oscillation; excessive damping can slow approach |
| Increase mass `m` | Lowers natural frequency and lowers damping ratio | More inertia and a different oscillation/settling profile |
| Increase initial velocity toward target | Adds incoming momentum | Can overshoot even when a resting example does not |

Changing one raw parameter can change speed and damping behavior together. For controlled tuning, choose `ωₙ` and `ζ`, then derive `k = mωₙ²` and `c = 2ζmωₙ`.

### Choose a damping regime

- `ζ = 0`: no damping; an ideal displaced spring oscillates indefinitely.
- `0 < ζ < 1`: underdamped; oscillation decays around the target.
- `ζ = 1`: critically damped; no oscillatory mode.
- `ζ > 1`: overdamped; nonoscillatory behavior with a slower dominant mode than critical damping at the same natural frequency.

For a resting displacement and a fixed target, critical damping gives a useful fast approach without overshoot. Critical and overdamped systems can still cross the target under suitable initial velocity. “No bounce” in a demo from rest is not a guarantee for a high-speed gesture.

Default to no visible overshoot for text-heavy surfaces, precise controls, bounded values, and repeated work. Modest underdamping can suit a tactile release or a playful accent when the transient remains controllable. The object's function and context decide whether recoil helps.

### Understand the curve and its limits

For `0 < ζ < 1`, write displacement from a fixed target as `y = x − x*`:

```text
ωd = ωₙ √(1 − ζ²)
y(t) = e^(−ζωₙt) [A cos(ωd t) + B sin(ωd t)]
A = y₀
B = (v₀ + ζωₙy₀) / ωd
```

Initial displacement and velocity determine phase and amplitude. A retargeted spring can preserve both by making its current `x` and `v` the initial state for the new target. Acceleration may change when the target jumps; position and velocity continuity do not imply continuity of every derivative.

With zero initial velocity and a standard step change, the fractional peak overshoot is `exp(−πζ/√(1−ζ²))`. At `ζ = 0.8`, it is about 1.5% of the step distance. An approximate 2% settling-envelope heuristic is `Ts ≈ 4/(ζωₙ)` for a typical underdamped response. It is not an exact finish time and does not apply unchanged to arbitrary release velocity, critical/overdamped cases, moving targets, or every runtime's termination rule.

### Tune purpose, then parameters

1. Choose a valid target and property domain. Position can overshoot within permitted space; opacity and percentages often require bounded output.
2. Choose the amount of visible recoil, including zero, for the context.
3. Tune frequency for the intended response and travel. Do not add damping simply to make it faster.
4. Test from rest, with a fast release toward the target, with velocity away from it, and after reversal.
5. Define stopping thresholds and final-value commitment. Use both displacement and speed; passing near the target at high speed is not rest.
6. Coordinate companions by the visible main movement, while allowing a harmless spring tail when suitable.

Illustrative coefficient-based presets with `m = 1` and seconds as the time unit:

| Role | `ωₙ` | `ζ` | `k` | `c` | Intended starting behavior |
| --- | --- | --- | --- | --- | --- |
| Precise settle | 24 | 1 | 576 | 48 | Firm approach from rest without oscillation |
| Soft settle | 18 | 1 | 324 | 36 | More measured approach |
| Restrained recoil | 24 | 0.8 | 576 | 38.4 | Small overshoot from rest |

These are mathematical examples, not portable library configurations. Match trajectories, units, initial velocity conventions, and stopping rules before mapping them to an engine.

### Distinguish physical and perceptual duration

An ideal damped spring approaches rest asymptotically. A runtime stops when its chosen thresholds are met. Some tools expose a perceptual or visual duration that coordinates the main movement while the final tail lasts longer. Others force a spring-shaped trajectory into a specified duration.

Document which model the token uses. A spring called “300ms” is ambiguous without that definition. Do not use a small residual movement to block interaction or delay semantic completion.

## 10. Handle gestures, inertia, and constraints

### Keep direct manipulation direct

While dragging, map the primary object to the controlling pointer with minimal unnecessary lag. A spring follower may suit an ornamental shadow; applying it indiscriminately to the dragged object can make the object feel detached from the hand.

Use one coordinate space for input, bounds, and output. Account for scrolling, transforms, zoom, device density, and container movement. Capture the pointer when appropriate so the gesture can continue outside the initial hit area. Release capture and clear state on cancellation, not just pointer-up.

Provide discoverable buttons or keyboard actions for dragging, reordering, dismissal, and other operations. Gesture physics does not replace accessible operation.

### Hand off release velocity

Estimate release velocity over a short recent window in real time. A single noisy sample or an old average over the entire drag can misrepresent intent. Use the platform's gesture system when it provides appropriate velocity tracking.

Choose the destination from position, direction, velocity, allowed states, and the action's consequences. A quick flick can reach a neighboring destination even after short travel, but a tiny noisy movement should not dismiss a critical editor. Do not interpret speed without its sign and axis.

For a simplified exponential inertial model:

```text
v(t) = v₀ e^(−t/τ)
x(t) = x₀ + v₀τ(1 − e^(−t/τ))
projected unconstrained destination = x₀ + v₀τ
```

`τ` is a time constant in seconds. This model decelerates without a restoring target; it is different from a spring. Use the projected destination as one input to snapping, then enforce valid destinations. Do not assume it reproduces a platform's scrolling physics.

### Make resistance and boundaries coherent

Use increasing resistance to make an elastic boundary perceptible. Once released, return toward a valid state with the current velocity and the chosen constraint behavior. Define whether a boundary clamps, absorbs energy, rebounds, or permits temporary overflow.

Position continuity at contact matters, but not every collision needs velocity continuity: a deliberate impact changes velocity. Make the impulse credible and bounded. Haptics or sound can reinforce actual contact when appropriate; do not fire them from an arbitrary timer unrelated to the collision.

For snap points, define hysteresis so tiny input changes near a boundary do not alternate destinations. When the viewport or content changes, recompute valid points and reconcile the current state. Do not let an old pixel destination strand a sheet halfway off-screen.

## 11. Establish spatial grammar

### Decide where things live

Persistent surfaces need stable origins, destinations, and return behavior. A drawer can remain conceptually just outside the trailing edge. A child view can emerge from a parent. A transient toast can appear in an established notification region without pretending to originate from the clicked button.

Use logical directions for navigation where meaning follows reading order, and physical directions where the actual device or gesture determines the relationship. Right-to-left adaptation is not a blind inversion of every animation: chronological graphs, maps, media controls, and a panel attached to a physical edge need contextual decisions.

### Set the origin and anchor

A popover growing from its trigger suggests ownership; scaling from the screen center suggests a different relationship. Choose transform origin from the visual attachment, not the default center. Reposition and update that origin when collision avoidance changes the popover's side.

Keep a stable landmark through an expansion: one corner, an image center, a baseline, or a title. Animating both edges outward while also moving the whole surface can make its origin hard to read.

### Distinguish transformations

| Operation | What it suggests | Design caution |
| --- | --- | --- |
| Translation | One object changes location | Retain orientation and identity unless the action requires otherwise |
| Expansion | A surface contains or reveals more | Avoid stretching text and borders as if they were a photograph |
| Mask / reveal | Content already exists behind a boundary | Clip at a meaningful edge; keep hidden controls in the correct semantic state |
| Overlay | Another layer enters above the current context | Preserve background relationship and modality rules |
| Reparenting | An entity moves into a different container | Use stable identity and correct final ownership |
| Duplication | A source remains while a representation travels | Make it clear whether an item moved, copied, or was added |
| Morph | A form changes while identity continues | Do not morph unrelated entities into a false relationship |
| Parallax | Layers imply relative depth | Reserve for useful depth or intentional expression; reduce simulated self-motion |
| Camera zoom / dolly | Viewpoint or field of view changes | Preserve orientation; avoid unnecessary full-field motion |

Digital scale enlargement is not automatically a camera dolly. A dolly changes viewpoint position and can change perspective relationships; changing field of view changes magnification differently. Name the intended effect precisely enough to implement it consistently.

## 12. Choose a transition structure

| Structure | Use when | Main failure to prevent |
| --- | --- | --- |
| Cut | The relationship is clear or immediate access dominates | Losing a consequential change with no persistent indication |
| Crossfade | Replacement has no useful travel path | Double exposure and unreadable intermediate text |
| Directional move | Position conveys hierarchy, adjacency, or persistence | Contradictory directions and excessive travel |
| Container transform | The same entity changes presentation | Warped content, duplicate focus targets, false identity |
| Reveal or wipe | A boundary or progressive disclosure carries meaning | Concealed content remaining operable or permanently hidden |
| Shared element | One entity anchors two compositions | Matching by visual similarity rather than actual identity |
| Staged replacement | A complex change requires separate readable phases | Serial delays that obstruct work |
| Morphing shape | Shape transformation communicates a state or identity | Incompatible path topology, self-intersection, lost meaning |

Default to the simplest structure that communicates the relationship. Use a cut rather than a decorative crossfade when the overlap makes reading worse. For a shared-element transition, keep one clear anchor and allow unrelated content to change separately.

An exit and an entrance need not be literal reverse recordings. They should preserve the same world model and state relationship. An opening may establish context; a closing may be shorter because that context is already understood. Cancellation, completion, and deletion can require different final destinations even when their controls look similar.

Specify layering during the transition, not just at endpoints. Watch clipped shadows, content crossing above a fixed header, transparent surfaces revealing duplicate text, and outgoing controls remaining clickable. A snapshot used for transition imagery is not the live interactive component.

## 13. Choreograph groups and sequences

### Establish a lead and relationships

Choose one dominant action for a local moment. Other movement can accompany it, reinforce it, or prepare the next beat. Keep unchanged regions still. A stable shell gives moving content a reference and prevents the whole screen from seeming rebuilt.

Use simultaneous onset for a coherent group. Use a stagger when order, propagation, rhythm, or spatial relationship benefits from it. Use a sequence when one event genuinely depends on another being understood. Do not sequence independent operations just because a timeline editor makes it convenient.

### Bound stagger by total time

For `n` elements, item duration `D`, and start interval `s`:

```text
total duration = D + (n − 1)s
```

Eight items at `D = 180ms` and `s = 20ms` finish in `320ms`. Thirty items with the same values finish in `760ms`. A subtle per-item delay becomes a long queue.

Cap the spread, animate only the meaningful visible group, group items into regions, or remove the stagger. Base order on meaning and reading sequence. A radial wave from a user's contact point is appropriate only when that origin itself matters.

Do not hide primary content or a needed action until a decorative cascade ends. A list can be operable while its nonessential presentation finishes, provided targets and focus remain stable.

### Overlap without confusing causes

Outgoing secondary content can fade while the main surface changes geometry; new content can appear once there is enough room to read it. Keep those phases related to the central action. Avoid a blank interval unless absence itself communicates something.

Synchronize to perceived events. A landing, contact, release, or successful result is a meaningful cue for sound and haptics. Their waveform onsets may need tuning around the visual event on real hardware. Equal numeric start times alone do not establish perceived synchronization.

## 14. Create feeling and expressive identity

### Translate mood into behavior

“Vibe” is the cumulative impression of pacing, shape, spacing, rhythm, amplitude, material, repetition, and context. Express it as a set of choices that someone else can reproduce.

| Intended character | Candidate motion choices | Risk to check |
| --- | --- | --- |
| Precise | Prompt acknowledgment, restrained travel, clear endpoints, little recoil | Abruptness or emotional coldness in a sensitive moment |
| Composed | Stable anchors, measured transitions, clean pauses, few competing events | Slow access or excessive solemnity |
| Buoyant | Rounded acceleration, modest recoil, light follow-through | Toy-like behavior in serious or repeated tasks |
| Tactile | Clear contact, resistance, credible release, matching sensory accent | Decorative deformation detached from input |
| Energetic | Strong rhythmic contrast, decisive movement, selective exaggeration | Fatigue, alarm, and competition with content |
| Organic | Curved trajectories, articulated overlap, controlled asymmetry | Mushy control, random timing, inconsistent identity |
| Mechanical | Quantized steps, rigid attachment, consistent cadence | Unintended stutter or difficulty reading movement |
| Cinematic | Deliberate staging, viewpoint, depth, pacing, and held emphasis | Spectacle that withholds content or causes discomfort |

These are hypotheses for a brief, not universal psychological mappings. A slow movement can feel calm, heavy, ominous, or broken. A bounce can feel friendly, frivolous, unstable, or sarcastic. The event, surrounding design, prior experience, and culture change the interpretation.

### Design a family resemblance

Choose a small set of recurring behaviors: a characteristic arrival, a relationship between container and content, a way of settling, or a distinctive rhythm. Reuse the underlying idea across scales while adapting its amplitude and duration.

Separate everyday working motion from moments with permission to be expressive. A utility product can have a memorable launch illustration and quiet selection feedback. A playful product still needs decisive errors, stable controls, and a readable reduced-motion experience.

For a signature move, state its purpose, where it appears, how often it repeats, its maximum attention demand, and its quiet alternative. Distinctiveness does not require every surface to repeat the signature.

### Use contrast and restraint

Movement feels more pronounced against stillness. A small acceleration change can carry more character than adding rotation, blur, scale, color, and sound together. Tune one influential variable at a time while comparing candidates; then judge the combined composition.

Avoid substituting duration for emotion. A dignified interaction may be immediate and clear. A joyful one may use one small rebound. The visual language, content, and outcome must support the feeling.

### Keep expression ethically aligned

Celebrate an achievement when the person would reasonably experience it as one. Avoid rewarding repeated spending, risky decisions, accidental actions, or compulsive activity with escalating sensory reinforcement. Do not use motion to draw attention away from costs, errors, or consent choices.

An error can be kind and clear without a comic shake. Motion should not humiliate a person for entering the wrong value. Provide understandable correction and preserve their work.

## 15. Compose narrative and illustrative motion

### Build beats before keyframes

For a linear explanation or identity sequence, define the idea, audience, viewing context, and desired progression. Sketch the key states, then place them in an animatic: a rough timed sequence that tests reading order and pace before detailed production.

A useful phrase has preparation, action, consequence, and enough time to register. Not every phrase needs all four as separate beats. Use anticipation when it improves comprehension, a decisive action when it carries the idea, and a hold when the audience needs to inspect the result.

For an explanation, preserve the causal order of the actual process. Do not imply that a later result causes an earlier step because it makes a better transition. Separate simultaneous activity from sequential activity when that distinction matters.

### Shape rhythm across scales

Work at frame, gesture, phrase, scene, and sequence scales. Local polish cannot rescue a sequence with no contrast. Alternate movement and stillness, dense and sparse scenes, fast actions and readable holds. Repeated equal-length beats can establish a deliberate machine rhythm; otherwise they often flatten emphasis.

A loop needs a coherent seam in position, velocity, appearance, and sound where continuity is intended. A deliberate reset can also work when it is readable. Check the first playback as well as repeated playback: the initial state may not have the context provided by the preceding loop.

### Choose stylization deliberately

Held drawings, stepped motion, smears, motion blur, shape exaggeration, and imperfect paths can establish a specific graphic voice. Stepped artwork does not justify dropping input updates or rendering frames in a live interface. Keep user-controlled movement responsive even if an accompanying character uses a limited animation cadence.

Motion blur can help depict fast movement but can also obscure text, precise boundaries, and state. Do not use blur to conceal an unreadable path or poor rendering. Camera motion and object motion should reinforce the same spatial model unless disorientation is an intentional, consented narrative goal.

### Coordinate image, type, and audio

Use a score or sound cue to support the structure; avoid forcing every visible movement onto a beat. A quiet visual event may need space around a loud cue. Speech and captions need reading time and should remain legible while other elements move.

If narration is necessary to understand the sequence, provide an appropriate text or media alternative. For process learning, add pause, replay, scrubbing, or step-by-step states as appropriate. A transient movie should not be the only way to compare complex states.

### Deliver for the actual medium

Specify resolution, aspect ratio, frame rate, duration, color handling, alpha requirements, looping, sound, captions, and safe placement of essential content. Test the exported file in its actual player. A correct project timeline does not establish correct encoding, alpha edges, autoplay, looping, or color on delivery.

For interactive vector or animation assets, verify supported effects and target renderer behavior. Keep essential controls and meaningful text in accessible native or DOM structures when an asset renderer cannot represent them. Provide a useful poster or final frame when playback fails.

## 16. Apply interaction patterns

Read [Interaction](interaction.md#4-choose-controls-by-meaning) for control behavior, [focus lifecycle](interaction.md#6-design-focus-and-selection), [feedback](interaction.md#11-communicate-response-and-progress), and [asynchronous truth](interaction.md#12-keep-asynchronous-work-trustworthy). Animate that contract without redefining it.

| Pattern | Motion decision | Constraint on the transition |
| --- | --- | --- |
| Press, hover, focus | Immediate state; optional restrained local response | Keep the target stable and focus legible from its first frame. |
| Popover, menu, dialog, sheet | Cut or short reveal from a meaningful origin | Entry must not delay operation; interrupted exit must reconcile correctly. |
| Accordion | Optional expansion of the owned region | Recompute for content growth and keep the final layout valid without animation. |
| Tabs | Immediate content change; optional local indicator movement | Selection must not wait for the indicator. |
| Navigation | Connect meaningful source/destination anchors or use a cut | Do not imply shared identity between unrelated entities. |
| Reorder | Direct tracking; peers make space | Reduce crossing paths; preserve the moving object's identity. |
| Add, copy, move, remove | Explain the actual source and destination; optionally close a gap | Reversal and undo must retarget or replace presentation safely. |
| Loading | Static placeholder by default; optional bounded activity | A shimmer or loop is activity, not measured progress. |
| Success, error, notification | Optional local accent around a stable outcome | The message and recovery route remain after the movement ends. |
| Live update | Local highlight followed by rest | Avoid continuous reflow and moving inspection targets. |

Reserve final geometry where useful. Tune the presentation for the whole state family rather than polishing only the success transition. Keep state ownership and recovery in the interaction contract; motion owns the transition between its valid endpoints.

## 17. Design scrolling and environmental motion

### Keep scrolling under the person's control

Default to platform scrolling. Avoid intercepting wheel or touch input to replace normal scrolling with a slow scripted camera unless the chosen experience explicitly depends on that interaction and an ordinary path remains available.

Distinguish a **scroll-triggered** animation, which starts a time-based sequence at a threshold, from a **scroll-driven** animation, whose progress maps to scroll position. A scrubbed sequence must work backward, during rapid jumps, on restored scroll positions, and when the viewport changes.

Do not run a long entrance every time an element crosses the threshold by one pixel. Use clear replay policy and hysteresis. Anchor links, Find in Page, keyboard scrolling, Back, and direct links must still lead to useful content.

### Use depth and camera effects sparingly

Parallax, pinning, full-screen zoom, and video scrubbing can suit an opted-in narrative. Keep essential text and controls usable independent of the effect. Plan mobile composition and reduced motion at the same time as the main treatment.

A pinned section should communicate how to leave it and should not trap keyboard focus or cover later content. Long blank scroll distances need a content reason. Avoid tying the visibility of essential content solely to a precise scroll interval or successful script execution.

### Bound ambient and looping effects

Environmental motion includes gradients, particles, noise, waves, marquees, cursor trails, and breathing or pulsing objects. Its job can be atmosphere or identity, but it consumes attention, energy, and rendering resources while the person does something else.

Default to stillness during work and reading. If a background moves, keep it subordinate, provide required controls, and suspend it when off-screen or the document is hidden. An element outside the viewport is not automatically free to render. Remove autonomous camera-like motion in the reduced-motion alternative.

Do not replace the system pointer or make a decorative follower obscure the target. Touch, keyboard, stylus, and reduced-motion paths need no imitation of pointer ornament.

## 18. Animate typography, symbols, and data

### Keep language readable

Use [Typography’s shaping and language guidance](typography.md#22-compose-across-languages-and-scripts) and [Accessibility’s semantic requirements](accessibility.md#8-make-structure-and-meaning-programmatic) before fragmenting text.

Animate meaningful units such as a phrase or heading. Character-level choreography changes reading rhythm and needs a content reason. Avoid scaling body text through long transitions: move a container or separate the background transformation from final text layout. If text states crossfade, limit overlap and preserve readable endpoints. Do not blur an important label immediately before activation.

### Give symbols coherent topology

A symbol can rotate, draw, fill, morph, or exchange parts. Preserve a stable optical center and a clear meaning at the final state. Check stroke widths, caps, corners, and alignment throughout a morph.

Path morphing requires compatible or normalized geometry in the chosen renderer. Equal command counts alone do not guarantee useful correspondence: point order, winding, subpaths, holes, and open/closed topology matter. Crossfade or replace a symbol when a forced morph creates knots or misleading intermediate forms.

A continuously rotating activity symbol can use linear timing so it does not appear to hesitate each cycle. A determinate ring must represent actual progress and preserve a text/programmatic value independently of its rotation or stroke animation.

### Preserve data truth

Animate a chart to explain a transformation, maintain a small number of meaningful correspondences, or show a specific change. Do not assume a moving chart is easier to understand. Animation is transient and can make exact comparison harder; provide stable labels, reference states, small multiples, or direct before/after views when comparison is the task.

Preserve identity with stable keys. Do not make one category become another merely because they occupy the same row index. If sorting and values change together, consider separating those changes or highlighting a selected entity. Never overshoot an actual numeric value with a decorative spring unless the temporary visual is clearly non-data and cannot mislead.

Avoid counting from zero on every metric appearance. It temporarily shows false values and delays access to the number. If an explanatory counter is appropriate, expose the final value accessibly and keep announcements from firing on every frame. Use limited, meaningful status announcements rather than a stream of changing digits.

For a live chart, bound update frequency and preserve inspection. People need to pause, select, compare, and read a tooltip without the target escaping beneath them.

## 19. Provide access and control

### Make the alternative equivalent in meaning

Reduced motion is a different presentation of the same state and operation. Replace unnecessary travel, zoom, parallax, rotation, oscillation, and spatial morphs with an immediate change or a restrained nonspatial alternative. A short fade can be suitable, but it is not automatically comfortable or required.

Do not merely accelerate the same large movement: a fast zoom can remain disorienting. Preserve input, focus, status, navigation, and outcome. If movement itself teaches a process, supply an understandable static sequence, labeled steps, or controllable playback rather than removing the explanation.

Honor the operating system's preference and consider an explicit in-product setting for motion-rich experiences. With settings such as System, Reduced, and Full, define precedence; default to System and keep a deliberate Reduced choice. Listen for preference changes while the experience is open. Pause or reconcile active effects when a setting changes.

Absence of a reduced-motion preference does not mean someone welcomes intense motion. Keep default movement considerate and allow control over substantial autonomous effects.

### Apply the right requirement

Apply [Accessibility’s motion, automatic-content, flashing, and timing requirements](accessibility.md#16-control-motion-time-and-interruption), [semantic visibility](accessibility.md#hide-only-the-right-things), and [Interaction’s focus lifecycle](interaction.md#specify-the-focus-lifecycle). Reduced-motion presentation and pause/stop controls answer different requirements; implement the ones the effect needs.

During animation, opacity, geometry, hit testing, focusability, and semantic exposure can disagree. A transformed element keeps its document order; an invisible element may still be interactive. Reconcile these properties with the declared state at entry, interruption, exit, and immediate completion. Decorative clones must not become duplicate controls.

### Prefer targeted opt-in animation

Keep the base experience usable and add nonessential motion when the preference permits it:

```css
/* The component's existing semantics and visibility behavior still apply. */
.inspector {
	opacity: 1;
	transform: none;
}

@media (prefers-reduced-motion: no-preference) {
	.inspector[data-entering="true"] {
		animation: inspector-arrive 220ms var(--motion-ease-arrive);
	}
}

@keyframes inspector-arrive {
	from { opacity: 0; transform: translateY(8px); }
	to { opacity: 1; transform: none; }
}
```

This is an entry-style example, not a complete inspector implementation. It assumes the arrival curve from section 8 and a component lifecycle that manages state independently of animation events. Without animation support, the final content remains visible.

Avoid global `* { animation-duration: 0.01ms !important; }` as the primary policy. It can leave large travel intact, trigger event-dependent bugs, damage essential media, and obscure which behaviors need alternatives. Define component-level behavior and make zero-duration completion a supported path.

## 20. Build a motion system

### Separate foundations, roles, and recipes

A system needs enough structure to create consistency without forcing every action into one gesture.

1. **Principles:** purpose, character, control, accessibility, and performance boundaries.
2. **Foundations:** durations, curve definitions, spring models, distance units, and supported properties.
3. **Semantic roles:** feedback, arrival, movement, departure, direct manipulation, and expressive accent.
4. **Recipes:** component transitions with states, properties, origins, coordination, and alternatives.
5. **Composition:** rules for coordinating recipes across a screen or sequence.
6. **Evidence and governance:** examples, owning components, versioning, exceptions, and checks.

Token names should describe use or stable behavior. `motion.duration.surface` communicates more than `duration7`; a duration scale can still exist beneath semantic aliases. Do not hide incompatible engines behind the same numeric token without an adapter contract.

### Keep time-based and physical models distinct

An illustrative, framework-neutral token structure:

```yaml
motion:
  duration:
    feedback: { value: 100, unit: ms }
    local: { value: 180, unit: ms }
    surface: { value: 280, unit: ms }
  easing:
    arrive: [0.16, 1, 0.3, 1]
    move: [0.4, 0, 0.2, 1]
    depart: [0.4, 0, 1, 1]
  spring:
    precise:
      model: linear-viscous
      timeUnit: s
      mass: 1
      stiffness: 576
      dampingCoefficient: 48
  policy:
    reducedMotion: immediate-state-with-equivalent-feedback
    background: suspend-nonessential-loops
```

This schema is an example, not an existing interchange standard. A real system must define distance and velocity units, stopping thresholds, property-domain handling, and implementation mappings. Native and web platforms can share semantic roles while retaining different tuned parameters.

Use separate handling for spatial properties and bounded appearance properties. A spring suitable for movement can overshoot a color channel or opacity in ways that clamp awkwardly. Use monotone timing or an appropriately bounded model for those values.

### Document recipes beyond tokens

A panel recipe should specify opening, closing, interruption, resizing, content changes, focus, reduced motion, and initial rendering. A single video of its opening leaves most of the behavior undefined.

Document variants by context: compact versus full-screen, touch versus keyboard, frequent versus occasional, and working versus expressive. Reuse semantic meaning even when geometry differs. Avoid adding an unrelated curve for every small exception; first ask whether a component is using the wrong role.

### Maintain the system

Assign owners for foundational changes and component recipes. Review a token change on representative transitions at small and large distances, under repeated use and reduced motion. A global duration change can alter hover feedback, navigation, and dense-list choreography differently.

Record exceptions with their use case and limits. Deprecate old recipes when replacements exist, and keep compatibility mappings explicit. A motion gallery should include failure, cancellation, rapid input, and accessibility states, not only polished happy-path loops.

## 21. Keep state correct through interruption

### Let application truth own the result

Animation presents state; it must not be the sole source of state. A task's completion, a menu's expanded value, a dialog's modality, or a deletion must not depend on reaching a decorative keyframe.

Model meaningful states explicitly. For a surface, `closed → opening → open → closing` may describe presentation while a separate desired state says whether it should be open. Repeated input changes the desired state; the renderer reconciles from its current presentation.

Choose concurrency behavior per operation:

| Policy | Appropriate use | Main caution |
| --- | --- | --- |
| Retarget | Panel position, selection indicator, gesture settling | Preserve current position and velocity where meaningful |
| Replace / latest wins | Search preview, transient visual feedback | Discard stale results and callbacks |
| Queue | A story sequence whose order carries meaning | Bound the queue; avoid accumulated interaction delay |
| Accumulate | Multiple notifications or independent additions | Keep identity and attention limits |
| Lock temporarily | An operation that truly cannot be reentered safely | Explain actual busy state; never lock merely for visual polish |

### Define continuity deliberately

- **Position continuity:** the object does not jump to a different value.
- **Velocity continuity:** movement does not suddenly change speed or direction at an ordinary handoff.
- **Acceleration continuity:** force changes do not produce an abrupt acceleration jump.

Use the continuity needed by the event. A spring retarget can preserve position and velocity. An impact may deliberately change velocity. A cut intentionally removes trajectory. A cubic interpolator can also be designed with velocity-aware boundary conditions; springs are not the only mathematical way to preserve continuity.

Do not restart an interrupted movement from its original keyframe. Sample the actual current presentation, or use a renderer that manages that state correctly. Reversing playback is useful only when the recorded path and current state fit the intended reverse action.

### Guard completion and cleanup

When a closing surface is reopened, the obsolete closing completion must not remove the reopened surface. Use an operation/version token or cancellation mechanism so only the current transition can commit presentation cleanup.

Cleanup must also work when animation is disabled, interrupted, unsupported, or canceled by unmounting. Avoid relying only on `transitionend`: it may not fire when a transition is removed or does not run. Filter relevant properties and targets when using events, and provide deterministic immediate/finalization paths.

Dispose of observers, frame loops, subscriptions, pointer capture, timers, temporary layers, and cloned imagery. Stop repeating effects on unmount, hidden-document transitions, or policy changes. On resume, reconcile with real current state rather than replaying stale elapsed frames.

### Handle geometry changes mid-flight

Rotation, responsive layout, browser zoom, text scaling, localization, late images, and changing data can invalidate the destination. Recompute from stable identity and current geometry. Decide whether to retarget, finish immediately, or restart a harmless local presentation.

A pixel coordinate captured before scrolling is not automatically valid after scrolling. A list item's index is not its identity. Stable models prevent visually polished transitions from connecting the wrong entities.

## 22. Choose implementation mechanisms

| Mechanism | Good fit | Limits to resolve |
| --- | --- | --- |
| CSS transition | A small set of declarative state changes | Explicit properties; lifecycle semantics; retargeting behavior |
| CSS keyframes | Authored sequences, loops, held steps | Cancellation, replay, hidden states, accessibility policy |
| Web Animations API | Imperative playback, timing control, coordinated effects | Current styles, canceled promises, cleanup, final state ownership |
| Runtime spring / animation library | Retargeting, gestures, layout orchestration | Units, model precedence, dependencies, platform behavior |
| View transitions | Visual continuity across DOM or route changes | Snapshot identity, focus, navigation, browser fallback |
| Scroll-driven animation | Nonessential mapping from scroll to progress | Unsupported browsers, reverse/jump behavior, accessible content |
| Native animation system | Platform components and integrated gestures | Platform-specific lifecycle, accessibility settings, and presets |
| SVG / vector asset | Path/stroke animation, scalable illustration | Renderer capability, topology, text semantics, cost |
| Canvas / WebGL | Dense graphical scenes and effects | Input semantics, accessible equivalents, resources, context loss |
| Video / raster sequence | Fixed narrative with predictable imagery | File size, decoding, captions, poster, playback control, responsiveness |

Choose the smallest mechanism that supports the needed behavior. A library is justified by orchestration or interaction complexity, not by the existence of a fade. Do not use CSS-versus-JavaScript ideology as a performance test: properties, scheduling, and rendering work determine cost.

Name the properties to transition instead of using `transition: all`. An unrelated layout, color, or visibility change should not acquire motion accidentally. Keep transform composition explicit: translation followed by rotation can produce a different trajectory from rotation followed by translation. Separate layers when one effect must not overwrite another effect's transform.

### Animate layout without distorting meaning

Layout animation can explain expansion or reordering, but changing geometry can trigger repeated layout and paint. Transforming a visual layer can avoid some of that cost while leaving layout unchanged. The correct choice depends on whether surrounding content must actually move during the transition.

The FLIP technique measures **First** and **Last** geometry, **Inverts** the visual difference with a transform, then **Plays** that transform to its final identity. Batch measurements and writes, use stable entity matching, and check transformed ancestors and scroll offsets.

Scaling a container also scales text, corners, borders, and shadows unless compensated or separated. Use nested layers, a background-only transform, clipping, or measured layout movement where appropriate. A performant rubbery label is still a poor result.

### Protect initial content and fallback

Server rendering and hydration must agree on meaningful initial state. Do not deliver essential content at zero opacity and depend on a successful observer, script, or animation library to reveal it. Use progressive enhancement and reconcile restored scroll positions.

If the browser lacks a transition API, perform the actual state change. If an animation asset fails, show the content or useful final frame. Route changes, focus, announcements, and form outcomes must remain correct without decorative playback.

### Keep a clear final state

Animation fill behavior can keep a visual style after playback, but it does not replace committed component state. Avoid stacks of completed animations holding obsolete styles. Commit the intended base style and dispose of temporary effects according to the mechanism's documented behavior.

When using JavaScript, handle cancellation separately from completion. A rejected animation promise is not automatically an application failure; it can be the expected result of retargeting or unmounting.

## 23. Protect rendering and responsiveness

### Use frame time as a budget

A 60Hz display has about 16.7ms per refresh; 120Hz has about 8.3ms. Those intervals include more than the animation callback: input, application logic, style, layout, paint, compositing, and other work share the pipeline. Variable refresh and power modes change the situation.

Use elapsed time rather than incrementing position once per frame. A fixed “move 5px each callback” changes speed with refresh rate and dropped frames. For a custom numerical solver, use stable integration, bounded steps or an appropriate fixed-step accumulator, and a policy for long pauses. Prefer a tested analytical or platform solver when available.

`requestAnimationFrame` schedules around rendering; it does not guarantee a particular rate, free main-thread time, or automatic suspension of every related resource. A background fetch, worker, timer, or media decoder can continue independently.

### Minimize expensive work

Default to transform and opacity when they express the intended change. They are often well optimized, but compositor execution is not guaranteed in every composition. Large translucent layers, masks, filters, blend modes, and blur can still cost substantial rasterization, memory, and compositing work.

Avoid interleaving layout reads with writes across many elements. Measure together, calculate, then update together. Keep application rerenders and data processing out of per-frame paths when they do not need to run there.

Use `will-change` only when profiling identifies a benefit, scope it to the relevant properties and period, and remove it afterward when appropriate. Promoting every element to a layer can waste memory and worsen rendering. Adding `translateZ(0)` is not a general repair.

### Profile the actual interaction

Inspect a performance trace while opening, scrolling, dragging, interrupting, and loading representative content. Look for long tasks, missed refresh opportunities, paint area, expensive effects, memory growth, and input latency. A high average frame rate can conceal a stutter at the decisive contact or first opening.

Test with realistic CPU/GPU pressure, large lists, slow assets, and an ordinary target device. Emulator smoothness is insufficient evidence for touch feel, power use, or high-refresh behavior. Separate a deliberate stepped-art cadence from unintended renderer stalls.

If performance is poor, first remove unnecessary visual work, reduce moving area or count, simplify effects, and shorten orchestration. Do not preserve a costly effect merely by hiding the resulting delay behind another animation.

## 24. Adapt to devices and platforms

Use established platform components and gestures when they suit the product. They often include tuned motion, interruption, accessibility, and input behavior. Do not layer a second custom animation over the same component without understanding the combined result.

| Context | Adaptation |
| --- | --- |
| Desktop / expert tools | Prioritize immediate keyboard response, stable targets, repeated-use restraint, and dense-workspace clarity |
| Touch devices | Test finger tracking, occlusion, release velocity, cancellation, scrolling conflicts, and reachable controls |
| Stylus and drawing | Preserve low-latency marks and accurate coordinates; ornament must not lag the primary stroke |
| Wearables | Keep glanceable states; reduce waiting, persistent loops, power use, and attention demand |
| Television / remote | Make focus changes unmistakable; avoid large distracting camera moves; test from viewing distance |
| Foldable or resizable surfaces | Preserve identity across geometry changes; adapt from current dimensions rather than replaying a fixed movie |
| Spatial / immersive experiences | Keep stable references, avoid unnecessary world movement and peripheral animation, provide low-motion navigation |
| Presentations / signage | Check viewing distance, passive audience, looping duration, required controls, captioning, and static alternatives |
| Exported film / identity asset | Fix playback cadence and output format; judge the encoded result in its actual setting |

A phone's pixel distance, a desktop window's distance, and a spatial object's angular movement are not interchangeable. Match perceived scale and role, then test. Respect platform motion preferences in addition to the web query when building native software.

In immersive contexts, avoid assuming that putting motion behind a user-initiated gesture makes it safe. Do not animate the whole world rotating merely to change direction. Offer alternatives such as a brief fade and repositioning when appropriate to the experience. Keep important content stable enough to inspect.

## 25. Specify and hand off

An executable specification describes what happens under actual conditions. Include a prototype or recording for intended appearance, but keep the behavioral contract in inspectable text.

| Field | Required content |
| --- | --- |
| Identity and purpose | Pattern name, entity, role, and intended character |
| Trigger and state | Initial state, action/data event, pending state, and final truth |
| Geometry | Origin, anchor, path, bounds, depth, clipping, and responsive rules |
| Properties | Exact start/end values or formulas and units; separate content and container |
| Timing/model | Duration and easing, or solver parameters and initial state; define visual/settling meaning |
| Coordination | Delays, overlaps, dependencies, stagger order, and total sequence |
| Interaction | When targets become usable; pointer, touch, keyboard, and alternative operation |
| Interruption | Retarget, replace, cancel, reverse, queue, and stale-callback handling |
| Accessibility | Reduced motion, focus, semantic visibility, announcements, pause/skip/replay, and nonmotion meaning |
| Runtime | Mechanism, supported platforms, resource cleanup, hidden/off-screen behavior, and fallback |
| Acceptance | Observable success/failure conditions and inspection method |

For authored media, add export settings, captions, sound mix, alpha, poster, looping, and player behavior. For reusable interactive assets, add renderer/version assumptions and supported property controls.

Record units explicitly: milliseconds versus seconds, pixels versus logical points, coefficient versus damping ratio, absolute versus normalized velocity. A handoff that says “spring 0.8, speed 300” cannot be implemented reliably.

A timeline is useful for fixed coordination. A state diagram is useful for interruption and asynchronous outcomes. Use both when each resolves a different question; neither replaces the other's contract.

## 26. Work through complete examples

### A. A command palette for repeated work

**Brief:** open a search surface many times per session; precise, immediate, predictable.

Use a well-implemented dialog or command surface. On the shortcut, update open state and place focus in the ready search field immediately. Default to a cut or a very brief appearance change; avoid a large scale/blur entrance and child cascade. The background can dim briefly if it clarifies modality without delaying input.

Typing during entry must reach the field. Escape closes the surface. Reopening during exit reverses or replaces presentation from its current state; an obsolete exit must not remove it. Restore focus to the relevant previous control on dismissal. Reduced motion uses immediate appearance and dismissal with the same behavior.

**Verify:** open, type immediately, navigate results, activate, reopen, close, and reopen rapidly. Confirm no lost keystrokes, duplicate shortcuts, delayed focus, or stale exit. Repeated use should feel as clear as the first opening.

### B. A draggable bottom sheet

**Brief:** show contextual details with direct touch control; tactile but composed.

Choose valid closed, partial, and expanded positions from actual viewport and content geometry. While dragging, the sheet follows input directly; a backdrop may map to sheet position with bounded opacity. At release, select a valid destination using position and signed velocity, then settle from the current position and velocity. Start from a critically damped or restrained-recoil model and tune on device.

Define out-of-bounds resistance and cancellation. A fast upward gesture near the lower snap should not be mistaken for dismissal. A visible close button and keyboard-operable actions provide alternatives. Modality and focus depend on whether the sheet is modal, not on how much backdrop is currently visible.

When rotation or text scaling changes bounds, reconcile to a valid snap. Reduced motion preserves direct manipulation if needed for the operation but removes nonessential recoil and uses a direct final snap on release; buttons provide the same destinations without dragging.

**Verify:** slow drag, flick both ways, release near each decision boundary, cancel the pointer, close while settling, reopen, resize, use keyboard alternatives, and change the motion preference mid-settle. Confirm the sheet never rests at an invalid coordinate.

### C. A card opening into a detail view

**Brief:** preserve the identity of one project while giving it more space.

Use the project's stable ID to connect source and destination. Select the thumbnail and title as recognizable anchors. Measure geometry, then animate the container or transition imagery while keeping live destination text laid out at its final size. Fade unrelated metadata independently if needed. A surface transition around the illustrative 280ms role is a starting point; reduce travel or use a cut if the mapping becomes difficult to follow.

Do not stretch the body copy or expose duplicate links to assistive technology. Make the destination operable when ready, update navigation/focus correctly, and maintain Back behavior. If the source card no longer exists on return, use a simple replacement rather than flying to an unrelated card. Reduced motion uses direct navigation with equivalent orientation through title and location.

**Verify:** filtering or reordering the source list, long titles, delayed images, viewport changes, rapid Back, missing source, and reduced motion. Correct entity correspondence matters more than an uninterrupted visual illusion.

### D. An upload with unknown processing time

**Brief:** establish immediate receipt, truthful progress, and recoverable outcomes.

On file selection, show the file identity and pending state without waiting for a reveal. If byte progress is available, display upload percentage; label subsequent server processing separately. An indeterminate processing indicator may move, but its activity does not pretend to estimate remaining time. A static status works in reduced motion.

On success, show the confirmed file and a persistent completion label; an optional small check accent can finish independently. On failure, retain identity and provide retry or cancel. Never display success merely because the progress animation reached its final frame. Do not delay a fast result so the indicator can look busy.

**Verify:** instant completion, slow upload, stalled progress, processing delay, failure, retry, cancellation, leaving and returning, and preference changes. Confirm announcements describe meaningful state changes rather than every percentage sample.

### E. A buoyant identity sting

**Brief:** a short, optional brand moment for a creative product; energetic, elastic, recognizable.

Sketch three poses: compressed preparation, decisive release, and recognizable final mark. Keep the mark's final silhouette readable. Use one controlled overshoot and a shorter secondary follow-through rather than sustained wobbling. Choose the phrase duration from the intended placement and reading time; ordinary component durations do not define a film phrase.

Align a subtle sound accent with the perceived release or landing when sound is appropriate. Provide a quiet poster/final mark and an accessible label. Avoid replaying the sting on every navigation. For autoplay alongside content, meet control requirements; for an explicit replay, keep the control accessible.

**Verify:** first playback, loop seam if applicable, muted playback, reduced motion, the exported file, small and large rendering, and the context where it appears. The reduced version should still carry the identity through composition, shape, and timing of a simple appearance.

### F. A sortable live data table

**Brief:** help a person understand order changes while preserving exact values and inspection.

Bind each row to its entity ID. On an explicit sort, update the correct semantic order, maintain focus identity, and optionally move a small visible set of rows to their new locations with a brief nonovershooting transition. If too many paths cross, replace the rows directly and indicate sort direction. Preserve the selected entity rather than animating every row for spectacle.

For incoming live data, offer an appropriate update policy and freeze/pause controls where required. Do not reorder continuously under a pointer or while someone reads a cell. Show final values directly; no decorative zero-to-value counters. Reduced motion uses immediate ordered states and a persistent sort indicator.

**Verify:** equal values, missing rows, selected/focused rows, rapid sort reversals, multiple updates, virtualization, keyboard sorting, and screen-reader announcements. A snapshot's neat crossing paths do not establish usable live behavior.

## 27. Review and diagnose

### Inspect behavior in several ways

Watch at intended speed first. Ask what changed, why it changed, what remains available, and whether the person can continue. Slow playback and frame stepping help diagnose paths, spacing, clipping, and joins; they do not establish the intended feel. Return to actual speed after each adjustment.

Review in context, with ordinary content and repeated actions. A recording can show timing but cannot prove input responsiveness. A screenshot can show a frame but cannot prove continuity. A performance trace can show rendering cost but cannot prove comfort or expressive quality. State which evidence was actually inspected.

Use a comparison that can disagree with the proposal. Try the same task with a cut, a simpler transition, and the candidate motion while keeping other variables stable. Observe comprehension, errors, time to usable state, missed input, and the viewer's interpretation. For consequential or motion-rich experiences, include people with relevant access needs and stop a session if someone experiences discomfort. Do not ask someone to endure an effect to validate it.

### Diagnose the cause before changing the duration

| Symptom | Plausible cause | First correction to try |
| --- | --- | --- |
| Feels slow | Delayed onset, slow initial curve, long tail, serial choreography, blocked input | Remove delay, expose useful state sooner, overlap independent events, permit input |
| Feels abrupt | Excessive travel for time, velocity discontinuity, poor arrival | Reduce travel, reshape endpoint, preserve incoming velocity |
| Feels mushy | Excessive lag, low stiffness, high overdamping, weak anchor | Restore direct control; tune frequency and damping separately |
| Feels frantic | Large amplitude, fast reversals, too many simultaneous events | Reduce motion count and distance; establish one lead |
| Feels mechanical unintentionally | Constant finite movement, identical beats, rigid timing everywhere | Adjust acceleration and meaningful phrasing |
| Feels toy-like | Universal bounce, rubbery text, repeated celebration | Reserve elasticity for appropriate material or expressive events |
| Meaning is unclear | Wrong origin, false shared identity, competing anchors | Repair the spatial/semantic model |
| Items become hard to follow | Path crossing, occlusion, simultaneous property changes | Stage changes, keep landmarks, use persistent comparison |
| Reversal jumps | Restart from original keyframe or incompatible geometry | Retarget from current presentation and reconcile bounds |
| Reopened content vanishes | Stale exit callback | Guard cleanup with current operation identity |
| Invisible control receives focus | Opacity/transform treated as semantic hiding | Correct focus, visibility, and interaction state |
| Reduced motion breaks content | Final state or cleanup depends on animation | Commit state independently; provide targeted alternative |
| Runs smoothly but feels delayed | Input blocked or result withheld during animation | Separate availability from visual completion |
| Stutters on first use | Asset decoding, layout, shader/effect preparation, large paint | Profile first activation; simplify or prepare necessary resources |
| Slows after repeated use | Leaked effects, observers, layers, timers, or assets | Verify cancellation and resource disposal |
| Causes discomfort | Large-field movement, depth conflict, sustained oscillation, flashing | Remove the provoking effect and provide a controllable alternative |

### Check delivery readiness

Confirm the actual task and emotional intent are served. The final state must be understandable without catching the animation, and every important operation must remain usable with reduced motion. Check immediate acknowledgment, truthful outcomes, stable targets, accessible alternatives, and correct focus.

Exercise reversal, cancellation, repeated input, stale asynchronous results, resize, long content, localization, hidden tabs, resumed playback, and failed assets where applicable. Inspect performance on representative devices and verify cleanup. Test pause, skip, replay, and preference changes, not merely their presence in code.

For a motion system, confirm that each recipe names its role, mechanics, units, coordination, interruption, access behavior, and fallback. For authored media, inspect the encoded export and actual player. Fix the largest semantic or behavioral defect before polishing minor curve differences. Approve the result when the movement communicates the intended change, carries the intended character, and leaves the person in control.
