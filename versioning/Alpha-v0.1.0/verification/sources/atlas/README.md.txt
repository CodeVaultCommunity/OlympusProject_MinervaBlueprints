# Atlas Specifications · Stable-v1.0.0

English · [Português brasileiro](README.pt-br.md)

**Atlas is an abstract model for declarative use-case specifications.** This Stable edition defines its semantic contract, Atlas JSON/Markdown/LaTeX representation profiles and a Python translator with exact-content checks. Other models may implement the abstraction through an explicit mapping. The model, an implementing model, a representation and a concrete project artifact have distinct responsibilities.

This folder is a self-contained edition: keep its files together to use its documentation, starters, examples, translator and tests without the repository root. Its runtime and example resources remain local. The root README and root `assets/` folder provide the illustrated project introduction; that artwork is not needed to use this edition. The skill is also independently portable. English is the normative source; Portuguese is the corresponding reading translation. **MUST**, **MUST NOT** and **REQUIRED** identify obligations. Schema success alone does not establish semantic conformance.

<a id="release-notes"></a>
## Release notes — Stable-v1.0.0

This edition preserves the Atlas L1 scope and corrects four audited defects: absent optional entity records; typed figure/source/assumption/issue references; exact CRLF/CR/LF in LaTeX cells; and Unicode separators in opaque data. A trailing-CR delimiter boundary is also corrected. Invalid references fail before output is written.

The model/profile identities are `Stable-v1.0.0`; the package and producer of newly authored documents are `1.0.0`. The historical Alpha edition is retained unchanged. Stable rejects incompatible profiles explicitly. Conversion preserves all authored identities and history. The starters and examples were migrated editorially, with provenance, and the task board includes two valid Stable revisions demonstrating an acceptance-link change.

OAL Stable-v1.0.0 was delivered as a local, pinned Git checkout and reviewed against the ten UCS and nine cross-layer clauses. Remote availability is not asserted. See [correspondence](#oal-conformance), the [compatibility policy](COMPATIBILITY.md), [verification record](verification/RELEASE.md), and [migration record](verification/editorial-migration.json). Publication and stakeholder approval are separate from these checks.

LaTeX publication in this edition includes editorial and plain themes, a self-contained ornamental cover, wrapped tables and optional decorative images kept outside specification content. The [publication-style contract](implementations/latex/README.md#publication-style) states what conversions preserve and how to retain custom appearance separately.

## Contents

- [Release notes](#release-notes) · [Versions](#versions) · [Start a specification](#quick-start)
- [Representation implementations](#implementations) · [Translation](#translation)
- [Abstract model](#abstract-model): [identity](#model-3), [concepts](#model-4), [text](#model-5), [references](#model-6), [consumption](#model-7), [entities](#model-8), [tools](#model-9), [cases and requirements](#model-10), [boundaries](#model-11), [provenance](#model-16), [invariants](#model-18)
- [Graph contract](#graph-contract) · [Resources](#resource-contract) · [Preservation](#preservation)
- [Examples](#examples) · [AI skill](#ai-skill) · [Verification](#verification)
- [OAL correspondence](#oal-conformance) · [Versioning](#versioning) · [Authorship](#authorship)

<a id="versions"></a>
## Versions

| Edition | Status | Release Notes | Reference rules | Verification Guide | Conformance Guide |
| --- | --- | --- | --- | --- | --- |
| Stable-v1.0.0 | Stable edition | [English](README.md#release-notes) · [Português](README.pt-br.md#release-notes) | [English](README.md#reference-rules) · [Português](README.pt-br.md#reference-rules) | [English](README.md#verification) · [Português](README.pt-br.md#verification) | [English](README.md#conformance) · [Português](README.pt-br.md#conformance) |

<a id="quick-start"></a>
## Start a specification

Use **Python 3.11+**. From this edition directory, create and activate a virtual environment, then install the local package:

```bash
python -m venv .venv
# POSIX: source .venv/bin/activate
# PowerShell: .venv\Scripts\Activate.ps1
python -m pip install .
python translator/atlas_translate.py formats
python translator/atlas_translate.py validate implementations/json/starter.atlas.json
```

Begin by copying [the JSON starter](implementations/json/starter.atlas.json), [the Markdown starter](implementations/markdown/starter.atlas.md) or [the LaTeX starter](implementations/latex/starter.atlas.tex) into your working folder. All three carry the same initial content. The starter is a structurally valid **draft shell** with editorial sections, empty domain collections and explicit unanswered scope/source questions. Replace the document identity/authorship and develop the specification from actual needs. A valid starter is not a complete L1 specification and does not invent business requirements. Use the complete examples to learn populated contracts.

Prefer JSON for structural authoring, validate it, then produce reading/publication representations. A text-only edit in Markdown/LaTeX belongs inside the marked authoritative records. Structural changes must update the appendix consistently; derived diagrams are regenerated. Record authored changes as content revisions.

```bash
python translator/atlas_translate.py convert implementations/json/starter.atlas.json --from json --to markdown -o work/specification.atlas.md
python translator/atlas_translate.py convert work/specification.atlas.md --from markdown --to latex -o work/specification.atlas.tex
python translator/atlas_translate.py convert work/specification.atlas.tex --from latex --to json -o work/returned.atlas.json
```

The starter has no external resources. For resource-bearing documents, follow [the package contract](#resource-contract). The installed `atlas-spec` command and `python -m atlas_spec` expose the same interface. The launcher uses only this edition or the runtime bundled beside it inside the skill; it never selects another repository version or installs dependencies automatically.

<a id="implementations"></a>
## Representation implementations

| Implementation | Authoritative content | Ready-to-use files |
| --- | --- | --- |
| [Atlas JSON](implementations/json/README.md) | Complete `atlas` payload, including prose and structure. | [Schema](implementations/json/atlas.schema.json) · [Starter](implementations/json/starter.atlas.json) |
| [Atlas Markdown](implementations/markdown/README.md) | Visible marked text records plus an identified appendix for structure. | [Starter](implementations/markdown/starter.atlas.md) |
| [Atlas LaTeX](implementations/latex/README.md) | Visible text environments/cells plus a commented structural appendix. | [Starter](implementations/latex/starter.atlas.tex) · [Style](implementations/latex/atlas.sty) |
| PDF publication | A compiled rendering for reading and sharing. | Included beside each complete example; not a reversible source. |

A **schema** checks supported structure; a **starter** is a document to copy and fill; an **example** demonstrates filled contracts; `atlas.sty` supplies LaTeX macros and presentation. The grammars linked above define controlled Markdown/LaTeX profiles. Arbitrary documents in those languages are not automatically Atlas instances.

<a id="translation"></a>
## Translation process

Four primitive transformations, Markdown ↔ JSON and LaTeX ↔ JSON, support all **six directed conversions between distinct formats**. Markdown ↔ LaTeX passes through validated Atlas JSON content in memory. JSON is the reference translator's intermediate; implementing the abstract model does not require JSON storage.

1. Read the selected profile/version and reject unsupported input.
2. Decode authoritative text and structure; check slots and derived regions.
3. Validate the recovered payload, references, ownership, RF/graph reciprocity, RNF references and resource contracts.
4. Encode the target and regenerate its derived presentation.
5. Decode and validate that output again; compare the entire `atlas` payload with type-aware equality.
6. Write the result only after successful verification; report a diagnostic otherwise.

Use `package` separately when relocating resources. Compile and visually inspect PDF as a subsequent publication step. The converter preserves authored versions, language, requirements and revision; it does not perform editorial changes, cross-model translation or an OAL layer derivation. [Preservation](#preservation) defines the exact guarantee and weaker diagnostic flags.

For another implementing model, publish the concept/invariant mapping, valid artifact domain, constraints, exclusions and preservation evidence. For another representation adapter, implement versioned decode/encode against the shared content, register it and test its declared domain. It must preserve required text, structure, extensions and resources or reject unsupported input. Same-layer membership alone does not establish a universal translator.

<a id="reference-rules"></a>
<a id="abstract-model"></a>
## Abstract model

The following numbered sections define the model. Field spellings identify the delivered profiles' mapping; another model may recover the same semantic roles through a declared mapping.

<a id="model-1"></a>
### 1. Purpose and position

Atlas specifies a system declaratively. It records:

- which concepts exist;
- which information each concept carries;
- which relations are allowed;
- which invariants must hold;
- how elements are identified and referenced;
- how behavior and its conditions are represented;
- what every implementation of the model must preserve.

Atlas Specifications is a reusable **abstract model of OAL L1 (UCS)**. OAL L1 defines responsibilities for reusable models; a project specification is an artifact of its selected model. Atlas establishes the L1 responsibilities of scope, actors and authorization, behavioral contracts, entities and rules, dependencies, complementary obligations, acceptance links, consistency, optional domains, and examples. It does not claim L2, L3, L4, an OAL derivation engine, or complete OAL coverage. The declared scope and correspondence are in [OAL correspondence](#oal-conformance).

The abstract model is independent of JSON, Markdown, and LaTeX. It can be explained and reviewed without reading any of the three implementations.

<a id="model-2"></a>
### 2. Model, implementation, instance

| Object | Meaning | Example |
| --- | --- | --- |
| OAL L1 metamodel | Responsibilities an L1 model must establish. | OAL Stable-v1.0.0 UCS rules. |
| Atlas abstract model | Reusable semantic concepts, relations, invariants, and preservation obligations. | This document. |
| Implementing or specializing model | Another reusable model with an explicit mapping to Atlas and the obligations it preserves. | A future domain-specific specification model implementing Atlas. |
| Representation implementation | A concrete syntax carrying the content of the selected model. | Atlas JSON, Atlas Markdown, Atlas LaTeX. |
| Project artifact / instance | Concrete content conforming to its selected model, possibly spread across several files. | The task-board specification. |
| Publication | A rendering of an instance for reading. | A PDF compiled from Atlas LaTeX. |

Other models MAY implement or specialize Atlas. Their conformance statement MUST identify their version, supported scope, concept mapping, additional constraints, unsupported constructions, and evidence that all obligations in the claimed scope remain recoverable. A specialization cannot remove an Atlas obligation while claiming full conformance. Different names or storage structures are permissible when their mapping is explicit. This relationship does not add an OAL layer or prescribe an additional metalevel.

The three delivered implementations are representation profiles of the same Atlas content model; three files do not establish three distinct OAL models. An implementing model may itself have several representations. Translation between distinct models requires its own declared mapping and preservation contract; these codecs do not provide that translation automatically.

Atlas JSON is the supplied translator's intermediate representation. It is not the abstract model. The field names in this specification describe semantic roles and map to the reference profiles; another implementing model may recover the same roles differently. JSON Schema, marker syntax, transport envelopes, and codec metadata are obligations of those profiles, not prerequisites for the existence of an Atlas implementing model. A PDF is a compiled publication, not a fourth reversible profile or a translator source.

<a id="model-3"></a>
### 3. Document identity and versions

Every Atlas artifact declares document identity, revision, selected model/version, language, review status, title, authorship, and creation/update dates. The delivered profiles map these roles as follows:

| Field | Meaning | Requirement |
| --- | --- | --- |
| `document_id` | Stable identifier of the specification document. | Required; follows the ID grammar. |
| `revision` | Revision of this document's content. | Required, non-empty string. |
| `spec_version` | Atlas abstract-model version implemented by the content. | Required; `Stable-v1.0.0` in this version. |
| `profile_version` | Version of the representation profile being used. | Required by the three delivered profiles; `Stable-v1.0.0`. |
| `translator_version` | Declared producer version retained in reference-profile content. | Required semver string by the delivered profiles; `1.0.0` for newly generated examples. It is not a content migration. |
| `language` | Language of the document's authored text (BCP 47-like tag). | Required. |
| `status` | Review/approval status of the document. | Required; independent of `nature`. |
| `title` | Authoritative document title. | Required text record. |
| `subtitle` | Optional subtitle. | Absent, `null`, or a text record; these are distinct. |
| `authors` | Document authorship. | Required list; authorship alone does not identify the accountable person for a claimed derivation (§16). |
| `created`, `updated` | ISO dates. | Required. |

A conversion MUST NOT change these values. A translator that cannot represent the declared version must reject the document. Representation conversion is not version migration.

<a id="model-4"></a>
### 4. Core concepts

The normative concept groups are:

| Concept | Purpose | Cardinality |
| --- | --- | --- |
| Section | Ordered editorial chapter with title, blocks, and references to concept elements. | At least one. |
| Actor | Person, system, organization, role, or other external participant. | Any; referenced by cases. |
| Term | Domain vocabulary with definition and optional synonyms. | Any. |
| Type | Named data type, constraints, and examples. | Any. |
| Entity | Data and relationships with identity, fields, states, transitions, validity conditions, and examples. | Any. |
| Validation | Named validity rule owned by an entity, with inputs, conditions, results, and a flow graph. | Zero or more per entity. |
| Tool | Abstract capability with one or more operations and contracts. | Any. |
| Use case | Behavior with objective, actors and permissions, inputs, conditions, dependencies, outcomes, RFs, RNFs, flows, acceptance criteria, and traceability. | Any. |
| Boundary | Interaction modality exposing use cases with explicit mappings. | Any. |
| Graph | Structured flow, state, or relation graph owned by a document, entity, validation, or use case. | Any; required where referenced. |
| Resource | Local or referenced visual/asset catalog entry with bytes, hashes, captions, alternative text, embedded text, and variants. | Any. |
| Assumption, decision, open issue, source, history entry | Recorded context, decisions, pending questions, provenance, and evolution. | Any. |
| Extension container | Declared opaque data under `extensions`. | Optional. |

Every declared actor, term, type, entity, tool, use case, and boundary has a stable ID and appears exactly once in the editorial structure. Sections reference concept IDs; the order of the `structure` array is the authoritative presentation order. A reference may point forward or backward; position in the document never changes identity or validity.

<a id="model-5"></a>
### 5. Text and rich content

Human-readable content is a text record: an object with a `text` member. Text records may optionally carry `id`, `nature`, `review_status`, `meta`, and `extensions`. The model never treats an absent text member as an empty string. The declared free-form `meta`, entity-example `data`, and `extensions` containers are opaque structural data: a key named `text`, `@text`, or `id` inside them is a literal data key, not an Atlas prose slot or element declaration. Their exact values and types are still preserved.

Rich content is an ordered list of blocks:

| Block | Required members | Meaning |
| --- | --- | --- |
| `paragraph` | `text` | Prose paragraph. |
| `note` | `text` | Author note. |
| `quote` | `text` | Quotation. |
| `heading` | `level`, `text` | Nested editorial heading (level 1–6). |
| `list` | `ordered`, `items` | Ordered or unordered list; items are text records with optional `children`. |
| `code` | `text`, optional `language` | Literal code; never executed. |
| `formula` | `text`, optional `display` | Formula source; never executed. |
| `figure` | `resource`, optional `caption`, `alt` | Reference to a catalog resource. |
| `table` | `columns`, `rows`, optional `caption` | Cell matrix of text records. |

Text is preserved exactly. Spaces, tabs, authored line endings, trailing spaces, Unicode sequences, and the presence or absence of a final newline are content. Implementations may introduce source-format line breaks, but those structural breaks MUST be distinguishable from authored breaks. No Unicode normalization, trimming, case folding, or language translation is allowed during conversion.

A distinction of nature (`observed`, `desired`, `inference`, `assumption`, `open_issue`, `decision`, `note`) answers **what kind of claim this is**. A review status (`draft`, `proposed`, `reviewed`, `approved`, `rejected`, `deprecated`) answers **where the claim stands in review**. They are independent and must not be conflated.

<a id="model-6"></a>
### 6. Identity and references

IDs use:

```text
[A-Z][A-Z0-9]*(-[A-Z0-9]+)+
```

Examples: `ENT-REQUEST`, `VLD-REQUEST-QUANTITY`, `UC-REQUEST-SUBMIT`, `RF-REQUEST-01`, `N-REQ-START`, `RES-REQUEST-WIRE`.

Rules:

1. IDs are globally unique across the document, including IDs of nested fields, validations, operations, graph nodes, and graph edges. `document_id` shares the namespace.
2. References are IDs, never positions. The only exceptions are qualified mapping strings in boundary input/result mappings (`form.code`, `result.invalid_data`), which are explicit mapping labels, not element references.
3. References are validated in both directions where a relation is declared by both sides. For example, an RF lists the graph elements it applies to, and those elements list the RF in `requirement_refs`.
4. IDs are stable through editorial reordering and conversion. Conversion MUST NOT regenerate them.
5. A missing reference, duplicate ID, or declared top-level concept omitted from editorial placement is a validation error, not a warning. A declaration need not be consumed by another concept merely to be documented.
6. An amendment retains an ID when the concept retains its identity; a replacement or split records the retired ID, successor IDs, reason, and affected references in history/decisions. A deleted concept cannot leave dangling references. A conversion never performs this editorial change.

<a id="model-7"></a>
### 7. Consumption rules

The primary presentation order is:

**entities → abstract tools → use cases → interaction boundaries.**

Context, objectives, scope, actors, vocabulary, types, and conventions may precede them.

| Element | May consume |
| --- | --- |
| Entity | No collaborator. |
| Abstract tool | Entities (as data meanings/types). |
| Use case | Entities, abstract tools, and other use cases of the same application. |
| Boundary | Use cases. |

Additional constraints:

- In the delivered Atlas profile, a tool declares a capability without internal tool/use-case calls. This is an Atlas modeling restriction, not a universal OAL rule. A specializing model that exposes composition must state its mapping and preserve the case-facing contract.
- An entity referencing another entity is a structural data relationship, not permission to query a service or infrastructure. Structural references are marked with `structural: true` in relationships in the examples; the model distinguishes the relation from a call.
- A case that needs an external condition requests it through a tool contract and applies the result. The entity does not gain collaborators because its validity depends on external state.
- Domains, when modeled, organize use cases; they do not duplicate entities or introduce dependencies. This version does not require a domain object; editorial sections can express grouping without changing the model.
- A use-case call preserves the called case's contract, actor context, and authorization conditions. The calling case records contract and authorization text; case composition is not permission escalation.
- Boundary interactions may reference only RFs from the case they expose. A newly discovered **domain need** is added to the responsible case and traced. A solution-introduced channel choice remains an interaction decision outside the L1 claim; it does not become a case RF merely because it appears in a boundary (§11).

<a id="model-8"></a>
### 8. Entities and validations

An entity defines:

- ID and name;
- domain meaning;
- identity description and identity fields;
- fields with type, cardinality, requiredness, meaning, constraints, and valid/invalid examples;
- relationships with target entity, kind, cardinality, description, and whether the relation is structural;
- states and transitions when relevant;
- validations;
- entity-level valid and invalid examples;
- assumption and open-issue references.

A validation declares:

- ID and name;
- scope: `field`, `between_fields`, `transition`, or `entity`;
- full statement;
- inputs and their meanings/sources;
- conditions with IDs, full text, and meanings;
- results (`pass`, `fail`, `error`, `not_applicable`) with descriptions;
- a flow graph owned by the validation;
- optional notes.

An entity owns its canonical intrinsic validity rules and does not gain collaborators. A condition involving external state is identified explicitly as contextual: the responsible use case obtains that state through a tool and applies the condition. Do not silently convert a contextual condition into a self-sufficient entity invariant.

A tool receiving an already valid entity assumes its intrinsic invariants and does not duplicate those checks. A contract accepting raw records identifies the construction/hydration point that applies canonical entity validation. Contextual authorization, uniqueness, existence, concurrency, and other conditions outside the ready entity remain explicit case/tool obligations where relevant. Data-only entities are allowed; Atlas does not require methods or an implementation language.

Validations are referenced by use cases; the entity owns the definition, the case owns application and behavior. For example, `VLD-REQUEST-QUANTITY` defines the positive-integer rule in the entity; `RF-REQUEST-02` in the case requires applying it and refusing invalid input.

<a id="model-9"></a>
### 9. Abstract tools

A tool defines a capability, not an implementation. Each operation declares:

- ID, name, purpose;
- inputs with names, types, meanings, requiredness;
- conditions of use;
- results with names, types, meanings, and guarantees;
- observable effects;
- failures with codes, meanings, and how the consumer distinguishes them;
- guarantees.

Where applicable, the contract also states atomicity, conflict behavior, and whether a failed response proves that an effect was not applied or leaves the outcome unknown. An unavailable response alone is not evidence of rollback. A signature alone is not a contract. The model deliberately does not prescribe databases, protocols, internal algorithms, or flowcharts for tool internals. Concrete implementation choices are outside this version and must satisfy consumer cases and contracts.

<a id="model-10"></a>
### 10. Use cases, RFs, and RNFs

A use case declares:

- ID, name, objective;
- an explicit initiating actor, permitted actor set, and applicable authorization conditions;
- trigger and context;
- inputs and entry conditions;
- entities used and validations applied;
- tools and operations used;
- other use cases called, with contract and authorization;
- outcomes: success, refusal, failure, or effect, each with description and effects;
- functional requirements;
- non-functional requirements;
- main flow graph and subflow graphs;
- a complete textual representation of the flows;
- acceptance criteria;
- traceability links;
- assumptions, sources, and open issues.

#### Actor context and authorization convention

The reference profiles use existing text fields; they do not require a technology, a class, or a universal actor-context JSON object:

1. `trigger` identifies the initiating actor by stable actor ID.
2. `actors[].permission` and `description` identify permitted roles and conditions.
3. `context` states the required caller-context information, its resolution origin, trust assumptions, and whether/when caller identity and authentication are required. A caller is the concrete person or system on whose behalf the request occurs; an actor is a declared interaction role.
4. `entry_conditions`, RFs, outcomes, and flow text state the observable denial for absent, unresolved, insufficient, or unauthorized context. No protected effect occurs before authorization. Missing context MUST NOT be interpreted as anonymous participation.
5. Anonymous or system participation, if allowed, is explicit. A derivation owner or document author is not automatically a runtime actor.
6. A composed case receives the relevant context and still applies its own contract; authorization cannot be bypassed by calling it indirectly.

These are semantic obligations. The validator checks references and structure; it cannot prove the adequacy of the authored trust/authorization prose.

#### 10.1 Functional requirements

All **L1 domain behavior** declarations classified as RF belong to use-case cards. There are no independent authoritative catalogs of those RFs in entities, tools, or boundaries. An external interaction restriction may be recorded with its origin; a solution-introduced channel choice belongs to L4 and is not reclassified as an RF by this convention. A general requirement index may be generated, but it is not an authoring location.

Each RF has a stable ID, a complete statement, scope, applicable targets, and `flow_refs`. It appears:

1. in the case's RF list;
2. on the pertinent graph elements (`requirement_refs`), which may be nodes, edges, or subflows.

The relation is many-to-many: one RF may cover several elements and one element may cover several RFs. The validator requires bidirectional consistency between `flow_refs` and each element's `requirement_refs`. This is coverage checking by ID; it does not prove that prose and drawing have the same meaning.

#### 10.2 Non-functional requirements

All declarations classified as RNF belong to use-case cards, in lists, with no graph of their own. An RNF records:

- ID and full statement;
- scope: `case`, `operation`, `interaction`, or `system`;
- identified origin, linked to a source or explicit documented premise/decision;
- applicability conditions;
- verifiable criterion;
- optional metric (name, unit, target as decimal string, operator);
- optional measurement start/end;
- verification method/scenario;
- references to affected elements.

A shared obligation has one canonical full definition and explicit references from other cases' RNF lists (`reference_to`). A reference chain is invalid, and a local self-reference is invalid. A target is not automatically divided among tools. If a quality condition requires a functional action, that action is an RF in the relevant case; the RNF remains in its list.

The declaration location and the obligation's reach are different: an RNF written in a case may cover the case execution, an operation it uses, or a complete interaction. Every obligation's origin MUST be recoverable individually. In the reference profiles, use `references` to source/assumption/decision IDs and state the origin in its statement or applicability; a generic document bibliography alone is insufficient. Numerical targets are authored requirements or explicitly labeled proposals/examples, never values invented by conversion.

Acceptance criteria identify the obligations they verify and an observable result. A shared integration criterion identifies its scope, affected case IDs, and one canonical definition, with explicit references elsewhere. This does not create extra use-case identities.

<a id="model-11"></a>
### 11. Interaction boundaries

A boundary declares:

- ID, name, modality (`web`, `app`, `cli`, `api`, `message`, `desktop`, `other`), purpose, audience;
- interactions available;
- for each interaction: exposed use case, trigger, description, input mapping, result mapping, referenced RFs, resources, examples;
- assumptions, sources, open issues.

Boundary material MUST distinguish its responsibility and origin in `purpose`, interaction `description`, and/or source-linked notes:

| Classification | L1 treatment |
| --- | --- |
| Domain interaction need | State the responsible case behavior and references; preserve authorization and domain semantics. |
| Externally imposed interaction restriction | Keep the restriction and its identified origin in L1, even when it mentions a protocol, route, or representation. |
| Solution-introduced channel decision | Label it as an L4 decision/reference or proposal; exclude it from the L1 conformance claim. |
| Illustration or exploratory wireframe | Label it as illustrative; it neither establishes an external requirement nor replaces explicit contracts. |

Route names, screen layout, payload encoding, and protocol choices introduced by the solution belong to ADIB (L4). Mentioning one in an Atlas package does not relocate it to L1. A file may contain references or illustrative material from another responsibility if the scope remains identifiable. If an interaction choice reveals a new domain need, revise the responsible UCS case and analyze affected derivations.

The boundary maps inputs/results; it does not absorb case authorization or domain decisions. Authorization remains effective for direct and composed calls. A wireframe cannot be the only statement of a required domain behavior. The Atlas translator preserves these declarations but does not implement ADIB.

<a id="model-12"></a>
### 12. Graphs and images

Graphs are structured data, not images. A graph has:

- ID, kind (`flow`, `state`, `relations`), owner (document, entity, validation, use case), title;
- nodes with ID, type, label, optional call (`validation`, `tool`, `operation`, `use_case`, `entity`), optional inputs/outputs/details, RF references;
- edges with ID, source, destination, optional label/condition/priority, RF references;
- optional notes.

The node type vocabulary for this version is: `start`, `end`, `action`, `decision`, `validation`, `tool`, `operation`, `use_case`, `result`, `refusal`, `failure`, `effect`, `note`, `state`, `entity`. Unsupported node kinds are rejected. Array order is meaningful for authoring and rendering; IDs and references do not depend on it.

The validation graph is the validation's flow. A case's main and subflow graphs are listed in its `flows` object. State/relation graphs are allowed for entities/document. The graph is the source for Markdown topology text and LaTeX TikZ drawings. Figures and flow tables are derived from the same graph; no independent copy of the logic is authoritative. Images derived from a graph record the graph fingerprint in `drawing_source.revision` and declare `derived_from_graph`; a mismatch is a stale-figure diagnostic.

A PDF may include TikZ flowcharts for validations, main flows, subflows, and state/relation diagrams. RNFs do not get their own diagrams, and tool internals do not get algorithm flowcharts.

<a id="model-13"></a>
### 13. Resources

The resource contract applies to images and files that carry or illustrate specification information. Purely decorative publication artwork, such as a cover ornament or a brand image with no specification meaning, belongs to the publication style and MAY remain outside the catalog. Such decoration MUST NOT be the only carrier of a requirement, actor, entity, rule, graph, acceptance criterion, provenance claim, or other specification information. A semantic resource cannot be exempted from preservation simply by calling it decorative.

A resource catalog entry records:

- ID, source URI (optional, may be `null`), package path, media type, size, SHA-256;
- caption and alternative text as text blocks;
- text present in the image (as text records);
- drawing source path/revision/tool;
- variants with path, media type, size, hash, relation, source, producer;
- optional derived-from-graph ID.

Resource originals are preserved. Conversions do not recompress or replace them. Variants are explicit and linked to the original. A catalog URL is only a reference; byte preservation requires the packaged files. The translator works offline when the files are present. A reference-only mode is not offered; `--no-check-resources` weakens validation and must not be described as byte preservation.

Text present inside an image must also occur in common textual content; pixel preservation alone is insufficient.

<a id="model-14"></a>
### 14. Editorial structure and appendices

The `structure` array is ordered. Each section has an ID, a relative level (1–5), a title text record, narrative blocks, and an ordered list of concept IDs. Every actor, term, type, entity, tool, use case, and boundary appears exactly once in the structure. Graphs, resources, assumptions, decisions, open issues, sources, and history are presented in generated appendices; they are still part of the document model.

Narrative blocks preserve the authored order. The appendices are part of the document, not an alternate model. Section order determines presentation only; references may point anywhere.

<a id="model-15"></a>
### 15. Presence, absence, null, empty, unknown

The model distinguishes:

| Form | Example | Meaning |
| --- | --- | --- |
| Absent member | no `subtitle` key | The document does not declare a subtitle at all. |
| `null` | `"subtitle": null` | The document explicitly declares no subtitle. |
| Empty text | `"subtitle": {"text": ""}` | The subtitle exists and is an empty string. |
| Empty list | `"notes": []` | The list is declared and contains nothing. |
| Unknown | not represented in this version | Atlas has no universal “unknown” sentinel; use an open issue, pending assumption, or an explicitly documented extension. |

Implementations MUST preserve these distinctions. A converter may not collapse absent and `null`, or empty and missing, to make a test pass.

<a id="model-16"></a>
### 16. Assumptions, decisions, open issues, sources, history

- An assumption has a statement, status (`open`, `validated`, `refuted`, `withdrawn`), and affected IDs.
- A decision records title, context, decision, alternatives, consequences, status, and references.
- An open issue records title, description, status, and references.
- A source records title, optional URI, revision, access date, and notes.
- A history entry records version, date, and description.

These records are referenced by cases/entities/boundaries or the document. They remain distinguishable from facts and requirements. Their status does not change the nature of the underlying statement. Sources MUST have sufficient identity/revision to locate the origin actually used; a link to a mutable homepage alone is not a baseline.

When an artifact claims a **Needs-to-L1 derivation**, record the external needs model's identity/version, the selected destination Atlas or implementing model/version, source and destination artifact baselines, a named accountable person, declared scope, and added decisions. The reference profiles may record these in source notes, document notes, decisions, and history; clear labeled prose is valid. Roles, "the team", and an AI tool do not substitute for the person's name. Do not fabricate this record when information is unavailable: mark the provenance unresolved and limit the claim.

Needs reconstructed from a UCS remain labeled reconstructed; synthetic teaching examples remain labeled synthetic. Neither is independent stakeholder evidence. A manual derivation records the same provenance and obligations, but does not thereby claim a constructed/executed transformer or Engine Needs-L1. A representation conversion also does not create such a derivation claim.

A changed contract, permission, or interaction decision records affected models, transformers, artifacts, and verification scenarios when those exist. For an L1-only artifact, record its impact and identify downstream work that has not yet been produced or evaluated.

<a id="model-17"></a>
### 17. Extensions

Unknown members at known object levels are rejected. A document may declare opaque data under an `extensions` object (namespace keys). The translator preserves extensions structurally and does not interpret them. Extensions must not be used to remove required content or to claim a different version. A format that cannot preserve an extension must reject the document rather than drop it.

<a id="model-18"></a>
### 18. Normative invariants

An artifact conforms to the abstract model only when its semantic obligations above and the applicable invariants below hold. For the three delivered profiles, structural conformance is additionally checked with the published JSON Schema, profile grammar, and validator. Passing those checks does not establish the truth of authored requirements or complete OAL conformance.

1. The artifact identifies its selected model/version and a representation capable of recovering the claimed content.
2. Required concepts, metadata, contracts, authorization, origins, acceptance conditions, and distinctions are recoverable without guessing.
3. Every ID is globally unique and follows the grammar.
4. Every reference resolves.
5. Every concept element appears exactly once in the structure; no unknown element is placed.
6. Entity identity fields, relationship targets, state transitions, and validation flow owners resolve.
7. A case's actor references, entity/validation uses, tool/operation pairs, and case calls resolve.
8. Every RF has at least one flow reference; each flow reference exists in the case's graphs; each graph RF reference exists in the case's RF list; and the relation is mirrored on both sides.
9. RNFs either have a full definition or a valid reference to a canonical full definition in another case; no chains or local self-references. Their applicability/references resolve, and each obligation has an identified origin, scope, and verifiable condition.
10. Boundary interactions reference an existing use case and only that use case's RFs; resources exist.
11. Graph owners match their graph kind, graph calls resolve, and edge endpoints exist.
12. Resource paths are safe and, when checking is enabled, files exist with matching size and SHA-256.
13. Resources derived from a graph record the current graph fingerprint.
14. Text embedded in a specification resource also occurs in common textual content.
15. Every required text record exists; absence, null, and empty remain distinct.
16. Every representation carries all text records exactly once and every structural member.

<a id="model-19"></a>
### 19. Authoritative sources and derived presentation

- In Atlas JSON, fields are authoritative for both text and structure.
- In Atlas Markdown and Atlas LaTeX, the visible marked text records are authoritative for prose. The clearly identified structure appendix is authoritative for non-text data.
- A visible change to an authoritative text record is imported.
- A change to a derived region (summary, topology, TikZ) without regenerating it produces a diagnostic with instructions. Derived content is identified as derived and verified.
- No representation may hide all text in a payload and ignore the visible body. No representation may silently prefer an old embedded copy over visible authored text.

<a id="model-20"></a>
### 20. Preservation obligation

Every valid conversion preserves the entire Atlas content: titles, paragraphs, notes, requirement and validation statements, contracts, examples, code, formula sources, captions, descriptions, node/edge labels, authored comments classified as content, declared metadata, types, values, IDs, references, relevant orders, graph structure, and preserved resource information/files.

Conversion does not summarize, paraphrase, correct, translate, reorganize logic, or update requirements. Equality is defined in [preservation contract](#preservation). JSON/Markdown/LaTeX need not have identical bytes; syntax differs. PDF pagination is not part of the reversible guarantee.

<a id="model-21"></a>
### 21. What an implementation must preserve

An implementation of Atlas must:

- carry all required concepts and their relations;
- preserve IDs, references, and relevant order;
- preserve exact text records and their metadata;
- preserve the editorial structure and appendices;
- preserve graph topology and labels;
- preserve resource catalog data and bytes (in full preservation mode);
- distinguish absent/null/empty and nature/review status;
- preserve extensions or reject the document;
- declare how its semantic concepts map to Atlas and how conformance is reviewed;
- if it claims compatibility with the supplied interoperability profiles, provide and verify a conversion path to/from Atlas JSON for its declared domain without changing Atlas version;
- diagnose unsupported constructions and inconsistencies instead of guessing.

#### Abstract-model conformance and codec interoperability

A model may implement Atlas without using JSON. That claim is assessed against the semantic contract and its mapping, not by JSON file existence. Compatibility with the **supplied translator** is a separate claim requiring the applicable profile grammar and adapter. A partial mapping states its domain and unsupported content; it cannot claim full, lossless interoperability. An honest loss report does not satisfy the full-preservation contract.

<a id="model-22"></a>
### 22. Non-goals

This version does not define: executable validation expressions, a concrete tool implementation, UI layout, HTTP routes, a database schema, automatic requirement generation, automatic version migration, a general Markdown/LaTeX importer, or a guarantee that a business application satisfies an RNF. Those belong to later versions or to other OAL layers.

<a id="graph-contract"></a>
## Graph structure and publication

The abstract model's graph obligations apply to all implementations. The delivered profiles serialize `id`, `kind`, `owner`, `title`, `nodes`, `edges`, and optional `notes`. The owner includes `kind` and `id`; both must resolve consistently. A graph contains at least one node and may have an empty edge list.

| Element | Profile contract |
| --- | --- |
| Node | Global ID, supported type and label; optional `call` to a validation, tool, operation, case or entity; rich input/output/detail blocks and RF references. |
| Edge | Global ID, `from` and `to` in the same graph; optional label, condition blocks, integer priority and RF references. |
| Validation flow | Referenced by the validation's `flow` and owned by that validation. |
| Case flow | Main/subflow graph referenced by `flows.main`/`flows.subflows` and owned by that case. |
| State/relation graph | May be owned by an entity or the document. |

A graph cannot be owned by one element and nominated by another. Node and edge array order is preserved. Each RF/graph association must resolve and be reciprocal in both directions, within the owning case's graphs.

Markdown displays authoritative node/edge text records and a generated `DERIVED-GRAPH-<id>` topology. LaTeX emits a deterministic `TIKZ-<graph-id>` region: wrapped labels, short edge keys and an exact edge-ID/label legend. The complete structured listing retains all nodes, edges and conditions. Reimport regenerates derived content and rejects stale edits. A graph image identifies its graph and fingerprint as described in the resource contract.

Validation flows, case main flows, subflows and declared state/relation diagrams may appear in a PDF. RNFs have no separate flow, and abstract tools do not expose internal algorithm diagrams. The renderer is not a general layout engine. Large graphs can become small when scaled; meaningful subflows and visual review improve publication without deleting content. There is no model-imposed node/edge count limit. Extending the node vocabulary requires a new declared profile capability, matching schema/renderer support and verification.

<a id="resource-contract"></a>
## Resource catalog and packages

A specification resource is catalogued with its ID, package-relative `path`, media type, byte size and SHA-256; caption/alternative text; visible `embedded_text`; drawing source path/revision/tool; explicit variants; and optional `source_uri` and `derived_from_graph`. `source_uri` may be a string or `null`. A variant records path, media type, size/hash, relation, `derived_from` path and optional producer. The original remains available alongside its variants.

- Validation resolves each original and variant inside the declared resource root, opens it and compares size and SHA-256. A path escaping that root, missing file, wrong size or wrong hash is an error.
- Conversion preserves the catalog but does not copy, rewrite, replace, recompress or download resources. URLs remain references. Local resources allow offline conversion.
- `--no-check-resources` skips byte access/checks. It preserves catalog content with a weaker guarantee, which must be stated explicitly.
- Text visible in an image must also occur in common textual content, such as captions, alternative text or graph labels. Missing textual occurrence produces `ATL-E-RESOURCE-TEXT`.
- A graph-derived figure declares `derived_from_graph`; its `drawing_source.revision` equals the SHA-256 of the canonical JSON graph. A stale figure produces `ATL-E-FIGURE-STALE`. Rebuild the figure and record its new hash/fingerprint after a graph change.
- LaTeX requires a compilable PDF/PNG/JPEG resource or explicit variant. The original SVG stays available. Without a usable variant, encoding reports `ATL-E-LATEX-RESOURCE`.

The resource root normally is the input file's parent directory. Supply `--resources PATH` when input/output placement requires another root. To relocate an instance with its files, use the separate `package` command. It validates the source, copies the document and every catalogued original/variant byte-for-byte, includes the style file when available, and validates the packaged instance against its new root. It does not convert the representation.

```bash
python translator/atlas_translate.py package examples/minimal/example.atlas.json --from json -o work/request-package
python translator/atlas_translate.py convert work/request-package/example.atlas.json --from json --to latex -o work/request-package/example.atlas.tex
```

Assets are not embedded as binary data in Atlas JSON/Markdown/LaTeX. SHA-256 is the supported catalog hash algorithm. Variant creation is an authoring/publication task, separate from conversion. Repository identity images in the root `assets/` folder are documentation assets; they become specification resources only when an instance explicitly catalogues them.

LaTeX also supports [publication-only styles and decorative images](implementations/latex/README.md#publication-style). These are kept outside authoritative records and the resource catalog. The decoder does not read or execute the optional `atlas-presentation.tex` settings file or load its decorative images. Conversion does not preserve custom presentation settings, and `package` does not discover or copy those extra files; retain them separately when reproducing a customized PDF. Required catalog resources remain subject to all checks above.

<a id="preservation"></a>
## Preservation and equality

A verified conversion satisfies:

`decode_target(convert(source)).atlas == decode_source(source).atlas`

The comparison is recursive and type-aware over the **entire** `atlas` payload. It preserves every authored text record and its metadata, identity/version/revision fields, actors, concepts, contracts, requirements, acceptance, graph topology, resource catalog, sources, decisions, history, presentation settings and extension data. Object-member order is irrelevant; array order is content. Boolean `true` and integer `1` are different values for this contract.

Representation-level transport metadata is outside payload equality: the JSON envelope's `format`, its optional `$schema`, and representation header metadata. Those fields still undergo their own profile/version checks. PDF page layout, font substitution, pagination, external styles and purely decorative publication artwork are outside reversible source conversion. An optional `atlas-presentation.tex` file is not part of `atlas`; it is not serialized into JSON or reconstructed from it. In contrast, any presentation settings actually declared **inside** `atlas` remain content and are compared exactly. Author names, producer version declared **inside** `atlas`, source baselines, resource hashes and other authored metadata also remain content.

### Exact text and data

- Use UTF-8 without BOM; a BOM is rejected. Read and write source without newline translation.
- Preserve Unicode sequences, tabs, trailing spaces, LF/CRLF/CR and final-newline presence exactly. Do not normalize Unicode, trim, fold case or collapse whitespace.
- Distinguish absent members, `null`, empty text and empty lists.
- Preserve integers exactly. Use strings for decimal values; reject binary floating-point JSON numbers and non-finite constants. Reject duplicate object keys.
- Keep `meta`, entity-example `data` and `extensions` opaque. Literal `text`, `@text` and `id` inside them are data, not prose slots or global Atlas IDs.

### Text slots and derived presentation

JSON carries text and structure directly. Markdown/LaTeX carry each declared text value once in marked visible records; an identified structure appendix carries remaining data and `@text` slots. Each slot must correspond to exactly one body record. Missing, duplicate, orphan or multiply referenced slots are errors. Structural strings and opaque data stay in the appendix. The appendix cannot override visible prose or supply a hidden second copy of it.

The codecs remove only their own delimiter line breaks/prefixes and reverse documented escapes. Authored changes in authoritative text records are imported. Summaries, topology and TikZ are explicitly derived; reimport regenerates them from current structure/text. Divergence raises `ATL-E-DERIVED-STALE` or `ATL-E-TIKZ-STALE`. A graph change requires regeneration of derived regions and associated figures.

A successful verified conversion never summarizes, paraphrases, corrects, translates natural language, reorganizes logic or migrates versions. A loss of specification content, unsupported construction, invalid reference, malformed marker, stale figure or resource mismatch is an error; it cannot accompany a claim of full preservation. `--no-verify` disables the post-encode equality check for that diagnostic execution, and `--no-check-resources` weakens resource checking. Report those modes accurately.

Exact structural/text equality does not prove that a flow drawing expresses the prose correctly or that a requirement is suitable. Semantic and publication review remain necessary.


<a id="examples"></a>
## Complete examples

| Example | Modeling purpose | Representations |
| --- | --- | --- |
| [Minimal request](examples/minimal/README.md) | Entity validation, one request case, authorization and packaged illustrations. | JSON, Markdown, LaTeX, PDF and local SVG/PNG resources. |
| [Composition](examples/composition/README.md) | Booking lookup/create/cancel, composed calls, authorization and explicit persistence outcomes. | JSON, Markdown, LaTeX and PDF. |
| [Task board](examples/task-board/README.md) | Create/complete/list tasks, conflict handling, requirement/flow/acceptance links and synthetic needs. | JSON, Markdown, LaTeX, PDF, needs and traceability. |

These are didactic artifacts. Their assumptions and proposed targets are identified; they are not independent stakeholder evidence or an executed application's behavior. The JSON instance is each example's maintained content source. Rebuild the reading formats with `python examples/build.py`; use `--check` to verify the existing representations and `--pdf` to compile PDFs. Read the [example guide](examples/README.md) for resource and publication details.

<a id="ai-skill"></a>
## AI skill

Copy [skills/atlas-specs/](skills/atlas-specs/SKILL.md) as a complete folder. Its instructions select three workflows: **create/revise**, **read/audit**, and **convert/publish**. Read the relevant references on demand, start from the bundled draft, distinguish evidence from assumptions and validate the artifact. Structural success never authorizes an agent to fabricate requirements or declare stakeholder approval.

The skill includes a version-matched Python runtime and `scripts/atlas_translate.py`. That launcher corresponds to `translator/atlas_translate.py`; the runtime is copied from the canonical translator source, rather than maintained as a second algorithm. To run the skill alone, follow its dependency and command instructions from that folder. The delivered bundle is ready to use; consuming it does not require rebuilding it.

### What `skills/build.py` does

This is an edition maintenance helper. A standalone skill needs local copies of the material it consumes, so the builder synchronizes them from one maintained source:

- the canonical English model manual and the three representation guides, with links relocated for the bundle;
- the translator runtime and identical launcher, JSON Schema, LaTeX style, starter, dependency list, and license;
- a source map recording source and bundled hashes to identify divergence.

It also synchronizes the schema and style packaged with the canonical runtime. It preserves authored `SKILL.md`, workflow instructions, and agent metadata. Run `python skills/build.py` from this edition after changing a canonical source, then `python skills/build.py --check` to verify correspondence. The check is read-only and returns a failure when generated files are stale. Keeping this helper avoids maintaining independent copies manually; it is not a prerequisite for creating or converting a specification.

<a id="verification"></a>
## Verification and publication

From this edition directory:

```bash
python -m pip install -e ".[test]"
python -m pytest tests
python examples/build.py --check
python skills/build.py --check
```

The checks cover strict loading, schema/references, identity/ownership, RF/graph reciprocity, shared RNFs, exact text and opaque data, resources, diagnostics, packaging and post-encode equality. Edition and skill portability are checked separately from semantic claims. A finite test collection establishes behavior only for its exercised cases; it is not a proof over every possible input.

For PDF publication, install pdfLaTeX and the packages used by [atlas.sty](implementations/latex/atlas.sty), then run `python examples/build.py --pdf`. The build runs two TeX passes in temporary output storage and replaces a publication only after success. Inspect the rendered pages, tables and graph legends. Conversion itself does not invoke TeX. Compilation success does not establish visual quality, and the resulting PDF is not accepted as a reversible input.

The supplied preamble supports a pdfLaTeX path and provides conditional XeLaTeX/LuaLaTeX support for broader scripts. Actual compilation evidence applies only to the engine exercised; it does not cover every font/engine combination. The project artwork is maintained separately at the repository root. With the complete repository available, run `python -m pip install ".[assets]"` and `python ../../assets/sources/render_images.py` from this edition to render it; the root `assets/README.md` documents the graphical dependencies. This presentation-only command is not required when using a copied edition.

Semantic review must still assess objectives/scope, claim origins, actor context and authorization, complete effects/failures, rule ownership, complementary obligations, acceptance/traceability and boundary responsibility. A contract about application behavior is not an observed runtime result. The OAL correspondence below specifies the scope of the model claim.

<a id="conformance"></a>
<a id="oal-conformance"></a>
## OAL L1 correspondence

### Baseline and claimed object

| Item | Pinned reference |
| --- | --- |
| OAL edition | **Stable-v1.0.0** |
| Repository | [OAL — Open Analysis Layers](https://github.com/CodeVaultCommunity/OAL_OpenAnalysisLayers) |
| Commit | `ce225141686d4b6b3e46923866c97d84c031903f` |
| Normative source | `versioning/Stable-v1.0.0/README.md`, [snapshot of received bytes](verification/oal/README.md.txt) |
| SHA-256 | `d6ad987008c200460af919eff3b03989dca5a3b0f7e14d7a9d5b4e67f598b2da` |
| Provenance | Clean local checkout; remote publication pending. [Identity](verification/oal/baseline.json) and [clause review](verification/OAL-CORRESPONDENCE.md). |
| Relevant clauses | Numbered cross-layer rules and UCS rules 1–10. OAL's context skill is informative. |
| Atlas model | **Atlas Specifications Stable-v1.0.0**, [abstract model](#abstract-model) |
| Claimed scope | Reusable abstract specification model of **UCS (L1)**; the three reference representation profiles and their preservation contract. |
| Assessment type | Normative document correspondence and explicit scope review. Executed code checks are reported separately in [verification](#verification). |

The model establishes the responsibilities listed below for artifacts in its declared scope. **An artifact must still satisfy those responsibilities.** A JSON Schema result, a conversion round trip, or an example's existence is not complete semantic approval of the artifact.

Atlas does not claim ADMV (ADPM + ADVS), ADI, ADIB, complete OAL layer coverage, an Engine Needs-L1/L1-L2/L2-L3/L3-L4 realization, or transformer construction/execution. The converter changes representations of one model. A package may contain illustrative boundary references without claiming an L4 implementation.

### UCS correspondence and review evidence

“Established” below means that this Atlas model explicitly requires the subject. It is a document-level assessment, not proof that every instance satisfies it or that the future application behaves correctly.

| UCS clause | Atlas requirement and mapping | Instance review / evidence needed | Assessment |
| --- | --- | --- | --- |
| **1 — Scope** | Abstract model §§1–4 and 14 require objectives, system boundary, actors, external participants, and context. Ordered sections hold scope without prescribing application code organization. | Recover the system's objectives, in/out scope and external participants from the artifact. | Established. |
| **2 — Use cases** | §§6 and 10 require stable ID, objective, initiating actor, permitted actor set, authorization conditions, required caller context, trust/resolution origin, and authentication policy. `trigger`, `actors[].permission`, `context`, RFs and outcomes carry this explicitly. | Review direct/composed calls, explicit anonymous/system choices, and denial for absent, unresolved, insufficient, or unauthorized context. No protected effect before authorization. | Established; semantic review required. |
| **3 — Behavioral contracts** | §§9–11 require triggers, inputs, conditions, guarantees, results, effects, alternatives, failures and observable denial. §11 classifies domain needs, external restrictions, solution channel choices, and illustrations by origin/responsibility. | Review branches, failure/effect guarantees and source-linked external restrictions. Ensure introduced routes/screens/encodings/protocols are not promoted to L1 requirements. | Established; channel proposals are excluded from the L1 claim. |
| **4 — Entities and rules** | §§7–8 require meaning, identity, data, relationships, intrinsic validity, contextual rules, and responsible applying cases. Canonical rules are referenced, not copied into every tool. | Trace each domain rule to its owner and applying case. Distinguish already-valid entities from raw records and contextual checks. | Established. |
| **5 — Composition and dependencies** | §§7 and 9–10 require case dependencies and abstract capabilities, input/results, conditions, guarantees, failures and contextual authorization. No storage, protocol, or call mechanism is prescribed. | Review composed-case contracts and actor-context preservation; verify tool operations supply the information/effects consumers require. | Established. The local restriction on internal tool calls is not attributed to OAL. |
| **6 — Complementary obligations** | §10.2 requires every relevant persistence/security/isolation/observability/performance/accessibility obligation to have individual origin, scope, applicability, verifiable criterion, and references. | Review the source of each RNF and observable acceptance condition. Treat invented/didactic targets as proposals/examples. Keep channel choices at L4. | Established; relevance and sufficiency require review. |
| **7 — Acceptance and links** | §§6 and 10 require acceptance criteria and explicit links to needs/sources, actors, entities, rules, dependencies, and RFs/RNFs. Shared integration criteria have one definition, scope, and affected case references. | Review criteria and trace links. Preserve stable case identities when later-layer artifacts are produced; this repository does not produce those layers. | Established for L1. Later-layer correspondence is not demonstrated here. |
| **8 — Consistency and evolution** | §§3, 5–6 and 15–17 require canonical shared definitions, ID/history preservation, source records, and distinct facts, desired requirements, inferences, assumptions, decisions, pending issues and review status. | Inspect canonical definitions, reference resolution and change/impact records. An approved review status does not turn an assumption into a fact. | Established. |
| **9 — Domains (recommendation)** | §§7 and 14 permit domain grouping in editorial sections, identifying associated cases/entities without duplication. | If domains are adopted, review their boundaries and associations. | Supported as optional organization; no mandatory domain object. |
| **10 — Representative examples** | §§8, 12–13 and the [example collection](examples/README.md) keep examples subordinate to explicit rules and acceptance criteria. | Verify examples agree with the rules; do not infer missing requirements from a picture or example. They do not replace ADVS scenarios. | Established; example validity is assessed separately. |

### Cross-layer rules affecting this L1 model

| OAL rule | Atlas treatment | Claim boundary |
| --- | --- | --- |
| **1 — Models and artifacts** | §2 distinguishes OAL metamodel, Atlas abstract model, another implementing/specializing model, representation, concrete artifact, and PDF publication. | Formats and file counts do not count models or layers. No Needs layer is introduced. |
| **2 — Accountable derivations** | §16 requires source/destination model identities and versions, artifact baselines, named accountable person, scope, and added decisions **when a Needs-to-L1 derivation is claimed**. Clear notes/records are permitted; no fixed technology is imposed. | This requirement applies to entry into L1, including manual derivations. Missing provenance is unresolved, not inferred from authorship. Synthetic/reconstructed needs are labeled. No derivation claim is inferred from codec execution. |
| **3 — Case identity** | §§6 and 10 retain stable case IDs and acceptance links for downstream use. | Exact ADPM/ADVS/ADI correspondences can be checked only when those artifacts exist. Their absence here is outside declared coverage, not approval. |
| **4 — Changes and claims** | §§6 and 16 require recorded changes and impact on affected models, transformers, artifacts and verification when applicable. [Versioning](#versioning) separates migration from conversion. | A changed source does not silently validate downstream artifacts. |
| **5 — People and actors** | §10 distinguishes role/actor, concrete caller, actor context, authentication/authorization and derivation owner. Origin/trust assumptions are explicit. | No required job title, class, fixed context fields or authentication technology is invented. |
| **6 — Conformance claims** | This document states edition, model/version, responsibility, scope and evidence. The [implementation guide](#implementations) separates abstract-model conformance, profile validity, and codec interoperability. | Model conformance, artifact conformance, layer coverage and complete coverage remain different claims. |
| **7 — Derivation engines** | No OAL engine claim is made. The deterministic codecs operate inside the same model. | Codec tests are not evidence of constructing or executing an OAL cross-layer transformer. |
| **8 — Conversion / translation / derivation** | [Preservation](#preservation) defines exact Atlas-content equality for conversions. Another model needs an explicit translation mapping; a cross-layer derivation has its own obligations. | A documented loss does not fulfill this converter's lossless contract. A shared L1 label does not establish a universal translator. |
| **9 — Combined packages** | Illustration/reference material retains its responsibility. | Co-locating content does not demonstrate an engine, transformer or composition. |

### Assessing a particular artifact

Review an artifact in two parts:

1. **Mechanical profile checks:** syntax/schema, IDs, references, ownership, RF/graph reciprocity, RNF references, text slots, resource hashes/freshness, and decoded payload equality after conversion. Record the actual command, version, input and result.
2. **Semantic L1 review:** objectives/scope; origin and status of claims; initiating actor and actor-context policy; complete behavior and failures; rule ownership; suitable complementary obligations; criteria/traceability; and boundary responsibility. Name unresolved conditions instead of interpreting a mechanical pass as approval.

Use distinct statuses: **unspecified**, **not evaluated**, **not demonstrated**, **inconclusive**, **nonconforming**, and **satisfied for the declared scope**. The first four are not approvals. A known violated requirement is nonconforming; an absent evaluation is not the same finding.

The [task-board example](examples/task-board/example.atlas.json) demonstrates create, complete and list contracts. It is a didactic artifact, not independent stakeholder evidence and not a deployed application's conformance result. The minimal/composition examples are additional codec and modeling fixtures. Use the verification commands above to reproduce the mechanical checks.

### Atlas choices beyond OAL's minimum

The following are local Atlas decisions, not requirements imposed on every OAL model:

- The three concrete profiles and JSON intermediary.
- The ID grammar and single document namespace.
- RF/RNF authoring in use-case cards and bidirectional RF/graph coverage.
- Exact-character preservation, visible text slots, structural appendices and freshness diagnostics.
- Local resource originals/variants with hashes and preserved bytes.
- Versioned repository layout, skill packaging and PDF publication.

A semantic correspondence review supports the stated model-level scope. It is not a universal theorem, a runtime security audit, or a claim that unspecified downstream work is complete.


[Stable surface policy and compatibility matrix](COMPATIBILITY.md).

<a id="versioning"></a>
## Version identities and evolution

| Identity | This edition | Meaning |
| --- | --- | --- |
| Atlas model | `Stable-v1.0.0` | Abstract semantic contract. |
| Representation profiles | `Stable-v1.0.0` | JSON, Markdown and LaTeX grammars. |
| Python package | `atlas-spec` / `1.0.0` | Translator implementation and CLI. |
| Document revision | Artifact-specific | Authored content evolution, independent of the edition. |
| OAL reference | `Stable-v1.0.0` | External metamodel baseline. |

The [release notes](#release-notes) describe this Stable edition. Representation conversion does not migrate earlier prototype content or change the selected model.

Adapters select a representation/version explicitly. The envelope/header and content version must agree with the supported profile. Unsupported versions or constructions are rejected. Conversion preserves `spec_version`, `profile_version`, `translator_version`, document revision and history; it does not relabel old content with the running tool's version.

An element retains its ID while it retains identity. Replacement, deletion or splitting records the old ID, successors where applicable, reason and affected references; update those references before accepting the artifact. Changes to semantics and changes to serialization are reviewed independently. A future migration must identify its baselines, scope, responsible person and intentional content changes, then rebuild and verify representations and resources. It is a separate authored operation, not a codec side effect.

### Folder map

| Path | Responsibility |
| --- | --- |
| `README.md` / `README.pt-br.md` | Model contract, common rules and complete edition manual. |
| `implementations/` | Profile grammars, JSON Schema, matching starters and LaTeX style. |
| `translator/` | Canonical runtime and direct launcher. |
| `tests/` / `pyproject.toml` | Edition tests, dependencies and package configuration. |
| `examples/` | Maintained JSON sources, reading formats and PDF publications. |
| `skills/` | Portable skill and its local bundle builder. |
| `LICENSE` | License carried with the independently usable edition. |

Shared presentation assets live in the repository root at `assets/`, outside this edition. Resources that belong to an example remain inside that example. The distinction keeps the complete operational edition portable while the root carries project-wide illustrations.

<a id="authorship"></a>
## Authorship and license

Atlas Specifications was conceived and developed by **Douglas de Oliveira Alkimim**. Distributed under the [MIT license](LICENSE).

[GitHub](https://github.com/douglas-alkimim) · [LinkedIn](https://www.linkedin.com/in/douglas-alkimim/)
