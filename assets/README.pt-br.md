# Assets — Minerva Blueprints

[English](README.md)

**Olympus Project · OAL L2 · ADMV (ADPM + ADVS) · Alpha-v0.1.0**

Os headers e os diagramas seguem a composição visual do Atlas Specifications: azul/teal, caixas claras e navy, setas explícitas e fundo transparente nos diagramas. As duas línguas expressam o mesmo conteúdo. As imagens explicam o modelo; os requisitos e contratos permanecem definidos na documentação da edição.

## Inventário

| PNG | Fonte editável | Dimensões | Conteúdo |
|---|---|---|---|
| [minerva-banner-pt-br.png](minerva-banner-pt-br.png) | [SVG](sources/minerva-banner-pt-br.svg) | 1600 × 534 | Identidade do projeto, camada e versão. Arte apenas decorativa. |
| [minerva-oal-position-pt-br.png](minerva-oal-position-pt-br.png) | [SVG](sources/minerva-oal-position-pt-br.svg) | 1400 × 1080 | Posição no OAL, partes do modelo e artefatos concretos. |
| [minerva-model-pt-br.png](minerva-model-pt-br.png) | [SVG](sources/minerva-model-pt-br.svg) | 1400 × 1180 | ADPM, ADVS e perfil de espelho YAML em L2. |
| [minerva-workflow-pt-br.png](minerva-workflow-pt-br.png) | [SVG](sources/minerva-workflow-pt-br.svg) | 1400 × 1230 | Entradas versionadas, revisão, realização e retorno das evidências. |

Cada arquivo tem uma versão `-en` e outra `-pt-br`. Os headers têm cantos transparentes e corpo opaco. Os diagramas têm canvas transparente e caixas opacas para leitura em temas claros e escuros. Todos os SVGs são independentes e contêm `title` e `desc`; nos headers, as imagens raster estão embutidas.

## Semântica e responsabilidade

O espelho por arquivo pertence a `docs/L2_MinervaBlueprints/apps/`. L3 documenta inventário, perfis, composição, execução, integrações concretas e evidências em `docs/L3_Vulcan/`. `docs/` é uma organização recomendada; criam-se apenas as pastas dos modelos adotados. `Shared/` é apoio transversal, sem constituir nova camada OAL. Conteúdos de interação preservam sua classificação L4 mesmo quando referenciados por L2 ou L3.

No perfil Minerva desta edição, `source.state` distingue `planned` de `observed`; `document.nature` distingue `designed`, `reconstructed` e `mixed`. Uma observação de fonte não comprova execução. As setas descrevem relações e etapas de trabalho com revisão; não prometem geração automática. Bibliotecas auxiliares não são obrigatórias para a arquitetura.

## Reprodução

Use Python 3.10+, CairoSVG 2.8.2, suas bibliotecas de sistema Cairo e as fontes **DejaVu Sans** e **DejaVu Sans Mono**. Essas dependências servem apenas para reproduzir imagens, sem se tornarem dependências do modelo ou de aplicativos Vulcan.

```sh
python -m pip install CairoSVG==2.8.2
python assets/sources/render_images.py
```

O comando parte da raiz do repositório; o script também aceita execução por caminho absoluto a partir de outro diretório. Ele usa somente arquivos locais, regrava oito SVGs e oito PNGs e copia os ícones originais para exibição. Não chama serviços de geração de imagens. Edite os rótulos e a geometria no script para manter a reprodução coerente; uma edição manual de SVG será substituída na próxima execução.

O texto permanece editável. As fontes não estão embutidas, portanto devem ser instaladas para reproduzir a composição. Versões distintas de Cairo e das fontes podem alterar pixels; não se promete identidade binária entre ambientes.

## Originais, proveniência e atribuição

- Os ícones fornecidos para o projeto estão em `sources/minerva-icon-original.png` e `sources/olympus-icon-original.png`. As cópias de exibição e os payloads embutidos nos SVGs preservam os bytes originais.
- A arte decorativa está em `sources/minerva-hero-art.png`. O [registro do prompt](sources/ARTWORK-PROMPT.md) contém o pedido exato, a procedência e os limites de reprodução.
- Os diagramas são geometria e texto SVG, criados a partir da documentação do modelo. A arte gerada não é usada como fonte de informação técnica.
- Composição visual e helpers SVG adaptados de [Atlas Specifications · Stable-v1.0.0](https://github.com/CodeVaultCommunity/OlympusProject_AtlasSpecifications/tree/b5941830515d9968bb7f313301f1abe25fb6f8aa/assets). Copyright (c) 2026 Douglas de Oliveira Alkimim. O [aviso MIT original](sources/ATLAS-LICENSE.txt) foi preservado.
- [asset-metadata.json](asset-metadata.json) registra nomes, dimensões, hashes SHA-256, revisão de origem e verificações. A licença da distribuição está no [LICENSE](../LICENSE).

## Revisão

Foram verificadas a decodificação completa dos PNGs, a transparência, a integridade dos originais e a independência dos SVGs. A revisão visual cobre cada header e diagrama nos dois idiomas, incluindo textos, conectores, cortes e legibilidade. Essa revisão verifica a apresentação dos assets, não certifica a conformidade de qualquer aplicativo.
