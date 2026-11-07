# Pool-maintenance micro-skills (catalog-lint + evidence-ledger) — Execution Plan
Plan-ID: plan-s03-pool-maint-microskills
Spec: artifacts/S03/specs/SPEC-cap-catalog-lint.md + artifacts/S03/specs/SPEC-cap-evidence-ledger.md (status: authorized-default for S03 planning; full skill authoring not required this scenario)
Goal: Produce two independently acceptable candidate-skill contracts and one sequential catalog-integration owner task without duplicate plans or parallel catalog writers.
Required route: fermin-executing-plans (single executor; local convergence). Subagent route deferred until W3.
Ledger: artifacts/S03/plan/PLAN-LEDGER.md

## Decision constraints
- Two capability IDs only: `cap-catalog-lint`, `cap-evidence-ledger` (see capability-map.md).
- Dependency direction: both → T-INT; peers have `depends_on: none` relative to each other.
- S03 does **not** implement full SKILL.md bodies; tasks stop at acceptance contracts + payload sketches + integration procedure.
- No GitHub push/PR this run (parent brief).
- Shared mutable artifact `catalog.yaml` (or merge overlay) has **exactly one** writer task: T03.
- Do not invent a second plan file for the same initiative.
- Existing eight R5 candidates remain untouched.
- Status of any future catalog row remains `candidate` / `epistemic: provisional` until real authoring + scenarios.

## Shared contracts
- Catalog entry schema required keys: id, status, source{repo,ref,path,url}, license_spdx, decision, rationale, fermin_tags, epistemic (skill-entry.schema.json).
- Catalog shell: version / updated / entries[] (catalog.base.yaml).
- Merge rule: merge-by-id; reject duplicate ids; no silent overwrite (prepare for S06).
- Capability map path: `artifacts/S03/capability-map.md`.
- Payload sketches live inside each SPEC; T03 consumes those sketches only after T01/T02 mark contracts complete.
- Output destinations for this scenario (planning-only): under `r6-eval/artifacts/S03/` — not `pool/skills/`.

## Acceptance and evidence map
| Requirement | Owning task | Concrete check | Retained artifact |
|---|---|---|---|
| Stable ID + independent AC for catalog-lint | T01 | Spec + map row present; AC list names bad/good fixture discrimination | specs/SPEC-cap-catalog-lint.md |
| Stable ID + independent AC for evidence-ledger | T02 | Spec + map row present; AC list names ledger/evidence pairing checks | specs/SPEC-cap-evidence-ledger.md |
| Single catalog integration owner | T03 | Exactly one task lists catalog.yaml (or overlay) in allowed_changes; T01/T02 omit it | this plan + briefs/T03-*.yaml |
| No duplicate plans | plan header | Only Plan-ID `plan-s03-pool-maint-microskills` for this initiative | plan/ directory listing |
| Acyclic deps | T01/T02/T03 | T01∥T02; T03 depends_on [T01,T02] | task YAML depends_on fields |

## Review focus
- Parallel catalog write anti-pattern must not appear in T01/T02.
- Capability removability: deleting one SPEC must not invalidate the other's acceptance text.
- Do not treat S03 planning artifacts as runtime_scenarios pass for a non-existent skill body.

---

## Tasks

### T01 — Catalog-lint capability contract
```yaml
task_id: T01
title: "cap-catalog-lint acceptance contract + catalog-entry payload sketch"
depends_on: []
surfaces: ["dc-bot"]
inputs:
  - "artifacts/S03/capability-map.md"
  - "artifacts/S03/specs/SPEC-cap-catalog-lint.md"
  - "r5-adapt-batch/schema/skill-entry.schema.json"
outputs:
  - "artifacts/S03/briefs/T01-catalog-lint-complete.yaml"
allowed_changes:
  - "r6-eval/artifacts/S03/specs/SPEC-cap-catalog-lint.md"
  - "r6-eval/artifacts/S03/briefs/T01-catalog-lint-complete.yaml"
consumes:
  - "capability id cap-catalog-lint"
produces:
  - "accepted contract text + payload sketch for id fermin-catalog-lint"
steps:
  - "Confirm SPEC lists independent acceptance (bad fixture reject / good pass / source unchanged)"
  - "Confirm allowed_changes exclude catalog.yaml"
  - "Emit T01 completion brief referencing AC-1..AC-4"
acceptance:
  - id: AC-T01-1
    check: "SPEC-cap-catalog-lint.md contains ID cap-catalog-lint and AC-1..AC-4"
    expected: "all present"
  - id: AC-T01-2
    check: "Brief states catalog.yaml not in allowed_changes"
    expected: "explicit omission recorded"
evidence:
  - "artifacts/S03/briefs/T01-catalog-lint-complete.yaml"
```

### T02 — Evidence-ledger capability contract
```yaml
task_id: T02
title: "cap-evidence-ledger acceptance contract + catalog-entry payload sketch"
depends_on: []
surfaces: ["dc-bot"]
inputs:
  - "artifacts/S03/capability-map.md"
  - "artifacts/S03/specs/SPEC-cap-evidence-ledger.md"
  - "r6-eval/evidence/_template.yaml"
outputs:
  - "artifacts/S03/briefs/T02-evidence-ledger-complete.yaml"
allowed_changes:
  - "r6-eval/artifacts/S03/specs/SPEC-cap-evidence-ledger.md"
  - "r6-eval/artifacts/S03/briefs/T02-evidence-ledger-complete.yaml"
consumes:
  - "capability id cap-evidence-ledger"
produces:
  - "accepted contract text + payload sketch for id fermin-evidence-ledger"
steps:
  - "Confirm SPEC lists independent ledger/evidence pairing acceptance"
  - "Confirm peer independence from cap-catalog-lint"
  - "Emit T02 completion brief"
acceptance:
  - id: AC-T02-1
    check: "SPEC-cap-evidence-ledger.md contains ID cap-evidence-ledger and AC-1..AC-5"
    expected: "all present"
  - id: AC-T02-2
    check: "Brief states catalog.yaml not in allowed_changes"
    expected: "explicit omission recorded"
evidence:
  - "artifacts/S03/briefs/T02-evidence-ledger-complete.yaml"
```

### T03 — Shared catalog integration (single owner)
```yaml
task_id: T03
title: "Sequential catalog.yaml integration owner procedure for both payload sketches"
depends_on: ["T01", "T02"]
surfaces: ["dc-bot"]
inputs:
  - "artifacts/S03/briefs/T01-catalog-lint-complete.yaml"
  - "artifacts/S03/briefs/T02-evidence-ledger-complete.yaml"
  - "payload sketches inside both SPECs"
  - "r5-adapt-batch/catalog-entries.yaml (merge-by-id pattern)"
  - "pool-skeleton/catalog.yaml"
outputs:
  - "artifacts/S03/briefs/T03-catalog-integration-owner.yaml"
allowed_changes:
  - "r6-eval/artifacts/S03/briefs/T03-catalog-integration-owner.yaml"
  # Live catalog.yaml write is OUT OF SCOPE for S03 dry-run; T03 defines the owner procedure only.
  # When a later wave authorizes apply: single writer may edit catalog.yaml OR catalog-entries overlay — never both workers.
consumes:
  - "fermin-catalog-lint payload sketch"
  - "fermin-evidence-ledger payload sketch"
produces:
  - "integration-owner procedure: merge order, dedup-by-id, conflict check, single-writer rule"
steps:
  - "Verify T01 and T02 briefs exist and omit catalog writes"
  - "Define merge order: apply fermin-catalog-lint entry, then fermin-evidence-ledger entry (or any order if ids distinct); reject duplicate ids"
  - "Name sole owner role: catalog-integration-owner (this task / future executor of this task only)"
  - "Record that parallel T01/T02 must not touch catalog.yaml"
  - "Do not apply live catalog mutation in S03 (planning + procedure only)"
acceptance:
  - id: AC-T03-1
    check: "Exactly one task in this plan lists catalog integration ownership"
    expected: "T03 only"
  - id: AC-T03-2
    check: "Procedure names dedup-by-id and forbids silent overwrite"
    expected: "explicit in T03 brief"
  - id: AC-T03-3
    check: "depends_on includes T01 and T02; no second plan file"
    expected: "acyclic single plan"
evidence:
  - "artifacts/S03/briefs/T03-catalog-integration-owner.yaml"
```
