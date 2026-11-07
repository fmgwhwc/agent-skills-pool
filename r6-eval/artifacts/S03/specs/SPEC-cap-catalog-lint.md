# Decision / Spec: Candidate micro-skill — catalog lint acceptance
ID: cap-catalog-lint
Status: authorized-default

## Outcome and beneficiary
A *candidate* micro-skill acceptance contract (not a full SKILL.md body in this S03 run) for pool-maintenance linting of `catalog.yaml` / skill-entry schema, so Fermin can later author `fermin-catalog-lint` without inventing acceptance after the fact. Beneficiary: pool maintainers and R6/W5 release gating.

## Inputs and observed current state
- `r5-adapt-batch/schema/skill-entry.schema.json` (required fields listed)
- `r5-adapt-batch/schema/catalog.base.yaml` / `pool-skeleton/catalog.yaml` (version/updated/entries)
- `r5-adapt-batch/catalog-entries.yaml` (eight-entry overlay; merge-by-id)
- Eight existing skills remain untouched this run

## Scope
In:
- Stable capability ID `cap-catalog-lint`
- Proposed skill id `fermin-catalog-lint` (status would be `candidate` if authored later)
- Acceptance criteria for lint behavior (good/bad fixtures)
- Catalog-entry *payload sketch* for later T-INT merge (fields only; no live catalog write)

Out / anti-goals:
- Implementing full `SKILL.md` / shipping into `pool/skills/` in S03
- Mutating live `catalog.yaml` from this capability's worker
- Replacing `validate_r5.py` wholesale (may *call* or complement it later)
- GitHub push / PR

## Decisions and alternatives
| Decision | Choice | Alternatives | Owner |
|---|---|---|---|
| Capability id | `cap-catalog-lint` | `cap-pool-catalog-validate` | Fermin proposed; authorized-default for S03 |
| Skill package name (future) | `fermin-catalog-lint` | fold into validate_r5 docs only | Fermin proposed |
| Catalog writes | forbidden in this capability; deferred to T-INT | allow worker to append catalog | writing-plans anti-pattern forbid |
| Depth this run | acceptance + payload sketch only | full SKILL body | parent brief |

## Execution contract
Surfaces: dc-bot
Allowed reads: r5-adapt-batch schema/catalog overlay; pool-skeleton; r6-eval
Allowed changes (when executed later under a plan task): only `pool/skills/fermin-catalog-lint/**` draft area + task report — **not** `catalog.yaml`
Dependencies: none (peer of `cap-evidence-ledger`)

## Acceptance
- AC-1 Stable ID `cap-catalog-lint` appears in capability map and this spec → artifact review
- AC-2 Independent check named: bad fixture rejected for intended pin reason; good fixture passes; source unchanged → would be evidenced when skill is authored (S03 records the check contract only)
- AC-3 No write to shared `catalog.yaml` by this capability's worker → plan task `allowed_changes` omits catalog
- AC-4 Catalog-entry payload sketch includes schema-required keys (id, status, source, license_spdx, decision, rationale, fermin_tags, epistemic) → artifact review

## Risks, assumptions, and open questions
- Assumption: S03 validates splitting/planning, not runtime of the future skill (effect: no false release claim).
- Unknown: owner may defer actual authoring; S03 still passes if split/plan contracts are sound.
- Risk: naming collision with validate_r5 — mitigate by framing skill as *acceptance workflow* around lint, not a second validator binary.

## Catalog-entry payload sketch (for T-INT only; not applied)
```yaml
id: fermin-catalog-lint
path: pool/skills/fermin-catalog-lint
status: candidate
source:
  repo: fmgwhwc/agent-skills-pool
  ref: local-s03-proposal
  path: pool/skills/fermin-catalog-lint/SKILL.md
  url: local://s03-proposal/fermin-catalog-lint
license_spdx: MIT
decision: adapt
rationale: "Pool-maintenance acceptance skill for catalog/entry schema lint; keeps lint gates out of ad-hoc chat."
fermin_tags: [pool-maintenance, catalog, lint, r6]
epistemic: provisional
```
