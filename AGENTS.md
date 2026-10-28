# Agent guide for Minerva Blueprints

## Select the edition

Respect the requested edition. The current Alpha-v0.1.0 is unpublished and its in-place reorganization was explicitly authorized by the owner. Do not create another edition unless requested. Root READMEs introduce the project; the edition README is navigation. `versioning/Alpha-v0.1.0/specification/model.md` is normative and `model.pt-br.md` is its translation.

## Locate contracts

Read the selected model, YAML profile, `specification/conformance.md`, `integrations/atlas/mapping.md` and `verification/REQUIREMENTS.md` before implementation changes. Check `verification/source-baselines.json` for pinned OAL and Atlas inputs. Preserve specification, realization and observation as distinct objects.

Minerva includes no Atlas-specific reader or translation engine. Integration is documented; examples elaborate the official Atlas minimal, task-board and composition cases with their source identities and contracts. The source catalogue is authored Minerva data, checked for internal consistency; its fidelity to L1 requires review. Do not add retired implementations or backward-compatibility fixtures for unpublished drafts.

For adopting applications, root `docs/` is recommended, with `L1_AtlasSpecifications`, `L2_MinervaBlueprints`, `L3_Vulcan` and `Shared` for adopted materials. The per-file mirror belongs to L2. Libraries and abstract base classes remain optional.

## Maintain and verify

Keep English and Portuguese aligned, preserve source IDs and frozen upstream bytes, update links and use edition-local commands. Record added decisions and limits. Never equate a code observation or validator pass with stakeholder acceptance.

Run edition tests, examples and `tests/fixtures/counterexamples/check.py`; from the root run `scripts/check_repository.py` and `scripts/tests`. Inspect changed artwork. Keep environments/build products outside the delivery tree. Update observed evidence before generating the root inventory. Stage intended files, generate `CONTENT-SHA256.json` last, verify and commit locally. Follow `docs/releasing.md` for packaging. Final commit and ZIP digests belong in an external receipt. Local delivery does not authorize remote publication.
