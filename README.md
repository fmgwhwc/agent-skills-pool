# agent-skills-pool

Fermin 规整后的 Agent Skills / Prompts 池。

- **不是**上游仓的 fork 或 mirror。
- 条目保留 `source.repo` / `source.ref` / `source.path` / `license`。
- 分析与筛选在 DC Bot 闭环；写入经 Cloud Agent；ACCEPT/ADAPT 才进 `pool/`。

## Current process skills (R5 → R6 released)

Eight reviewed Fermin process skills live under `pool/skills/` with **`status: released`** after **S12** candidate→release governance (`quality_gate.runtime_scenarios` / `release`: pass). Retained limits stay explicit: same-author self-review; S11 static loader only; no live multi-agent production. See [`r6-eval/artifacts/S12/PROMOTION.md`](r6-eval/artifacts/S12/PROMOTION.md). Provenance and adaptation notes: [`research/reports/R5-ADAPT-REPORT.md`](research/reports/R5-ADAPT-REPORT.md). Machine index: `catalog.yaml`.

## Roadmap (R6)

- Item-by-item build and eval plan: [`research/matrix/R6-item-build-plan.md`](research/matrix/R6-item-build-plan.md)
- Eval harness + evidence: [`r6-eval/`](r6-eval/) — **W0 complete**; **S01**–**S12** **pass**; `fermin-using-skills` Step 4 typo-path clarification applied. Eight process skills are **`released`** with retained limits (W1.4 applied; W2.1–W2.2 done; W2.3 skipped — no copy edits; W3.1 S05 pass; W3.2 S06 pass; W3.3 S10 pass; W3.4 skipped — no verification-dod matrix edits; W4.1 S07 pass; W4.2 S09 pass; W4.3 skipped — no tdd/anatomy body edits; W5.1 S11 pass; W5.2 S12 pass — see [`r6-eval/artifacts/S12/PROMOTION.md`](r6-eval/artifacts/S12/PROMOTION.md)).

详见 `research/` 与上级章程 `agent-skills-pool-charter.md`（首次推送时同步）。
