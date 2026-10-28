---
name: "haptic-design"
description: "Reference for designing and evaluating touch, tactile materials, physical controls, force feedback, vibration, and embodied experiences across digital products, objects, print, and spaces."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Apple"
  - "Susan J. Lederman"
  - "Roberta L. Klatzky"
  - "Alison I. Weber"
  - "Sliman J. Bensmaia"
  - "Hsin-Ni Ho"
  - "Lynette A. Jones"
  - "Elvin Karana"
  - "Bahareh Barati"
  - "Valentina Rognoli"
  - "Anouk Zeeuw van der Laan"
  - "Hapticlabs"
  - "Google"
  - "Texas Instruments"
  - "Michael J. Adams"
  - "Davide Filingeri"
  - "Şevval Mumcu"
  - "Creative Market"
  - "Artiss"
  - "World Wide Web Consortium"
type: "reference"
status: "experimental"
---

# Haptic design

Haptic design shapes what people learn and feel through contact and bodily action. A handle reveals how firmly to grip it. A dial makes an increment tangible. A fabric yields, drags, warms, and recovers. A brief vibration can make a digital boundary perceptible. These experiences depend on the body, the object, the action, and the situation together.

Use this guide to design actual touch and the expectations surrounding it. It covers tactile perception, movement and force, materials and finishes, physical controls, digital feedback, print, wearables, and spaces. Its default is purposeful, coherent feedback with enough variation to communicate what matters and enough restraint to remain comfortable in use.

The conventions are design starting points. Validate them with the intended people, physical samples, and supported hardware. A written pattern, material name, render, or waveform cannot establish how something feels.

## Contents

- [1. Establish the purpose of touch](#1-establish-the-purpose-of-touch)
- [2. Separate the channels of experience](#2-separate-the-channels-of-experience)
- [3. Understand human perception](#3-understand-human-perception)
- [4. Design for exploration and movement](#4-design-for-exploration-and-movement)
- [5. Describe tactile character precisely](#5-describe-tactile-character-precisely)
- [6. Shape feeling and meaning](#6-shape-feeling-and-meaning)
- [7. Design texture at the right scale](#7-design-texture-at-the-right-scale)
- [8. Choose materials and finishes](#8-choose-materials-and-finishes)
- [9. Design geometry, grip, and contact](#9-design-geometry-grip-and-contact)
- [10. Shape force, travel, and resistance](#10-shape-force-travel-and-resistance)
- [11. Compose vibration and temporal feedback](#11-compose-vibration-and-temporal-feedback)
- [12. Build an interaction vocabulary](#12-build-an-interaction-vocabulary)
- [13. Coordinate touch, sight, and sound](#13-coordinate-touch-sight-and-sound)
- [14. Choose the delivery technology](#14-choose-the-delivery-technology)
- [15. Apply platform conventions](#15-apply-platform-conventions)
- [16. Implement reliable feedback](#16-implement-reliable-feedback)
- [17. Design print and packaging](#17-design-print-and-packaging)
- [18. Design spaces and bodily journeys](#18-design-spaces-and-bodily-journeys)
- [19. Design wearables and mediated touch](#19-design-wearables-and-mediated-touch)
- [20. Preserve access, comfort, and control](#20-preserve-access-comfort-and-control)
- [21. Prototype and evaluate](#21-prototype-and-evaluate)
- [22. Specify and hand off](#22-specify-and-hand-off)
- [23. Work through concrete examples](#23-work-through-concrete-examples)
- [24. Diagnose and review](#24-diagnose-and-review)

## 1. Establish the purpose of touch

Touch can reduce the need to look, make boundaries and changes recognizable, support dexterity, express material identity, and give an action a credible physical consequence. It can also consume attention, increase effort, irritate skin, confuse an outcome, or make an object difficult to clean. Choose it because a particular experience benefits.

A useful brief states who makes contact, where contact occurs, what the person does, what the touch communicates, and what counts as a successful result. Include the expected frequency and length of use. A phone confirmation lasts briefly. A chair supports the body for hours. Their quality depends on different evidence.

| Purpose | Useful application | Evidence to seek |
| --- | --- | --- |
| Orientation | A shaped grip reveals the intended holding direction. | People orient it without repeated visual checking. |
| Control | A detent makes a meaningful setting perceptible. | People reach the intended value without overshoot or excessive effort. |
| Confirmation | A short cue acknowledges a completed action. | People understand what completed and avoid unnecessary repetition. |
| Warning | A distinct cue draws attention to an actionable problem. | People notice it, identify the problem, and recover. |
| Material expression | A finish communicates a deliberate contact character. | The physical sample supports the intended description in its actual use. |
| Comfort | A support distributes pressure and allows movement. | Comfort persists during representative use without harmful contact. |
| Atmosphere and identity | A coherent material palette gives a place or object a recognizable character. | People encounter that character through the intended contact sequence. |
| Immersion | Resistance or vibration reinforces a simulated event. | Feedback supports believable action without misleading force or distracting repetition. |

Write the primary job before aesthetic adjectives. "Make each alignment snap distinguishable while dragging" is actionable. "Make it premium and satisfying" needs further definition.

Use the simplest adequate means. Geometry or a passive mechanical detent may communicate a boundary more reliably than an added actuator. A visible state change may already make a routine action clear. Choose no additional cue when it contributes little.

## 2. Separate the channels of experience

Haptics includes information from the skin and information about bodily position, movement, and effort. These interact during ordinary handling. Temperature also contributes to material experience. Balance, posture, and movement through space belong in the wider embodied experience, although they are not all skin touch.

| Channel | What the person encounters | What the designer can change |
| --- | --- | --- |
| Cutaneous or tactile | Pressure, vibration, slip, stretch, edges, and surface contact. | Surface structure, contact geometry, friction, deformation, actuator output. |
| Kinaesthetic and proprioceptive | Position, movement, effort, load, and resistance. | Travel, mass distribution, torque, force profile, constraints, support. |
| Thermal | Initial coolness or warmth and change over contact. | Material construction, temperature, contact area, insulation, heat transfer. |
| Visual material expectation | Apparent softness, weight, grain, polish, or roughness. | Lighting, form, rendering, photography, colour, visual texture. |
| Auditory material expectation | A click, scrape, ring, creak, or muted impact. | Mechanism, damping, enclosure, sound design, synchronization. |

Actual texture changes contact. Implied texture changes what a person expects to feel. A paper-grain image on glass remains glass under the finger. Embossed stock has real relief. A virtual spring can look elastic while the input device supplies no resistance.

Distinguish two different uses of "active" and "passive". Active exploration means that a person moves to obtain information. Passive touch means that stimulation arrives without that exploratory movement. Separately, passive hardware uses its inherent material and mechanics, while powered hardware generates or changes output. A person can actively explore a passive surface or passively receive a powered vibration.

Distinguish information from simulation. A short buzz can indicate contact with a virtual wall. It does not reproduce the wall's sustained resistance. Document which property is delivered, which is suggested, and which remains unavailable.

## 3. Understand human perception

### Skin deformation carries information

Touch starts with mechanical and thermal interaction. Skin deforms around edges, contact patches change, and movement across a surface produces vibration. Receptors and subsequent processing organize these signals into properties such as slip, roughness, shape, and load.

Several overlapping mechanoreceptive channels contribute. Slowly adapting responses help represent sustained deformation and spatial features. Rapidly adapting responses emphasize changes and vibration. Skin stretch also contributes information about movement and handling. These channels work together. There is no separate receptor for "luxury", "trust", or a particular material.

Common terminology distinguishes Merkel-associated slowly adapting type I afferents, Meissner-associated rapidly adapting type I afferents, Pacinian-associated rapidly adapting type II afferents, and slowly adapting type II responses associated with skin stretch. These categories help explain spatial detail, changing contact, and vibration sensitivity. They do not divide perception into exclusive frequency bands or supply a recipe for activating one isolated sensation. Temperature and potentially damaging stimuli involve additional sensory pathways.

Fingertips, palms, forearms, soles, and other body sites differ in spatial sensitivity, tissue mechanics, and contact conditions. A pattern recognizable at a fingertip may be vague at the wrist. Stronger output may spread through tissue or an enclosure rather than become more localized. Design and test for the actual contact site.

### Texture has spatial and temporal information

Larger surface features can form spatial patterns of skin deformation. Fine texture often produces informative vibration as a finger or tool moves across it. This is why a texture can become clearer during a stroke than during static contact.

Movement speed, pressure, direction, and skin condition change the physical signal. Perception can remain more stable than the raw vibration because people integrate information across the action. Do not infer perceived roughness directly from one spectral peak or assume it increases in proportion to speed.

### Perception is relative and selective

A sensation is judged against its surroundings and recent experience. A small tap can be obvious during a quiet hold and disappear during walking or a strong grip. Two sequential effects can mask or merge with one another. A persistent texture can become less consciously noticeable without becoming mechanically irrelevant.

Separate sensory adaptation, attention, learning, and fatigue. Familiarity can improve recognition. Repetition can reduce notice or increase annoyance. Physical fatigue can make the same resistance harder to manage. One short demonstration cannot establish prolonged comfort.

Use perceptually separable differences rather than tiny parameter changes. A just-noticeable difference is conditional on the stimulus, body site, method, and person. It is not a universal token spacing rule. Weber-like proportional discrimination is a useful question to investigate within a range, not a license to prescribe one percentage for every haptic dimension.

### Heat flow shapes material identity

An object at room temperature may feel cool because it draws heat from warmer skin quickly. Another object at the same temperature may feel warmer because heat transfer is slower. Thermal effusivity describes a material's ability to exchange heat during contact and depends on conductivity, density, and heat capacity. Coatings, thickness, backing, contact pressure, and initial temperatures also affect the result.

Do not equate cool touch with a lower measured object temperature. Separate initial contact, continued contact, and environmental exposure. A metal handrail indoors and the same handrail after sun exposure present different design problems.

Wetness is also a perceptual interpretation involving thermal and mechanical cues. Perceived dampness need not track water content directly. Compare actual moisture, temperature, drag, and adhesion separately when a textile or contact surface feels unexpectedly clammy.

### Bodies and circumstances vary

Age, calluses, injury, neuropathy, medication, cold, fatigue, sensory sensitivity, and individual experience can affect perception or tolerance. Gloves, footwear, sleeves, moisture, and assistive devices change coupling. Do not infer an individual's ability from a demographic label. Provide alternatives and test representative conditions.

Pain and protective withdrawal are not aesthetic tuning targets. A single temperature, vibration level, or force limit cannot establish safety across materials, body sites, and exposure times.

## 4. Design for exploration and movement

People discover properties through actions. Allow the action that reveals the property you want them to understand.

| Property sought | Typical exploratory action | Design implication |
| --- | --- | --- |
| Texture | Stroke or rub a surface. | Provide a reachable area and useful direction of travel. |
| Compliance | Press or squeeze. | Make deformation and recovery perceptible without bottoming out painfully. |
| Weight and balance | Lift, support, or rotate. | Evaluate the assembled object in the intended grip. |
| Shape and volume | Enclose with the hand or follow a contour. | Keep critical edges and transitions discoverable. |
| Thermal character | Maintain contact. | Separate the initial impression from the sustained experience. |
| Friction and security | Slide, grip, release, or twist. | Test realistic moisture, pressure, speed, and contamination. |
| Mechanical state | Press, turn, latch, or pull. | Align the tactile transition with the actual state transition. |

These are common strategies, not mandatory gestures. A person with limited movement may explore differently. A display sample fixed to a wall cannot reveal an object's balance. A fabric swatch under glass cannot establish hand feel.

Map the whole sequence of contact. For a cup, consider reaching, first touch, lifting, gripping, drinking, setting down, washing, and drying. The lip meets the mouth while the handle meets the fingers. Each needs a different contact specification.

For an interface, map anticipation, input, movement, threshold crossing, commit, release, interruption, and recovery. A pleasing pulse at release does not repair an unclear threshold during the gesture.

## 5. Describe tactile character precisely

Use separate dimensions before combining them into an aesthetic judgment. "Soft" may refer to compression, a rounded vibration onset, a low-force mechanism, or a fuzzy surface. Specify which meaning applies.

| Dimension | Physical contributors | Useful description or comparison |
| --- | --- | --- |
| Roughness and relief | Feature height, spacing, shape, distribution, and skin deformation. | Fine grain versus coarse ridges, shallow stipple versus sharp protrusions. |
| Friction | Adhesion, surface structure, moisture, load, speed, and counter-surface. | Easy initial movement, secure grip, smooth sliding, intermittent sticking. |
| Compliance | Deformation under load, structure, thickness, and backing. | Firm at first contact, yielding under grip, supportive before bottoming out. |
| Recovery | Elasticity, viscosity, hysteresis, and time. | Immediate rebound, slow recovery, permanent indentation. |
| Thermal character | Heat transfer and contact history. | Cool at first contact, quickly neutral, insulating during prolonged use. |
| Weight and balance | Mass, centre of mass, inertia, and grip position. | Light to lift, stable in the hand, resistant to rotation. |
| Geometry | Curvature, edge radius, contact area, and surface transitions. | Rounded contact, a distinct locating ridge, a broad support area. |
| Moisture and adhesion | Absorption, evaporation, surface energy, and skin condition. | Dry after use, tacky when damp, slick after cleaning. |
| Vibration character | Output spectrum, onset, duration, decay, and coupling. | Compact tap, rounded pulse, sustained hum, uneven rattle. |
| Resistance | Force or torque over position, velocity, and direction. | Smooth drag, increasing spring force, discrete detents, firm end stop. |
| Material sound | Resonance, damping, mechanism, and enclosure. | Muted closure, hollow knock, short click, sustained ring. |

Distinguish stiffness from hardness, roughness from friction, and mass from apparent heaviness. A thin metal sheet can flex despite a hard surface. Smooth silicone can feel tacky. A thick foam can feel firm once compressed against a rigid base. "Matte" describes optical reflection and does not guarantee a dry or low-friction feel.

Use anchored comparisons. Keep reference samples or device effects whose identity can be recovered. "Less tacky than sample B after the cleaning cycle" can guide revision. "More natural" cannot until the relevant difference is named.

Separate measured properties from perceived qualities. A surface roughness average does not describe every feature shape or direction. A coefficient of friction belongs to a defined pair of surfaces and test conditions. A normalized intensity value is a software command, not a force measurement.

### Resolve friction, softness, and recovery

Separate the force needed to start sliding from resistance during movement. Intermittent sticking and slipping can create vibration, chatter, and an uneven feel. Adhesion during finger lift-off is another experience. A surface can slide acceptably yet feel unpleasantly sticky on release. Test pressing, sliding, holding, and detaching where those actions occur.

Moisture can change skin compliance, contact area, and lubrication. It does not make every surface uniformly more slippery or more grippy. Record skin condition, surface contamination, force, and speed rather than attaching one permanent friction rating to a material.

Compliance describes how much a construction deforms under load. Elastic behavior recovers after unloading, viscous behavior depends on time and motion, and many soft materials combine both. Creep is continued deformation under sustained load. Hysteresis means that loading and unloading follow different paths. These differences explain why two equally soft first impressions can provide different support and recovery during use.

## 6. Shape feeling and meaning

A material experience includes what is sensed, what the person thinks it means, what emotion it evokes, and what it invites them to do. Record these separately. A person may recognize a surface as soft, interpret it as domestic, enjoy touching it, and still reject it for a clinical control because it seems difficult to clean.

### Translate intent into a hypothesis

| Intended character | Candidate design choices | Question that can reject the hypothesis |
| --- | --- | --- |
| Precise | A clear threshold, little play, compact feedback, repeatable return. | Can people identify the setting, or does sharpness merely feel harsh? |
| Gentle | Rounded contact, distributed pressure, modest resistance, restrained feedback. | Does it remain detectable and controllable for the intended people? |
| Substantial | Stable balance, supported surfaces, controlled movement and decay. | Does added weight or damping increase fatigue or slow use? |
| Playful | A small expressive variation, elastic behavior, occasional surprise after clear action. | Is the meaning still recognizable after repeated use? |
| Calm | Predictable behavior, low repetition, quiet mechanisms, an easy way to disengage. | Does the design reduce interruption, or simply make important events easy to miss? |
| Crafted | Deliberate grain, resolved joins, consistent contact transitions, suitable aging. | Does close handling support the promise made by appearance? |
| Secure | Stable grip, a clear latch or boundary, truthful completion feedback. | Is security mechanically real and understandable, rather than merely suggested? |

These are conditional craft proposals. Polished metal can feel precise, slippery, cold, familiar, or unpleasant. Plush surfaces can comfort one person and overwhelm another. Natural origin, visible irregularity, gloss, heaviness, and high price do not establish tactile quality.

### Keep expressed and felt emotion separate

A pattern can express urgency without making every person feel afraid. A soft surface can suggest care without producing comfort. Ask separately what people recognize, how they describe the material, how they feel, and whether they want to continue using it.

Pleasant social touch has its own physiology and context. Findings about slow stroking on hairy skin do not prescribe a reassuring vibration rate for a phone, a wearable, or a palm-held control. Avoid neurotransmitter promises, medical benefits, and fixed frequency-to-emotion mappings.

### Use identity without overloading meaning

Build a recognizable family through consistent transitions, finish relationships, tactile geometry, and restrained temporal motifs. Preserve established action meanings. A signature brand pulse must not replace a platform's familiar error or selection behavior with a conflicting message.

Functional feedback needs a stable interpretation. Expressive artifacts may use ambiguity or unexpected material contrast deliberately. Keep that freedom away from controls, safety boundaries, consent, and essential instructions.

### Account for memory, culture, and ownership

Touch can acquire meaning through craft traditions, previous products, personal memories, and repeated handling. A worn edge may suggest familiarity to its owner and poor maintenance to a visitor. A surface associated with cleanliness in one setting can feel clinical in another. Ask which references the intended audience recognizes rather than assigning a fixed personality to a material.

Offer opportunities for deliberate exploration where enjoyment of material is part of the purpose. A thumb resting in a well-resolved contour, a page turning cleanly, or a textile recovering after compression can create satisfaction through an ordinary action. Evaluate that satisfaction during use instead of adding an unrelated decorative pulse.

## 7. Design texture at the right scale

Texture has scale, organization, direction, density, and contrast. Describe the texture in relation to the body and action that encounters it.

### Macrostructure, surface detail, and fine vibration

Large ribs may guide a hand or improve purchase. Smaller relief may distinguish controls. Fine structure may change drag and produce vibration during sliding. These are overlapping scales rather than fixed size categories.

Consider feature height, spacing, tip shape, rounding, continuity, orientation, and transitions into adjacent smooth areas. A repeated pattern can create a texture. An irregular surface can also have a consistent tactile character. Neither regularity nor irregularity is inherently more authentic.

For an ideal periodic structure scanned at constant speed, an encounter rate can be approximated by `f = v / λ`, where `v` is travel speed and `λ` is feature spacing. Use consistent length units. For example, 60 mm/s across 1 mm spacing produces 60 feature encounters per second. Skin mechanics, stick-slip, multiple contacts, and material deformation alter the resulting vibration. The equation does not predict a unique sensation or roughness rating.

### Direction and transition

Brushed grain, woven fibres, grooves, and pile can feel different in different directions. Test the intended movement and plausible reverse movement. A directional grip should not become abrasive when the person repositions the hand.

Resolve boundaries. The join between materials can create an unwanted ridge even when each swatch feels pleasant. A coating edge, seam, burr, or mould parting line can dominate a contact experience. Treat those details as part of the design.

### Compose contrast and rest

Use tactile contrast where it helps orientation or expression. A smooth resting area beside a subtly ribbed adjustment ring can distinguish support from control. If every surface is heavily textured, texture loses its locating role and can increase cleaning or comfort problems.

There is no universal number of textures for an object or room. Choose a hierarchy based on contact frequency, function, contrast, maintenance, and sensory demand. Keep prolonged contact surfaces comfortable even when occasional accent surfaces are expressive.

### Visual texture remains a separate composition

In graphics and rendered materials, control grain scale, contrast, direction, repetition, lighting, and placement. Keep text and control edges clear. Check textures at intended display and print sizes because resampling can erase detail or introduce moiré.

A photograph can suggest fibres or stone without proving their physical finish. A bump or normal map changes rendered appearance, not fabricated relief. If physical touch matters, specify the manufacturing feature separately and inspect a sample.

## 8. Choose materials and finishes

Select the material construction rather than relying on a category name. Record the base material, thickness, structure, finish, coating, backing, joining method, and expected conditions. The outermost contact layer and the structure beneath it both matter.

| Material family | Qualities worth exploring | Conditions and tradeoffs to test |
| --- | --- | --- |
| Metals | Cool initial contact, rigidity, mass, detailed machining, resonance. | Surface temperature, slip, sharp edges, fingerprints, coating wear, corrosion, enclosure ringing. |
| Wood and cork | Grain, porosity, directional variation, comparatively insulating contact. | Sealant, splinters, moisture, dimensional change, cleaning, compression, batch variation. |
| Stone, ceramic, and glass | Hardness, cool contact, relief, glaze or polish, stable forms. | Chips, impact, edges, thermal exposure, wet slip, grout or joints, weight. |
| Rigid polymers | Broad form and finish control, lightweight structures, integrated textures. | Wall thickness, flex, mould seams, hollow sound, oils, scratching, ultraviolet exposure. |
| Elastomers | Grip, compliance, damping, sealing, local deformation. | Tack, dust pickup, sweat, skin contact suitability, cleaning chemistry, aging, compression set. |
| Foams and gels | Pressure distribution, cushioning, damping, recovery behavior. | Bottoming out, creep, retained heat or moisture, hygiene, cover material, long-term support. |
| Woven and knitted textiles | Fibre, weave, pile, stretch, breathability, directional hand feel. | Abrasion, snagging, seams, pilling, wet behavior, cleaning, shedding, skin sensitivity. |
| Leather and coated alternatives | Grain, flexibility, changing surface character, layered constructions. | Finish chemistry, dye transfer, cracking, adhesion, sweat, maintenance, sourcing claims. |
| Paper and board | Fibre, caliper, stiffness, grain direction, coating, fold behavior. | Humidity, rubbing, tearing, print coverage, edge feel, finishing tolerances. |
| Composites and layered assemblies | Tunable stiffness, damping, local compliance, surface/backing combinations. | Delamination, uneven transitions, repair, hidden rigidity, inconsistent response over the area. |

### Treat the finish as part of the material

Polishing, blasting, brushing, glazing, embossing, flocking, coating, and texturing change contact as well as appearance. A clear resin can cover visible wood grain with a smooth continuous surface. A thin soft coating can feel pleasant initially and become tacky or peel after exposure. Verify the actual process, not a visual substitute.

A finish specification should include a physical reference sample and manufacturing information sufficient to reproduce it. Where measurements matter, specify their method and conditions. Gloss values do not replace tactile references. A roughness metric does not replace grip testing.

### Test the material through its life

Evaluate new, conditioned, cleaned, wet, worn, and repaired states as relevant. Include the conditions people introduce through skin oils, sanitizer, sunscreen, dust, food, and repeated contact. Avoid claiming resistance to a substance unless the actual construction has supporting evidence.

Decide whether aging should preserve uniformity or develop acceptable variation. Patina can support character. Flaking, sticky degradation, sharp wear edges, and loss of readable controls are defects. State replacement and maintenance conditions.

Balance sensory appeal with durability, cleanability, repair, sourcing, and disposal. "Natural", "recycled", and "biobased" describe different claims. None guarantees softness, health, sustainability, or user preference.

## 9. Design geometry, grip, and contact

Contact geometry determines how forces reach the body. A small edge concentrates pressure. A broad contour can distribute it but may fit some hands poorly. Evaluate the actual range of grips, hand sizes, reach, and use duration rather than designing to one ideal hand.

Shape should help people find, orient, and operate the object. Use a locating ridge, notch, concavity, asymmetry, or spacing when it supports a real distinction. Avoid ornamental relief that suggests an action the object does not support.

### Grip without unnecessary effort

Provide enough purchase for intended use without requiring excessive squeeze. Consider the load, centre of mass, direction of movement, handle clearance, and likely counterforces. A very grippy surface may help lifting but drag against skin during repositioning. A freely sliding surface may support adjustment but compromise secure holding.

Test with dry and damp hands, realistic gloves, and common alternative grips when relevant. Do not add aggressive texture to compensate for an unsuitable handle diameter, poor balance, or excessive operating force.

### Resolve seams, edges, and thermal contact

Place unavoidable seams away from repeated high-pressure contact where possible. Round contact transitions sufficiently for the actual load and movement. A visually small edge can still be uncomfortable during a strong grip.

Keep resting areas distinct from moving joints, pinch points, and hot or cold parts. Evaluate accessible protrusions and broken or worn states. A rounded external shell does not make the mechanism inside safe.

### Preserve discoverability without sight

Where tactile orientation matters, make distinctions detectable through the likely contact path. Two controls with different silhouettes may feel identical when only their top faces are reachable. A tiny raised icon may be harder to read than a change in shape or spacing.

Tactile distinction is not equivalent to a standardized tactile symbol or Braille. Use established standards and specialist review where those are required. Keep visible and assistive descriptions consistent with the physical arrangement.

## 10. Shape force, travel, and resistance

A control's feel emerges through its entire force or torque profile. Specify the movement before adding vibration.

| Behavior | What it contributes | What to resolve |
| --- | --- | --- |
| Spring | Increasing resistance and return toward a reference. | Stiffness, preload, travel, rebound, resting position. |
| Damping | Resistance related to motion that can control speed and settling. | Slow versus fast movement, temperature dependence, overshoot. |
| Friction | Resistance to starting or maintaining movement. | Breakaway, smooth travel, stick-slip, wear, direction. |
| Detent | A localized stable position or transition. | Spacing, strength, release, reversibility, meaning. |
| Snap-through | A distinct drop or transition in force. | Activation timing, accidental triggering, reset behavior. |
| End stop | A physical limit. | Contact force, cushioning, rebound, clearance, overload. |
| Backlash and play | Movement before the output responds. | Tolerance stack, rattle, precision, deterioration. |

An ideal linear spring follows `F = kx`, where stiffness `k` relates displacement `x` to force `F`. An ideal viscous damper follows `F = cv`, where `c` relates velocity `v` to opposing force. Real mechanisms can be nonlinear, direction-dependent, and affected by friction. Use these as explanatory models, not complete specifications.

For a button, describe initial contact, free travel, rising force, actuation, force drop if present, bottom-out, release, and reset. For a dial, describe starting torque, running resistance, detents, angular spacing, end stops, and return behavior. Include units such as newtons, millimetres, degrees, and newton-metres where measurements apply.

### Align the felt event with the state

Place the clear tactile transition at the meaningful change. If a latch clicks before it secures, the click gives false reassurance. If a dial's detent falls between valid settings, people must fight the control to reach a stable value.

Use hysteresis intentionally. Separate activation and release thresholds can prevent chatter near a boundary. Too much separation can make reversal confusing. Define and test both directions.

### Use weight and damping deliberately

Additional mass can provide stability while increasing fatigue and impact energy. Damping can make motion controlled while increasing effort. Avoid treating heavy, slow, or resistant as automatic indicators of quality.

Powered force feedback needs control engineering as well as interaction design. Validate stability, force and travel limits, watchdogs, release, and behavior under lost tracking or power. A vibration pattern cannot substitute for a force model. Do not improvise a universal control-loop rate or safe force limit from aesthetic preference.

## 11. Compose vibration and temporal feedback

Compose an event around its cause and desired interpretation. A transient is a compact event such as a tap. A continuous event sustains an evolving sensation. A sequence arranges events and gaps. Start with the simplest structure that communicates the intended distinction.

| Parameter | Perceptual question | Design caution |
| --- | --- | --- |
| Onset | Does the event arrive abruptly, softly, or late? | Slow hardware rise can blur a precise cue. |
| Intensity | Is it detectable and proportionate? | Equal command values do not guarantee equal perceived strength. |
| Sharpness or spectral character | Does it feel rounded, crisp, smooth, or buzzy? | API sharpness may abstract several signal properties. It is not a universal frequency knob. |
| Duration | Does it read as a tap, pulse, or sustained state? | Command duration can differ from physical ringing time. |
| Envelope | How does strength grow, sustain, and decay? | A long tail can obscure the next event. |
| Rhythm and spacing | Can events be grouped and distinguished? | Closely spaced pulses may merge, overlap, or become a buzz. |
| Modulation | Does the event evolve with action or state? | Avoid unrelated variation that makes meaning unstable. |
| Location | Can people identify where the event belongs? | Mechanical coupling can spread vibration away from the actuator. |
| Repetition | Is the cue useful after many occurrences? | Novelty and initial preference do not establish long-term tolerance. |

### Separate carrier, envelope, and event rate

The vibration carrier is the underlying oscillation. The envelope changes its strength over time. Event rate describes how frequently taps or pulses recur. A high-frequency actuator can produce a slow pulse sequence through its envelope. Do not call all three "frequency" without qualification.

An ideal sinusoid can be described by `x(t) = A sin(2πft + φ)`. Actual output depends on the driver, actuator, mounting, enclosure, and body contact. A digital waveform is an input to that system. Its amplitude alone does not establish displacement, acceleration, force, or sensation at the skin.

### Build contrast on more than strength

Distinguish important events with structure as well as amplitude. A compact selection tick and a separated outcome phrase can remain different when device strength varies. Too many similar patterns increase learning and confusion. Keep the vocabulary small enough for its actual task.

Match intensity to frequency of use and significance. Frequent feedback should generally be restrained. Reserve more salient patterns for events that justify attention. A critical event also needs reliable state presentation and recovery information. Increasing intensity cannot supply those meanings.

### Design silence and termination

Leave gaps so that events retain definition. Long-running feedback belongs where continuous state matters, such as a deliberate simulation or guided interaction. Stop it when that state ends, contact is lost, or the person cancels.

Do not automatically repeat an unnoticed cue indefinitely. Escalation needs a reason, a bound, and a way to acknowledge or stop it. Keep essential notification behavior within the appropriate platform notification system.

## 12. Build an interaction vocabulary

Give each functional cue a stable relationship to an event. Separate input receipt, a changing value, a boundary, an accepted action, a completed outcome, and an error. These may occur at different times.

| Interaction | Default convention | Failure to avoid |
| --- | --- | --- |
| Ordinary button | Use native control behavior. Add a cue only for a useful distinction. | Vibrating every visible tap without a purpose. |
| Discrete selection | A restrained cue at meaningful value changes. | Treating selection as success or firing on every movement sample. |
| Alignment or snap | A compact cue when alignment is entered or a snap commits. | Repeated cues while resting on the same alignment. |
| Threshold gesture | A cue when an actionable threshold is crossed, with a clear cancellation path. | Success feedback before the action is committed. |
| End boundary | A distinct but restrained indication when the person reaches the limit. | Repeating a strong pulse while input remains against the limit. |
| Significant success | Outcome feedback after completion is established. | Treating local button acceptance as completed remote work. |
| Warning or error | An appropriate platform pattern with an explanation and recovery path. | A punishing long buzz or a code the person must memorize to recover. |
| Ongoing activity | Usually maintain visible or otherwise accessible state. Use continuous touch only when it helps active control. | A generic background hum that conveys no actionable information. |
| Notification | Follow system settings, categories, and delivery behavior. | Simulating an unsolicited notification with foreground interaction effects. |

### Discrete values and continuous gestures

Bind a selection cue to a semantic step. If a slider has meaningful increments, detect changes in the active step rather than raw pointer movement. A high-resolution timeline may need cues at chapters, beats, or snapping points rather than every numerical unit.

During rapid motion, preserve the current interaction instead of replaying a backlog of ticks. Coalesce obsolete events. Test whether a lower cue density or a distinct landmark communicates more effectively.

Use hysteresis or equivalent boundary logic to prevent jitter from repeatedly entering and leaving a snap. Reset that logic when the gesture ends or its target changes. Do not suppress a deliberate new entry after a genuine exit.

### Realism and abstraction

Physical metaphors work when their causes align. A cue at collision can imply contact. Increasing resistance near a boundary can help regulate motion. Abstract patterns can communicate outcomes without pretending that a simulated object exists.

Choose abstraction when realism would be noisy, difficult to reproduce, or semantically misleading. A digital error does not need to feel like damage. A payment does not need an exaggerated impact. Preserve game and artwork freedom when the expressive context supports it.

### Consistency includes absence

Define where the product stays quiet. Equivalent actions should follow the same policy unless context changes the need. An isolated cue on one arbitrary card can imply special behavior that the card does not have.

Keep motion, haptics, and state in agreement across touch, keyboard, pointer, voice, and assistive input. Different inputs may need different physical delivery. They still need equivalent confirmation of the state.

## 13. Coordinate touch, sight, and sound

People combine senses to infer an event. A surface's appearance, a closure sound, and its vibration can support one material interpretation or contradict it. Design them together while preserving the necessary information in accessible forms.

### Synchronize the meaningful event

Choose the anchor explicitly. It may be first contact, threshold crossing, alignment, latch engagement, animation impact, or confirmed completion. The start of a gesture or animation is not automatically the right anchor.

For a snapping card, align the cue with the snap rather than finger-down. For an asynchronous save, input acknowledgement can occur immediately, but completion feedback must wait for the relevant save state. If the outcome arrives later, make its relationship understandable through the interface.

Latency includes sensing, gesture recognition, state processing, scheduling, driver response, and physical onset. Jitter is variation in that delay. Measure the chain you need to improve. Avoid a universal millisecond rule detached from the action and hardware. Set a project target, test the worst relevant conditions, and distinguish command timestamps from measured output.

### Match material logic

A crisp visual collision may pair with a compact tactile onset. A yielding object may need a gradual force profile and damped release. These are craft hypotheses, not mandatory mappings between colours, materials, and vibration presets.

A sound can change perceived material character. Listen to and feel the assembled product together. Also inspect channels separately to detect a mechanical rattle or a sensation masked by a persuasive audio track.

Vibration can be audible through an enclosure or tabletop. A cue intended to be private may still attract attention or reveal a recognizable rhythm. Consider the resting device, shared desk, microphone, camera, and motion sensors as part of the context.

### Use deliberate incongruity carefully

A soft-looking object that feels rigid can be expressive in an artwork or exhibit. State the intended discrepancy and test its interpretation. Do not use incongruity to obscure a load-bearing boundary, hot surface, control state, or permission decision.

### Distinguish pseudo-haptics from delivered force

Changing the relationship between physical movement and displayed movement or deformation can alter apparent resistance, weight, or stiffness. This is often called pseudo-haptic feedback. For example, an object that deforms less for the same tracked hand movement may appear stiffer even without an actuator supplying that resistance.

Use such effects cautiously in simulations and expressive interfaces. They can also feel like lag, poor tracking, or a broken control. Preserve predictable control, evaluate reversibility and task accuracy, and disclose the physical limitation in the specification. A change in apparent stiffness does not create a load-bearing force.

## 14. Choose the delivery technology

Choose the physical property and contact arrangement before the mechanism. Availability alone does not make a technology suitable.

| Delivery method | Useful capability | Main limits and questions |
| --- | --- | --- |
| Passive geometry and materials | Persistent shape, texture, compliance, grip, thermal character. | Fixed or slowly changing behavior, wear, fabrication tolerances. |
| Mechanical springs, detents, and dampers | Travel, resistance, stable positions, return, clear transitions. | Effort, packaging, noise, durability, tolerance stack. |
| Eccentric rotating mass motor | Simple vibration or rumble. | Spin-up and spin-down can blur short events. Amplitude and speed are coupled. |
| Linear resonant actuator | Efficient vibration around a designed resonance, controllable transients with a suitable driver. | Useful bandwidth, braking, enclosure coupling, driver capabilities. |
| Piezoelectric or broadband actuator | Potentially rapid response or wider signal shaping. | Displacement, mounting, drive electronics, load, cost, contact distribution. |
| Voice-coil or other displacement actuator | Controlled movement and potentially rich vibration within its design range. | Size, stroke, power, heat, force, control and mounting. |
| Skin indentation, stretch, or pneumatic systems | Local pressure, deformation, directional or squeeze cues. | Attachment, bulk, response, comfort, leakage, release behavior. |
| Surface friction modulation | Changes in sliding friction on supported surfaces. | Often depends on movement, skin condition, contact force, and specialized hardware. |
| Shape-changing or pin-array surfaces | Local relief, changing contours, tactile display elements. | Resolution, speed, force, noise, durability, physical depth. |
| Force-feedback motors and brakes | Resistance, guidance, torque, constraints, virtual mechanics. | Stable control, safety, power, backdrivability, mechanical limits. |
| Thermal systems | Controlled warming or cooling. | Slow response relative to many vibration cues, energy, condensation, exposure limits. |
| Mid-air ultrasound | Contactless pressure sensations in a controlled interaction area. | Tracking, usable volume, field geometry, intensity, limited material and force reproduction. |

These capabilities vary by implementation. An actuator class does not guarantee a particular quality. Use the actual data sheet, driver requirements, mounting constraints, and measured assembly behavior.

### Design the complete signal chain

The delivery chain includes the requested event, generated signal, driver, actuator, mounting, enclosure, coupling, and body. A loose mounting can turn a clean signal into a rattle. A soft backing can absorb output. A case or tight strap can change transmission. Stronger drive may excite an unwanted resonance rather than improve clarity.

Plan mounting location, orientation, required space, electrical and thermal limits, acoustic isolation, serviceability, and production tolerances early. Bench performance with an unloaded actuator does not establish performance in the final object.

### Match capability to the promised sensation

Ordinary whole-device vibration cannot independently reproduce temperature, static relief, sustained load, arbitrary spatial detail, or a material's compliance. A single actuator also has limited ability to assign separate sensations to distant virtual objects. Spatialized arrays require validation of actual localization and mechanical cross-talk.

When hardware is insufficient, simplify the promise. Convey "boundary reached" rather than claiming to simulate a stone wall. Use physical samples when material selection depends on actual contact.

## 15. Apply platform conventions

Treat platform behavior as a semantic contract and verify the current documentation for the target SDK, operating system, hardware, and connected accessory. Preserve the same intended meaning across platforms while allowing each platform to deliver it appropriately.

### Apple platforms

Prefer standard controls and their existing feedback where suitable. Check what they already provide before adding effects. Use selection feedback for changing a selection, impact feedback for a physical metaphor, and notification feedback for an outcome. Do not choose a success pattern for an arbitrary tap because it feels attractive.

Custom Core Haptics patterns can combine transient and continuous events with intensity, sharpness, and supported audio. Use custom patterns when a clear purpose exceeds standard feedback. Intensity and sharpness are expressive controls interpreted by the system. They are not direct specifications of skin force and frequency.

Do not infer support from the platform name alone. The relevant output may come from an iPhone, Apple Watch, supported trackpad, Apple Pencil Pro, or controller, with different capabilities and documented patterns. An iPad experience must account for its actual device or accessory path. visionOS or hand tracking does not by itself guarantee physical force or tactile output.

On supported Mac trackpads, use documented alignment and pressure-level meanings appropriately. On Apple Watch, keep system patterns such as direction, start, stop, success, failure, and retry aligned with their meanings. A watch pattern is not an arbitrary brand vocabulary.

### Android

Prefer action-oriented `HapticFeedbackConstants` through the appropriate view or toolkit API for standard interactions. Select by meaning and required SDK availability. Use predefined or composed vibration effects when their additional control is necessary.

Check capabilities for custom effects. Amplitude control, primitives, and envelope support vary. Platform fallback for a predefined effect does not imply that every custom composition has an automatic fallback. Provide a simpler supported alternative or omit the optional cue when needed.

Keep interaction feedback distinct from notifications and alarms. Respect the relevant user settings and usage classification. Do not bypass disabled touch feedback to preserve a decorative effect.

### Web

Treat browser vibration as optional enhancement. The Vibration API has limited browser support and exposes simple durations and pauses rather than a portable, precisely calibrated haptic instrument. Availability of a method is not evidence that the person felt output.

Check browser policy, user activation requirements, hardware, visibility, and settings for the intended deployment. Keep the action and its accessible state complete without vibration. Do not promise an iPhone-like click, texture reproduction, or equivalent output across browsers from an on/off pattern.

### Controllers, pens, trackpads, and other devices

Query the connected device's supported features and handle reconnection or loss. Rumble motors, trigger resistance, stylus feedback, and localized trackpad effects offer different kinds of information. Their parameters and meanings are not interchangeable.

Prefer the platform's documented interaction path. Keep essential state visible or otherwise accessible when an accessory is absent. Test the actual controller model, pen grip, handedness, and contact conditions that the experience requires.

## 16. Implement reliable feedback

A good pattern can fail through incorrect event ownership, duplication, lifecycle handling, or scheduling. Centralize the semantic policy while keeping device implementations replaceable.

### Own events at the correct state transition

Emit feedback from the component that knows the meaningful change occurred. Rendering, re-rendering, hover, and repeated network observations should not trigger the same cue again. Separate event identifiers from component lifetimes.

A framework-neutral event path can follow this logic:

```text
When a semantic transition occurs:
    Validate the current interaction and state.
    Identify the event and its meaning.
    Apply user preferences and platform policy.
    Ignore an already-handled event.
    Discard feedback that is no longer relevant.
    Select a supported platform effect or fallback.
    Resolve priority and interruption.
    Play once at the intended anchor.
    Keep the resulting state available through other channels.
```

This describes behavior, not a drop-in API. Verify the concrete framework's lifecycle and threading rules before implementation.

### Resolve collisions and cancellation

Define a priority policy. An important outcome may replace a decorative effect. Frequent selection ticks should coalesce rather than queue behind a long sequence. Avoid layering incompatible effects on an actuator that cannot render them distinctly.

Cancel continuous feedback and queued nonessential cues when an interaction ends, the context changes, or the app loses the necessary contact or lifecycle state. A late tick after the finger lifts suggests a new event. A success cue after cancellation can report the wrong state.

Use bounded repetition and project-specific rate limits. Choose limits through the intended gesture and hardware, then test them. Arbitrary global cooldowns can hide a valid new interaction or suppress an important outcome.

### Prepare and recover

Where an API supports preparation, prepare close enough to anticipated use to reduce cold-start delay without keeping resources active indefinitely. Handle engine errors, interruptions, resets, and device loss. Recreate invalid resources as required by the API. Do not replay old interaction cues after recovery.

Verify foreground/background transitions, app suspension, power constraints, and interactions with audio capture or playback. Keep the main action reliable if optional feedback cannot play. Report errors through appropriate state and diagnostics rather than making the action depend on a vibration engine.

### Respect settings without inventing equivalences

Use separate controls when people need independent preferences for sound, vibration, motion, and notifications. Reduced motion is not a universal haptics-off preference. Silent audio mode does not necessarily mean that every haptic is unwanted. Follow platform behavior and explicit product settings.

Make authored haptics easy to disable and offer a sample preview when customization helps. If strength controls exist, keep important distinctions recognizable across the supported range. Do not expose an elaborate pattern editor unless it serves the product's actual purpose.

### Verify output, not only calls

Logs can show that an event was requested. They cannot show that a person perceived it. A successful API return, emulator run, or unit test does not establish tactile quality. Use real hardware for onset, strength, acoustic leakage, coupling, and repeated use.

For timing investigation, distinguish the input timestamp, semantic transition, playback request, and measured physical output. Use a suitable sensor or recording method when those differences matter. A microphone may capture a sound without establishing the vibration at the hand.

## 17. Design print and packaging

Print has actual material contact as well as graphic texture. Specify stock, caliper, stiffness, grain direction, surface finish, print coverage, folds, joins, and finishing operations. A digital mockup communicates appearance and intent. A production proof establishes the physical construction.

### Design the handling sequence

Consider picking up, opening, turning, holding, writing, tearing, dispensing, closing, and disposing. A package's first stroke is only one moment. An inaccessible opening can dominate the experience of an otherwise pleasing surface.

Use tactile changes to locate an opening, distinguish a grip area, or support hierarchy. Keep the cue discoverable before the action. A pull tab that is visible but impossible to grasp needs a mechanical revision.

### Choose finishes by their contact role

| Treatment | Potential contribution | What to verify |
| --- | --- | --- |
| Embossing or debossing | Relief, identity, a locating feature. | Actual depth, edge character, reverse impression, stock and tooling limits. |
| Letterpress or impression | Local relief and a particular paper interaction. | Legibility, consistency, compression, marks on the reverse. |
| Foil | Optical contrast and sometimes a local edge or finish difference. | It may have little perceptible relief. Do not promise raised tactility from appearance alone. |
| Raised ink or spot coating | Local thickness, smoothness, gloss or friction contrast. | Cured height, durability, sharpness, rubbing, blocking between surfaces. |
| Lamination or soft coating | A changed contact layer and possible protection. | Fingerprints, tack, scuffing, delamination, writing, recycling implications. |
| Uncoated or textured stock | Fibre character, absorbency, drag, stiffness. | Ink spread, abrasion, moisture, folded edges, production consistency. |
| Perforation or tear feature | A guided mechanical action. | Starting force, propagation, incomplete tears, sharp remnants, dexterity demands. |

Keep text readable over textured areas and at folds or relief transitions. Do not treat decorative embossing as readable Braille. Where standardized tactile labels are needed, verify dimensions, placement, durability, and applicable requirements separately.

Test packaging with realistic contents. Weight, internal fit, cushioning, seal strength, and friction change the opening experience. Provide an obvious recovery route when the first attempt fails. Avoid complicated rituals that delay access without adding value.

## 18. Design spaces and bodily journeys

An environment is encountered through feet, hands, clothing, assistive devices, posture, and movement as well as sight. Map reachable contact, load-bearing surfaces, repeated support, and transitions along a route.

Prioritize floors, thresholds, handles, rails, seats, counters, controls, and reachable walls. A visually textured facade may contribute atmosphere without providing direct touch. Keep that distinction clear in the spatial concept.

### Put material character where people encounter it

Choose touch-rich areas intentionally. A handrail's section, temperature, joints, and continuity matter more to its feel than a distant decorative wall. A seat needs pressure distribution, edge comfort, support, and suitable thermal and moisture behavior over time.

Evaluate the bodily sequence. Arrival may involve a cold exterior handle, a heavy door, a threshold, a resting point, and a reception counter. Conflicting friction, height, force, and material transitions can make a route tiring even when each item looks resolved.

### Make transitions legible and usable

A change of texture can signal a zone, but it can also obstruct wheels, catch a cane, increase rolling resistance, or create a trip hazard. Preserve stable, usable circulation. Use established tactile warning and guidance systems where required. Decorative strips must not imitate those systems ambiguously.

Test floors under expected contaminants, footwear, cleaning, and weather. An aggressive finish can improve some grip conditions while increasing abrasion, cleaning difficulty, or rolling effort. A generic "non-slip" label does not establish suitability for the actual conditions.

Continuous rails, discoverable controls, clear edges, and accessible routes require current local standards and specialist review when applicable. This guide supports sensory design and does not replace building, access, fire, or product compliance work.

### Compose atmosphere with maintenance

Use differences in softness, resonance, thermal character, and surface detail to support the intended place. Let frequent contact areas provide sensory rest when the environment is already busy. There is no universal rule that warm-looking materials are welcoming or that smooth surfaces are sterile.

Inspect installed assemblies and full-scale mockups. Grout, joints, fasteners, upholstery seams, backing, lighting, and cleaning procedures change the experience. A beautiful material board cannot establish the feel of a whole room.

## 19. Design wearables and mediated touch

A wearable delivers feedback through changing contact. Fit, strap tension, placement, clothing, motion, and body site can alter both sensation and comfort. Design attachment and removal alongside the signal.

### Design for stable, tolerable coupling

Check whether feedback remains detectable at the loosest acceptable fit and comfortable at the tightest intended fit. Look for pressure concentration, trapped moisture, movement restriction, rubbing, and changes during activity. Do not tighten a device beyond acceptable use merely to make a cue clearer.

A wrist cue does not inherit fingertip localization. Test whether people can distinguish locations or patterns while moving and when attention is elsewhere. Keep directions consistent with the wearing orientation, handedness, and body reference frame.

### Make remote touch consensual

A message rendered on the body can feel intimate, intrusive, affectionate, or alarming depending on the relationship and timing. Let recipients control who can send touch, when it can arrive, and how to stop it. Provide blocking, rate limits, and quiet periods where the experience requires them.

A transmitted pulse can represent another person's gesture without reproducing it. Avoid claims that the recipient is feeling the sender's exact pressure, movement, or emotion unless the system actually captures, reproduces, and validates those properties.

### Keep immersion within physical capability

In virtual or augmented experiences, align feedback with tracked contact, tool state, and plausible location. Handle tracking loss and mismatched physical/virtual boundaries. A controller buzz can acknowledge contact but cannot prevent the hand from passing through a virtual object.

Do not imply support, resistance, or a safe surface where none exists. Physical props can improve contact realism when their position and geometry are controlled. Their registration and mechanical safety remain part of the experience.

## 20. Preserve access, comfort, and control

Make essential meaning and operation available without requiring a particular tactile sensitivity. Provide clear state, labels, accessible announcements when appropriate, and alternative input paths. Haptics can be valuable for access, but one sensory channel cannot cover every person's needs.

### Redundancy should preserve meaning

Do not instruct someone solely to "wait for the vibration" or "press the rough button" when that property is necessary to complete the task. Include an identifiable control or persistent state through another suitable channel. For screen interfaces, preserve semantics, focus behavior, and assistive technology support.

A visible label is not a sufficient alternative for a blind person using a haptic cue. Sound alone is not sufficient for a deaf person. Design alternatives around the actual task and available senses rather than checking a count of channels.

Standardized tactile information and learned tactile communication systems can carry rich meaning for trained users. Do not generalize the limits of casual phone vibration into a claim that touch cannot support complex information. Such systems require their own conventions, training, and specialist validation.

### Support different sensory preferences

Provide a way to reduce or disable authored vibration. Let people avoid unnecessary textured contact where feasible. Some people seek strong input, while others experience mild vibration, coarse fabrics, or sticky finishes as distressing. Do not label either preference as incorrect.

For physical controls, reduce the need for sustained grip, precise fingertip force, simultaneous actions, and awkward wrist positions. Where task requirements demand resistance or force, justify it and provide a suitable alternative where possible.

### Manage physical exposure through engineering

Evaluate prolonged pressure, abrasion, pinch and shear, thermal exposure, repeated effort, vibration, and materials in contact with skin. Use relevant product-specific standards and qualified expertise for medical, industrial, transport, child, or other regulated use.

Comfort ratings do not establish safety. People with reduced sensation may not notice harmful exposure. A consumer microinteraction and a vibrating tool used for hours have different exposure questions. Do not transfer a safe-looking duration or amplitude between them.

Powered mechanisms need bounded output and a defined fail-safe state. For constricting or force-producing devices, make disengagement and release effective during a fault. Stop a trial when pain, numbness, skin irritation, dizziness, or distress occurs. Investigate the cause rather than increasing tolerance demands.

### Preserve agency

Touch should help people understand and act. Avoid using insistent vibration, resistance, or unpleasant surfaces to pressure a purchase, prevent cancellation, or punish an error. A satisfying closure cue must report the actual transaction state, not encourage premature trust.

Treat privacy as a design question. Audible vibration, visible body reactions, and shared surfaces can expose activity. Avoid unnecessary storage of intimate touch patterns or detailed body-response data. Collect only what the experience needs and explain it appropriately.

## 21. Prototype and evaluate

Use prototypes to answer explicit questions. A visual prototype can test discoverability and expectations. A material sample can test contact. A physical mechanism can test force and travel. An instrumented assembly can test delivery. None substitutes for all the others.

### Progress toward the real contact

1. Define the task, contact site, intended property, alternative behavior, and failure conditions.
2. Gather physical or device references and explore deliberately different candidates.
3. Compare a small set while changing one meaningful property at a time where possible.
4. Integrate candidates into representative geometry, mounting, mass, backing, and software state.
5. Test complete actions with intended people and environments.
6. Revisit the first impression after repeated or prolonged use.
7. Check production variation, aging, cleaning, interruption, and missing-feedback conditions.
8. Revise the specification and preserve the accepted reference sample or device build.

Early rough prototypes are useful when their limitations are explicit. A hidden operator triggering feedback can explore timing and meaning, but does not establish automatic detection accuracy or system latency. A loose actuator on the bench cannot establish enclosure feel.

### Separate expectations from contact judgments

Compare visual-only, touch-only, and combined conditions when the relationship matters. Blind or concealed-material comparisons can reveal a visual bias. Restore the full context afterward because real use includes those expectations.

For materials, normalize sample size, backing, temperature, and preparation where the comparison requires it. Record when the actual product intentionally differs. Give people a realistic exploratory action instead of forcing one fixed stroke that does not match use.

For patterns, randomize or counterbalance presentation order, allow rest, and avoid changing several parameters at once when trying to identify a cause. Compare at appropriate perceived strengths so a louder or stronger candidate does not win solely through salience.

### Evaluate distinct questions

| Question | Suitable observation or measure | Interpretation limit |
| --- | --- | --- |
| Detection | Missed cues and false reports under realistic conditions. | Detectable does not mean understandable or pleasant. |
| Discrimination | Confusion between patterns, locations, textures, or states. | Laboratory distinctions may disappear during activity. |
| Meaning | Unprompted interpretation, learned association, correct next action. | Recognition after training does not establish first-use clarity. |
| Control | Errors, overshoot, accidental activation, effort, recovery, task time. | Faster is useful only if accuracy and comfort remain acceptable. |
| Timing | Perceived causality, measured onset and variability. | Request timestamps do not establish output timing. |
| Character | Anchored descriptions and comparison with the brief. | Preference does not establish a universal material meaning. |
| Comfort | Ratings and observation during representative use, including later feedback. | Absence of immediate complaint does not establish safety. |
| Durability | Contact, performance, and appearance after relevant conditioning. | An improvised aging cycle does not prove a service-life claim. |
| Access | Successful use with alternative inputs, senses, and reduced feedback. | One participant cannot represent every access need. |

Ask neutral questions such as "What changed?", "Where did you feel it?", and "What would you do next?" before supplying words such as "premium" or "reassuring". Capture participants' own descriptions. Distinguish recognition, preference, comfort, and task performance.

### Test the missing and failed cases

Disable haptics. Remove or loosen the accessory. Use the object through a case or glove. Cancel a gesture, reverse direction, change orientation, interrupt audio, suspend the app, and reconnect hardware as relevant. Verify that essential state remains understandable and that old cues do not arrive afterward.

Test repeated actions at realistic speed. A good isolated tick can become a harsh buzz in a scrolling sequence. Test long contact for pressure, heat, friction, and fatigue. Include the device on a desk because acoustic leakage can be worse than in the hand.

### Choose acceptance criteria before selecting the winner

Set project-specific criteria tied to the task. A snap cue might need to be distinguishable from an end-stop cue during realistic dragging. A handle may need to support a specified load without excessive grip effort. An opening must work for the intended range of users with actual contents.

Define the method, conditions, and unacceptable failures before reviewing results. Report actual sample size, participant characteristics relevant to the task, device versions, conditions, and uncertainty. Do not turn a small preference test into a universal score for tactile quality.

## 22. Specify and hand off

Keep intent, semantics, implementation, and verification distinct but connected. A manufacturer needs construction details. A developer needs event rules. A reviewer needs the reference and evidence that establish acceptance.

### The haptic brief

Record these decisions:

| Field | Required content |
| --- | --- |
| Purpose and task | What the person needs to understand, control, or feel. |
| Contact | Body site, grip, contact area, direction, duration, and expected movement. |
| Context | Environment, use frequency, clothing or gloves, moisture, accessibility, attention. |
| Intended character | Observable qualities and anchored references. |
| Physical channel | Actual material, mechanics, vibration, force, thermal output, or implied texture. |
| Meaning | The state or interpretation the experience should communicate. |
| Constraints | Hardware, fabrication, power, acoustics, maintenance, comfort, safety, access. |
| Alternatives | What happens when touch is absent, unwanted, or unavailable. |
| Evidence | What has been proposed, built, measured, felt, or tested, and by whom. |
| Acceptance | Task-specific pass conditions and remaining uncertainties. |

### Semantic event specification

Use stable names such as `selection.step`, `alignment.enter`, `action.completed`, and `action.failed`. Names should describe meaning rather than a waveform or an arbitrary strength. Map each name to a supported implementation per platform.

For each event, specify the trigger, state prerequisite, anchor, ownership, repetition, interruption, cancellation, preference behavior, supported devices, fallback, visual or assistive state, and test cases. Keep versioned pattern assets and tuning information beside the implementation.

A concrete proposal might read:

```yaml
id: alignment.enter
purpose: Confirm entry into an active alignment target.
trigger: The active gesture changes from unaligned to aligned.
prerequisites:
  - The gesture is still active.
  - The alignment target is valid in the current state.
anchor: The committed snap transition.
repeat: Once per distinct entry, after a genuine exit.
priority: Interaction feedback; coalesce obsolete entries.
cancel: Gesture end, target removal, context change, or lost device.
implementation:
  mac_trackpad: Documented alignment feedback where supported.
  other_devices: Supported semantic effect chosen and tested per platform.
fallback: Preserve the visible alignment guide and accessible position state.
verification:
  - No repeated cue while holding on the same target.
  - Deliberate exit and re-entry can produce a new cue.
  - Cancellation does not leave queued feedback.
status: Proposed; device tuning and user evaluation pending.
```

This example defines behavior. It does not claim that a pattern has been implemented or felt.

### Physical material and mechanism specification

For a surface, record construction, supplier and revision, finish process, texture direction, contact geometry, sample identity, acceptable variation, cleaning, aging, and relevant measurement methods. Include a retained approved sample when reproducibility matters.

For a mechanism, include the force or torque versus travel profile, actuation and release points, damping, play, end stops, intended loading, environmental conditions, tolerances, and life requirements. Distinguish target values from measured results.

For an actuator assembly, include the part, driver, mounting, orientation, enclosure, contact arrangement, calibrated output conditions, pattern asset, power limits, and failure behavior. Do not let an actuator part number substitute for an assembly specification.

### Keep evidence honest

A specification can be conceptually complete while awaiting physical verification. Label that state plainly. An AI may propose a finish, generate an asset, or inspect code without being able to feel its result. Never claim tactile comfort, exact material equivalence, or real-device quality from images and source code alone.

## 23. Work through concrete examples

The following examples illustrate design reasoning. They are proposals to prototype and test, not validated recipes.

### A precision value dial in a mobile interface

The task is to reach a meaningful setting without constant visual checking. Start with native selection feedback at semantic increments. Keep the current value visible and accessible. Avoid assigning a tick to every pixel of movement.

Define one event per step transition. Coalesce obsolete ticks during fast movement and distinguish an end boundary only if that distinction helps. If snapping is active, use boundary logic that prevents repeated cues while a finger jitters around one value.

Test slow and fast movement, reversal, overshoot, accessibility input, haptics disabled, and different devices. Reject a candidate that feels impressive in isolation but merges into a buzz during actual adjustment.

### A significant action with a remote outcome

A person submits a transfer. The initial control state acknowledges input, then communicates progress. The outcome cue occurs only when the relevant completion state is confirmed. An error produces its own explanation and recovery action.

Do not use the outcome pattern on finger-down. Track event identity so retries, reconnection, and screen re-creation do not produce duplicate completion cues. Keep the receipt or status available after the cue has ended.

Test delayed completion, cancellation, uncertain network state, duplicate responses, and settings that disable feedback. A reassuring pulse cannot resolve an unknown transaction state.

### A hand-held adjustment knob

The intended character is controlled and easy to locate. Explore a rounded grip with a distinct adjustment ring. Compare subtle knurling with a smoother high-friction finish while keeping diameter and mechanism constant.

Specify starting torque, running resistance, meaningful detents, end stops, axial play, and the mechanism's sound. Test with the actual mounted object, dry and damp hands, representative gloves, and repeated use. A loose prototype knob cannot establish the precision of the final assembly.

Reject aggressive relief that hurts during sustained adjustment, and reject extra damping if it makes rapid changes tiring. Preserve tactile distinctions after cleaning and wear.

### A paper invitation or small publication

The intended character is quiet and materially present. Explore a suitable uncoated stock with restrained relief in one meaningful area. Keep fine text away from deep impressions and textured interference.

Evaluate stiffness, page turning, edge feel, fold behavior, ink coverage, and the reverse impression. Inspect actual proofs at the intended size. A grain overlay in the mockup does not establish the stock's feel.

If a coating improves visual appearance but produces unwanted drag or tack, revise the construction rather than adding more graphical texture. Keep the opening and reading experience primary.

### A public interior

The goal is a clear, comfortable arrival route. Map the door pull, opening effort, threshold, handrail, seating edge, and service counter. Choose material changes that support these contact roles rather than distributing decorative texture everywhere.

Test full-scale details with mobility aids, realistic footwear, wet conditions where relevant, cleaning, and prolonged resting contact. Preserve regulated tactile guidance and accessible circulation. Keep expressive surface changes away from ambiguous hazards.

Review initial and sustained thermal contact. A cool handle can be acceptable indoors but unsuitable after exterior temperature exposure. Evaluate the installed condition rather than inferring it from a material board.

### A wrist-worn navigation cue

The task is to convey an upcoming direction while the person moves. Begin with a small, learnable vocabulary and a consistent wearing orientation. Confirm that location or rhythm distinctions survive ordinary arm movement and fit variation.

Allow strength adjustment or a simpler supported cue when needed, and preserve another navigation channel. Test under sleeves, at realistic strap tensions, with pauses, route changes, and ambiguous positioning.

Do not reuse the same pattern for a social message or completion event. Stop obsolete guidance when the route changes. Treat the cue as navigation assistance whose reliability must be tested in context.

### A simulated rough surface

The experience asks a person to drag a tool across a virtual material. Couple the feedback to contact state, movement, and supported surface behavior. Design coherent sound and visual scale while distinguishing rendered appearance from actual resistance.

Compare candidates while changing speed and pressure. Avoid simply playing a fixed buzz whenever the pointer is over the texture. Stop feedback when contact ends or tracking fails.

If the device supplies only whole-controller vibration, describe the result as a texture cue. Do not claim that it reproduces the original surface's relief, friction, compliance, and temperature.

## 24. Diagnose and review

### Find the cause of a weak result

| Symptom | Plausible cause | Next useful check or change |
| --- | --- | --- |
| A cue feels detached from the action. | Wrong anchor, latency, jitter, or unrelated sound. | Trace the semantic transition and measure physical onset. |
| A short click feels like a buzz. | Long drive, ringing, poor braking, or dense repetition. | Inspect the real assembly and shorten or simplify the event sequence. |
| Feedback seems stronger on a desk than in the hand. | Acoustic amplification and different mechanical coupling. | Test both contexts and inspect mounting and enclosure response. |
| Two cues are confused. | Similar rhythm, weak contrast, device variation, or insufficient learning. | Compare structure and meaning under realistic movement. |
| A pattern is detectable but annoying. | Excessive frequency, intensity, duration, or poor causal value. | Reduce its demand or remove unnecessary occurrences. |
| A grip slips when wet. | Contact friction changed, geometry is inadequate, or drainage is poor. | Test wet assembly behavior and revise grip construction. |
| A soft surface becomes uncomfortable. | Bottoming out, pressure concentration, heat, moisture, or drag. | Evaluate support and prolonged contact rather than the first stroke. |
| A material feels different from its render. | Finish, coating, backing, scale, or expectation mismatch. | Compare actual construction with the promised property. |
| A precise mechanism feels cheap. | Play, uneven friction, rattle, misplaced detents, or inconsistent return. | Inspect the full force profile and tolerance stack. |
| A successful action feels uncertain. | Weak state presentation or cue emitted at the wrong transition. | Clarify acknowledgement versus completion. |
| A surface is hard to maintain. | Relief, pores, joints, or finish conflict with cleaning. | Inspect cleaned and aged samples using the intended process. |
| A wearable works only when overtightened. | Poor placement or coupling, unsuitable actuator, or wrong cue design. | Revise attachment and delivery without compromising fit. |
| A cue fires after the action ends. | Stale scheduling or incorrect ownership. | Cancel by interaction identity and discard obsolete events. |

### Review the complete experience

Before accepting a design, establish the following:

- The touch has a clear purpose and an appropriate place in the whole task.
- Actual sensation, visual suggestion, and semantic meaning are distinguished.
- Body site, movement, grip, duration, and environmental conditions are explicit.
- Material, geometry, force, timing, and sound support the intended character.
- State transitions and pattern meanings are truthful and consistent.
- The mechanism and hardware can deliver the properties being promised.
- Frequent and prolonged use remain tolerable, with room for individual preference.
- Essential state and operation remain accessible when haptics are absent.
- Contact, interruption, failure, cleaning, wear, and production variation have appropriate checks.
- The specification identifies what has actually been built, measured, felt, and tested.

Accept the design when it supports its intended action and character under representative conditions. Retain unresolved physical or user-testing questions explicitly instead of treating a convincing description as proof of feel.
