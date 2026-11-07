# Fermin task-pack and report contracts

Use these as artifacts, not as sprawling chat messages. Paths are illustrative; use the project's authorized workspace.

## Dispatch task pack

```yaml
plan_id: "<stable plan id>"
task_id: "T<nn>"
title: "<deliverable>"
surface: "cursor-cloud|ubuntu|dc-bot"
context:
  spec: "<path + approval/version state>"
  plan: "<path>"
  global_constraints:
    - "<exact constraint from spec>"
inputs:
  - path: "<path or authorized URL>"
    role: "<requirements | upstream evidence | interface>"
    revision: "<pin where external>"
outputs:
  - "<exact artifact path>"
  - "<exact report path>"
interfaces:
  consumes: ["<exact names/types/assets>"]
  produces: ["<exact names/types/assets>"]
allowed_changes: ["<bounded paths/actions>"]
prohibited_side_effects:
  - "<external writes, installs, or claims outside grant>"
acceptance:
  - id: "AC-T<nn>-1"
    method: "<command or artifact inspection>"
    expected: "<observable evidence>"
provenance:
  source_repo: "<owner/repo or not-applicable>"
  source_ref: "<full SHA or not-applicable>"
  source_path: "<upstream path>"
  license_spdx: "<SPDX or unknown; unknown cannot release>"
report_contract: "DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED"
```

## Implementer report

```markdown
# Task T<nn> report
Status: DONE | DONE_WITH_CONCERNS | NEEDS_CONTEXT | BLOCKED

## Artifacts
- <path>: <what it is; draft/ready state>

## Executed checks
- <command or inspection>: <actual result and evidence path>

## Contract trace
| Acceptance | Evidence | Result |
|---|---|---|
| AC-... | <artifact / log> | pass | fail | pending |

## Scope and provenance
- Changed: <paths or none>
- Sources used: <repo@ref/path, license>

## Concerns and unattempted checks
- <exact item, effect, and suggested route; or “none”>
```

## Scheduler ledger row

| Task | Dispatch identity / attempt | State | Artifacts | Review / evidence | Decision / blocker |
|---|---|---|---|---|---|

Record an attempt before dispatch. Mark complete only after artifact inspection and acceptance review. Do not treat a return status alone as completion evidence.
