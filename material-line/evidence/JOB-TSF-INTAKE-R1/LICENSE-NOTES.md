# LICENSE-NOTES — JOB-TSF-INTAKE-R1

| 字段 | 值 |
|---|---|
| checked_at | 2026-11-09 Asia/Shanghai |
| method | `gh api repos/<repo> --jq .license` + SKILL frontmatter 抽样 + LICENSE 文件头 |

## Repo-level SPDX（GitHub API）

| repo | license.spdx_id | used_as |
|---|---|---|
| moonlight-lupin/agent-skills | MIT | C01 primary ADAPT |
| jeffreytse/grimoire-core | MIT | C02 secondary cite |
| AtlasOmnia/donna-starter | MIT | C03 secondary cite |
| pjt222/agent-almanac | MIT | C04 secondary cite |
| clawic/skills | MIT | C06 primary ADAPT（landscape 可再分发主源） |
| makaronz/skilslsls | **NONE**（无仓级 SPDX） | C07 结构启发；**不**整文件复制进 pool |
| FerroxLabs/murage | **AGPL-3.0** | C08/C09 **HOLD** |
| hwspen7/PoreiaGo | MIT | C10 primary ADAPT |

## Critical: FerroxLabs/murage AGPL vs claimed Apache

| 证据 | 观察 |
|---|---|
| 仓 `license.spdx_id` | `AGPL-3.0` |
| `LICENSE` 文件头 | `GNU AFFERO GENERAL PUBLIC LICENSE Version 3` |
| C08 frontmatter | `license: Apache-2.0`（food-tourism-planner） |
| C09 frontmatter | `license: Apache-2.0`（international-cuisine-explorer） |

**处置：`hold_license`。** 主题极相关（尤其 C08），可留在 intake 分析 / VERDICT / MATRIX，**禁止**把 murage SKILL 正文 ADAPT 进 `pool/skills/`，直至许可冲突澄清。本轮 food Fermin 仅用 C10（MIT）。

## makaronz/skilslsls

- README 自称 Manus Skills 库；根目录未见 SPDX LICENSE 文件（API `license` = null）。
- `landscape-photography/SKILL.md` EXISTS，但缺少可再分发许可证明。
- Fermin `fermin-tsf-landscape-shoot`：以 clawic MIT 摄影工序为可再分发主 provenance；对 C07 仅保留格点/场景启发与路径 cite，不粘贴上游正文。

## pin freeze（2026-11-10）

Gate3 ACCEPT 同步冻 pin：`ref` 改为 default-branch tip 的不可变 commit SHA；移除 `pin_pending`。  
明细见同目录 `PIN-FREEZE.md`。makaronz 仅冻 SHA + cite，**不**宣称 SPDX 许可。

## Skill-level claims（抽样）

| id | skill frontmatter license | repo SPDX | action |
|---|---|---|---|
| C01 | MIT | MIT | OK |
| C03 | MIT | MIT | OK |
| C04 | MIT | MIT | OK |
| C08 | Apache-2.0 | AGPL-3.0 | **HOLD** |
| C09 | Apache-2.0 | AGPL-3.0 | **HOLD** |
| C07 | （无） | NONE | 不整文件复制 |
