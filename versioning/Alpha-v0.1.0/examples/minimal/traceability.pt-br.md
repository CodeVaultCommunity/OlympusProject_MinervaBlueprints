# Correspondência de obrigações

A fonte L1 permanece canônica. Esta tabela é uma visão dos vínculos do blueprint; não é evidência de execução.

| L1 | L2 | Relation |
| --- | --- | --- |
| ENT-REQUEST | ENT-REQUEST | preserves |
| VLD-REQUEST-QUANTITY | VLD-REQUEST-QUANTITY | preserves |
| VLD-REQUEST-CODE | VLD-REQUEST-CODE | preserves |
| TOL-REQUEST-STORE | TOL-REQUEST-STORE | preserves |
| OP-REQUEST-STORE | OP-REQUEST-STORE | preserves |
| UC-REQUEST-SUBMIT | UC-REQUEST-SUBMIT, BT-REQUEST-SUBMIT | preserves |
| RF-REQUEST-01 | UC-REQUEST-SUBMIT | preserves |
| RF-REQUEST-02 | UC-REQUEST-SUBMIT | preserves |
| RF-REQUEST-03 | UC-REQUEST-SUBMIT | preserves |
| RF-REQUEST-04 | UC-REQUEST-SUBMIT | preserves |
| RF-REQUEST-05 | UC-REQUEST-SUBMIT | preserves |
| RF-REQUEST-06 | UC-REQUEST-SUBMIT | preserves |
| RF-REQUEST-07 | UC-REQUEST-SUBMIT | preserves |
| RNF-REQUEST-01 | UC-REQUEST-SUBMIT | preserves |
| AC-REQUEST-01 | BT-REQUEST-SUBMIT, SC-REQUEST-01 | verifies |
| AC-REQUEST-02 | BT-REQUEST-SUBMIT, SC-REQUEST-02 | verifies |
| AC-REQUEST-03 | BT-REQUEST-SUBMIT, SC-REQUEST-SUBMIT-AUTH-ABSENT, SC-REQUEST-SUBMIT-AUTH-UNRESOLVED, SC-REQUEST-SUBMIT-AUTH-UNKNOWN, SC-REQUEST-SUBMIT-AUTH-INSUFFICIENT, SC-REQUEST-SUBMIT-AUTH-EXPIRED, SC-REQUEST-SUBMIT-AUTH-ANONYMOUS | verifies |
| AC-REQUEST-04 | BT-REQUEST-SUBMIT, SC-REQUEST-04 | verifies |
| AC-REQUEST-05 | BT-REQUEST-SUBMIT, SC-REQUEST-05 | verifies |
| AC-REQUEST-06 | BT-REQUEST-SUBMIT, SC-REQUEST-06 | verifies |
| AC-REQUEST-SUBMIT-QUALITY | BT-REQUEST-SUBMIT, SC-REQUEST-SUBMIT-QUALITY | verifies |
| RNF-REQUEST-01 | CHK-RNF-REQUEST-01 | verifies |
| OP-REQUEST-STORE | CHK-OP-REQUEST-STORE | verifies |

A revisão considera autorização antes dos efeitos, validação canônica, falhas distintas, incerteza de escrita, obrigações compartilhadas e limites da fonte. Os testes de consistência não provam equivalência semântica.
