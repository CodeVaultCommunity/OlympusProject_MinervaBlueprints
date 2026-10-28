# Atlas → Minerva: documentary mapping

[Português](mapping.pt-br.md) · [Compatibility](compatibility.json) · [Examples](../../examples/README.md)

This directory documents integration. It contains no reader, executable translator or transformation engine. The shipped examples are AI-assisted editorial derivations of the official Atlas sources pinned at commit `b5941830515d9968bb7f313301f1abe25fb6f8aa`.

| Atlas concept | Minerva location | Preservation duty |
| --- | --- | --- |
| Document identity/revision | `source_l1`, example `provenance.json` | Retain original identity, revision, commit, artifact and byte hash |
| Case | `adpm.cases[].source_case_id` | Exactly one case per selected L1 case; preserve objectives, inputs, outcomes and algorithm |
| Actor and case permission | `source_l1.catalog`, case `permission` | Catalogue records the case-specific permitted set; preserve trusted context and denial order |
| Entity, fields, validation | `adpm.entities`, rules and `origin_refs` | Preserve exact data, rule ownership and canonical construction |
| Tool and operation | `adpm.tools[].operations` | Preserve guarantees, distinct failures, atomicity and write uncertainty separately from mechanism |
| RF | Catalogue, case behavior, `traceability` | Preserve the obligation and its verification links |
| RNF and `reference_to` | Catalogue and one canonical supporting check | Preserve origin, applicability, metric, measurement boundary and affected cases |
| Acceptance criterion | Catalogue, behavioral test and scenarios | Preserve criterion identity and observable oracle |
| Case call | Dependencies with `context_forwarding` | Preserve principal, consumed result and called-case authorization |
| Graph | `adpm.graphs` with original identities | Preserve nodes, transitions and readable meaning; L1 remains the origin |
| Assumption/open issue | Document decisions and limitations | Retain unresolved status; do not manufacture stakeholder acceptance |
| Boundary illustration | Pinned L1 package | Retain as illustration; no channel implementation is selected by copying it |

The reviewed source catalogue is an authored index inside a Minerva blueprint. Entries use `ref` instead of `id` to keep source and L2 namespaces separate. `kind` types the reference; `case_refs` states criterion/requirement scope; `actor_refs` states the permitted set for a source case. `source_pointer` is an editorial locator, not an instruction executed by the validator. `traceability` names the L2 targets and whether a link preserves, refines or verifies a source element.

The validator reads only Minerva YAML plus opaque source bytes for hashing. It rejects undeclared entity origins, unresolved rule origins and actors outside a catalogue's source-case set. It cannot detect a false but internally consistent catalogue. Review compares the catalogue, contracts and scenarios against the pinned source; external Atlas validation checks the source using Atlas tooling. No claim of a deterministic translation engine is made.

## Case composition

Booking cancellation first checks its own permission, then calls lookup with the same trusted principal/context. Lookup checks its own permission. Cancellation-only permission does not permit lookup, and lookup denial stops before saving. The example includes a dedicated scenario for this boundary.

## Shared obligations

Atlas RNF references retain their own IDs in the catalogue. Creation and cancellation both link to `CHK-RNF-BOOKING-CREATE-RESPONSE`, preserving the canonical two-second, 30-request teaching condition. Task creation/listing share the retention check. These are planned obligations, not measured claims. Native source files remain unchanged; no `minerva_shared_criteria` extension is inserted.

## Graph mapping and design choices

Atlas result nodes map to Minerva end nodes; refusal nodes map to failure terminals; operation, validation and use-case call nodes map to actions. Original IDs and edge labels remain recoverable. Complete Atlas-specific graph metadata remains in the pinned source. Entity transition rules apply to the transition, not to the hydration of every existing entity. Caller context is an explicit L2 entity. Success data and named refusal/failure outcomes describe a contract without choosing a language exception/result mechanism.

## Change review

Compare source revisions before editing L2. Preserve stable case IDs, identify changed criteria/RFs/RNFs, update affected scenario oracles and trace links, and record remaining gaps. TaskBoard revision 3 refines `AC-TASK-LIST-EMPTY` to state authorized consistent emptiness and absence of state/revision changes. The paired examples preserve that delta without inventing a fourth case.

The source cancellation RNF references a canonical procedure that still names 30 creation requests and the creation stimulus. The example preserves this wording and records `DEC-QUALITY-SCOPE`: cancellation-specific timing needs source-owner clarification. No separate cancellation latency guarantee is inferred.
