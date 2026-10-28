# Registro da revisão local · Alpha-v0.1.0

[English](RELEASE.md) · [Requisitos](REQUIREMENTS.pt-br.md) · [Validação](VALIDATION.pt-br.md) · [Revisão dos contratos](reviews/contract-review.pt-br.md)

A Alpha-v0.1.0 existente e não publicada foi revisada no próprio lugar por solicitação do responsável. Nenhuma nova edição ou versão do modelo, perfil ou ferramenta foi criada. Minerva entrega o modelo L2, representação YAML, validador, documentação e exemplos elaborados a partir das fontes oficiais. A integração Atlas é documental; nenhum reader Atlas ou motor de tradução é entregue.

Especificação, regras de conformidade e correspondência OAL ficam em `specification/`; o perfil YAML selecionado fica em `implementations/yaml/`; mapeamento documental e compatibilidade ficam em `integrations/atlas/`. Os exemplos principais são `minimal`, `task-board` e `composition`, com snapshots das revisões 2/3 do TaskBoard. Fixtures ficam em `tests/fixtures/`. Requisitos, fontes fixadas, revisões técnicas e resultados efetivos ficam separados dentro de `verification/`.

O [registro de validação](VALIDATION.pt-br.md) informa 50 testes da edição, 33 da raiz, 12 resultados de contraexemplos, validação de fontes, edição isolada e wheel. Cenários de domínio continuam planejados. A revisão da fonte identifica a questão aberta da fronteira de medição compartilhada pelo cancelamento. Não se afirma aceite semântico do responsável nem execução do CI hospedado.

Conclua documentos e evidências antes de gerar `CONTENT-SHA256.json` na raiz; depois confira e faça commit local conforme o [procedimento de distribuição](../../../docs/releasing.pt-br.md). O inventário é o único inventário ativo da entrega e exclui a si mesmo. O identificador do commit final e eventual hash de ZIP pertencem fora da árvore que identificam. As fontes fixadas registram bytes de origem separadamente e não substituem o inventário de entrega. Este registro não afirma publicação remota ou release no GitHub.
