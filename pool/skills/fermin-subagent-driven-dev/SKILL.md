---
name: fermin-subagent-driven-dev
description: Schedules independent Fermin task packs with bounded context, artifact-based reporting, and separate acceptance review. Use when DC Bot coordinates multiple code or skill-production tasks across Cursor Cloud or Ubuntu, or when isolated implementation and review contexts are worth their cost.
---

# Fermin Subagent-Driven Development

## Purpose

DC Bot acts as scheduler and decision owner, not as an additional unreviewed implementer. Convert a plan into atomic task packs, dispatch to supported workers, integrate results, and verify before progressing. Preserve the pool's Bot-closed loop: execution may leave DC Bot; judgment and promotion decisions return to it.

This skill intentionally omits upstream's harness scripts, model-price rules, rigid fix-round caps, worktree assumptions, and required GitHub ceremony. Fermin's artifact contracts replace those runtime bindings.

## Load / do not load

Load when tasks have explicit acceptance, mostly independent write scopes, and fresh implementation or review contexts improve quality.

Do not use it for a trivial edit, one tightly coupled design problem, or an unavailable executor. In those cases use `fermin-executing-plans` or return to planning. Never simulate a dispatch or review.

## Roles and authority

| Role | Owns | Does not own |
|---|---|---|
| DC Bot scheduler | task decomposition, context, ledger, integration, final decisions | fabrication of worker evidence |
| Implementer | bounded artifact production and task evidence | scope expansion, promotion to catalog, self-approval |
| Reviewer | artifact inspection against contract and findings | rewriting scope, subjective rubber stamp |
| Requester / authorized owner | goals, tradeoffs, external and irreversible approvals | duplicated by any skill text |

Separate implementer and reviewer contexts when feasible. If only one context exists, disclose self-review as weaker evidence and apply `fermin-verification-dod`.

## Steps

### 1. Setup and preflight

Read the specification, plan, shared contracts, and ledger. Confirm that selected task surfaces are available. Keep one canonical workspace/ledger; do not create a hidden second pool on a worker.

For every task check:

- dependencies are acyclic and their input artifacts exist;
- output and write scopes are unique or explicitly sequenced;
- required source repo/ref/path/license is known for adapted material;
- attempts and approvals needed on the worker surface are within the task grant;
- task reports will return to DC Bot rather than becoming the final decision themselves.

Group independent research reads where useful, but never serialize false claims of parallel completion. Shared catalog edits get one integration owner.

### 2. Build a task pack

Each task pack points to the minimum authoritative inputs rather than copying the session history. Use [references/task-pack.md](references/task-pack.md) for the complete template.

Required contents:

- stable task and plan IDs;
- purpose and one bounded deliverable;
- input artifact paths and exact source references;
- upstream interface inputs and required outputs;
- allowed write scope and prohibited side effects;
- concrete acceptance commands/checks and expected results;
- required provenance, quality gate, and report path;
- explicit completion states.

Use this contract:

```text
DONE: contract and checks satisfied; evidence paths returned.
DONE_WITH_CONCERNS: artifact exists but a disclosed issue remains for adjudication.
NEEDS_CONTEXT: a specific missing decision/input prevents valid work.
BLOCKED: unavailable tool, failed check, or denied permission prevents completion.
```

The worker returns a concise status and artifact pointers. The complete report lives at its declared path. “DONE” is a claim for review, not automatically truth.

### 3. Dispatch only ready work

Dispatch tasks in dependency order. Independent tasks may run concurrently only if they do not mutate the same asset, account, environment, or finite resource in a conflicting way.

Choose a worker by required capability and supported surface, not generic prestige or an unverifiable cost claim. Record dispatch identity, attempt, state, inputs, and report path in the ledger.

Give the implementer the original task requirements, not an unchecked paraphrase. For changes that depend on a prior decision, include its exact contract and location rather than pasting a growing narrative.

### 4. Control work while it runs

Continue useful scheduler work: validate completed artifacts, prepare independent briefs, update the ledger, and reconcile dependencies. Follow the host's recommended waiting and progress mechanisms; do not poll continuously.

On worker questions, answer from the authoritative spec or return a scope decision to the requester. Do not let a worker change acceptance silently to obtain DONE.

For an interrupted/resumed worker, supply its original brief, exact evidence state, and remaining gap. Do not start a duplicate worker that may overwrite the same artifact.

### 5. Adjudicate the report

| State | Scheduler action |
|---|---|
| DONE | Read report and artifact, assemble acceptance package, review. |
| DONE_WITH_CONCERNS | Inspect concerns and artifact; accept only after review and documented reversible adjudication. |
| NEEDS_CONTEXT | Resolve the exact missing input or replan; do not count as completion. |
| BLOCKED | Record blocker and failed check; retain usable partial output separately. |

Check provenance and scope even if the worker reports success. Any unexpected external side effect, secret, license gap, or unsafe content stops promotion and requires explicit handling under governing rules.

### 6. Review task output independently

Send the reviewer the task contract, result artifact, evidence report, and the factual source specification for comparison rather than inference. For code, provide the relevant change artifact; for skills, the SKILL/meta/catalog material and scenario results.

Review axes:

- fidelity to the requested outcome and task boundaries;
- observable acceptance evidence;
- integration contract and schema/link correctness;
- content quality, minimal context load, and absence of upstream harness residue;
- provenance/license completeness and unapproved content.

The scheduler checks claimed outputs against the artifacts and required tests. Review authority does not permit either agent to silently discard a finding; log accepted fixes, rejected findings with rationale, and deferred minors.

### 7. Use a bounded evidence-driven fix loop

For material accepted findings, send the exact finding and unchanged acceptance contract back to the same worker or a new scoped implementer. Verify the fix with a failing-before/passing-after check when possible and targeted re-review.

There is no magic round count. Stop revising when the next attempt would exceed authority, overwrite good work, repeat a structurally failing approach, or cost more than re-planning. Record that decision; do not park a requirement-blocking defect to claim completion.

### 8. Integrate, final-review, and close

Only mark a task complete when all required acceptance checks are supported by evidence or its output is explicitly demoted to draft/blocked. `DONE_WITH_CONCERNS` does not equal release-quality.

After all tasks, run the integrated check and a cross-task review: links, schemas, catalog collisions, source/license consistency, contradictory instructions, and acceptance coverage. DC Bot returns delivered paths, evidence, open risks, and the next permitted action.

## Anti-patterns

| Pattern | Correction |
|---|---|
| Dispatching whole chat history | Provide the bounded contract and referenced artifacts. |
| Worker self-reports become merge approval | Scheduler verifies independently before promotion. |
| Two workers each edit the catalog | Assign one integration owner and sequential writes. |
| Adding a reviewer inside the implementer task without need | Let the scheduler assign the intended review context; disclose any proxy review. |
| Looping on red checks indefinitely | Diagnose, bound, escalate, or re-plan with findings. |
| Repeating upstream model tier claims as facts | Select by available capability and observed task need. |

## Done when

- [ ] Every dispatch has a completed task pack and an available, authorized executor.
- [ ] Shared mutations were sequenced and integration ownership is explicit.
- [ ] Each status is backed by an inspectable report and artifacts; no worker success was blindly trusted.
- [ ] A separate-review disclosure or independent review exists for every accepted result.
- [ ] Accepted findings were fixed and rechecked; rejected/deferred ones have rationales.
- [ ] Provenance, links/schema, cross-skill consistency, and integrated acceptance were checked.
- [ ] DC Bot owns the final ledger and does not mark unresolved concerns as released.
- [ ] No cloud, GitHub, external-message, or other permission-expanded action occurred without its own grant.
