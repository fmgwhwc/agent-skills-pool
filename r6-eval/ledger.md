# R6 ledger — agent-skills-pool process skills

Timezone: Asia/Shanghai. Update after every item. Do not invent pass without artifacts.

| Wave | Item | Scenario | Status | Evidence | Notes | Updated |
|------|------|----------|--------|----------|-------|---------|
| W0 | Scaffolding | — | complete | r6-eval/ | README, scenarios S01–S12, template, ledger, plan copy | 2026-11-07 08:22 CST |
| W1.3 | Validator discrimination | S08 | pass | evidence/S08-validator-discrimination.yaml | self-test EXIT 0; TEMP broken SHA EXIT 1 with wrong R3 pin; original meta SHA unchanged | 2026-11-07 08:22:57 CST |
| W1.1 | Router / low ceremony | S01 | pass | evidence/S01-router-low-ceremony.yaml | Bounded typo fix; only using-skills; patch proposed for Step 4 | 2026-11-07 08:23:11 CST |
| W1.2 | Router / consequential unknown | S02 | pass | evidence/S02-router-consequential-unknown.yaml | Read-before-ask; default=deepen eight via R6; ≤1 fork Q non-blocking | 2026-11-07 08:25:21 CST |
| W1.4 | Router / validator patches | S01/S08 | applied | patches/fermin-using-skills.SKILL.md.diff | Step4 typo-path patch merged via PR#4 | 2026-11-07 |
| W2.1 | Requirements splitting | S03 | pass | evidence/S03-requirements-splitting.yaml | IDs cap-catalog-lint + cap-evidence-ledger; T03 sole catalog owner; 1 plan; no patches | 2026-11-07 08:27 CST |
| W2.2 | Resume behavior | S04 | pass | evidence/S04-resume-behavior.yaml | T01 done→interrupt→cold resume at T02; T01 sha unchanged; no patches | 2026-11-07 08:29 CST |
| W2.3 | Plan skill copy edits | S03/S04 | skipped | — | S03/S04 needed no skill-body patches; Step1 resume wording already correct | 2026-11-07 08:30 CST |
| W3.1 | Dispatch isolation | S05 | pass | evidence/S05-dispatch-isolation.yaml | 2 packs; A ACCEPTED w/ artifact; B REJECTED/NEEDS_EVIDENCE; no chat dump; no patches | 2026-11-07 08:31 CST |
| W3.2 | Shared-write collision | S06 | pass | evidence/S06-shared-write-collision.yaml | collision+T-INT sequential; ID dedup; no silent overwrite; no patches | 2026-11-07 08:34 CST |
| W3.3 | Permission negative | S10 | not-run | — | — | — |
| W3.4 | DoD matrix patch | S05/S10 | not-run | — | — | — |
| W4.1 | Code RED/GREEN | S07 | not-run | — | — | — |
| W4.2 | Authoring baseline | S09 | not-run | — | — | — |
| W4.3 | tdd/anatomy patches | S07/S09 | not-run | — | — | — |
| W5.1 | Loader portability | S11 | not-run | — | — | — |
| W5.2 | Candidate→release | S12 | not-run | — | Owner/promotion | — |
| W5.3 | Pool docs sync | — | not-run | — | README/ATTRIBUTION | — |
