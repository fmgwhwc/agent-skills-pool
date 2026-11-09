# RUN-NOTE — JOB-PY-RAW-040-E06-GATE2

| 字段 | 值 |
|---|---|
| 状态 | **placeholder** — 待 Validator 写入实跑日志 |
| Job | `JOB-PY-RAW-040-E06-GATE2` |
| 主线门禁 | Python **3.11.18** |
| 预检环境（仅复现逻辑） | CPython 3.13.5（2026-11-09）；不替代 3.11 门禁 |

## 已知预检（非本仓 Gate2 正式跑）

独立核验曾复现 E06：第三次 `ref() is None` 实测为 `False`（物料误预测 `True`）；`box` 仍持有强引用。详见物料 `NOTES.md`。

## 待写入（Gate2 正式跑后）

- [ ] 解释器版本字符串
- [ ] 输入文件哈希
- [ ] 提取的代码块清单
- [ ] stdout / stderr
- [ ] 预测 vs 实际
- [ ] verdict（pass/fail）+ `gate-result` sidecar
