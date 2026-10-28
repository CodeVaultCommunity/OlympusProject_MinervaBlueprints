# OAL L2 correspondence

English · [Português brasileiro](OAL-ALIGNMENT.pt-br.md) · [Conformance](../README.md#conformance)

The authoritative basis is the [frozen OAL Stable-v1.0.0 text](../verification/sources/oal/README.md.txt), whose upstream commit and content hashes are in [source-baselines.json](../verification/source-baselines.json). This mapping paraphrases the responsibilities and states what this candidate model establishes. It is an inspectable conformance argument, not approval by OAL maintainers or an automated proof.

## ADMV as one L2

Minerva defines one program-and-verification instance with two distinguishable components. The schema requires both groups; reviewed instances require a nonempty selected source scope. Source records alone return `source_record_only`. A draft returns inconclusive for full consistency. This establishes a way to express the integrated L2; semantic coverage still requires review of the particular instance.

## ADPM subjects

| OAL ADPM subject | Minerva rules and constructions | Automated support / remaining review |
| --- | --- | --- |
| 1. Responsibilities | MIN-004–008; cases, entities, tools and source bindings | Typed references and independent IDs; reviewers assess faithful L3 mapping |
| 2. Cases | MIN-005, 012–013; behavior, permission and dependencies | Source-case correspondence; context-forwarding declaration; actual algorithm and authorization need review |
| 3. Entities | MIN-007; owned invariants, canonical construction and dependencies | Entity-to-tool/case edges rejected; semantic rule distribution reviewed |
| 4. Tools and validation location | MIN-008–009; operation guarantees, ready-entity assumption, contextual conditions | Declared entity revalidation rejected; semantic equivalents cannot be detected automatically |
| 5. Composition | MIN-011; received collaborators, selection location, ownership | References checked; completeness and hidden lookup reviewed |
| 6. Persistence | MIN-010; capabilities, failures, guarantees and contextual conditions | Required textual contracts; concurrency/atomicity and unknown outcomes require evidence |
| 7. Authorization | MIN-012; context input, trust source, four denial categories, policy before effects | Declared inputs/actors/categories checked; trust and execution order reviewed/tested in realization |
| 8. Faithful representation | MIN-014–015, 024; semantic text, pseudocode, structured graphs | Schema/topology checks; recoverability and algorithm equivalence reviewed |
| 9. Optional domains | MIN-011; domains and reciprocal case links | References checked; no universal grouping or access grant inferred |
| 10. Lifetime | MIN-011; composition lifetime, scope and ownership | Referenced elements checked; adequate lifecycle remains a model decision |

## ADVS subjects

| OAL ADVS subject | Minerva rules and constructions | Automated support / remaining review |
| --- | --- | --- |
| 1. One behavioral test per UCS case | MIN-017; case/source-case link, selected baseline | Exactly one direct logical test per selected source case; test files do not determine cardinality |
| 2. Scenario/subtest contracts | MIN-018; preparation, context, action, expected results/effects, boundary/configuration | Required structure; meaningful oracle and sufficient preparation reviewed |
| 3. Permissions | MIN-020; allowed and denied contexts, optional explicit anonymous | Category presence checked; absence of protected effects requires real observation |
| 4. Failures and limits | MIN-021, 023; alternatives, failures, risks and referenced channel obligations | Declared criterion/channel links checked; full risk coverage is not inferred |
| 5. Trace and status | MIN-019, 022; criteria, shared support, realization references, executions | Ownership/coverage/reciprocity/evidence references checked; report truth and breadth reviewed |

## Adjacent layers and provenance

The [frozen Atlas model](../verification/sources/atlas/README.md.txt) describes an L1 model. Minerva consumes a pinned source artifact through an explicit adapter. It does not rewrite the source's needs, actors or acceptance criteria, translate every possible L1 model, or claim an OAL derivation process from a handwritten link.

Vulcan is an L3 organization/realization model. Source-record paths bind L2 meaning to L3 artifacts; they do not make every source record a complete program model. Implementation decisions and observed execution evidence remain attributable to their realization. Interaction decisions stay L4 even when their source document is stored beside L2/L3 documents in `docs/Shared/`.

The TaskBoard source in this edition is a separately identified, didactic reconstruction matching the companion demo. Its title normalization, application-assigned ID, insertion-order list, local persistence and idempotent completion are its own contracts. The different TaskBoard in the Atlas repository has other obligations. A shared product name is not an equivalence mapping.

## Boundary of the claim

A successful reference run establishes only the named supported checks in its declared configuration. It does not establish semantic sufficiency, complete L1 validation, correctness of program code, broad environmental behavior or certification. The [validation record](../verification/VALIDATION.md) records actual commands and limits. Pending project-owner review remains explicit in the edition and instance provenance.
