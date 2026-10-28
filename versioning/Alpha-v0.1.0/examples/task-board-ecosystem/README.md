# TaskBoard — complete didactic L2 instance

English · [Português brasileiro](README.pt-br.md)

The [blueprint](docs/L2_MinervaBlueprints/blueprint.yaml) models three cases from **ATLAS-VULCAN-TASKBOARD revision 1**, the explicitly reconstructed [Atlas source](docs/L1_AtlasSpecifications/task-board.atlas.json). It has three program cases, three directly linked behavioral tests, eleven acceptance criteria, four structured graphs and a fifteen-file L2 mirror. “Complete” here means populated ADPM and ADVS for the selected three-case teaching scope; documented risks and unexecuted scenarios do not become proven coverage.

| Source case | Program responsibility | Direct behavioral identity |
| --- | --- | --- |
| UC-TASK-001 | Authorize `tasks:create`; ask the tool to construct and retain a task from raw title | BT-TASK-001 |
| UC-TASK-002 | Authorize `tasks:read`; return tasks in insertion order or a distinct storage failure | BT-TASK-002 |
| UC-TASK-003 | Authorize `tasks:complete`; find, canonically complete and retain the task, preserving idempotence | BT-TASK-003 |

The tool generates a UUID4 hex identity and calls canonical entity construction before inserting. The title value is stripped and constrained to 1–120 characters. Completing an already completed entity preserves its state. The realization skips the redundant save; the L1 idempotence contract does not require every possible realization to skip a low-level update. Known, resolved actors need the case-specific permission before tool access. A browser-supplied permission field never supplies trusted context.

ADVS covers denied-context categories, positive behavior, invalid or absent data where relevant, and injected pre-connection storage failures. Supporting checks can serve several logical tests without creating additional directly linked test identities. [Interaction obligations](docs/Shared/interaction.md) retain their L4 origin and have HTTP/CLI scenarios. LegacyReports is represented by a multi-unit source record without invented Vulcan business cases.

## Validate the model

From this edition directory:

```bash
python validator/minerva_validate.py examples/task-board-ecosystem/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/task-board-ecosystem --json
```

Expected: exit 0 for supported model/record checks. This directory intentionally contains **no application source code**. Its observed source records are snapshots of the companion Vulcan Ecosystem Alpha-v0.1.0 realization, with matching path and hash. To inspect the current realization, run `--verify-code` against the companion ecosystem with these L2 records. Requesting that option against this Minerva-only directory returns exit 4 because source availability cannot be established. It is not a success claim about code.

The source specifications and blueprint are manually reconstructed teaching material prepared with AI assistance. They do not derive from, implement or replace the different TaskBoard example published in the Atlas repository. Project-owner review is pending. Observed test execution belongs in an execution report with its revision/environment; `advs.executions` is empty here because a reference to a test is not its result.
