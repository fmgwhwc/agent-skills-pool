# PIN-FREEZE — JOB-TSF-INTAKE-R1

| 字段 | 值 |
|---|---|
| checked_at | 2026-11-10T02:35:39Z (UTC) / 2026-11-10 Asia/Shanghai |
| method | GitHub REST API：`GET /repos/{owner}/{repo}` → default_branch tip；`GET .../contents/{path}?ref={tip_sha}` 确认路径 EXISTS；blob URL 改写为 tip SHA |
| scope | 三条 `fermin-tsf-*` 的 `source` / `adapted_from` / `license_evidence`（原 `ref: main` + `pin_pending: true`） |
| outcome | 全部改为不可变 commit SHA；移除 `pin_pending`；**不**升 `status=released` |

## Frozen tip SHAs（default branch tip that contains the path）

| repo | default_branch | frozen tip SHA | tip committer date (UTC) | notes |
|---|---|---|---|---|
| moonlight-lupin/agent-skills | main | `ceacc13d2bbc98d9dea5cbabcb4f44e4c7fd14a9` | 2026-11-07T10:49:52Z | C01 primary + LICENSE |
| jeffreytse/grimoire-core | main | `7ff5861b00836cb0d675c00a09a26d143722579e` | 2026-10-16T14:03:17Z | C02 secondary cite |
| AtlasOmnia/donna-starter | main | `b6eaf1bab0527daab22ad02043fcd7c9869d0323` | 2026-10-26T23:33:53Z | C03 secondary cite |
| clawic/skills | main | `f825206afbf1c697202533a9187be68c7b697e0e` | 2026-07-27T08:18:49Z | C06 primary + LICENSE |
| makaronz/skilslsls | main | `f2d8e7b86fb4b5b2bebd32e8a657285fa62977d3` | 2026-09-17T04:29:49Z | C07 structure cite only |
| pjt222/agent-almanac | main | `ce87dce34c9e6ff9621cb597af3ea3be10d49f3c` | 2026-11-06T16:40:50Z | C04 secondary cite |
| hwspen7/PoreiaGo | main | `76d5e2171b302594ad0ae83d9b36d513c4b7ac44` | 2026-11-03T02:06:15Z | C10 primary + LICENSE |

与 `PATH-CHECK.md`（2026-11-09）记录的 main HEAD 一致；本轮 API 复检 tip 未漂移。

## Path EXISTS at frozen tip（blob sha）

| repo | path | EXISTS | blob sha |
|---|---|---|---|
| moonlight-lupin/agent-skills | productivity/travel-itinerary/SKILL.md | YES | `51a73421672ccf61aae032e1503ea8fabc686258` |
| moonlight-lupin/agent-skills | LICENSE | YES | `f1b98146720211aef66d294624b28798c827f37d` |
| jeffreytse/grimoire-core | skills/travel/planning/skills/design-trip-itinerary/SKILL.md | YES | `41d9e46d57ed5cb34621fae6e93eeb3d79039ac4` |
| AtlasOmnia/donna-starter | skills/productivity/destination-trip-planning/SKILL.md | YES | `3813bd1e58c92e2b1b402f6e95be3ca03f999ec1` |
| clawic/skills | skills/photography/SKILL.md | YES | `c096c61e01665c8895a70503345ec4821a7c4402` |
| clawic/skills | LICENSE | YES | `066f752f69339bfb5957da09258424da5bf6f98b` |
| makaronz/skilslsls | landscape-photography/SKILL.md | YES | `749bf95d2d3cb5b3c8a517f125f6e9760f52ab2d` |
| pjt222/agent-almanac | skills/plan-hiking-tour/SKILL.md | YES | `4292c121ad8e491d4e61ff1d387fbed8b721a73a` |
| hwspen7/PoreiaGo | plugins/skills/culinary-specialty-discovery/SKILL.md | YES | `5822268b42743c7fda2fd84970c013c2d2cf1a98` |
| hwspen7/PoreiaGo | LICENSE | YES | `df996f52ee381ee501b9f3e3d046b0d8aae1b3a4` |

## makaronz/skilslsls（无仓级 SPDX）

- SHA **已冻结**（cite 路径 EXISTS）。
- **不**复制正文进 `pool/`；**不**宣称可再分发许可（`license: unknown` 保持）。
- 可再分发主 provenance 仍为 clawic/skills（MIT）。

## FerroxLabs/murage

- **仍 HOLD**（AGPL-3.0 vs Apache frontmatter）。本轮不对 murage 做 pin 写入 `adapted_from` / pool 正文。
- 见 `LICENSE-NOTES.md`；禁止正文 ADAPT。

## Catalog / meta

已更新：`pool/skills/fermin-tsf-*/meta.yaml`、`catalog.yaml`、`catalog-entries.yaml`。  
`status` 仍为 `candidate`；`quality_gate.runtime_scenarios` / `release` 仍为 `pending`。
