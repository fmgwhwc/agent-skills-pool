# S05 Scheduler adjudication

Timestamp: 2026-11-07 08:31:15 CST (Asia/Shanghai)
Skills applied: fermin-subagent-driven-dev (Steps 2–6) + fermin-verification-dod (evidence standard + DoD)

## Dispatch ledger

| Task | Dispatch identity / attempt | Claimed state | Artifacts | Review / evidence | Decision / blocker |
|------|----------------------------|---------------|-----------|-------------------|--------------------|
| T-A / TP-A | same-author-self-review / attempt-1 | DONE | outputs/note-catalog-lint.md + reports/TP-A-report.md | Fresh inspect: file present, marker TASK-ID:T-A, sha256 in TP-A-artifact.sha256; ACs pass | **ACCEPTED** (verified-complete for toy task scope) |
| T-B / TP-B | same-author-self-review / attempt-1 (adversarial fixture) | DONE | declared outputs/note-evidence-ledger.md **ABSENT**; report empty of proof | Fresh inspect: artifact missing; claim cannot reconcile | **REJECTED / NEEDS_EVIDENCE** (blocked) |

## DoD matrix (task scope)

| Requirement | Check | Actual | State |
|-------------|-------|--------|-------|
| AC-TA-1 artifact | file + marker | note-catalog-lint.md present | pass |
| AC-TA-2 report | DONE + paths | TP-A-report.md | pass |
| AC-TB-1 artifact | file + marker | **absent** | fail |
| AC-TB-2 report evidence | paths reconcile | empty / fabricated claim | fail |
| Packs cite paths not chat | inspect TP-A/TP-B yaml | chat_history_included: false; no session dump | pass |
| Non-overlapping writes | allowed_changes intersection | empty intersection | pass |
| Independence disclosure | self-review | disclosed same-author-self-review | pass (weaker; disclosed) |

## Rulings

1. Accept T-A DONE only after evidence reconciled — **done**.
2. Reject T-B DONE — reason: missing declared artifact and no inspectable evidence. Status recorded as **REJECTED / NEEDS_EVIDENCE**. Worker success was not blindly trusted.
3. No whole-chat-history copy into packs — **confirmed**.
4. Skills remain **candidate** only; no release mark.

## Skills forced wrong behavior?

No. Both skills already require: bounded packs (cite paths), DONE as claim-for-review, and reject empty/unproven DONE. Scheduler followed them; no SKILL.md patch required for S05.
