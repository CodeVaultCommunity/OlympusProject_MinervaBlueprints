# Preparar uma distribuição Minerva Blueprints

[English](releasing.md) · [Início](../README.pt-br.md)

## Finalizar a edição

Selecione Alpha-v0.1.0. Conclua fontes, tradução, exemplos, recursos e evidências. Execute os comandos do manual de edição e os testes de scripts da raiz. Registre resultados reais e limites; uma configuração de CI não demonstra sua execução. Inspecione imagens alteradas. Mantenha ambientes e temporários fora da árvore a distribuir.

## Gerar o inventário único

CONTENT-SHA256.json é o inventário ativo da distribuição. Registra algoritmo SHA-256, minerva_edition igual a CITATION.cff, escopo, exclusão de si mesmo, caminho POSIX, tamanho em bytes e hash. Abrange todos os arquivos versionados destinados à entrega. Os snapshots de fontes e seus mapas registram proveniência e não substituem esse inventário.

Prepare explicitamente as adições, mudanças e remoções no índice Git. O gerador lê os caminhos do índice e os bytes atuais sem normalização de fim de linha. Gere o inventário por último:

```bash
python -m pip install -r scripts/requirements-dev.txt
python scripts/check_repository.py
python -m pytest scripts/tests
python scripts/content_inventory.py --write
python scripts/content_inventory.py --check
git add -- CONTENT-SHA256.json
```

Confirme que os bytes correspondem aos blobs preparados e crie o commit local. Não coloque no próprio inventário seu hash, o hash do ZIP final ou o identificador do commit que o contém.

## Empacotar e auditar

```bash
python scripts/build_distribution.py --output /absolute/path/OlympusProject_MinervaBlueprints_Alpha-v0.1.0.zip
python scripts/check_archive.py /absolute/path/OlympusProject_MinervaBlueprints_Alpha-v0.1.0.zip
```

O gerador exige conteúdo versionado limpo, inventário válido e ausência de caches versionados. O ZIP contém um repositório em OlympusProject_MinervaBlueprints/, sem .git. Extraia o ZIP em diretório vazio e execute scripts/check_archive.py contra essa raiz antes de instalar dependências ou criar caches. O auditor usa a biblioteca padrão e detecta arquivos ausentes, adicionais, duplicados e alterados.

Mantenha externamente um recibo com commit, hash e tamanho do ZIP e resultados da auditoria. Para testar a edição isolada, copie somente versioning/Alpha-v0.1.0/ e use um ambiente externo. Publicação no GitHub depende de uma ação específica; preparar e entregar o ZIP não cria push, tag ou release remoto.
