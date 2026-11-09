# Material Line — 进度看板

| 字段 | 值 |
|---|---|
| 更新 | 2026-11-09 Asia/Shanghai |
| 成熟度 | **demo + init** → 目标：**job**（样板闭环） |

---

## 总览

| 里程碑 | 状态 | 说明 |
|---|---|---|
| W6 Material Line init | **done** | 目录树、schemas、样板 Job 规格、Gate runners 最小可跑 |
| W6.1 TSF intake R1 | **in_progress（本 PR）** | 主题收集 → VERDICT/MATRIX → 3×`fermin-tsf-*` candidate；Gate2 path/license 已核；Gate3 human pending |
| W6.1 样板 Job 执行（PY-RAW） | pending | 修复 E06 → Gate2 实跑 → Evidence |
| W6.2 Gate2 对比器 | pending | stub → 隔离执行 + 预测对比 |
| W6.3 Human Gate3 | pending | 接受 / 有条件接受 / 退回 |
| W6.x Phase2 扩源 | blocked | 等样板 Job 证明「能产出并验证物料」 |

---

## 资产清单

| 资产 | 路径 | 水位 |
|---|---|---|
| Subject (PY) | `subjects/SUBJ-python-textbook.yaml` | scaffold |
| Theme (PY) | `themes/THEME-py-object-model.yaml` | scaffold |
| Value card (PY) | `value-cards/VC-python-textbook-weakref.yaml` | scaffold |
| Subject (TSF) | `subjects/SUBJ-trip-decision-maker.yaml` | active |
| Theme (TSF) | `themes/THEME-trip-scenic-food.yaml` | active |
| Value card (TSF) | `value-cards/VC-tsf-less-waste.yaml` | active |
| Job 队列 | `jobs/QUEUE.yaml` | PY queued + TSF in_progress |
| 样板 Job (PY) | `jobs/JOB-PY-RAW-040-E06-GATE2/` | spec ready / not executed |
| Intake Job (TSF) | `jobs/JOB-TSF-INTAKE-R1/` | Gate2 verified; Gate3 pending |
| 物料 (PY) | `materials/L2-canonical-candidate/PYTEXT-PY-RAW-040/` | **L2 Candidate**；E06 硬伤未修 |
| 物料 (TSF) | `materials/L2-canonical-candidate/TSF-INTAKE-R1/` | VERDICT+MATRIX；对应 3 candidate skills |
| L3 / L4 | `materials/L3-validated/` · `L4-production/` | 空位（禁止假完成） |
| Gate1 runner | `gates/runners/gate1_check.py` | `--self-test` 可跑 |
| Gate2 runner | `gates/runners/gate2_exec_stub.py` | stub + `--dry-run` |
| Evidence (PY) | `evidence/JOB-PY-RAW-040-E06-GATE2/RUN-NOTE.md` | 占位 |
| Evidence (TSF) | `evidence/JOB-TSF-INTAKE-R1/` | PATH-CHECK + LICENSE-NOTES + RUN-NOTE |
| 复盘 | `retrospectives/` | init 骨架 + PROCESS-LOG |

---

## TSF intake 焦点（W6.1）

| 字段 | 值 |
|---|---|
| active_theme | THEME-trip-scenic-food |
| active_job | JOB-TSF-INTAKE-R1 |
| fermin_candidates | `fermin-tsf-itinerary-structure`, `fermin-tsf-landscape-shoot`, `fermin-tsf-food-discovery` |
| released_this_round | **none** |
| hold_license | C08/C09 FerroxLabs/murage AGPL-3.0 vs Apache claim |

Next（TSF）：Gate3 human 审 VERDICT + 三条 candidate；可选冻 SHA；murage 许可澄清前禁止正文 ADAPT。

---

## KPI（改口后）

成功看 **物料 Job 闭环数**，不看 Skills 条目数或流程文厚度。

当前闭环数：**0**（PY 规格已立未跑；TSF Gate2 证据已立，Gate3 未收）。

Skills catalog（`catalog.yaml`）与物料 INDEX（`materials/INDEX.yaml` + `INDEX.md`）分开维护。
