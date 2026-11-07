# PLAN — S07 Code RED/GREEN

| Task | Contract | Output |
|------|----------|--------|
| T01 | Write focused unittest for `is_valid_skill_name` + `name_matches_dir` before real impl | fixture/tests/test_toy_validate.py |
| T02 | Stub SUT that fails the contract (always-True / mismatch) → observe RED | fixture/toy_validate.py + logs/red.* |
| T03 | Minimal GREEN implementation (kebab-case regex + equality) → observe GREEN | fixture/toy_validate.py + logs/green.* |
| T04 | Regression: re-run full fixture suite + characterization of empty/edge | logs/regression.* |
| T05 | Outside-scope inventory/sentinel proof; evidence + WAVE + ledger | scheduler/*; evidence/S07-*.yaml |
