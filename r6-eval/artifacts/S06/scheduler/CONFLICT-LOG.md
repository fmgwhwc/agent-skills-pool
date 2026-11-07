# S06 Conflict log — shared-write collision

Timestamp: 2026-11-07 08:34:39 CST (Asia/Shanghai)
Scheduler skills: fermin-writing-plans (Step 2 / anti-pattern shared writers) + fermin-subagent-driven-dev (Step 1/3/8 + anti-pattern catalog)

## Detection

| Check | Result |
|-------|--------|
| TP-W1 desired_write_targets ∩ TP-W2 desired_write_targets | `artifacts/S06/shared/catalog-toy.yaml` — **COLLISION** |
| Proposal target_path equal | both → same catalog path — **COLLISION** |
| Entry ID overlap | `skill-alpha` proposed by both W1 and W2 — **ID COLLISION** |
| Live catalog before apply | sha256 `91cf1015bc84b84d7424ee60bc4d0bb0ecd3e2d444772082f55887454ef424b5` (unchanged by workers) |

## Ruling

1. **Refuse parallel apply** of W1 and W2 proposals to the live catalog.
2. **Appoint one sequential integration owner**: `T-INT`.
3. **Merge order**: apply W1 ops first, then W2 with ID collision gate.
4. **Dedup by ID**: `skill-alpha` appears once in final catalog.
5. **No silent overwrite**: W2's overlapping `skill-alpha` update rejected and logged; W1's alpha fields kept; W2's non-overlapping `skill-beta` update applied; W1's `skill-delta` add applied; `skill-gamma` untouched.

## Counterfactual (what silent last-writer-wins would have done)

- `skill-alpha.notes` would have become W2's overlapping claim (see ADJUDICATION.json `counterfactual_silent_overwrite_alpha_notes`).
- Actual post notes remain W1's — overwrite prevented.

## Events

1. update_applied skill-alpha ← W1
2. add_applied skill-delta ← W1
3. update_applied skill-beta ← W2
4. id_collision skill-alpha ← W2 → conflict_resolved_keep_first (W2 rejected)
