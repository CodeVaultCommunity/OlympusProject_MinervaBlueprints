# Blueprint mínimo de escopo selecionado

[English](README.md) · Português brasileiro

Este exemplo seleciona somente **UC-TASK-002**, listar, da [fonte Atlas didática fixada](docs/L1_AtlasSpecifications/task-board.atlas.json). A origem mantém seus três casos; `source_l1.case_ids` explicita o recorte L2 de um caso. O [blueprint](docs/L2_MinervaBlueprints/blueprint.yaml) contém contratos, regras de entidades/ferramentas, autorização, um teste comportamental direto, cobertura de critérios, cenários permitidos/negados/vazio e falha de armazenamento. É um escopo reduzido, não realização completa de todos os casos da origem.

Nenhuma fonte de código é fornecida ou alegada pelo espelho declarado. Fichas não são pré-requisito para raciocinar antes da implementação. Verificações de apoio identificam realizações pretendidas separadamente dos resultados; não se alega execução aqui.

A partir da pasta da edição:

```bash
python validator/minerva_validate.py examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/minimal --json
```

Resultado esperado: saída 0, um caso, um teste comportamental direto e três critérios. Revise confiança do contexto, ordem de inserção, diferença entre armazenamento vazio confirmado e falha e ausência de escritas na listagem. Sucesso estrutural não prova essas alegações contra código.
