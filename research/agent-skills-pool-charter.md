# Agent Skills Pool — 架构组约束落地章程

| 项 | 内容 |
|----|------|
| 文档 | FMS-RES-GH-POOL-001 |
| 日期 | 2026-11-06（Asia/Shanghai） |
| 上位方案 | `github-oss-matrix-research-scheme.md` |
| 状态 | 架构组已支持分析框架；本文件落实**两条限定** |

---

## 1. 架构组硬约束（必须遵守）

### 约束 A — Bot 闭环

**所有分析过程，以及 GitHub 开源 Agent Skills / Prompts 的采集、筛选、规整，在 DC Bot 上闭环完成。**

含义：

| 做 | 不做 |
|----|------|
| 在本对话 / DC Bot 工具链内完成：选题、取源、研判、矩阵增量、扫盲卡、筛选记录 | 把「半成品分析」甩到无关第三方聊天里断档 |
| 过程产物（雷达、短名单、仓卡片、否决清单）留在 Bot 工作区，并可按轮次写入 Pool 仓的 `research/` | 要求架构组人工在浏览器里重复同一套分析 |
| 重 clone / 重跑例可派 Ubuntu，但**研判结论与入库决定回到 Bot 收口** | 在 Ubuntu 上另起一套无证据的「平行池」 |

> 「闭环」= 分析与决策链路以 DC Bot 为班长收口；不是「所有算力必须在 15GiB box 上跑」。

### 约束 B — 自建 `agent-skills-pool`，禁止直接 fork

在关联 GitHub 账号下**新建**仓库（建议名：`agent-skills-pool`），用于存放**经 Bot 分析、筛选、规整后的 Skills / Prompts 池**。

| 允许 | 禁止 |
|------|------|
| 新建空仓后，由 Bot 写入规整后的 Skill 包 | `fork` 上游仓当作我们的 Pool |
| 保留上游溯源：`source.repo` / `source.ref` / `source.path` / `license` | 无出处复制、删许可、伪装原创 |
| 改写、切割、合并、重命名以适配 Fermin 契约 | 整仓 mirror / 未筛选批量搬迁 |
| 明确 `REJECTED` 清单（看过但不收录） | 用星数代替筛选理由 |

---

## 2. 闭环流水线（与多轮矩阵方案对齐）

```text
R0 定镜（名单+主题）          ┐
R1 公司雷达                   │
R2 仓短名单冻结               ├─ 全过程在 DC Bot 闭环
R3 仓/Skill 深读卡片          │
R4 横切（Skills/Prompts 形态）│
R5 筛选决定：ACCEPT / ADAPT / REJECT
                              ┘
        │ ACCEPT/ADAPT 才规整入库
        ▼
 GitHub: owner/agent-skills-pool
        ├── research/     # 过程矩阵与报告（可选同步）
        ├── pool/         # 规整后的 skills / prompts
        ├── catalog.yaml  # 索引
        └── ATTRIBUTION.md
```

**入库门禁（ACCEPT/ADAPT 必过）：**

1. 有 pinned 上游 `owner/repo@ref` + 路径  
2. License 允许我们这种再分发/衍生（不知则标 `license_unknown`，不得进 `pool/released`）  
3. 有一句话「为何收」与适用执行面  
4. 有最小验收（能说明怎样算这个 Skill 可用）  
5. 与已有 pool 条目不重复，或显式声明取代关系  

---

## 3. Pool 仓建议结构（规整后，非 fork 布局）

```text
agent-skills-pool/
├── README.md                 # 池的目的、非 fork 声明、如何贡献（仅经 Bot 闭环）
├── LICENSE                   # 仓级许可（与条目级 SPDX 分开说明）
├── ATTRIBUTION.md            # 上游致谢与许可证汇总
├── catalog.yaml              # 机读索引（id, path, source, status, tags）
├── schema/
│   └── skill-entry.schema.json   # 条目元数据约定
├── research/                 # Bot 闭环过程产物（矩阵切片、报告版本）
│   ├── matrix/
│   ├── cards/
│   └── reports/
├── pool/
│   ├── skills/               # 规整后的 SKILL 包（一目录一条）
│   │   └── <skill-id>/
│   │       ├── SKILL.md
│   │       ├── meta.yaml     # source/license/status/fermin_tags
│   │       └── ...
│   ├── prompts/              # 规整后的 prompts（同样 meta）
│   └── _inbox/               # 仅 Bot 工作区同步用的暂存（未过门禁）
└── rejected/                 # 否决记录（理由 + 上游指针），禁止当可用 Skill
    └── YYYY-MM-DD-<slug>.md
```

**单条 `meta.yaml` 最小字段：**

```yaml
id: example-skill-id
status: draft | candidate | released | deprecated
source:
  repo: owner/name
  ref: "<tag-or-commit>"
  path: "path/in/upstream"
  url: "https://github.com/owner/name/tree/<ref>/path"
license_spdx: MIT   # or unknown
decision: adapt     # accept | adapt | reject
rationale: "一句话为何进池"
fermin_tags: [agent-skills, literacy, ...]
epistemic: verified | evidenced | provisional | unknown
```

---

## 4. 建仓与写入方式（工具现实）

| 步骤 | 谁做 | 说明 |
|------|------|------|
| 1. 在 GitHub **新建空仓** `agent-skills-pool` | **人**（或架构组指定账号 `fmgwhwc` / 组织） | Cursor/DC Bot **不能直接创建 GitHub 空仓**；需你在 GitHub 网页创建后把 URL 发我 |
| 2. 授予 Cursor GitHub App 可见该仓 | 人 | 以便 Cloud Agent 推送 |
| 3. 分析与筛选 | **DC Bot 闭环** | 按 R0–R5 |
| 4. 首次写入目录骨架 + README/章程 | Cloud Agent 推到该空仓 | 仍由 Bot 发起与验收 |
| 5. 后续条目增量 | Bot 研判 → Cloud Agent PR/提交 → 人合并（建议） | 生产门禁可保留人合并 |

备选：若希望草稿仓先在 Cursor Origin，再镜像到 GitHub——须架构组另批；**默认按你们要求走 GitHub 关联仓。**

---

## 5. 与「不建第二套 GitHub」的关系

- Pool 仓是 **Fermin 的 Skills/Prompts 准生产池**，条目级指向上游，不是 GitHub 全站镜像。  
- `research/` 存的是我们的分析过程，方便闭环可回查，不是上游内容的第二副本库。  
- 上游更新：开「修订轮」比较 `ref`，再决定是否 ADAPT 新版本——不自动跟踪 fork sync。

---

## 6. 请架构组 / 你确认的落地项（确认后 Bot 即按此执行）

1. 仓名是否确定为 `agent-skills-pool`？owner 用 `fmgwhwc` 还是组织？public / private？  
2. 空仓创建并回复 URL 后，是否授权我发起「骨架 + 本章程」首次提交？  
3. 合并策略：Bot 直推 `main`，还是一律 PR 由人合并？  
4. 第一枪横切是否仍为 **Agent Skills / Prompts 形态**（沿用矩阵方案启动切片）？

---

## 7. 纪要可贴

> 分析框架获支持。限定：（1）开源 Agent Skills/Prompts 的分析筛选规整在 DC Bot 闭环；（2）GitHub 新建 `agent-skills-pool` 存放规整后的池，禁止 fork 上游充数；条目保留溯源与许可；过程矩阵可置于仓内 `research/`。建仓由人完成空库，Bot 负责闭环分析与经 Cloud Agent 写入。

