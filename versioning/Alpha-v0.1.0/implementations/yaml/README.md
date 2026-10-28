# Minerva YAML · profile 0.1.0

English · [Português brasileiro](README.pt-br.md) · [Model rules](../../specification/model.md#reference-rules)

This is a representation of Minerva Blueprints `Alpha-v0.1.0`, targeting OAL `Stable-v1.0.0`. The canonical [JSON Schema](../../minerva_blueprints/schemas/minerva.schema.json) is packaged with the reference validator. A representation check establishes readable supported data, not the sufficiency of its semantics.

## Documents and roots

Two document kinds share `format: minerva-yaml`, `model_version: Alpha-v0.1.0` and `profile_version: 0.1.0`:

| Kind | Role | Required top-level groups |
| --- | --- | --- |
| `blueprint` | An integrated program/verification instance, including scope and provenance | `oal_edition`, `document`, `source_l1`, `adpm`, `advs`, `mirror`, `traceability` |
| `source` | A per-file binding/description; several units may occupy one file | `document_id`, `source`, `units`, `graphs`, `dependencies`, `limitations` |

The `--root` option identifies the ecosystem root. Every artifact path in these documents resolves from that root. The document supplied on the command line is an ordinary filesystem path. The recommended mirror root is `docs/L2_MinervaBlueprints`; alternatives such as `design/program` are valid. Given mirror root `R` and source path `P`, the record path is exactly **`R/P.yaml`**. For example, `apps/Billing/Task.go` maps to `docs/L2_MinervaBlueprints/apps/Billing/Task.go.yaml`. Directory names and source extensions are preserved.

Paths use `/`, are relative and cannot contain `..`, drive prefixes or backslashes. Resolved paths and symlinks cannot escape the selected root. Move the complete package to preserve relationships. `mirror.documents` lists all included records; `coverage: declared` means only the selected bindings, while `coverage: complete` additionally declares source scope through `include_patterns` and reasoned `exclusions`. Coverage of current source files is checked only with `--verify-code`.

## Model-to-representation mapping

| Model construction | YAML mapping and meaning |
| --- | --- |
| Document identity and revision | `document.id`, `revision`, `title`, `scope`, `responsible`; revision is a string |
| Authored state | `document.status`: `draft` or `reviewed`; review authority and pending approval remain explicit in prose |
| Document provenance | `document.nature`: `designed`, `reconstructed` or `mixed` |
| Decisions and observations | `document.decisions[]`: independent `id`, kind, statement, source, review status |
| Source baseline | `source_l1`: model/version, artifact path, document identity/revision, selected case IDs, authored catalogue and hash (required for reviewed blueprints) |
| Data entities | `adpm.entities[]`: fields, meaning, canonical construction, invariant references, behavior, dependencies |
| Primitive refinements | `adpm.types[]`: stable ID, primitive base, textual constraints |
| Tool capabilities | `adpm.tools[].operations[]`: semantic contract independent of mechanism |
| Program cases | `adpm.cases[]`: source case, application, objective, data, collaborators, rules, permission, behavior and failures |
| Canonical rules | `adpm.rules[]`: identity, owner, origin references, statement, kind |
| Wiring and ownership | `adpm.dependencies`, `composition.selection_location`, `composition.lifetimes` |
| Domain grouping | `adpm.domains[]`, reciprocal `case.domain_ref`; grouping alone grants no permission |
| Semantic algorithms | `behavior.summary`, steps, pre/postconditions, effects and graph references |
| Graphs | `adpm.graphs[]` and source `graphs[]`; structured owner, entry, nodes and edges |
| Behavioral identity | `advs.behavioral_tests[]`: one case/source-case link, criteria, scenarios and supporting-check references |
| Scenario oracle | Each scenario: preparation, actor context, action, boundary/configuration, expected result/effects, applicability and rationale |
| Supporting realization | `advs.supporting_checks[]`: its own contract and optional path/qualified-symbol/status reference |
| Observed execution | `advs.executions[]`: checks, implementation revision, environment, result, time, report and limitations |
| Declared gaps | `advs.unverified_risks[]` and document limitations; absence of a scenario does not become approval |
| Interaction obligations | `advs.channel_obligations[]`: statement, source and affected cases; scenarios link them through `obligation_refs` |
| Source binding | `source.path`, app, language, state, hash, purpose and observation; `units[].model_refs` preserve logical identity |

All objects have closed field sets in profile `0.1.0`; unknown fields are errors. There is no arbitrary extension namespace in this YAML profile. A future extension must receive an explicitly supported profile/mapping. Do not disguise unknown semantics as absent fields. This restriction belongs to the delivered profile, not to the abstract possibility of another Minerva representation.

## IDs and data types

IDs match `^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$`, for example `UC-TASK-001` and `BT-TASK-001`. They are globally unique across the loaded blueprint and source records. References identify the required kind of element. The same text may identify the corresponding L1 source concept in its separate source namespace. IDs are authored identities; after renaming files preserve the existing IDs rather than deriving fresh IDs from new paths.

A datum requires `name`, `description`, `type` and boolean `required`; an optional `cardinality` supplies a textual cardinality when useful. Supported type forms are:

```yaml
# Scalar or entity
kind: primitive
name: string
nullable: true
```

```yaml
kind: entity
ref: ENT-TASK
```

```yaml
kind: array
items:
  kind: entity
  ref: ENT-TASK
```

`type` references a named primitive refinement through `ref`. `map` declares a `values` type; map keys are text. Primitive names are `string`, `integer`, `number`, `boolean`, `bytes` and `null`. These are contract types, not runtime values in this document. `bytes` does not authorize executable YAML binary tags. Operational inputs/outputs stay distinct from `technical_parameters` and native signatures in source records.

Requiredness and nullability differ: required means that the argument/field is part of the contract; nullable allows an explicit absent value. The actor context is an invocation input, not an untrusted business JSON payload. Tool objects and database resources belong to dependency/composition or technical-parameter descriptions.

## Source state and observed correspondence

`source.state: planned` records intended structure before code exists and requires `sha256: null`. `observed` records a source observation; a current code-correspondence claim requires matching bytes and a non-null SHA-256. Neither state says that tests ran. A `designed` blueprint may contain planned sources; a `reconstructed` blueprint records intentional reconstruction from an observed realization; `mixed` requires the decisions to explain the split. Pending issues are explicit `open_issue` decisions, draft status or limitations, not invented observation states.

Each source unit identifies `code_name`, `kind`, `role`, `model_refs`, description, attributes and operations. `class`, `struct`, `function` and `module` describe physical units. Their role may be use case, entity, value object, tool, boundary, composition, test or support. Functions associated with a C/Go struct can be documented in that unit; Python symbol inspection only supports the Python forms it declares.

An operation records its semantic input/output contract and behavior; technical operations may describe injected collaborators separately. A source dependency's `from_unit` must identify a local unit; its textual `target` describes an import, call or resource observation, and is not a universal cross-language import resolver. The logical ADPM dependency graph separately resolves typed element IDs.

## Source catalogue and traceability

`source_l1` identifies the model, revision, artifact, hash and selected cases. `catalog` is an authored Minerva list: each entry contains `ref`, `kind`, `statement` and, where relevant, `case_refs`, `actor_refs` and an editorial `source_pointer`. Source identities occupy a separate namespace from L2 IDs. No Atlas reader is included; the L1 file is read only as bytes for hashing.

`traceability` contains `source_ref`, `target_refs`, `relation` (`preserves`, `refines` or `verifies`) and `rationale`. Declared in-scope requirements and criteria require links. `source_entity_id` resolves a declared entity; `origin_refs` resolves a typed origin or an explicit decision; actors are checked against the declared source-case set. These checks do not prove correct catalogue transcription. Separate review must compare source, catalogue and oracles.

Shared obligations preserve a canonical definition and reciprocal links between supporting checks and affected tests. [Atlas integration](../../integrations/atlas/mapping.md) explains the documentary mapping of native references without changing Atlas.

## Graph semantics

A graph's `owner_ref` identifies the behavior it describes. `entry` names one of its nodes. Edges have globally identified IDs, `from`, `to`, textual `condition` and `action`. `flow` nodes use start/action/decision/end/failure as appropriate; a finite flow declares at least one end or failure. A `state_machine` uses identifiable states and transitions; self-loops and cycles are valid. The validator checks references and reachability without evaluating conditions or proving termination. Empty edge action text means “no additional action”; a condition still has to state its meaning.

## Missing, null, empty and unknown values

Required fields cannot be omitted. `null` is accepted only in explicitly nullable slots such as absent observed hash, no source-entity mapping, no supporting-code reference or no execution observation. Empty arrays mean “none declared in this selected scope”, not “unknown”. Empty substantive strings are rejected; graph actions are a deliberate exception. A required optionality decision cannot be concealed in an empty collection: reviewed blueprints need nonempty source cases, program cases and directly linked tests. Unknown information belongs in a decision or limitation and often keeps the document a draft.

The loader accepts a deliberately restricted YAML scalar subset: lowercase `true`, `false`, `null`, JSON decimal integers/floats, strings, mappings and sequences. `yes`, `on`, dates and leading-zero numbers such as `012` remain strings. Quote revisions such as `'1'`. Explicit tags, anchors, aliases, duplicate/non-string mapping keys, non-finite numeric results and documents over 8 MiB are refused. Comments are editorial and are not model content; the tool does not promise formatting-preserving round trips.

## Validation workflow

```bash
# From the edition directory
python validator/minerva_validate.py examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/minimal --json
python tests/fixtures/counterexamples/check.py
```

First validate structure. Then inspect source links, case/test cardinality, criterion coverage, typed references, ownership and graph checks. Review the semantics and open issues. Only request `--verify-code` against a supplied realization; inspect its hashes and symbol correspondence. Execute application tests separately and record genuine results with the evaluated revision and environment. This profile does not write or approve code, perform a layer derivation, or turn a source inspection into an execution report.
