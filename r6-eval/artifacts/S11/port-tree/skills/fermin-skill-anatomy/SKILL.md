---
name: fermin-skill-anatomy
description: Authors, adapts, revises, and audits Fermin pool skills with portable contracts, complete provenance, and evidence-based quality gates. Use when turning selected upstream material into a Fermin skill, fixing skill discovery or execution, or preparing a candidate for DC Bot, Cursor Cloud, and Ubuntu.
---

# Fermin Skill Anatomy and Authoring

## Purpose

Turn useful process knowledge into a small, testable Fermin execution contract—not a promotional article, session story, runtime installer, or upstream mirror. A good skill helps an agent decide when to load it, what to do, and what evidence closes it.

This skill governs pool-side authoring and candidate quality. It does not install a skill into a runtime or mark it released.

## Load / do not load

Load to create, adapt, revise, audit, or add a skill reference package or catalog entry.

Do not use it for one-off project conventions better kept in project instructions, or for constraints cheaply enforced entirely by code. Do not copy an upstream skill merely because it is popular.

## Skill contract

A skill directory is self-contained:

```text
pool/skills/<skill-id>/
├── SKILL.md          # required, procedural entry point
├── meta.yaml         # required, Fermin provenance and gate results
└── references/       # optional, only for material checks/templates
    └── <kebab-id>.md
```

`SKILL.md` has YAML frontmatter delimited by `---` with at least:

```yaml
---
name: <same-as-directory>
description: <what it does followed by concrete Use-when triggers/exclusions>
---
```

Use model-neutral procedures. Runtime controls belong in a platform adapter or sanctioned metadata extension, not in invented top-level Agent Skills fields. Fermin's richer provenance lives in `meta.yaml`.

## Steps

### 1. Prove need and select one capability

State:

- recurrent task/failure the skill addresses;
- who uses it, on which surface;
- what distinct capability it owns;
- expected reusable artifact and acceptance evidence;
- why existing pool entries cannot cover it.

Search existing catalog IDs and descriptions. Merge or supersede deliberately, recording the decision. One capability gets one canonical Fermin entry; do not create “Obra TDD” and “Addy TDD” side by side.

Avoid creating skills for one-off sessions, facts already clear in the request, generic motivational advice, or purely mechanical checks that should simply be a validator.

### 2. Read selective authoritative material at a fixed revision

Inspect only the relevant upstream skill, its required supporting references, and license. Do not mirror an entire repository to author one skill.

Record every contributing source:

```yaml
source:
  repo: owner/repo
  ref: <full immutable commit SHA>
  path: <exact file/directory used>
  url: <URL containing the same full SHA/path>
license_spdx: MIT  # or confirmed permissive SPDX
```

If multiple paths contribute, use `adapted_from` as a list of the same full source objects; let `source` identify the primary source. Do not cite an unread or nonexistent file. `license_unknown` cannot be released or used to clear acceptance.

Preserve upstream copyright/license notices required for substantial adaptations. For a substantial two-MIT-source merge, use `license_spdx: MIT AND MIT` and retain both upstream notices in a packaged notice file or the pool attribution directory, according to the established pool convention.

### 3. Separate reusable method from upstream residue

Keep useful workflow, failure detection, acceptance contracts, and succinct reasoning. Rewrite for Fermin's actual surfaces:

- materials → indexed assets;
- DC Bot decision and ledger ownership;
- bounded task packs and artifact-linked reports;
- Cursor Cloud and Ubuntu as authorized workers, not unbounded owners;
- evidence-gated candidate/release progression.

Cut or replace:

- marketplace and multiple-runtime install scripts;
- telemetry/configuration for upstream companion tooling;
- branding, stars, superiority claims, or unverified productivity claims;
- code-only branch/commit/PR ceremony when the requested scope is content;
- large do-everything lifecycle lists and duplicate workflows;
- hardcoded machine/user/context details and nonportable paths;
- unrelated defensive-security content unless separately accepted.

Do not turn “upstream says production-grade” into a Fermin performance promise. Attribute uncertain claims and prefer observable local evidence.

### 4. Design for discovery before writing detail

Write `name` and `description` last-iterated but early-tested.

- `name`: lowercase kebab-case, stable and equal to the directory.
- `description`: third-person capability plus concrete triggers. Include relevant symptoms/artifacts (“resume a plan”, “author a skill”), not a compressed recipe.
- Identify body triggers and explicit non-triggers so a task can skip the skill cheaply.
- Ensure the description does not instruct the reader to skip reading the full skill.

Load the skill yourself before following a description: the summary is an index, not the workflow.

### 5. Write the minimum executable body

Prefer this shape, renaming headings when clearer:

1. **Purpose:** output and benefit.
2. **Load / do not load:** observable conditions.
3. **Steps:** ordered decisions, concrete paths/contracts where applicable.
4. **Exceptions/evidence:** how to handle wrong input, red checks, missing tools, and permission boundaries.
5. **Done when:** observable checklist for this procedure.

For each step ask whether an executor knows what artifact to produce and how to judge it. Replace “ensure quality” with a criterion and actual check.

Choose guidance based on the failure:

| Observed failure | Effective contract |
|---|---|
| Wrong/unclear output shape | Positive template and required fields. |
| Missing condition handling | Branch keyed to an observable predicate. |
| Known verification skipped | Required evidence and rebuttal of the specific rationalization. |
| Simple reference lookup | Lean reference and retrieval/application check. |

Use only short rationalization tables for observed or credible recurring failure modes; do not fill every paragraph with absolutes. One precise example beats multiple shallow languages/framework examples.

### 6. Apply progressive disclosure and portability

Target roughly 200–400 lines for `SKILL.md` in this pool; keep shorter when sufficient and never pad to the target. Move large checklists/templates to a directly linked `references/<name>.md`, one hop from the skill.

Omit unused `scripts/` folders. Use a script only when repeatable executable behavior earns it, and test that script on its intended environment.

Package every needed reference inside the skill. Do not inherit Addy's repo-root sibling links that disappear on single-skill install. Check every local link using the shipped directory—not only a repo browser.

### 7. Complete provenance and quality metadata

Use the local `meta.yaml` contract in [references/meta-contract.md](references/meta-contract.md). Include:

- schema-compatible ID/status/source/license/adapt/rationale/tags/epistemic;
- all contributing source pins;
- Fermin tag and supported surfaces;
- adaptation changes and dedup choice;
- gate outcomes with real check names/results and explicit pending runtime scenarios;
- unresolved risks and known validation limitations.

Metadata cannot rescue missing body content, and green static checks cannot prove runtime effectiveness.

### 8. Build a discriminating evaluation

Before writing or changing procedure substantially, define at least one plausible scenario that distinguishes the desired behavior from an inadequate baseline.

For each candidate:

1. **Baseline:** previous skill/minimal-instruction behavior, or an intentionally broken input where a fresh agent run is unavailable; label weaker substitutes.
2. **Scenario:** realistic task including relevant ambiguity or pressure, required output, and acceptance rubric.
3. **With-skill run:** check that the executor loads, applies, and closes with the expected evidence.
4. **Adverse case:** irrelevant/malformed/conflicting input or inappropriate trigger; ensure it handles or rejects correctly.
5. **Regression:** repeat static/integration checks and inspect for new contradictions.

If behavioral wording is disputed, compare variants under the same realistic prompt and rubric, including no-guidance control. Do not claim a statistically supported improvement from a single sample; disclose sample count/setup. Do not invent cross-model transfer claims from upstream research without independently reading and validating them.

### 9. Gate candidate status, not imagined release

Run static and content checks locally, inspect catalog merge, and run available scenarios. A candidate with good structure but no runtime scenario must state `runtime: pending` and remain `status: candidate`.

Release requires the specified scenario(s) on an intended Fermin execution surface, owner acceptance, and remaining approval/licensing gates. No batch efficiency argument replaces per-skill evaluation.

## Content review lens

- **Decision relevance:** does it change Fermin behavior or just restate good intentions?
- **Atomicity:** can it be used without hunting upstream?
- **Nonduplication:** does it own one capability or overlap another entry?
- **Epistemic honesty:** are source claims, actual checks, and pending evidence distinct?
- **Authority hygiene:** does it avoid granting itself repository/external permissions?
- **Maintainability:** are exact sources, version pins, and next revision triggers retained?
- **Token discipline:** is the main body shorter than its reference dump and free of repetition?

## Done when

- [ ] A reusable Fermin capability, owner surfaces, artifact, and acceptance rationale are explicit.
- [ ] Only selective source paths at full SHAs were used; every source/license attribution is correct.
- [ ] `name` matches the path and `description` exposes concrete load/non-load semantics without summarizing the workflow.
- [ ] Steps are model-neutral, concrete, scoped, and include exceptions and observable done-when checks.
- [ ] Upstream installers, telemetry, marketing, rigid runtime assumptions, and duplicate lifecycle paths were removed.
- [ ] Supporting references are necessary, portable, one-hop, and present in the skill package.
- [ ] `meta.yaml` passes the pool schema plus Fermin extension checks and states real gate results.
- [ ] Static/catalog/link checks and available scenario evaluations have evidence; unrun gates remain pending.
- [ ] Entry is `candidate`, not released, until intended-surface runtime review and owner acceptance pass.
