# Material Line — 进度看板

| 字段 | 值 |
|---|---|
| 更新 | 2026-11-09 Asia/Shanghai |
| 成熟度 | **demo + init** → 目标：**job**（样板闭环） |

---

## 总览

| 里程碑 | 状态 | 说明 |
|---|---|---|
| W6 Material Line init | **done（本 PR）** | 目录树、schemas、样板 Job 规格、Gate runners 最小可跑 |
| W6.1 样板 Job 执行 | pending | 修复 E06 → Gate2 实跑 → Evidence |
| W6.2 Gate2 对比器 | pending | stub → 隔离执行 + 预测对比 |
| W6.3 Human Gate3 | pending | 接受 / 有条件接受 / 退回 |
| W6.x Phase2 扩源 | blocked | 等样板 Job 证明「能产出并验证物料」 |

---

## 资产清单（init）

| 资产 | 路径 | 水位 |
|---|---|---|
| Subject | `subjects/SUBJ-python-textbook.yaml` | scaffold |
| Theme | `themes/THEME-py-object-model.yaml` | scaffold |
| Value card | `value-cards/VC-python-textbook-weakref.yaml` | scaffold |
| Job 队列 | `jobs/QUEUE.yaml` | 1 queued |
| 样板 Job | `jobs/JOB-PY-RAW-040-E06-GATE2/` | spec ready / not executed |
| 物料 | `materials/L2-canonical-candidate/PYTEXT-PY-RAW-040/` | **L2 Candidate**；E06 硬伤未修 |
| L3 / L4 | `materials/L3-validated/` · `L4-production/` | 空位（禁止假完成） |
| Gate1 runner | `gates/runners/gate1_check.py` | `--self-test` 可跑 |
| Gate2 runner | `gates/runners/gate2_exec_stub.py` | stub + `--dry-run` |
| Evidence | `evidence/JOB-PY-RAW-040-E06-GATE2/RUN-NOTE.md` | 占位 |
| 复盘 | `retrospectives/` | init 骨架 + PROCESS-LOG |

---

## KPI（改口后）

成功看 **物料 Job 闭环数**，不看 Skills 条目数或流程文厚度。

当前闭环数：**0**（规格已立，执行未跑）。

Skills catalog（`catalog.yaml`）与物料 INDEX（`materials/INDEX.yaml`）分开维护。
