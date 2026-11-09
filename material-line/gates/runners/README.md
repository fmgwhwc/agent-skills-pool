# Gate runners

| 脚本 | 作用 | 成熟度 |
|---|---|---|
| `gate1_check.py` | 结构 / YAML / 目录自检 | **init 可跑**（`--self-test`） |
| `gate2_exec_stub.py` | 提取 python fence；`--dry-run` | **stub** → 完整对比器后续 |

依赖：标准库 + PyYAML（与根 `requirements-validation.txt` 一致即可）。

```bash
python material-line/gates/runners/gate1_check.py --self-test
python material-line/gates/runners/gate2_exec_stub.py --dry-run material-line/materials/L2-canonical-candidate/PYTEXT-PY-RAW-040/NOTES.md
```

不修改 `validate_r5.py` 行为。
