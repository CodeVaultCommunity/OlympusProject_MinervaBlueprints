# Composição de reservas

Este exemplo preserva os casos e contratos de `ATLAS-EX-COMPOSITION`, revisão `2`, do Atlas Stable-v1.0.0. A elaboração do L2 foi editorial e assistida por IA. A aprovação do responsável permanece pendente.

[Atlas JSON](docs/L1_AtlasSpecifications/example.atlas.json) · [Minerva YAML](docs/L2_MinervaBlueprints/blueprint.yaml) · [Proveniência](provenance.json) · [Rastreabilidade](traceability.pt-br.md)

| Caso | Teste comportamental | Critérios |
| --- | --- | --- |
| UC-BOOKING-LOOKUP | BT-BOOKING-LOOKUP | 5 |
| UC-BOOKING-CREATE | BT-BOOKING-CREATE | 6 |
| UC-BOOKING-CANCEL | BT-BOOKING-CANCEL | 7 |

Todos os cenários estão planejados. A ausência de código e de execuções é intencional: L2 pode ser elaborado antes de L3. Os canais ilustrativos da fonte continuam propostas; seus desenhos e recursos foram preservados quando presentes.

```bash
python validator/minerva_validate.py examples/composition/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/composition --json
```

Execute a partir da edição. O resultado verifica declarações Minerva e hashes, não interpreta Atlas nem executa os cenários.
