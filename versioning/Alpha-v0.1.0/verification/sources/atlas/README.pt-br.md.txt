# Atlas Specifications · Stable-v1.0.0

[English](README.md) · Português brasileiro

**Atlas é um modelo abstrato para especificações declarativas de casos de uso.** Esta edição Stable define seu contrato semântico, os perfis Atlas JSON/Markdown/LaTeX e um tradutor Python com verificação de conteúdo exato. Outros modelos podem implementar a abstração mediante mapeamento explícito. Modelo, modelo implementador, representação e artefato concreto de projeto possuem responsabilidades distintas.

Esta pasta é uma edição autossuficiente: mantenha seus arquivos juntos para usar documentação, documentos iniciais, exemplos, tradutor e testes sem depender da raiz do repositório. Os recursos do runtime e dos exemplos permanecem locais. O README e a pasta `assets/` da raiz apresentam o projeto com ilustrações; essas imagens não são necessárias para usar esta edição. A skill também funciona isoladamente. O inglês é a fonte normativa; o português é a tradução de leitura correspondente. **DEVE**, **NÃO DEVE** e **OBRIGATÓRIO** indicam obrigações. Aprovação no schema não estabelece, por si só, conformidade semântica.

<a id="release-notes"></a>
## Notas da versão — Stable-v1.0.0

Esta edição preserva o escopo L1 do Atlas e corrige quatro defeitos auditados: ausência de registros opcionais de entidades; referências tipadas de figuras/fontes/premissas/pendências; CRLF/CR/LF exatos nas células LaTeX; e separadores Unicode em dados opacos. Corrige também a fronteira entre CR autoral final e delimitador. Referências inválidas falham antes da gravação da saída.

As identidades de modelo/perfil são `Stable-v1.0.0`; pacote e produtor de novos documentos são `1.0.0`. A edição Alpha histórica permanece intacta. A Stable rejeita perfis incompatíveis explicitamente. A conversão preserva todas as identidades e histórico autorais. Starters e exemplos receberam migração editorial com proveniência, e o quadro de tarefas contém duas revisões Stable válidas demonstrando uma mudança de vínculo de aceite.

O OAL Stable-v1.0.0 foi entregue por checkout Git local fixado e revisado contra dez cláusulas UCS e nove transversais. Não se afirma disponibilidade remota. Consulte a [correspondência](#oal-conformance), a [política de compatibilidade](COMPATIBILITY.pt-br.md), o [registro de verificação](verification/RELEASE.md) e o [registro da migração](verification/editorial-migration.json). Publicação e aprovação de stakeholders são distintas dessas verificações.

A publicação LaTeX desta edição inclui temas editorial e plain, capa ornamental autocontida, tabelas com quebra de texto e imagens decorativas opcionais mantidas fora do conteúdo da especificação. O [contrato de estilo de publicação](implementations/latex/README.pt-br.md#publication-style) explica o que a conversão preserva e como manter a aparência personalizada separadamente.

## Sumário

- [Notas da versão](#release-notes) · [Versões](#versions) · [Iniciar uma especificação](#quick-start)
- [Implementações de representação](#implementations) · [Tradução](#translation)
- [Modelo abstrato](#abstract-model): [identidade](#model-3), [conceitos](#model-4), [texto](#model-5), [referências](#model-6), [consumo](#model-7), [entidades](#model-8), [ferramentas](#model-9), [casos e requisitos](#model-10), [fronteiras](#model-11), [proveniência](#model-16), [invariantes](#model-18)
- [Contrato de grafos](#graph-contract) · [Recursos](#resource-contract) · [Preservação](#preservation)
- [Exemplos](#examples) · [Skill para IA](#ai-skill) · [Verificação](#verification)
- [Correspondência OAL](#oal-conformance) · [Versionamento](#versioning) · [Autoria](#authorship)

<a id="versions"></a>
## Versões

| Edição | Status | Notas da versão | Regras de referência | Guia de verificação | Guia de conformidade |
| --- | --- | --- | --- | --- | --- |
| Stable-v1.0.0 | Edição Stable | [English](README.md#release-notes) · [Português](README.pt-br.md#release-notes) | [English](README.md#reference-rules) · [Português](README.pt-br.md#reference-rules) | [English](README.md#verification) · [Português](README.pt-br.md#verification) | [English](README.md#conformance) · [Português](README.pt-br.md#conformance) |

<a id="quick-start"></a>
## Iniciar uma especificação

Use **Python 3.11+**. No diretório desta edição, crie e ative um ambiente virtual e instale o pacote local:

```bash
python -m venv .venv
# POSIX: source .venv/bin/activate
# PowerShell: .venv\Scripts\Activate.ps1
python -m pip install .
python translator/atlas_translate.py formats
python translator/atlas_translate.py validate implementations/json/starter.atlas.json
```

Comece copiando [o documento inicial JSON](implementations/json/starter.atlas.json), [Markdown](implementations/markdown/starter.atlas.md) ou [LaTeX](implementations/latex/starter.atlas.tex) para sua pasta de trabalho. Os três carregam o mesmo conteúdo inicial. É um **rascunho estruturalmente válido**, com seções editoriais, coleções de domínio vazias e perguntas explícitas sobre escopo/fontes. Substitua identidade/autoria e desenvolva a especificação a partir de necessidades reais. Um documento inicial válido não é uma especificação L1 completa e não inventa requisitos de negócio. Os exemplos completos ensinam contratos preenchidos.

Prefira JSON para autoria estrutural, valide-o e gere as representações de leitura/publicação. Uma edição somente textual em Markdown/LaTeX pertence aos registros autoritativos marcados. Mudanças estruturais exigem atualizar o apêndice de modo consistente; diagramas derivados são regenerados. Registre mudanças autorais como revisões de conteúdo.

```bash
python translator/atlas_translate.py convert implementations/json/starter.atlas.json --from json --to markdown -o work/specification.atlas.md
python translator/atlas_translate.py convert work/specification.atlas.md --from markdown --to latex -o work/specification.atlas.tex
python translator/atlas_translate.py convert work/specification.atlas.tex --from latex --to json -o work/returned.atlas.json
```

O documento inicial não usa recursos externos. Para documentos com recursos, siga o [contrato de pacotes](#resource-contract). O comando instalado `atlas-spec` e `python -m atlas_spec` oferecem a mesma interface. O launcher usa somente esta edição ou o runtime distribuído ao seu lado na skill; nunca seleciona outra versão do repositório nem instala dependências automaticamente.

<a id="implementations"></a>
## Implementações de representação

| Implementação | Conteúdo autoritativo | Arquivos para uso |
| --- | --- | --- |
| [Atlas JSON](implementations/json/README.pt-br.md) | Payload `atlas` completo, incluindo prosa e estrutura. | [Schema](implementations/json/atlas.schema.json) · [Documento inicial](implementations/json/starter.atlas.json) |
| [Atlas Markdown](implementations/markdown/README.pt-br.md) | Registros de texto visíveis marcados e apêndice identificado para estrutura. | [Documento inicial](implementations/markdown/starter.atlas.md) |
| [Atlas LaTeX](implementations/latex/README.pt-br.md) | Ambientes/células de texto visíveis e apêndice estrutural comentado. | [Documento inicial](implementations/latex/starter.atlas.tex) · [Estilo](implementations/latex/atlas.sty) |
| Publicação PDF | Renderização compilada para leitura e compartilhamento. | Incluída junto de cada exemplo completo; não é fonte reversível. |

Um **schema** verifica a estrutura suportada; um **documento inicial (starter)** é um arquivo para copiar/preencher; um **exemplo** demonstra contratos preenchidos; `atlas.sty` fornece macros e apresentação LaTeX. As gramáticas vinculadas definem perfis controlados de Markdown/LaTeX. Documentos arbitrários nesses idiomas de marcação não são automaticamente instâncias Atlas.

<a id="translation"></a>
## Processo de tradução

Quatro transformações primitivas, Markdown ↔ JSON e LaTeX ↔ JSON, permitem as **seis conversões dirigidas entre formatos distintos**. Markdown ↔ LaTeX passa pelo conteúdo Atlas JSON validado em memória. JSON é o intermediário do tradutor de referência; implementar o modelo abstrato não exige armazenamento JSON.

1. Ler o perfil/versão escolhido e recusar entrada não suportada.
2. Decodificar texto e estrutura autoritativos; verificar slots e regiões derivadas.
3. Validar o payload recuperado, referências, propriedade, reciprocidade RF/grafo, referências de RNF e contratos de recursos.
4. Codificar o destino e regenerar sua apresentação derivada.
5. Decodificar e validar essa saída novamente; comparar todo o payload `atlas`, distinguindo tipos.
6. Gravar somente após verificação bem-sucedida; emitir diagnóstico caso contrário.

Use `package` separadamente para deslocar recursos. Compile e revise visualmente o PDF como etapa posterior de publicação. O conversor preserva versões autorais, idioma, requisitos e revisão; não faz mudanças editoriais, tradução entre modelos ou derivação entre camadas OAL. [Preservação](#preservation) define a garantia exata e os modos diagnósticos mais fracos.

Para outro modelo implementador, publique o mapeamento de conceitos/invariantes, domínio de artefatos válidos, restrições, exclusões e evidência de preservação. Para outra representação, implemente decode/encode versionados sobre o conteúdo comum, registre o adaptador e teste seu domínio declarado. Ele deve preservar texto, estrutura, extensões e recursos exigidos ou recusar a entrada não suportada. Pertencer à mesma camada não estabelece um tradutor universal.

<a id="reference-rules"></a>
<a id="abstract-model"></a>
## Modelo abstrato

As seções numeradas seguintes definem o modelo. Os nomes de campos identificam o mapeamento dos perfis fornecidos; outro modelo pode recuperar os mesmos papéis semânticos por um mapeamento declarado.

<a id="model-1"></a>
### 1. Finalidade e posição

Atlas Specifications é um **modelo abstrato reutilizável do L1 (UCS) do OAL**. Ele define conceitos, informações, relações, invariantes, identidades, referências, contratos comportamentais e obrigações de preservação de uma especificação declarativa.

O L1 do OAL estabelece responsabilidades para modelos reutilizáveis. Uma especificação de projeto é um artefato do modelo escolhido. Atlas estabelece escopo, atores e autorização, contratos de comportamento, entidades e regras, dependências, obrigações complementares, aceite, consistência, domínios opcionais e exemplos. Não declara cobertura de L2, L3, L4, de um engine de derivação ou de todas as camadas. Consulte a [matriz de conformidade](#oal-conformance).

O modelo abstrato independe de JSON, Markdown e LaTeX. Sua compreensão não exige conhecer a disposição dos objetos JSON.

<a id="model-2"></a>
### 2. Modelo, implementação e instância

| Objeto | Significado | Exemplo |
| --- | --- | --- |
| Metamodelo OAL L1 | Responsabilidades que um modelo L1 deve estabelecer. | Regras UCS do OAL Stable-v1.0.0. |
| Modelo abstrato Atlas | Conceitos, relações, invariantes e preservação. | Este documento. |
| Modelo implementador ou especialização | Outro modelo reutilizável com mapeamento explícito para Atlas. | Um futuro modelo de especificação de um domínio. |
| Implementação de representação | Sintaxe concreta que carrega o conteúdo do modelo escolhido. | Atlas JSON, Atlas Markdown e Atlas LaTeX. |
| Artefato de projeto / instância | Conteúdo concreto conforme seu modelo, possivelmente distribuído em arquivos. | A especificação do quadro de tarefas. |
| Publicação | Renderização de uma instância para leitura. | PDF compilado de Atlas LaTeX. |

Outros modelos PODEM implementar ou especializar Atlas. A declaração DEVE identificar versão, escopo suportado, mapeamento de conceitos, restrições adicionais, construções não suportadas e evidência de que as obrigações do escopo continuam recuperáveis. Uma especialização não pode remover uma obrigação de Atlas e declarar conformidade completa. Nomes ou estruturas diferentes são permitidos com mapeamento explícito. Isso não cria uma camada adicional do OAL nem exige um novo metanível.

As três implementações entregues são perfis de representação do mesmo conteúdo Atlas. Três arquivos não estabelecem três modelos OAL. Um modelo implementador pode ter várias representações. Tradução entre modelos distintos exige outro mapeamento e contrato de preservação; os codecs não o inferem.

Atlas JSON é o intermediário do tradutor fornecido, e não a definição do modelo abstrato. Os nomes de campos deste documento identificam papéis semânticos e seu mapeamento nos perfis de referência. Outro modelo pode recuperá-los de outra forma. JSON Schema, marcadores, envelopes e metadados de codec são obrigações dos perfis. PDF é publicação derivada, sem importação ou conversão reversível.

<a id="model-3"></a>
### 3. Identidade e versões do documento

Todo artefato declara identidade, revisão, modelo/versão escolhidos, idioma, estado de revisão, título, autoria e datas de criação/atualização. Nos perfis entregues:

| Campo | Significado / obrigação |
| --- | --- |
| `document_id` | Identificador estável do documento, conforme a gramática de IDs. |
| `revision` | Revisão do conteúdo; texto não vazio. |
| `spec_version` | Versão abstrata: `Stable-v1.0.0`. |
| `profile_version` | Versão do perfil; obrigatória nos três perfis: `Stable-v1.0.0`. |
| `translator_version` | Versão declarada do produtor preservada no conteúdo; obrigatória nos perfis. Os novos exemplos usam `1.0.0`. |
| `language` | Idioma do texto autoral. |
| `status` | Estado de revisão/aprovação; independente de `nature`. |
| `title` | Registro de texto do título. |
| `subtitle` | Opcional: ausente, `null` ou registro de texto; estados distintos. |
| `authors` | Lista de autoria; não substitui o responsável nominal de uma derivação. |
| `created`, `updated` | Datas ISO. |

Uma conversão NÃO DEVE mudar esses valores. Versão não suportada provoca recusa. Conversão de representação não é migração de versão.

<a id="model-4"></a>
### 4. Conceitos centrais

| Conceito | Responsabilidade |
| --- | --- |
| Seção | Capítulo editorial ordenado, com título, blocos e referências a elementos; ao menos uma. |
| Ator | Participante externo: pessoa, sistema, organização ou papel. |
| Termo | Vocabulário do domínio, definição e sinônimos opcionais. |
| Tipo | Tipo de dado nomeado, restrições e exemplos. |
| Entidade | Significado, identidade, campos, relações, estados, transições, validade e exemplos. |
| Validação | Regra de validade da entidade com entradas, condições, resultados e grafo. |
| Ferramenta | Capacidade abstrata com operações e contratos. |
| Caso de uso | Objetivo, atores, condições, dependências, resultados, RFs/RNFs, fluxos, aceite e rastreabilidade. |
| Fronteira | Necessidade/restrição de interação ou referência claramente classificada, com mapeamento dos casos expostos. |
| Grafo | Fluxo, estados ou relações estruturados; proprietário explícito. |
| Recurso | Arquivo/ativo com origem, caminho, hash, textos, fonte editável e variantes. |
| Premissa, decisão, pendência, fonte e histórico | Contexto, escolhas, dúvidas, proveniência e evolução. |
| Extensão | Dados declarados em `extensions`, preservados como conteúdo opaco. |

Atores, termos, tipos, entidades, ferramentas, casos e fronteiras declarados aparecem exatamente uma vez na estrutura editorial. A ordem de `structure` define apresentação. Referências anteriores ou posteriores são válidas; posição não define identidade.

<a id="model-5"></a>
### 5. Texto e conteúdo rico

Conteúdo legível usa registros com `text`. Metadados opcionais: `id`, `nature`, `review_status`, `meta`, `extensions`. Ausência de texto não equivale a texto vazio. Os contêineres livres `meta`, `data` de exemplos de entidade e `extensions` são dados estruturais opacos: chaves `text`, `@text` ou `id` neles são dados literais, não slots textuais ou declarações de elemento Atlas. Seus valores e tipos continuam preservados.

| Bloco | Conteúdo |
| --- | --- |
| `paragraph`, `note`, `quote` | Texto de parágrafo, nota ou citação. |
| `heading` | Nível de 1 a 6 e texto. |
| `list` | Ordem e itens textuais; filhos opcionais. |
| `code` | Fonte literal e idioma opcional; não executada. |
| `formula` | Fonte literal e indicação de exibição; não executada. |
| `figure` | Recurso e legenda/texto alternativo opcionais. |
| `table` | Colunas e linhas de registros de texto; legenda opcional. |

Texto é preservado exatamente: espaços, tabulações, quebras autorais, espaços finais, sequências Unicode e presença/ausência de quebra final. Quebras introduzidas pelo formato devem ser distinguíveis. Conversão não normaliza Unicode, não apara texto, não altera caixa e não traduz idioma natural.

`nature` distingue `observed`, `desired`, `inference`, `assumption`, `open_issue`, `decision`, `note`. `review_status` distingue `draft`, `proposed`, `reviewed`, `approved`, `rejected`, `deprecated`. A natureza de uma afirmação e sua situação na revisão são independentes.

<a id="model-6"></a>
### 6. Identidade e referências

Gramática:

```text
[A-Z][A-Z0-9]*(-[A-Z0-9]+)+
```

Exemplos: `ENT-TASK`, `UC-TASK-CREATE`, `RF-TASK-CREATE-01`.

1. IDs são globalmente únicos, incluindo campos, operações, validações, nós, arestas e `document_id`.
2. Referências usam IDs, não posições. Rótulos de mapeamento como `form.code` são rótulos explícitos, não referências a elementos.
3. Relações declaradas dos dois lados são consistentes nos dois sentidos, como RF ↔ elemento de grafo.
4. Reordenação ou conversão não troca IDs.
5. Referências ausentes, IDs duplicados e conceitos declarados sem posição editorial são erros. Um conceito não precisa ser consumido por outro para poder ser documentado.
6. Mudança que preserva a identidade mantém o ID. Substituição, exclusão ou divisão registra ID anterior, sucessores, razão e referências afetadas em histórico/decisões. Nenhuma referência pode ficar pendente. Conversão não realiza essa edição.

<a id="model-7"></a>
### 7. Regras de consumo

Ordem de apresentação principal: **entidades → ferramentas abstratas → casos de uso → fronteiras de interação**. Contexto, escopo, atores, vocabulário e tipos podem vir antes.

| Elemento | Pode consumir |
| --- | --- |
| Entidade | Nenhum colaborador. |
| Ferramenta | Entidades como significado/tipo de dado. |
| Caso de uso | Entidades, ferramentas e outros casos da mesma aplicação. |
| Fronteira | Casos de uso. |

Nos perfis entregues, uma ferramenta não descreve chamadas internas a ferramentas/casos. Essa é uma restrição local de Atlas, não uma regra universal de OAL. Especializações que exponham composição declaram o mapeamento e preservam o contrato consumido pelos casos.

Relação estrutural entre entidades não autoriza acesso a infraestrutura. Nos perfis, essas relações são identificadas por `structural: true`; uma relação estrutural não é uma chamada. Condições externas são obtidas pelo caso por contrato de ferramenta. Domínios opcionais organizam casos e identificam entidades associadas, sem duplicar entidades nem introduzir dependências. Não se exige objeto de domínio nesta versão; seções editoriais podem expressar o agrupamento. Uma chamada de caso preserva contrato, contexto de ator e autorização do caso chamado; composição não amplia permissões.

Uma interação referencia somente RFs do caso que expõe. Uma necessidade nova do domínio deve entrar no caso responsável. Uma escolha de canal introduzida pela solução permanece fora da declaração L1, conforme §11.

<a id="model-8"></a>
### 8. Entidades e validações

Uma entidade declara ID, nome, significado, identidade/campos de identidade, campos tipados com cardinalidade/obrigatoriedade/restrições/exemplos, relações, estados/transições pertinentes, validações, exemplos válidos/inválidos, premissas e pendências.

Uma validação declara ID, nome, escopo (`field`, `between_fields`, `transition`, `entity`), enunciado completo, entradas e significados/origens, condições identificadas, resultados (`pass`, `fail`, `error`, `not_applicable`), grafo próprio e notas opcionais.

A entidade é dona das regras intrínsecas canônicas. Uma condição dependente de estado externo é explicitamente contextual; o caso obtém esse estado por ferramenta e aplica a condição. Não transforme silenciosamente uma condição contextual em invariante autossuficiente da entidade.

Ferramentas que recebem uma entidade já válida assumem suas invariantes intrínsecas, sem repeti-las. Contratos que aceitam registros brutos identificam a construção/hidratação que aplica a validação canônica. Autorização contextual, unicidade, existência, concorrência e outras condições externas à entidade pronta continuam explícitas quando pertinentes. Entidades somente de dados são permitidas; não se exige uma linguagem ou métodos.

A entidade é dona da definição; o caso é responsável pela aplicação e comportamento. O caso referencia a validação canônica.

<a id="model-9"></a>
### 9. Ferramentas abstratas

Ferramentas definem capacidades, não implementações. Cada operação declara ID, nome, propósito, entradas tipadas e significados, condições de uso, resultados e garantias, efeitos observáveis, falhas e sua distinção pelo consumidor.

Quando pertinente, o contrato também define atomicidade, conflitos e se uma resposta de falha prova que o efeito não ocorreu ou deixa o resultado desconhecido. Uma resposta indisponível não prova rollback.

Uma assinatura não basta. Não se prescreve banco, protocolo, algoritmo interno nem fluxograma de implementação. A implementação futura deve satisfazer os casos consumidores e contratos.

<a id="model-10"></a>
### 10. Casos de uso, RFs e RNFs

Cada caso declara ID, nome, objetivo, ator iniciador, atores permitidos e condições de autorização, gatilho/contexto, entradas e condições de entrada, entidades/validações, ferramentas/operações, chamadas a outros casos, resultados/efeitos, RFs/RNFs, grafo principal/subfluxos, fluxo textual completo, aceite, rastreabilidade, premissas, fontes e pendências.

#### Contexto do ator e autorização

Os perfis usam campos de texto existentes, sem exigir uma classe, tecnologia ou objeto JSON universal:

1. `trigger` identifica o ator iniciador por ID.
2. `actors[].permission` e `description` declaram papéis e condições permitidos.
3. `context` define informação exigida do chamador, origem e confiança da resolução, e quando identidade/autenticação são necessárias. O chamador é a pessoa/sistema concreto em cujo nome ocorre a solicitação; ator é o papel declarado.
4. Condições, RFs, resultados e fluxo definem recusa observável para contexto ausente, não resolvido, insuficiente ou não autorizado. Não há efeito protegido antes da autorização. Contexto ausente NÃO DEVE ser tratado como anonimato.
5. Participação anônima ou de sistema é explícita. Autores e responsáveis de derivação não são automaticamente atores de execução.
6. O caso composto recebe o contexto pertinente e continua sujeito ao próprio contrato.

A ferramenta valida estrutura/referências; não prova a adequação da política textual de confiança/autorização.

#### 10.1 Requisitos funcionais

Declarações de **comportamento do domínio em L1** classificadas como RF pertencem às fichas dos casos. Entidades mantêm validações; ferramentas, contratos; fronteiras, mapeamentos. Índices gerais podem ser derivados, mas não são a fonte de autoria.

Restrição externa de interação mantém sua origem. Escolha de canal da solução pertence a L4 e não se torna RF por essa convenção.

Cada RF tem ID, enunciado completo, escopo, alvos aplicáveis e `flow_refs`. Ele aparece na lista do caso e nos `requirement_refs` dos elementos pertinentes do grafo. A relação é muitos-para-muitos e recíproca. A verificação por IDs não prova equivalência de significado entre texto e desenho.

#### 10.2 Requisitos não funcionais

RNFs são listas nas fichas dos casos, sem grafo próprio. Cada um declara ID, enunciado, escopo (`case`, `operation`, `interaction`, `system`), origem individual identificada, aplicabilidade, critério verificável, método/cenário de verificação e elementos afetados. Métrica e início/fim de medição são opcionais; alvos decimais usam texto.

Uma obrigação compartilhada tem uma definição completa canônica e referências explícitas por `reference_to` nos demais casos. Cadeias de referências e autorreferências locais são inválidas. Uma meta não é automaticamente dividida entre ferramentas. Se uma obrigação exige uma ação funcional, essa ação é RF do caso e o RNF continua na lista.

O local de declaração difere do alcance: um RNF pode cobrir o caso, uma operação ou interação completa. A origem DEVE ser recuperável por obrigação: nos perfis, use `references` para IDs de fonte/premissa/decisão e explicite a origem no enunciado/aplicabilidade. Bibliografia genérica não basta. Metas numéricas são requisitos autorais ou propostas/exemplos identificados; conversão não as inventa.

Critérios de aceite apontam as obrigações verificadas e o resultado observável. Critério de integração compartilhado declara escopo, casos afetados e definição única, sem criar novos casos.

<a id="model-11"></a>
### 11. Fronteiras de interação

Uma fronteira declara ID, nome, modalidade, propósito, público, interações e respectivos casos, gatilhos, descrições, mapeamentos de entrada/resultado, RFs referenciados, recursos, exemplos, premissas, fontes e pendências.

O propósito, a descrição e notas vinculadas às fontes DEVEM distinguir:

| Classificação | Tratamento em L1 |
| --- | --- |
| Necessidade de interação do domínio | Comportamento explícito do caso responsável, preservando autorização e semântica. |
| Restrição imposta externamente | Restrição e origem identificada permanecem em L1, mesmo que mencionem protocolo/rota/representação. |
| Escolha de canal introduzida pela solução | Decisão/referência/proposta de L4, excluída da declaração de conformidade L1. |
| Ilustração ou wireframe exploratório | Material ilustrativo; não estabelece requisito externo nem substitui contrato. |

Rotas, telas, codificações e protocolos escolhidos pela solução pertencem a ADIB. Sua presença no pacote não muda essa responsabilidade. Responsabilidades de outros níveis podem ser referenciadas se o escopo for identificável. Uma nova necessidade de domínio descoberta na interação exige revisão do caso UCS e análise das derivações afetadas.

A fronteira mapeia entradas/resultados, sem absorver autorização ou decisões de domínio do caso. Autorização continua válida em chamadas diretas/compostas. Comportamento obrigatório não pode existir apenas no wireframe. O tradutor preserva as declarações, sem implementar ADIB.

<a id="model-12"></a>
### 12. Grafos e imagens

Grafos são dados estruturados, não imagens. Declaram ID, tipo (`flow`, `state`, `relations`), proprietário (documento, entidade, validação ou caso), título, nós e arestas identificados e notas opcionais.

Nós têm tipo, rótulo, chamada opcional a validação/ferramenta/operação/caso/entidade, entradas/saídas/detalhes e referências a RFs. Vocabulário: `start`, `end`, `action`, `decision`, `validation`, `tool`, `operation`, `use_case`, `result`, `refusal`, `failure`, `effect`, `note`, `state`, `entity`. Tipos desconhecidos são recusados.

Arestas têm origem/destino, rótulo/condição/prioridade opcionais e RFs. Ordem de arrays é significativa para autoria/apresentação; identidade usa IDs.

Validação é dona de seu grafo. `flows` identifica principal e subfluxos de cada caso. Grafos de estados/relações podem pertencer a entidade/documento. Texto topológico Markdown e desenho TikZ derivam da mesma estrutura. Não há outra cópia autoritativa da lógica. Imagens derivadas declaram `derived_from_graph` e impressão digital atual em `drawing_source.revision`; divergência é erro de figura desatualizada.

PDF pode conter fluxos de validação/caso/subfluxos e diagramas declarados de estados/relações. RNFs não têm diagrama próprio; não se expõem algoritmos internos de ferramentas.

<a id="model-13"></a>
### 13. Recursos

O contrato de recursos vale para imagens e arquivos que carregam ou ilustram informação da especificação. Arte puramente decorativa de publicação, como um ornamento de capa ou uma imagem de identidade sem significado para a especificação, pertence ao estilo de publicação e PODE ficar fora do catálogo. Essa decoração NÃO DEVE ser o único suporte de requisito, ator, entidade, regra, grafo, critério de aceite, afirmação de proveniência ou outra informação da especificação. Chamar um recurso semântico de decorativo não o dispensa da preservação.

O catálogo declara ID, URI de origem opcional/nula, caminho, tipo de mídia, tamanho, SHA-256, legenda/texto alternativo, textos visíveis na imagem, fonte/revisão/ferramenta de desenho, variantes com origem/produtor e derivação de grafo opcional.

Originais são preservados, sem recompressão ou substituição. Variantes são explícitas e vinculadas. URL preserva referência, não os bytes remotos. Preservação dos bytes exige arquivos locais empacotados. O tradutor opera offline quando eles estão presentes. `--no-check-resources` enfraquece a validação e não equivale a preservar/verificar bytes.

Texto da imagem também aparece no conteúdo textual comum. Preservar somente pixels não basta.

<a id="model-14"></a>
### 14. Estrutura editorial e apêndices

`structure` é ordenado. Seções têm ID, nível relativo de 1 a 5, título, blocos narrativos e lista ordenada de conceitos. Cada ator/termo/tipo/entidade/ferramenta/caso/fronteira aparece uma vez.

Grafos, recursos, premissas, decisões, pendências, fontes e histórico aparecem nos apêndices gerados, permanecendo parte do modelo. A ordem narrativa é autoral. Apêndices não são um modelo alternativo; referências podem apontar para qualquer posição.

<a id="model-15"></a>
### 15. Ausente, nulo, vazio e desconhecido

| Estado | Significado |
| --- | --- |
| Membro ausente | Informação não declarada. |
| `null` | Ausência explicitamente declarada onde permitida. |
| Texto vazio | Registro existente com conteúdo `""`. |
| Lista vazia | Lista declarada sem elementos. |
| Desconhecido | Sem sentinela universal nesta versão; usar pendência, premissa ou extensão documentada. |

Implementações DEVEM preservar essas diferenças. Não podem igualar vazio/ausente/nulo para obter aprovação de um teste.

<a id="model-16"></a>
### 16. Premissas, decisões, pendências, fontes e histórico

Premissas têm enunciado, estado (`open`, `validated`, `refuted`, `withdrawn`) e IDs afetados. Decisões têm título, contexto, escolha, alternativas, consequências, estado e referências. Pendências têm título, descrição, estado e referências. Fontes têm título, URI opcional, revisão, acesso e notas. Histórico registra versão, data e descrição.

Esses registros permanecem distinguíveis de fatos/requisitos. Fontes DEVEM identificar a origem efetivamente usada e sua revisão; uma homepage mutável não é baseline suficiente.

Ao declarar **derivação Needs-to-L1**, registre modelo externo de necessidades e versão, modelo Atlas/implementador de destino e versão, baselines dos artefatos de origem/destino, pessoa nominal responsável, escopo e decisões acrescentadas. Notas, fontes, decisões e histórico podem conter prosa claramente rotulada. Cargo, “equipe” ou ferramenta de IA não substituem o nome. Não fabrique proveniência: registre a pendência e limite a declaração.

Necessidades reconstruídas de UCS são identificadas como reconstruídas. Exemplos sintéticos são identificados como sintéticos. Nenhum é evidência independente de stakeholders. Derivação manual mantém proveniência e obrigações, sem implicar construção/execução de um transformer ou engine. Conversão de representação não cria uma derivação.

Mudança de contrato, permissão ou interação registra impacto sobre modelos, transformers, artefatos e cenários de verificação existentes. Se há apenas L1, registre o impacto e os trabalhos posteriores ainda não produzidos/avaliados.

<a id="model-17"></a>
### 17. Extensões

Membros desconhecidos de objetos conhecidos são recusados. Dados adicionais pertencem a `extensions`, com namespaces declarados. O tradutor os preserva estruturalmente e não interpreta seu significado. Não substituem conteúdo obrigatório nem alteram versão. Incapacidade de preservá-los exige recusa, não descarte.

<a id="model-18"></a>
### 18. Invariantes normativas

Conformidade abstrata exige as obrigações semânticas anteriores e as invariantes pertinentes. Os perfis entregues também exigem gramática, JSON Schema e validação. Aprovação mecânica não comprova verdade das afirmações ou conformidade OAL completa.

1. Modelo/versão e representação capaz de recuperar o conteúdo são identificados.
2. Conceitos, metadados, contratos, autorização, origens, aceite e distinções são recuperáveis sem adivinhação.
3. IDs são únicos e seguem a gramática.
4. Referências resolvem.
5. Conceitos têm posição editorial única, sem elementos desconhecidos.
6. Identidade, relações, transições e propriedade de validações resolvem.
7. Atores, entidades/validações, ferramentas/operações e chamadas dos casos resolvem.
8. RFs têm referências aos grafos do caso, com reciprocidade integral.
9. RNFs têm definição completa ou referência canônica válida, sem cadeias/autorreferência. Aplicabilidade/referências resolvem; origem, escopo e critério são identificados.
10. Interações apontam caso existente, RFs desse caso e recursos existentes.
11. Proprietários/chamadas dos grafos e extremos das arestas são válidos.
12. Recursos têm caminhos seguros e, na verificação completa, tamanho/hash corretos.
13. Figuras derivadas registram a impressão digital atual do grafo.
14. Texto inserido em um recurso da especificação também existe no conteúdo textual comum.
15. Registros textuais obrigatórios existem; ausência/nulo/vazio são distintos.
16. Representações carregam cada texto uma vez e toda a estrutura.

<a id="model-19"></a>
### 19. Fontes autoritativas e apresentação derivada

Atlas JSON tem texto e estrutura nos campos. Atlas Markdown/LaTeX têm texto nos registros visíveis marcados e dados restantes no apêndice estrutural.

Edição de texto autoritativo é importada. Edição isolada de resumo, topologia ou TikZ derivado gera diagnóstico para regeneração. Uma representação não pode esconder todo o texto em um payload e ignorar o corpo visível, nem preferir silenciosamente uma cópia antiga ao texto editado.

<a id="model-20"></a>
### 20. Obrigação de preservação

Conversão válida preserva todo o conteúdo: textos, títulos, notas, requisitos, contratos, exemplos, fontes literais, legendas, rótulos, comentários autorais classificados como conteúdo, metadados, tipos/valores, IDs/referências/ordens, grafos e recursos.

Conversão não resume, parafraseia, corrige, traduz idioma, reorganiza lógica ou atualiza requisitos. Consulte [contrato de preservação](#preservation). Bytes de JSON/Markdown/LaTeX podem diferir pela sintaxe; paginação de PDF está fora da reversibilidade.

<a id="model-21"></a>
### 21. Obrigações de uma implementação

A implementação preserva conceitos/relações, IDs/referências/ordens, texto exato/metadados, estrutura editorial, grafos/rótulos, catálogo e bytes de recursos no modo completo, distinções de ausência/nulo/vazio e natureza/revisão. Preserva extensões ou recusa o documento.

Ela declara o mapeamento semântico e a revisão da conformidade. Se declara compatibilidade com os perfis de interoperabilidade fornecidos, implementa e verifica caminho de ida/volta ao Atlas JSON no domínio declarado, sem alterar versão. Construções não suportadas e inconsistências recebem diagnóstico.

Um modelo pode implementar Atlas sem JSON: a declaração se apoia no contrato semântico, não na existência de arquivo JSON. Compatibilidade com o tradutor é outra declaração. Mapeamento parcial declara seu domínio; perda documentada não satisfaz uma promessa de preservação completa.

<a id="model-22"></a>
### 22. Fora do escopo

Esta versão não define expressões executáveis de validação, implementação concreta de ferramentas, layout de interface, rotas HTTP, esquema de banco, geração automática de requisitos, migração automática, importador genérico de Markdown/LaTeX nem garantia de que uma aplicação satisfaz RNFs. Tais responsabilidades pertencem a outros trabalhos/versões/camadas identificados.

<a id="graph-contract"></a>
## Estrutura e publicação dos grafos

As obrigações de grafos do modelo abstrato valem para todas as implementações. Os perfis fornecidos serializam `id`, `kind`, `owner`, `title`, `nodes`, `edges` e `notes` opcionais. O proprietário inclui `kind` e `id`, que devem resolver de forma consistente. Um grafo contém ao menos um nó e pode ter lista de arestas vazia.

| Elemento | Contrato do perfil |
| --- | --- |
| Nó | ID global, tipo suportado e rótulo; `call` opcional para validação, ferramenta, operação, caso ou entidade; blocos de entrada/saída/detalhes e referências a RFs. |
| Aresta | ID global, `from` e `to` no mesmo grafo; rótulo, blocos de condição, prioridade inteira e RFs opcionais. |
| Fluxo de validação | Referenciado por `flow` da validação e pertencente a ela. |
| Fluxo de caso | Principal/subfluxo referenciado por `flows.main`/`flows.subflows` e pertencente ao caso. |
| Grafo de estados/relações | Pode pertencer a uma entidade ou ao documento. |

Um grafo não pode pertencer a um elemento e ser indicado como fluxo próprio por outro. A ordem dos arrays de nós/arestas é preservada. Cada associação RF/grafo deve resolver e ser recíproca nos dois sentidos, dentro dos grafos do caso responsável.

Markdown mostra os registros autoritativos de texto dos nós/arestas e uma topologia gerada `DERIVED-GRAPH-<id>`. LaTeX emite uma região determinística `TIKZ-<graph-id>`: rótulos com quebra de linha, chaves curtas de aresta e uma legenda com os IDs/rótulos exatos. A listagem estruturada completa conserva nós, arestas e condições. A importação regenera o conteúdo derivado e recusa edições desatualizadas. Uma imagem de grafo identifica seu grafo e impressão digital conforme o contrato de recursos.

Fluxos de validação, principal, subfluxos e diagramas declarados de estados/relações podem aparecer no PDF. RNFs não têm fluxo separado, e ferramentas abstratas não expõem diagramas de algoritmos internos. O renderizador não é um mecanismo geral de layout. Grafos grandes podem ficar pequenos ao serem escalados; subfluxos significativos e revisão visual melhoram a publicação sem excluir conteúdo. O modelo não impõe limite de nós/arestas. Estender o vocabulário exige capacidade declarada do perfil, suporte correspondente no schema/renderizador e verificação.

<a id="resource-contract"></a>
## Catálogo de recursos e pacotes

Um recurso de especificação registra ID, `path` relativo ao pacote, tipo de mídia, tamanho em bytes e SHA-256; legenda/texto alternativo; `embedded_text` visível; caminho/revisão/ferramenta da fonte do desenho; variantes explícitas; e `source_uri`/`derived_from_graph` opcionais. `source_uri` pode ser texto ou `null`. Uma variante registra caminho, tipo de mídia, tamanho/hash, relação, caminho `derived_from` e produtor opcional. O original continua disponível junto das variantes.

- A validação resolve cada original/variante dentro da raiz de recursos declarada, abre o arquivo e compara tamanho e SHA-256. Caminho que escape da raiz, arquivo ausente, tamanho ou hash incorreto é erro.
- A conversão preserva o catálogo, sem copiar, reescrever, substituir, recomprimir ou baixar recursos. URLs permanecem referências. Recursos locais permitem conversão offline.
- `--no-check-resources` dispensa acesso/verificação dos bytes. Preserva o catálogo com garantia mais fraca, que deve ser explicitada.
- Texto visível em imagem também deve ocorrer no conteúdo textual comum, como legendas, texto alternativo ou rótulos de grafo. A falta dessa ocorrência gera `ATL-E-RESOURCE-TEXT`.
- Figura derivada de grafo declara `derived_from_graph`; `drawing_source.revision` é o SHA-256 do JSON canônico do grafo. Figura desatualizada gera `ATL-E-FIGURE-STALE`. Após mudar o grafo, reconstrua a figura e registre novo hash/impressão digital.
- LaTeX exige recurso PDF/PNG/JPEG compilável ou variante explícita. O SVG original continua disponível. Sem variante utilizável, a codificação relata `ATL-E-LATEX-RESOURCE`.

A raiz de recursos normalmente é a pasta do arquivo de entrada. Use `--resources CAMINHO` quando a localização da entrada/saída exigir outra raiz. Para deslocar a instância junto dos arquivos, use o comando separado `package`. Ele valida a origem, copia o documento e cada original/variante catalogado byte a byte, inclui o estilo quando disponível e valida a instância empacotada na nova raiz. Ele não converte a representação.

```bash
python translator/atlas_translate.py package examples/minimal/example.atlas.json --from json -o work/request-package
python translator/atlas_translate.py convert work/request-package/example.atlas.json --from json --to latex -o work/request-package/example.atlas.tex
```

Os binários não são embutidos em Atlas JSON/Markdown/LaTeX. SHA-256 é o algoritmo de hash suportado pelo catálogo. Criar variantes é tarefa de autoria/publicação, separada da conversão. As imagens de identidade na pasta `assets/` da raiz pertencem à documentação; só se tornam recursos de especificação quando uma instância as cataloga explicitamente.

LaTeX também aceita [estilos e imagens decorativas exclusivos da publicação](implementations/latex/README.pt-br.md#publication-style). Eles ficam fora dos registros autoritativos e do catálogo de recursos. O decodificador não lê nem executa o arquivo opcional de configuração `atlas-presentation.tex`, nem carrega suas imagens decorativas. A conversão não preserva a configuração visual personalizada, e `package` não descobre nem copia esses arquivos extras; mantenha-os separadamente ao reproduzir um PDF personalizado. Recursos obrigatórios do catálogo continuam sujeitos a todas as verificações acima.

<a id="preservation"></a>
## Preservação e igualdade

Uma conversão verificada satisfaz:

`decode_target(convert(source)).atlas == decode_source(source).atlas`

A comparação é recursiva e distingue tipos sobre **todo** o payload `atlas`. Preserva cada registro textual e seus metadados, identidade/versão/revisão, atores, conceitos, contratos, requisitos, aceite, topologia dos grafos, catálogo de recursos, fontes, decisões, histórico, configuração de apresentação e extensões. A ordem dos membros de objetos é irrelevante; a ordem dos arrays é conteúdo. O booleano `true` e o inteiro `1` são valores diferentes nesse contrato.

Metadados de transporte da representação ficam fora da igualdade do payload: `format` do envelope JSON, `$schema` opcional e metadados dos cabeçalhos de representação. Esses campos continuam sujeitos às próprias verificações de perfil/versão. Layout, substituição de fontes, paginação, estilos externos e arte puramente decorativa da publicação ficam fora da conversão reversível das fontes. Um arquivo opcional `atlas-presentation.tex` não pertence a `atlas`; ele não é serializado em JSON nem reconstruído a partir dele. Em contrapartida, configurações de apresentação efetivamente declaradas **dentro** de `atlas` continuam sendo conteúdo e são comparadas exatamente. Autores, versão do produtor declarada **dentro** de `atlas`, baselines de fontes, hashes de recursos e demais metadados autorais também continuam sendo conteúdo.

### Texto e dados exatos

- Use UTF-8 sem BOM; BOM é recusado. Leia e grave fontes sem tradução automática de quebras de linha.
- Preserve sequências Unicode, tabulações, espaços finais, LF/CRLF/CR e presença de quebra final. Não normalize Unicode, apare texto, altere caixa ou compacte espaços.
- Distinga membros ausentes, `null`, texto vazio e listas vazias.
- Preserve inteiros exatamente. Use texto para decimais; recuse números JSON de ponto flutuante e constantes não finitas. Recuse chaves duplicadas.
- Mantenha `meta`, `data` de exemplos de entidade e `extensions` opacos. Chaves literais `text`, `@text` e `id` nesses objetos são dados, não slots de prosa nem IDs globais de Atlas.

### Slots de texto e apresentação derivada

JSON carrega texto e estrutura diretamente. Markdown/LaTeX carregam cada texto declarado uma vez em registros visíveis marcados; um apêndice estrutural identificado contém os dados restantes e slots `@text`. Cada slot corresponde exatamente a um registro do corpo. Slots ausentes, duplicados, órfãos ou referenciados mais de uma vez são erros. Strings estruturais e dados opacos permanecem no apêndice. O apêndice não pode sobrepor a prosa visível nem fornecer outra cópia oculta dela.

Os codecs removem somente quebras/prefixos próprios dos delimitadores e revertem os escapes documentados. Edições autorais em registros de texto autoritativos são importadas. Resumos, topologia e TikZ são explicitamente derivados; a importação os regenera a partir da estrutura/texto atuais. Divergência gera `ATL-E-DERIVED-STALE` ou `ATL-E-TIKZ-STALE`. Mudar um grafo exige regenerar regiões derivadas e figuras associadas.

Uma conversão verificada bem-sucedida não resume, parafraseia, corrige, traduz idioma natural, reorganiza lógica ou migra versões. Perda de conteúdo da especificação, construção não suportada, referência inválida, marcador malformado, figura desatualizada ou recurso divergente é erro; não pode acompanhar uma declaração de preservação completa. `--no-verify` desativa a comparação após codificação naquela execução diagnóstica, e `--no-check-resources` enfraquece a verificação de recursos. Informe esses modos corretamente.

Igualdade estrutural/textual exata não prova que um desenho de fluxo exprime corretamente a prosa ou que um requisito é adequado. Revisão semântica e de publicação continuam necessárias.


<a id="examples"></a>
## Exemplos completos

| Exemplo | Finalidade de modelagem | Representações |
| --- | --- | --- |
| [Solicitação mínima](examples/minimal/README.pt-br.md) | Validação da entidade, um caso de solicitação, autorização e ilustrações empacotadas. | JSON, Markdown, LaTeX, PDF e recursos locais SVG/PNG. |
| [Composição](examples/composition/README.pt-br.md) | Consulta/criação/cancelamento de reserva, chamadas compostas, autorização e resultados explícitos de persistência. | JSON, Markdown, LaTeX e PDF. |
| [Quadro de tarefas](examples/task-board/README.pt-br.md) | Criar/concluir/listar, conflitos, vínculos requisito/fluxo/aceite e necessidades sintéticas. | JSON, Markdown, LaTeX, PDF, necessidades e rastreabilidade. |

São artefatos didáticos. Premissas e metas propostas são identificadas; não são evidência independente de stakeholders nem comportamento de uma aplicação executada. A instância JSON é a fonte de conteúdo mantida de cada exemplo. Reconstrua os formatos de leitura com `python examples/build.py`; use `--check` para verificar as representações existentes e `--pdf` para compilar PDFs. Consulte o [guia dos exemplos](examples/README.pt-br.md) para recursos e publicação.

<a id="ai-skill"></a>
## Skill para IA

Copie [skills/atlas-specs/](skills/atlas-specs/SKILL.md) como pasta completa. Suas instruções selecionam três fluxos: **criar/revisar**, **ler/auditar** e **converter/publicar**. Leia referências pertinentes sob demanda, comece pelo rascunho distribuído, distinga evidências de premissas e valide o artefato. Aprovação estrutural nunca autoriza o agente a fabricar requisitos ou declarar aprovação de stakeholders.

A skill inclui um runtime Python da mesma versão e `scripts/atlas_translate.py`. Esse launcher corresponde a `translator/atlas_translate.py`; o runtime é copiado do tradutor canônico, sem manter um segundo algoritmo. Para usar somente a skill, siga suas instruções de dependências/comandos a partir daquela pasta. O pacote distribuído está pronto para uso; consumi-lo não exige reconstrução.

### Para que serve `skills/build.py`

Este é um auxiliar de manutenção da edição. Uma skill independente precisa de cópias locais do material que consome, por isso o construtor as sincroniza a partir de uma única fonte mantida:

- o manual canônico do modelo em inglês e os três guias de representação, com links adaptados ao pacote;
- runtime do tradutor, launcher idêntico, JSON Schema, estilo LaTeX, documento inicial, lista de dependências e licença;
- um mapa de fontes com hashes das fontes e das cópias distribuídas, para identificar divergências.

Ele também sincroniza o schema e o estilo empacotados com o runtime canônico. Preserva `SKILL.md`, instruções de workflow e metadados do agente escritos manualmente. Execute `python skills/build.py` nesta edição após alterar uma fonte canônica, depois `python skills/build.py --check` para verificar a correspondência. A verificação é somente leitura e retorna falha quando há arquivos gerados desatualizados. Manter esse auxiliar evita atualizar cópias independentes manualmente; ele não é pré-requisito para criar ou converter uma especificação.

<a id="verification"></a>
## Verificação e publicação

No diretório desta edição:

```bash
python -m pip install -e ".[test]"
python -m pytest tests
python examples/build.py --check
python skills/build.py --check
```

As verificações cobrem carregamento estrito, schema/referências, identidade/propriedade, reciprocidade RF/grafo, RNFs compartilhados, texto exato/dados opacos, recursos, diagnósticos, empacotamento e igualdade após codificação. A portabilidade da edição e da skill é verificada separadamente das declarações semânticas. Uma coleção finita de testes estabelece comportamento somente nos casos exercitados; não é prova sobre toda entrada possível.

Para publicar PDFs, instale pdfLaTeX e os pacotes usados por [atlas.sty](implementations/latex/atlas.sty), depois execute `python examples/build.py --pdf`. O construtor faz duas passagens TeX em saída temporária e substitui uma publicação somente depois do sucesso. Inspecione páginas renderizadas, tabelas e legendas de grafos. A conversão não invoca TeX. Compilar com sucesso não estabelece qualidade visual, e o PDF não é aceito como entrada reversível.

O preâmbulo fornecido oferece caminho pdfLaTeX e suporte condicional a XeLaTeX/LuaLaTeX para outros sistemas de escrita. A evidência efetiva de compilação vale somente para o mecanismo exercitado; não cobre toda combinação de fontes/mecanismos. As imagens do projeto são mantidas separadamente na raiz do repositório. Com o repositório completo disponível, execute `python -m pip install ".[assets]"` e `python ../../assets/sources/render_images.py` a partir desta edição para renderizá-las; `assets/README.pt-br.md` na raiz documenta as dependências gráficas. Esse comando de apresentação não é necessário ao usar uma edição copiada.

A revisão semântica ainda deve avaliar objetivos/escopo, origens das afirmações, contexto do ator/autorização, efeitos/falhas completos, propriedade de regras, obrigações complementares, aceite/rastreabilidade e responsabilidade de fronteiras. Um contrato sobre comportamento de aplicação não é resultado observado em execução. A correspondência OAL abaixo define o escopo da declaração sobre o modelo.

<a id="conformance"></a>
<a id="oal-conformance"></a>
## Correspondência com OAL L1

### Baseline e objeto da declaração

| Item | Referência fixada |
| --- | --- |
| Edição OAL | **Stable-v1.0.0** |
| Repositório | [OAL — Open Analysis Layers](https://github.com/CodeVaultCommunity/OAL_OpenAnalysisLayers) |
| Commit | `ce225141686d4b6b3e46923866c97d84c031903f` |
| Fonte normativa | `versioning/Stable-v1.0.0/README.md`, [snapshot dos bytes recebidos](verification/oal/README.md.txt) |
| SHA-256 | `d6ad987008c200460af919eff3b03989dca5a3b0f7e14d7a9d5b4e67f598b2da` |
| Proveniência | Checkout local limpo; publicação remota pendente. [Identificação](verification/oal/baseline.json) e [revisão por cláusula](verification/OAL-CORRESPONDENCE.md). |
| Cláusulas | Regras numeradas entre camadas e UCS 1–10. A skill de contexto do OAL é informativa. |
| Modelo Atlas | **Atlas Specifications Stable-v1.0.0**, [modelo abstrato](#abstract-model) |
| Escopo declarado | Modelo abstrato reutilizável de especificação **UCS (L1)**, seus três perfis de representação e contrato de preservação. |
| Tipo de avaliação | Correspondência documental normativa e revisão explícita do escopo. Verificações executadas estão no [guia de verificação](#verification). |

O modelo estabelece as responsabilidades abaixo para seus artefatos. **Cada artefato ainda precisa satisfazê-las.** JSON Schema, ida e volta de conversão ou existência de exemplo não equivalem à aprovação semântica completa.

Atlas não declara ADMV (ADPM + ADVS), ADI, ADIB, todas as camadas OAL, realização dos Engines Needs-L1/L1-L2/L2-L3/L3-L4, nem construção/execução de transformers. O conversor muda representações do mesmo modelo. Um pacote pode referenciar ilustrações de fronteira sem declarar implementação L4.

### Correspondência UCS e evidência de revisão

“Estabelecido” indica uma exigência explícita do modelo Atlas. É uma avaliação do documento do modelo, não prova de que toda instância cumpre a exigência ou de que uma aplicação futura se comporta corretamente.

| Cláusula UCS | Obrigação e mapeamento em Atlas | Revisão da instância | Avaliação |
| --- | --- | --- | --- |
| **1 — Escopo** | §§1–4 e 14 exigem objetivos, fronteira do sistema, atores, participantes externos e contexto. Seções não prescrevem organização do código. | Recuperar objetivos, dentro/fora do escopo e participantes. | Estabelecido. |
| **2 — Casos** | §§6 e 10 exigem ID, objetivo, ator iniciador, permitidos, autorização, contexto do chamador, origem/confiança da resolução e política de autenticação. | Revisar chamadas diretas/compostas, participação anônima/de sistema explícita e recusa de contexto ausente/não resolvido/insuficiente/não autorizado, antes de efeitos protegidos. | Estabelecido; revisão semântica necessária. |
| **3 — Contratos** | §§9–11 exigem gatilho, entradas, condições, garantias, resultados, efeitos, alternativas/falhas e recusa observável. §11 classifica necessidades, restrições externas, escolhas de canal e ilustrações. | Revisar ramificações, garantias de falha/efeito e origens. Rotas/telas/codificações/protocolos introduzidos pela solução não são promovidos a requisitos L1. | Estabelecido; propostas de canal ficam fora da declaração L1. |
| **4 — Entidades e regras** | §§7–8 exigem significado, identidade, dados, relações, validade intrínseca, regras contextuais e casos responsáveis. Regras canônicas são referenciadas. | Identificar dono/aplicador de cada regra e distinguir entidade pronta, registro bruto e condição contextual. | Estabelecido. |
| **5 — Composição e dependências** | §§7 e 9–10 exigem dependências, capacidades, entradas/resultados, condições, garantias/falhas e autorização contextual, sem mecanismo técnico. | Revisar contrato do caso composto, preservação do contexto e operações consumidas. | Estabelecido. A restrição interna de ferramentas é local de Atlas. |
| **6 — Obrigações complementares** | §10.2 exige origem individual, escopo, aplicabilidade, critério verificável e referências para obrigações pertinentes de persistência, segurança, isolamento, observabilidade, desempenho, acessibilidade etc. | Revisar origem de cada RNF; distinguir meta confirmada de exemplo/proposta. Escolhas de canal pertencem a L4. | Estabelecido; pertinência e suficiência dependem de revisão. |
| **7 — Aceite e vínculos** | §§6 e 10 exigem aceite e vínculos a necessidades/fontes, atores, entidades, regras e dependências. Critérios compartilhados têm definição única, escopo e casos afetados. | Revisar critérios/vínculos e conservar IDs ao produzir camadas seguintes. | Estabelecido em L1; correspondência posterior não demonstrada aqui. |
| **8 — Consistência e evolução** | §§3, 5–6 e 15–17 exigem definições canônicas, IDs/histórico, fontes e distinções entre fatos, requisitos, inferências, premissas, decisões, pendências e revisão. | Inspecionar referências e mudanças/impactos. Estado aprovado não transforma premissa em fato. | Estabelecido. |
| **9 — Domínios (recomendação)** | §§7 e 14 permitem agrupar entidades/casos em seções sem duplicação. | Quando adotados, revisar limites e associações. | Organização opcional suportada; objeto de domínio não obrigatório. |
| **10 — Exemplos** | §§8 e 12–13 e a [coleção de exemplos](examples/README.pt-br.md) mantêm exemplos subordinados a regras e aceite explícitos. | Conferir concordância com regras; imagem não preenche requisito ausente e exemplo não substitui cenário ADVS. | Estabelecido; validade dos exemplos é avaliada separadamente. |

### Regras entre camadas que afetam este modelo L1

| Regra OAL | Tratamento Atlas | Limite da declaração |
| --- | --- | --- |
| **1 — Modelos e artefatos** | §2 distingue metamodelo OAL, abstração Atlas, modelo implementador, representação, instância e publicação. | Formato/quantidade de arquivos não contam modelos/camadas. Não há camada Needs. |
| **2 — Derivações responsáveis** | §16 exige modelos/versões de origem/destino, baselines, pessoa nominal, escopo e decisões **quando se declara derivação Needs-to-L1**. Prosa claramente identificada é permitida. | Aplica-se à entrada em L1, inclusive manual. Autoria não supre proveniência. Necessidades reconstruídas/sintéticas são rotuladas. Codec não implica derivação. |
| **3 — Identidade de caso** | §§6 e 10 preservam IDs e vínculos de aceite. | Correspondências ADPM/ADVS/ADI só podem ser verificadas com tais artefatos. Ausência fora do escopo não significa aprovação. |
| **4 — Mudanças e declarações** | §§6 e 16 exigem registro de mudanças e impacto aplicável. [Versionamento](#versioning) separa migração de conversão. | Alteração de origem não revalida silenciosamente artefatos derivados. |
| **5 — Pessoas e atores** | §10 distingue ator, chamador concreto, contexto, autenticação/autorização e responsável da derivação. | Não inventa cargo, classe, campos fixos ou tecnologia de autenticação obrigatórios. |
| **6 — Conformidade** | Documento identifica edição, modelo/versão, responsabilidade, escopo/evidência. O [guia de implementações](#implementations) distingue conformidade abstrata, validade de perfil e interoperabilidade. | Conformidade de modelo, de artefato, cobertura de camadas e cobertura completa permanecem declarações distintas. |
| **7 — Engines** | Nenhum engine OAL é declarado. Codecs atuam dentro do mesmo modelo. | Testes de codec não demonstram construção/execução de transformer entre camadas. |
| **8 — Operações distintas** | [Preservação](#preservation) define igualdade exata do conteúdo. Outro modelo precisa de mapeamento próprio; derivação tem obrigações específicas. | Perda documentada não satisfaz contrato sem perdas; dois modelos L1 não implicam tradutor universal. |
| **9 — Pacotes combinados** | Referências/ilustrações mantêm responsabilidades identificadas. | Coexistência de arquivos não demonstra engine, transformer ou composição. |

### Avaliação de um artefato específico

A avaliação possui duas partes:

1. **Verificação mecânica do perfil:** sintaxe/esquema, IDs, referências, propriedade, reciprocidade RF/grafo, vínculos de RNF, slots de texto, hashes/atualidade de recursos e igualdade do payload recuperado. Registrar comando, versão, entrada e resultado efetivos.
2. **Revisão semântica L1:** escopo/objetivos, natureza/origem das afirmações, ator iniciador/contexto, comportamento/falhas, propriedade de regras, obrigações adequadas, aceite/rastreabilidade e responsabilidade de fronteiras. Condições pendentes devem ser nomeadas.

Distinguir estados **não especificado**, **não avaliado**, **não demonstrado**, **inconclusivo**, **não conforme** e **satisfeito no escopo declarado**. Os quatro primeiros não são aprovações. Violação conhecida difere de avaliação ausente.

O [quadro de tarefas](examples/task-board/example.atlas.json) demonstra criar, concluir e listar. É um artefato didático, sem alegação de evidência independente de stakeholders ou comportamento de aplicação implantada. Os exemplos mínimo/de composição são outras referências de modelagem e codec. Use os comandos de verificação acima para reproduzir as verificações mecânicas.

### Escolhas locais de Atlas

Não são exigências universais de OAL: três perfis com JSON intermediário; gramática/globalidade de IDs; RF/RNF em fichas de caso e cobertura recíproca por grafo; texto exato com slots/apêndices; recursos locais com variantes/hashes; estrutura de repositório, skills e PDF.

A revisão documental sustenta o escopo declarado do modelo. Não é teorema universal, auditoria de segurança em execução ou declaração de que trabalhos posteriores não especificados estão concluídos.


[Política de superfície estável e matriz de compatibilidade](COMPATIBILITY.pt-br.md).

<a id="versioning"></a>
## Identidades de versão e evolução

| Identidade | Esta edição | Significado |
| --- | --- | --- |
| Modelo Atlas | `Stable-v1.0.0` | Contrato semântico abstrato. |
| Perfis de representação | `Stable-v1.0.0` | Gramáticas JSON, Markdown e LaTeX. |
| Pacote Python | `atlas-spec` / `1.0.0` | Implementação do tradutor e CLI. |
| Revisão do documento | Própria do artefato | Evolução do conteúdo autoral, independente da edição. |
| Referência OAL | `Stable-v1.0.0` | Baseline externo do metamodelo. |

As [notas da versão](#release-notes) descrevem esta edição Stable. A conversão de representação não migra conteúdo de protótipos anteriores nem altera o modelo selecionado.

Adaptadores selecionam representação/versão explicitamente. Envelope/cabeçalho e versão do conteúdo devem concordar com o perfil suportado. Versões ou construções não suportadas são recusadas. Conversão preserva `spec_version`, `profile_version`, `translator_version`, revisão e histórico; não troca os rótulos de conteúdo antigo pela versão da ferramenta executada.

Um elemento mantém seu ID enquanto conserva a identidade. Substituição, exclusão ou divisão registra ID anterior, sucessores pertinentes, motivo e referências afetadas; atualize essas referências antes de aceitar o artefato. Mudanças semânticas e de serialização são avaliadas separadamente. Uma migração futura deve identificar baselines, escopo, responsável e mudanças intencionais de conteúdo, depois reconstruir e verificar representações/recursos. É uma operação autoral separada, sem efeito implícito do codec.

### Organização da edição

| Caminho | Responsabilidade |
| --- | --- |
| `README.md` / `README.pt-br.md` | Contrato do modelo, regras comuns e manual completo da edição. |
| `implementations/` | Gramáticas, JSON Schema, documentos iniciais equivalentes e estilo LaTeX. |
| `translator/` | Runtime canônico e launcher direto. |
| `tests/` / `pyproject.toml` | Testes, dependências e configuração do pacote da edição. |
| `examples/` | Fontes JSON mantidas, formatos de leitura e publicações PDF. |
| `skills/` | Skill portátil e construtor local do pacote. |
| `LICENSE` | Licença que acompanha a edição independente. |

Os recursos de apresentação compartilhados ficam na pasta `assets/` da raiz do repositório, fora desta edição. Recursos pertencentes a um exemplo permanecem dentro dele. Essa distinção mantém a edição operacional completa e portátil, enquanto a raiz reúne as ilustrações do projeto.

<a id="authorship"></a>
## Autoria e licença

Atlas Specifications foi idealizado e desenvolvido por **Douglas de Oliveira Alkimim**. Distribuído sob a [licença MIT](LICENSE).

[GitHub](https://github.com/douglas-alkimim) · [LinkedIn](https://www.linkedin.com/in/douglas-alkimim/)
