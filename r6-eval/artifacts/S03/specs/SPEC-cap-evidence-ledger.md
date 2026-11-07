# Decision / Spec: Candidate micro-skill — evidence ledger acceptance
ID: cap-evidence-ledger
Status: authorized-default

## Outcome and beneficiary
A *candidate* micro-skill acceptance contract for keeping `r6-eval/ledger.md` and `r6-eval/evidence/*.yaml` consistent (template fields, scenario id pairing, no orphan evidence). Beneficiary: R6 wave runners and candidate→release reviewers.

## Inputs and observed current state
- `r6-eval/evidence/_template.yaml` (required evidence fields)
- `r6-eval/ledger.md` + `scenarios.yaml` (wave↔scenario pairing)
- Existing evidence: S01, S02, S08 (pass; same-author-self-review noted)
- Peer capability `cap-catalog-lint` (no dependency)

## Scope
In:
- Stable capability ID `cap-evidence-ledger`
- Proposed skill id `fermin-evidence-ledger` (future `candidate`)
- Acceptance criteria for ledger/evidence hygiene
- Catalog-entry payload sketch for T-INT

Out / anti-goals:
- Full SKILL.md authoring in S03
- Rewriting historical evidence files except via explicit later tasks
- Owning `catalog.yaml` merges
- Claiming statistical quality from one scenario

## Decisions and alternatives
| Decision | Choice | Alternatives | Owner |
|---|---|---|---|
| Capability id | `cap-evidence-ledger` | `cap-r6-ledger-hygiene` | Fermin proposed; authorized-default |
| Coupling to catalog-lint | none (peer) | evidence-ledger depends on catalog-lint | rejected — independent acceptance |
| Catalog writes | deferred to T-INT | worker appends catalog | forbidden by writing-plans |
| Depth this run | acceptance + payload sketch | full SKILL | parent brief |

## Execution contract
Surfaces: dc-bot
Allowed reads: r6-eval/**; scenario registry; evidence template
Allowed changes (later task): only `pool/skills/fermin-evidence-ledger/**` draft + task report — **not** `catalog.yaml`
Dependencies: none

## Acceptance
- AC-1 Stable ID `cap-evidence-ledger` in map + this spec → artifact review
- AC-2 Independent check: fixture ledger row + evidence YAML with all template fields pass; missing `result` or path that does not exist fails → contract recorded (runtime when authored)
- AC-3 No shared-catalog write by this capability's worker → plan `allowed_changes`
- AC-4 Payload sketch has schema-required keys → artifact review
- AC-5 Peer independence: removing this capability does not require rewriting `cap-catalog-lint` spec → map review

## Risks, assumptions, and open questions
- Assumption: ledger remains markdown table; skill describes checks, not a new DB.
- Risk: overlap with `fermin-verification-dod` — mitigate by scoping to *r6-eval evidence/ledger mechanics*, not general DoD matrices.
- Unknown: whether ledger format will gain YAML companion later; out of S03 scope.

## Catalog-entry payload sketch (for T-INT only; not applied)
```yaml
id: fermin-evidence-ledger
path: pool/skills/fermin-evidence-ledger
status: candidate
source:
  repo: fmgwhwc/agent-skills-pool
  ref: local-s03-proposal
  path: pool/skills/fermin-evidence-ledger/SKILL.md
  url: local://s03-proposal/fermin-evidence-ledger
license_spdx: MIT
decision: adapt
rationale: "Pool-maintenance acceptance skill for r6-eval ledger/evidence pairing and template completeness."
fermin_tags: [pool-maintenance, evidence, ledger, r6]
epistemic: provisional
```
