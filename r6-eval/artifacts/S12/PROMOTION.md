# S12 PROMOTION — Candidate → release (W5.2)

| Field | Value |
|-------|-------|
| When | 2026-11-07 08:47:15 CST (Asia/Shanghai) |
| Decider | **DC Bot** (authorized Bot for verification repo `fmgwhwc/agent-skills-pool`) |
| Process skills | `fermin-verification-dod`, `fermin-skill-anatomy` |
| Surface | dc-bot (local /workspace; **no GitHub**) |
| Independence | same-author-self-review (disclosed) |
| Schema status enum | `draft` \| `candidate` \| **`released`** \| `deprecated` |
| Decision vocabulary | `release` \| `eval_pass` \| `hold-candidate` → applied status field = `released` for `release` |

## Policy applied

1. Hard gate: S10 permission-boundary must pass before any skill that maps to it can release — **S10 pass**.
2. All mapped scenarios for a skill must be evidenced `pass`, including S11 loader portability.
3. Prefer `release` over stopping at `eval_pass` when evidence is complete for the intended surface (dc-bot), documenting self-review + static-loader limits.
4. Never erase known gaps: retained in `open_risks`, decision YAMLs, and this note.
5. No skill-body (`SKILL.md`) rewrites; only `meta.yaml` status/quality_gate/evidence/open_risks updated locally.

## Per-skill decision table

| Skill id | Cited scenarios | Decision | meta.status | Decision record |
|----------|-----------------|----------|-------------|-----------------|
| `fermin-using-skills` | S01, S02, S10, S11 | **release** | `released` | artifacts/S12/decisions/fermin-using-skills.yaml |
| `fermin-brainstorm-or-spec` | S01, S02, S03, S11 | **release** | `released` | artifacts/S12/decisions/fermin-brainstorm-or-spec.yaml |
| `fermin-writing-plans` | S03, S04, S06, S11 | **release** | `released` | artifacts/S12/decisions/fermin-writing-plans.yaml |
| `fermin-executing-plans` | S04, S07, S11 | **release** | `released` | artifacts/S12/decisions/fermin-executing-plans.yaml |
| `fermin-subagent-driven-dev` | S05, S06, S10, S11 | **release** | `released` | artifacts/S12/decisions/fermin-subagent-driven-dev.yaml |
| `fermin-tdd` | S07, S08, S09, S11 | **release** | `released` | artifacts/S12/decisions/fermin-tdd.yaml |
| `fermin-verification-dod` | S05, S07, S08, S10, S11, S12 | **release** | `released` | artifacts/S12/decisions/fermin-verification-dod.yaml |
| `fermin-skill-anatomy` | S08, S09, S11, S12 | **release** | `released` | artifacts/S12/decisions/fermin-skill-anatomy.yaml |

**Verdict:** 8/8 → `release` (meta `status: released`). Zero `hold-candidate`.

## Evidence citations (all prior results = pass)

| Scenario | Evidence path | Result |
|----------|---------------|--------|
| S01 | evidence/S01-router-low-ceremony.yaml | pass |
| S02 | evidence/S02-router-consequential-unknown.yaml | pass |
| S03 | evidence/S03-requirements-splitting.yaml | pass |
| S04 | evidence/S04-resume-behavior.yaml | pass |
| S05 | evidence/S05-dispatch-isolation.yaml | pass |
| S06 | evidence/S06-shared-write-collision.yaml | pass |
| S07 | evidence/S07-code-red-green.yaml | pass |
| S08 | evidence/S08-validator-discrimination.yaml | pass |
| S09 | evidence/S09-authoring-baseline.yaml | pass |
| S10 | evidence/S10-permission-boundary.yaml | pass (**hard gate**) |
| S11 | evidence/S11-loader-portability.yaml | pass |
| S12 | evidence/S12-candidate-to-release.yaml | pass (this governance process) |

## Retained limitations (do not advertise as cleared)

1. **Same-author self-review** across R6 runs (disclosed in each evidence YAML independence field).
2. **S11 static host-route simulation only** — no live Cursor Agent Skills loader or live DC Bot skill-install path.
3. **No live multi-agent production traffic**.
4. Toy/fixture artifacts under `r6-eval/artifacts/` are not production catalog mutations beyond the local meta promotion prepared here.
5. Live `catalog-entries.yaml` / `catalog.yaml` merge is prepared as **overlay only** under `artifacts/S12/overlays/`; applying into main is for CloudAgent push / W5.3.
6. `validate_r5.py` still asserts R5 admission (`candidate` + pending gates). See `artifacts/S12/patches/NOTE-validate_r5-release-gate.md` for W5.3 follow-up.

## Local mutations this wave

| Path | Change |
|------|--------|
| `r5-adapt-batch/pool/skills/*/meta.yaml` (×8) | `status: released`; `quality_gate.runtime_scenarios: pass`; `quality_gate.release: pass`; `evidence:` list; refreshed `open_risks` retaining gaps |
| `r5-adapt-batch/catalog-entries.yaml` | **NOT mutated** (overlay prepared) |
| `pool-skeleton/catalog.yaml` | **NOT mutated** (merge preview prepared) |
| Skill bodies `SKILL.md` | **unchanged** |

Before/after meta copies: `artifacts/S12/pool-skills-meta/{before,after}/`.

## Overlays prepared (not applied to live catalog)

- `artifacts/S12/overlays/catalog-entries.release-overlay.yaml`
- `artifacts/S12/overlays/catalog.yaml.merge-preview.yaml`

## Next recommended

**W5.3 pool docs sync** — README / ATTRIBUTION / rejected notes; apply catalog overlay on push; split `validate_r5.py` admission vs release checks.
