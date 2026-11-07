# SPEC — S07 Code RED/GREEN (disposable toy)

## Goal
Implement a tiny skill-name validator in a disposable fixture under `artifacts/S07/fixture/` using observed TDD (RED → GREEN → REGRESSION). Prove no unrelated user/pool files outside the fixture were deleted or changed.

## Acceptance
1. Focused test command exists and is runnable without pytest (stdlib unittest).
2. Meaningful RED observed for missing/wrong behavior (failure reason matches contract).
3. Minimal GREEN fix makes the focused tests pass.
4. Regression/neighbor check re-run after GREEN still passes.
5. Sentinel + inventory outside `fixture/` unchanged.
6. Evidence YAML + WAVE report + ledger/scenarios updated; zip ready.
7. Do not mutate production `pool/skills` or real `validate_r5.py` as SUT.

## Non-goals
GitHub pushes; skill release promotion; patches unless skill forced skipping RED / deleting outside scope.
