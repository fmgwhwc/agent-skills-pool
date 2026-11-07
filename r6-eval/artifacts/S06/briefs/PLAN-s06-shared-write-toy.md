# S06 Shared-write collision — Execution Plan
Plan-ID: plan-s06-shared-write-collision
Spec: r6-eval/artifacts/S06/briefs/SPEC-s06-shared-write-toy.md (accepted-for-eval)
Goal: Detect concurrent catalog write proposals, refuse parallel apply, merge via one sequential integration owner with ID dedup and no silent overwrite.
Required route: fermin-subagent-driven-dev
Ledger: r6-eval/artifacts/S06/scheduler/DISPATCH-LEDGER.md

## Decision constraints

- Shared mutable artifact: `artifacts/S06/shared/catalog-toy.yaml` only.
- Workers may **propose** patches; they must not apply directly to the live catalog.
- Overlapping write scope on the same catalog path is a **collision** even if entry IDs differ.
- Merge rule on same `id`: keep higher-priority field set from integration owner decision; never silent last-writer-wins.
- No GitHub / external messages / installs / deletes.

## Shared contracts

- Catalog schema: `version`, `updated`, `entries[]` with stable `id`, `name`, `status`, `owner`, `notes`.
- Dedup key: `entries[].id` (exact string).
- Proposal format: YAML patch proposal under `artifacts/S06/proposals/`.

## Tasks (intentionally overlapping write scope to exercise collision)

| Task | Role | Write target | Intentional collision |
|------|------|--------------|----------------------|
| T-W1 / TP-W1 | Worker1 propose | same catalog path | yes — proposes skill-alpha update + skill-delta add |
| T-W2 / TP-W2 | Worker2 propose | same catalog path | yes — proposes skill-beta update + skill-alpha overlapping update |
| T-INT | Sequential integration owner | same catalog path | sole apply authority after collision detect |

## Acceptance and evidence map

| Requirement | Owning task | Check | Artifact |
|-------------|-------------|-------|----------|
| Collision detected | scheduler | conflict log names same write target | CONFLICT-LOG.md |
| Parallel apply refused | scheduler | no concurrent apply; proposals only | DISPATCH-LEDGER.md |
| One integration owner | T-INT | single owner named | INTEGRATION-OWNER.md |
| Dedup by ID | T-INT | skill-alpha appears once | catalog-toy.yaml post |
| No silent overwrite | T-INT | pre/post sha256 + conflict log | catalog-pre/post.sha256 |

## Review focus

- writing-plans Step 2 / anti-pattern: no two independent writers on same mutable artifact without merge owner.
- subagent-driven-dev Step 1/3/8 + anti-pattern: shared catalog → one integration owner; refuse conflicting concurrent mutate.
