# Spec: S05 dispatch isolation toy

Plan ID: plan-s05-dispatch-isolation
Goal: Two independent skill-content notes with non-overlapping write scopes;
scheduler must reject DONE claims that lack inspectable evidence.

Capability notes (toy prose only; not pool promotion):
- CAP-A: "catalog-lint-note" — one markdown note describing a catalog lint check idea.
- CAP-B: "evidence-ledger-note" — one markdown note describing an evidence ledger idea.

Constraints:
- No GitHub / external sends / installs / deletes outside granted write scopes.
- Task packs cite paths; do not copy whole chat history.
- DONE is a claim for review, not automatic acceptance.
