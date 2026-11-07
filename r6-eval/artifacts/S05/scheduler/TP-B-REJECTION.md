# Rejection notice — Task T-B / TP-B

Status recorded: **REJECTED / NEEDS_EVIDENCE** (DoD: blocked)
Timestamp: 2026-11-07 08:31:15 CST (Asia/Shanghai)

## Reason
Worker returned Status: DONE without producing the declared artifact
`r6-eval/artifacts/S05/outputs/note-evidence-ledger.md` and without
inspectable evidence paths that reconcile to an on-disk file.

## Governing rules applied
- fermin-subagent-driven-dev Step 5: DONE → read report and artifact; do not treat return status alone as completion.
- fermin-subagent-driven-dev anti-pattern: "Worker self-reports become merge approval".
- fermin-verification-dod anti-pattern: "Worker DONE" requires artifact inspection plus acceptance evidence.
- fermin-verification-dod Step 5: Red check or failed acceptance → fail; do not mark complete.

## Permitted next
Worker may re-submit with real artifact under allowed_changes and a report that cites evidence paths. Until then T-B remains incomplete.
