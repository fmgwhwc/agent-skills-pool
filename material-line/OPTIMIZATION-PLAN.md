# agent-skills-pool 优化方案：物料产出生产线（增量，不删现有）

| 字段 | 值 |
|---|---|
| 文档 ID | FMS-SKILLS-POOL-MATERIAL-LINE-OPT-2026-11-09 |
| 仓 | https://github.com/fmgwhwc/agent-skills-pool |
| 基线 | main `7cb3098`（R6 released + raw；demo+init） |
| 约束 | **禁止删除**现有 `pool/`、`raw/`、`r6-eval/`、`rejected/`、`research/`、校验脚本与目录；只增量 |
| 标尺 | PY-RAW-040 物料级（结构+证据+边界+复核）；非格式克隆 |
| 日期 | 2026-11-09 Asia/Shanghai |

---

## 0. 目标陈述（写入项目 README）

当前定位诚实表述：

> **demo + init**：Skills 半成品货架与过程技能已立；**尚未**达到可脱机 Job、可持续产出有主体/功能/主题/价值的物料级规模。

目标态：

> 在保留现有 Skills 池与 R6 过程资产的前提下，增量建设 **物料产出生产线（Material Line）**：  
> 脱机 Job → 主题物料 → Gate1/2/3 → Canonical 候选 → Human 接受；  
> KPI = **物料 Job 闭环数**，不是条目堆叠或流程文厚度。

分流：

| 层 | 目录（既有或新增） | 角色 |
|---|---|---|
| Skills 半成品 | `pool/`、`raw/`、`catalog.yaml` | 装载面 / 工序技能 / 上游对回 |
| 过程验证（保留） | `r6-eval/` | R6 证据与复盘；不迁移、不删除 |
| **物料生产线（新增）** | `material-line/` | 主体·主题·Job·物料·门禁·复盘 |

---

## 1. 新目录树（完整实现于仓内）

在仓库根新建（**仅新增**）：

```text
material-line/
├── README.md                      # 生产线章程 + 与 pool 的边界
├── OPTIMIZATION-PLAN.md           # 本方案落仓副本（便于复盘）
├── STATUS.md                      # demo+init → job 进度看板
├── schemas/
│   ├── subject.schema.yaml
│   ├── theme.schema.yaml
│   ├── job.schema.yaml
│   ├── material.schema.yaml
│   └── gate-result.schema.yaml
├── subjects/
│   └── SUBJ-python-textbook.yaml  # 样板主体
├── themes/
│   └── THEME-py-object-model.yaml
├── jobs/
│   ├── QUEUE.yaml                 # 脱机队列
│   ├── templates/
│   │   └── JOB-TEMPLATE.yaml
│   └── JOB-PY-RAW-040-E06-GATE2/
│       ├── job.yaml
│       ├── BRIEF.md
│       └── EXPECTED.md
├── materials/
│   ├── INDEX.yaml                 # 物料索引（与 catalog.yaml 分离）
│   ├── L0-raw/
│   ├── L1-parsed/
│   ├── L2-canonical-candidate/
│   │   └── PYTEXT-PY-RAW-040/
│   │       ├── README.md          # 指针+水位说明（不要求贴全文）
│   │       ├── LEVEL.yaml
│   │       └── NOTES.md           # E06 硬伤与处置
│   ├── L3-validated/              # .gitkeep + README
│   └── L4-production/             # .gitkeep + README
├── gates/
│   ├── README.md
│   ├── gate1-structure.md
│   ├── gate2-facts.md
│   ├── gate3-accept.md
│   └── runners/
│       ├── README.md
│       ├── gate1_check.py         # 可跑的结构检查（最小）
│       └── gate2_exec_stub.py     # 提取/执行/对比骨架（标明 stub→实装路径）
├── evidence/
│   ├── README.md
│   └── JOB-PY-RAW-040-E06-GATE2/
│       └── RUN-NOTE.md            # 占位：待 Validator 写入实跑日志
├── retrospectives/
│   ├── README.md
│   ├── RETRO-2026-11-09-init.md   # 本次立项复盘骨架
│   └── PROCESS-LOG.md             # 过程时间线（持续追加）
└── value-cards/
    └── VC-python-textbook-weakref.yaml
```

原则：

- 不改动、不移动、不删除 `pool/skills/*`、`raw/**`、`r6-eval/**`。
- `materials/INDEX.yaml` **独立于** `catalog.yaml`（Skills ≠ 物料）。
- 过程保留：`retrospectives/` + `OPTIMIZATION-PLAN.md` + 既有 `r6-eval/` 并行。

---

## 2. README.md 增补（主仓，增量段落）

在现有 README **末尾追加**（保留全部旧文）：

1. **Current maturity**：明确 `demo + init`。
2. **Target: Material production line**：主体/功能/主题/价值/脱机 Job/Gate/L0–L4。
3. **Layout** 图增加 `material-line/`。
4. **Roadmap** 新行：W6 Material Line init（本 PR）；后续 W6.x 样板 Job 闭环。
5. 链到 `material-line/README.md`。

可选：若存在 `research/` 内索引 MD，追加一条指针；没有则不造。

---

## 3. 样板闭环（实现为「可开跑」规格，不假装已 Validated）

**Job ID：** `JOB-PY-RAW-040-E06-GATE2`

- 输入：PY-RAW-040 L2 Candidate；已知 E06 预测错误（第三行应为 False；需 `del box`）。
- 工序：Cursor 修实验 → Ubuntu/本地指定 Python 跑 Gate2 → Evidence → DC Bot 汇总 → Human Gate3。
- `materials/.../NOTES.md` 记录硬伤；**不要**把未修复全文标成 L3。
- `evidence/.../RUN-NOTE.md` 写清：独立核验曾在 CPython 3.13.5 复现逻辑错误；主线仍锁定 3.11.18 门禁。

---

## 4. Gate runners 实现深度

**本 PR 必须可运行：**

- `gate1_check.py`：校验 `material-line` 下关键 YAML 字段、目录存在、JOB 有 BRIEF；exit 非 0 即失败；`--self-test`。
- `gate2_exec_stub.py`：能从给定 `.md` 抽出 fenced `python` 块并打印清单；执行模式可 `--dry-run`；文档写明完整对比器后续迭代，不假装已通。

**本 PR 不做：** 改 `validate_r5.py` 行为；删 raw；合进 Production 假数据。

---

## 5. 验收标准（Done）

1. 新目录 `material-line/` 按树完整落地，含 schemas、样板 subject/theme/job/value、L 级材料位、gates、evidence、retrospectives。
2. 根 `README.md` 增补物料生产线目标与 demo+init 诚实定位；旧章节仍在。
3. `git` diff **无**对 `pool/skills`、`raw`、`r6-eval` 的删除。
4. `python material-line/gates/runners/gate1_check.py --self-test` 通过。
5. 开 PR；说明写清「增量生产线，保留全部既有构建以便复盘」。

---

## 6. 非目标

- 不批量再生百科正文。
- 不在本 PR 合并 Phase2 扩源（Scrapling 等）。
- 不替换 R6 过程技能为「物料」。
- 不要求格式必须等于 encyclopedia-v2；契约可并存。

END_OF_PLAN
