# Examples

English · [Português brasileiro](README.pt-br.md) · [Edition guide](../README.md)

All commands below run from the **edition directory**, not the repository root. These artifacts are authored examples with explicit scope and provenance; they do not invent execution evidence or constitute approval by the project owner.

| Example | Scope | Ordinary result |
| --- | --- | --- |
| [Minimal](minimal/README.md) | Selected L1 list case, ADPM and one behavioral test; no source mapping required yet | Exit 0, declared model checks |
| [Task-board ecosystem](task-board-ecosystem/README.md) | Three cases, eleven criteria, ADPM/ADVS and fifteen observed source records | Exit 0 for model checks; code lives in companion Vulcan |
| [Planned](planned/README.md) | List-case blueprint and a planned source record before code exists | Exit 0; explicit code inspection is inconclusive |
| [Legacy](legacy/README.md) | Several procedural units in one file record | Exit 0, source record only; no complete ADMV claim |
| [Counterexamples](counterexamples/README.md) | Thirteen independently inspectable expected outcomes, including valid cycle and observed drift | Runner exits 0 only when every expectation matches |

```bash
python run_examples.py --list
python run_examples.py --all
python run_examples.py minimal --json
python examples/counterexamples/check.py --json
python run_examples.py --test
```

The [starter](../implementations/yaml/starter.minerva.yaml) is a structurally valid draft shell. `--all` checks its structure only; normal consistency validation returns exit 4. A source record alone does not provide the missing program/verification component. Keep source-observation state and test-execution state separate.
