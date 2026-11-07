# WAVE W4.2 report — S09 Authoring baseline variant

| Field | Value |
|-------|-------|
| When | 2026-11-07 08:42:43 CST (Asia/Shanghai) |
| Surface | dc-bot executor (local /workspace only; **no GitHub writes**) |
| Tree | /workspace/fermin-main-subject/r6-eval/ |
| Skills | fermin-skill-anatomy → fermin-tdd (eval honesty only) |

## Result

| Item | Scenario | Result | Evidence |
|------|----------|--------|----------|
| W4.2 Authoring baseline | S09 | **pass** | evidence/S09-authoring-baseline.yaml |

## What happened

1. **Task**: toy 1-page skill `fermin-catalog-lint-note` (catalog lint note on static failures); matched prompts in `briefs/PROMPTS.md`.
2. **Rubric**: explicit `rubric/S09-rubric.yaml` (C1–C6, max 20); `statistical_claim_allowed: false`.
3. **Variant A `with-form/`**: authored under anatomy Steps 1–9 + meta-contract; SKILL.md + meta.yaml (candidate, runtime pending); discriminating fixture idea; **no stats claim**. Score **20/20**.
4. **Variant B `without-form/`**: bare prompt only; no frontmatter/meta/field contract; vague steps + soft marketing/optional external side effects. Score **3/20**.
5. **Scoring**: same rubric; qualitative notes; delta=17 labeled **observational / sample-setup n=1 only**.
6. Skill pins unchanged (`PINNED_MATCH=yes`); empty references/ removed from with-form package.

## Artifacts

- `artifacts/S09/briefs/{TASK-catalog-lint-note,PROMPTS}.md`
- `artifacts/S09/rubric/S09-rubric.yaml`
- `artifacts/S09/with-form/fermin-catalog-lint-note/{SKILL.md,meta.yaml}`
- `artifacts/S09/without-form/fermin-catalog-lint-note/SKILL.md`
- `artifacts/S09/with-form|without-form/sample-lint-note/toy-entry.md`
- `artifacts/S09/scores/{SCORES.yaml,QUALITATIVE-NOTES.md}`
- `artifacts/S09/scheduler/{ADJUDICATION.md,skill-revisions*.sha256}`
- `evidence/S09-authoring-baseline.yaml`

## Patch note

**No patches.** `fermin-skill-anatomy` §8 already forbids claiming statistically supported improvement from a single sample and requires disclosing sample count/setup. Skills did not force a false statistical claim in this run. W4.3 remains available if owner later wants stronger wording elsewhere.

## Limitations

Same-author self-review (disclosed); n=1 sample/setup only — do not generalize; toy not in pool; no GitHub; skills remain candidate.

## Recommended next

**W4.3** patches only if owner wants extra copy; else **W5.1 / S11 Loader portability**.
