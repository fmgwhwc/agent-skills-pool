# Material Line（物料产出生产线）

| 字段 | 值 |
|---|---|
| 文档 | FMS-SKILLS-POOL-MATERIAL-LINE-CHARTER |
| 仓 | `agent-skills-pool` |
| 状态 | **init**（脚手架已立；样板 Job 待闭环） |
| 日期 | 2026-11-09 Asia/Shanghai |

---

## 1. 边界（Skills ≠ 物料）

| 层 | 目录 | 角色 |
|---|---|---|
| Skills 半成品 | `pool/`、`raw/`、根 `catalog.yaml` | 装载面 / 工序技能 / 上游对回 |
| 过程验证（保留） | `r6-eval/` | R6 证据与复盘；**不迁移、不删除** |
| **物料生产线（本目录）** | `material-line/` | 主体·主题·Job·物料·门禁·复盘 |

**禁止混称：** `catalog.yaml` 索引 Skills；`materials/INDEX.yaml` 索引物料。二者独立。

本目录是**增量**建设：不删除、不搬迁既有 `pool/`、`raw/`、`r6-eval/`、`rejected/`、`research/`、`schema/`、`validate_r5.py`。

---

## 2. 目标态

脱机 Job → 主题物料 → Gate1/2/3 → Canonical 候选 → Human 接受。

KPI = **物料 Job 闭环数**，不是条目堆叠或流程文厚度。

当前仓成熟度仍为 **demo + init**（见根 `README.md`）。本线把「可脱机跑 Job、可持续产出有主体/功能/主题/价值的物料」立为下一目标。

标尺：PY-RAW-040 物料级（结构 + 证据 + 边界 + 复核）；非格式克隆。

---

## 3. 目录一览

```text
material-line/
├── schemas/           # subject / theme / job / material / gate-result
├── subjects/          # 主体定义
├── themes/            # 主题包
├── jobs/              # 脱机队列 + Job 规格
├── materials/         # L0–L4 + INDEX（≠ catalog.yaml）
├── gates/             # Gate1/2/3 文档 + runners
├── evidence/          # Job 实跑证据占位
├── retrospectives/    # 过程复盘 + PROCESS-LOG
└── value-cards/       # 价值陈述卡
```

过程资产：本目录 `retrospectives/` + `OPTIMIZATION-PLAN.md` 与既有 `r6-eval/` **并行保留**，供后续复盘。

---

## 4. 样板 Job

**`JOB-PY-RAW-040-E06-GATE2`**

- 输入：`PYTEXT-PY-RAW-040`（L2 Canonical Candidate；已知 E06 硬伤）
- 工序：修实验 → 指定 Python 跑 Gate2 → Evidence → DC Bot 汇总 → Human Gate3
- 诚实水位：材料**不得**伪标 L3/L4；E06 未修前 Gate2 视为失败样例

详见 `jobs/JOB-PY-RAW-040-E06-GATE2/` 与 `materials/L2-canonical-candidate/PYTEXT-PY-RAW-040/`。

---

## 5. 快速检查

```bash
# Gate1 结构自检（本 PR 必须绿）
python material-line/gates/runners/gate1_check.py --self-test

# Gate2 stub：列出 markdown 中的 python fence（完整对比器后续迭代）
python material-line/gates/runners/gate2_exec_stub.py --dry-run path/to/notes.md
```

Skills 池校验仍用根目录 `validate_r5.py`（行为不变）。

---

## 6. 非目标（本 init）

- 不批量再生百科正文
- 不合并 Phase2 扩源（Scrapling 等）
- 不把 R6 过程技能改称为「物料」
- 不要求格式必须等于 encyclopedia-v2

更多：`OPTIMIZATION-PLAN.md` · `STATUS.md`
