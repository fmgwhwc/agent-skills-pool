# Catalog lint note

TASK-ID: T-A
plan_id: plan-s05-dispatch-isolation

## Idea
A lightweight catalog lint would check that each skill directory name matches
its meta.yaml `id`, that `path` fields agree with on-disk location, and that
duplicate IDs are rejected before merge.

## Non-goals
- Not a pool promotion or release claim.
- Toy prose for S05 dispatch isolation only.
