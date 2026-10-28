# Migration to Minerva Blueprints Alpha-v0.1.0

[Português](MIGRATION.pt-br.md) · [Manual](../README.md) · [Coverage](REQUIREMENTS.md)

This edition extracts and revises **Vulcan Architecture Alpha-v0.1.0-Alkimim** into two Olympus models: Minerva Blueprints (L2) and Vulcan Ecosystem (L3). The original archive remains historical input. It is not rewritten, and its old execution results are not relabeled as new runs. See [source baselines](source-baselines.json).

The [machine-readable mapping](requirements/migration.json) retains all 40 former rule IDs, their destination requirements and original Portuguese rationale. The [full correspondence table](MIGRATION.pt-br.md#correspondência-das-40-regras-anteriores) preserves the original wording. The catalog records the earlier requirements exercise, including its original proposal statuses; the delivery coverage separately records adoption for this Alpha, implementation and evidence. Preparation and technical review were AI-assisted. Project-owner approval is not asserted.

## Changes of responsibility

| Former artifact family | Destination and treatment |
| --- | --- |
| Per-file YAML record | L2: `docs/L2_MinervaBlueprints/apps/<App>/<path>/<File.ext>.yaml`, preserving extensions and multiple legacy units. |
| ADPM and ADVS | Minerva L2 blueprint, with stable identities, contracts and verification specification. |
| Source cases and acceptance criteria | A dedicated Atlas instance explicitly identified as didactic reconstruction. |
| Manifest merging contracts, organization and channels | Split by responsibility: L2 contracts, L3 realization and identified L4 interaction. |
| Inventory, composition and execution | `docs/L3_Vulcan/`, referencing canonical L2 definitions. |
| Supporting documentation | `docs/Shared/`, without introducing an OAL layer. |
| Shared root runner and validator | Edition-local tools; Minerva representation validation and Vulcan structural inspection remain distinct. |

`apps/` and a root startup mechanism remain required in an instantiated Vulcan ecosystem. `docs/` and its layer folders are recommended; a declared alternative is accepted when the required information and references remain recoverable. Partial adoption does not require empty folders.

## Example compatibility

The demonstration uses `ATLAS-VULCAN-TASKBOARD`, revision `1`. Its contract retains application-generated identities, trimmed titles, boolean idempotent completion and insertion-order listing. It does not add optimistic task revisions or caller-selected creation identities. The separately published Atlas TaskBoard has a different contract and is not claimed as equivalent. A storage exception does not establish absence of effects; ambiguous write failures and distributed protocols were not simulated in this Alpha.

Model edition (`Alpha-v0.1.0`), instance revision (`1`), Minerva YAML profile version (`0.1.0`) and Python tool version (`0.1.0a0`) are independent identifiers. Moving a file updates bindings while retaining logical IDs whose meaning did not change. Changing the contract requires impact review across L1/L2/L3/L4 and its checks before updating evidence.

No automatic migrator for arbitrary applications is supplied. The deliverable provides the models, formats, procedures, examples and explicit correspondence for review.
