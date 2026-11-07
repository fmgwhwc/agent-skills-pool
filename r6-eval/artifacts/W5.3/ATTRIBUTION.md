# Attribution — agent-skills-pool (R5 ADAPT → R6 released)

This is new Fermin packaging/procedural adaptation, **not a fork or mirror**. Substantial method and checklists were selected, reorganized, rewritten, and translated to Fermin execution surfaces from two MIT repositories. Eight process skills were promoted to `status: released` after R6 scenario evidence (W1–W5.2).

## Upstream pins (frozen)

| Upstream | Copyright | Exact pinned source (full SHA) | Retained notice |
|---|---|---|---|
| `addyosmani/agent-skills` | Addy Osmani (2025) | `301b02b12bff98e4688e6984af6556802322bbde` | [ADDYOSMANI-MIT.txt](ADDYOSMANI-MIT.txt) |
| `obra/superpowers` | Jesse Vincent (2025) | `22f0b463e7a5e579904dd6211a520321035526f7` | [OBRA-MIT.txt](OBRA-MIT.txt) |

## Released skills (R6) — source.repo@ref + license

| Skill id | status | Primary `source.repo@ref` / path | `license_spdx` | Also adapted_from |
|---|---|---|---|---|
| `fermin-using-skills` | released | `addyosmani/agent-skills@301b02b12bff98e4688e6984af6556802322bbde` / `skills/using-agent-skills/SKILL.md` | MIT | (primary only) |
| `fermin-brainstorm-or-spec` | released | `addyosmani/agent-skills@301b02b12bff98e4688e6984af6556802322bbde` / `skills/spec-driven-development/SKILL.md` | MIT AND MIT | + `obra/superpowers@…/skills/brainstorming/SKILL.md` |
| `fermin-writing-plans` | released | `obra/superpowers@22f0b463e7a5e579904dd6211a520321035526f7` / `skills/writing-plans/SKILL.md` | MIT | (primary only) |
| `fermin-executing-plans` | released | `obra/superpowers@22f0b463e7a5e579904dd6211a520321035526f7` / `skills/executing-plans/SKILL.md` | MIT | (primary only) |
| `fermin-subagent-driven-dev` | released | `obra/superpowers@22f0b463e7a5e579904dd6211a520321035526f7` / `skills/subagent-driven-development/SKILL.md` | MIT | + Obra implementer brief (see meta) |
| `fermin-tdd` | released | `obra/superpowers@22f0b463e7a5e579904dd6211a520321035526f7` / `skills/test-driven-development/SKILL.md` | MIT AND MIT | + Addy TDD skill (see meta) |
| `fermin-verification-dod` | released | `addyosmani/agent-skills@301b02b12bff98e4688e6984af6556802322bbde` / `references/definition-of-done.md` | MIT AND MIT | + Addy using-agent-skills + Obra verification-before-completion |
| `fermin-skill-anatomy` | released | `addyosmani/agent-skills@301b02b12bff98e4688e6984af6556802322bbde` / `docs/skill-anatomy.md` | MIT AND MIT | + selective Obra `writing-skills` |

Exact contributing paths, adaptation notes, and per-entry reasoning remain in each `pool/skills/*/meta.yaml`. R6 runtime/release evidence lives under `r6-eval/evidence/` and promotion records under `r6-eval/artifacts/S12/` (see `r6-eval/artifacts/S12/PROMOTION.md` and `r6-eval/ledger.md`).

`license_spdx: MIT AND MIT` on multi-source entries means attributions to both MIT sources are retained; it is **not** a claim that the root Fermin repository's packaging license has changed. Root `LICENSE` keeps its own original-packaging notice; this attribution directory must ship when adapted skill content is copied or distributed as a pool.

## Rejected / not promoted (separate)

Scoped rejects and path corrections are **not** attributions for released skills. See `rejected/README.md` and `rejected/2026-11-07-r5-path-corrections.md`. No Anthropic documentation skill was adapted or copied.

License texts at the pins above were read on 2026-11-07. No legal conclusion is drawn about the upstream repositories beyond inspecting their root MIT texts at the listed revisions.

Updated: 2026-11-07 08:49:24 CST (Asia/Shanghai) — R6 W5.3 pool docs sync.
