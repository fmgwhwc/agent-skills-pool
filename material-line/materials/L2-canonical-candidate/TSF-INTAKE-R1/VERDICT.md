# TSF-INTAKE-R1 VERDICT

| 字段 | 值 |
|---|---|
| job | JOB-TSF-INTAKE-R1 |
| theme | THEME-trip-scenic-food |
| collected_at | 2026-11-09T16:10:00+08:00 |
| verified_at | 2026-11-09 Asia/Shanghai（live GitHub API） |
| query_freeze | 5 |
| candidates | 25（≤30） |

## 收集规模

- code search 命中量级（仅取 top 页）：travel~3360 / photo~5232 / food~118 / trip-path~181
- 去重后关键词保留 ~55；纳入本轮队列 **25** 条

## 处置摘要

| 处置 | 数量 | IDs |
|---|---|---|
| adapt（进 Fermin 主源） | 4 | C01, C06, C07, C10 |
| adapt_secondary | 3 | C02, C03, C04 |
| hold_license | 2 | C08, C09 |
| hold_queue | 6 | C05, C13, C14, C15, C19, C25 |
| duplicate_like | 4 | C12, C16, C17, C18 |
| weak_fit | 2 | C11, C24 |
| reject / reject_narrow | 4 | C20, C21, C22, C23 |

## 评分与处置全表

| id | repo | path | score | disposition | license notes |
|---|---|---|---:|---|---|
| C01 | moonlight-lupin/agent-skills | productivity/travel-itinerary/SKILL.md | 3 | **adapt** | repo MIT；skill MIT |
| C02 | jeffreytse/grimoire-core | skills/travel/planning/skills/design-trip-itinerary/SKILL.md | 3 | adapt_secondary | repo MIT |
| C03 | AtlasOmnia/donna-starter | skills/productivity/destination-trip-planning/SKILL.md | 3 | adapt_secondary | repo MIT；skill MIT |
| C04 | pjt222/agent-almanac | skills/plan-hiking-tour/SKILL.md | 3 | adapt_secondary | repo MIT；skill MIT |
| C05 | pjt222/agent-almanac | skills/plan-tour-route/SKILL.md | 2 | hold_queue | — |
| C06 | clawic/skills | skills/photography/SKILL.md | 3 | **adapt** | repo MIT |
| C07 | makaronz/skilslsls | landscape-photography/SKILL.md | 3 | **adapt** | **repo SPDX 缺失** → 正文引用谨慎；结构启发 + clawic MIT 主可再分发 |
| C08 | FerroxLabs/murage | skills-library/food-tourism-planner/SKILL.md | 3 | **hold_license** | repo **AGPL-3.0**；frontmatter 自称 Apache-2.0 → **冲突 HOLD**；仅分析引用，**禁止** pool 正文 ADAPT |
| C09 | FerroxLabs/murage | skills-library/international-cuisine-explorer/SKILL.md | 2 | **hold_license** | 同仓 AGPL-3.0；frontmatter 自称 Apache-2.0 |
| C10 | hwspen7/PoreiaGo | plugins/skills/culinary-specialty-discovery/SKILL.md | 3 | **adapt** | repo MIT；反编造纪律强 |
| C11 | mickpletcher/AI-Skills | claude/skills/food-analyzer/SKILL.md | 2 | weak_fit | 营养分析非旅游美食发现 |
| C12 | mickpletcher/AI-Skills | claude/skills/travel-itinerary/SKILL.md | 2 | duplicate_like | — |
| C13 | injurka/trip-scheduler | .agents/skills/travel-itinerary-enricher/SKILL.md | 2 | hold_queue | — |
| C14 | majiayu000/spellbook | skills/trip-planner/SKILL.md | 2 | hold_queue | — |
| C15 | torlyai/Schengen-master | skills/plan-trip/SKILL.md | 2 | hold_queue | — |
| C16 | hummbl-io/agent-skills | skills/travel-itinerary/SKILL.md | 2 | duplicate_like | — |
| C17 | skills-on-ai/skills-on-ai | skills/travel-itinerary/SKILL.md | 2 | duplicate_like | — |
| C18 | skills-on-ai/skills-on-ai | skills/photography/SKILL.md | 2 | duplicate_like | — |
| C19 | modbender/skill-library-mcp | data/photography/SKILL.md | 2 | hold_queue | — |
| C20 | DedInc/chef-agentic-skills | skills/chef-cuisine-french/SKILL.md | 1 | reject_narrow | 单一菜系过窄 |
| C21 | nexscope-ai/Amazon-Skills | amazon-product-photography/SKILL.md | 0 | reject | 电商产品摄影 |
| C22 | tourmind-com/Tourmind-Booking-Skills | skills/tourmind-booking/SKILL.md | 1 | reject | 平台绑定预订 |
| C23 | lightspeedwp/.github | skills/tour-operator-gravity-forms-configuration/SKILL.md | 0 | reject | WP 表单配置 |
| C24 | princemanjee/EngineeredPromptLibrary | plugins/pl-critique-review/skills/food-critic/SKILL.md | 1 | weak_fit | — |
| C25 | fewling/travel-plans | .claude/skills/travel-itinerary/SKILL.md | 2 | hold_queue | — |

## 建议本轮 Fermin 限定 Skills（3）

1. **fermin-tsf-itinerary-structure** ← C01（+C02/C03 cite）
2. **fermin-tsf-landscape-shoot** ← C06 主可再分发 + C07 结构启发（+C04 cite）；C07 仓无 SPDX 不整文件复制
3. **fermin-tsf-food-discovery** ← C10；**C08 仅 VERDICT/MATRIX 分析引用，不复制正文**

## Gate2 焦点结果

| 检查 | 结果 |
|---|---|
| PATH EXISTS（C01,C02,C03,C04,C06,C07,C08,C09,C10） | **PASS** — 见 `evidence/JOB-TSF-INTAKE-R1/PATH-CHECK.md` |
| LICENSE murage | **HOLD** — AGPL-3.0 仓 vs Apache-2.0 frontmatter |
| LICENSE makaronz/skilslsls | **SPDX 缺失** — SHA 已冻；正文未复制；见 LICENSE-NOTES / PIN-FREEZE |
| pin | **已冻 tip SHA**（2026-11-10）；`pin_pending` 已移除 — 见 `evidence/.../PIN-FREEZE.md` |
| Gate3 | **接受（ACCEPT）** — 2026-11-10 Asia/Shanghai；decider=user fermin gl via DC Bot；**≠ release** |

## 能证明 / 不能证明

**能证明**

- 所列 adapt/hold 路径在 GitHub default-branch tip 上 EXISTS（API `contents` 200）；tip SHA 已写入 meta/catalog
- murage 仓级 license SPDX = AGPL-3.0；C08/C09 frontmatter `license: Apache-2.0`
- C01/C02/C03/C04/C06/C10 仓级 MIT（API）
- Human Gate3 ACCEPT（见 `GATE3.md`）

**不能证明**

- runtime scenario pack（故 `quality_gate.runtime_scenarios` / `release` 仍 pending；status 仍 candidate）
- makaronz 仓可再分发许可条款（无 SPDX；仅 cite）
- murage 作者是否意图 Apache（与仓 LICENSE 冲突未澄清）
- 任何真实目的地营业时间、路况、店名真实性（本 Job 不产出攻略事实库）

## 指标

| 指标 | 值 |
|---|---|
| candidates | 25 |
| score ≥ 2 | 21 / 25 = 84% |
| adapt + adapt_secondary | 7 |
| hold_license | 2 |
| reject* | 4 |
| Fermin candidates written | 3 |
