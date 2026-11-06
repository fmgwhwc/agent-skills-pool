# R3 Deep-Read Index — Agent Skills shortlist (five)

**Round:** R3 (frozen shortlist)  
**Closed-loop:** DC Bot research executor  
**Snapshot time:** 2026-11-06 ~16:23–16:30 Asia/Shanghai  
**Constraint:** No forks; no GitHub repo/PR creation; no attack-skill install  

| # | Card | Repo | Stars* | License (API) | fermin_tag | One-line verdict |
|---|------|------|--------|---------------|------------|------------------|
| 1 | [R3-1-anthropics-skills.md](./R3-1-anthropics-skills.md) | anthropics/skills | 187894 | null (mixed per README) | **depend_candidate** / selective borrow | De facto Agent Skills origin + template/spec pointer; pool by skill after license screen. |
| 2 | [R3-2-google-skills.md](./R3-2-google-skills.md) | google/skills | 22544 | Apache-2.0 | **depend_candidate** / borrow patterns | Large GCP/product skill catalog + `npx skills`; index/depend, don’t mirror. |
| 3 | [R3-3-microsoft-skills.md](./R3-3-microsoft-skills.md) | microsoft/skills | 3177 | MIT | **watch** / selective borrow | Azure/Foundry context pack + explorer; WIP; watch unless Azure face is active. |
| 4 | [R3-4-obra-superpowers.md](./R3-4-obra-superpowers.md) | obra/superpowers | 313210 | MIT | **borrow** / watch as full dep | Methodology OS for agents; borrow process skills, don’t swallow whole harness. |
| 5 | [R3-5-addyosmani-agent-skills.md](./R3-5-addyosmani-agent-skills.md) | addyosmani/agent-skills | 113589 | MIT | **borrow** / depend_candidate | Lifecycle + verification anatomy; best complementary engineering pack to Superpowers. |

\*Stars/forks are API snapshots at card time — not quality scores.

## Cross-cut notes for architecture

1. **Standard surface:** Anthropic template + agentskills.io; Google/Microsoft/Addy/Obra all speak `SKILL.md`.  
2. **Pool rule reinforced:** ACCEPT/ADAPT with provenance — never fork these five into `agent-skills-pool`.  
3. **Dedup next (R4):** Superpowers ↔ Addyosmani process overlap; vendor catalogs (Google/MS) stay depend indexes.  
4. **License traps:** Anthropic document skills source-available; Anthropic repo SPDX null — per-skill screen mandatory.  
5. **API notes:** `search_code` for `repo:microsoft/skills filename:SKILL.md` returned 0 (likely indexing lag); contents API used instead. obra `list_commits` returned oversized payload — SHA extracted successfully.

## Pinned SHAs (quick)

| Repo | SHA |
|------|-----|
| anthropics/skills | `ca45fc496a3436251f191354091d557da31c15b5` |
| google/skills | `c2cf4ba74c0e47f0e7a81d29e053e740998a0ae2` |
| microsoft/skills | `4f831bbbf54e004507758d8ef2ab420c77bb81b6` |
| obra/superpowers | `22f0b463e7a5e579904dd6211a520321035526f7` |
| addyosmani/agent-skills | `301b02b12bff98e4688e6984af6556802322bbde` |

## Suggested architecture next step

Freeze R3 tags → pick **≤8** skill candidates for ADAPT into `agent-skills-pool` (once empty repo URL exists) → capability-layer matrix (R4).

## Bot follow-through (2026-11-06 17:58 Asia/Shanghai)

- Wrote `research/matrix/R4-skills-prompts-form-crosscut.md` (form cross-cut + provisional ≤8 ADAPT list).
- Prepared local `pool-skeleton/` for first Cloud Agent push once empty repo URL exists.
- Live check: `fmgwhwc/agent-skills-pool` still absent on GitHub.
