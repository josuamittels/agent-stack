---
name: "sound-design"
description: "Reference for understanding, composing, synthesising, shaping, implementing, and judging sound, including perception, emotion, musical structure, and audio for technology products."
version: "0.2.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "Henry Reich"
  - "Aatish Bhatia"
  - "William A. Sethares"
  - "Hans Zimmer"
  - "Yo-Yo Ma"
  - "Resonance Sound Design"
  - "Josh H. McDermott"
  - "Raja Marjieh"
  - "Peter M. C. Harrison"
  - "Patrik N. Juslin"
  - "Daniel Västfjäll"
  - "Miller Puckette"
  - "Robert Hutchinson"
  - "Simon Fraser University Sonic Studio"
  - "Stephen A. Brewster"
  - "Peter C. Wright"
  - "Alistair D. N. Edwards"
  - "Harrison Zafrin"
  - "Conor O’Sullivan"
  - "Apple"
  - "Microsoft"
  - "World Wide Web Consortium"
  - "International Telecommunication Union"
  - "MDN contributors"
type: reference
status: "experimental"
---

# Sound design

Sound gives events a material character, organises attention through time, and suggests relationships between bodies, places, actions, and feelings. Its meaning emerges from the signal, the listener, and the situation. A technically clean sound can be emotionally empty; a rough recording can be exactly right.

Use this guide to reason about music, effects, ambience, voice, sonic identity, and interactive feedback. A good result fulfils its intended role with a coherent form, an appropriate demand on attention, and convincing behaviour on the playback system. Pleasantness, realism, novelty, and complexity are choices within that purpose.

## Use this reference

This guide owns auditory perception, acoustic character, musical structure, sound construction, sonic vocabulary, mixing, and playback. Apply the shared [framework](reference.md) for decision priorities, requirements language, and evidence.

For UI, start with [1](#1-frame-the-sound), [3](#3-understand-hearing), and [11–15](#11-design-product-sound-systems). Use [2](#2-understand-the-material) and [8–10](#8-construct-a-sound) when producing audio; [4–7](#4-design-timbre-and-tuning-together) for musical composition. [Interaction](interaction.md) owns the event and attention policy; [Haptics](haptics.md) owns tactile reinforcement; [Accessibility](accessibility.md) owns equivalent access and media requirements.

## Contents

1. [Frame the sound](#1-frame-the-sound)
2. [Understand the material](#2-understand-the-material)
3. [Understand hearing](#3-understand-hearing)
4. [Design timbre and tuning together](#4-design-timbre-and-tuning-together)
5. [Shape emotion and meaning](#5-shape-emotion-and-meaning)
6. [Use musical structure](#6-use-musical-structure)
7. [Compose and perform](#7-compose-and-perform)
8. [Construct a sound](#8-construct-a-sound)
9. [Record and transform](#9-record-and-transform)
10. [Mix space and perspective](#10-mix-space-and-perspective)
11. [Design product sound systems](#11-design-product-sound-systems)
12. [Implement reliable playback](#12-implement-reliable-playback)
13. [Specify and deliver](#13-specify-and-deliver)
14. [Work through concrete examples](#14-work-through-concrete-examples)
15. [Listen, diagnose, and decide](#15-listen-diagnose-and-decide)

## 1. Frame the sound

Describe the event before choosing an instrument or preset. Establish who listens, what happens, what changes, what the listener should understand or experience, and what else is audible. For a narrative, define the point of view and emotional movement. For an interface, define the state transition and the value of hearing it.

Write a brief with these decisions:

| Decision | What to specify |
| --- | --- |
| Purpose | Confirmation, orientation, expression, atmosphere, warning, identity, or musical development. Name the primary job. |
| Context | Intended audience, cultural references, environment, playback devices, expected attention, and repetition. |
| Character | A few qualities with observable consequences: restrained means fewer events and less prominence; tactile means a credible contact transient. |
| Form | Duration, phrase or event structure, recognisable feature, and relationship to neighbouring sounds. |
| Constraints | Speech or music coexistence, available bandwidth, latency, channel layout, mute behaviour, production resources, and rights. |
| Evidence | What can be measured, what requires listening, and what requires testing with the intended audience. |

Translate adjectives into hypotheses. “Warm” might mean a rounded onset, restrained high-frequency energy, and a close perspective. “Premium” has no stable acoustic definition. Compare examples and identify the feature that actually matters. Do not change level, pitch, brightness, and timing together when trying to learn which feature caused a response.

For an AI, distinguish a proposed sound, an implemented signal, and an auditioned result. A patch description is not audio. A spectrum does not establish emotional effect. Report which channels were actually inspected; never claim to have heard a file from its transcript, filename, waveform, or code. Make original structures from references and preserve source and licence information for recordings and samples.

## 2. Understand the material

A sound in air is changing pressure transmitted through a medium. An audio signal represents that variation; a loudspeaker converts it back into physical motion. Playback hardware and rooms therefore participate in the result.

### Frequency, time, amplitude, and phase

A sinusoid can be written as `x(t) = A sin(2πft + φ)`, where `A` is amplitude, `f` is frequency in hertz, `t` is time in seconds, and `φ` is phase. Its period is `1/f`. Complex signals combine components whose amplitudes and frequencies can evolve independently.

- **Frequency and pitch:** frequency is a physical repetition rate; pitch is a percept. Some sounds have a clear pitch, some have several candidates, and some have none. Raising frequency generally raises pitch, but spectra, duration, and listening conditions affect perception.
- **Amplitude and loudness:** amplitude is signal magnitude; loudness is perceived strength. Frequency balance, duration, masking, and playback level also matter.
- **Phase:** relative position within a cycle affects how overlapping signals add. The same signal delayed against itself can reinforce some frequencies and cancel others. Phase relationships matter in layered transients, stereo processing, and mono playback.
- **Time:** onsets, offsets, gaps, duration, and rates of change shape identity as strongly as steady-state tone. Listen to how a sound arrives, develops, and leaves.

### Spectrum, timbre, and envelope

A **partial** is a frequency component. A **harmonic** is a component at an integer multiple of a fundamental: `f, 2f, 3f…`. An **overtone** lies above the fundamental; it need not be harmonic. The first overtone of an ideal harmonic tone is its second harmonic. Inharmonic partials occur in many bells, bars, membranes, and synthetic sounds. Inharmonicity can be an intended material quality.

**Timbre** includes spectral balance, noise, onset, internal motion, and decay. Two sounds with the same fundamental can differ radically in character. A missing fundamental can still be perceived from the organisation of its harmonics; the lowest measured spectral peak is therefore not always the perceived pitch.

An amplitude **envelope** describes magnitude over time. In an attack-decay-sustain-release envelope, attack reaches the initial peak, decay approaches the sustain level, sustain is a level held while the note continues, and release follows note-off. Sustain is not a duration. One-shot impacts often need only an onset and decay. Shape pitch and spectral envelopes separately: an impact can begin bright and noisy, then leave a simpler ringing body.

A waveform shows signal variation through time; a spectrum shows frequency content over an analysis window; a spectrogram shows how that content changes. Short windows reveal timing better, while long windows resolve nearby frequencies better. Use these views to investigate a listening question, not to infer beauty from an attractive plot.

### Levels and units

Decibels express ratios. For comparable amplitudes, `ΔdB = 20 log10(A2/A1)`; for powers, use `10 log10(P2/P1)`. Doubling amplitude adds about 6 dB. This does not mean twice the perceived loudness.

| Unit | Meaning | Design consequence |
| --- | --- | --- |
| dBFS | Digital level relative to full scale. | Check clipping at fixed-range outputs. Floating-point processing headroom does not protect the final converter or export. |
| dBTP | Estimated peak of the reconstructed waveform. | Check intersample peaks and peaks introduced by conversion or encoding. |
| LUFS / LKFS | Frequency-weighted programme loudness relative to digital full scale. | Compare appropriate programme material with a defined measurement method. |
| dB SPL | Physical sound pressure level relative to 20 µPa in air. | Requires an acoustic measurement or calibrated playback relationship. |

A file level cannot guarantee a listening SPL. Do not equate a device's volume percentage with acoustic loudness or safety. Judge at comfortable levels and avoid using increased playback volume to compensate for fatigue or a weak mix.

## 3. Understand hearing

The outer and middle ear transmit vibration; the cochlea analyses it through overlapping frequency-sensitive regions. Auditory processing then organises changing activity into perceptual sources. Hearing is selective and inferential rather than an exact transcription of a waveform.

### Sensitivity and masking

Equal signal amplitudes at different frequencies need not sound equally loud. Sensitivity also changes with playback level. A bass-heavy mix that feels balanced loudly can lose weight quietly; boosting bass cannot make a small speaker reproduce energy outside its useful range.

**Masking** makes a sound harder to hear because another sound is present or occurs nearby in time. It does not remove the masked signal from the file. Competition depends on spectrum, level, timing, and listening conditions. A short cue can disappear behind speech, a percussion hit, or its own dense tail.

First try a gap, a shorter tail, a different register, a clearer transient, or a less crowded arrangement. Increase level only when that serves the listening context. Preserve speech intelligibility by reducing competing activity where and when speech needs space; no fixed equalisation cut solves every voice.

### Grouping, attention, and repetition

Common onsets and harmonic relationships can make components belong to one apparent source. Separated onsets, contrasting registers, and distinct rhythms can help sources separate. This supports two different tasks: fuse layers into one convincing object, or make concurrent messages distinguishable.

A sudden change captures attention relative to its surroundings. A soft isolated event may be conspicuous in a quiet room; a loud steady bed may recede during a busy scene. Do not judge salience from peak level alone. Familiar cues can become easier to recognise while becoming less consciously noticeable. Repetition may also reveal irritation that a first impression misses.

### Spatial hearing

Differences in arrival time and level between ears, spectral filtering by the head and outer ears, reflections, and head movement contribute to localisation. Stereo panning is one spatial cue; it does not reproduce every property of a source in three-dimensional space.

Keep critical information recoverable with one ear, mono playback, and imperfect localisation. Headphone spatialisation based on a generic head-related transfer function may vary in effectiveness across listeners. Use space to support meaning and separation, then test the actual playback route.

## 4. Design timbre and tuning together

Separate four questions:

1. **Roughness:** do nearby components produce rapid fluctuations or unresolved interference?
2. **Harmonicity:** does the combined spectrum resemble multiples of a common fundamental?
3. **Musical function:** what does the sonority imply within the established style and sequence?
4. **Preference:** does this listener value the result here?

These questions interact, but their answers need not agree. A smooth chord can remain unresolved; a rough texture can be pleasurable; an unfamiliar consonant interval can have little musical meaning.

### Beats, roughness, and partial interactions

Two nearby sinusoids in the same channel produce beats at the absolute frequency difference: 440 and 442 Hz produce two amplitude beats per second. As separation grows, slow fluctuation can become roughness and, eventually, distinguishable tones. The boundaries depend on frequency, level, and stimulus. A fixed difference in hertz does not describe the same perceptual spacing everywhere.

For complex tones, interactions occur between partials as well as fundamentals. Pairwise roughness models weight these interactions and sum them across the spectrum. Sweeping an interval produces a curve with peaks and local minima; varying two notes above a fixed note produces a surface of triads. The positions of its valleys depend on the chosen spectra and model assumptions.

With harmonic tones, several low-order partials align near simple ratios. With inharmonic spectra, the smoother intervals can move. The model does not predict a complete aesthetic judgement: it simplifies time evolution, perceptual weighting, masking, and nonlinear interactions, and it does not supply a theory of musical syntax.

Include interactions within each tone when they matter: a single inharmonic sound can already have intrinsic roughness. State whether a calculation includes this baseline. In a triad surface, each of the three note pairs contributes a relationship; a low-roughness relationship with the bass does not guarantee agreement between the upper notes. Compare the complete voicing.

### Tuning choices

An octave has a frequency ratio of `2:1`. In twelve-tone equal temperament, a semitone multiplies frequency by `2^(1/12)`, and `n` semitones multiply it by `2^(n/12)`. Cents express logarithmic distance: `1200 log2(f2/f1)`. An octave contains 1200 cents.

**Just intonation** uses specified rational frequency ratios. A just fifth is `3:2`; a just major third is `5:4`, about 386 cents, compared with 400 cents in equal temperament. These ratios can reduce selected interactions in harmonic spectra. Fixed just ratios can conflict when harmony changes, while equal temperament permits consistent transposition across its pitch system. Neither is a universal optimum.

Choose tuning, register, voicing, and timbre as a system:

- For dense low chords, first spread the lower voices or reduce sustained upper partials. Transposing every voice together may preserve the congestion.
- For bell-like or stretched spectra, compare interval choices on the actual patch. A keyboard label does not establish spectral agreement.
- Use slight detuning deliberately for slow beating or width. Check whether the motion feels alive or unstable in context.
- Preserve intentional beating in traditions and instruments where it is part of the desired character. Eliminating every beat can erase that character.
- Treat tuning systems beyond twelve-tone equal temperament as coherent practices with their own structures and performance conventions. Acoustic models can suggest relationships; they do not establish a culture's musical history or preferences.

A useful experiment holds envelope and level comparable while changing the spectrum from a sine to a harmonic complex to an inharmonic complex. Compare the same intervals, then alter their tuning. Record what was heard separately from what the model predicted. Pure-tone roughness alone does not explain all special roles of octaves, fifths, or other musical intervals.

For a more diagnostic comparison, build the harmonic complex one partial at a time. Adding `2f` creates an opportunity for alignment at the octave; adding `3f` introduces alignment at a fifth; adding `4f` supports a fourth relationship. This exposes which components make a tuning difference audible. Compare same-channel presentation with a tone sent separately to each ear; the acoustic mixture and perceptual interactions change. Do not assume that splitting tones between ears eliminates every kind of beating or dissonance.

Real instruments complicate an ideal harmonic spectrum. Stiff piano strings can have stretched partials, contributing to the practice of stretching the tuning across the keyboard. Body resonances and radiation also shape a recorded instrument differently across notes. Test the sampled or modelled instrument across its working register rather than extrapolating from one stationary note.

## 5. Shape emotion and meaning

Distinguish **expressed emotion**, which a listener recognises in a sound, from **felt emotion**, which the listener experiences, and **aesthetic judgement**, which concerns the experience's value. Sad music can be comforting or pleasurable. Recognising urgency does not mean enjoying it.

Emotion can arise through several routes: abrupt acoustic change, expressive resemblance to gesture or voice, learned associations, personal memory, imagined scenes, expectations, rhythmic engagement, and the significance of the situation. These are explanatory possibilities, not switches an AI can reliably activate.

Valence, the positive or negative character of a response, and arousal, its degree of activation, help specify intent. They do not exhaust tenderness, awe, ambiguity, nostalgia, humour, or mixed feeling. Define the intended trajectory, such as guarded curiosity becoming relief, rather than assigning one emotion to a whole piece.

### Translate feeling into coordinated choices

The following are craft hypotheses to audition. Their effect depends on style, listener, and context.

| Intended quality | Candidate treatment | Tradeoff or counterexample |
| --- | --- | --- |
| Intimacy | Close perspective, exposed detail, restrained density, phrase-level dynamic movement. | Close breath or friction can feel intrusive; quietness alone may seem distant. |
| Energy | Clear pulse, active articulation, faster event density, strong contrast. | High tempo with soft attacks can float; slow music can be forceful. |
| Calm | Predictable behaviour, rounded transients, room between events, limited spectral agitation. | Excessive predictability can feel inert; familiar sounds may carry unwanted memories. |
| Suspense | Delayed completion, unstable texture, withheld bass resolution, silence around significant events. | Continuous maximal tension removes contrast and becomes tiring. |
| Weight | A firm onset and substantial body, slower resonant decay, grounded low-mid structure. | Sub-bass alone may vanish on the target device or obscure detail. |
| Fragility | Sparse exposure, delicate articulation, narrow dynamic margin, incomplete closure. | Weak audibility or random instability can read as a defect. |
| Delight | A small, intelligible surprise within an established pattern. | A conspicuous flourish can become irritating when repeated. |

Major does not guarantee happiness, minor does not guarantee sadness, and a key name does not encode a universal emotional character. Register, instrument resonances, tuning, learned associations, and performance can make transposition matter. Choose a key for the actual voice or sound, not a chart of supposedly inherent emotions.

Establish enough regularity for a deviation to mean something. Repetition can teach a motif, a rhythmic expectation, or a product cue. Change one consequential relationship at the right moment. An expectation must exist before its fulfilment or violation can carry much force.

## 6. Use musical structure

Musical theory names relationships and practices. Apply the system relevant to the work; the following tonal vocabulary is a useful working foundation rather than a definition of all music.

### Pitch, scales, and melody

An **interval** relates two pitches; a **scale** supplies an ordered pitch collection; a **key** establishes a tonal centre and relationships around it. A **mode** supplies a particular organisation of scale degrees. Pitch classes group octave-related pitches, but register remains audible and consequential.

The major scale uses semitone steps `2–2–1–2–2–2–1`; natural minor uses `2–1–2–2–1–2–2`. Harmonic and melodic minor alter degrees for particular harmonic or melodic purposes. Other modal, chromatic, pentatonic, microtonal, and non-octave systems require their own context. A pitch collection alone does not specify how to compose in a tradition.

A scale organises notes across time as well as simultaneous combinations. A semitone can be rough in a sustained cluster and useful as a melodic neighbour or directed step. Do not build a melody solely by selecting minima from a simultaneous-roughness curve.

A melody needs a perceptible shape and hierarchy. Establish a central gesture, a contour, significant arrivals, and room for breath. Stepwise motion can connect; a leap can mark an event; a repeated note can gain meaning through rhythm or harmony. Judge the phrase's direction before adding ornament. A motif may be primarily rhythmic, timbral, or gestural rather than a tune.

### Harmony, voicing, and motion

A chord names a pitch collection; its **voicing** determines the register, spacing, and doubling of its notes. An **inversion** changes the bass member. Two voicings of the same chord can differ more in impact than two chord labels suggest.

| Construction | Semitones above the root in equal temperament | Typical use within tonal practice |
| --- | --- | --- |
| Major triad | 0, 4, 7 | A clearly defined major sonority. |
| Minor triad | 0, 3, 7 | A clearly defined minor sonority. |
| Diminished triad | 0, 3, 6 | Instability or directed connection in suitable contexts. |
| Augmented triad | 0, 4, 8 | Symmetry and ambiguous direction. |
| Suspended second / fourth | 0, 2, 7 / 0, 5, 7 | An omitted third and an open or suspended character. |
| Seventh or extended chord | Add selected sevenths, ninths, elevenths, or thirteenths. | Added colour or function; spacing and omissions determine clarity. |

In functional tonality, tonic supports arrival, predominant prepares motion, and dominant can create an expectation of return. A dominant seventh resolving to tonic derives direction from the established key and the movement of its voices. A roughness number cannot supply that context. Modal harmony, drones, parallel planing, quartal structures, and sound masses can organise music through other relationships.

**Voice leading** concerns the paths of individual parts. Retain common tones and move other voices economically when continuity is desired. Use contrary motion or independent rhythms when parts need separate identities. Deliberate parallel motion can create a unified block. Restrictions from a particular counterpoint style are not universal quality rules.

The bass can change the apparent foundation without changing the upper motif. Harmonic rhythm, the rate of chord change, can accelerate a passage while tempo stays fixed. Avoid changing every chord, bass note, texture, and melody at once unless the moment needs a rupture.

For example, in C major, `Dm7 → G7 → Cmaj7` supplies a predominant–dominant–tonic sequence. Over bass notes D, G, and C, use upper voices `F–A–C → F–G–B → E–G–B`. F stays during the first change, A and C descend, and F then resolves to E while G and B remain. The G7 voicing omits its fifth; the last chord retains B as a major seventh and closes differently from a plain C triad. Compare both endings with the same rhythm and timbre, then change the bass spacing. This separates function, voice leading, and voicing.

### Rhythm, metre, and form

**Pulse** is a recurring reference; **tempo** is its rate; **metre** groups beats; **rhythm** arranges events and durations. At 120 beats per minute, a beat lasts 500 ms. The perceived pace also depends on subdivision, accents, note lengths, and density.

Syncopation displaces emphasis against an established metric expectation. Swing changes subdivision timing according to style and performance; it is not one universal delay percentage. A 3:2 polyrhythm places three evenly spaced events against two over a shared span. Use such relationships when they create a legible interaction, not to display arithmetic.

At larger scales, make repetition, contrast, development, and return perceptible. A short cue may need only onset, implication, and closure. Longer music may use an A–B–A return, a changing loop, a verse/refrain, or a gradual process. Choose form by the intended journey rather than filling a standard number of sections.

## 7. Compose and perform

### Build a world and a small generative idea

Define the work's palette early: source materials, register, rhythmic language, space, and permissible transformations. A constraint makes later departures audible. A single expressive instrument can establish a stronger identity than a large interchangeable ensemble.

Find a motif that can survive changes of texture. Develop it through altered rhythm, contour, register, harmony, articulation, or instrumentation. Augmentation lengthens its durations; diminution shortens them; fragmentation develops one part; inversion reverses its pitch direction. Preserve a recognisable feature so development remains connected to what came before.

Keep rough sketches before judging them as finished pieces. Compare genuinely different mechanisms: a held texture against a rhythmic motif, an exposed solo against a fused ensemble, or an unresolved ending against closure. Reorchestrating the same idea can reveal a new relationship; piling all variants together usually obscures the strongest one.

### Shape a foreground and an arc

Assign parts a role: lead, support, pulse, bass, atmosphere, or accent. Let the foreground move deliberately. Build intensity through density, register, harmonic activity, articulation, proximity, or spectral change as well as level. A climax needs room around it. Removing a layer can make the next event feel larger.

For picture, establish what the music reveals about the scene that image and dialogue do not already say. Support subtext, perspective, or continuity when useful. Hitting every edit or movement can overexplain the scene; exact synchronisation can also be an intentional style. Choose the moments of alignment.

Treat silence as a timed relationship. A rest can mark a phrase, preserve ambiguity, focus attention on another source, or make an arrival matter. Distinguish removing music from removing every environmental sound. The remaining acoustic world shapes the silence's meaning.

### Make performance carry intention

Specify articulation, phrase direction, dynamic contour, note length, timbral change, and the relationship between parts. Legato connection, detached attacks, accented entries, breath, bow changes, and release behaviour change the same written notes.

Write for the source's actual capabilities. Acoustic performers need feasible ranges, breathing or bowing, transitions, and recoverable physical gestures. A sampled or synthetic instrument can exceed those limits, but decide whether the result should suggest a physical performer or an invented instrument.

Humanisation needs structure. Vary timing and intensity around phrase hierarchy and shared ensemble behaviour; independent random offsets on every note can weaken intention. Allow expressive timing to return to a reference where the style needs one. During collaboration, describe the desired gesture or emotional movement as well as the technical instruction, then listen to what the performer contributes.

Music can connect people without communicating one identical message to everyone. Let intended listeners describe what they took from a performance before explaining what they were supposed to feel. Borrowing across practices is most productive when the relevant relationships, tuning, and articulation are understood, with source credit and collaboration where appropriate.

## 8. Construct a sound

Think in terms of **excitation, resonating body, evolution, and acoustic setting**. A hit, scrape, breath, oscillation, or noise burst supplies energy; a body or processing system shapes it; damping determines what remains. Even an impossible object benefits from consistent behaviour.

### Choose a construction method

| Method | Principal controls | Useful applications and limits |
| --- | --- | --- |
| Additive synthesis | Partial frequencies, levels, phases, and independent envelopes. | Precise harmonic or inharmonic structures; many static partials can sound lifeless. |
| Subtractive synthesis | Oscillator or noise source, filter shape, cutoff, resonance, envelopes. | Broad tonal shaping; a filter cannot restore source components that are absent. |
| Frequency or phase modulation | Carrier/modulator relationships and modulation depth through time. | Rich evolving spectra and metallic or tonal attacks; sidebands can change pitch clarity. |
| Wavetable synthesis | Table content, scan position, interpolation, modulation. | Continuous spectral movement; abrupt changes can introduce unwanted discontinuities. |
| Sampling | Recording, start point, pitch, playback speed, looping, articulation layers. | Detailed material identity; repetition and extreme transposition expose the source. |
| Granular synthesis | Grain duration, density, position, pitch, distribution, and windowing. | Transform recorded material into particles or sustained textures; dense overlap can blur the gesture. |
| Physical or modal modelling | Excitation, resonant modes, damping, coupling. | Coherent material-like behaviour; uncontrolled resonances can ring excessively. |
| Spectral processing | Analysis windows, component transformation, resynthesis. | Reshape recorded spectra; time/frequency tradeoffs and processing artefacts can smear attacks. |

An oscillator's waveform suggests a starting spectrum. A sine contains one component; an ideal saw contains all integer harmonics with decreasing amplitude; an ideal square contains odd harmonics; a triangle's upper odd harmonics fall more steeply. Actual digital implementations must manage bandlimiting.

Low-frequency modulation can create tremolo through amplitude, vibrato through pitch, or slow brightness movement through filtering. Audio-rate modulation changes the spectrum. In simple sinusoidal FM, sidebands occur around the carrier at multiples of the modulation frequency; their levels depend on modulation depth. Listen for the intended pitch rather than assuming the carrier alone determines it.

White noise has equal power per unit bandwidth; pink noise has approximately equal power per octave. Filtered noise can suggest friction, air, or diffuse material. Noise need not be an unwanted contaminant.

### Build in a useful order

1. Create the core gesture with one source. Establish pitch or noise character, onset, duration, and decay.
2. Shape spectral evolution. Decide which components appear first and which persist. A uniformly sustained spectrum often lacks a material story.
3. Add a layer only for a distinct role: contact, body, friction, air, resonance, or space. Remove layers that duplicate the same job.
4. Align layers when they should form one event. Use a delayed component only when it reads as a secondary action or reflection.
5. Map meaningful variation. Velocity might affect excitation and brightness together; pressure might affect intensity and noise; size might affect resonance and decay.
6. Recheck the whole gesture at its intended level and rate of recurrence. Preserve its recognisable feature during variation.

Small onset or release ramps can prevent clicks caused by abrupt discontinuities. Set them by the signal and desired attack: a ramp long enough to erase a deliberate contact transient changes the gesture. Smooth parameter jumps as well as note boundaries.

## 9. Record and transform

Choose a source for its behaviour, not only its everyday identity. A small object recorded closely and slowed can suggest weight; layered friction can suggest machinery; a resonant room can supply the character of an invented place. The transformation must preserve whatever makes the event credible.

Record useful variations of force, position, material contact, and distance. Leave headroom, capture room tone and tails, and check handling noise, wind, and unwanted reflections. Microphone position changes directness and spectral balance; correcting a poor position with processing may lose useful detail.

| Transformation | What it changes | Listen for |
| --- | --- | --- |
| Playback-speed change | Duration and pitch together. | Altered material scale, transient weight, lost high-frequency detail. |
| Independent time stretch or pitch shift | Duration or pitch with partial independence. | Smearing, grain, formant changes, phase artefacts. |
| Reverse | The temporal order of attack and decay. | Anticipation or an unnatural suction gesture; it may cease to identify the source. |
| Equalisation and filtering | Spectral balance or resonant regions. | Clarity and material identity; excessive cuts can hollow the body. |
| Saturation or distortion | Nonlinear spectral and dynamic change. | Added density or aggression, new partials, aliasing, lost transient definition. |
| Compression or expansion | Level-dependent dynamics. | Attack shape, sustain, noise emphasis, pumping, recovery between events. |
| Convolution | Response of a chosen impulse system. | Space or resonant identity, plus loss of clarity or excess tail. |
| Delay and modulation effects | Repetition, movement, or changing phase relationships. | Rhythmic clutter, artificial width, cancellation in mono. |

Processor order changes the result. Distortion before a filter generates components that the filter can remove; distortion after the filter can generate new components. Compression before reverb changes the excitation; compression after it also acts on the tail. Compare routes at matched apparent loudness.

For compression, the threshold establishes where reduction begins, the ratio determines how strongly level above it is reduced, and the knee shapes the transition. Attack and release govern how the gain reduction responds and recovers. A fast attack can reduce impact; a release that does not recover between hits can flatten a sequence. Makeup gain can conceal that loss by making the result louder. For filters, distinguish cutoff, slope, and resonance: raising resonance emphasises a region and can create ringing rather than merely making the sound brighter.

Use denoising and editing to remove distractions while retaining useful breath, friction, and room character. Destructive cleaning can leave modulation artefacts or an unnaturally empty recording. Keep an editable original and document meaningful transformations.

## 10. Mix space and perspective

Make the intended foreground intelligible, then decide the supporting balance. Equal peak readings do not imply equal prominence. Solve arrangement and timing conflicts before accumulating corrective processors.

**Depth** depends on the direct-to-reverberant relationship, reflections, spectrum, level, and source detail. Lowering gain alone may sound like a quiet nearby source. A more distant perspective often needs several cues together, but low-pass filtering is not a universal distance law.

**Reverberation** establishes a surrounding acoustic response. Early reflections help suggest boundaries and position; the later tail suggests persistence and enclosure. Pre-delay separates the direct event from reverberant onset. Decay time, damping, diffusion, and wet/dry balance should support the imagined space and the pace of events. A long bright tail on a frequently repeated cue can dominate its identity and obscure later actions.

**Width** is separate from depth. Contrast a stable focal source with a wider bed when that clarifies the scene. Phase-based widening can lose energy in mono; hard panning can lose information with one earbud. A stable central component is useful for essential cues.

For interactive scenes, decide whether a sound belongs to an object, the surrounding world, or the listener's interface. Apply distance, occlusion, orientation, and movement consistently with that role. Do not attach world attenuation to information that must remain available regardless of camera position. Distinguish stereo presentation from spatially tracked audio.

Automation can make room for a significant line or event without permanently thinning the mix. Use ducking, the temporary reduction of another signal, with controlled entry and recovery. Avoid audible pumping unless it is part of the desired rhythm.

In a soundscape, separate a continuous environmental bed, recognisable recurring activity, and occasional foreground events. Vary their relationships rather than filling every frequency and moment. A stable background can make one changed detail meaningful. For voice, protect consonant detail and phrase boundaries; breath, pauses, pitch contour, and emphasis carry intention. When voice communicates instructions, prioritise intelligibility and natural pacing over decorative processing, and test every supported language with its actual speech rhythm.

## 11. Design product sound systems

### Decide when sound earns attention

Use sound where it provides information across distance, confirms an otherwise uncertain action, supports eyes-free operation, conveys continuous change, or contributes meaningfully to the experience. For ordinary screen interfaces, default to quiet behaviour for frequent, obvious actions. Immersive, musical, and explicitly auditory products may need continuous or spatial feedback.

| Role | Design priority | Common failure |
| --- | --- | --- |
| Contact or manipulation | A credible relation between gesture and response. | A long flourish for every small action. |
| Completion | Clear closure after an outcome is known. | Celebrating submission before it succeeds. |
| Notification | Recognisability and proportionate interruption. | Every event competing for highest priority. |
| Recoverable error | A distinct invitation to inspect and act. | Punitive or alarming sound for a routine correction. |
| Urgent alert | Reliable detection and appropriate action. | Treating a pleasant chime as a validated alarm system. |
| Continuous state | Legible mapping from change to sound. | A loop that conveys activity while the operation has stalled. |
| Sonic identity | A memorable relationship across relevant experiences. | Replaying a brand signature where it delays the task. |

An **auditory icon** borrows a recognisable everyday event, such as a container closing. An **earcon** is an abstract learned pattern, such as a short sequence that identifies completion. **Sonification** maps data or state to sound. Naturalistic sounds are not automatically intuitive, and abstract sounds are not automatically unusable. Test the mapping.

### Build a coherent and distinguishable family

Define shared materials, a register range, envelope character, spatial treatment, and a small rhythmic vocabulary. Give semantic opposites distinct gestures. Use differences that survive ordinary playback, rather than relying only on a tiny pitch shift or level change.

A family might use a dry contact for a local action, a related two-event gesture for completion, and a contrasting rhythm for an error. Shared timbre establishes kinship; rhythm and contour distinguish roles. Avoid encoding many independent variables in one brief cue. If training is required, provide it and test recognition after a delay.

Pitch rises can suggest increasing quantity or completion in some contexts, but a rising gesture is not a universal “success” symbol. Choose mappings consistently and validate them with intended users. For continuous parameters, decide whether pitch, rate, roughness, or another dimension gives a usable ordering; test distinguishability across the actual range.

### Compose the event stream

A product is heard as a sequence, sometimes alongside several other products. Define a priority and concurrency policy, not only an asset library.

- Merge bursts of equivalent notifications where individual sounds add no information.
- Set per-event cooldowns and concurrency limits appropriate to meaning and recurrence.
- Let a consequential event interrupt a decorative tail, using a clean release where possible.
- Drop stale feedback. Do not play an old success cue after a newer failure or cancellation.
- Avoid endlessly queuing sounds that describe states which have already passed.
- Reserve explicit acknowledgement or escalation for events that actually need it. Safety-critical alarms require their domain's standards and validation.

Keep functional identity stable during variation. Small changes of performance or excitation can reduce mechanical sameness; random pitch changes can confuse a musical vocabulary or collide with concurrent audio. A large variant bank does not fix an irritating core gesture.

### Respect the listener's context

Apply [Accessibility’s equivalent-media requirements](accessibility.md#17-provide-image-audio-and-video-equivalents) and [automatic-audio controls](accessibility.md#provide-control-over-automatic-content), with [Interaction’s attention policy](interaction.md#14-protect-attention-and-informed-choice). Use [Haptics](haptics.md#13-coordinate-touch-sight-and-sound) for tactile coordination.

Audition alongside screen-reader speech and realistic competing audio. High-frequency-only or stereo-only distinctions can vanish with hearing differences or a changed output route. Shared rooms and recognizable audible cues can expose private activity. Keep the same sonic role intelligible at low level, in mono, and through the product's supported listening conditions.

## 12. Implement reliable playback

Bind playback to [Interaction’s feedback events](interaction.md#11-communicate-response-and-progress) and [asynchronous-state contract](interaction.md#12-keep-asynchronous-work-trustworthy). Keep audio-engine scheduling separate from application state.

Preload and decode frequently needed assets before their moment of use. Schedule rhythmic events against the audio engine's clock rather than repeated UI timers. Account for output latency, including wireless routes; no one latency budget fits musical performance, ambient playback, and ordinary notifications.

For Web Audio, create or resume an `AudioContext` through an appropriate user interaction, handle its suspended state, and tolerate denied playback. Reuse the context and decoded buffers as appropriate; create new one-shot source nodes for each playback. Smooth gain changes, stop obsolete voices, and release resources. Avoid main-thread work or network fetches on a timing-critical path.

For native products, select audio-session behaviour according to the sound's role. Decide whether other audio mixes, ducks, or pauses; whether background playback is justified; and what happens on calls, route changes, and headphone disconnection. Verify the current platform contract instead of assuming every device treats silent mode identically.

Expose separate controls for materially different roles, such as effects, music, and voice, when the experience needs them. Honour the system's final volume control. Restore interrupted playback only when the user's context and platform policy justify it.

## 13. Specify and deliver

### Render with a defined technical contract

Choose sample rate, channel count, format, and runtime behaviour for the destination. A 48 kHz production master is a practical default for many audiovisual pipelines; use the established rate when another pipeline requires it. Higher sample rates do not automatically improve a poorly constructed sound.

Frequencies above half the sample rate cannot be represented unambiguously. Use appropriate antialiasing when sampling and bandlimited generation when synthesising. Nonlinear processing and modulation can create new high-frequency components; oversampling with proper filtering may help. Increasing output sample rate after aliasing does not recover the lost distinction.

Keep lossless editable masters, commonly floating-point or 24-bit PCM according to the workflow. When reducing to an integer bit depth, use appropriate dither at the final reduction where needed. Evaluate runtime encodings after decoding: short transients, gaps, and loop boundaries can change. Do not repeatedly encode a lossy intermediate.

Use true-peak checks and a documented margin suited to conversion and encoding. Retain room for simultaneous cues and mix buses. A limiter can catch peaks but cannot repair poor hierarchy. Do not normalise every cue to the same sample peak or import a streaming loudness target into a UI library without a reason.

Programme loudness methods use defined integration and gating windows; very short cues may be shorter than those windows. Compare microcues through consistent measurement windows, peaks, and listening in context. Record the method rather than reporting an unexplained LUFS value as proof of balance.

Trim unintended leading silence while preserving intentional anticipation. Retain a natural or designed release. Check loops for discontinuities, repeated landmarks, stereo behaviour, and phase-dependent cancellation. A zero-crossing edit alone does not guarantee a clean stereo loop or consistent texture.

### Handoff specification

For each asset or procedural patch, record:

- Semantic event, intended meaning, trigger, cancellation, and priority.
- Source or synthesis graph, tuning, envelope, processing, and allowed variation.
- File or patch identifier, version, duration, channels, sample rate, and encoding.
- Gain reference, peak checks, measurement method, looping, and overlap rules.
- Source provenance and rights, target devices, controls, and accessible equivalents.
- Checks completed and perceptual questions still requiring audition or user testing.

The specification should reproduce the behaviour without relying on an adjective such as “friendly”. Keep technical metadata out of the product's ordinary user flow unless the user needs it to make a choice.

## 14. Work through concrete examples

These are proposed starting specifications, not auditioned presets or universal targets.

### Quiet completion cue

**Brief:** confirm that a user-initiated export has completed in a desktop tool. It may recur during a working session and must coexist with speech or music.

Start with two short, rounded tonal events, 90 ms apart, at 660 and 880 Hz. Each uses a fundamental and a quieter second harmonic, a 5 ms onset, and an approximately 120 ms decay. Begin the second event below the first event's level; adjust that relationship by listening because pitch changes can alter apparent prominence. Use little or no reverb and retain a mono-compatible core.

The 4:3 relationship and shared spectrum propose a coherent family; the sequence proposes closure. Neither establishes that listeners will identify success. Compare a single event and a nonpitched alternative if the two-note version sounds too musical. Trigger only on confirmed completion, suppress obsolete results, provide a visible status, and test recurrence before adding ornament.

### Tension without continuous loudness

**Brief:** a character appears composed while anticipating an uncertain outcome. The scene includes dialogue and ends without resolution.

Use a sparse motif with one withheld answer, an exposed register, and a slowly changing supporting texture. Maintain intensity through a constrained spectral or harmonic instability; avoid filling every gap. Let the texture approach an arrival, then remove the expected resolving event. Place the most exposed motion between important lines rather than underneath them.

Compare the scene with no score. If performance and sound already hold the tension, the composition may need fewer entries. Specify phrasing and perspective before increasing layers or volume. A roughness curve may help inspect the texture's components, but cannot decide whether the scene feels suspenseful.

### Coherent material for an invented object

**Brief:** a small virtual mechanism should feel precise and slightly elastic without imitating an existing device.

Begin with a brief filtered-noise contact, followed by a quiet resonator with several controlled modes. Make the upper modes decay sooner than the lower body. For stronger gestures, increase excitation and initial brightness together within bounds; preserve the characteristic mode relationships. Add a small rebound only if it reads as a second physical action.

Compare variants with the same contact but different damping, then with the same body but different contacts. This reveals whether material identity comes from the onset or resonance. Check rapid manipulation and overlapping instances: a compelling single strike can become a tonal wash. Remove a redundant layer before adding another effect.

## 15. Listen, diagnose, and decide

### Match the evidence to the claim

Use four complementary checks:

| Check | What it can establish | What it cannot establish alone |
| --- | --- | --- |
| Signal inspection | Duration, spectrum, clipping, discontinuities, channel and encoding properties. | Pleasure, semantic clarity, or emotional effect. |
| Comparative listening | Audible differences and fit under stated playback conditions. | A universal preference or reliable interpretation by all users. |
| Contextual prototype | Timing, overlap, speech competition, controls, and state correctness. | Long-term comfort or cultural interpretation across audiences. |
| Intended-listener testing | Recognition, confusion, response, preference, and fatigue in the tested conditions. | Effects outside those conditions without further evidence. |

Compare candidates at comparable apparent loudness, include the current baseline or silence, and vary order where practical. Begin with the whole event or scene, then isolate the suspected problem. Rejoin the mix after every repair. Solo listening can justify a change that damages the whole.

Test on representative speakers and headphones, at low and ordinary levels, in mono, and alongside realistic competing audio. Listen through a representative session, including dense bursts and quiet periods. A short loop is useful for detecting artefacts but can exaggerate annoyance; realistic recurrence is needed for a product judgement.

Ask separately what a cue meant, whether it was noticed, whether it was pleasant, and whether it helped. Measure confusions between sound roles and false impressions of completion, not only average preference. Preserve minority reports where they reveal an access or context problem.

### Diagnose the cause before changing the signal

| Symptom | Possible cause | First useful comparison |
| --- | --- | --- |
| Harsh or tiring | Excess upper-mid energy, strong roughness, too abrupt an onset, or excessive recurrence. | Match level, then change spectrum, onset, and event rate separately. |
| Muddy or indistinct | Crowded low voices, overlapping decays, resonances, or competing layers. | Remove layers or shorten tails before boosting treble. |
| Thin on small speakers | Identity depends on unreproduced bass or stereo differences. | Add useful audible body or harmonics; compare mono on the target device. |
| Artificial in an unwanted way | Static spectrum, implausible envelopes, identical retriggers, or random expression. | Add one meaningful dependency between excitation and response. |
| Beautiful but uninformative | Semantic roles share the same gesture or require unavailable context. | Contrast rhythm or articulation and test recognition without explanation. |
| Weak despite high level | Poor transient contrast, masking, or no phrase hierarchy. | Open space around the important event and compare at equal loudness. |
| Detached from interaction | Wrong trigger, latency, excess tail, or mismatched gesture. | Inspect the state transition and onset together in the prototype. |
| Impressive once, irritating later | Excess ornament, salience, repetition, or an attention-seeking tail. | Test a shorter, quieter version and a version with fewer triggers. |

Keep a sound when its purpose is intelligible, its form supports the intended experience, its technical behaviour is reliable, and its attention cost is justified under realistic listening. State remaining uncertainty precisely. A claim of emotional success needs listener evidence; a claim of completed audio review needs actual access to audio.
