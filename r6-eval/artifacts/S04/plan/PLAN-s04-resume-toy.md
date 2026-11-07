# S04 resume toy (3 file outputs) — Execution Plan
Plan-ID: plan-s04-resume-toy
Spec/request: r6-eval/scenarios.yaml#S04 (authorized local reversible eval; no GitHub)
Goal: Produce three sequential file artifacts so resume behavior can be demonstrated after an interrupt between T01 and T02.
Required route: fermin-executing-plans
Ledger: artifacts/S04/plan/PLAN-LEDGER.md

## Decision constraints
- Exactly one plan file for this initiative (`plan-s04-resume-toy`).
- Toy content may reuse S03 capability *ideas* (catalog-lint / evidence-ledger) as prose only; do not mutate `pool/skills/` or live `catalog.yaml`.
- Outputs live only under `r6-eval/artifacts/S04/`.
- No GitHub writes this run.
- Resume must use ledger + files only; conversational memory is not an authority.

## Shared contracts
- Output paths (exact):
  - T01 → `artifacts/S04/outputs/T01-catalog-lint-note.md`
  - T02 → `artifacts/S04/outputs/T02-evidence-ledger-note.md`
  - T03 → `artifacts/S04/outputs/T03-integration-index.md`
- Each note must contain its task_id line and a non-empty body (≥3 lines).
- T03 must cite relative paths to T01 and T02 outputs and refuse to invent content if either is missing.
- Ledger states: `pending` | `in-progress` | `complete` | `blocked`.

## Acceptance and evidence map
| Requirement | Owning task | Concrete check | Retained artifact |
|---|---|---|---|
| First note written | T01 | File exists; contains `task_id: T01` | outputs/T01-catalog-lint-note.md |
| Second note written | T02 | File exists; contains `task_id: T02`; T01 hash unchanged after resume | outputs/T02-evidence-ledger-note.md |
| Integration index | T03 | File exists; links both prior outputs | outputs/T03-integration-index.md |
| Resume correctness | executor | After interrupt, first incomplete = T02; T01 not rewritten | plan/PLAN-LEDGER.md + resume/RESUME-PASS.md |

## Review focus
- Do not rewrite completed artifacts on resume.
- Ledger and filesystem must reconcile (status `complete` ⇒ file present with expected marker).

---

## Tasks

### T01 — Catalog-lint note
```yaml
task_id: T01
title: "Write T01 catalog-lint note artifact"
depends_on: []
surfaces: ["dc-bot"]
inputs:
  - "artifacts/S03/capability-map.md (ideas only; optional)"
  - "artifacts/S04/plan/PLAN-s04-resume-toy.md"
outputs:
  - "artifacts/S04/outputs/T01-catalog-lint-note.md"
allowed_changes:
  - "r6-eval/artifacts/S04/outputs/T01-catalog-lint-note.md"
  - "r6-eval/artifacts/S04/briefs/T01-complete.yaml"
  - "r6-eval/artifacts/S04/plan/PLAN-LEDGER.md"
consumes:
  - "plan-s04-resume-toy T01 contract"
produces:
  - "T01 note file with task_id marker"
steps:
  - "Write note summarizing catalog-lint capability idea (prose only)"
  - "Emit T01 completion brief"
  - "Mark T01 complete in PLAN-LEDGER"
acceptance:
  - id: AC-T01-1
    check: "outputs/T01-catalog-lint-note.md exists and contains 'task_id: T01'"
    expected: "present"
  - id: AC-T01-2
    check: "briefs/T01-complete.yaml records sha256 of T01 output"
    expected: "sha256 field set"
evidence:
  - "artifacts/S04/briefs/T01-complete.yaml"
```

### T02 — Evidence-ledger note
```yaml
task_id: T02
title: "Write T02 evidence-ledger note artifact"
depends_on: [T01]
surfaces: ["dc-bot"]
inputs:
  - "artifacts/S04/outputs/T01-catalog-lint-note.md"
  - "artifacts/S04/plan/PLAN-LEDGER.md"
outputs:
  - "artifacts/S04/outputs/T02-evidence-ledger-note.md"
allowed_changes:
  - "r6-eval/artifacts/S04/outputs/T02-evidence-ledger-note.md"
  - "r6-eval/artifacts/S04/briefs/T02-complete.yaml"
  - "r6-eval/artifacts/S04/plan/PLAN-LEDGER.md"
consumes:
  - "T01 complete + artifact present"
produces:
  - "T02 note file with task_id marker"
steps:
  - "Verify T01 artifact exists; do not rewrite it"
  - "Write evidence-ledger capability idea note"
  - "Emit T02 completion brief; mark T02 complete"
acceptance:
  - id: AC-T02-1
    check: "outputs/T02-evidence-ledger-note.md exists and contains 'task_id: T02'"
    expected: "present"
  - id: AC-T02-2
    check: "T01 sha256 equals pre-resume pin"
    expected: "unchanged"
evidence:
  - "artifacts/S04/briefs/T02-complete.yaml"
```

### T03 — Integration index
```yaml
task_id: T03
title: "Write T03 integration index linking T01+T02"
depends_on: [T01, T02]
surfaces: ["dc-bot"]
inputs:
  - "artifacts/S04/outputs/T01-catalog-lint-note.md"
  - "artifacts/S04/outputs/T02-evidence-ledger-note.md"
outputs:
  - "artifacts/S04/outputs/T03-integration-index.md"
allowed_changes:
  - "r6-eval/artifacts/S04/outputs/T03-integration-index.md"
  - "r6-eval/artifacts/S04/briefs/T03-complete.yaml"
  - "r6-eval/artifacts/S04/plan/PLAN-LEDGER.md"
consumes:
  - "T01 and T02 output paths"
produces:
  - "index citing both notes"
steps:
  - "Confirm both inputs exist"
  - "Write index with relative links"
  - "Mark T03 complete"
acceptance:
  - id: AC-T03-1
    check: "index contains both relative paths and task_id: T03"
    expected: "present"
evidence:
  - "artifacts/S04/briefs/T03-complete.yaml"
```
