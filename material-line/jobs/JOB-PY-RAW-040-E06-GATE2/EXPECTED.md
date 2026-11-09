# EXPECTED — JOB-PY-RAW-040-E06-GATE2

## Gate 通过标准

| Gate | 期望 |
|---|---|
| Gate1 | Job 目录含 `job.yaml` + `BRIEF.md`；物料 INDEX 条目存在；关键 YAML 字段齐 |
| Gate2 | E06 代码在 Python **3.11.18** 执行；预测与实际一致；日志写入 Evidence |
| Gate3 | Human：接受 / 有条件接受 / 退回；通过后才可议 L3 |

## E06 正确预测（修复后）

常见运行、无额外隐藏强引用时：

| 步骤 | 预期 |
|---|---|
| `print(shallow[0] is box)` | `True` |
| `del container` 后 `print(ref() is shallow[0])` | `True` |
| `del shallow` 后 `print(ref() is None)` | **`False`**（原物料误写 True） |
| 追加 `del box` 后 `print(ref() is None)` | 常见运行中 `True` |

## 度量（本轮试验建议记录）

- E06 类逻辑错误检出率 / 修复率
- Gate2 误报率
- 代码块执行成功率
- Human 验收结果

## 完成定义（Job 闭环）

- [ ] 预测与推演已修
- [ ] Gate2 Evidence 齐（版本、输入哈希、stdout、verdict）
- [ ] DC Bot 差异报告已交
- [ ] Human Gate3 有结论
- [ ] 物料 level **仍诚实**（未过门禁不写 L3/L4）
