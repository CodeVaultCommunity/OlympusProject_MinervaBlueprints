# TaskBoard — instância L2 didática completa

[English](README.md) · Português brasileiro

O [blueprint](docs/L2_MinervaBlueprints/blueprint.yaml) modela três casos de **ATLAS-VULCAN-TASKBOARD revisão 1**, a [fonte Atlas](docs/L1_AtlasSpecifications/task-board.atlas.json) explicitamente reconstruída. Possui três casos, três testes comportamentais diretamente vinculados, onze critérios, quatro grafos estruturados e espelho L2 de quinze arquivos. “Completa” significa ADPM e ADVS preenchidas para o recorte didático de três casos; riscos documentados e cenários não executados não se tornam cobertura provada.

| Caso de origem | Responsabilidade de programa | Identidade comportamental direta |
| --- | --- | --- |
| UC-TASK-001 | Autorizar `tasks:create`; solicitar à ferramenta construção e retenção a partir do título bruto | BT-TASK-001 |
| UC-TASK-002 | Autorizar `tasks:read`; devolver tarefas em ordem de inserção ou falha de armazenamento distinta | BT-TASK-002 |
| UC-TASK-003 | Autorizar `tasks:complete`; localizar, concluir canonicamente e reter, preservando idempotência | BT-TASK-003 |

A ferramenta gera identidade UUID4 hexadecimal e invoca construção canônica antes de inserir. O título é normalizado com remoção de espaços externos e limitado a 1–120 caracteres. Concluir novamente preserva o estado. A realização evita salvar outra vez; o contrato L1 de idempotência não exige que toda realização omita atualização de baixo nível. Atores conhecidos e resolvidos precisam da permissão específica antes do acesso à ferramenta. Um campo de permissões enviado pelo navegador não fornece contexto confiável.

A ADVS cobre categorias de recusa, comportamento positivo, dados inválidos/ausentes pertinentes e falhas injetadas antes da conexão. Verificações de apoio podem servir a vários testes lógicos sem criar identidades comportamentais diretas extras. As [obrigações de interação](docs/Shared/interaction.pt-br.md) preservam origem L4 e possuem cenários HTTP/CLI. LegacyReports é representado por ficha com múltiplas unidades, sem casos Vulcan inventados.

## Validar o modelo

A partir da pasta desta edição:

```bash
python validator/minerva_validate.py examples/task-board-ecosystem/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/task-board-ecosystem --json
```

Esperado: saída 0 nas verificações suportadas do modelo/fichas. Este diretório intencionalmente **não contém código da aplicação**. Suas fichas observadas são snapshots da realização Vulcan Ecosystem Alpha-v0.1.0 companheira, com caminho e hash correspondentes. Para inspecionar a realização atual, utilize `--verify-code` no ecossistema companheiro com estas fichas L2. Solicitar essa opção no diretório exclusivamente Minerva retorna 4 por não estabelecer disponibilidade das fontes. Não constitui sucesso sobre o código.

Especificação e blueprint são reconstruções didáticas manuais com auxílio de IA. Não derivam, realizam nem substituem o outro TaskBoard publicado pelo Atlas. A revisão do responsável está pendente. Execução observada deve estar em relatório com revisão/ambiente; `advs.executions` permanece vazio porque referência a teste não é resultado.
