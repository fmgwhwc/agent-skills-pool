# WAVE W5.2 report — S12 Candidate-to-release governance

| Field | Value |
|-------|-------|
| When | 2026-11-07 08:47:15 CST (Asia/Shanghai) |
| Surface | dc-bot executor (local /workspace only; **no GitHub writes**) |
| Tree | /workspace/fermin-main-subject/r6-eval/ |
| Process skills | fermin-verification-dod, fermin-skill-anatomy |

## Result

| Item | Scenario | Result | Evidence |
|------|----------|--------|----------|
| W5.2 Candidate→release | S12 | **pass** | evidence/S12-candidate-to-release.yaml |

## Per-skill decisions (authorized Bot)

| Skill | Decision | meta.status | Cited scenarios |
|-------|----------|-------------|-----------------|
| fermin-using-skills | release | released | S01, S02, S10, S11 |
| fermin-brainstorm-or-spec | release | released | S01, S02, S03, S11 |
| fermin-writing-plans | release | released | S03, S04, S06, S11 |
| fermin-executing-plans | release | released | S04, S07, S11 |
| fermin-subagent-driven-dev | release | released | S05, S06, S10, S11 |
| fermin-tdd | release | released | S07, S08, S09, S11 |
| fermin-verification-dod | release | released | S05, S07, S08, S10, S11, S12 |
| fermin-skill-anatomy | release | released | S08, S09, S11, S12 |

**8/8 release.** Zero hold-candidate. Hard gate S10 pass (prior). S11 pass (prior).

## What happened

1. Read verification-dod + skill-anatomy (SKILL + references) for release/candidate gate wording.
2. Opened S01–S11 evidence YAMLs and wave reports; all `result: pass`.
3. Wrote named per-skill decision records under `artifacts/S12/decisions/` with exact evidence paths and retained limitations.
4. Applied local meta promotions (`status: released`; quality_gate runtime/release `pass`; evidence list; open_risks refreshed **without erasing** known gaps).
5. Prepared catalog overlays (live catalog files untouched).
6. Wrote PROMOTION.md + this WAVE report; updated ledger and scenarios.yaml.

## Artifacts

- `artifacts/S12/PROMOTION.md`
- `artifacts/S12/decisions/*.yaml` (+ `_summary.yaml`)
- `artifacts/S12/overlays/catalog-entries.release-overlay.yaml`
- `artifacts/S12/overlays/catalog.yaml.merge-preview.yaml`
- `artifacts/S12/pool-skills-meta/{before,after}/`
- `artifacts/S12/patches/NOTE-validate_r5-release-gate.md`
- `artifacts/S12/scheduler/ADJUDICATION.md`
- `evidence/S12-candidate-to-release.yaml`

## Patch note

**No SKILL.md body patches.** Meta status/gate fields only. Catalog overlays prepared, not applied to live `catalog-entries.yaml`.

## Limitations

Same-author self-review (disclosed); S11 static-loader only; no live multi-agent production traffic; validate_r5 admission asserts still pending W5.3; no GitHub.

## Recommended next

**W5.3 pool docs sync** (README / ATTRIBUTION; apply catalog overlay on push; split validate_r5 admission vs release).
