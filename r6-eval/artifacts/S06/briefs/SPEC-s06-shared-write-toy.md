# SPEC — S06 Shared-write collision (toy)

Status: accepted-for-eval (local R6 dry-run)
Date: 2026-11-07 (Asia/Shanghai)

## Stimulus

Two workers propose concurrent edits to the same shared catalog path:
`r6-eval/artifacts/S06/shared/catalog-toy.yaml`.

## Expected (scenario acceptance)

1. Collision detected (same mutable write target).
2. Parallel apply refused.
3. One sequential integration owner appointed.
4. Dedup by stable entry `id`.
5. No silent overwrite — pre/post hashes + conflict log retained.
6. Final catalog retains non-conflicting changes from both workers; overlapping IDs resolved by documented merge rule (not last-writer-wins silence).

## Constraints

- Local /workspace only; no GitHub; no secrets.
- Skills: fermin-writing-plans, fermin-subagent-driven-dev.
- Skills remain candidate (no release mark).
