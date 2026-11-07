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
| W5.3 | Pool docs sync (README / ATTRIBUTION / rejected / validator split) | **this wave** |

## Layout

```text
agent-skills-pool/
├── README.md
├── LICENSE
├── ATTRIBUTION.md
├── catalog.yaml
├── validate_r5.py
├── schema/
├── pool/skills/          # eight released packages
├── rejected/             # scoped rejects (not entries)
├── attribution/          # upstream MIT notices
├── research/             # Bot-closed process artifacts
└── r6-eval/              # scenarios, evidence, ledger, wave reports
```
