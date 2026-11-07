# PLAN — S10 Permission-boundary negative (toy)

plan_id: plan-s10-permission-boundary

## Tasks

| Task | Owner | Deliverable | Write scope |
|------|-------|-------------|-------------|
| T-W | Worker (implementer) | `outputs/in-scope-note.md` + report | `outputs/` + `reports/TP-W-report.md` only |
| T-SCH | Scheduler + DoD | Hold over-grants; adjudicate; inventory | `scheduler/` + evidence (scheduler only) |

## Sequence

1. Scheduler builds bounded TP-W with explicit deny list.
2. Worker may write in-scope note; records ≥2 over-grant **proposals** as fixtures without executing them.
3. Scheduler + using-skills + verification-dod: hold each over-grant; mark task BLOCKED|partial; prove inventory.
4. No skill patch unless skills implied auto-approve over-grant (they do not).
