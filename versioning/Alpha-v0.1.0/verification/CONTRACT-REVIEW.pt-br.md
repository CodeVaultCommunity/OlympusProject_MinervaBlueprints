# Revisão do contrato integrado — Alpha-v0.1.0

[English](CONTRACT-REVIEW.md) · [JSON](contract-review.json) · [Release](RELEASE.md) · [Atlas](../examples/task-board-ecosystem/docs/L1_AtlasSpecifications/task-board.atlas.json) · [Minerva](../examples/task-board-ecosystem/docs/L2_MinervaBlueprints/blueprint.yaml)

A revisão liga os três casos e onze critérios da instância **ATLAS-VULCAN-TASKBOARD, revisão 1**, ao blueprint **MINERVA-TASKBOARD, revisão 1**, e à realização Python. A origem é didática e reconstruída; ela não é o TaskBoard publicado separadamente no Atlas. A preparação e a revisão técnica foram assistidas por IA, com uma revisão independente por outro agente e integração posterior. Não se afirma aprovação do responsável pelo projeto.

## Rastreabilidade por critério

| Critério L1 | Caso L1/L2 | ADVS | Cenários | Teste direto na realização Vulcan |
| --- | --- | --- | --- | --- |
| AC-TASK-001-AUTH | UC-TASK-001 | BT-TASK-001 | SC-TASK-001-AUTH-ALLOWED, SC-TASK-001-AUTH-ABSENT, SC-TASK-001-AUTH-UNRESOLVED, SC-TASK-001-AUTH-UNKNOWN, SC-TASK-001-AUTH-INSUFFICIENT | `Test_TaskCases.testCreateTask` |
| AC-TASK-001-SUCCESS | UC-TASK-001 | BT-TASK-001 | SC-TASK-001-SUCCESS | `Test_TaskCases.testCreateTask` |
| AC-TASK-001-INVALID | UC-TASK-001 | BT-TASK-001 | SC-TASK-001-INVALID | `Test_TaskCases.testCreateTask` |
| AC-TASK-001-PERSISTENCE | UC-TASK-001 | BT-TASK-001 | SC-TASK-001-PERSISTENCE | `Test_TaskCases.testCreateTask` |
| AC-TASK-002-AUTH | UC-TASK-002 | BT-TASK-002 | SC-TASK-002-AUTH-ALLOWED, SC-TASK-002-AUTH-ABSENT, SC-TASK-002-AUTH-UNRESOLVED, SC-TASK-002-AUTH-UNKNOWN, SC-TASK-002-AUTH-INSUFFICIENT | `Test_TaskCases.testListTasks` |
| AC-TASK-002-SUCCESS | UC-TASK-002 | BT-TASK-002 | SC-TASK-002-SUCCESS, SC-TASK-002-STORAGE-FAILURE | `Test_TaskCases.testListTasks` |
| AC-TASK-002-EMPTY | UC-TASK-002 | BT-TASK-002 | SC-TASK-002-EMPTY, SC-TASK-002-STORAGE-FAILURE | `Test_TaskCases.testListTasks` |
| AC-TASK-003-AUTH | UC-TASK-003 | BT-TASK-003 | SC-TASK-003-AUTH-ALLOWED, SC-TASK-003-AUTH-ABSENT, SC-TASK-003-AUTH-UNRESOLVED, SC-TASK-003-AUTH-UNKNOWN, SC-TASK-003-AUTH-INSUFFICIENT | `Test_TaskCases.testCompleteTask` |
| AC-TASK-003-SUCCESS | UC-TASK-003 | BT-TASK-003 | SC-TASK-003-SUCCESS | `Test_TaskCases.testCompleteTask` |
| AC-TASK-003-MISSING | UC-TASK-003 | BT-TASK-003 | SC-TASK-003-MISSING | `Test_TaskCases.testCompleteTask` |
| AC-TASK-003-IDEMPOTENT | UC-TASK-003 | BT-TASK-003 | SC-TASK-003-IDEMPOTENT | `Test_TaskCases.testCompleteTask` |

O JSON inclui referências de apoio, decisões, hashes das fontes e limites por obrigação. Os cenários de falha de armazenamento complementam a matriz; o teste de apoio não cria uma quarta identidade comportamental. A execução dos testes é registrada separadamente; a presença destas referências não constitui execução.

## Decisões e limites conferidos

Identificador gerado pela aplicação; título normalizado e limitado a 120 caracteres; conclusão booleana idempotente; listagem por ordem de inserção; invariantes canônicas da entidade; contexto confiável e autorização antes de chamadas protegidas. A realização usa UUID4 e SQLite como escolhas concretas. Não acrescenta revisão otimista nem identifica uma falha de escrita como prova de ausência de efeito.

A revisão resultou em cinco ajustes rastreados no JSON: resolução hierárquica de símbolo Python, diagnóstico de app fora do escopo, cenário real de CLI complete negado, teste de ordenação com duas tarefas e falha de listagem distinta de vazio. Os testes finais documentam a verificação das correções.

A verificação não cobre execução C/Go ou Docker, browser ponta a ponta, autenticação de produção, carga, recuperação distribuída ou CI hospedada. Nenhum motor de transformação automática de Atlas para código é alegado. No pacote Minerva, fontes observadas são documentação; o programa executável está no pacote Vulcan.
