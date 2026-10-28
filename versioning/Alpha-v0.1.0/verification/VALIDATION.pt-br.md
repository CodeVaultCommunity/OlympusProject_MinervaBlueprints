# Validação observada e limites

[English](VALIDATION.md) · [Comandos, ambiente e hashes](evidence/checks.json) · [Revisão da fonte](reviews/contract-review.pt-br.md)

A Alpha-v0.1.0 revisada e não publicada foi verificada em **Windows / CPython 3.12.14**. Os resultados dizem respeito às ferramentas, documentos de origem e empacotamento. Não são execuções dos cenários de domínio nem aceite do responsável.

| Verificação | Resultado observado | Evidência |
| --- | --- | --- |
| Regressões da edição | 50 testes aprovados | [Saída](evidence/validator-tests.stderr.txt) |
| Manutenção do repositório | 33 testes aprovados | [Saída](evidence/repository-tests.stdout.txt) |
| Exemplos Minerva | Três exemplos principais e dois snapshots de revisão aprovados; starter conferido somente na estrutura | [Relatórios](evidence/model-examples.stdout.txt) |
| Contraexemplos | 12 resultados esperados correspondentes | [Relatórios](evidence/counterexamples.stdout.txt) |
| Entradas Atlas originais | Cinco fontes aceitas pela ferramenta oficial fixada, com conferência de recursos | [Comandos e saídas individuais](evidence/checks.json) |
| Edição isolada | Exemplos e contraexemplos aprovados em cópia somente da edição, com diretório de trabalho externo | [Exemplos](evidence/isolated-examples.stdout.txt) · [Fixtures](evidence/isolated-counterexamples.stdout.txt) |
| Pacote Python wheel | Construído sem isolamento de build, instalado sem dependências em destino novo; schema empacotado e validação mínima aprovados | [Build](evidence/wheel-build.stdout.txt) · [Conferência](evidence/wheel-smoke.stdout.txt) |
| Ilustrações | Oito pares PNG/SVG conferidos; dois diagramas de modelo alterados revisados visualmente | [Registro](evidence/artwork.json) |

Dependências de execução: PyYAML 6.0.3 e jsonschema 4.25.1. Testes da raiz: pytest 9.2.0. Build: build 1.6.1, setuptools 84.2.1 e wheel 0.48.0. Versões completas, comandos, horários, códigos de saída e stdout/stderr foram registrados juntos. As dependências já existiam no teste do wheel; isso não demonstra instalação nova pela rede. A cópia isolada não dispunha de recursos do repositório pai.

As regressões exercitam YAML restrito, raízes portáveis, fontes opacas, hashes, espaços de identidade do catálogo, origens tipadas, atores permitidos por caso, tipo/propriedade das invariantes, cardinalidade caso/teste, obrigações compartilhadas canônicas, autorização na composição, integridade/ciclos dos grafos, estados incompletos/não suportados e inspeção opcional de símbolos Python sem importar módulos. Uma fonte binária identificada por um modelo diferente do Atlas exercita a ausência de reader Atlas.

## Reproduzir

A partir da edição, com dependências instaladas externamente:

```bash
python run_examples.py --test
python run_examples.py --all --json
python tests/fixtures/counterexamples/check.py --json
```

A partir da raiz:

```bash
python scripts/check_repository.py
python -m pytest scripts/tests
python scripts/content_inventory.py --check
```

O suporte declarado é Python 3.11+, mas esta execução observou somente 3.12.14 no Windows. A matriz CI Linux/Windows configurada não é apresentada como executada. A validação estabelece declarações suportadas e consistência selecionada, não fidelidade da transcrição do catálogo ou equivalência semântica. A revisão da fonte está documentada separadamente. `--verify-code` confere bytes/símbolos selecionados; não importa código nem executa a aplicação. Todos os cenários de domínio dos exemplos continuam planejados, com listas de execução vazias. A ambiguidade de medição do cancelamento permanece explícita na revisão dos contratos.
