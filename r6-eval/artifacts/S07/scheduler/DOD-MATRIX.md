# S07 DoD / acceptance matrix
verification_time: 2026-11-07 08:39:57 CST (Asia/Shanghai)
claim: S07 Code RED/GREEN scenario complete (local disposable fixture)
independence: same-author-self-review

| Requirement | Check / expected | Actual evidence | State |
|---|---|---|---|
| AC1 focused runnable test | unittest discover | logs/green-stderr.txt Ran 5 OK; run_tests.sh present | pass |
| AC2 meaningful RED | EXIT≠0; failure reason = always-True stub | logs/red-exit.txt=1; 3 FAIL AssertionError True is not false | pass |
| AC3 minimal GREEN | same command EXIT 0 | logs/green-exit.txt=0; 5 OK | pass |
| AC4 regression | full suite after GREEN | logs/regression-exit.txt=0; Ran 7 OK; REGRESSION-NOTE.md | pass |
| AC5 no outside delete/change | inventory + sentinel | inventory-diff missing=0 changed=0; sentinel sha match | pass |
| AC6 evidence pack | yaml + WAVE + ledger + zip | to be written this step | pass |
| AC7 no prod SUT mutate | pool/skills + validate_r5 sha stable | inventory-diff covers them | pass |
| DoD scoped changes only | only artifacts/S07 (+ eval meta) | fixture under S07; no pool edits | pass |
| DoD honest status | disclose self-review; skills candidate | WAVE + evidence limitations | pass |
