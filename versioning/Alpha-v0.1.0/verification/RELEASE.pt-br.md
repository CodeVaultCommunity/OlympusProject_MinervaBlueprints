# Relatório da entrega — Minerva Blueprints Alpha-v0.1.0

[English](RELEASE.md) · [Manual](../README.md) · [Requirements](REQUIREMENTS.md) · [Contract review](CONTRACT-REVIEW.md) · [Migration](MIGRATION.md)

**As verificações listadas abaixo passaram no ambiente registrado.** Esta é uma entrega Alpha para revisão do modelo, dos formatos e dos exemplos. Ela distingue validação documental, avaliação estrutural, revisão semântica assistida por IA e execução observada. Não afirma aprovação do responsável pelo projeto ou certificação geral de conformidade OAL.

## Resultados observados

| Verificação | Resultado e escopo |
| --- | --- |
| Validador Minerva | 44 testes passaram; nenhum erro ou falha. |
| Fixtures públicas | 13 resultados coincidiram com a expectativa, incluindo casos inválidos, incompletos e o controle de ciclo legítimo. |
| Exemplos | Quatro exemplos passaram na validação do modelo; o starter passou somente no nível estrutural declarado. |
| Inspeção de código | A correspondência das 15 fontes observadas é verificada na realização companheira Vulcan. O pacote Minerva sozinho não contém esses aplicativos. |
| Ferramentas de distribuição | 33 testes passaram para inventário, conteúdo exato e verificação dos pacotes. |
| Isolamento da edição | Passou: somente a pasta da edição foi copiada; comandos foram invocados de fora dela com ambiente Python externo. |
| Fonte Atlas | Instância própria validada pelo tradutor oficial Atlas Stable-v1.0.0 fixado por commit. |
| Arte e integridade visual | Oito renders e oito SVGs por projeto; ícones preservados byte a byte; todas as imagens revisadas visualmente e metadados/hashes conferidos. |

A contagem é de métodos de teste, não de cada subcaso ou asserção. As 33 verificações da distribuição são a suíte de manutenção de cada repositório; não são casos de domínio adicionais.

## Ambiente e reprodução

- Python: **3.12.14** (CPython).
- Platform: `Linux-6.18.55-x86_64-with-glibc2.39`.
- PyYAML: `6.0.3`; jsonschema: `4.25.1`; pytest: `8.4.2`.
- Comandos, horários, saídas e hashes das fontes Python: [observed/checks.json](observed/checks.json).
- Isolamento: [observed/isolation.json](observed/isolation.json).
- Última conferência documental: [observed/final-document-check.json](observed/final-document-check.json).
- Validador Atlas: [observed/atlas-validation.json](observed/atlas-validation.json).
- Imagens: [observed/artwork.json](observed/artwork.json).
- Links e fontes fixadas: [observed/repository-check.json](observed/repository-check.json).

A edição declara Python 3.11+, mas o ambiente efetivamente observado nesta entrega é o acima. Não se apresenta a matriz Linux/Windows e Python 3.11/3.12 configurada no GitHub Actions como se ela já tivesse sido executada.

## Preservação do contrato

A [matriz de revisão](contract-review.json) liga os três casos e onze critérios do Atlas próprio ao ADPM, à ADVS e à realização. Ela registra identificador gerado pela aplicação, título normalizado, conclusão idempotente, ordem de inserção, autorização e semântica de falhas. A origem foi reconstruída para este demo; não é o exemplo diferente publicado no Atlas.

A revisão cruzada corrigiu referências Python qualificadas aceitas na classe errada, escopo de app excluído silenciosamente, duas divergências entre cenário e teste e a observação de falha de listagem. O validador também recebeu uma regressão para grafos locais de fichas de fonte. A conferência documental final acrescentou o atributo interno de título ausente na ficha da entidade e registrou corretamente o argumento opcional de conclusão. Essas últimas alterações não mudaram o contrato de negócio ou o código dos apps.

## Limites da evidência

A automação não prova suficiência de todo cenário, equivalência de qualquer algoritmo ou confiança de autenticação em produção. As falhas de conexão simuladas não estabelecem garantias de recuperação após commit ambíguo. HTTP e conteúdo HTML foram verificados sem navegação em browser ponta a ponta. Adaptações C/Go são descritivas; não houve execução dessas linguagens, Docker, carga, recuperação distribuída ou implantação remota.

No Minerva, modelo e espelho são documentos; o validador nunca importa ou executa o programa descrito. No Vulcan, a execução é um comando explícito separado e a validação L2 usa a cópia versionada do Minerva. A disposição dos arquivos não apaga a responsabilidade L4 dos canais.

## Integridade da distribuição

O inventário único `CONTENT-SHA256.json`, na raiz do repositório, é gerado depois dos documentos e das evidências finais. Ele registra caminho, tamanho em bytes e SHA-256 de cada arquivo distribuído, exceto o próprio inventário. O builder empacota apenas o commit verificado e recusa conteúdo rastreado sujo, inventário antigo ou artefatos temporários.

O arquivo ZIP efetivo e sua extração são auditados depois do empacotamento. O commit final e o SHA-256 do próprio ZIP ficam no recibo externo de entrega, evitando uma referência circular dentro do arquivo que identificam. Confira a cópia extraída antes de instalar dependências ou gerar novos arquivos:

```bash
python scripts/check_archive.py .
```

Esta entrega local não implica criação de repositório remoto, push, tag ou release no GitHub. Os arquivos estão organizados para revisão e publicação posterior a partir do conteúdo conferido.
