# JOB-TSF-INTAKE-R1 — Brief

## 权限与目标

Human 已授权构建并验证。链路：有限主题 TSF → GitHub 收集 → material-line 分析物料 → Gate → Fermin 限定 Skills（`candidate`）。

## 硬约束

- 不删除既有 `pool/` / `raw/` / `r6-eval/` / material-line 内容；只增量。
- 不凭空写旅游攻略当终点；分析物料必须对回 GitHub 源。
- FerroxLabs/murage 仓 license = **AGPL-3.0**，SKILL frontmatter 自称 Apache-2.0 → **HOLD**（可进 intake 分析，禁止把正文 ADAPT 进 pool 直至许可澄清）。
- Fermin Skills 本轮 status=`candidate`（不做假 released）。
- pin：`ref: main` + `pin_pending: true`（未冻 commit SHA 可接受，但必须写 pin_pending）。

## 冻结查询（本轮用过，勿再扩）

1. `travel itinerary filename:SKILL.md`
2. `photography OR photo OR camera filename:SKILL.md`
3. `restaurant OR culinary OR food OR cuisine filename:SKILL.md`
4. `trip OR tour OR itinerary path:skills filename:SKILL.md`
5. `landscape OR scenic OR outdoor photography filename:SKILL.md`

## 本轮 Fermin ADAPT（3）

| id | 主源 | 辅 cite | 收窄 |
|---|---|---|---|
| fermin-tsf-itinerary-structure | C01 moonlight-lupin travel-itinerary (MIT) | C02/C03 | TSF 一日/半日；节点与拍摄/就餐同轴；禁未核验营业时间/路况 |
| fermin-tsf-landscape-shoot | C07+C06 | C04 | 风景外拍卡；与行程时间轴咬合；版权 UNKNOWN；非商品/人像主线 |
| fermin-tsf-food-discovery | C10 PoreiaGo culinary-specialty-discovery | C08 仅分析 | 短名单 + 禁编造店名；事实栏来源或 UNKNOWN |

## 验收

- PR 打开；无删除 `pool/raw/r6-eval`
- PATH-CHECK 覆盖 ADAPT/HOLD 条目
- 3 条 `fermin-tsf-*` candidate 在 `pool/skills` + catalog
- VERDICT.md 含评分与处置
