# Minerva Blueprints · Alpha-v0.1.0

English · [Português brasileiro](README.pt-br.md)

**Minerva Blueprints is the Olympus Project model for OAL L2: Analysis-Driven Modeling and Verification (ADMV).** A blueprint combines a program model (ADPM) and a verification specification (ADVS). It explains how the specified cases, entities and tool contracts collaborate, and how their obligations will be checked. It can be authored before source code exists.

Atlas Specifications supplies an L1 specification when that model is selected. Vulcan Ecosystem organizes the L3 realization when that model is selected. Minerva owns the semantic blueprints and the per-file YAML mirror. Neither YAML nor a particular code architecture is the abstract model. Concrete abstract base classes, interfaces and a future convenience library are optional realization choices.

This edition is self-contained. Keep this folder together to use its manuals, schema, validator, starter, examples and tests without another version or the repository root. The root provides the illustrated project introduction. English is the normative text; Portuguese is a corresponding translation. **MUST**, **MUST NOT**, **SHOULD** and **MAY** identify obligations, recommendations and options. This is an **alpha candidate prepared with AI assistance and awaiting project-owner review**, not a published stable standard or certification.

<a id="release-notes"></a>
## Release notes — Alpha-v0.1.0

This first Minerva edition extracts L2 responsibilities from the earlier Vulcan teaching package and makes ADPM/ADVS relationships explicit. It introduces independent logical identities, source and criterion links, versioned YAML, a read-only validator, planned-file records, a legacy multi-unit record and public counterexamples. The task-board instance is reconstructed from the companion Vulcan demo. It does **not** claim to implement the different TaskBoard published by Atlas.

The abstract model edition is `Alpha-v0.1.0`; the YAML profile is `0.1.0`; the Python package/tool version is `0.1.0a0`. The OAL reference is `Stable-v1.0.0`. The supplied L1 reader supports Atlas Specifications `Stable-v1.0.0` JSON. These identities describe different objects and need not have the same spelling.

Source baselines are pinned in [source-baselines.json](verification/source-baselines.json). [Requirements coverage](verification/REQUIREMENTS.md) records this delivery against the agreed catalogue. [Validation evidence](verification/VALIDATION.md) distinguishes actual checks from planned verification. Historical source packages are not rewritten by this edition.

## Contents

- [Quick start](#quick-start) · [Versions](#versions) · [Abstract model and reference rules](#reference-rules)
- [YAML representation](implementations/yaml/README.md) · [Examples](examples/README.md)
- [Conformance](#conformance) · [Verification](#verification) · [Versioning](#versioning)
- [OAL correspondence](references/OAL-ALIGNMENT.md) · [Composition and change review](references/REVIEW-EXAMPLES.md)

<a id="versions"></a>
## Versions

| Edition | Status | Rules | Verification | Conformance |
| --- | --- | --- | --- | --- |
| Alpha-v0.1.0 | First candidate; owner review pending | [Reference rules](#reference-rules) | [Guide](#verification) | [Scope](#conformance) |

<a id="quick-start"></a>
## Start a blueprint

Use **Python 3.11+**. Commands below run from this edition directory. No other checkout is needed.

```bash
python -m venv .venv
# POSIX: source .venv/bin/activate
# PowerShell: .venv\Scripts\Activate.ps1
python -m pip install .
python run_examples.py --all
python examples/counterexamples/check.py
python run_examples.py --test
```

Installing the package exposes `minerva-validate`; `python -m minerva_blueprints` and the edition-local launcher expose the same interface. Alternatively, install `requirements.txt` and use the launcher directly. Neither launcher selects another edition or installs dependencies automatically.

```bash
python validator/minerva_validate.py \
  examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml \
  --root examples/minimal --json
```

Copy [the starter](implementations/yaml/starter.minerva.yaml) into your ecosystem's chosen L2 directory. Give it a document identity, scope, source specification and responsible party. Select the source cases, model their contracts and collaborators, then define one logical behavioral test for each case and the necessary scenarios. Add source-file records as the realization is designed or observed. Change `document.status` from `draft` to `reviewed` only after the stated technical review, recording unresolved issues and the actual review authority. The label never grants stakeholder approval.

The starter is a deliberately incomplete draft. Schema-only checking returns success; full consistency checking returns **4 (inconclusive)**. This distinction prevents an empty shell from being advertised as complete L2.

```bash
python validator/minerva_validate.py implementations/yaml/starter.minerva.yaml --structure-only
```

The recommended ecosystem layout is `apps/`, plus `docs/L1_AtlasSpecifications/`, `docs/L2_MinervaBlueprints/`, `docs/L3_Vulcan/` and `docs/Shared/`. `docs/` at the root is a recommendation. An alternative documentary location is valid when its root and mapping are declared and its references remain resolvable. Minerva does not prescribe where executable applications must live for every L3 model.

<a id="reference-rules"></a>
<a id="abstract-model"></a>
## Abstract model and reference rules

The following rules define semantic obligations independently of YAML field spellings. The identifiers also map to the agreed requirements catalogue. The YAML guide supplies the representation mapping; the correspondence guide explains the OAL obligations. A complete claim applies to a declared scope, not automatically to every application in a repository.

### MIN-001 — Integrated program and verification model

A Minerva instance MUST distinguish its program model and verification specification and preserve their relationships in one L2 scope. ADPM alone, ADVS alone or a catalogue of source files alone MUST NOT be described as complete ADMV. Each coverage statement MUST identify which component, selected cases and obligations it covers.

### MIN-002 — Semantics before syntax

The model consists of identifiable cases, entities, tool capabilities, operations, rules, dependencies, decisions, behavioral tests, scenarios and evidence relationships. A representation MUST recover these roles and their invariants. YAML, Markdown descriptions and pictures are carriers of meaning, not additional OAL layers. A different representation requires an explicit mapping and preservation contract; this edition supplies only the YAML profile.

### MIN-003 — Identity, revision and baseline

A blueprint MUST identify itself, its content revision, model edition, selected OAL edition, scope, responsible party and versioned L1 source. A representation also identifies its profile version. Content revisions change authored meaning; model/profile versions change reusable contracts. Source identities and revisions MUST be resolvable. The supplied profile permits a source hash to strengthen the content pin.

### MIN-004 — Logical elements and source bindings

Logical identities MUST remain independent of file paths, symbols and physical grouping. Renaming a file updates its binding, not the identity of a responsibility that remains the same. A source record MAY describe several classes, structs, functions or a module; several source records MAY bind the same logical element. The one-class-per-file rule belongs to the optional Vulcan Architecture organization, not to Minerva's ability to document arbitrary applications.

### MIN-005 — Program cases

Every in-scope L1 case MUST map to exactly one program case. The program case MUST preserve the specified objective, conditions, decisions, results, effects and relevant failures, and identify its collaborators and delegated entity behavior. Added design choices MUST be distinguishable from inherited requirements. A convenience procedure without a source case cannot silently become an extra modeled use case.

### MIN-006 — Operational data and technical collaborators

Operation contracts MUST identify inputs and outputs by name, meaning, type, requiredness and applicable cardinality. Business data, invocation actor context and injected collaborators MUST remain distinguishable. The Vulcan integration uses primitives, entities and typed collections for operational data; a named scalar type refines a primitive. Tools, connection factories and runtimes are technical collaborators, not serialized business inputs. A native signature may document language details separately.

### MIN-007 — Canonical entity rules

Entities MUST identify their data, relationships, invariants, delegated behavior and dependencies. Each rule MUST have an owner and recoverable origin. Entities MUST NOT depend on cases or tools. Minerva allows either data-oriented entities or entities with explicitly delegated behavior; it does not prescribe one universal distribution of all domain behavior.

### MIN-008 — Tool capability contracts

A tool MUST declare operations, conditions, results, effects, guarantees and failures separately from the selected mechanism. Cases consume those contracts. Satisfying a tool contract MUST NOT require a particular superclass, interface keyword, dependency-injection container or library. A plain concrete object with the documented behavior is a valid realization choice.

### MIN-009 — Ready entities and contextual conditions

A tool receiving a ready entity MUST rely on its canonical internal validity and MUST NOT repeat the entity's invariant validation, including a renamed or automatically generated equivalent check. Hydration starts from raw records and MUST use canonical construction. A distinct contextual condition, such as persisted existence or atomic uniqueness, MUST identify its object, purpose and responsibility. Such conditions do not transfer case authorization to the tool.

### MIN-010 — Persistence guarantees

Where persistence is used, the contract MUST state reading and alteration capabilities, ownership, relevant transaction/concurrency guarantees and failures. A pre-query cannot replace an atomic guarantee required by the contract. When an operation may have taken effect despite a reported failure, the model MUST distinguish an unknown outcome from established absence of effect. The demo promises local durable success and propagation of failures; it does not promise distributed recovery or classify every possible mid-commit outcome.

### MIN-011 — Dependencies and composition

The model MUST show what cases and tools receive, where realizations are selected and how they are composed. Required dependencies MUST NOT disappear into undocumented global lookup. Chosen domains, lifetimes and ownership MUST be stated where relevant. A domain groups responsibilities; it does not itself grant access. Minerva does not require a folder layout or singleton lifetime.

### MIN-012 — Case authorization

Each case MUST receive an explicit actor context with a declared trust source and decide permission before protected effects. Missing, unresolved, unknown and insufficient contexts MUST be denied. Authenticated identity and explicit anonymous participation are separate contract decisions. A caller-provided JSON field is not trusted simply because its shape matches an entity. Authorization MUST remain effective on direct core calls.

### MIN-013 — Case composition

A call to another case MUST declare the dependency, forwarded actor context, consumed contract and result. The called case MUST apply its own policy. Delegation or acting on behalf of another participant requires an explicit rule; an internal call adds no permission. The [composition example](references/REVIEW-EXAMPLES.md#case-composition) demonstrates two policies without changing the TaskBoard's source scope or inventing a fourth business case.

### MIN-014 — Recoverable behavior

Semantic prose or structured pseudocode MUST make sequence, decisions, failures, results and effects recoverable. A diagram MAY complement that description. A bare method signature or a generic box labelled “process” is insufficient to recover the behavior. The chosen level of detail SHOULD explain the contract without reproducing incidental implementation syntax.

### MIN-015 — Identified graphs

A graph MUST identify its owner, kind, entry, nodes and transitions, including conditions and actions. A flow represents control passage; an end or failure node identifies a terminal result. A state machine represents a state and permitted transitions, including legitimate self-loops. A graph inherited from an L1 specification keeps its L1 origin; storing it as YAML does not reclassify the decision as L2.

### MIN-016 — Added decisions, observations and open issues

The model MUST distinguish inherited obligations, decisions, assumptions, open issues and code observations, retaining source and review status. An observed source change MUST NOT overwrite intended semantics automatically. Review MUST identify affected cases, tool/entity contracts, scenarios and bindings before approving a revision. [Change review](references/REVIEW-EXAMPLES.md#change-impact) and the drift counterexample preserve intended and observed content together.

### MIN-017 — One directly linked behavioral test

Each selected UCS case MUST have exactly one logical behavioral test directly linked to that case. A behavioral test MAY contain many scenarios and consume many supporting checks. Test functions, files and framework fixtures are realizations; their number does not redefine the logical case/test correspondence. A shared check MUST NOT manufacture another directly linked test for an existing case.

### MIN-018 — Verification scenario contracts

Each scenario or supporting check MUST state preparation and preconditions, action, expected result and effects, observed boundary and relevant configuration. Case scenarios MUST state actor context, including deliberate absence. A condition marked not applicable MUST retain its rationale; it does not contribute applicable coverage. The expected behavior is an oracle to review, not an observed execution result.

### MIN-019 — Acceptance-criterion traceability

Every selected criterion MUST link to its case's behavioral test and the applicable scenarios or supporting checks that cover it. A shared integration criterion MUST retain one canonical statement and identify every affected case and their tests. No extra case is invented for the shared criterion. The supplied Atlas reader supports an explicitly documented extension for shared criteria; it does not infer shared meaning from similar text.

### MIN-020 — Permission and absence of prohibited effects

ADVS MUST specify allowed and denied invocation scenarios for each case, including the four denial categories and explicitly anonymous participation when permitted. The oracle MUST observe the absence of protected domain or storage effects before valid authorization, rather than checking only an error string. The reference validator checks declared categories and links; the reviewer checks whether the scenarios actually establish the policy.

### MIN-021 — Relevant alternatives, failures and limits

The verification plan MUST cover the alternatives, failures and boundaries necessary for its claimed contract, including needed entity and tool guarantees. Relevant unverified conditions MUST be visible and prevent an unqualified claim of complete coverage. Declared criterion links alone do not prove that scenarios are sufficient. Risks beyond the demo include production authentication, distributed recovery and exhaustive storage failure behavior.

### MIN-022 — Plan, realization and observed evidence

A planned test, its executable or procedural realization and an execution observation MUST remain distinguishable. An observed result MUST identify the evaluated implementation revision, environment, time, checks and evidence report, with limitations. A source file or observed symbol is not evidence that a test ran. Blueprint examples contain no fabricated successful executions; validation reports concern the documentation and the requested checks.

### MIN-023 — Referenced interaction obligations

When a selected L4 interaction introduces observable obligations, ADVS MUST reference their source and specify relevant scenarios. Channel choice, route/CLI syntax and representation remain L4 responsibilities; externally required constraints retain their L1 origin. The full example links HTTP and CLI obligations in `docs/Shared/interaction.md` without making those channels mandatory for Minerva.

### MIN-024 — Versioned YAML mirror in L2

The YAML profile MUST provide one source record per file in its declared mirror scope, preserving subdirectories and the original extension before `.yaml`. In the recommended layout, `apps/TaskBoard/entities/Entity_Task.py` maps to `docs/L2_MinervaBlueprints/apps/TaskBoard/entities/Entity_Task.py.yaml`. `Task.py` and `Task.go` remain distinct. Each record carries purpose, units and members, semantic description, inputs/outputs and dependencies directly or through logical references. Model intention, observed bytes and pending questions MUST remain distinguishable.

### MIN-025 — Roots, references and packaging

A package MUST declare the documentary root, source-record list, selected coverage and exclusions. All relative paths resolve against the explicitly supplied ecosystem root, not a changing process working directory. Moving the entire package MUST preserve relationships. Planned source records MAY exist before their code, with no observed hash. Claiming current realized-source correspondence requires a current code inspection over the declared scope; a model-only check cannot establish it.

### MIN-026 — Predictable data-only reading

The supplied reader MUST treat YAML as data. It rejects duplicate/non-string mapping keys, anchors, aliases and explicit tags, including executable tags. It fixes scalar interpretation, rejects non-finite numeric values and imposes an 8 MiB document limit. Text that looks like a command remains text. The reader MUST NOT import application modules or execute source files, YAML fields or tests while validating a blueprint.

### MIN-027 — Structural and consistency validation

The reference validator MUST check its supported schema, declared IDs, typed references, allowed relationships, selected case/test cardinality and criterion links. Diagnostics MUST distinguish that finite check from semantic review. A schema-valid source record alone does not establish ADMV. A reviewed empty model cannot claim coverage. Full sufficiency, algorithm equivalence and behavioral correctness remain outside automated proof in this edition.

### MIN-028 — Graph validation

For supported graphs the validator MUST check owners, node/edge references, entry and reachability, plus a terminal declaration for finite flows. It MUST permit legitimate cycles, such as idempotent completion. Passing these checks does not prove termination or the correctness of edge conditions. A derived diagram SHOULD identify its authoritative graph and edition; an illustrative overview is not a replacement for the graph contract.

### MIN-029 — Reviewable diagnostics

Diagnostics MUST contain code, severity, document, element and reason. Text and JSON output expose the same problem. Success, invalid input, unsupported profile, operational error and inconclusive assessment MUST have distinguishable process results. Automation MUST inspect the requested validation level and scope in addition to the exit code.

### MIN-030 — Examples and counterexamples

This edition MUST include a populated ADPM/ADVS instance, a minimum selected scope, a legacy multi-unit binding, a planned-source example and reproducible counterexamples. Expected outcomes MUST be stated separately from actual test evidence. Examples are teaching artifacts with declared provenance; successful validation does not approve the model on behalf of the project owner.

<a id="conformance"></a>
## Conformance and scope

The model claims to establish the **subjects of OAL L2 ADPM and ADVS**. [OAL correspondence](references/OAL-ALIGNMENT.md) maps all ten ADPM and five ADVS subjects. It does not claim to implement OAL's other layers or a general derivation engine. Atlas and Vulcan are compatible selected companions when their actual source and realization contracts agree; sharing an Olympus name does not prove compatibility.

A representation conformance claim identifies the model/profile editions and preserves all required content in its declared scope. An instance claim also identifies its source baseline, selected cases, decisions, gaps and review evidence. A source-only record is a binding excerpt. `draft` is incomplete. `reviewed` means the declared technical review was performed; the responsible party and limitations must say by whom, and whether stakeholder approval remains pending.

The validator returns `layer_coverage: declared_adpm_and_advs` for a reviewed blueprint whose two components were inspected. This means both components were supplied, **not** that the plan is sufficient or the realization conforms. A criterion-linked scenario can still have a wrong oracle. A matching hash can still describe a buggy program. Human semantic review and implementation evidence are required for broader claims.

<a id="verification"></a>
## Verification

```bash
python run_examples.py --all
python examples/counterexamples/check.py --json
python run_examples.py --test
python validator/minerva_validate.py examples/planned/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/planned --json
```

`--structure-only` reads one document and validates its representation; it does not resolve L1 or companion records. Normal mode resolves declared records and checks supported consistency. `--verify-code` additionally checks source presence/hashes, Python top-level units and methods, named supporting-test symbols and declared file coverage. It never executes the application or tests.

The complete Minerva example includes observed records of the companion Vulcan sources **without distributing those application sources here**. Its default model validation is self-contained. Requesting `--verify-code` against that Minerva-only directory returns inconclusive code availability. Run that check against the companion ecosystem after copying the same L2 records, or place the explicitly corresponding realization at the declared paths. Do not remove the option and then describe the result as code correspondence.

| Exit | Meaning | Example |
| --- | --- | --- |
| `0` | Requested checks passed | Valid model; or valid schema-only draft |
| `1` | Invalid supported document | Missing test, duplicate ID, broken graph, source drift |
| `2` | Unsupported model/profile/adapter | YAML profile `2.0.0`; also CLI usage errors |
| `3` | Operational failure | Unreadable file or missing runtime dependency |
| `4` | Inconclusive requested assessment | Draft consistency; source unavailable for code inspection |

The validator does not validate all Atlas semantics; use the pinned Atlas tool for full L1 validation. It does not parse arbitrary languages, prove transaction semantics, compare algorithms, validate production authentication or execute scenario oracles. Source checks support Python names and hashes; other languages receive hash checks with an explicit symbol-inspection limitation. See [recorded evidence and limitations](verification/VALIDATION.md).

<a id="versioning"></a>
## Versioning and change control

This edition is explicitly selected by path. The package does not resolve a mutable “latest” profile. Unsupported model/profile identities are refused. A content change increments the blueprint revision; a logical element retains its identity while its responsibility remains continuous. A model or representation change needs its own edition/profile version and migration statement. Renaming a file updates its mirrored path and observed snapshot, while preserving element identities.

Keep proposed intent, observed drift and review decisions together until the change is resolved. A new implementation observation does not silently revise L1 requirements. A change to a tool failure guarantee may affect cases, acceptance interpretation, scenarios, boundary representations and L3 tests. [Review examples](references/REVIEW-EXAMPLES.md) provide a concrete impact procedure. The frozen source baselines and release records make the basis of this alpha inspectable.

## Authorship and license

Minerva Blueprints belongs to the Olympus Project, authored by Douglas de Oliveira Alkimim. This candidate edition and examples were prepared with AI assistance; technical checks do not imply the author's approval or public publication. The edition is distributed under [MIT](LICENSE); reference source provenance and retained source licenses are recorded under `verification/sources/`.
