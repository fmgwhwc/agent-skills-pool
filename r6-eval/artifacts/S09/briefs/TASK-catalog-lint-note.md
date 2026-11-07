# S09 authoring task — toy skill “catalog lint note”

**Setup label:** sample/setup only (n=1 matched pair). Do **not** infer statistical improvement.

## Stimulus (identical for both variants)

Draft a **1-page** toy Fermin skill package that helps an agent produce a short **catalog lint note** when a pool catalog entry fails a static check (e.g. missing `id`, bad `status`, or name≠directory).

Required deliverable shape (minimum):

- Skill id directory: `fermin-catalog-lint-note/`
- At least a procedural entry document an agent could follow
- Scope: content-only; no installers, no send/publish, no GitHub write

Acceptance for this toy (not production pool entry):

1. Agent knows **when to load** vs skip.
2. Output of a run is a **lint note** with fixed fields (entry id, check name, observed vs expected, severity, next action).
3. Procedure stays model-neutral and local to `/workspace` or a named catalog path.
4. Status of the skill itself remains **candidate** if metadata is present.

## Matched prompt setups

| Variant | Label | Guidance given to author |
|---------|-------|--------------------------|
| A | `with-form/` | Full `fermin-skill-anatomy` Steps 1–9 + `references/meta-contract.md`; also apply `fermin-tdd` discriminating-evaluation / evidence-loop guidance for skill fixtures (no false statistical claim). |
| B | `without-form/` | Bare prompt only: “Write a skill that helps write catalog lint notes.” No anatomy form, no meta contract, no TDD evidence-loop text. |

Same author scores both under one rubric. Independence: **same-author-self-review** (disclosed).
