# Evidência de validação e limites

[English](VALIDATION.md) · Português brasileiro · [Guia](../README.pt-br.md#verification)

Este registro descreve **verificações observadas da candidata**, sem afirmar execução de todo cenário ou aprovação do responsável. Comandos, horários, ambiente e hashes estão em [observed/checks.json](observed/checks.json), com stdout/stderr ao lado. A [revisão contratual](CONTRACT-REVIEW.pt-br.md) examina contratos didáticos e vínculos de evidência separadamente.

## Resultados observados

| Verificação | Resultado observado | Evidência |
| --- | --- | --- |
| Regressões do validador | **44 testes passaram** em CPython 3.12.14 / Linux | [Saída](observed/validator-tests.stderr.txt) · [comandos/ambiente](observed/checks.json) |
| Exemplos normais | Mínimo, TaskBoard completo, planejado e legado passaram no escopo declarado | [Relatórios](observed/model-examples.stdout.txt) |
| Starter em rascunho | Passou somente na estrutura; resultado inconclusivo normal testado separadamente | [Relatórios](observed/model-examples.stdout.txt) · suíte |
| Fixtures públicas | **13 resultados esperados corresponderam**, incluindo inválidos, não suportado, inconclusivo e ciclo válido | [Saída](observed/counterexamples.stdout.txt) |
| Edição isolada | Cópia somente desta edição executou exemplos/fixtures a partir de diretório externo | [Isolamento](observed/isolation.json) |
| Wheel Python | Build offline, instalação temporária e validação mínima pelo pacote instalado passaram; schema incluído | [Empacotamento](packaging.json) |

O suporte declarado é Python 3.11+; a evidência exercita **somente 3.12.14**. Utilizamos PyYAML 6.0.3 e jsonschema 4.25.1. A suíte unittest não exige pytest; verificações de distribuição usam seu ambiente registrado. Workflow configurado não demonstra execução no GitHub Actions.

## O que as regressões estabelecem

Os testes exercitam chaves duplicadas, tags/aliases proibidos, escalares determinísticos, versões/hashes da origem, vínculos caso/teste ausentes/duplicados, propriedade/cobertura de critérios, referências tipadas, validação canônica, categorias de contexto, composição, arestas/alcançabilidade/ciclos, grafos locais, raízes alternativas, critérios compartilhados, divergência, estados de rascunho/erro/não suportado e JSON da CLI.

Uma regressão rejeita `Expected.testRun` quando o método pertence apenas a `Other`; a inspeção segue propriedade léxica qualificada. Outra fornece arquivo cujo código de primeiro nível lançaria exceção ao importar e demonstra inspeção sem importação/execução. As verificações cobrem o **validador**, não o domínio; a quantidade não altera as três identidades comportamentais diretamente vinculadas do TaskBoard.

## Observação do empacotamento

A tentativa padrão de build isolado não conseguiu obter setuptools porque o ambiente bloqueou a conexão de rede/proxy. O build bem-sucedido utilizou setuptools 84.1.0 e wheel 0.48.0 já disponíveis com `--no-build-isolation`; o wheel foi instalado em destino temporário novo sem baixar dependências de execução. A validação carregou `minerva_blueprints` desse destino e localizou o schema empacotado.

Isso sustenta empacotamento/instalação local com dependências disponíveis. Não afirma instalação nova pela rede, outro sistema ou todas as versões Python. Produtos de build, caches e instalações temporárias não integram a distribuição de fontes.

## Reproduzir

Nesta edição, com dependências declaradas instaladas:

```bash
python run_examples.py --all --json
python examples/counterexamples/check.py --json
python run_examples.py --test
```

Para reproduzir o wheel offline, disponibilize previamente backend setuptools compatível e ferramentas wheel:

```bash
python -m pip wheel . --no-deps --no-build-isolation --wheel-dir /tmp/minerva-wheel
```

`python -m pip install .` pode precisar de rede para dependências de build/execução. O launcher direto também utiliza ambientes que já satisfaçam `requirements.txt`.

## Limites e interpretação

- Aprovação estabelece estrutura suportada, vínculos e consistência selecionada. Correção de oráculos, suficiência completa, equivalência de algoritmo e conformidade semântica exigem revisão.
- O exemplo completo contém fichas observadas sem código da aplicação. Alegar correspondência atual exige `--verify-code` no ecossistema companheiro. Ausência retorna inconclusivo quando a inspeção é solicitada.
- A inspeção confere hashes, símbolos léxicos Python e cobertura declarada. Não executa aplicativos/testes, prova transações, valida autenticação de produção ou inspeciona todas as linguagens.
- Referências a testes não são resultados. `advs.executions` está vazio nos blueprints. Relatórios reais pertencem à realização/configuração avaliadas.
- O leitor L1 é o adaptador Atlas Stable JSON escolhido, não um mecanismo geral de derivação ou validador Atlas completo.
- Fontes, correções, autoridade de revisão e limites pendentes permanecem visíveis. A evidência não constitui certificação geral OAL ou aprovação do responsável.
