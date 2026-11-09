# NOTES — PYTEXT-PY-RAW-040 硬伤与处置

## E06 硬伤（Gate2 失败样例）

**位置：** 案例推演 · E06「浅复制与弱引用的对照」  
**严重度：** 技术准确性硬伤

原实验在 `del container` / `del shallow` 后预测 `ref() is None` 为 `True`。  
**错误原因：** 名字 `box` 仍持有强引用，故第三次输出应为 **`False`**。

若要观察弱引用失效，还需：

```python
del box
print(ref() is None)  # 常见运行中 True
```

### 独立核验摘要（2026-11-09）

- 环境：CPython **3.13.5**（仅复现引用逻辑；**不替代**主线 3.11.18 门禁）
- 实测：`line3_after_del_shallow False`；`del box` 后弱引用才失效
- 结论：Human 指出的错误成立

## 最小修复（Job 待做）

1. 第三行预测改为 `False`，推演写明「`box` 仍是强引用」
2. 追加 `del box` + 第四行预测
3. 「能证明 / 不能证明」同步改写：归因于剩余强引用集合，不是 `copy` 模块
4. 元数据保留 `gate2_failed: E06` 直至 Gate2 重跑通过

## 等级纪律

| 等级 | 本材料 |
|---|---|
| L2 Canonical Candidate | **当前** |
| L3 Validated | **未完成** — 缺独立执行证据与预测对齐 |
| L4 Production | **未完成** — 缺 Human 接受 |

**禁止**在本 Job 完成前把目录挪到 `L3-validated/` 或 `L4-production/`，或把 `level` 伪标升级。
