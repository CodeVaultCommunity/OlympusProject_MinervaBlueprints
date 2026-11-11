# Minerva Blueprints · Stable-v1.0.0

O Minerva é a camada L2 orientada à geração entre o Atlas Specifications e o
código Vulcan. Sua fonte semântica é uma **árvore distribuída de módulos
Markdown estritos com a forma da futura base de código**. Não é um manual
voltado a humanos, um blueprint YAML central nem um apêndice do Atlas.

## Contrato do ecossistema

- O Atlas Stable-v1.1.0 fornece todo o significado L1 por
  `atlas-normalized/1.1.0`.
- Cada conceito Atlas é preservado exatamente no bloco controlado
  `atlas-source-json` do módulo que o possui.
- `minerva-design-json` acrescenta arquivo/símbolo alvo, classes, métodos,
  parâmetros, ordem de chamadas, colaboradores, algoritmos, falhas, efeitos,
  injeção de dependência e testes.
- Ferramentas abstratas permanecem protocolos. Cada uma possui ao menos um
  **projeto** de ferramenta concreta, sem implementação executável no Minerva.
- Boundary significa apenas adaptador de interação que expõe casos de uso.
  Cenários de teste usam `observation_points`.
- Grafos de casos de uso e validações de entidade são preservados e também
  indexados no grafo de conhecimento.

`minerva.project.yaml` serve apenas para descoberta. A autoridade semântica
está nos módulos Markdown listados. A validação cobre hash da fonte, cobertura
total, caminhos seguros, alvos de geração únicos, linhagem de ferramentas,
terminologia de Boundary e completude do grafo.

Veja o [manual canônico em inglês](README.md) para formato, comandos e árvore.

Distribuído sob a [licença MIT](LICENSE).
