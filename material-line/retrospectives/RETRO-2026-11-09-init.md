# RETRO — Material Line init（2026-11-09）

| 字段 | 值 |
|---|---|
| 类型 | 立项复盘骨架 |
| 范围 | `material-line/` 增量脚手架 |
| 状态 | init 完成；样板 Job **未**执行闭环 |

## 背景

Skills pool 已有工程 init（8 released 过程技能 + raw + validate），但 Human 以 PY-RAW-040 为标尺判定：仍缺脱机 Job、主体/功能/主题/价值与物料级验证门。

## 本次做了什么

- 新建 `material-line/` 全树（schemas / subjects / themes / jobs / materials L0–L4 / gates / evidence / retrospectives / value-cards）
- 样板 Job `JOB-PY-RAW-040-E06-GATE2` 规格可开跑
- 样板物料诚实标 L2 + E06 硬伤；L3/L4 空位
- `gate1_check.py --self-test` 可跑；`gate2_exec_stub.py` 标明 stub
- 根 README 增补 demo+init 与目标态；**未删**既有资产

## 刻意没做

- 不批量贴百科全文
- 不 Phase2 扩源
- 不改 `validate_r5.py` 行为
- 不把 R6 过程技能改称物料

## 后续复盘点

1. E06 修复率与 Gate2 实跑证据
2. stub → 完整对比器的误报率
3. Human Gate3 结论
4. KPI：物料 Job 闭环数是否 > 0

过程时间线见 `PROCESS-LOG.md`；R6 细节仍查 `r6-eval/`。
