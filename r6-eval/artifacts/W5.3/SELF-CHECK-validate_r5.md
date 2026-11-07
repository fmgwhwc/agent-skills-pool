# W5.3 self-check — validate_r5.py admission vs release

Timestamp: 2026-11-07 08:49:24 CST (Asia/Shanghai)
Tree: `/workspace/fermin-main-subject/r5-adapt-batch/` (eight metas `status: released`)

## Mode contract

| `--mode` | Behavior |
|----------|----------|
| `auto` (default) | Per skill: `candidate` → admission gates; `released` → release gates |
| `admission` | Force candidate + `runtime_scenarios/release == pending` (R5 ADAPT intake) |
| `release` | Force `released` + both gates `pass` + non-empty path-like `evidence` (r6-eval paths must exist) |

Admission is **not** weakened: a `released` skill with empty evidence still fails under `auto`/`release`.

## Results (this wave)

| Check | Expected | Observed |
|-------|----------|----------|
| Live tree `--mode release` | PASS (8 skills) | **PASS** (530 assertions) — see `self-check-release.log` |
| Live tree `--mode auto` | PASS | **PASS** |
| Live tree `--mode admission` | FAIL (skills are released, not candidate) | **FAIL** exit 1 — proves admission still demands candidate+pending |
| Temp copy: one meta `status:released` + `evidence: []` | FAIL | **FAIL** `released requires non-empty evidence paths` |
| Temp copy: evidence path `r6-eval/evidence/DOES-NOT-EXIST.yaml` | FAIL | **FAIL** `missing evidence file …` |

Logs: `self-check-*.log` beside this note.

## Conclusion

Split works. New ADAPT intake should use `--mode admission` (or ship candidates with pending gates under `auto`). Released pool validates with `--mode release` or `auto`.
