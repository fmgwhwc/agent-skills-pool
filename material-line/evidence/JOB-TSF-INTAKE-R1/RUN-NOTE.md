# RUN-NOTE — JOB-TSF-INTAKE-R1

| 字段 | 值 |
|---|---|
| run_date | 2026-11-09 Asia/Shanghai |
| actor | Cursor Cloud Agent |
| authorization | Human authorized build+verify |
| branch | `cursor/tsf-intake-r1-7c93` |

## 执行摘要

1. 读取上传 INTAKE-BRIEF / intake-queue / VERDICT-SEED / THEME pipeline 叙事。
2. 增量创建 `material-line/`（theme/subject/value-card/job/L2/evidence/STATUS/PROCESS-LOG/INDEX）。
3. Live GitHub API 核验 adapt/hold 路径 EXISTS + 许可笔记（尤其 murage AGPL）。
4. 写入三条 `fermin-tsf-*` candidate（SKILL.md + meta.yaml）；**未**复制 murage 正文。
5. 追加 `catalog.yaml` / `catalog-entries.yaml`；扩展 `validate_r5.py` 以容纳 TSF candidate。
6. 打开 PR；无删除 `pool/raw/r6-eval`；status 均为 candidate。

## 非目标（本轮未做）

- 未写真实城市攻略/店名清单当 Skill 终点
- 未 mark released
- 未冻 SHA（保留 pin_pending）
