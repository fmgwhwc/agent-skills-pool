# Task T-INT report
Status: DONE

## Artifacts
- r6-eval/artifacts/S06/shared/catalog-toy.yaml: post-integration catalog
- r6-eval/artifacts/S06/scheduler/CONFLICT-LOG.md
- r6-eval/artifacts/S06/scheduler/catalog-pre.sha256 / catalog-post.sha256
- r6-eval/artifacts/S06/scheduler/ADJUDICATION.json

## Executed checks
- Collision detect on write-target intersection: pass
- Parallel apply refused: pass
- Sequential merge W1→W2 with ID gate: pass
- skill-alpha unique; notes remain W1 (not W2 overwrite): pass
- skill-beta updated; skill-delta added; skill-gamma baseline retained: pass

## Contract trace
| Acceptance | Evidence | Result |
|---|---|---|
| Collision detected | CONFLICT-LOG.md | pass |
| One owner | INTEGRATION-OWNER.md | pass |
| Dedup by ID | catalog post + ADJUDICATION.json alpha_count=1 | pass |
| No silent overwrite | pre/post sha + rejected W2 alpha in conflict_events | pass |

## Scope and provenance
- Changed: shared/catalog-toy.yaml (sole apply)
- Sources used: W1/W2 proposals against catalog-pre

## Concerns and unattempted checks
- none for toy scope; merge priority (first-proposer) is documented choice, not a general catalog policy claim
