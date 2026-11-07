# WAVE W2.2 report — S04 Resume behavior

| Field | Value |
|-------|-------|
| When | 2026-11-07 08:28:52 CST (Asia/Shanghai) |
| Surface | dc-bot executor (local /workspace only; **no GitHub writes**) |
| Tree | /workspace/fermin-main-subject/r6-eval/ |
| Skills | fermin-writing-plans → fermin-executing-plans |

## Result

| Item | Scenario | Result | Evidence |
|------|----------|--------|----------|
| W2.2 Resume behavior | S04 | **pass** | evidence/S04-resume-behavior.yaml |

## What happened

1. **writing-plans**: one plan `plan-s04-resume-toy` with T01→T02→T03 file outputs + canonical `PLAN-LEDGER.md`.
2. **executing-plans (phase A)**: completed T01 (wrote `T01-catalog-lint-note.md`, pinned sha256 `e8b7dbd26e5e5ab2b3775d6d54353a545ab9cbe393d1dda8bcf49b08d2769680`).
3. **Interrupt**: ledger showed T01 complete / T02+T03 pending; T02/T03 files absent; `INTERRUPT.md` recorded.
4. **Cold resume (phase B)**: read only ledger + files; first incomplete = **T02**; verified T01 hash; **did not rewrite T01**; wrote T02 then T03.
5. T01 sha256 unchanged through entire resume session.

## Artifacts

- `artifacts/S04/plan/PLAN-s04-resume-toy.md`
- `artifacts/S04/plan/PLAN-LEDGER.md`
- `artifacts/S04/outputs/T01-catalog-lint-note.md`
- `artifacts/S04/outputs/T02-evidence-ledger-note.md`
- `artifacts/S04/outputs/T03-integration-index.md`
- `artifacts/S04/briefs/T01-complete.yaml` / `T02-complete.yaml` / `T03-complete.yaml`
- `artifacts/S04/resume/INTERRUPT.md` / `RESUME-PASS.md` / `T01-sha256.pre-resume.txt`

## Patch note

**No patches.** `fermin-executing-plans` Step 1 already requires resume at first incomplete task and forbids reproducing completed artifacts without verification. Skills did not force wrong resume behavior.

## Limitations

Same-author self-review (memory unused by discipline, not a wiped separate process); toy prose outputs; no GitHub.

## Recommended next

**W2.3** optional copy edits to writing/executing-plans resume wording, or proceed to **W3.1 / S05 Dispatch isolation**.
