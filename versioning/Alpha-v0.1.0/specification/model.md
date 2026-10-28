# Minerva Blueprints model · Alpha-v0.1.0

[Português brasileiro](model.pt-br.md) · [Edition entry](../README.md) · [Conformance](conformance.md)

This is the normative edition text. MUST, MUST NOT, SHOULD and MAY mark obligations, prohibitions, recommendations and options. Minerva establishes OAL L2 / ADMV, combining ADPM and ADVS. YAML is a representation; code organization and execution belong to the L3 realization. Libraries, interfaces and abstract base classes remain optional.

This Alpha is unpublished and was revised in place with explicit project-owner authorization. Model edition `Alpha-v0.1.0`, YAML profile `0.1.0` and tool `0.1.0a0` remain explicitly selected. Compatibility with earlier unpublished drafts is not promised. Pinned external source bytes are preserved.

The edition includes no Atlas-specific reader or translation engine. Examples were authored with AI assistance from identified official sources. Any future engine is independent. Authorization to edit does not replace semantic acceptance of the result.

<a id="reference-rules"></a>
## Reference rules
### MIN-001 — Integrated program and verification model

A Minerva instance MUST distinguish its program model and verification specification and preserve their relationships in one L2 scope. ADPM alone, ADVS alone or a catalogue of source files alone MUST NOT be described as complete ADMV. Each coverage statement MUST identify which component, selected cases and obligations it covers.

### MIN-002 — Semantics before syntax

The model consists of identifiable cases, entities, tool capabilities, operations, rules, dependencies, decisions, behavioral tests, scenarios and evidence relationships. A representation MUST recover these roles and their invariants. YAML, Markdown descriptions and pictures are carriers of meaning, not additional OAL layers. A different representation requires an explicit mapping and preservation contract; this edition supplies only the YAML profile.

### MIN-003 — Identity, revision and baseline

A blueprint MUST identify itself, its content revision, model edition, selected OAL edition, scope, responsible party and versioned L1 source. A representation also identifies its profile version. Reviewed YAML blueprints MUST pin the source artifact by SHA-256 and declare a source catalogue with identities, kinds, case ownership and permitted actors. The catalogue is authored Minerva content. Its fidelity to the source MUST be reviewed separately; the validator treats the L1 artifact as opaque bytes.

### MIN-004 — Logical elements and source bindings

Logical identities MUST remain independent of file paths, symbols and physical grouping. Renaming a file updates its binding, not the identity of a responsibility that remains the same. A source record MAY describe several classes, structs, functions or a module; several source records MAY bind the same logical element. The one-class-per-file rule belongs to the optional Vulcan Architecture organization, not to Minerva's ability to document arbitrary applications.

### MIN-005 — Program cases

Every in-scope L1 case MUST map to exactly one program case. The program case MUST preserve the specified objective, conditions, decisions, results, effects and relevant failures, and identify its collaborators and delegated entity behavior. Added design choices MUST be distinguishable from inherited requirements. A convenience procedure without a source case cannot silently become an extra modeled use case.

### MIN-006 — Operational data and technical collaborators

Operation contracts MUST identify inputs and outputs by name, meaning, type, requiredness and applicable cardinality. Business data, invocation actor context and injected collaborators MUST remain distinguishable. The YAML profile uses primitives, entities and typed collections for operational data; a named scalar type refines a primitive. Tools, connection factories and runtimes are technical collaborators, not serialized business inputs. A native signature may document language details separately.

### MIN-007 — Canonical entity rules

Entities MUST identify their data, relationships, invariants, delegated behavior and dependencies. Each rule MUST have an owner and recoverable origin. Entities MUST NOT depend on cases or tools. Minerva allows either data-oriented entities or entities with explicitly delegated behavior; it does not prescribe one universal distribution of all domain behavior.

### MIN-008 — Tool capability contracts

A tool MUST declare operations, conditions, results, effects, guarantees and failures separately from the selected mechanism. Cases consume those contracts. Satisfying a tool contract MUST NOT require a particular superclass, interface keyword, dependency-injection container or library. A plain concrete object with the documented behavior is a valid realization choice.

### MIN-009 — Ready entities and contextual conditions

A tool receiving a ready entity MUST rely on its canonical internal validity and MUST NOT repeat the entity's invariant validation, including a renamed or automatically generated equivalent check. Hydration starts from raw records and MUST use canonical construction. A distinct contextual condition, such as persisted existence or atomic uniqueness, MUST identify its object, purpose and responsibility. Such conditions do not transfer case authorization to the tool.

### MIN-010 — Persistence guarantees

Where persistence is used, the contract MUST state reading and alteration capabilities, data ownership, transaction/concurrency guarantees and failures. A pre-query cannot replace an atomic guarantee required by the contract. When an operation may have taken effect despite a reported failure, the model MUST distinguish an unknown outcome from established absence of effect. The Atlas-aligned examples specify these distinctions and planned checks; no persistence implementation or distributed recovery execution is delivered.

### MIN-011 — Dependencies and composition

The model MUST show what cases and tools receive, where realizations are selected and how they are composed. Required dependencies MUST NOT disappear into undocumented global lookup. Chosen domains, lifetimes and ownership MUST be stated where relevant. A domain groups responsibilities; it does not itself grant access. Minerva does not require a folder layout or singleton lifetime.

### MIN-012 — Case authorization

Each case MUST receive an explicit actor context with a declared trust source and decide permission before protected effects. Missing, unresolved, unknown and insufficient contexts MUST be denied. Authenticated identity and explicit anonymous participation are separate contract decisions. A caller-provided JSON field is not trusted simply because its shape matches an entity. Authorization MUST remain effective on direct core calls.

### MIN-013 — Case composition

A call to another case MUST declare the dependency, forwarded actor context, consumed contract and result. The called case MUST apply its own policy. Delegation or acting on behalf of another participant requires an explicit rule; an internal call adds no permission. The [composition example](../examples/composition/README.md) preserves cancellation calling lookup, both permission decisions and the called case's refusal/failure outcomes.

### MIN-014 — Recoverable behavior

Semantic prose or structured pseudocode MUST make sequence, decisions, failures, results and effects recoverable. A diagram MAY complement that description. A bare method signature or a generic box labelled “process” is insufficient to recover the behavior. The chosen level of detail SHOULD explain the contract without reproducing incidental implementation syntax.

### MIN-015 — Identified graphs

A graph MUST identify its owner, kind, entry, nodes and transitions, including conditions and actions. A flow represents control passage; an end or failure node identifies a terminal result. A state machine represents a state and permitted transitions, including legitimate self-loops. A graph inherited from an L1 specification keeps its L1 origin; storing it as YAML does not reclassify the decision as L2.

### MIN-016 — Added decisions, observations and open issues

The model MUST distinguish inherited obligations, added decisions, assumptions, open issues and code observations, retaining source and review status. An observed source change MUST NOT overwrite intended semantics automatically. Review MUST identify affected cases, tool/entity contracts, scenarios and bindings before approving a revision. The [TaskBoard revisions](../examples/task-board/revisions/README.md) retain case identities while making the criterion refinement and its verification impact explicit.

### MIN-017 — One directly linked behavioral test

Each selected UCS case MUST have exactly one logical behavioral test directly linked to that case. A behavioral test MAY contain many scenarios and consume many supporting checks. Test functions, files and framework fixtures are realizations; their number does not redefine the logical case/test correspondence. A shared check MUST NOT manufacture another directly linked test for an existing case.

### MIN-018 — Verification scenario contracts

Each scenario or supporting check MUST state preparation and preconditions, action, expected result and effects, observed boundary and relevant configuration. Case scenarios MUST state actor context, including deliberate absence. A condition marked not applicable MUST retain its rationale; it does not contribute applicable coverage. The expected behavior is an oracle to review, not an observed execution result.

### MIN-019 — Acceptance-criterion traceability

Every selected criterion MUST link to its case's behavioral test and applicable scenarios or supporting checks. Shared obligations MUST retain one canonical definition and identify affected cases and their tests; no extra case is invented. Source obligations and L2 elements MUST have explicit traceability links. The YAML validator resolves the declared catalogue and mappings. Source completeness, meaning and shared-obligation equivalence require a documented review; no Atlas-specific extension or source reader is required.

### MIN-020 — Permission and absence of prohibited effects

ADVS MUST specify allowed and denied invocation scenarios for each case, including the four denial categories and explicitly anonymous participation when permitted. The oracle MUST observe the absence of protected domain or storage effects before valid authorization, rather than checking only an error string. The reference validator checks declared categories and links; the reviewer checks whether the scenarios actually establish the policy.

### MIN-021 — Relevant alternatives, failures and limits

The verification plan MUST cover the alternatives, failures and boundaries necessary for its claimed contract, including needed entity and tool guarantees. Relevant unverified conditions MUST be visible and prevent an unqualified claim of complete coverage. Declared criterion links alone do not prove that scenarios are sufficient. Risks requiring realization evidence include production authentication, distributed recovery and exhaustive storage failure behavior.

### MIN-022 — Plan, realization and observed evidence

A planned test, its executable or procedural realization and an execution observation MUST remain distinguishable. An observed result MUST identify the evaluated implementation revision, environment, time, checks and evidence report, with limitations. A source file or observed symbol is not evidence that a test ran. Blueprint examples contain no fabricated successful executions; validation reports concern the documentation and the requested checks.

### MIN-023 — Referenced interaction obligations

When a selected L4 interaction introduces observable obligations, ADVS MUST reference their origin and specify relevant scenarios. Channel choice, route/CLI syntax and representation remain L4 responsibilities; externally required constraints retain L1 origin. Source illustrations do not select an L4 implementation. The examples preserve interaction-scoped quality obligations as planned checks and leave concrete channels unselected.

### MIN-024 — Versioned YAML mirror in L2

The YAML profile MUST provide one source record per file in its declared mirror scope, preserving subdirectories and the original extension before `.yaml`. In the recommended layout, `apps/TaskBoard/entities/Entity_Task.py` maps to `docs/L2_MinervaBlueprints/apps/TaskBoard/entities/Entity_Task.py.yaml`. `Task.py` and `Task.go` remain distinct. Each record carries purpose, units and members, semantic description, inputs/outputs and dependencies directly or through logical references. Model intention, observed bytes and pending questions MUST remain distinguishable.

### MIN-025 — Roots, references and packaging

A package MUST declare the documentary root, source-record list, selected coverage and exclusions. All relative paths resolve against the explicitly supplied ecosystem root, not a changing process working directory. Moving the entire package MUST preserve relationships. Planned source records MAY exist before their code, with no observed hash. Claiming current realized-source correspondence requires a current code inspection over the declared scope; a model-only check cannot establish it.

### MIN-026 — Predictable data-only reading

The supplied reader MUST treat YAML as data. It rejects duplicate/non-string mapping keys, anchors, aliases and explicit tags, including executable tags. It fixes scalar interpretation, rejects non-finite numeric values and imposes an 8 MiB document limit. Text that looks like a command remains text. The reader MUST NOT import application modules or execute source files, YAML fields or tests while validating a blueprint.

### MIN-027 — Structural and consistency validation

The reference validator MUST check the supported Minerva schema, IDs, typed references, allowed relationships, selected case/test cardinality, declared source origins and criterion links. It MUST reject an entity linked to an undeclared source entity, an unresolved rule origin and a case actor outside the source-case actor set declared in the catalogue. This checks Minerva consistency, not the truth of that catalogue against L1. Diagnostics MUST distinguish these checks from semantic review. A reviewed empty model cannot claim coverage; schema validity does not prove behavioral preservation.

### MIN-028 — Graph validation

For supported graphs the validator MUST check owners, node/edge references, entry and reachability, plus a terminal declaration for finite flows. It MUST permit legitimate cycles, including state-machine self-loops. Passing these checks does not prove termination or the correctness of edge conditions. A derived diagram SHOULD identify its authoritative graph and edition; an illustrative overview is not a replacement for the graph contract.

### MIN-029 — Reviewable diagnostics

Diagnostics MUST contain code, severity, document, element and reason. Text and JSON output expose the same problem. Success, invalid input, unsupported profile, operational error and inconclusive assessment MUST have distinguishable process results. Automation MUST inspect the requested validation level and scope in addition to the exit code.

### MIN-030 — Examples and counterexamples

This edition MUST include L2 versions of the pinned Atlas minimal, task-board and composition examples, including the identified TaskBoard revisions. Planned-source fixtures and reproducible counterexamples exercise the current tooling. Expected outcomes MUST remain separate from actual execution evidence. Example preparation and technical review do not assert project-owner acceptance.
