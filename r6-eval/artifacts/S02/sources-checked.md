# S02 sources checked (read before asking)

Timezone labels: Asia/Shanghai (CST). Checked during W1.2 dry-run on dc-bot.

| # | Path | What was taken |
|---|------|----------------|
| 1 | `r5-adapt-batch/MANIFEST.md` | Eight skill dirs + catalog overlay + validator + reports packaged for R5 |
| 2 | `r5-adapt-batch/catalog-entries.yaml` | Eight `id`s; every entry `status: candidate`; `runtime_scenarios: pending`; `release: pending` |
| 3 | `r5-adapt-batch/pool/skills/*/` | Eight packages present: using-skills, brainstorm-or-spec, writing-plans, executing-plans, subagent-driven-dev, tdd, verification-dod, skill-anatomy |
| 4 | `r5-adapt-batch/pool/skills/fermin-using-skills/SKILL.md` | Route table; unclear goal → brainstorm-or-spec; Step 4 already contains single-path typo exemption text; sha256 `f22ce33c…` |
| 5 | `r5-adapt-batch/pool/skills/fermin-brainstorm-or-spec/SKILL.md` | Read-before-ask; stated/observed/proposed/unknown; one high-impact question or authorized default; sha256 `979fbaf9…` |
| 6 | `r5-adapt-batch/R5-NEXT-EVALUATION.md` | Twelve runtime scenarios; local copy still stamped "NOT RUN" for all rows (document lag vs r6-eval ledger) |
| 7 | `pool-skeleton/README.md` | Pool is not an upstream mirror; ACCEPT/ADAPT only |
| 8 | `pool-skeleton/catalog.yaml` | Local skeleton still `version: 0`, `entries: []` (stale vs R5 batch overlay; do not treat as GitHub main) |
| 9 | `research/matrix/R6-item-build-plan.md` | W0–W5 queue; W1.2 = S02; owner said continue item-by-item |
| 10 | `r6-eval/ledger.md` | W0 complete; S08 pass; S01 pass; S02 was `not-run` before this run |
| 11 | `r6-eval/scenarios.yaml` | S02 expected: read before asking; one question or default; observed/proposed/unknown |
| 12 | `r6-eval/WAVE-W0-W1-REPORT.md` | Prior wave local-only; recommended next was W1.2 |
| 13 | `r6-eval/patches/fermin-using-skills.SKILL.md.diff` | Step 4 patch note from S01; local SKILL.md already matches patched text (hash moved vs S01 baseline) |

## Explicitly not fetched this run

- Live GitHub tree for `fmgwhwc/agent-skills-pool` (no network inventory). Parent conversation previously reported PR #1/#2/#3 merged to `main`; that is **not** re-verified here and is not used as a file-level fact.
