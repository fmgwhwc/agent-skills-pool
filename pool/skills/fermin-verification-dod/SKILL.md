---
name: fermin-verification-dod
description: Gates Fermin completion claims on fresh artifact-linked evidence and reconciles task acceptance with a stable Definition of Done. Use when marking a task, skill, task pack, or indexed asset complete, ready, or released, or when handing a result to the requester.
---

# Fermin Verification and Definition of Done

## Purpose

Make completion a traceable evidence decision rather than a sentence that feels plausible. Reconcile two distinct standards:

- **Acceptance criteria:** did this request produce the intended outcome?
- **Definition of Done (DoD):** does the result meet Fermin's standing integrity, quality, integration, provenance, and handoff floor?

Both are required. The route to completion can be `pass`, `draft`, `blocked`, or `partial`; a file's existence or a subagent's DONE alone is never enough.

## Load / do not load

Load before any completion/release claim, task transition, pool promotion, or integrated handoff.

Do not use it as a reason to run unrelated tests continuously, redo unchanged checks without cause, or convert every low-risk read into heavyweight QA. Select verification proportional to the claim and its risk.

## Evidence standard

Evidence must be:

- **fresh:** gathered after the relevant final change;
- **specific:** names command/inspection, actual result, and artifact;
- **scoped:** says what it proves and what it does not;
- **traceable:** linked to requirement, source, output path, and ledger;
- **honest:** separates passes, failures, skips, unattempted checks, foreign tests, and self-review.

“Should pass,” “looks right,” and quoted success claims are status leads, not evidence.

## Steps

### 1. Bind the claim to its exact artifact

Write the intended claim and scope:

```yaml
claim: "<task complete | candidate ready | released>"
plan_or_request: "<path/reference>"
artifacts: ["<exact paths/versions>"]
acceptance_source: "<spec/plan/task/request>"
verification_time: "<actual timestamp + timezone>"
surfaces_checked: ["dc-bot|cursor-cloud|ubuntu"]
```

Check that the artifact to be verified is the artifact to be delivered. Do not validate a different draft or a cache while presenting a newer asset as ready.

### 2. Build the acceptance matrix

For every explicit requirement, identify an observable check and evidence location. Include non-goals and negative outcomes where relevant.

| Requirement | Check / expected result | Actual evidence | State |
|---|---|---|---|
| `<AC-ID>` | `<command, inspection, scenario>` | `<path + observed result>` | `pass/fail/pending/not-run` |

If acceptance is missing or reduced to “it works,” return to the spec/plan rather than retrofitting a lower standard after seeing the result.

### 3. Run or obtain fresh checks

Appropriate evidence includes:

- project test/build commands with exit result and observed counts;
- original bug/symptom reproduction after fix;
- actual runtime output, DOM, file read, query result, or consumer parsing;
- schema, frontmatter, reference/path, and relative-link validation;
- independent task/peer review with named verdict and limitations;
- cross-skill consistency and source/repo/ref/path/license checking.

Re-run unchanged verification only when a risk-specific reason exists. Otherwise cite the fresh result and ensure no change invalidates it.

Do not count a check as performed because it was planned, a worker announced it, or a historical report says it passed. Cite the actual fresh evidence or mark `not-run`.

### 4. Apply the standing DoD

Use [references/fermin-dod.md](references/fermin-dod.md) at the appropriate scope:

- **task:** required task checks, content/domain quality, scoped changes, blockers;
- **integrated asset:** cross-item constraints, links/schema, final consumer use, completed ledger;
- **pool candidate:** all integrated checks plus provenance/license and quality gate;
- **external release:** separate permission, delivery, and environment gates outside this skill.

Mark each item `pass`, `fail`, `pending`, or `N/A` with a reason. `N/A` requires an observable reason, not “I did not want to check.”

### 5. Reconcile discrepancies

- Red check or failed acceptance: `fail`; do not mark complete.
- Unavailable required check: `pending` or `blocked`; keep candidate/draft.
- Not-applicable optional check: record why.
- Self-review only: disclose weaker independence; require the proper reviewer for higher-risk promotion.
- Unchecked upstream factual claim: attribute to source and mark provisional; do not transform author marketing into verified performance.
- Unexpected scope or permission concern: hold promotion and route to the authorized owner.

Record each deviation and resolution in the ledger. Re-grade findings by effect on the consumer, not just the severity label of an upstream or reviewer.

### 6. Decide the status and report precisely

Use one of:

| Status | Requirement |
|---|---|
| `verified-complete` | Every required acceptance/DoD item passes for the declared scope. |
| `candidate` | Static and available checks pass, but explicitly named runtime/human gates remain. |
| `partial` | Useful bounded output exists, with failed or missing required items. |
| `blocked` | Missing input, permission, environment, or material failure prevents valid closure. |

Return delivered paths, exact evidence, limitations, rulings, and the permitted next step. Preserve blockers and deferred items instead of deleting the ledger to “finish clean”.

## Pool minimum gate

A Fermin skill can be a candidate when:

1. source ownership, full commit SHA, exact paths, and permissive license are recorded and traceable;
2. its trigger, steps, exclusions, and done-when checks are concrete;
3. required references travel inside the skill directory or an explicit package contract;
4. catalog entry and directory agree; links resolve from shipped location;
5. duplicate capabilities are merged and no upstream installer/telemetry/marketing workflow remains;
6. static and content checks pass.

Before `released`, it additionally needs a realistic scenario run in an intended Fermin surface and acceptance by the designated pool owner. “No discovered issues in author review” is not runtime proof.

## Anti-patterns

| Claim | Evidence required |
|---|---|
| “8 skills complete” | Eight shippable directories, structural checks, content links, catalog consistency, and honest runtime status. |
| “Worker DONE” | Artifact inspection plus acceptance evidence and scoped review. |
| “All tests pass” | Actual fresh suite command/output, scope, exit status, failures/skips. |
| “License-compatible” | Exact upstream source at fixed revision and applicable license text, not repository popularity. |
| “Production-grade / best practice” | Attributed upstream claim plus Fermin scenario evidence; otherwise provisional. |
| “Doc-only change needs no verification” | Links, paths, schema, consumer use, and changed claims still get appropriate checks. |

## Done when

- [ ] Claim, artifact version/location, acceptance source, and verification scope are bound together.
- [ ] Every acceptance criterion maps to fresh evidence or an explicit non-pass state.
- [ ] Integrated and project-specific checks were selected and run after final edits.
- [ ] DoD results include failures, skips/pending, N/A rationale, and review independence.
- [ ] For pool material, exact provenance/permissive licensing, portable references, dedup, and quality gates are checked.
- [ ] Final status matches evidence; no downstream approval is inferred from technical verification.
- [ ] Handoff names evidence, blockers, residual risks, and next permitted action.
