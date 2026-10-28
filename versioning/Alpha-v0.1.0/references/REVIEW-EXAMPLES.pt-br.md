# Composição, persistência e revisão de mudanças

[English](REVIEW-EXAMPLES.md) · Português brasileiro

Estes são **recortes ilustrativos de projeto**, não casos adicionais da fonte TaskBoard nem alegações de execução. Demonstram obrigações de revisão que o validador estrutural não decide sozinho.

<a id="case-composition"></a>
## Composição com duas decisões de autorização

Considere outra especificação L1 que declare explicitamente `UC-REPORT-EXPORT` com permissão `reports:export` e `UC-REPORT-READ` com `reports:read`. A exportação precisa dos dados do caso de leitura. Ambos são casos normais de origem, cada um com seu próprio teste comportamental diretamente vinculado. Declare a dependência da exportação para a leitura e a transmissão do mesmo contexto de ator resolvido. Um ponto de composição injeta o caso de leitura, sem descobri-lo por registro global.

```text
exportReport(actor_context, report_id)
  autorizar reports:export; recusar antes de efeitos protegidos
  report = read_case.readReport(actor_context, report_id)
  construir a exportação autorizada a partir de report
  retornar o resultado

readReport(actor_context, report_id)
  autorizar reports:read; recusar antes de efeitos protegidos
  usar a ferramenta declarada de leitura e retornar seu resultado contratual
```

| Contexto | Decisão de exportar | Decisão de ler | Observação exigida |
| --- | --- | --- | --- |
| Duas permissões | Permitir | Permitir | Exportação corresponde à leitura autorizada |
| Apenas exportar | Permitir | Recusar | Sem leitura protegida ou exportação produzida |
| Apenas ler | Recusar | Não chamado | Nem caso chamado nem ferramenta são acessados |
| Ausente ou não resolvido | Recusar | Não chamado | Sem efeito de domínio/armazenamento |

Atuar em nome de outro participante exige política explícita de delegação, escopo e confiança no contrato L1/L2. Substituir o contexto por ator privilegiado somente porque a chamada é interna viola o contrato. Testes em `tests/test_validation.py` conferem que a dependência exige contexto transmitido; esses testes estruturais não implementam o cenário hipotético de relatórios.

## Condições contextuais e escritas ambíguas

Uma `Task` pronta já é internamente válida. A ferramenta não repete validação do tamanho do título antes de salvar. Uma linha bruta hidratada ainda passa pela construção canônica. Unicidade global atômica, revisão esperada de armazenamento ou existência de recurso podem ser condições contextuais distintas, com objeto, finalidade e responsável próprios.

| Situação | Alegação corretamente delimitada |
| --- | --- |
| Construção canônica rejeita título bruto antes de abrir armazenamento | Essa operação não tentou inserir |
| Falha de conexão injetada ocorre antes de qualquer acesso | Não houve escrita nessa fixture controlada |
| Confirmação remota se perde após envio de escrita | Resultado pode ser desconhecido; falha não prova ausência de efeito |
| Unicidade atômica é exigida | Uma consulta prévia não estabelece a garantia sob concorrência |

Os cenários TaskBoard utilizam SQLite local e falha injetada **antes da conexão**. Não implementam os dois últimos contratos nem alegam recuperação de resultados distribuídos desconhecidos. Um projeto que precise dessas garantias deve especificá-las e acrescentar cenários/evidências pertinentes.

<a id="change-impact"></a>
## Preservar a intenção quando o código diverge

A [fixture observed-drift](../examples/counterexamples/observed-drift.yaml) preserva a operação pretendida “retornar um” e o hash de sua fonte observada de referência. A [fonte atual](../examples/counterexamples/apps/Drift/Example.py) retorna dois. `--verify-code` informa `CODE_HASH_MISMATCH`. Não reescreve o blueprint para aprovar a alteração nem afirma que comparar hashes estabeleceu a diferença comportamental.

O revisor segue estes passos:

1. Identificar bytes, símbolos e IDs lógicos alterados, mantendo intenção anterior e nova observação.
2. Decidir se a mudança é defeito, refinamento que preserva contrato ou proposta de alteração de requisito/projeto.
3. Se o contrato muda, identificar casos/critérios L1, regras de entidade/ferramenta e cenários L2, realização/testes L3 e projeções L4 afetados. Obter a revisão apropriada antes de mudar contratos autoritativos.
4. Para renomeação aceita sem mudança semântica, preservar IDs e atualizar caminhos, espelho e hash. Para mudança semântica aceita, revisar documento e contratos explicitamente.
5. Revalidar referências/cobertura e executar verificações pertinentes da realização. Registrar revisão, configuração e resultado efetivos; efeitos não resolvidos continuam como lacunas.

Por exemplo, elevar o limite de título de 120 para 200 é proposta contratual que afeta critério L1 de título inválido, regra canônica, construção, cenários de limite e observações de fonte. Alterar apenas `ValueObject_TaskTitle` e atualizar o hash esconderia a decisão pendente. Um comentário interno pode mudar o hash e preservar contratos; o revisor registra essa conclusão mais limitada após inspecionar.

## Autoridade da revisão

`reviewed` no exemplo significa a revisão técnica declarada desta candidata alpha. Não significa que Douglas de Oliveira Alkimim aprovou a entrega. O texto de responsável e a pendência explícita preservam essa revisão ainda necessária. Um projeto consumidor deve substituir a procedência do exemplo por autoria/revisão reais e decisões efetivas; copiar um exemplo não aprova seus requisitos.
