# R6 evaluation harness (Bot-side)

Date: 2026-11-07 (Asia/Shanghai). Local-only until parent pushes to `agent-skills-pool`.

## Purpose

Run the R5-NEXT runtime scenarios against Fermin process skills, record evidence, and only then propose catalog status moves (`candidate` → `eval_partial` → `eval_pass` → `release`). Static `validate_r5.py` success is **not** a runtime pass.

## Layout

| Path | Role |
|------|------|
| `scenarios.yaml` | Stable IDs S01–S12 + skill mapping |
| `evidence/_template.yaml` | Copy per run; fill every field |
| `evidence/SNN-*.yaml` | Completed evidence records |
| `fixtures/` | Disposable inputs for dry-runs |
| `patches/` | Proposed SKILL.md diffs (not silently applied to pool) |
| `artifacts/` | Outputs produced by scenario runs |
| `ledger.md` | Wave / item progress |
| `R6-item-build-plan.md` | Build plan copy for packaging |
| `WAVE-*.md` | Wave summary reports |

## How to run

1. Pick a scenario ID from `scenarios.yaml`.
2. Copy `evidence/_template.yaml` → `evidence/SNN-<slug>.yaml`.
3. Set `surface`, `run_id`, `skill_revision` (immutable SHA or local tree hash), and `baseline_artifact`.
4. Execute the stimulus on the authorized surface. Prefer a **fresh disposable fixture** under `fixtures/` or a temp copy; do not mutate pool skills in place without a patch note.
5. Capture commands, exit codes, and short stdout/stderr snippets in the evidence file.
6. Set `result` to `pass|fail|partial|blocked|not-run` honestly. List gaps under `limitations`.
7. Update `ledger.md` for the wave item.

### Validator (W1.3)

```bash
source /workspace/r5-validation-venv/bin/activate
cd /workspace/fermin-main-subject/r5-adapt-batch
python validate_r5.py --self-test
# Negative control on a TEMP copy only — never edit pool/skills in place for this test.
```

### Router / low ceremony (W1.1)

```bash
# Create or refresh fixtures/typo-doc.md with a known typo, then apply a bounded fix.
# Follow fermin-using-skills: no brainstorm/writing-plans for a documented single-path typo.
```

## Recording rules

- Asia/Shanghai timestamps with zone label.
- `independence` must be truthful (`fresh-worker` | `same-author-self-review` | `static-only`).
- Do not mark `runtime_scenarios: pass` in meta.yaml from this harness alone until owner/promotion process reviews evidence.
- Proposed skill edits go under `patches/*.diff` with a one-line rationale in the wave report.

## Packaging

Zip `r6-eval/` (and patches) for parent to push; this executor does **not** write GitHub.
