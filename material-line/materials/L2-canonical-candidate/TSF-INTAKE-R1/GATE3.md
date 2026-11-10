# GATE3 — JOB-TSF-INTAKE-R1

| 字段 | 值 |
|---|---|
| job | JOB-TSF-INTAKE-R1 |
| decision | 接受（ACCEPT） |
| decider | user fermin gl via DC Bot |
| timestamp | 2026-11-10 Asia/Shanghai |
| scope | `fermin-tsf-itinerary-structure`, `fermin-tsf-landscape-shoot`, `fermin-tsf-food-discovery` |
| channel | DC Bot chat |

## 含义

- **ACCEPT** 是 Human Gate3 裁决：三条 TSF Fermin candidate 的相关性 / 可装载性 / 值得进入 Fermin 限定集，予以接受。
- **不是** release 晋升。`status` 保持 `candidate`。
- `quality_gate.runtime_scenarios` 与 `quality_gate.release` **仍为 pending**（无 runtime scenario pack）。
- 本轮同步完成上游 pin 冻 SHA（见 `evidence/JOB-TSF-INTAKE-R1/PIN-FREEZE.md`）。
- FerroxLabs/murage AGPL vs Apache frontmatter **仍 HOLD**；禁止正文进 pool。

## 剩余风险（接受后仍开放）

- 无 runtime scenario pack → 不可标 `released`。
- makaronz/skilslsls 无仓级 SPDX（仅 cite + SHA 冻结）。
- murage 许可冲突未澄清。
