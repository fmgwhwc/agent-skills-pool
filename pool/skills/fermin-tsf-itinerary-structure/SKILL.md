---
name: fermin-tsf-itinerary-structure
description: Builds a TSF-narrowed half-day or one-day itinerary where travel nodes stay coaxial with shoot windows and food stops, with explicit fact-vs-opinion columns. Use when structuring a leisure day pack for trip × scenic photo × nearby food; do not use for business-trip exports, platform booking, or unverified city encyclopedias.
---

# Fermin TSF Itinerary Structure

## Purpose

Turn an accepted TSF day intent into a **small, coaxial node plan**: movement, shoot windows, and nearby food stops share one timeline. This is an ADAPT of upstream itinerary-structure skills, narrowed to THEME-trip-scenic-food — not a destination guidebook.

## Provenance (ADAPT)

- Primary: `moonlight-lupin/agent-skills` `productivity/travel-itinerary/SKILL.md` (MIT) — trip/day/node mental model; export/business machinery cut.
- Secondary cite only: `jeffreytse/grimoire-core` design-trip-itinerary; `AtlasOmnia/donna-starter` destination-trip-planning (MIT) — clustering / theme lock ideas; no wholesale copy.

Full pins and `pin_pending` live in `meta.yaml`.

## Load / do not load

Load when the user needs a **half-day or one-day** TSF pack with ordered nodes and buffers, and will accept UNKNOWN for unverified facts.

Do not load for multi-week generic city tours, business-trip PDF/ICS export stacks, platform-bound booking skills, or when the ask is only food critique or only portrait/product photography.

## Fermin boundaries

- Nodes must declare role: `transit | shoot | food | buffer | admin`.
- Facts vs opinions in separate columns; never promote opinion to fact.
- Forbidden as facts: unverified hours, live road conditions, prices, ticket stock, invented venues.
- Stay inside TSF intersection; reject pure hotel-hopping or pure restaurant crawls without shoot/transit coaxiality.

## Steps

### 1. Lock the TSF day contract

Capture: date window, start/end points, mobility constraints, must-keep shoot or food intents, and hard exclusions. If destination theme is unset, stop and clarify — do not fill a generic city template.

Record the contract path or inline block the executor will update.

### 2. Place immovable anchors then cluster

Lock fixed anchors (arrival, reserved experience if **user-supplied**, sunset window if timed). Cluster remaining candidate nodes by geography so transit does not thrash between shoot and food.

Prefer one primary cluster per half-day. Cite secondary upstream practice (cluster-by-geography) without importing unverified attraction lists.

### 3. Build coaxial day nodes

Emit a day skeleton:

```text
Day
├── Anchor / start
├── Node (role + window)
├── Link / transit assumption (labeled opinion or UNKNOWN if unmeasured)
├── Node …
└── Buffer
```

Each node fields (minimum):

| field | rule |
|---|---|
| `id` | stable within the day |
| `role` | transit / shoot / food / buffer / admin |
| `window` | local time range or UNKNOWN |
| `place_ref` | user-supplied or sourced id — never invent a venue name |
| `fact` | only sourced or UNKNOWN |
| `opinion` | sequencing taste, vibe, “worth trying if …” |
| `tsf_link` | which shoot or food node this supports |

### 4. Enforce evidence columns and cut waste

For every factual claim (hours, distance, access), require a source URL/path **or** write `UNKNOWN`. Mark travel-time guesses as opinion. Drop nodes that cannot coaxialize with at least one shoot or food intent unless the user explicitly wants a pure transit admin node.

Self-review: no fabricated venues; no AGPL murage body; business-export steps absent.

### 5. Hand off to sibling TSF skills

- Shoot windows → `fermin-tsf-landscape-shoot`
- Food shortlist structure → `fermin-tsf-food-discovery`

Return the day artifact path plus open UNKNOWNs. Do not mark catalog `released`.

## 能证明 / 不能证明

**能证明**

- Day artifact has coaxial roles and fact/opinion split.
- Every fact cell is sourced or UNKNOWN.
- Provenance points at MIT primary path in meta.

**不能证明**

- Real-world hours, traffic, or that a named place exists unless the user or a verified source provided it.
- That secondary cites were executed end-to-end in this session.

## Done when

- One half-day or one-day node plan exists with roles and TSF links.
- Fact/opinion/UNKNOWN discipline holds; no invented venues.
- Handoff notes name shoot and food sibling skills when relevant.
- meta remains `status: candidate` with `pin_pending: true` on sources.
