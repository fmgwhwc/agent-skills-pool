# Gate 1 · 结构门

检查 YAML、目录、Job BRIEF、物料 INDEX 字段完整性。执行者：CLI / Python（`runners/gate1_check.py`）。

## 最低检查项

1. `material-line/` 关键子目录存在（schemas / subjects / themes / jobs / materials / gates / evidence / retrospectives / value-cards）
2. schemas 五个文件存在
3. 样板 subject / theme / value-card / QUEUE / 样板 Job（`job.yaml` + `BRIEF.md`）存在
4. `materials/INDEX.yaml` 可解析且含 `PYTEXT-PY-RAW-040`
5. L2 候选目录含 `LEVEL.yaml`（level 为 L2，非伪 L3/L4）
6. L3 / L4 目录存在（可空）

失败 → exit ≠ 0。

```bash
python material-line/gates/runners/gate1_check.py --self-test
python material-line/gates/runners/gate1_check.py
```
