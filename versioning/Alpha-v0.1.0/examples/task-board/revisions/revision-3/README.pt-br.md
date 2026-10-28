# Task board — create, complete, and list

Este exemplo preserva os casos e contratos de `DOC-TASK-BOARD`, revisão `3`, do Atlas Stable-v1.0.0. A elaboração do L2 foi editorial e assistida por IA. A aprovação do responsável permanece pendente.

[Atlas JSON](docs/L1_AtlasSpecifications/example.atlas.json) · [Minerva YAML](docs/L2_MinervaBlueprints/blueprint.yaml) · [Proveniência](provenance.json) · [Rastreabilidade](traceability.pt-br.md)

| Caso | Teste comportamental | Critérios |
| --- | --- | --- |
| UC-TASK-CREATE | BT-TASK-CREATE | 5 |
| UC-TASK-COMPLETE | BT-TASK-COMPLETE | 7 |
| UC-TASK-LIST | BT-TASK-LIST | 4 |

Todos os cenários estão planejados. A ausência de código e de execuções é intencional: L2 pode ser elaborado antes de L3. Os canais ilustrativos da fonte continuam propostas; seus desenhos e recursos foram preservados quando presentes.

```bash
python validator/minerva_validate.py examples/task-board/revisions/revision-3/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/task-board/revisions/revision-3 --json
```

Execute a partir da edição. O resultado verifica declarações Minerva e hashes, não interpreta Atlas nem executa os cenários.
