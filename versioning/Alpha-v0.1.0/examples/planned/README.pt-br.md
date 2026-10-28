# Fonte planejada antes da implementação

[English](README.md) · Português brasileiro

Este [blueprint](docs/L2_MinervaBlueprints/blueprint.yaml) seleciona o caso de listar do exemplo mínimo e o vincula a uma [ficha planejada](docs/L2_MinervaBlueprints/apps/TaskBoard/usecases/TaskManagement/UseCase_ListTasks.py.yaml). `source.state` é `planned`; `sha256` é nulo. Classe, operação, contexto e vínculo lógico pretendidos existem sem arquivo executável. Não se alega código ou execução.

A partir da pasta da edição:

```bash
python validator/minerva_validate.py examples/planned/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/planned --json
```

Esperado: saída 0 no modelo. Acrescentar `--verify-code` é intencionalmente inconclusivo (4): ficha planejada não estabelece correspondência com implementação ausente. Quando a fonte existir, revise a semântica, registre observação/hash reais e revise o documento. Não transforme intenção em evidência observada silenciosamente porque um nome de arquivo apareceu.
