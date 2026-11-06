# R4 横切 — Skills / Prompts 形态对比（官方 vs 方法论）

| 项 | 内容 |
|----|------|
| 轮次 | R4（基于 R3 五仓深读） |
| 日期 | 2026-11-06（Asia/Shanghai） |
| 输入 | `research/cards/R3-1`…`R3-5` + INDEX |
| 约束 | DC Bot 闭环；不 fork；本文件不写 GitHub |
| 状态 | 草案，供架构组冻结 R3 tags 与 ≤8 ADAPT 候选 |

---

## 1. 形态轴（五仓对照）

| 轴 | anthropics/skills | google/skills | microsoft/skills | obra/superpowers | addyosmani/agent-skills |
|----|-------------------|---------------|------------------|------------------|-------------------------|
| 契约表面 | SKILL.md + agentskills.io spec | SKILL.md + index.json / npx | SKILL.md + AGENTS.md / Explorer | SKILL.md + 多 harness 适配 | SKILL.md + slash commands |
| 内容重心 | 规范样板 + 文档类技能 | 产品/域目录（GCP 深） | Azure/Foundry 上下文包 | 全流程方法论 OS | 生产工程生命周期 + 验收 |
| 许可 | SPDX null；文档技能 source-available | Apache-2.0 | MIT | MIT | MIT |
| 建议 fermin_tag（R3） | depend_candidate / selective borrow | depend_candidate / borrow patterns | watch / selective borrow | borrow / watch-as-full-dep | borrow / depend_candidate |
| 入池策略 | 按 skill 过许可门禁后 ADAPT | 指针索引为主，不镜像 | 非 Azure 当面则 watch | 拆过程技能 ADAPT，不吞 harness | 选生命周期技能 ADAPT |
| Prompts 形态 | 少见独立 prompt 堆；偏 skill 包 | 同左 | AGENTS.md + 技能双轨 | AGENTS.md 引导强制工作流 | commands + references 检查表 |

**横切结论（有证据）：**

1. **统一表面已收敛到 `SKILL.md`**；Pool 仓条目应以此为唯一规范面，避免微软式双路径重复。
2. **官方仓 = 依赖/索引；方法论仓 = ADAPT 原料。** Google/MS 体量大，镜像即违反章程。
3. **许可门禁在 Anthropic 最紧**：整仓 SPDX 空 + 文档技能特殊许可 → 不得批量 ACCEPT。
4. **过程重叠在 Obra ↔ Addy**：计划/TDD/验收需去重后再 ADAPT，避免两套同义 skill。
5. **Prompts 单独成类价值低**（五仓均以 skill+契约为主）；R5 优先 `pool/skills`，`pool/prompts` 仅收显式独立契约片段。

---

## 2. 能力层映射（对照 Fermin Agent Decision）

| Fermin 能力层 | 优先借用形态 | 上游指针（R3） | 备注 |
|---------------|--------------|----------------|------|
| 规范/扫盲 | agentskills.io + template | anthropics/skills | 引用不托管 |
| 执行面安全（CLI/Ubuntu） | help-before-execute 模式 | google/skills `gcloud` 叙事 | 模式借款，非整技能 |
| 云厂商当面 | 目录+安装向导 | google / microsoft | 当面未开则 watch |
| 计划→实现→验收 | 过程 skill 链 | obra + addyosmani | 必须去重 |
| 验收门禁 | DoD / verification / evals | addy + ms eval 叙事 | 对齐 ACCEPT 五条 |
| 物料/Pack 对照 | （本批五仓外） | NVIDIA SimReady 等 R2 | R3 后续切片 |

---

## 3. 去重裁定（Obra × Addy）草案

| 主题 | 倾向保留上游 | 另一侧处理 | 理由 |
|------|--------------|------------|------|
| brainstorm / spec | addy `spec-driven-development` 或 obra `brainstorming` 二选一 ADAPT | 另一侧 REJECT 重复 | 避免双入口 |
| writing/executing plans | obra `writing-plans` / `executing-plans` | addy `/plan` 作对照 | Obra 文件化计划更贴「抗 context 丢失」 |
| TDD | 合并为一条 Fermin `test-driven-development` | 双源 provenance | 同名技能两边都有 |
| 子代理驱动开发 | obra `subagent-driven-development` | addy 无对等则 borrow | 贴 DC Bot 调度角色 |
| verification / DoD | addy `verification` + references | obra `verification-before-completion` 合并 | Addy 检查表更可机读 |
| 全 harness 安装层 | **不进 pool** | watch | 属运行时绑定，非 Fermin 规整技能 |

---

## 4. ≤8 ADAPT 候选（R5 预审，待人点头）

> 规则：MIT/Apache 优先；Anthropic 仅列「许可过关后」占位；不收录攻击向；官方大盘不整仓。

| # | 建议 skill-id | 上游 | pinned_ref（R3） | license | decision | 一句话为何收 | 适用执行面 |
|---|---------------|------|------------------|---------|-----------|--------------|------------|
| 1 | `fermin-using-skills` | addyosmani/agent-skills `skills/using-agent-skills` | `301b02b1…` | MIT | ADAPT | 技能使用元契约，Pool 自举 | DC Bot / Cursor |
| 2 | `fermin-brainstorm-or-spec` | obra `brainstorming` **或** addy `spec-driven-development`（确认时二选一） | 见 R3-4/5 | MIT | ADAPT | 需求澄清入口唯一化 | Human→Agent Decision |
| 3 | `fermin-writing-plans` | obra `writing-plans` | `22f0b463…` | MIT | ADAPT | 文件化计划抗上下文丢失 | DC Bot 任务包 |
| 4 | `fermin-executing-plans` | obra `executing-plans` | 同上 | MIT | ADAPT | 计划执行与拆分 | Cursor Cloud / Ubuntu |
| 5 | `fermin-subagent-driven-dev` | obra `subagent-driven-development` | 同上 | MIT | ADAPT | 子代理闭环贴调度站角色 | DC Bot 调度 |
| 6 | `fermin-tdd` | obra 与 addy 的 TDD **合并改编** | 双 SHA | MIT | ADAPT | 统一测试驱动门禁 | 编码执行面 |
| 7 | `fermin-verification-dod` | addy verification + `references/definition-of-done` | `301b02b1…` | MIT | ADAPT | 可机读验收，对齐入库门禁 | 全执行面 |
| 8 | `fermin-skill-anatomy` | addy `docs/skill-anatomy`（改编为 skill）或 obra `writing-skills` | 见 R3 | MIT | ADAPT | 写/改 Skill 的自举教材 | Pool 维护 |

**明确本批不进 ≤8（REJECT / watch 预登记）：**

- anthropics 文档类技能（许可未清）→ `rejected/` 待许可矩阵  
- google/microsoft 整仓目录 → depend 索引，不作 ADAPT 条目  
- obra 全量 harness / telemetry companion → watch  
- addy `security-and-hardening` → 需人 ACCEPT 且仅防御叙事  

---

## 5. 知态与下一步

| 主张 | 知态 |
|------|------|
| 五仓形态轴与 tag | 有证据（R3 卡片） |
| ≤8 候选列表 | 暂采用（待架构确认） |
| Obra/Addy 去重裁定 | 暂采用 |
| agent-skills-pool 远程仓 | **未知/不存在**（2026-11-06 17:58 查 `fmgwhwc` 无此仓） |

**Bot 可继续（不等人）：** 本地 pool 骨架、`meta.yaml` 样例、rejected 预登记草稿。  
**人必须做的一步：** 在 GitHub 新建空仓 `agent-skills-pool` 并把 URL 发回（章程 §4）。
