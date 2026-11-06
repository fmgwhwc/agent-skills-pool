---
name: fermin-writing-plans
description: Converts an approved Fermin decision or specification into resumable task packs with explicit inputs, interfaces, evidence, and dependencies. Use when preparing multi-step implementation, research-to-index conversion, or a handoff to Cursor Cloud, Ubuntu, or another agent.
---

# Writing Fermin Plans

## Purpose

Preserve the decisions another executor cannot infer from the request. A plan is the durable contract between a specification, workers, and verification; it is neither a transcript of imagined code nor a list of vague aspirations.

Use a plan only when there is a decision record/specification or equivalently concrete accepted request. If scope or acceptance is unsettled, return to `fermin-brainstorm-or-spec`.

## Load / do not load

Load for multiple dependent outputs, nontrivial implementation, delegated task packs, or work that may be interrupted and resumed.

Do not load for a single unambiguous read/edit. Do not duplicate an existing plan when updating its ledger is sufficient.

## Plan unit

A task is the smallest unit that:

- has a distinct deliverable and acceptance check;
- can be reviewed independently from its neighbors;
- states the inputs and interfaces it consumes and produces;
- can be completed without unexplained coordination with a parallel writer.

Fold necessary setup and documentation into the task that needs them. Split by capability, not by arbitrary file count or number of commands.

## Steps

### 1. Establish the canonical artifacts

Choose a project-owned location or authorized scratch workspace. Name:

- one plan file;
- one progress ledger;
- one directory for task briefs and reports;
- the source specification and its status;
- the output/index destinations.

For pool work, keep drafts separate from released entries. Do not put analysis scratch into `pool/skills` merely because a skill is planned.

### 2. Map dependencies and contracts

Identify inputs, outputs, consumers, and direction of dependency. Use exact paths, IDs, fields, signatures, schema versions, and selected values where they matter.

Preflight the interfaces between tasks. Resolve contradictions against the controlling specification. Do not assign two independent writers the same mutable artifact; make that artifact a sequential integration task or define a merge owner.

### 3. Write the plan header

```markdown
# <Title> — Execution Plan
Plan-ID: <stable id>
Spec: <path / reference and approval state>
Goal: <one observable sentence>
Required route: fermin-executing-plans | fermin-subagent-driven-dev
Ledger: <path>

## Decision constraints
[Verbatim values, scope limits, formats, provenance, platform and approval constraints.]

## Shared contracts
[Schemas, IDs, exact interfaces, locations, base/ref where relevant.]

## Acceptance and evidence map
[Requirement -> owning task -> concrete check -> retained artifact.]

## Review focus
[High-impact behavior, failure modes, untrusted-data boundaries, or omitted cases.]
```

If there is no reachable specification, name the accepted request used instead and mark interpretations as proposed until properly accepted.

### 4. Author each task contract

```yaml
task_id: T01
title: "<result, not activity>"
depends_on: []
surfaces: ["dc-bot|cursor-cloud|ubuntu"]
inputs:
  - "<exact path, pinned source, or approved artifact>"
outputs:
  - "<exact file / index / report path>"
allowed_changes:
  - "<bounded write scope>"
consumes:
  - "<exact upstream interface or decision>"
produces:
  - "<exact interface downstream tasks will use>"
steps:
  - "<action plus checkable expected result>"
acceptance:
  - id: AC-T01-1
    check: "<test, comparison, query, or artifact review>"
    expected: "<observable pass condition>"
evidence:
  - "<log/result/report destination>"
```

For behavior changes covered by automated tests, specify a RED check, its expected failure reason, the minimal implementation boundary, then the GREEN and regression checks. Do not prescribe a test framework before inspecting the project.

For research/skill work, replace code-only steps with selective source reads, provenance capture, drafting, link/schema checks, scenario testing, and catalog verification. A task whose only acceptance is “understand X” is incomplete: define the decision it supports and the evidence in its output.

### 5. Specify evidence and exception behavior

Every command-based check needs its actual project command, expected result, and output destination. Every qualitative review needs the artifact, criterion, and reviewer role.

Tell the executor where to record deviations and what to do when an input is absent. Approval-bound actions remain gated regardless of how the plan phrases the next step.

### 6. Self-review against the source contract

Check backward from each source requirement to a task and then to evidence. Check forward from every task to a needed outcome; cut orphan work.

Check:

- exact names and types agree across tasks;
- dependencies are acyclic;
- no parallel writers collide;
- acceptance covers negative and error cases, not just happy paths;
- provenance/license gates exist where external material is adapted;
- plan length stays below the cost of the actual work;
- blank “handle appropriately” placeholders are replaced with decisions or explicit gates.

### 7. Publish the executable route

Link the plan, specification, and ledger. Choose:

- `fermin-executing-plans` for one executor and local convergence;
- `fermin-subagent-driven-dev` for separable work needing isolated task contexts and review;
- a direct read-only response when no execution plan was necessary after all.

Review/approval requirements come from the work, not from an automatic “stop after every plan” rule.

## Anti-patterns

| Pattern | Correction |
|---|---|
| “Create useful tests” | Name behavior, input, assertion, command, and expected evidence. |
| “Use SHA-pinned sources” without pins | Put exact repo/ref/path in the inputs and provenance contract. |
| Multiple tasks rewrite the same catalog independently | Make integration sequential with one owner and conflict checks. |
| Plan supplies the whole implementation | Retain signatures, decisions, and tests; remove derivable bodies. |
| Acceptance only asks whether a file exists | Validate its contract, content, links, and intended use. |
| Planning bypasses a required permission | Keep the gate explicit and separate from asset approval. |

## Done when

- [ ] The plan points to the controlling spec/request and one canonical ledger.
- [ ] Tasks are independently acceptable and ordered by explicit dependencies.
- [ ] Inputs, output paths, allowed changes, interfaces, and execution surfaces are concrete.
- [ ] Each task has observable acceptance and a place for retained evidence.
- [ ] Tests use the target project's discovered tools; research/skill tasks have source and quality checks.
- [ ] Shared artifact ownership and integration order prevent parallel overwrite/conflict.
- [ ] A forward/backward coverage review found no unsourced scope or unowned requirement.
- [ ] The next executor skill is named and required approvals remain intact.
