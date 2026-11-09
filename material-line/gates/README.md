# Gates（质量门）

| Gate | 文档 | Runner | 本 PR 深度 |
|---|---|---|---|
| Gate1 结构 | `gate1-structure.md` | `runners/gate1_check.py` | **可跑** + `--self-test` |
| Gate2 事实 | `gate2-facts.md` | `runners/gate2_exec_stub.py` | **stub**：提取 fence + `--dry-run` |
| Gate3 接受 | `gate3-accept.md` | Human | 文档 only |

原则：生成完成 ≠ 事实已验证。同一物料禁止单一模型既生产又自证通过。

Skills 池仍用根 `validate_r5.py`；本目录门禁只管 **物料 Job**。
