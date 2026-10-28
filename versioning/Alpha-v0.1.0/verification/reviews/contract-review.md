# Source and contract review

[Português](contract-review.pt-br.md) · [Detailed comparison](contract-review.json) · [Mapping](../../integrations/atlas/mapping.md)

This is an AI-assisted technical review of the official pinned Atlas examples and their authored Minerva models. Owner acceptance remains pending. The one-off comparison used for this review is outside the delivered product; no source reader or translation engine is included.

| Example | Cases / logical behavioral tests | Criteria | Planned scenarios |
| --- | --- | --- | --- |
| Minimal request register | 1 / 1 | 7 | 12 |
| Task board | 3 / 3 | 16 | 31 |
| Booking composition | 3 / 3 | 18 | 33 |
| TaskBoard revision 2 | 3 / 3 | 16 | 31 |
| TaskBoard revision 3 | 3 / 3 | 16 | 31 |

The main three examples have seven cases and 41 criteria. Revision examples are separate snapshots, not additional application cases. Every source JSON matches the pinned official checkout byte-for-byte; original resources and licenses remain with the minimal example. The comparison checked every catalogue locator and statement, case identities/objectives/flow/actors, criterion/test links, requirement mappings and graph IDs/endpoints. Artifact hashes and exact criterion mappings are in the JSON record. External Atlas validation is recorded in [checks](../evidence/checks.json).

## Semantic review

Minimal preserves the exact case-sensitive request code, integer quantity of at least one, code-before-quantity validation, duplicate refusal, authorization before protected work and unknown write outcomes. Its response-time obligation remains a synthetic, unexecuted teaching condition.

TaskBoard preserves caller-provided identifiers, exact titles with the source limit, open/completed status, revision zero at creation, conditional completion, refusal of repeated completion, board scope, atomic conflict protection and deterministic source ordering. A store failure is not an empty successful list. Revision 3 refines `AC-TASK-LIST-EMPTY` to expose authorized consistent emptiness and no state/revision changes; revision 2 retains its original source wording.

Composition preserves uppercase alphanumeric codes (1–12 characters), meaningful exact titles, insert with expected version zero, conditional replacement with a positive version and version increments. Cancellation calls lookup with the same trusted context; lookup still makes its own permission decision. Failed lookup does not reach save. An unknown write cannot establish no effect or justify an automatic retry.

Entity transition rules stay separate from invariant references used by construction/hydration. Planned checks distinguish allowed calls and absent, unresolved, unknown, insufficient, expired and explicitly anonymous contexts. Shared RNFs retain a canonical supporting check and reciprocal case/test links.

## Open issues and limits

The canonical response-time RNF referenced by cancellation still names 30 creation requests and the creation stimulus. The example preserves that exact procedure and records `DEC-QUALITY-SCOPE`. Cancellation-specific timing requires source clarification; it is not an inferred guarantee. Interaction timing needs an actual selected channel; direct-core timing alone does not establish visible response time.

Caller-context representation is an explicit L2 decision; no identity provider, storage mechanism or interaction channel is chosen. Graph projection preserves identities, topology and labels; remaining Atlas-specific metadata stays in the pinned source. Source assumptions and open issues retain their unresolved status.

All ADVS scenarios are plans and `executions` remains empty. This review does not demonstrate production authorization, persistence/concurrency behavior, response times, exhaustive scenario sufficiency, universal OAL conformity or stakeholder acceptance. Those require evaluation of the selected realization and responsible review.
