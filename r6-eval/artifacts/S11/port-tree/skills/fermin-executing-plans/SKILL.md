---
name: fermin-executing-plans
description: Executes a Fermin plan in one accountable session while preserving a resumable evidence ledger. Use when a single executor owns the tasks on DC Bot, Cursor Cloud, or Ubuntu, or when task-by-task subagents are unavailable or unnecessary.
---

# Executing Fermin Plans

## Purpose

Carry an accepted plan through implementation and evidence collection without losing its decisions at compaction or handoff. The plan defines the work; this skill governs execution quality. It does not authorize deployment, repository writes, external messaging, or any other separate action.

## Load / do not load

Load when one executor will perform a multi-step plan, especially when later tasks depend on earlier outputs.

Do not load for isolated tasks needing no plan, or when `fermin-subagent-driven-dev` has been selected for task-isolated parallel/dispatched execution. Do not switch execution modes without updating the same ledger.

## Terms

- **Spec/request:** binding outcome and constraints.
- **Plan:** selected tasks and contracts, subordinate to the spec/request.
- **Ledger:** durable execution facts: current task, artifacts, checks, rulings, and blockers.
- **Ruling:** a small, reversible interpretation within granted scope; it is never a substitute for permission or a changed requirement.

## Steps

### 1. Preflight and resume

Read the plan, specification/request, global constraints, and current ledger. Confirm that task input paths and required tools exist.

If the ledger identifies this same plan, resume at its first incomplete task. Do not reproduce completed artifacts merely because the conversation no longer remembers them; verify their existence and references first. If it belongs to another plan, leave it untouched and create a separate workspace.

Initialize or restore:

```markdown
# Fermin execution ledger
Plan: <canonical plan path>
Spec/request: <path/reference>
Execution surface: <dc-bot|cursor-cloud|ubuntu>
State: <preflight|in-progress|blocked|ready-for-final-review>

| Task | State | Output | Evidence | Ruling / blocker |
|---|---|---|---|---|
| T01 | pending | <path> | <path> | <none> |
```

Check interface consumers against producers before the first task. Record a conflict and its authorized resolution before it becomes hidden rework.

### 2. Take exactly one owned task

Read the current task's exact contract, not a recollected summary. Mark it `in-progress`. Check its dependencies are complete and inputs match expected IDs or versions.

Keep attention on the task's allowed changes and acceptance. Do not “improve” unrelated areas.

### 3. Execute the contract in order

For each action, compare the actual result with the expected result.

- **Behavioral code change:** load `fermin-tdd`; preserve observed RED and GREEN evidence.
- **Research or skill content:** use the pinned sources, record source paths/ref/license, run the scenario/content checks, and keep rejected alternatives visible.
- **Interface/data conversion:** run structural validation plus a representative roundtrip or downstream use.
- **Qualitative review:** inspect the actual artifact against the named criterion and produce a finding or explicit pass.

Store large results in the task workspace and retain references, exit results, counts, and material failures in the ledger. Do not flood the conversation with content that can live in an artifact.

### 4. Handle deviation without silent drift

If implementation is wrong, diagnose and fix the cause within scope. If the plan is wrong, record the smallest authorized ruling:

```text
T<NN> Ruling: <conflict> — <decision and reason> — <cost/risk if wrong> — <outputs updated>
```

Update the affected contract and ledger so downstream tasks consume the ruling. If the conflict changes user goals, acceptance, external effects, cost, or safety/approval boundaries, stop and obtain the required decision.

Unresolved material failures remain `blocked` or `pending`. Never rename a check to make a red result appear compliant.

### 5. Close a task with acceptance evidence

Before marking it complete:

1. run the task's fresh verification;
2. read its real result and output;
3. inspect that the intended artifact was written at the declared path;
4. run relevant regression/schema/link checks;
5. use `fermin-verification-dod` to reconcile with acceptance.

Record the command or check, observed result, artifact path, and unresolved issues. Only then mark it `complete`.

A failure that predated the task may be out of repair scope but is not out of the report. Record it explicitly.

### 6. Integrate and perform final review

After all tasks, inspect the combined result against the source acceptance map. Task-local success is insufficient if contracts no longer compose or the index points at the wrong assets.

Use an independent reviewer when available and proportionate to risk. Re-grade findings by observable effect, not by whether the spec happened to predict them. Fix acceptance-blocking findings within scope and rerun their checks; keep deferred minor items visible with reasons.

### 7. Handoff

Return:

- delivered paths and their status;
- evidence actually executed and key results;
- rulings that an owner should know;
- blocked/unattempted checks;
- residual risk and the next permitted step.

Retain plan and ledger history. Do not delete the sole record of unresolved work as a “cleanup”.

## Anti-patterns

| Pattern | Correction |
|---|---|
| Doing an adjacent refactor while executing | Return to the task boundary; propose it separately. |
| Red test fixed by weakening its assertion | Restore the contract; fix implementation or escalate a real contract change. |
| “Tests are probably green” | Run and cite the fresh result. |
| Relying on worker or memory status | Check the ledger, artifact, and independent evidence. |
| Unlogged plan deviation | Record an in-scope ruling or stop for an out-of-scope decision. |
| Finishing by deleting blockers | Preserve the ledger and name the unresolved checks. |

## Done when

- [ ] Resumption used the correct plan and one canonical ledger.
- [ ] Every completed task has fresh, artifact-linked acceptance evidence.
- [ ] Relevant regression and integrated checks ran, or gaps are explicitly pending.
- [ ] Each plan deviation is an authorized, documented ruling with downstream effects recorded.
- [ ] No separate permission was inferred from executing an approved plan.
- [ ] Final handoff includes all material rulings, deferred items, blockers, and output paths.
- [ ] Output locations and index/catalog references point to the delivered assets.
