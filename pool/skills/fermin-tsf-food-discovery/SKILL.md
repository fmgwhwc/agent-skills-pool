---
name: fermin-tsf-food-discovery
description: Builds a TSF food shortlist with strict anti-fabrication rules — sourced or UNKNOWN facts, taste as opinion, coaxial with itinerary nodes. Use when ranking nearby meal candidates for a scenic day pack; do not use to invent restaurant names/menus or to copy AGPL food-tourism planner bodies.
---

# Fermin TSF Food Discovery

## Purpose

Produce a **bounded food shortlist** for TSF days: structured candidates, provenance, and taste-vs-fact split. ADAPT from MIT culinary-specialty-discovery discipline. FerroxLabs/murage food-tourism-planner (C08) is **HOLD** — analyze in VERDICT only; **do not** copy its body into this package.

## Provenance (ADAPT)

- Primary: `hwspen7/PoreiaGo` `plugins/skills/culinary-specialty-discovery/SKILL.md` (MIT) — no invented specialties; UNKNOWN over guesswork; advisory output.
- HOLD cite only (not adapted_from body): `FerroxLabs/murage` `skills-library/food-tourism-planner/SKILL.md` — theme fit high; repo AGPL-3.0 vs frontmatter Apache-2.0 → see LICENSE-NOTES.

## Load / do not load

Load when the itinerary needs nearby meal candidates with honest evidence limits.

Do not load to fabricate “must-eat” lists, write critic prose as fact, copy murage AGPL content, or run nutrition-lab analyzers as travel discovery.

## Fermin boundaries

- Never invent venue names, menus, prices, hours, or allergen guarantees.
- Facts require user/provider source or UNKNOWN.
- Taste, “worth it,” and vibe are opinion.
- Shortlist stays coaxial with shoot/transit nodes when a day plan exists.
- C08 may be mentioned as HOLD upstream in reports — not inlined here.

## Steps

### 1. Collect only allowed inputs

Accept: user-named places, provider JSON, prior itinerary food nodes, dietary constraints stated by the user. Reject the urge to “fill the city” from model memory.

If inputs are empty, return an empty shortlist plus questions — do not hallucinate a slate.

### 2. Normalize candidate rows

For each supplied candidate:

| field | rule |
|---|---|
| `id` | stable |
| `name` | only if provided by input/source |
| `node_link` | itinerary node id or UNKNOWN |
| `fact` | hours/address/cuisine label only with source |
| `opinion` | taste fit, spice, queue expectation |
| `allergen_hours` | UNKNOWN unless sourced |
| `limitations` | what was not verified |

Cap list length to keep context small (prefer ≤7 unless user asks otherwise).

### 3. Apply anti-fabrication protocol

Follow PoreiaGo-style reliability: do not invent attractions/menus/schedules; treat missing fields as unknown; keep output advisory; never commit itinerary mutations silently.

If a model completion suggests a new venue name not in inputs, drop it or mark `UNVERIFIED_SUGGESTION` only when the user explicitly allows brainstorming — still not a fact.

### 4. Align with TSF timeline

Map shortlist rows to meal windows beside shoot nodes. Flag transit conflicts. Hand structural gaps back to `fermin-tsf-itinerary-structure` rather than inventing filler stops.

### 5. Record HOLD and stop conditions

In the run note: state that C08 murage planner remains HOLD (AGPL conflict) and was not copied. Close when shortlist + limitations artifact is written and status remains candidate.

## 能证明 / 不能证明

**能证明**

- Shortlist rows trace to inputs or are explicitly empty.
- C10 path EXISTS under MIT repo license.
- C08 cited only as HOLD in material-line VERDICT/LICENSE-NOTES — body absent from this skill.

**不能证明**

- That any restaurant is open, good, or allergen-safe without sources.
- That murage Apache frontmatter overrides AGPL LICENSE (it does not for this pool).

## Done when

- Shortlist artifact exists with fact/opinion/UNKNOWN columns.
- Zero fabricated venue names presented as fact.
- No murage AGPL prose in `pool/skills/`.
- meta `status: candidate`; sources pinned to immutable SHAs (not released).
