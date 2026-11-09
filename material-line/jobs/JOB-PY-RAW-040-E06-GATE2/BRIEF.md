# BRIEF — JOB-PY-RAW-040-E06-GATE2

| 字段 | 值 |
|---|---|
| Job | `JOB-PY-RAW-040-E06-GATE2` |
| 输入物料 | `PYTEXT-PY-RAW-040`（《弱引用》，L2 Canonical Candidate） |
| 主线 Python | **3.11.18**（门禁） |
| 已知硬伤 | E06「浅复制与弱引用的对照」第三行预测错误 |

## 目标

最小闭环试验（不批量再生）：

1. Cursor：修 E06 预测与推演；补 `del box` 完整对照。
2. Ubuntu / 本地：在 **3.11.18** 跑 Gate2（提取代码块 → 执行 → 对比预测）。
3. 写入 `evidence/JOB-PY-RAW-040-E06-GATE2/`。
4. DC Bot 汇总差异报告 → Human Gate3。

## 输入指针

- 物料水位说明：`materials/L2-canonical-candidate/PYTEXT-PY-RAW-040/`
- 复核意见（外部）：`PY-RAW-040-EVAL-REVIEW-2026-11-09`（E06 证据）
- 正文全文：**不在本仓粘贴**；以指针 + NOTES 记录硬伤即可

## 不做

- 不伪标 L3 Validated / L4 Production
- 不扩写百科正文充数
- 不改 `validate_r5.py` / 不删 `pool/`·`raw/`·`r6-eval/`
