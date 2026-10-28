# Assets — Minerva Blueprints

[Português brasileiro](README.pt-br.md)

**Olympus Project · OAL L2 · ADMV (ADPM + ADVS) · Alpha-v0.1.0**

The headers and diagrams follow the visual composition of Atlas Specifications: blue/teal, light and navy cards, explicit arrows, and transparent diagram backgrounds. Both languages express the same content. Images explain the model; the edition documentation defines requirements and contracts.

## Inventory

| PNG | Editable source | Dimensions | Content |
|---|---|---|---|
| [minerva-banner-en.png](minerva-banner-en.png) | [SVG](sources/minerva-banner-en.svg) | 1600 × 534 | Project identity, layer and version. Decorative artwork only. |
| [minerva-oal-position-en.png](minerva-oal-position-en.png) | [SVG](sources/minerva-oal-position-en.svg) | 1400 × 1080 | OAL position, model parts and concrete artifacts. |
| [minerva-model-en.png](minerva-model-en.png) | [SVG](sources/minerva-model-en.svg) | 1400 × 1180 | ADPM, ADVS and the L2 YAML file-mirror profile. |
| [minerva-workflow-en.png](minerva-workflow-en.png) | [SVG](sources/minerva-workflow-en.svg) | 1400 × 1230 | Versioned inputs, review, realization and evidence feedback. |

Every asset has an `-en` and a `-pt-br` version. Headers have transparent corners and an opaque body. Diagrams use a transparent canvas and opaque cards for legibility in light and dark themes. All SVGs are standalone and contain `title` and `desc`; raster inputs are embedded in headers.

## Semantics and ownership

The per-file mirror belongs in `docs/L2_MinervaBlueprints/apps/`. L3 records inventory, profiles, composition, execution, concrete integrations and evidence in `docs/L3_Vulcan/`. The `docs/` layout is recommended; only adopted models need corresponding folders. `Shared/` contains cross-cutting support and is not an OAL layer. Interaction content retains its L4 classification when referenced from L2 or L3.

In this edition's Minerva profile, `source.state` distinguishes `planned` from `observed`; `document.nature` distinguishes `designed`, `reconstructed` and `mixed`. An observation about source code is not proof of execution. Arrows describe relationships and reviewed working steps; they do not promise automatic generation. Supporting libraries are optional for the architecture.

## Reproduction

Use Python 3.10+, CairoSVG 2.8.2, its system Cairo libraries, and the **DejaVu Sans** and **DejaVu Sans Mono** fonts. These dependencies only reproduce images; they are not dependencies of the model or Vulcan applications.

```sh
python -m pip install -r assets/requirements-artwork.txt
python assets/sources/render_images.py
```

Run this from the repository root; the script also works by absolute path from another directory. It uses local files only, rewrites eight SVGs and eight PNGs, and copies original icons for display. It does not call an image-generation service. Edit labels and geometry in the script to keep reproduction consistent; manual SVG edits are overwritten by the next run.

Text remains editable. Fonts are not embedded and must be installed for matching layout. Different Cairo or font versions can change pixels; binary identity across environments is not promised.

## Originals, provenance and attribution

- The supplied project icons are retained in `sources/minerva-icon-original.png` and `sources/olympus-icon-original.png`. Display copies and SVG-embedded payloads preserve the original byte streams.
- Decorative art is retained in `sources/minerva-hero-art.png`. The [prompt record](sources/ARTWORK-PROMPT.md) includes the exact request, provenance and reproduction limits.
- Diagrams are native SVG geometry and text authored from the model documentation. Generated art is not used as a source of technical information.
- Visual composition and SVG helpers were adapted from [Atlas Specifications · Stable-v1.0.0](https://github.com/CodeVaultCommunity/OlympusProject_AtlasSpecifications/tree/b5941830515d9968bb7f313301f1abe25fb6f8aa/assets). Copyright (c) 2026 Douglas de Oliveira Alkimim. The [original MIT notice](sources/ATLAS-LICENSE.txt) is preserved.
- [asset-metadata.json](asset-metadata.json) records names, dimensions, SHA-256 hashes, source revision and checks. The distribution license is in [LICENSE](../LICENSE).

## Review

Full PNG decoding, transparency, original-icon integrity and standalone SVGs are checked. The current revision visually reviewed the two changed model diagrams in both languages, including text, connectors, clipping and readability. The other six renders retain their baseline bytes; the metadata records this scope. This review checks asset presentation; it does not certify conformity of any application.
