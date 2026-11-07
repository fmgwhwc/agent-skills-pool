---
name: fermin-tdd
description: Produces proof that a behavior-changing implementation or regression is correct using observed failing and passing checks. Use for Fermin code changes, bug fixes, refactors, and automatable task/skill contracts; adapt the evidence loop to validation tests when conventional unit tests do not fit.
---

# Fermin Test-Driven Development

## Purpose

Specify behavior with a check before implementing it, watch that check discriminate between absent and present behavior, then implement minimally and run regression evidence. Combine Obra's observed RED/GREEN discipline with Addy's repository-tool discovery and real-boundary testing.

TDD proves selected behavior; it does not replace acceptance, runtime review, source validation, or permission gates. Never make claims beyond what a check exercises.

## Load / do not load

Load when implementing or changing observable behavior, fixing a bug, or changing a validator/parser.

Do not manufacture code tests for pure prose or static content. For skill and research artifacts, use validation fixtures/scenario checks and the documented evidence loop below; not every document needs fictional production code.

Throwaway exploration must remain explicitly exploratory. Promoting it into a deliverable requires the appropriate RED baseline and acceptance evidence, not retroactive labels.

## Evidence loop

```text
Define observable contract → RED (target failure observed)
→ GREEN (minimal change, target pass observed)
→ REGRESSION (relevant integrated checks observed)
→ REFACTOR without behavior change → re-run affected checks
```

A previously passing characterization test may be useful for legacy behavior. Label it characterization, not new-behavior TDD.

## Steps

### 1. Discover the target project's test and validation contract

Read existing manifests, wrappers, test configuration, nearby tests, contributor docs, and CI definitions. Identify:

- focused test command;
- full/relevant suite command;
- test location and naming conventions;
- fixtures and external service boundaries;
- how output and exit status distinguish pass, fail, skip, and error.

Use the project's supported commands and environment. Do not invent `npm test` or install a harness merely for uniformity. If no runnable framework exists, use an existing validator or create the smallest project-appropriate check with its own stated command and expected output.

### 2. Translate one acceptance behavior into a test

Choose one behavior and write a descriptive test. State:

- input and starting condition;
- trigger/operation;
- expected observable result or error;
- why the current artifact cannot satisfy it;
- which regression it prevents.

Prefer public behavior and real state over private method-call assertions. Keep setup local enough to understand the test. Use the simplest test double only at a genuinely nondeterministic, unsafe, slow, or unavailable boundary; test the real implementation where practical.

For bug fixes, reproduce the reported symptom as directly as feasible. An unrelated unit that turns red does not yet prove the original user-visible defect.

For skill/prompt changes, the test can be an intentionally broken skill fixture plus schema/link/provenance validation and one task scenario that differentiates compliant output. A fixture that simply matches the new text proves only text matching.

### 3. RED — run and inspect the failing check

Run the focused check before the implementation change. Retain its command, result, and relevant output.

Expected RED:

- one target behavior absent/wrong;
- failure reason matches that missing behavior;
- no unrelated setup error prevents a meaningful assertion.

If the test passes immediately, determine whether behavior already exists, the test is vacuous, or the wrong path is loaded. If it errors before the intended assertion, repair the test setup or fixture, not the production expectation.

No production-code-before-test for new behavior merely because code was already drafted. Quarantine the draft, write the behavior check, then implement from the contract. Do not delete unrelated or user-owned work while resetting an experiment.

### 4. GREEN — implement the minimum contract

Make only the change needed for the observed failing behavior and its explicitly required interfaces. Do not add speculative options or adjacent cleanups.

Run the focused check again and inspect actual results. If it fails, fix the cause without deleting, skipping, or weakening the intended assertion.

When a test itself was wrong, correct it only with evidence from the authoritative contract; log the correction as a plan/spec ruling where necessary.

### 5. Regression and integration

Run relevant neighboring tests and the project's defined full/required suite when available. Inspect failures, skips, exit codes, and meaningful warnings.

For interfaces, schemas, or content packs, additionally test:

- parsing with the intended consumer, not only a generic YAML parser;
- required fields and source references;
- relative link resolution from the shipped artifact location;
- one realistic use of the produced index or dispatch pack.

Report unrelated pre-existing failures separately; they are not automatically fixed but cannot be hidden.

### 6. REFACTOR while checks protect behavior

Remove duplication, clarify names, and reduce incidental complexity without changing the accepted contract. Re-run each affected focused test and the appropriate regression check after edits.

Do not use the same unchanged command repetitively for reassurance. Run again after a change or to probe a specifically suspected nondeterministic failure, and disclose that reason.

### 7. Preserve the evidence chain

For the task ledger or final report, record:

| Behavior / defect | RED command + observed failure | GREEN command + result | Regression + result | Artifact |
|---|---|---|---|---|

Pair this with `fermin-verification-dod` before saying complete. A green focused test is not a green suite; a suite is not proof that all acceptance criteria are met.

## Test quality guardrails

- Assert behavior, not implementation trivia or the mock's own behavior.
- Cover meaningful failure and edge cases from the contract, not arbitrary coverage targets.
- Use deterministic inputs, state isolation, and project-supported fixtures.
- Prefer one excellent, readable test to many copies in unrelated languages.
- For crash/rollback/external effects, use a safe real or controlled boundary; don't claim a method mock proves process termination, delivery, or database rollback.
- Never run destructive or external side-effect tests against real users or production resources without explicit approval and an appropriate environment.

## Adaptation to skills and structured files

When the deliverable is a Fermin skill:

1. choose a realistic task scenario and required output/evidence;
2. create a missing/invalid fixture or record the prior failing scenario where available;
3. write/change the skill and run structural checks;
4. exercise the scenario and compare the artifact with acceptance;
5. run cross-skill link, source-path, catalog, and contradiction checks.

Historical baseline scenarios or static review alone are weaker than fresh execution. Mark such validation honestly and keep the skill at `candidate` if its required runtime gate has not been run.

## Anti-patterns

| Pattern | Correction |
|---|---|
| “Test passed before the fix; that still counts” | Rebuild a discriminating test or label it characterization. |
| “Full suite means all requirements are done” | Map acceptance and runtime/qualitative evidence separately. |
| Over-mocking until only mocks are verified | Use real behavior at practical boundaries. |
| Broad DEFAULT command without inspecting the repo | Discover its supported focused and full commands first. |
| Delete a red test to make progress | Resolve contract vs implementation explicitly; never hide the finding. |
| Fictional test results in a skill report | Record pending checks as pending and keep candidate status. |

## Done when

- [ ] The target project's actual focused and regression commands were identified or a proportionate validator was explicitly chosen.
- [ ] Each new behavior/defect has a meaningful observed RED or an honestly labeled alternative baseline.
- [ ] The minimal change produced observed GREEN with actual output/exit status.
- [ ] Relevant suite/integration checks ran after final edits and failures/skips are disclosed.
- [ ] Tests verify real observable behavior and include contract-relevant negative cases.
- [ ] Skill-only artifacts used meaningful structural and scenario checks, not pretend unit tests.
- [ ] Evidence is connected to artifacts and acceptance completion remains subject to `fermin-verification-dod`.
