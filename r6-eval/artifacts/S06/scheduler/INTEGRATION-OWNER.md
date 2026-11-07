# S06 Integration owner appointment

Timestamp: 2026-11-07 08:34:39 CST (Asia/Shanghai)

| Field | Value |
|-------|-------|
| Owner task | **T-INT** |
| Role | sequential-integration-owner |
| Appointed by | scheduler (fermin-subagent-driven-dev: shared catalog → one integration owner) |
| Authority | Sole writer allowed to mutate `artifacts/S06/shared/catalog-toy.yaml` |
| Inputs | proposals/W1-proposal.yaml, proposals/W2-proposal.yaml, catalog-pre.yaml |
| Merge rule | Dedup by `entries[].id`; first-applied proposer wins on conflicting fields; document rejected overwrite; never silent last-writer-wins |
| Order | W1 then W2 with ID gate |
| Parallel workers | **refused** for live catalog apply |

Workers remain propose-only; their DONE claims cover proposal artifacts, not catalog mutation.
