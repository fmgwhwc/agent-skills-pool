# agent-skills-pool

Fermin 规整后的 Agent Skills / Prompts 池。

- **不是**上游仓的 fork 或 mirror。
- 条目保留 `source.repo` / `source.ref` / `source.path` / `license`。
- 分析与筛选在 DC Bot 闭环；写入经 Cloud Agent；ACCEPT/ADAPT 才进 `pool/`。

## Current candidates (R5)

Eight reviewed Fermin process-skill candidates live under `pool/skills/` (`status: candidate`; runtime release gates still pending). Provenance, adaptation notes, and static validation are summarized in [`research/reports/R5-ADAPT-REPORT.md`](research/reports/R5-ADAPT-REPORT.md). Machine index: `catalog.yaml`.

## Roadmap (R6)

- Item-by-item build and eval plan: [`research/matrix/R6-item-build-plan.md`](research/matrix/R6-item-build-plan.md)
- Eval harness + evidence: [`r6-eval/`](r6-eval/) — **W0 complete**; **S01** / **S02** / **S03** / **S04** / **S05** / **S06** / **S07** / **S08** / **S09** / **S10** **pass**; `fermin-using-skills` Step 4 typo-path clarification applied. Skills remain `candidate` (W1.4 applied; W2.1–W2.2 done; W2.3 skipped — no copy edits; W3.1 S05 pass; W3.2 S06 pass; W3.3 S10 pass; W3.4 skipped — no verification-dod matrix edits; W4.1 S07 pass; W4.2 S09 pass; W4.3 skipped — no tdd/anatomy body edits).

详见 `research/` 与上级章程 `agent-skills-pool-charter.md`（首次推送时同步）。
