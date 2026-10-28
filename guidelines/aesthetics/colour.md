---
name: colour
description: "Colour reference for perception, history and language, descriptive vocabulary, theory, models and formats, conversion, composition, palettes, meaning and psychology, accessibility, interface systems, visualisation, and colour-managed production."
version: "0.1.0"
updated: "2026-10-28"
author:
  - "Josua Mittelstaedt"
references:
  - "World Wide Web Consortium"
  - "Apple"
  - "International Color Consortium"
  - "International Commission on Illumination"
  - "Björn Ottosson"
  - "Paul Kay"
  - "Brent Berlin"
  - "Vox"
  - "Terry Regier"
  - "Edward Gibson"
  - "Noga Zaslavsky"
  - "Jonathan Winawer"
  - "Delwin T. Lindsey"
  - "Angela M. Brown"
  - "Josef Albers"
  - "Albert H. Munsell"
  - "Cynthia Brewer"
  - "Samantha Remboldt"
  - "Andrew J. Elliot"
  - "Markus A. Maier"
  - "Pantone"
type: reference
status: experimental
---

# Colour

Colour is a perceptual experience produced by light, an observer, and a viewing context. A useful colour decision connects that experience to a purpose. It makes an action recognisable, separates information, establishes an atmosphere, or preserves an identity across materials.

Use this guide when choosing, describing, combining, implementing, converting, or reviewing colour in identities, interfaces, publications, images, and physical production. It covers the concepts needed for dependable decisions without replacing a specialist colour-science, press, or accessibility assessment.

**Requirements** protect information, access, and correct reproduction. **Defaults** provide a practical starting point. Harmony schemes, emotional associations, and numerical aesthetic ranges are proposals to test in context. A colour is not approved in isolation. Approve its role, neighbours, scale, state, and output conditions together.

## Contents

1. [Define the colour task](#1-define-the-colour-task)
2. [Understand light and perception](#2-understand-light-and-perception)
3. [Use history to distinguish different problems](#3-use-history-to-distinguish-different-problems)
4. [Separate colour, language, and categorisation](#4-separate-colour-language-and-categorisation)
5. [Describe colour precisely](#5-describe-colour-precisely)
6. [Choose models, spaces, and formats](#6-choose-models-spaces-and-formats)
7. [Construct and mix colours](#7-construct-and-mix-colours)
8. [Convert without losing the specification](#8-convert-without-losing-the-specification)
9. [Combine colours deliberately](#9-combine-colours-deliberately)
10. [Compose colour in context](#10-compose-colour-in-context)
11. [Build a palette that supports real work](#11-build-a-palette-that-supports-real-work)
12. [Use meaning and psychology responsibly](#12-use-meaning-and-psychology-responsibly)
13. [Provide contrast and redundant information](#13-provide-contrast-and-redundant-information)
14. [Adapt to appearance and environment](#14-adapt-to-appearance-and-environment)
15. [Encode data with colour](#15-encode-data-with-colour)
16. [Manage colour across screens and materials](#16-manage-colour-across-screens-and-materials)
17. [Implement a dependable colour system](#17-implement-a-dependable-colour-system)
18. [Verify and diagnose the result](#18-verify-and-diagnose-the-result)

## 1. Define the colour task

Before choosing swatches, identify what colour must accomplish and where people will encounter it.

| Decision | Establish before selection |
| --- | --- |
| Purpose | Distinguish functional information, brand recognition, atmosphere, illustration, and quantitative encoding. A colour may serve several purposes, but their priorities must be clear. |
| Audience | Identify languages, markets, colour-vision differences, age-related needs, expertise, and relevant conventions. Investigate actual users rather than demographic stereotypes. |
| Medium | Name the display or print conditions, materials, gamut, application, and expected lighting. A web accent, embroidery thread, and illuminated sign need separate specifications. |
| Context | Include surrounding colours, photography, typography, object size, distance, texture, transparency, and motion. |
| Constraints | Identify existing brand assets, required safety conventions, platform settings, accessibility targets, and production limits. |
| Success | Define observable results, such as readable labels, recognisable states, distinguishable chart series, or an accepted production proof. |

Default digital work to colour-managed sRGB delivery, semantic colour roles, and WCAG 2.2 Level AA for web interfaces. Use a wider gamut when the content benefits and the complete delivery path supports it. Default physical work to a named material and production condition, not a generic CMYK conversion.

## 2. Understand light and perception

### Light reaching the eye

An emitting display produces light. An ordinary surface absorbs some incoming wavelengths and reflects others. Transparent materials transmit and filter light. Fluorescence and structural colour introduce additional mechanisms, so reflective pigment is only one way objects acquire their appearance.

For a simple nonfluorescent surface, the light reaching the eye depends on the illuminant's spectral power distribution multiplied by the surface's spectral reflectance. Neither a paint name nor its RGB preview describes that whole relationship.

Most human daylight colour vision begins with three overlapping cone sensitivities, conventionally called S, M, and L for shorter, medium, and longer wavelengths. They are not three narrow blue, green, and red detectors. Neural processing compares their signals and contributes opponent relationships, including reddish versus greenish and bluish versus yellowish. These perceptual relationships differ from a display's RGB channels.

Rods become more influential at low illumination, when colour discrimination weakens. Do not rely on subtle chromatic distinctions in dim environments. The relative apparent brightness of different hues can also change with adaptation.

### A spectrum is not a colour wheel

Visible spectral wavelengths form a continuous interval with approximate, observer-dependent limits. A rainbow does not contain every perceived colour. Magenta and many purples arise from combinations of wavelengths rather than one corresponding spectral wavelength. Brown depends strongly on a darker stimulus within a brighter context. Pink is not a separate band of the rainbow.

A colour wheel joins hue categories into a useful circular arrangement. The join is a design representation, not evidence that the physical spectrum is circular.

### Context changes appearance

| Mechanism | Practical consequence |
| --- | --- |
| Chromatic adaptation and colour constancy | Vision partly discounts illumination. A surface can appear relatively stable under different lights, but constancy is incomplete. Review under intended lighting. |
| Simultaneous contrast | A swatch can appear lighter, darker, warmer, or cooler because of its surround. Compare colours within the actual composition. |
| Assimilation | Fine interleaving or surrounding marks can pull apparent colour towards neighbouring colours. Tiny patterns may behave differently from large swatches. |
| Successive contrast and afterimages | Looking at a strong colour changes subsequent appearance. Alternate comparisons and take breaks during critical matching. |
| Area and surround | A full-screen field has a different impact from a small chip. Judge backgrounds at full size and accents at their smallest use. |
| Individual variation | Colour vision, visual acuity, lens ageing, adaptation, and experience vary. A match for one observer is not a universal match. |

**Metamerism** occurs when different spectral distributions match under a particular observer and illumination but cease to match when those conditions change. Two fabrics can match in a light booth and differ outdoors. A screen can match a print for one observer more closely than for another. Check critical material combinations under more than one relevant light.

## 3. Use history to distinguish different problems

Colour theory combines several histories. Physical explanations, material recipes, perceptual exercises, naming systems, and aesthetic teaching answer different questions.

| Development | Contribution that remains useful | Boundary |
| --- | --- | --- |
| Pigments, dyes, and craft traditions across cultures | Material knowledge links colour to availability, trade, permanence, ritual, and status. | Surviving artefacts may have faded or changed. Today's reproduction may misrepresent the original. |
| Newton's prism investigations in the 1660s and published communication in 1672 | White light can be decomposed into spectral components. Mixing light is distinct from mixing substances. | A spectrum does not explain every aspect of perceived appearance. |
| Goethe's work, published in 1810 | Attention to observation, afterimages, and the conditions under which colour appears. | Experiential observations do not make his objections to Newton a replacement for modern optics. |
| Chevreul's simultaneous-contrast work, published in 1839 | Adjacent colours change apparent appearance. | A contextual effect does not change the pigment's measured reflectance. |
| Munsell's early twentieth-century notation | Separates hue, value, and chroma in an organised colour solid. | Maximum available chroma varies by hue and value. The solid is not a regular cylinder. |
| CIE standard colorimetry from 1931 and CIELAB in 1976 | Provides standardised observer models, tristimulus coordinates, and approximate perceptual differences. | A standard observer represents specified matching behaviour, not every individual or viewing environment. |
| Twentieth-century design education, including Albers's 1963 exercises | Tests relationships by manipulating colour in actual compositions. | Teaching schemes describe possibilities, not universal recipes for beauty. |
| Digital colour management and newer perceptual spaces | Connects encoded values to reproducible interpretation and makes palette construction more controllable. | Numerical consistency still requires profiles, gamut handling, and contextual review. |

Do not treat a familiar historical diagram as a universal law. Ask whether the current problem concerns light, pigments, perception, communication, or reproduction, then use the corresponding model.

## 4. Separate colour, language, and categorisation

### Naming is a selective organisation of experience

People can distinguish many more colour differences than their language has basic colour terms. A basic term is a broad, conventional lexical category, not every expression a speaker can use. A language can describe distinctions through compounds, comparisons with objects, material terms, or context even when it lacks an independent everyday category word.

Languages partition colour differently. Russian commonly distinguishes light blue, *goluboy*, from darker blue, *siniy*, as basic categories. English commonly groups both within blue. Neither organisation describes a visual defect. A colour category in another language need not have exactly the same boundaries as its nearest English translation.

Naming, discrimination, memory, and cultural symbolism are separate questions. Language can influence speed and performance in some colour tasks. In a well-known blue-discrimination experiment, a Russian category advantage weakened under verbal interference. That finding does not mean English speakers cannot see the difference or that language permanently determines the sensory signal.

### Shared tendencies do not establish a universal timetable

Comparative research has found recurring patterns in basic colour categories. A simplified historical proposal begins with broad light and dark categories, then red, followed by differentiation of green and yellow, then blue, and later categories such as brown, purple, pink, orange, and grey. This is a summary of a family of hypotheses. It is not a fixed sequence every language must pass through.

Early work used small samples and assumptions about what counted as a basic term. Later surveys expanded the evidence and found both shared patterns and variation across and within languages. Research examines perceptual structure, communicative needs, object use, and social history as contributing explanations. Similarities do not establish one exclusive cause.

Fewer basic terms do not indicate lower intelligence, lesser cultural development, or an earlier biological stage of vision. Historical claims that ancient people could not see blue because surviving texts lacked a modern blue category are unsupported. A poetic description is not a clinical vision test.

### Consequences for design

Use visible examples alongside colour names when people must make a choice. A theme picker can show a swatch and a descriptive label. A status legend needs its meaning, not merely "green" or "amber". Instructions should say "Select Approve" rather than "Press the green button".

Test translations of colour names with native speakers in the actual product domain. Retain stable internal identifiers while localising display names. When a precise match matters, provide a numerical or physical specification in addition to ordinary language. Do not assume everyone groups teal, cyan, turquoise, and blue in the same way.

## 5. Describe colour precisely

### Keep the dimensions distinct

| Term | Meaning and appropriate use |
| --- | --- |
| Hue | The attribute associated with such families as red, yellow, green, and blue. In cylindrical spaces it is represented by an angle. Neutral colours have no meaningful hue. |
| Lightness | Apparent lightness relative to a reference white under specified conditions. CIELAB L* and OKLCH L are model-specific correlates. |
| Brightness | How much light a stimulus appears to emit or reflect. It depends on viewing conditions and is not interchangeable with lightness. |
| Luminance | A photometric quantity weighted by human visual sensitivity, commonly measured in cd/m². Relative luminance is normalised for a defined calculation. |
| Chroma | Colourfulness relative to a similarly illuminated reference white. In practical perceptual spaces, distance from the neutral axis. |
| Saturation | Colourfulness relative to perceived brightness. The numerical saturation controls in HSL and HSV are model-specific, not direct measures of this perceptual definition. |
| Value | Often a light-to-dark dimension in art. Munsell value is a defined scale. HSV value is the largest RGB channel. Name the intended meaning. |
| Tint, shade, tone | In traditional mixing, white added, black added, and grey added respectively. "Tone" also has broader everyday meanings, so specify the operation when precision matters. |
| Warm and cool | Contextual hue relationships. An orange-biased red can be warmer than a blue-biased red. These terms do not state a temperature in kelvin. |
| Undertone or bias | A secondary directional description, such as yellow-biased green. It is useful for comparison but lacks a universal numerical scale. |
| Neutral | Achromatic or sufficiently low in chroma for a particular use. A warm grey is not mathematically achromatic. |

A low-chroma colour may be light or dark. A vivid colour may still be too light for white text. "More saturated", "darker", and "higher contrast" ask for different changes.

Correlated colour temperature describes the chromaticity of near-white light relative to a thermal radiator. Higher kelvin values generally appear cooler or bluer, despite the aesthetic word "warm" being associated with lower-kelvin light. Do not use colour temperature to specify arbitrary saturated surfaces.

### Give feedback as a controlled change

Use descriptive vocabulary to identify a direction, then confirm it with examples. "Pale" usually means high lightness and low-to-moderate chroma. "Deep" usually combines lower lightness with substantial chroma. "Muted" and "dusty" suggest reduced chroma. "Vivid" suggests strong chroma, while "electric" often suggests a highly chromatic, luminous appearance that may reproduce poorly in print. These words are relative descriptions, not standard coordinates. "Pastel" does not identify a fixed lightness threshold.

Replace "make it pop" with the property, comparison, and purpose. For example, "Increase the action colour's chroma against the neutral surface, while retaining the label's measured contrast." Replace "less bright" with "lower the background's lightness" or "reduce its chroma", depending on the intended change.

For an exact handoff, include a stable name, role, colour space, coordinates, alpha, appearance variant, and permitted pairings. For physical production, also identify the substrate and process. Evocative names help discussion but cannot replace these specifications.

## 6. Choose models, spaces, and formats

A **model** describes dimensions, such as RGB or CMYK. A **space** gives those dimensions a defined interpretation, such as sRGB or Display P3. A **gamut** is the set of colours representable or reproducible under specified conditions. A **profile** characterises the relationship between encoded values and a colourimetric interpretation. A **format** stores or writes values. Hexadecimal is a notation, not a separate gamut.

### Choose the representation for the work

| Representation | Use it for | Limit to remember |
| --- | --- | --- |
| sRGB | General web graphics, ordinary interface delivery, broad interchange. | Its gamut excludes some colours available on wider-gamut displays and some physical materials. |
| Display P3 | Wide-gamut photography, artwork, and selected interface accents in managed pipelines. | It shares the sRGB transfer curve but has different primaries. It is not cinema DCI-P3 with its different viewing specification. |
| Adobe RGB | Some photographic and print-preparation workflows. | Its coverage differs from P3. Neither is simply the other's universal superset. Avoid untagged delivery. |
| Rec. 2020 and HDR encodings | Specified video and advanced display pipelines. | Primaries, transfer function, brightness assumptions, and actual device capabilities must all be identified. Wide gamut alone is not HDR. |
| RGB hex and `rgb()` | Compact sRGB values in CSS. | Eight-digit CSS hex puts alpha last, unlike some other platform encodings. |
| HSL | Convenient hue-based editing of sRGB. | Equal HSL lightness or saturation does not mean equal perceived lightness or colourfulness. |
| HSV or HSB | Common picker interaction, especially for artists. | Value or brightness is a channel maximum. HSV is not HSL, and CSS has no standard `hsv()` colour function. |
| CIE XYZ | Standard colour matching and conversion intermediates. | Coordinates need the relevant white point and scale. Distances are not perceptually uniform. |
| CIELAB and LCH | Material measurement, print interchange, perceptual comparison. | Specify reference white and observer. CSS Lab uses D50. Uniformity is approximate. |
| Oklab and OKLCH | Constructing ramps, adjusting lightness/chroma/hue, and perceptual interpolation. | They approximate perception under reference conditions. Their lightness is not WCAG relative luminance. |
| CMYK | Separations for a specified printing process. | Four percentages without an output condition are an incomplete colour specification. |
| Spot-colour and material libraries | Named ink, paint, textile, or material references. | Include system, identifier, edition where relevant, finish, and substrate. A library preview is an approximation. |

LCH is the polar form of Lab. OKLCH is the polar form of Oklab. Their hue numbers, lightness scales, and chroma values are not interchangeable. An HSL hue angle does not identify the same direction as an equal OKLCH angle.

### Read common syntax correctly

These first four examples describe the same opaque sRGB colour:

```css
#336699
#369
rgb(51 102 153)
hsl(210 50% 40%)
```

Alpha changes compositing rather than changing the underlying space:

```css
rgb(51 102 153 / 50%)
#33669980 /* Alpha is 128/255, approximately 50.2%, not exactly 50%. */
```

Examples in other spaces use their own coordinates. These are independent examples, not equivalents of the colour above:

```css
color(display-p3 0.2 0.5 0.8)
lab(60% -12 -20)
lch(60% 24 240)
oklab(0.65 -0.04 -0.08)
oklch(65% 0.12 250)
```

In CSS OKLCH, L can be written as a number from 0 to 1 or as a percentage. C is commonly written as a nonnegative number. If C uses a percentage, 100% maps to 0.4, not to the maximum displayable chroma. Hue is an angle and wraps around. Near zero chroma, hue has little perceptual meaning. Preserve useful hue metadata for later editing without treating it as visible colour.

### Separate gamut, precision, and dynamic range

An 8-bit RGB encoding has 256 possible values per channel and 16,777,216 possible triplets. That is a count of codes, not a count of equally distinguishable colours or a limit on RGB as a model. Higher bit depth gives finer steps. A larger gamut gives different coverage. HDR supports a wider luminance range through a defined encoding and rendering pipeline. None of these properties automatically supplies the other two.

Use higher precision during substantial image edits and delicate gradient work, then inspect the delivered file for banding. A 16-bit working file cannot prevent banding introduced by an 8-bit export, compression, or a poor display path.

## 7. Construct and mix colours

### Choose the mixing mechanism

| Mechanism | What happens | Use and caution |
| --- | --- | --- |
| Additive light | Spectral light contributions combine. Appropriate red, green, and blue primaries can produce a reference white. | Use linear-light calculations for physical light addition. No three real primaries reproduce every visible colour. |
| Subtractive filtering and pigments | Materials remove parts of the illuminating spectrum. Real pigments also scatter light. | CMY is a useful idealisation. Actual paint mixing depends on pigment, binder, concentration, opacity, and substrate. |
| Process printing | CMYK inks, halftoning, paper, and press behaviour interact. Black supports density and economical, controlled separations. | A process profile and press limits matter more than a simple subtractive diagram. |
| Optical or spatial mixing | Small marks or pixels merge perceptually at a viewing distance. | Test at the intended size, resolution, and distance. The result can differ when enlarged. |
| Numerical interpolation | Software follows a path between coordinates in a chosen space. | Specify the space and hue path. A digital blend is not a paint recipe. |

Traditional red-yellow-blue teaching describes a historically useful pigment palette. It is not a universal set of physical primaries. Red plus green light can appear yellow. Red and green paint need not do so. Likewise, opposite positions on a colour wheel do not guarantee that mixing those particular materials creates a neutral.

### Construct a colour by controlling dimensions

For interface and graphic palette work, start in OKLCH when the tools support it.

1. Choose a hue family for the intended relationship or identity.
2. Set lightness according to the role and its background. Establish a readable label/background pair before polishing its chroma.
3. Add only enough chroma to create the intended emphasis. Check gamut and neighbouring elements.
4. Review the result at actual size. Small lines, large surfaces, and dense text need different treatment.
5. Store the accepted role and approved pairings, then derive variants deliberately.

At a fixed lightness and hue, the largest reproducible chroma depends on the destination gamut. Near white and black, available chroma usually narrows substantially. A constant-chroma ramp can therefore leave gamut at its ends. Reduce chroma or adjust the trajectory rather than expecting every step to remain equally vivid.

Tinting and shading through automatic white or black mixing can change hue and reduce chroma unevenly. For a controlled ramp, adjust lightness, chroma, and sometimes hue independently. If visual character matters more than a constant hue angle, permit a modest hue shift and document the accepted result.

### Choose interpolation by intent

Use Oklab as a practical default for perceptually smoother blends. Use OKLCH when you need explicit control over the hue route. Use linear-light RGB when the intended operation concerns physical light energy. Retain encoded-sRGB interpolation when matching an existing asset or established rendering behaviour is the priority.

```css
/* Perceptual blend between two independently chosen colours. */
.banner {
	background: linear-gradient(90deg in oklab, #2255aa, #e88422);
}

/* Explicitly choose the shorter route around the hue circle. */
.spectrum {
	background: linear-gradient(
		90deg in oklch shorter hue,
		oklch(65% 0.15 30),
		oklch(65% 0.15 300)
	);
}
```

Do not use a rainbow hue path when the intended impression is a restrained transition. Review intermediate colours, not only endpoints. Keep translucent interpolation compatible with premultiplied alpha so that changing opacity does not introduce unintended dark fringes. A whole-element `opacity` also fades its text and children. Use an alpha background colour when only the background should be translucent.

## 8. Convert without losing the specification

### Distinguish rewriting, converting, and mapping

- **Rewriting notation** expresses the same coordinates differently, such as sRGB bytes in hex and decimal.
- **Converting a space** computes coordinates for the same colourimetric target in another space, within the precision and assumptions of the conversion.
- **Gamut mapping** changes an unreproducible target into a reproducible one. It necessarily makes a compromise.
- **Assigning a profile** changes how existing values are interpreted. **Converting to a profile** changes values to preserve appearance as far as the destination permits.

Do not assign a destination profile to an already tagged image as a shortcut for conversion. Assign only when the actual source interpretation is known and missing or incorrect. Preserve an original before changing profiles or flattening an image.

### Simple conversions with defined assumptions

For `#336699`, hexadecimal pairs `33`, `66`, and `99` equal decimal 51, 102, and 153. Dividing by 255 gives encoded sRGB values 0.2, 0.4, and 0.6. Its HSL coordinates are 210°, 50%, 40%. Its HSV coordinates are 210°, about 66.7%, 60%. Converting HSL to HSV by copying the saturation and final component changes the colour.

For RGB-to-HSL conversion, first use normalised encoded RGB values. Let M be the maximum channel, m the minimum, and d = M − m. Then lightness is `(M + m) / 2`. For a chromatic colour, saturation is `d / (1 − |2L − 1|)`. Hue comes from which channel is maximal and the relative differences between the other channels. For an achromatic colour, saturation is zero and hue is undefined. Use tested conversion code for channel ties, endpoints, and hue wrapping.

A general RGB-space conversion decodes the source transfer function, transforms linear RGB through XYZ, adapts reference white if necessary, transforms into destination coordinates, and applies the destination encoding. CSS Lab uses D50 while sRGB, Display P3, and Oklab use D65 references. Copying coordinates or skipping required chromatic adaptation produces a different colour.

When converting Lab to LCH, calculate `C = sqrt(a² + b²)` and `h = atan2(b, a)` in degrees, normalised to a full turn. Use `atan2`, not plain `atan(b/a)`, to preserve the quadrant and handle zero components. The same polar operation applies to Oklab, using its own coordinates.

### Handle out-of-gamut colour deliberately

Keep high-precision source coordinates until output. Early rounding and repeated conversions accumulate error. Avoid silently clipping each channel into range. Clipping can change hue, flatten detail, and collapse distinct palette steps.

For a UI accent, reducing chroma while approximately retaining lightness and hue is often a useful mapping strategy. For an image, use a suitable colour-management transform and review the result as a whole. Exact mapping algorithms and browser implementations can differ, so inspect important colours in the actual output path.

A wider destination does not restore information lost in an earlier sRGB export. A mathematical conversion cannot recover clipped detail or identify an unknown original profile.

### Never present generic CMYK as an exact equivalent

The elementary formula based on `1 − R`, `1 − G`, and `1 − B` describes an idealised model. It does not account for ink, paper, dot gain, black generation, or total ink limits. Use the printer's requested output profile and workflow. A web converter's CMYK percentages are, at most, an unqualified estimate.

For a critical conversion, record source and destination spaces or profiles, rendering intent where relevant, mapping method, precision, and proof conditions. Report an approximation as an approximation.

## 9. Combine colours deliberately

A harmony scheme proposes hue relationships. Its appearance still depends on lightness, chroma, proportion, placement, and context. Identify the wheel or space before applying angles.

| Scheme | Construction | Useful starting point | Main risk |
| --- | --- | --- | --- |
| Achromatic | Black, white, and greys. | Content-led work or a neutral base. | Weak hierarchy if values are too close. |
| Monochromatic | One hue family with varied lightness and chroma. | Cohesive systems with restrained hue variation. | Adjacent states become indistinguishable. |
| Analogous | Neighbouring hue families. | A continuous atmosphere or related groups. | Categories lack separation. |
| Complementary | Two opposing hue directions on the chosen wheel. | A clear dominant/supporting relationship. | Equal-chroma, equal-lightness edges can appear to vibrate. |
| Split-complementary | A base plus two hues on either side of its opposite. | Contrast with more flexibility than one opposing pair. | Three colours compete when their area and emphasis are equal. |
| Triadic | Three roughly equally spaced hue directions. | A deliberately varied identity or illustration. | Equal weighting creates noise. |
| Tetradic | Two complementary pairs. A square is the equally spaced special case. | A system that needs several distinct hue families. | Complexity exceeds the number of meaningful roles. |
| Neutral with accent | A neutral structure and a limited chromatic emphasis. | Interfaces and editorial hierarchy. | Everything becomes accented as exceptions accumulate. |

On a digital RGB hue wheel, red is opposite cyan. The traditional artist's wheel often pairs red with green. Neither pairing is a universal perceptual or material opposite. Distinguish a wheel complement, an additive neutralising mixture, a pigment mixture, and an afterimage relationship.

Use hue geometry to generate candidates. Then assign a dominant field, supporting colours, and accents. Vary lightness and chroma to establish order. Opposite hues can have similar luminance and fail text contrast despite appearing strongly different.

Do not add a colour solely to complete a scheme. A useful palette can be asymmetrical, mostly neutral, or deliberately discordant. Coherence comes from repeated relationships and a clear purpose, not from satisfying every point of a diagram.

## 10. Compose colour in context

### Control visual weight

Visual weight depends on area, lightness contrast, chroma, edge sharpness, placement, and semantic relevance. A tiny saturated warning can dominate a large quiet panel. A large pastel background can define the whole atmosphere despite low chroma.

Start with the largest field, then establish readable foregrounds, structural surfaces, and emphasis. Review the composition with actual text and images. Equal-sized palette chips conceal the proportions that people will see.

The familiar 60/30/10 distribution is an optional exercise in dominance, support, and accent. It is not a requirement or a formula for every screen. Count meaningful emphasis rather than forcing pixel-area quotas.

### Coordinate the relationships

- Use lightness to establish broad hierarchy before adding hue distinctions. A greyscale view can reveal lost value structure, but it does not test all colour-vision differences.
- Reserve the strongest accents for the information or action that deserves attention. Repetition teaches meaning. Decorative reuse can weaken it.
- Balance chroma across area. Reduce a colour's chroma or area if it overwhelms neighbouring content before replacing its hue.
- Judge temperature relatively. A slightly warm neutral can unify vivid accents. A cool neutral can make a warm accent appear stronger.
- Use space, outlines, or lightness separation around competing vivid colours. Avoid thin, similarly luminous red/blue or red/green boundaries for essential text and detail.
- Let imagery participate in the palette. A neutral interface may become very colourful once photographs and charts are present.

Do not darken every image to make an overlaid title readable if an opaque caption area preserves the content better. For variable imagery, provide a controlled backing, scrim, or separate label area and test the weakest region under the text. Blur alone does not guarantee contrast.

### Read edges and transitions

Colours with close lightness can merge at a distance. Strong complementary boundaries may shimmer or appear unstable, especially in small saturated details. Chromatic aberration can make saturated red/blue fine detail uncomfortable. Increase lightness separation, change proportions, or insert a neutral boundary.

A gradient can introduce an unintended focal point or false boundary through uneven lightness. Inspect its entire path. In an illustration this may be expressive. In quantitative encoding it can misrepresent the data.

## 11. Build a palette that supports real work

### Start from roles and constraints

1. Collect representative content and contexts, including a dense screen or page, an error state, a chart, and important brand imagery where applicable.
2. Define required roles before choosing a colour count. Separate brand expression, content colours, interactive actions, and semantic status.
3. Establish neutral surfaces and text pairs. Make the main reading and task flow work before introducing secondary accents.
4. Choose a recognisable anchor and one plausible alternative direction. Compare whole compositions rather than dozens of isolated chips.
5. Build the necessary ramps and paired foregrounds. Adjust each family for its actual gamut and contrast needs.
6. Assign state and appearance variants. Test every permitted pairing and reject unnecessary combinations.
7. Review recognisability, cultural fit, accessibility, and production. Document the approved system and its exceptions.

A reference image can supply a direction without supplying a usable palette. Dominant extracted colours may be unsuitable for text or actions. Sampling a photograph also reflects its illumination and grading, not a material's intrinsic specification.

### Separate primitives, semantic roles, and components

| Layer | Example | Responsibility |
| --- | --- | --- |
| Primitive | `blue-700`, `neutral-50` | Stores a specific family step in a defined space. The number is an internal ordering convention. |
| Semantic | `text-primary`, `surface-raised`, `action-primary`, `on-action-primary` | States purpose and defines approved relationships across themes. |
| Component | `button-primary-background-hover` | Maps a specific component state to the semantic system when necessary. |

Do not let a primitive name imply accessibility. `blue-500` can be safe in one pairing and unusable in another. The same step number across two hue families need not have equal luminance or contrast.

Build enough distinctions to support actual use. A neutral family may need more steps than a decorative accent. A short-lived campaign may need fewer tokens than an application with many states. Palette size follows requirements.

### Construct ramps and status families

A useful ramp has a deliberate lightness progression, controlled chroma, recognisable character, and no accidental reversals after gamut mapping. Space steps according to their jobs rather than assuming equal numeric increments look equal. Test subtle adjacent surfaces separately from foreground/background pairs.

For each status, define a foreground, subtle background, strong fill, on-fill text, and border only where those roles are needed. Keep success, warning, error, information, selection, and ordinary action distinct in meaning. Do not assume warning must be yellow or information must share the brand accent. Retain well-established domain conventions where they help recognition.

A yellow warning fill usually needs a dark label. Making the fill darker enough for white text may change the intended colour identity. Solve the pair, rather than insisting that every status use identical label styling.

### Define the contract

Record each role's values per appearance, approved foreground/background pairs, minimum contrast target, allowed uses, and prohibited confusions. Include a policy for user-generated colours and exceptions. A colour picker should prevent or warn about unreadable combinations in contexts where users depend on them.

For a brand palette, also document primary and secondary proportions through examples, colour usage with imagery, monochrome reproduction, and digital versus material specifications. A signature colour can remain recognisable while using different functional variants for small text, large fields, and print.

## 12. Use meaning and psychology responsibly

### Distinguish association, convention, and effect

An association is something a person connects with a colour. A convention is a learned shared use, such as an error indicator. A measured psychological effect concerns a defined task and population under specified conditions. None automatically establishes the others.

The same hue can suggest danger, celebration, appetite, political identity, or a particular brand. Meaning depends on lightness, chroma, surrounding colours, material, language, category, and situation. Dark red velvet and a flashing red validation message do not provide the same experience.

### Use associations as questions

| Family | Possible associations to investigate | Decision risk |
| --- | --- | --- |
| Red | Urgency, prohibition, vitality, affection, celebration. | A brand accent can compete with errors. Financial gain/loss conventions differ across markets. |
| Orange and yellow | Warmth, visibility, play, caution, ripeness. | Light versions often fail with white labels. Caution semantics depend on the domain. |
| Green | Growth, vegetation, permission, success, money. | Ecological or safety implications may be misleading. Red/green distinctions exclude some users. |
| Blue and cyan | Water, distance, coolness, technical or institutional identity. | Category similarity may reduce distinctiveness. Blue does not inherently create trust. |
| Violet and pink | Fantasy, ceremony, softness, intensity, subcultural identity. | Gendered or luxury readings are neither stable nor universal. |
| Brown and earth colours | Soil, craft, food, age, durability. | Material and texture may drive the reading more than hue alone. |
| White, black, and greys | Clarity, restraint, formality, mourning, emptiness, status. | Ritual associations vary. Pure black and white can also create uncomfortable large-area contrast. |

These are prompts, not a dictionary of fixed meanings. Specific combinations can evoke a holiday, sports team, flag, political movement, or competitor more strongly than individual colours do. Metallic gold is a reflective material effect. A flat yellow approximation does not carry all of its appearance or associations.

### Evaluate psychological claims at the right level

Avoid prescriptions such as "blue makes people trust", "red raises conversion", or "green is calming" without relevant evidence. Apparent effects may depend on task, learned association, surrounding design, luminance, and culture. A hue change that also changes contrast cannot isolate hue as the cause.

For an important decision, compare plausible options in realistic tasks. Ask what users notice, how they interpret it, and whether they complete the action correctly. Separate aesthetic preference, recognition, readability, and behaviour. If testing business outcomes, keep text, layout, exposure, and other conditions comparable and report uncertainty. A successful experiment in one product does not establish a universal colour rule.

Use cultural charts and self-selected association polls to identify questions for local research. Do not infer an individual's interpretation from nationality. Validate critical semantic choices with people who know the relevant language, domain, and current context.

## 13. Provide contrast and redundant information

### Apply the correct threshold and scope

For web work, use WCAG 2.2 Level AA as the default baseline. These ratios describe particular foreground/background relationships, not a general score for a palette.

| Content | Baseline requirement | Scope |
| --- | --- | --- |
| Normal text and images of text | At least 4.5:1 at AA. | Includes placeholders and text shown on hover or focus when it is intended to be read. |
| Large text | At least 3:1 at AA. | At least 18 pt regular or 14 pt bold, approximately 24 CSS px or 18.67 CSS px respectively. A heading is not automatically large text. |
| Enhanced text contrast | At least 7:1 normal or 4.5:1 large at AAA. | A useful stronger target for demanding reading contexts. |
| Required visual information identifying controls, states, and graphical objects | At least 3:1 against relevant adjacent colours at AA. | Applies to the information needed to identify or understand them. Not every decorative border or surface must meet 3:1. |
| Keyboard focus | Visible focus at AA, with applicable non-text contrast requirements. | Do not remove the browser indicator without a dependable replacement. Focus visibility, contrast, and obscuring are separate checks. |

Inactive controls, incidental text, and logotypes have specified contrast exceptions. Do not use an exception to make necessary instructions, a live placeholder, or secondary content unreadable. A lower hierarchy is not an inactive state.

SC 2.4.13 Focus Appearance is AAA. It requires an indicator area at least equivalent to a 2 CSS px thick perimeter of the unfocused component, plus at least 3:1 change between the same pixels in focused and unfocused states, subject to its exceptions. Do not mislabel that whole requirement as AA. As a practical product default, provide an obvious focus outline with sufficient separation from both control and surrounding surface.

### Calculate sRGB contrast correctly

For opaque sRGB colours, normalise each channel to a value c from 0 to 1 and decode it to linear light:

```text
c_linear = c / 12.92                         if c <= 0.04045
c_linear = ((c + 0.055) / 1.055) ^ 2.4       otherwise

Y = 0.2126 R_linear + 0.7152 G_linear + 0.0722 B_linear
contrast = (Y_lighter + 0.05) / (Y_darker + 0.05)
```

Do not average encoded RGB channels, use HSL lightness, or substitute OKLCH L for Y. Compare the unrounded result with the threshold. A result of 4.499:1 fails a 4.5:1 requirement.

Examples on opaque white:

| Foreground | Contrast, rounded for display | Result |
| --- | --- | --- |
| `#000000` | 21:1 | Meets normal-text AAA. |
| `#336699` | 6.00:1 | Meets normal-text AA, below normal-text AAA. |
| `#767676` | 4.54:1 | Meets normal-text AA with little margin. |
| `#777777` | 4.48:1 | Fails normal-text AA. |
| `#FFFF00` | 1.07:1 | Fails text and required non-text contrast on white. |

For alpha, gradients, images, filters, and blend modes, determine the actual rendered colours against the actual backdrop. The simple channel equation `out = alpha × foreground + (1 − alpha) × background` assumes an opaque background and a specified compositing space. It is not a universal perceptual mixing rule. Prefer computed rendering or a checker that supports the relevant pipeline.

Wide-gamut colours require space-aware handling. Do not feed Display P3 channel numbers into the sRGB formula as though they were sRGB. Check the delivered rendering and fallback with a tool that documents its colour-space support. APCA can supply additional perceptual information, but it does not replace the WCAG 2.2 contrast-ratio requirement when claiming that conformance.

### Make information survive a loss of hue

Use labels, icons, shapes, patterns, line styles, position, or explicit state text alongside colour. Error fields need a message and an identifiable field. Positive and negative trends need signs or words. Selection needs a visible marker or another dependable distinction.

Default inline links to a persistent underline. A colour-only link treatment needs additional conditions, including sufficient distinction from surrounding text and a non-colour cue on interaction. Passing text contrast against the page alone does not establish that a link is identifiable.

Colour-vision differences include red/green, blue/yellow, and rarer forms with much less colour information. Simulate relevant deficiencies to find candidate collisions, then test functional distinctions. A simulator is an approximation, and greyscale is not a complete substitute. Give dense charts or specialist tools customisation where fixed palettes cannot serve all users.

Avoid rapidly flashing colour changes, especially saturated red transitions. Flash safety depends on frequency, area, luminance, and colour thresholds. Use appropriate analysis for flashing content rather than assuming a small animation or a different hue is safe.

## 14. Adapt to appearance and environment

### Design light and dark relationships separately

Dark mode is a separate composition. Reassign roles deliberately rather than inverting RGB values. Large bright fields can glare in a dark environment, while weak text and near-black surfaces can merge on a poor display.

Use sufficiently distinct surfaces, readable foregrounds, and carefully controlled chroma. A bright accent may need lower chroma or a different lightness in dark mode. Avoid a universal rule that every dark-theme colour must be desaturated. The correct adjustment depends on the colour, area, and surroundings.

Use lighter raised surfaces where they help establish depth in a dark composition, supported by borders or other cues when needed. Test shadows rather than relying on a dark shadow to separate two already dark surfaces. Preserve state meaning across modes even when the numeric colours change.

### Respect platform and user choices

On Apple platforms, prefer dynamic semantic colours through their intended APIs. Custom roles need appropriate light, dark, and increased-contrast variants. Do not copy documented system RGB values as permanent constants or repurpose separator colours as text colours. Review custom assets and colours with the relevant accessibility and appearance settings.

Follow the system appearance by default. On the web, an explicit user preference may override that default where the product offers one. Support forced-colour environments using system colours and visible borders or outlines. Background fills and box shadows can disappear or be replaced. Avoid opting out of forced colours unless preserving a particular colour is essential and an accessible alternative exists.

In translucent or glass-like interfaces, the backdrop participates in the final colour. Use colour sparingly for emphasis, test variable backdrops, and provide sufficiently opaque alternatives when transparency is reduced. A resting screenshot does not establish legibility while content moves behind a control.

### Test viewing conditions

Review on representative devices in daylight and dim surroundings. Automatic white-point adjustment, night settings, display brightness, glare, ageing screens, and power-saving modes can alter appearance. Distinguish controlled colour-critical review from ordinary use testing. The former needs a managed display and consistent conditions. The latter should include the variability people actually encounter.

Do not claim identical appearance across all devices. Set an achievable target of consistent interpretation, adequate contrast, and acceptable reproduction within defined conditions.

## 15. Encode data with colour

Choose the scale from the data relationship, then choose hues.

| Data relationship | Colour strategy | Check |
| --- | --- | --- |
| Unordered categories | Distinct hue families with comparable visual emphasis. | Keep category assignments stable across views. Add direct labels, symbols, or line styles. |
| Ordered magnitude | A sequential scale with a clear lightness progression. | Inspect monotonic order after rendering and gamut mapping. Hue variation may assist without creating false bands. |
| Deviation around a meaningful centre | A diverging scale with two distinguishable directions and an explicit midpoint. | Place the midpoint at the actual reference value. Do not imply a meaningful zero if none exists. |
| Cyclic values, such as angle or time of day | A cyclic scale whose ends join smoothly. | Avoid an artificial discontinuity and confirm that repeated colour does not imply identical noncyclic values. |
| Missing, excluded, or uncertain data | A separate treatment such as a neutral, pattern, or explicit label. | Do not let missing data look like the lowest measured value or the midpoint. |

Default away from rainbow scales for ordinary ordered magnitude. Their uneven lightness and hue boundaries can create false features. A deliberately designed multihue scale can work when its perceptual order is tested.

Do not invent a universal maximum number of distinguishable colours. Distinction depends on mark size, separation, display, task, and observer. When the reader must repeatedly consult a legend or confuse similar series, reduce categories per view, use small multiples, add direct labels, or provide filtering.

Test graph marks against their background and against touching marks where boundaries carry information. Use visible separators or alternative encodings when necessary. A palette can pass text contrast and still fail to communicate a chart.

## 16. Manage colour across screens and materials

### Identify the relevant standard

Different standards govern encoding, measurement, exchange, viewing, and access. Specify the applicable edition in production contracts or conformance claims. These are the main families relevant to this guide, not interchangeable certifications.

| Standard or specification | What it establishes | What it does not establish |
| --- | --- | --- |
| IEC 61966-2-1, sRGB | An RGB encoding with defined primaries, white point, transfer function, and reference conditions. | Identical appearance on unmanaged or differently adjusted displays. |
| ISO/CIE 11664 series | Standard colorimetric observers, illuminants, coordinates, and related calculations. Part 4 defines CIELAB. | An aesthetic palette or a guarantee of identical individual perception. |
| ICC profile specifications and ISO 15076-1 | Architecture and data structures for exchanging colour interpretations and transforms. | An accurate profile for an unmeasured device or an acceptable gamut-mapping choice for every image. |
| ISO 3664 | Defined viewing conditions for graphic-arts and photographic reflection and transmission evaluation. | A specification for soft-proofing displays or every material industry. |
| CSS Color specifications | Web colour syntax, space definitions, conversion, and interpolation behaviour. | Universal implementation support for every feature or automatic contrast compliance. |
| WCAG 2.2 | Accessibility success criteria, including specific uses of colour and contrast. | A general colour-appearance standard or a complete physical-product specification. |

### Keep the pipeline explicit

Preserve meaningful embedded profiles in raster assets and inspect the final exported files. Application previews, screenshots, SVG styling, browser rendering, and print software may interpret colour differently. Verify the destination rather than assuming that a matching picker value establishes a matching result.

Calibration adjusts a device towards a target condition. Profiling characterises its response. A monitor profile describes that monitor. It is not normally the working colour space to embed in every deliverable. Recheck critical devices as their behaviour changes.

For general web delivery, export sRGB assets unless a verified wide-gamut pipeline is intended. For P3 assets, preserve the appropriate profile and test both wide-gamut and ordinary displays. Avoid converting an image and then stripping the metadata that explains its interpretation.

### Match the printing workflow

Agree the production process, stock, output profile, total ink coverage, black treatment, proof, and final file requirements with the provider. Use the requested PDF/output-intent convention where applicable. Some workflows accept tagged RGB and perform managed conversion downstream. Do not convert prematurely merely because the final object is printed.

Use single-channel black for small black text when the printer specifies it. A four-ink rich black can improve large dark fields but creates registration and ink-load risks in fine detail. Do not prescribe a universal rich-black recipe. Keep registration colour out of ordinary artwork.

Review overprint and knockouts. Accidental overprint can change colours or make light objects disappear. Spot inks, varnishes, metallics, fluorescent materials, and white ink need explicit separations and production instructions. Their effects cannot be fully represented by a normal RGB preview.

### Choose a rendering intent by the compromise

| Intent | Typical reason to use it | Consequence to inspect |
| --- | --- | --- |
| Relative colorimetric | Preserve in-gamut relationships relative to destination white. | Out-of-gamut distinctions may collapse. Black-point compensation can help adapt shadow range where supported. |
| Perceptual | Preserve an image's overall relationships across different gamuts. | In-gamut colours may also shift. Results depend on the profile and colour-management implementation. |
| Absolute colorimetric | Simulate a source medium's white for proofing. | Paper-white simulation can appear tinted on the proofing medium. |
| Saturation | Prioritise colourfulness for suitable business graphics. | Hue and precise matching can shift. It is usually unsuitable for critical brand matching or photographs. |

Soft-proof using the intended output profile and appropriate paper/black simulation. A screen cannot reproduce every printed texture, gloss, fluorescence, or reflection. Obtain a physical proof or material sample when those properties or critical brand matches matter.

A spot-colour identifier must include the relevant library and suffix. Coated and uncoated appearances can differ even with the same nominal ink because the paper changes absorption and reflection. Specify an accepted physical reference. Treat RGB and process equivalents as separately approved reproductions.

### Measure what matters

For critical material matching, record the illuminant, standard observer, measurement geometry, backing, and relevant material conditions. State the colour-difference formula, such as ΔE00, together with an agreed tolerance. A bare "ΔE < 2" is incomplete without its formula and measurement conditions.

A small measured difference does not guarantee an acceptable match for every texture, gloss, large field, or observer. Use instrumental measurement and visual acceptance together. Check metamerism under the intended lighting, and distinguish the sign-off sample from an uncontrolled photograph of it.

## 17. Implement a dependable colour system

### Keep role pairs explicit

The following minimal CSS example uses opaque sRGB values. It illustrates semantic pairing and appearance mapping, not a complete palette. The blue action with white text measures about 6.00:1. Its white focus outline is separated from the white page by a dark outer ring.

```css
:root {
	color-scheme: light dark;
	--surface: #ffffff;
	--text-primary: #17202a;
	--action-primary: #336699;
	--on-action-primary: #ffffff;
}

@media (prefers-color-scheme: dark) {
	:root {
		--surface: #17202a;
		--text-primary: #ffffff;
		--action-primary: #a8d0ff;
		--on-action-primary: #17202a;
	}
}

body {
	background: var(--surface);
	color: var(--text-primary);
}

.primary-action {
	background: var(--action-primary);
	color: var(--on-action-primary);
	border: 1px solid currentColor;
}

.primary-action:focus-visible {
	outline: 2px solid #ffffff;
	outline-offset: 2px;
	box-shadow: 0 0 0 6px #17202a;
}

@media (forced-colors: active) {
	.primary-action {
		background: ButtonFace;
		color: ButtonText;
		border-color: ButtonText;
	}

	.primary-action:focus-visible {
		outline-color: Highlight;
		box-shadow: none;
	}
}
```

Extend the same contract to hover, pressed, selected, disabled, visited, loading, error, and success states where the component needs them. A passing base colour does not certify those variants. Give text selection, caret, form autofill, scrollbars where customised, and validation feedback appropriate treatment as well.

Do not encode a state solely through a darker shade. Pair colour with a clear border, marker, label, or other meaningful change when the state must be identifiable.

### Use newer syntax with a real fallback

When a feature is optional, provide a usable earlier declaration and conditionally override it. A custom property can store an unsupported colour expression without proving that the consuming property can render it.

```css
:root {
	--brand-accent: #336699;
}

@supports (color: oklch(50% 0.1 250)) {
	:root {
		--brand-accent: oklch(50% 0.1 250);
	}
}
```

The two values above are an illustrative fallback and enhancement, not an exact conversion. Measure any text pair using each value. For a wide-gamut enhancement, test both syntax support and the intended display capabilities. Ensure the sRGB version remains a complete, intentional design.

Use `color-mix()` and relative-colour syntax to express a design decision, not to outsource it. Mixing an action colour with white by a fixed percentage does not guarantee a readable hover state. A token generator should preserve approved values and flag untested combinations rather than labelling every output accessible.

### Deliver the specification

Include the canonical coordinates and space, fallback values, profile-bearing assets, role mappings, state/appearance definitions, approved pair matrix, and production-specific equivalents. Keep generated files traceable to their source tokens. Review downstream exports after token changes, especially when a colour is reused for both branding and information.

## 18. Verify and diagnose the result

### Review the complete context

A palette is ready when its intended roles work in representative compositions and delivery conditions.

1. Confirm each colour has a purpose and stable meaning. Check unintended resemblance to warnings, competitors, flags, and domain conventions.
2. Check lightness structure, accent distribution, and edge behaviour at full scale and the smallest required size.
3. Measure approved text and non-text pairs, including states, alpha, variable backgrounds, and fallback output. Leave practical margin above thresholds where possible.
4. Check information without hue. Inspect colour-vision simulations, keyboard focus, forced colours, and increased-contrast or reduced-transparency settings as applicable.
5. Review light and dark appearances with actual content, images, charts, and user-generated material.
6. Inspect final exports, profiles, gamut mapping, and gradient banding on representative devices. Obtain physical proofs where material appearance matters.
7. Record accepted exceptions with the affected role, reason, alternative information channel, and scope. Recheck affected pairings whenever a shared value changes.

### Diagnose the mechanism before changing hue

| Symptom | Likely mechanisms to inspect | Corrective direction |
| --- | --- | --- |
| The same hex looks different in two applications. | Profiles, colour management, backdrop, display, or screenshot interpretation. | Compare tagged files and rendering conditions before editing the source values. |
| A vivid button has an unreadable white label. | Its luminance is too high despite strong chroma. | Use a dark label or a darker functional variant. |
| A muted palette looks muddy. | Crowded lightness, excessive neutral mixing, unwanted hue drift, or low local separation. | Restore a clear lightness hierarchy and controlled chroma relationships. |
| Colours look attractive as chips but chaotic on a page. | Wrong area proportions, competing accents, imagery, or missing roles. | Recompose at actual scale and reduce simultaneous emphasis. |
| A ramp has a sudden jump or repeated endpoint. | Clipping, uneven lightness, rounding, or changing interpolation spaces. | Review high-precision coordinates and the mapped result. |
| A gradient has visible bands. | Limited bit depth, compression, long shallow transitions, or display processing. | Preserve working precision and inspect the final encoding. Test dithering where appropriate. |
| A chart passes contrast checks but remains confusing. | Category collisions, excess series, colour-only legends, or inappropriate scale type. | Add direct labels and alternative encodings, or simplify the view. |
| Print looks duller or shifted. | Smaller/different gamut, stock, ink, missing profile, wrong intent, or lighting. | Use the actual output profile and proof. Approve a material-specific reproduction. |
| Two materials match in one room and clash in another. | Illuminant metamerism, fluorescence, texture, or gloss. | Compare spectra or samples under intended lights and adjust the material specification. |
| Dark mode feels glaring or flat. | Excessive bright area, uncontrolled chroma, or insufficient surface separation. | Rebalance large fields, foregrounds, and depth cues independently. |
| A status is misread in one market. | Local domain convention, translation, or competing learned association. | Validate locally and strengthen labels or symbols. |
