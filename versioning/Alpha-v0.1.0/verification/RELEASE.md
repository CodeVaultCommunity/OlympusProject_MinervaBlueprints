# Local revision record · Alpha-v0.1.0

[Português](RELEASE.pt-br.md) · [Requirements](REQUIREMENTS.md) · [Validation](VALIDATION.md) · [Contract review](reviews/contract-review.md)

The existing unpublished Alpha-v0.1.0 was revised in place at the owner's request. No new edition, model version, profile version or tool version was created. Minerva delivers the L2 model, YAML representation, validator, documentation and authored official-source examples. Atlas integration is documentation; no Atlas reader or translation engine is delivered.

Specification, conformance rules and OAL correspondence are in `specification/`; the selected YAML profile is in `implementations/yaml/`; documentary mapping and compatibility are in `integrations/atlas/`. Main examples are `minimal`, `task-board` and `composition`, with TaskBoard revision 2/3 snapshots. Testing fixtures are under `tests/fixtures/`. Requirements, source snapshots, technical reviews and actual check outputs are separate inside `verification/`.

The [validation record](VALIDATION.md) reports 50 edition tests, 33 repository tests, 12 counterexample outcomes, source validation, isolated edition and wheel checks. Domain scenarios remain planned. The source review identifies the unresolved shared cancellation measurement boundary. Owner semantic acceptance and hosted CI execution are not asserted.

Finish documents and evidence before generating the root `CONTENT-SHA256.json`, then verify and commit locally as described in the [distribution procedure](../../../docs/releasing.md). The inventory is the sole active delivery inventory and excludes itself. Any final commit identifier or ZIP digest belongs outside the tree it identifies. Source baselines separately pin upstream bytes and do not replace the delivery inventory. This record does not claim remote publication or a GitHub release.
