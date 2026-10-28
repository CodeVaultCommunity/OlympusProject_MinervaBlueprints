# Correspondência com o L2 do OAL

[English](OAL-ALIGNMENT.md) · Português brasileiro · [Conformidade](../README.pt-br.md#conformance)

A base autoritativa é o [texto congelado OAL Stable-v1.0.0](../verification/sources/oal/README.pt-br.md.txt), com commit e hashes em [source-baselines.json](../verification/source-baselines.json). O mapeamento parafraseia responsabilidades e informa o que esta candidata estabelece. É um argumento de conformidade inspecionável, sem aprovação dos mantenedores OAL ou prova automática.

## ADMV como um único L2

Minerva define uma instância de programa e verificação com dois componentes distinguíveis. O schema exige ambos; instâncias revisadas exigem escopo de origem selecionado não vazio. Fichas isoladas retornam `source_record_only`. Rascunho retorna inconclusivo na consistência completa. Isso estabelece como expressar L2 integrado; a cobertura semântica depende da revisão da instância.

## Assuntos ADPM

| Assunto OAL ADPM | Regras e construções Minerva | Apoio automático / revisão restante |
| --- | --- | --- |
| 1. Responsabilidades | MIN-004–008; casos, entidades, ferramentas e vínculos de fontes | Referências tipadas e IDs próprios; revisão do mapeamento L3 fiel |
| 2. Casos | MIN-005, 012–013; comportamento, permissão e dependências | Correspondência de origem e contexto transmitido; algoritmo e autorização requerem revisão |
| 3. Entidades | MIN-007; invariantes com responsável, construção e dependências | Dependências para caso/ferramenta rejeitadas; distribuição semântica revisada |
| 4. Ferramentas e localização da validação | MIN-008–009; garantias, entidade pronta e condições contextuais | Revalidação declarada rejeitada; equivalências semânticas não são detectadas automaticamente |
| 5. Composição | MIN-011; colaboradores recebidos, seleção e propriedade | Referências conferidas; completude e buscas ocultas revisadas |
| 6. Persistência | MIN-010; capacidades, falhas, garantias e condições contextuais | Contratos textuais; concorrência/atomicidade e resultados desconhecidos exigem evidência |
| 7. Autorização | MIN-012; entrada de contexto, confiança, quatro recusas e política anterior a efeitos | Entradas/atores/categorias conferidos; confiança e ordem de execução revisadas/testadas |
| 8. Representação fiel | MIN-014–015, 024; texto semântico, pseudocódigo e grafos | Schema/topologia; recuperabilidade e equivalência de algoritmo revisadas |
| 9. Domínios opcionais | MIN-011; domínios e vínculos recíprocos | Referências conferidas; não se infere agrupamento universal ou acesso concedido |
| 10. Tempo de vida | MIN-011; escopo, duração e propriedade na composição | Elementos referenciados conferidos; adequação do ciclo de vida é decisão do modelo |

## Assuntos ADVS

| Assunto OAL ADVS | Regras e construções Minerva | Apoio automático / revisão restante |
| --- | --- | --- |
| 1. Um teste comportamental por caso UCS | MIN-017; caso/origem e baseline selecionada | Exatamente um teste lógico direto por caso; quantidade de arquivos não define cardinalidade |
| 2. Contratos de cenários/subtestes | MIN-018; preparação, contexto, ação, resultados/efeitos, limite/configuração | Estrutura obrigatória; oráculo e preparação suficientes requerem revisão |
| 3. Permissões | MIN-020; acesso permitido/negado e anonimato explícito aplicável | Presença de categorias; ausência de efeitos exige observação real |
| 4. Falhas e limites | MIN-021, 023; alternativas, falhas, riscos e obrigações de canal | Vínculos declarados conferidos; cobertura completa de riscos não é inferida |
| 5. Rastro e estado | MIN-019, 022; critérios, apoio compartilhado, realização e execução | Propriedade/cobertura/reciprocidade/evidência; veracidade e amplitude dos relatórios revisadas |

## Camadas adjacentes e procedência

O [modelo Atlas congelado](../verification/sources/atlas/README.pt-br.md.txt) descreve L1. Minerva consome uma fonte fixada por adaptador explícito. Não reescreve necessidades, atores ou aceite da origem, não traduz todo modelo L1 e não afirma realizar processo de derivação OAL por possuir um vínculo manual.

Vulcan é modelo de organização/realização L3. Caminhos das fichas relacionam significado L2 a artefatos L3; não tornam cada ficha um modelo de programa completo. Decisões de implementação e evidências de execução continuam atribuíveis à realização. Decisões de interação permanecem L4 mesmo quando o documento é armazenado próximo de L2/L3 em `docs/Shared/`.

A fonte TaskBoard desta edição é uma reconstrução didática identificada separadamente e compatível com o demo companheiro. Normalização de título, ID atribuído pela aplicação, lista em ordem de inserção, persistência local e conclusão idempotente são seus contratos. O outro TaskBoard publicado pelo Atlas possui outras obrigações. Nome de produto em comum não constitui mapeamento de equivalência.

## Limites da alegação

Uma execução bem-sucedida estabelece somente as verificações suportadas na configuração declarada. Não estabelece suficiência semântica, validação L1 completa, correção do código, comportamento ambiental amplo ou certificação. O [registro de validação](../verification/VALIDATION.pt-br.md) informa comandos e limites efetivos. A revisão pendente do responsável permanece explícita na procedência da edição e das instâncias.
