# Capability map — S03 pool-maintenance micro-skills

Stimulus: propose two independently testable *candidate* micro-skills for pool maintenance, plus one shared `catalog.yaml` integration.

Split verdict (**fermin-brainstorm-or-spec Step 2**): **split** — distinct consumers/assets, independent acceptance, either skill removable without rewriting the other.

| Capability ID | Outcome / asset | Depends on | Independent acceptance |
|---|---|---|---|
| `cap-catalog-lint` | Candidate micro-skill package `fermin-catalog-lint` (acceptance contract for linting catalog/entry schema) | none | Fixture catalog with one known-bad entry is rejected for the stated pin reason; good fixture passes; source tree unchanged |
| `cap-evidence-ledger` | Candidate micro-skill package `fermin-evidence-ledger` (acceptance contract for r6-eval ledger/evidence hygiene) | none | Ledger row + evidence YAML pair for a fixture scenario satisfy template fields; missing `result` or orphan evidence path is rejected |

**Shared mutable asset (not a third capability):** `catalog.yaml` (and/or merge overlay). Must not have two parallel writers.

**Dependency direction (acyclic):**

```
cap-catalog-lint ────────┐
                         ├──► T-INT catalog integration (single owner)
cap-evidence-ledger ─────┘
```

Neither capability depends on the other. Integration consumes both packages' catalog-entry payloads and performs a single sequential merge.
