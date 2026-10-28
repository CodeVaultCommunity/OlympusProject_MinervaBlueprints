# Conformidade e alcance da avaliação

[English](conformance.md) · [Regras normativas](model.pt-br.md) · [Correspondência OAL](oal-correspondence.pt-br.md)

Minerva estabelece os assuntos do L2 do OAL Stable-v1.0.0: dez de ADPM e cinco de ADVS. Regras do modelo, conformidade da instância, preservação da fonte e resultados observados da realização são alegações distintas.

| Avaliação | O que estabelece | O que não estabelece |
| --- | --- | --- |
| Schema | Representação Minerva suportada e campos exigidos | Consistência dos vínculos ou suficiência comportamental |
| Consistência | Identidades, vínculos tipados, catálogo de origem, relação caso/teste, cobertura de critérios e topologia dos grafos declarados | Verdade/completude das declarações de origem ou equivalência semântica |
| Integridade da fonte | Arquivo fornecido corresponde ao hash declarado | Transcrição correta da identidade, revisão ou requisitos |
| Inspeção de código | Bytes solicitados e nomes lexicais Python suportados | Execução, imposição de autorização ou resultados de testes |
| Revisão semântica | Comparação e avaliação de projeto registradas no escopo indicado | Aprovação de stakeholders ou propriedades não observadas em execução |

`layer_coverage: declared_adpm_and_advs` significa que os dois componentes foram inspecionados. Não é certificação OAL. `reviewed` indica a revisão técnica declarada; responsável e pendências preservam a aceitação ainda pendente do autor. Um rascunho é inconclusivo no modo de consistência. Uma ficha de fonte isolada não constitui ADMV completa.

O catálogo de origem é conteúdo Minerva com espaço de identidades separado. O validador nunca interpreta Atlas ou outro modelo L1. Uma declaração incorreta acrescentada de forma consistente ao catálogo pode passar; a revisão deve compará-la com a fonte fixada. Veja a [integração Atlas](../integrations/atlas/mapping.pt-br.md).

Fora do escopo: tradução automática, aplicativos de domínio executáveis, conformidade de arquitetura L3, autenticação de produção, garantias reais de persistência, resultados de CI remoto e prova geral de algoritmos. Contratos podem ser especificados e receber verificações planejadas antes dessas realizações existirem.
