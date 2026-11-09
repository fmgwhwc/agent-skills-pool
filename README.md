# agent-skills-pool

Fermin 规整后的 Agent Skills / Prompts 池（验证开发仓）。

## Charter (not a fork)

- **不是**上游仓的 fork 或 mirror；不做整仓搬迁。
- 条目保留 `source.repo` / `source.ref` / `source.path` / `license`；多源条目见 `ATTRIBUTION.md`。
- 分析与筛选在 DC Bot 闭环；写入经 Cloud Agent；**ACCEPT/ADAPT 才进 `pool/`**；REJECT 进 `rejected/`。
- 详见 `research/` 与章程 `agent-skills-pool-charter.md`（若已同步）。

## Released process skills (R6)

Eight process skills completed R5 ADAPT intake and R6 scenario evaluation (S01–S12). Catalog / meta `status: **released**` as of 2026-11-07 (Asia/Shanghai).

| id | role (short) | Primary upstream pin |
|----|--------------|----------------------|
| `fermin-using-skills` | Router / minimal applicable workflow | addyosmani/agent-skills@301b02b1… |
| `fermin-brainstorm-or-spec` | Requirements intake + acceptance | addyosmani + obra |
| `fermin-writing-plans` | Atomic task / evidence contracts | obra/superpowers@22f0b463… |
| `fermin-executing-plans` | Resumable single-executor loop | obra/superpowers@22f0b463… |
| `fermin-subagent-driven-dev` | Scheduler / bounded task packs | obra/superpowers@22f0b463… |
| `fermin-tdd` | RED→GREEN + honest fixtures | obra + addyosmani |
| `fermin-verification-dod` | Acceptance + standing DoD gate | addyosmani + obra |
| `fermin-skill-anatomy` | Portable authoring / provenance | addyosmani + obra |

- Packages: `pool/skills/<id>/` (`SKILL.md` + `meta.yaml` [+ `references/`])
- Index: `catalog.yaml` (machine) — merge provenance from R5/R6 catalog overlay
- Promotion record: `r6-eval/artifacts/S12/PROMOTION.md`
- Progress ledger: `r6-eval/ledger.md`
- Attribution: `ATTRIBUTION.md` + `attribution/*.txt`
- Rejected (not promoted): `rejected/`

### Retained limitations (do not advertise as cleared)

1. **Same-author self-review** across R6 evidence runs (disclosed in evidence YAML).
2. **S11 static host-route / loader simulation only** — no live Cursor Agent Skills loader or live DC Bot skill-install path.
3. **No live multi-agent production traffic** was exercised.

### Validation

```bash
pip install -r requirements-validation.txt   # or repo-equivalent
python validate_r5.py --mode auto            # per-skill: candidate→admission; released→release
python validate_r5.py --mode admission       # R5 ADAPT intake: require candidate + pending gates
python validate_r5.py --mode release         # require released + runtime/release pass + evidence paths
python validate_r5.py --self-test --mode auto
```

## Roadmap

| Wave | Goal | Status |
|------|------|--------|
| W0 | Evidence scaffolding (`r6-eval/`) | **done** |
| W1 | Router + validator discrimination (S01/S02/S08) | **done** |
| W2 | Spec / plan / resume (S03/S04) | **done** |
| W3 | Dispatch / collision / permission (S05/S06/S10) | **done** |
| W4 | TDD + authoring baseline (S07/S09) | **done** |
| W5.1 | Loader portability (S11) | **done** |
| W5.2 | Candidate→release (S12) | **done** |
| W5.3 | Pool docs sync (README / ATTRIBUTION / rejected / validator split) | **done** |
| W6 | Material Line init (`material-line/` scaffold + Gate1 self-test) | **done** |
| W6.1 | TSF intake R1 — theme collect → material-line → 3×`fermin-tsf-*` candidates | **this wave** |
| W6.x | Sample offline Job closed loop (E06 fix → Gate2 evidence → Gate3) | next |

## Layout

```text
agent-skills-pool/
├── README.md
├── LICENSE
├── ATTRIBUTION.md
├── catalog.yaml            # Skills index (≠ materials INDEX)
├── validate_r5.py
├── schema/
├── pool/skills/            # eight released process packages + TSF candidates
├── raw/                    # archival upstream snapshots at R3 pins (not loadable; loaders use pool/ only)
├── rejected/               # scoped rejects (not entries)
├── attribution/            # upstream MIT notices
├── research/               # Bot-closed process artifacts
├── r6-eval/                # scenarios, evidence, ledger, wave reports (retained)
└── material-line/          # Material production line (subjects/themes/jobs/materials/gates) + TSF intake
```

---

## Current maturity: demo + init

**demo + init**：Skills 半成品货架与过程技能已立（R6 released + raw 对回 + `validate_r5.py`）；**尚未**达到可脱机 Job、可持续产出有主体 / 功能 / 主题 / 价值的物料级规模。

KPI 改口后看 **物料 Job 闭环数**，不是 Skills 条目堆叠或流程文厚度。

## Target: Material production line

在保留现有 Skills 池与 R6 过程资产的前提下，增量建设 **物料产出生产线（Material Line）**：

> 脱机 Job → 主题物料 → Gate1/2/3 → Canonical 候选 → Human 接受

设计对象：

| 维度 | 含义 |
|------|------|
| Subject | 为谁存、谁用、谁验收 |
| Function | 装上后 Agent 多会做哪类事 |
| Theme | 窄、可证伪的主题包（如 Python 对象模型 / 弱引用；或 TSF 旅游×风景×美食） |
| Value | Human 可一句话否决或接受的价值陈述 |
| Offline Job | 可调度单元：锁版本 → 出稿 → Gate → 交审 |
| Gates | Gate1 结构 → Gate2 事实/代码 → Gate3 Human |
| L0–L4 | Raw → Parsed → Canonical Candidate → Validated → Production |

章程与样板：[`material-line/README.md`](material-line/README.md) · 方案副本 `material-line/OPTIMIZATION-PLAN.md` · 进度 `material-line/STATUS.md`。

**分流：** `catalog.yaml` = Skills 装载面索引；`material-line/materials/INDEX.yaml` = 主题物料索引。二者独立，禁止混称「进 pool 就算物料完成」。
