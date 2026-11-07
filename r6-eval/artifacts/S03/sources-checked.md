# S03 sources checked (fermin-brainstorm-or-spec Step 1)

Checked before writing capability map / specs / plan. No remote GitHub fetch this run.

| # | Source | Kind | Notes |
|---|--------|------|-------|
| 1 | r6-eval/scenarios.yaml S03 row | stated/observed | W2.1 Requirements splitting; skills brainstorm + writing-plans; expected: two stable IDs, dep direction, one catalog owner, no duplicate plans |
| 2 | r6-eval/R6-item-build-plan.md W2.1 | observed | Done-when matches scenario expected |
| 3 | r6-eval/ledger.md | observed | W2.1 not-run before this run |
| 4 | pool/skills/fermin-brainstorm-or-spec/SKILL.md | observed | sha256 979fbaf9…; split rule + capability-map + decision-record structure |
| 5 | pool/skills/fermin-writing-plans/SKILL.md | observed | sha256 a93dfe05…; one plan + ledger; no parallel catalog writers; sequential integration owner |
| 6 | r5-adapt-batch/catalog-entries.yaml | observed | eight candidate entries; overlay merge-by-id pattern |
| 7 | pool-skeleton/catalog.yaml | observed | version 0, entries [] (local skeleton; not treated as live GitHub main) |
| 8 | r5-adapt-batch/schema/skill-entry.schema.json | observed | required: id, status, source, license_spdx, decision, rationale, fermin_tags, epistemic |
| 9 | r5-adapt-batch/schema/catalog.base.yaml | observed | version/updated/entries shell |
| 10 | r6-eval/evidence/_template.yaml + S01/S02/S08 evidence | observed | evidence YAML shape; same-author-self-review allowed as limitation |
| 11 | Parent task brief (W2.1 / S03 only; no GitHub) | stated | Propose two candidate micro-skills: catalog-lint acceptance + evidence-ledger acceptance + shared catalog.yaml integration owner; do not implement full SKILL bodies unless needed for plan artifacts |

## Classification seed

- **Stated:** two independently testable skill outputs + one shared catalog; Fermin-local candidate micro-skills for pool maintenance; no GitHub this run.
- **Observed:** existing eight candidates; empty local skeleton catalog; schema + overlay merge-by-id; writing-plans forbids parallel catalog writers.
- **Proposed (this run):** capability IDs and plan below.
- **Unknown:** whether owner wants these micro-skills actually authored after S03 (S03 only validates splitting/planning behavior).
