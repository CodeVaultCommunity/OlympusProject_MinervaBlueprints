# Minerva YAML · perfil 0.1.0

[English](README.md) · Português brasileiro · [Regras do modelo](../../README.pt-br.md#reference-rules)

Esta representação implementa Minerva Blueprints `Alpha-v0.1.0`, dirigido ao OAL `Stable-v1.0.0`. O [JSON Schema canônico](../../minerva_blueprints/schemas/minerva.schema.json) acompanha o validador. Verificar a representação estabelece dados legíveis e suportados, não suficiência semântica.

## Documentos e raízes

Dois tipos compartilham `format: minerva-yaml`, `model_version: Alpha-v0.1.0` e `profile_version: 0.1.0`:

| Tipo | Papel | Grupos obrigatórios no primeiro nível |
| --- | --- | --- |
| `blueprint` | Instância integrada de programa/verificação com escopo e procedência | `oal_edition`, `document`, `source_l1`, `adpm`, `advs`, `mirror` |
| `source` | Ficha descritiva de vínculo por arquivo; várias unidades podem ocupar uma fonte | `document_id`, `source`, `units`, `graphs`, `dependencies`, `limitations` |

`--root` identifica a raiz do ecossistema. Todo caminho de artefato dentro dos documentos é resolvido por essa raiz. O documento passado na linha de comando é um caminho comum do sistema de arquivos. A raiz recomendada do espelho é `docs/L2_MinervaBlueprints`; alternativas como `design/program` são válidas. Dados raiz `R` e caminho de fonte `P`, a ficha fica exatamente em **`R/P.yaml`**. Assim, `apps/Billing/Task.go` corresponde a `docs/L2_MinervaBlueprints/apps/Billing/Task.go.yaml`, preservando diretórios e extensão.

Caminhos usam `/`, são relativos e não contêm `..`, prefixo de unidade ou barras invertidas. Caminhos resolvidos e symlinks não podem escapar da raiz. Mova o pacote completo para preservar relações. `mirror.documents` lista as fichas; `coverage: declared` indica apenas os vínculos selecionados; `coverage: complete` declara também o escopo de fontes em `include_patterns` e exclusões justificadas. A cobertura dos arquivos atuais só é conferida com `--verify-code`.

## Mapeamento do modelo

| Construção | Representação e significado |
| --- | --- |
| Identidade e revisão | `document.id`, `revision`, `title`, `scope`, `responsible`; revisão é texto |
| Estado elaborado | `document.status`: `draft` ou `reviewed`; autoridade de revisão e aprovação pendente permanecem explícitas |
| Procedência | `document.nature`: `designed`, `reconstructed` ou `mixed` |
| Decisões e observações | `document.decisions[]`: ID próprio, tipo, declaração, origem e revisão |
| Fonte versionada | `source_l1`: modelo/versão, caminho, identidade/revisão, casos selecionados e hash opcional |
| Entidades | `adpm.entities[]`: campos, significado, construção canônica, invariantes, comportamento e dependências |
| Refinamentos de primitivos | `adpm.types[]`: ID, base primitiva e restrições textuais |
| Capacidades de ferramentas | `adpm.tools[].operations[]`: contrato semântico independente do mecanismo |
| Casos de programa | `adpm.cases[]`: caso de origem, app, objetivo, dados, colaboradores, regras, permissão, comportamento e falhas |
| Regras canônicas | `adpm.rules[]`: identidade, responsável, origens, declaração e tipo |
| Composição e propriedade | `adpm.dependencies`, `composition.selection_location`, `composition.lifetimes` |
| Domínios | `adpm.domains[]` e `case.domain_ref` recíprocos; agrupamento não concede permissão |
| Algoritmos semânticos | `behavior.summary`, passos, pre/pós-condições, efeitos e grafos |
| Grafos | `adpm.graphs[]` e `graphs[]` da ficha; proprietário, entrada, nós e arestas estruturados |
| Identidade comportamental | `advs.behavioral_tests[]`: um vínculo com caso/origem, critérios, cenários e referências de apoio |
| Oráculo de cenário | Preparação, contexto, ação, limite/configuração, resultado/efeitos, aplicabilidade e justificativa |
| Realização de apoio | `advs.supporting_checks[]`: contrato próprio e referência opcional de caminho/símbolo qualificado/estado |
| Execução observada | `advs.executions[]`: verificações, revisão, ambiente, resultado, momento, relatório e limitações |
| Lacunas | `advs.unverified_risks[]` e limitações; ausência de cenário não se torna aprovação |
| Interação | `advs.channel_obligations[]`: declaração, origem e casos; cenários usam `obligation_refs` |
| Vínculo com fonte | `source.path`, app, linguagem, estado, hash, objetivo e observação; `units[].model_refs` preserva identidade lógica |
| Estruturas legadas | Várias `units[]` na mesma ficha, cada uma identificada e descrita |

Todos os objetos têm campos fechados no perfil `0.1.0`; campos desconhecidos são erros. Não há namespace arbitrário de extensões neste perfil YAML. Uma extensão futura exige perfil/mapeamento explicitamente suportado. Não disfarce semântica desconhecida como campo ausente. Essa restrição é do perfil entregue, não da possibilidade abstrata de outra representação Minerva.

## Identidades e tipos

IDs seguem `^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$`, como `UC-TASK-001` e `BT-TASK-001`. São únicos no blueprint carregado e em suas fichas. Referências apontam o tipo de elemento exigido. O mesmo texto pode identificar o conceito correspondente no namespace separado da fonte L1. IDs são identidades elaboradas; ao renomear arquivos preserve-os em vez de gerar outros a partir dos caminhos novos.

Um dado exige `name`, `description`, `type` e `required` booleano; `cardinality` opcional informa cardinalidade textual. Exemplos:

```yaml
kind: primitive
name: string
nullable: true
```

```yaml
kind: entity
ref: ENT-TASK
```

```yaml
kind: array
items:
  kind: entity
  ref: ENT-TASK
```

`type` referencia refinamento nomeado de primitivo por `ref`. `map` declara o tipo de `values`; chaves são textuais. Primitivos: `string`, `integer`, `number`, `boolean`, `bytes` e `null`. São tipos do contrato, não valores de execução presentes no documento. `bytes` não autoriza tags binárias executáveis. Entradas/saídas operacionais permanecem separadas de `technical_parameters` e assinaturas nativas.

Obrigatoriedade e nulabilidade diferem: obrigatório significa integrar o contrato; anulável admite ausência explícita. Contexto de ator é entrada da invocação, não payload JSON de negócio não confiável. Objetos de ferramenta e recursos de banco pertencem à composição/dependência ou à descrição de parâmetros técnicos.

## Estado da fonte e correspondência observada

`source.state: planned` registra estrutura pretendida antes do código e exige `sha256: null`. `observed` registra observação; alegar correspondência atual exige bytes iguais e SHA-256 não nulo. Nenhum estado afirma execução de testes. Um blueprint `designed` pode conter fontes planejadas; `reconstructed` registra reconstrução intencional de realização observada; `mixed` exige decisões explicando a divisão. Pendências ficam em decisões `open_issue`, rascunho ou limitações, sem estados observacionais inventados.

Cada unidade identifica `code_name`, `kind`, `role`, `model_refs`, descrição, atributos e operações. `class`, `struct`, `function` e `module` descrevem unidades físicas. Os papéis incluem caso, entidade, value object, ferramenta, boundary, composição, teste, apoio e legado. Funções associadas a uma struct C/Go podem ser descritas nessa unidade; a inspeção Python só suporta as formas Python declaradas.

Uma operação registra contrato de dados e comportamento; operações técnicas descrevem colaboradores separadamente. `dependencies[].from_unit` aponta uma unidade local; `target` textual descreve importação, chamada ou recurso, sem implementar resolvedor universal entre linguagens. O grafo lógico de dependências ADPM resolve IDs tipados separadamente.

## Adaptador L1 e critérios

O leitor suporta **JSON de Atlas Specifications Stable-v1.0.0** em `source_l1.artifact`. Confere identidade fixada, revisão, casos selecionados, critérios e atores. Não substitui o validador semântico completo Atlas. Outros modelos podem ter mapeamento L2 abstrato válido, mas esta ferramenta informa adaptador não suportado.

Uma extensão Atlas explicitamente selecionada, `atlas.extensions.minerva_shared_criteria`, pode conter registros `{id, case_ids, statement}`. Cada critério compartilhado precisa de declaração canônica não vazia e de todos os casos participantes no escopo. Cada teste afetado lista o critério; a verificação comum vincula todos esses testes reciprocamente. Isso é uma **convenção do adaptador**, não campo normativo novo do Atlas nem outro caso UCS. A suíte demonstra vínculos compartilhados completos e incompletos.

## Semântica dos grafos

`owner_ref` identifica o comportamento descrito. `entry` aponta um nó do grafo. Arestas possuem IDs globais, `from`, `to`, `condition` e `action` textuais. Nós `flow` utilizam início/ação/decisão/fim/falha conforme pertinente; fluxo finito declara ao menos um fim ou falha. `state_machine` utiliza estados e transições identificados, permitindo auto-transições e ciclos. O validador confere referências e alcançabilidade sem avaliar condições ou provar terminação. Ação vazia significa “sem ação adicional”; a condição ainda precisa explicar seu significado.

## Ausente, nulo, vazio e desconhecido

Campos obrigatórios não podem ser omitidos. `null` só é aceito onde explicitamente permitido: hash ainda não observado, ausência de entidade de origem, ausência de referência de código ou de observação de execução. Lista vazia significa “nenhum declarado no escopo”, não “desconhecido”. Texto substantivo vazio é rejeitado; ação de aresta é exceção deliberada. Uma decisão obrigatória não pode ficar escondida em lista vazia: blueprints revisados exigem casos de origem, casos de programa e testes diretamente vinculados não vazios. Informação desconhecida pertence a decisão/limitação e frequentemente mantém o documento em rascunho.

O leitor aceita subconjunto escalar restrito: `true`, `false`, `null` minúsculos, inteiros/decimais JSON, textos, mapas e listas. `yes`, `on`, datas e números com zero inicial como `012` permanecem texto. Escreva revisões como `'1'`. Tags explícitas, âncoras, aliases, chaves duplicadas/não textuais, resultados numéricos não finitos e documentos maiores que 8 MiB são recusados. Comentários são editoriais, não conteúdo do modelo; a ferramenta não promete preservar formatação em ida e volta.

## Fluxo de validação

```bash
# A partir da pasta da edição
python validator/minerva_validate.py examples/minimal/docs/L2_MinervaBlueprints/blueprint.yaml --root examples/minimal --json
python examples/counterexamples/check.py
```

Valide primeiro a estrutura. Depois examine vínculos de origem, cardinalidade caso/teste, cobertura de critérios, referências tipadas, propriedade e grafos. Revise semântica e pendências. Solicite `--verify-code` somente contra realização fornecida e examine hashes e símbolos. Execute testes da aplicação separadamente e registre resultados reais com revisão e ambiente avaliados. O perfil não escreve nem aprova código, não realiza derivação de camada e não converte inspeção de fonte em relatório de execução.
