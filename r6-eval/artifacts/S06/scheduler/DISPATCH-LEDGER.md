# S06 Dispatch ledger

| Task | Dispatch identity / attempt | State | Artifacts | Review / evidence | Decision / blocker |
|------|----------------------------|-------|-----------|-------------------|--------------------|
| T-W1 / TP-W1 | same-author-self-review / attempt-1 | DONE (propose-only) | proposals/W1-proposal.yaml + reports/TP-W1-report.md | Proposal present; live catalog untouched | **ACCEPTED as proposal**; apply deferred to T-INT |
| T-W2 / TP-W2 | same-author-self-review / attempt-1 | DONE (propose-only) | proposals/W2-proposal.yaml + reports/TP-W2-report.md | Proposal present; live catalog untouched; overlaps W1 write target + skill-alpha | **ACCEPTED as proposal**; apply deferred; collision flagged |
| T-INT | scheduler sequential owner / attempt-1 | DONE | shared/catalog-toy.yaml (post) + CONFLICT-LOG + hashes | Collision detected; parallel refused; ID dedup; no silent overwrite | **ACCEPTED** integrated catalog |
