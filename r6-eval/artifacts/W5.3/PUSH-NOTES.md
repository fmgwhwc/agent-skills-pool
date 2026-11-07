# W5.3 PUSH-NOTES — CloudAgent overwrite map

Timestamp: 2026-11-07 08:49:24 CST (Asia/Shanghai)  
Source package: `/workspace/fermin-main-subject/r6-w5.3.zip`  
Repo: `fmgwhwc/agent-skills-pool`  
Constraint origin: Bot prepared locally; **this file tells CloudAgent what to write**.

## Recommended PR title

`R6 W5.3: pool docs sync — eight released skills + validate_r5 admission/release split`

## Recommended PR body (short)

W5.3 pool docs sync after S12 release. Apply catalog released overlay, sync README/ATTRIBUTION/rejected, split validate_r5 admission vs release modes. No SKILL.md body changes. Retained limits: same-author self-review; S11 static loader; no live multi-agent production.

## Exact repo paths to overwrite / add

| Repo path | Action | Local source in zip / workspace |
|-----------|--------|----------------------------------|
| `README.md` | **overwrite** | `r6-eval/artifacts/W5.3/README.repo.md` |
| `ATTRIBUTION.md` | **overwrite** | `r6-eval/artifacts/W5.3/ATTRIBUTION.md` (same as r5-adapt-batch/attribution/ATTRIBUTION.md) |
| `catalog.yaml` | **overwrite** | `r6-eval/artifacts/W5.3/catalog.yaml` (eight released schema-required entries; version 1) |
| `catalog-entries.yaml` (if tracked at root or under tooling) | **overwrite** | `r6-eval/artifacts/W5.3/catalog-entries.yaml` — **full provenance + quality_gate + r6_promotion** |
| `validate_r5.py` | **overwrite** | `r6-eval/artifacts/W5.3/validate_r5.py` |
| `rejected/README.md` | **add** | `r6-eval/artifacts/W5.3/rejected-README.md` |
| `rejected/2026-11-07-r5-path-corrections.md` | keep/ensure present | already on main from R5 if pushed |
| `attribution/ATTRIBUTION.md` | **overwrite** if mirrored under attribution/ | same ATTRIBUTION body |
| `pool/skills/*/meta.yaml` (×8) | **overwrite** if S12 metas not yet on main | from S12 push / `pool-skills-meta/...` in r6-w5.2.zip — status must be `released` |
| `r6-eval/WAVE-W5.3-REPORT.md` | **add** | included in zip |
| `r6-eval/ledger.md` | **overwrite** | W5.3 row complete |
| `r6-eval/artifacts/W5.3/**` | **add** | self-check + drafts + PUSH-NOTES |

## What CloudAgent must write into repo `catalog.yaml`

Use the eight-entry released index (schema-required fields only is OK at root `catalog.yaml`):

- `version: 1`
- `updated: "2026-11-07"`
- Each entry: `id`, `path`, `status: released`, `source` (repo/ref/path/url/license), `license_spdx`, `decision: adapt`, `rationale`, `fermin_tags`, `epistemic: evidenced`

Do **not** drop provenance. Full `quality_gate` / `adapted_from` / `r6_promotion` belong in `catalog-entries.yaml` (or merged into catalog if the repo keeps a single fat catalog — prefer merge-by-id without deleting fields).

If main already has a fat `catalog.yaml` from R5 candidates: **merge by id**, set `status: released`, set `quality_gate.runtime_scenarios` + `release` to `pass`, attach `r6_promotion` from the overlay; keep source pins.

## Validator

After push, CI or local:

```bash
python validate_r5.py --mode auto
# or explicitly:
python validate_r5.py --mode release
```

Do not run `--mode admission` against the released tree expecting PASS.

## Do not

- Rewrite any `SKILL.md` bodies.
- Invent new skills.
- Promote anything from `rejected/`.
- Claim live multi-agent or live loader proof.
