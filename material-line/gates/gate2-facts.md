# Gate 2 · 事实门

官方来源、版本、代码运行、预测与实际结果。执行者：CLI + Python + 独立检查器。

## 最低能力清单（目标态）

1. 自动提取 Markdown 中的 Python 代码块
2. 在指定 Python 版本的隔离环境执行
3. 对比预测输出和实际输出
4. 检查运行异常
5. 将运行日志、环境版本、输入哈希、结果写入 Evidence
6. 未执行实验明确标记 `NOT_EXECUTED`

## 本 PR（stub）

`runners/gate2_exec_stub.py`：

- 能 list / extract fenced `python` 块
- 支持 `--dry-run`（不假装已完成完整对比器）
- 完整隔离执行 + 预测对齐 → **后续迭代**

主线门禁版本：Job 声明的 `python_pin`（样板为 **3.11.18**）。
