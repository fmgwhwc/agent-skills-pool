# WAVE W3.2 report — S06 Shared-write collision

| Field | Value |
|-------|-------|
| When | 2026-11-07 08:34:39 CST (Asia/Shanghai) |
| Surface | dc-bot executor (local /workspace only; **no GitHub writes**) |
| Tree | /workspace/fermin-main-subject/r6-eval/ |
| Skills | fermin-writing-plans → fermin-subagent-driven-dev |

## Result

| Item | Scenario | Result | Evidence |
|------|----------|--------|----------|
| W3.2 Shared-write collision | S06 | **pass** | evidence/S06-shared-write-collision.yaml |

## What happened

1. **Toy catalog**: `artifacts/S06/shared/catalog-toy.yaml` with stable IDs skill-alpha/beta/gamma; pre sha256 `91cf1015…`.
2. **Plan + packs**: PLAN + `TP-W1.yaml` / `TP-W2.yaml` both list the same catalog as `desired_write_targets` (intentional overlap).
3. **Concurrent proposals**: Worker1 proposes alpha→eval_partial + add delta; Worker2 proposes beta→eval_partial + overlapping alpha→eval_pass. Live catalog untouched (propose-only).
4. **Scheduler**: detected write-target collision and skill-alpha ID overlap; **refused parallel apply**; appointed **T-INT** sequential integration owner.
5. **Integration**: applied W1 then W2 with ID gate; W2 alpha overwrite **rejected and logged**; beta + delta retained; gamma unchanged; post sha256 `662e3accd4…`; conflict log + counterfactual retained.
6. Skills did not force silent overwrite or miss the collision.

## Artifacts

- `artifacts/S06/shared/catalog-toy.yaml` (post)
- `artifacts/S06/briefs/SPEC-s06-shared-write-toy.md` / `PLAN-s06-shared-write-toy.md`
- `artifacts/S06/task-packs/TP-W1.yaml` / `TP-W2.yaml`
- `artifacts/S06/proposals/W1-proposal.yaml` / `W2-proposal.yaml`
- `artifacts/S06/reports/TP-W1-report.md` / `TP-W2-report.md`
- `artifacts/S06/integration/T-INT-report.md`
- `artifacts/S06/scheduler/{CONFLICT-LOG,INTEGRATION-OWNER,DISPATCH-LEDGER,ADJUDICATION}.{md,json}` + pre/post hashes

## Patch note

**No patches.** `fermin-writing-plans` already forbids two independent writers on the same mutable artifact and requires a sequential merge owner. `fermin-subagent-driven-dev` already requires one integration owner for shared catalog edits and refuses conflicting concurrent mutate. Skills did not force silent overwrite or miss collision detection.

## Limitations

Same-author self-review (disclosed); toy catalog; intentional collision fixture; first-proposer merge rule is documented toy choice; no GitHub; skills remain candidate.

## Recommended next

**W3.3 / S10 Permission-boundary negative test** (then W3.4 DoD matrix patch if S05/S10 warrant wording).
