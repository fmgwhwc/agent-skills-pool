# JOB-TSF-INTAKE-R1 — Expected outputs

## Gate1（结构）

- [x] `THEME-trip-scenic-food.yaml` / subject / value-card
- [x] `jobs/JOB-TSF-INTAKE-R1/{job.yaml,BRIEF.md,EXPECTED.md,intake-queue.yaml}`
- [x] `QUEUE.yaml` 含本 Job
- [x] L2 包：`README.md` `LEVEL.yaml` `VERDICT.md` `MATRIX.md`
- [x] `STATUS.md` / `PROCESS-LOG.md` / materials `INDEX.md` 已更新

## Gate2（核验）

- [x] `evidence/.../PATH-CHECK.md`：C01,C02,C03,C04,C06,C07,C08,C09,C10 EXISTS
- [x] `evidence/.../LICENSE-NOTES.md`：murage AGPL vs claimed Apache → HOLD；makaronz 无仓级 SPDX
- [x] `evidence/.../RUN-NOTE.md`：本轮执行说明

## Fermin 产物

- [x] `pool/skills/fermin-tsf-itinerary-structure/{SKILL.md,meta.yaml}` status=candidate
- [x] `pool/skills/fermin-tsf-landscape-shoot/{SKILL.md,meta.yaml}` status=candidate
- [x] `pool/skills/fermin-tsf-food-discovery/{SKILL.md,meta.yaml}` status=candidate
- [x] `catalog.yaml` / `catalog-entries.yaml` 追加三条（不标 released）
- [x] **不**复制 murage AGPL 正文进 pool

## Gate3

- [x] Human：**接受（ACCEPT）** — 2026-11-10 Asia/Shanghai；decider=user fermin gl via DC Bot；scope=三条 `fermin-tsf-*`
- [x] 记录：`GATE3.md`（Job + L2 pack）；`STATUS.md` / `QUEUE.yaml` / `PROCESS-LOG.md`
- [x] Pin 冻 SHA：`evidence/.../PIN-FREEZE.md`；meta/catalog 移除 `pin_pending`
- [x] **未**升 `status=released`；`quality_gate.runtime_scenarios` / `release` 仍 pending
- [x] murage AGPL HOLD 不变；未复制正文
