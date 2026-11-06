# R5 ADAPT report — Fermin process foundations

| Item | Result |
|---|---|
| Date | 2026-11-07 (Asia/Shanghai) |
| Scope | Eight selected process skills; local-only DC Bot content adaptation, no repo/fork/PR/push |
| Source pins | `addyosmani/agent-skills@301b02b12bff98e4688e6984af6556802322bbde`; `obra/superpowers@22f0b463e7a5e579904dd6211a520321035526f7` |
| License inspection | Both upstream root MIT license texts read at their exact pins; original notices preserved in `attribution/` |
| Rule compliance | Selective path reads only, no clone/mirror, no Anthropic doc-skill content, no security/hardening batch, no harness installers/telemetry imports |
| State | All eight `status: candidate`; no claimed runtime effectiveness or release |
| Layout | `pool/skills/<skill-id>/{SKILL.md,meta.yaml}`; only three skill-local support files, each linked directly from SKILL.md |

## 1. Deliverables and one-line verdict

| Skill | Primary provenance | Lines | Candidate verdict | Main Fermin rewrite / quality decision |
|---|---|---:|---|---|
| `fermin-using-skills` | Addy `skills/using-agent-skills/SKILL.md` | 106 | **Keep as candidate:** compact router rather than a full lifecycle dump. | Minimum applicable skill; assets/ledger/authority before routing; no nonexistent upstream skill links. |
| `fermin-brainstorm-or-spec` | Addy `skills/spec-driven-development/SKILL.md` + selective Obra brainstorming | 131 | **Keep as candidate:** clear DoD plus focused clarification; needs user-loop scenario tuning. | Addy selected primary for observable acceptance/capability mapping; Obra supplies question quality. Removes mandatory hard gate, visual companion, and code-stack boilerplate. |
| `fermin-writing-plans` | Obra `skills/writing-plans/SKILL.md` | 157 | **Keep as candidate:** atomic task/evidence contracts survive handoff without over-specifying code. | Exact inputs/outputs/interfaces and single-owner integration; research/skill tasks get non-code acceptance. |
| `fermin-executing-plans` | Obra `skills/executing-plans/SKILL.md` | 129 | **Keep as candidate:** resumable one-session execution with visible rulings and evidence. | Replaces shell/BASE/worktree machinery with durable ledger, output and integrated-check contracts. |
| `fermin-subagent-driven-dev` | Obra `skills/subagent-driven-development/SKILL.md` and implementer brief | 146 | **Keep as candidate:** scheduler-role fit is strong; actual worker/dispatcher run remains pending. | Bounded task pack and report file, separate review, serialized shared mutations; strips model-price/tier and rigid-round rules. |
| `fermin-tdd` | Obra + Addy `skills/test-driven-development/SKILL.md` | 153 | **Keep as candidate:** useful merged evidence loop; no fictional unit tests for prose. | Observed RED/GREEN plus stack discovery and real boundaries; explicit honest characterization/skill-fixture path. |
| `fermin-verification-dod` | Addy `references/definition-of-done.md`, Addy using-agent-skills + Obra verification-before-completion | 144 | **Keep as candidate:** acceptance and standing DoD are distinct and evidence-linked; false upstream path fixed. | Per-claim matrix and truthful candidate/partial/blocked statuses; pool candidate/release separation. |
| `fermin-skill-anatomy` | Addy `docs/skill-anatomy.md` + selective Obra `writing-skills` | 195 | **Keep as candidate:** self-bootstraps authoring while retaining provenance and unrun gates; no fabricated baseline. | Portable agent-skill frontmatter beside rich meta; package references travel; scenario/eval taxonomy, not auto-deploy checklists. |

Line counts above are approximate if subsequent editorial fixes are made; `validate_r5.py` checks every body remains at or below 400 lines. Bodies were intentionally kept shorter where sufficient rather than padded to the upper limit.

## 2. Adaptation map and source trace

| Target | `source.repo / source.ref / source.path` | Decision | `license_spdx` | Source and quality evidence |
|---|---|---|---|---|
| using-skills | Addy @ `301b02b12…2bbde` / `skills/using-agent-skills/SKILL.md` | ADAPT | MIT | Skill usage routing and evidence rule read; new R5-only Fermin route. |
| brainstorm-or-spec | Addy @ same / `skills/spec-driven-development/SKILL.md`; Obra @ `22f0b463…526f7` / `skills/brainstorming/SKILL.md` | ADAPT merged | MIT AND MIT | Acceptance/capability + intent/question patterns; one entry only. |
| writing-plans | Obra @ same / `skills/writing-plans/SKILL.md` | ADAPT | MIT | Exact interface and proportionate task detail retained. |
| executing-plans | Obra @ same / `skills/executing-plans/SKILL.md` | ADAPT | MIT | Recovery, completion, rulings, integrated review retained. |
| subagent-driven-dev | Obra @ same / `skills/subagent-driven-development/SKILL.md`, `implementer-prompt.md` | ADAPT | MIT | Worker state/report brief-file ideas read at same pin. |
| tdd | Obra + Addy @ their respective same pins / `skills/test-driven-development/SKILL.md` | ADAPT merged | MIT AND MIT | Duplicate upstream workflows reconciled into one canonical owner. |
| verification-dod | Addy @ same / `references/definition-of-done.md`, `skills/using-agent-skills/SKILL.md`; Obra @ same / `skills/verification-before-completion/SKILL.md` | ADAPT merged | MIT AND MIT | Nonexistent verification-skill path replaced with real, read files. |
| skill-anatomy | Addy @ same / `docs/skill-anatomy.md`; Obra @ same / `skills/writing-skills/SKILL.md` | ADAPT merged | MIT AND MIT | Portable anatomy + authoring verification; no universal testing dogma. |

Full SHAs and blob URLs appear in every primary `meta.yaml`, every contributing `adapted_from` object, and `catalog-entries.yaml`. `license_evidence` records exact LICENSE links and copyright holders. A source-level `license: MIT` accompanies each contributing path. Multi-source licenses mean both upstream MIT notices are retained, not replacement of Fermin's own root packaging license.

## 3. Obra × Addy dedup decisions

1. **Spec wins as primary over separate brainstorming.** Addy supplies an explicit verification section and scopes multi-capability decomposition by independently testable behavior. Obra's approach-first conversation improves requirements quality but overlaps the same intake capability, so it is a secondary source not a ninth entry.
2. **Writing/executing plans stay Obra-owned.** Addy is referenced indirectly as the spec input only; there is no duplicate Addy planning/workflow clone.
3. **TDD is one Fermin entry.** Addy contributes repository-tool discovery and testing distinctions; Obra contributes strong observed-RED behavior and anti-rationalization. Duplicated examples, rationalization lists, and browser-specific appendices are removed.
4. **Verification/DoD is one Fermin entry.** Addy's standing DoD is made portable inside `references/fermin-dod.md`; Obra's fresh-evidence rule is integrated into the same gate rather than becoming a sibling skill.
5. **Skill anatomy is one authoring entry.** Addy anatomy provides discovery and packaging rules; Obra contributes failure-driven scenario evaluation. Runtime installer/deployment checklists remain outside the pool content.
6. **Subagent scheduling is one distribution mode.** No second upstream-orchestration checklist is adopted. Native and subagent plans refer to the same ledger/evidence concepts.

## 4. Upstream quality issues found at the pinned inputs

| Upstream defect / risk | Action |
|---|---|
| R4 expected a standalone Addy `skills/verification/SKILL.md`; 404 at the pinned SHA. | Exact-path correction documented and excluded from provenance; alternative real paths inspected before use. |
| Addy's required reference `../../references/definition-of-done.md` is outside the per-skill directory, a portability gap acknowledged upstream (#361). | Fermin DoD adaptation is bundled with its owning skill. Only three needed references are packaged across the batch. |
| Addy has skill rollout links to many skills not present in the R5 skeleton. | R5 router only links to the eight local Fermin capabilities, avoiding dead upstream references. |
| Both upstream packs contain fairly absolute process directives, repetitive rationalizations, and model/workflow-specific requirements. | Replaced with observable condition/action/artifact/evidence; retained authority and proportional-validation escape hatches without reverting to generic advice. |
| Obra has worktree/shell scripts, mandatory commit/finish workflow, visual companion and model-tier/price choices. | Removed from portable process content. Pool changes stay local in R5; Cloud Agent is the parent's choice, not embedded in every workflow. |
| Addy promotes production claims and fixed pyramid percentages; Obra cites measured real-session/model behavior. | No unverified or unmeasured claim is restated as Fermin result. Attribution/pending evidence remain explicit; star counts are absent from skill body decisions. |
| Addy cites WikiSkill arXiv `2608.27454` for cross-model transfer effects. | Not independently read or validated in R5, so not used as factual support. Fermin asks for disclosed comparisons instead. |
| Obra writing-skills recommends costly repeated pressure tests and per-edit absolutes while forbidding batching. | Each candidate still needs an appropriate discriminating evaluation, but R5 clearly reserves runtime scenarios for the next gate rather than inventing them cheaply. |

See `rejected/2026-11-07-r5-path-corrections.md` for the exclusions/corrections. Existing R4 rejects (Anthropic doc license pending, Google/Microsoft wholesale catalogs, harness installs, security batch exclusion) remain unchanged rather than silently accepted.

## 5. Content-quality cuts and rewrites for Fermin

- **From coding-assistant generality to closed-loop assets:** all skills connect decision records, plan/ledger, task packs, evidence, and catalog state. DC Bot retains synthesis; workers get bounded authority.
- **Evidence without ceremony:** test-first retains observed failures where meaningful; skill files use structural + scenario validation, not fake production tests. Every DoD checkbox can be `pending` with truthful status.
- **Portability:** frontmatter uses only `name`, `description`. Rich source/quality fields sit adjacent in `meta.yaml`. Local references avoid sibling/package breakage and upstream harness links.
- **Interface discipline:** shared catalog writes are serialized, interfaces are preflighted, and artifacts not vague summaries are returned by workers.
- **Search/load clarity:** descriptions identify when to load; each body has explicit load/non-load conditions, numbered steps and done-when checks.
- **Permissions remain distinct from procedure:** accepted spec/plan does not grant send/publish/push/spend/delete/install/deployment permission.
- **No generic upstream stack:** no marketplace banners, install commands, telemetry, multi-harness plugins, attack content, warning suppression, or unverified speed promises.
- **Lean package:** eight bodies total ~1,150 lines; long operational templates are separated into three necessary in-package references, not copied whole upstream references directories.

## 6. Real validation and limitations

Validation is implemented in `validate_r5.py` using PyYAML and jsonschema in an isolated local environment. Final commands/results are recorded in `R5-VALIDATION.json` after the last content edit.

The validator checks:

- exactly eight named skill directories and catalog entries;
- portable YAML frontmatter, `name == directory`, kebab-case names, description ≤1024 chars and explicit Use-when/Use-for triggers;
- required load/steps/done-when sections and ≤400 lines per body;
- adjacent meta against the existing `skill-entry.schema.json` (all eight);
- primary and contributing source objects with correct 40-character R3 pins, path+SHA URLs and source-level MIT markers;
- required skill package references, relative link targets, three declared surfaces, status and candidate/pending gate states;
- catalog entry parity with every meta object, relative catalog paths, rejection notes and attribution notices.

It also runs a full catalog merge against a copy of the R4 skeleton with unique IDs and working local paths. A mutation check deliberately changes a copied skill SHA and requires the validator to reject it, so validation is not treated as success merely because a script exists.

These are **static/structural/manual-content checks**, not proof of operational effectiveness. No fresh subagent baseline-vs-skill behavior trial, Cursor Cloud/Ubuntu execution, or release-owner acceptance was performed. All eight remain `candidate` with `runtime_scenarios: pending` and `release: pending`.

### Recommended next evaluation gate (not completed)

1. Run plan-resume and one bounded Cloud Agent/task-pack dispatch with two non-overlapping outputs, then an adversarial shared-catalog collision.
2. Run a requirements scenario showing a clear request does not spawn an unnecessary long spec, and a genuinely unclear request produces useful acceptance questions.
3. Load one prototype skill through its expected runtime loader to verify adjacent meta is ignored safely and frontmatter discovery works.
4. Run one actual code TDD scenario plus the R5 static-validator broken fixture and scenario review.
5. Evaluate all skill routes against an out-of-scope/external action request, ensuring no permission is invented.

These checks should be performed by parent/authorized workers with output artifacts and rubric scores. Only after review should relevant candidates move to `released`.

## 7. Integration instructions for the parent Cloud Agent

1. Copy the entire `pool/skills/` tree, each containing SKILL + meta and linked references as appropriate.
2. Merge the eight items from `catalog-entries.yaml` by ID into the repository's `catalog.yaml` (bump its version/update per existing convention).
3. Keep `R5-ADAPT-REPORT.md` under `research/reports/`, rejection update under `rejected/`, and include upstream notices under `attribution/` or roll their equivalent content into a root `ATTRIBUTION.md`.
4. Retain original root Fermin `LICENSE`; do not overwrite it with either upstream license.
5. Run `validate_r5.py` from this content directory before copying/committing. A schema copy and `requirements-validation.txt` are included. Install its two small validation dependencies and run from the package root as `python validate_r5.py --self-test`; the normal catalog overlay is checked by ID, using the included empty R4 base overlay fixture (merge behavior with pre-existing other-pool entries is not assumed). The validator is tooling, not a skill runtime dependency.
6. Do not advertise candidates as released; no Anthropic or security content is included.

**Suggested commit subject:** `R5: add eight Fermin process skill candidates`

**Recommended push task summary:** `Add the eight reviewed R5 ADAPT skill packages, full pinned provenance and MIT attributions, candidate catalog entries, and the R5 source-correction report. Runtime release gates remain explicitly pending.`

This recommendation describes content only. The parent owns any Cloud Agent invocation, repository write, PR, or merge.
