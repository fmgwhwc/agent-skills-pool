# Decision / Spec: Next bounded improvement for agent-skills-pool
ID: r6-s02-improve-pool-default
Status: authorized-default

## Outcome and beneficiary

After this decision, Fermin has **one** named next improvement for the pool (not an open-ended polish program), with observable acceptance, for the pool owner (fermin gl) and DC Bot closed-loop builders.

## Inputs and observed current state

**Stated (requester / governing asks):**

- Continue building item-by-item (owner authorized an R6 plan and sequential construction).
- This executor run is W1.2 only; no GitHub writes.

**Observed (with references):**

- Eight ADAPT candidates exist under `r5-adapt-batch/pool/skills/` with matching `catalog-entries.yaml` ids; all `status: candidate`; `quality_gate.runtime_scenarios` and `release` remain `pending` (catalog-entries.yaml).
- Local `pool-skeleton/catalog.yaml` is still empty (`version: 0`, `entries: []`) — skeleton snapshot, not proof of empty GitHub main.
- R6 plan defines waves W0–W5; ledger shows W0 complete, S08 pass, S01 pass, S02 was not-run before this artifact.
- `fermin-using-skills` route table maps unclear goal/acceptance → `fermin-brainstorm-or-spec`.
- Local `fermin-using-skills` Step 4 text already includes the single-path typo exemption (sha256 `f22ce33c…`); S01 had recorded pre-patch hash `3b3140fd…` and left a diff under `patches/`.

**Proposed (Fermin default):**

- Treat “improve the pool” for this cycle as **deepening the current eight** via the R6 eval queue (evidence → eval_partial/eval_pass → owner release), **not** as an open call to ADAPT new upstream skills immediately.
- **Single next improvement:** finish W1 router/validator closure (this S02 evidence + then W1.4 catalog notes / Step 4 patch sync), then enter W2 (spec→plan→execute) per `R6-item-build-plan.md`.
- Keep all eight at `candidate` until scenario evidence exists; do not invent `release`.

**Unknown (material):**

- Whether the owner’s “improve” intent is **bounded to the current eight + R6**, or should **also ADAPT new skills** in this same cycle. That choice changes the asset set and acceptance.

## Scope

In:

- Decision record + S02 evidence under `r6-eval/`
- Default next-improvement pointer aligned with R6 W1→W2

Out / anti-goals:

- No new skill ADAPT in this W1.2 run
- No silent pool SKILL rewrite
- No GitHub push/PR from this executor
- No claiming remote `main` file contents without a fetch
- No marking `runtime_scenarios: pass` in meta from this harness alone

## Decisions and alternatives

| Decision | Choice | Rationale | Alternatives not taken |
|----------|--------|-----------|------------------------|
| Ceremony | Load using-skills → brainstorm-or-spec | Goal/acceptance unclear; not a single-path typo | Skip to writing-plans (premature); ad-hoc edits with no contract |
| Improvement focus | Default: deepen eight via R6 | Plan already authorized; catalog pending runtime | Immediately ADAPT more upstream skills; cosmetic README-only polish |
| Questioning | Default proposal selected; one fork question recorded | Brainstorm allows authorized default for reversible local work; fork remains explicit | Block all progress until owner answers; ask many low-impact process questions |

## Execution contract

Surfaces: dc-bot (this run); later waves may use cursor-cloud for repo writes under separate authority.

Allowed reads: local `/workspace/fermin-main-subject/**` listed in routing note.

Allowed changes: `r6-eval/**` artifacts/evidence/ledger/scenarios/WAVE reports + zip packaging only.

Dependencies: R6 plan; existing R5 candidates; prior S01/S08 evidence.

## Acceptance

- AC-1 Sources listed in `sources-checked.md` were read before any question → file exists with paths.
- AC-2 Decision distinguishes observed / proposed / unknown → sections above.
- AC-3 Exactly one default proposal named (“deepen eight via R6; next = finish W1 then W2”) **or** ≤1 high-impact question asked as the blocking gate → default selected; one fork question retained under open questions (non-blocking).
- AC-4 No pool skill file content mutated this run; no GitHub writes.

## Risks, assumptions, and open questions

| Item | Kind | Effect | Owner |
|------|------|--------|-------|
| Owner may want breadth (new ADAPts) not depth | Unknown / high-impact question | Would replace the default next improvement | Requester |
| Local skeleton catalog empty vs R5 overlay | Observed inconsistency across local trees | Must not invent which tree equals GitHub main | Executor (do not fabricate) |
| using-skills hash moved vs S01 | Observed | W1.4 should reconcile patch file vs applied local text | W1.4 |

### High-impact question (≤1; non-blocking under authorized-default)

**If this default is wrong:** Is “improve the pool” for this cycle **only** finishing R6 eval/release of the current eight candidates, **or** should we also ADAPT additional upstream skills before W2?

Consequence: the first answer keeps the asset set fixed and maximizes evidence quality; the second expands catalog scope and delays release of the eight.

## Next route

- Complete S02 evidence packaging (this wave item).
- Per plan queue: **W1.4** (patch/catalog notes) then **W2.1**.
- Load `fermin-writing-plans` only when a multi-step contract for W2 is opened—not for this decision alone.
