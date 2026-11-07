---
name: fermin-catalog-lint-note
description: Drafts a structured catalog lint note when a Fermin pool catalog entry fails a static check. Use when validate/catalog review reports missing id, bad status, name≠directory, or similar field defects; do not use for rewriting skill bodies, releasing candidates, or sending external messages.
---

# Fermin Catalog Lint Note

## Purpose

Produce one short, reviewable **catalog lint note** that records what failed, where, and the smallest next local action. The note is an artifact for humans/schedulers—not an auto-fix and not a release decision.

## Load / do not load

Load when a static catalog or meta check already failed (or a fixture is prepared to fail) and the operator needs a consistent note shape.

Do not load to invent failures, to mutate `pool/skills` without a task grant, to mark `release`, or to send/publish/install anything.

## Lint-note contract

Write exactly one Markdown file per failure batch item:

```text
artifacts/<run>/lint-notes/<entry-id>.md
```

Required fields (use these headings):

| Field | Content |
|-------|---------|
| entry_id | Catalog / skill id under review |
| check_name | Named static check (e.g. `name_matches_dir`) |
| observed | What the checker saw |
| expected | Contract expectation |
| severity | `error` \| `warn` |
| next_action | One local, reversible step (edit path + field) |
| skill_status_reminder | Always `candidate` unless owner evidence says otherwise |

## Steps

### 1. Bound the input

Record the catalog path or fixture path actually read. If none is supplied, stop and ask for one path—do not scan the whole machine.

### 2. Identify one failing check

Pick the first failing check with a clear pin reason. Do not bundle unrelated failures into one vague paragraph.

### 3. Fill the lint-note template

Create the note file with all required fields. Quote observed values; do not paraphrase away the mismatch.

### 4. Keep authority local

Propose edits only under the granted tree. HOLD any send/publish/install/delete outside the task pack.

### 5. Close with evidence pointers

Link the note to the checker command/exit (or fixture path). Leave skill `status` as candidate; do not claim runtime pass from a static lint note.

## Exceptions / evidence

| Condition | Action |
|-----------|--------|
| Check actually passed | Do not invent a lint note; record `no-op` with command output. |
| Path missing / unreadable | Note `blocked` + missing path; do not guess contents. |
| Multiple failures | One note per entry-id (or clearly listed sections); no silent drop. |
| Pressure to “just release” | Refuse; lint note ≠ release gate. |

**Discriminating sample (setup only, n=1):** broken fixture with `name: Foo_Bar` vs directory `foo-bar` should yield severity=error and next_action pointing at frontmatter `name`. A bare “write nicer docs” baseline that omits `check_name`/`observed` fails this rubric item. **No statistical improvement claimed from one sample.**

## Done when

- [ ] Lint note path exists with all required fields filled from real observation.
- [ ] check_name and observed/expected are specific, not motivational.
- [ ] next_action is local and reversible; no external side effect claimed.
- [ ] Candidate/release boundary respected; sample/setup labeled if used for eval.
