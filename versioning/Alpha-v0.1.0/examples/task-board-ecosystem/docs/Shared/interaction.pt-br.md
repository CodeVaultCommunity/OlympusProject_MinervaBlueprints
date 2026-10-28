# Mapeamentos de interação — L4

Esta é a projeção canônica dos canais da **demonstração local**. Estar em `Shared/` não altera sua responsabilidade L4. Contratos e cenários de domínio são referenciados em [Minerva L2](../L2_MinervaBlueprints/blueprint.yaml); a documentação L3 do Vulcan companheiro (`docs/L3_Vulcan/README.pt-br.md` naquele ecossistema) registra composição e execução concretas.

| Estímulo / operação pública | Caso preparado | Representação de entrada | Resultado de canal |
| --- | --- | --- | --- |
| Botão Create task / `POST /tasks` | `UC-TASK-001`, `UseCase_CreateTask.createTask` | Objeto JSON contendo somente `title`; contexto resolvido no servidor | HTTP 201 com projeção da tarefa |
| Botão Refresh / `GET /tasks` | `UC-TASK-002`, `UseCase_ListTasks.listTasks` | Sem corpo; contexto resolvido no servidor | HTTP 200 `{ "tasks": [...] }` |
| Botão Complete / `POST /tasks/{task_id}/complete` | `UC-TASK-003`, `UseCase_CompleteTask.completeTask` | Identificador codificado na rota e objeto JSON vazio | HTTP 200 com projeção da tarefa |
| CLI `create --title TEXT` | `UC-TASK-001` | Argumento textual e token resolvido pela composição | Projeção na saída padrão, código 0 |
| CLI `list` | `UC-TASK-002` | Token resolvido pela composição | Envelope de tarefas na saída padrão, código 0 |
| CLI `complete TASK_ID` | `UC-TASK-003` | Identificador textual e contexto resolvido | Projeção na saída padrão, código 0 |
| LegacyReports `GET /report` ou `/` / CLI `report` | Função existente `create_report`; não é caso Vulcan inventado | URL TaskBoard e token leitor configurados | Contagens `total`, `completed`, `pending` |

Uma projeção contém os primitivos `task_id` (texto), `title` (texto) e `completed` (booleano). O canal serializa uma entidade, sem expor value object, conexão, composição ou permissões fornecidas pelo cliente. O navegador insere títulos com `textContent` e dispara as operações HTTP; não acessa SQLite.

TaskBoard HTTP projeta recusa em 403, entrada/corpo inválidos em 422, tarefa ou rota inexistente em 404 e falha de armazenamento capturada em 503. Corpos são objetos JSON de até 8192 bytes pelo comprimento declarado. Criação aceita exatamente `title`; conclusão não aceita campos. Validação do formato pode recusar requisição malformada antes de autorizar ator; qualquer efeito de domínio continua exigindo autorização do caso. O escopo é desenvolvimento local, com servidor HTTP da biblioteca padrão Python.

Na CLI TaskBoard, erros de domínio são JSON em stderr: 3 recusa, 2 dado inválido, 4 ausência e 5 armazenamento. Erros de parser/configuração podem usar texto de uso com código 2. LegacyReports projeta `upstream_unavailable_or_invalid` em HTTP 502 ou CLI 5; seu erro JSON de CLI permanece em stdout para preservar a interface procedural existente.

`GET /health` é metadado operacional, sem novo caso de domínio: devolve app, prontidão e identidade da execução. A página `GET /` do TaskBoard é apresentação. Endpoints de relatório são agregados **locais** sem autenticação própria, usando identidade leitora no upstream; exposição remota exigiria política de acesso especificada separadamente.

`Test_Boundaries` exercita os canais. Servir e ler HTML está coberto; cliques e renderização no navegador não estão. O material não reivindica modelo OAL L4 completo e reutilizável.
