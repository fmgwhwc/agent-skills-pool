# R6 逐项构建计划 — agent-skills-pool 过程技能候选 → 可 release

| 项 | 内容 |
|----|------|
| 日期 | 2026-11-07（Asia/Shanghai） |
| 仓 | https://github.com/fmgwhwc/agent-skills-pool （验证开发仓；可直接推/合） |
| 输入 | R5 八条 `candidate`（main）+ `research/reports/R5-NEXT-EVALUATION.md` |
| 原则 | Bot 侧内容与质量优先；每项 = **改写/补强** + **场景跑证** + **证据入仓**；不冒充未跑过的 pass |
| 状态约定 | `candidate` → `eval_partial` → `eval_pass` → `release`（须 owner 或授权 Bot 按门禁升） |

---

## 总览：五波，每波可独立交付

| 波次 | 目标 | 主技能 | 场景（来自 R5-NEXT） | 交付物 |
|------|------|--------|---------------------|--------|
| **W0** | 证据轨与跑证脚手架 | （基建） | — | `r6-eval/` 目录、证据模板、ledger、场景 ID 表 |
| **W1** | 路由与静态门禁 | using-skills；skill-anatomy 轻触；validate | Router/low；Validator discrimination | 证据 YAML + 必要 SKILL 修补 |
| **W2** | 需求→计划闭环 | brainstorm-or-spec；writing-plans；executing-plans | Requirements splitting；Resume | 计划样例包 + 证据 + 文案收紧 |
| **W3** | 调度与验收 | subagent-driven-dev；verification-dod | Dispatch isolation；Shared-write；Permission negative | task-pack 实跑痕迹 + DoD 修补 |
| **W4** | TDD 与自举写作 | tdd；skill-anatomy | Code RED/GREEN；Authoring baseline | 可丢弃 fixture + 评分表 |
| **W5** | 装载与升格 | 全八条 | Loader portability；Candidate→release | catalog 升格批 + release 笔记 |

每波结束：**Bot 本地证据** → Cloud Agent 推 PR → 直接合 `main`（验证仓授权）。

---

## W0 — 证据轨（先做，约 0.5 单元）

1. 在仓内建立：
   - `r6-eval/README.md`（怎么跑、结果怎么写）
   - `r6-eval/scenarios.yaml`（12 场景 ID 与技能映射）
   - `r6-eval/evidence/_template.yaml`
   - `r6-eval/ledger.md`（进度总表）
2. Done-when：模板可填；ledger 列出 W1–W5 行且全部 `not-run`。

---

## W1 — 路由 + 校验器（第 1 优先构建项）

| # | 项 | 动作 | Done-when |
|---|----|------|-----------|
| 1.1 | `fermin-using-skills` 场景 A | 刺激：修一处文档 typo（给定路径）；期望不另起 spec/plan | 证据 `pass` 或带 `limitations` 的 `partial`；若 skill 过严/过松则改 SKILL 再跑 |
| 1.2 | `fermin-using-skills` 场景 B | 刺激：「改进 pool」无验收；期望先读后问 / 区分 observed·proposed·unknown | 同上 |
| 1.3 | Validator discrimination | 临时坏 fixture 跑 `validate_r5.py`；源树不变 | 负例按预期拒绝；证据入库 |
| 1.4 | 补丁 | 根据 1.1–1.3 收紧 router 文案（仍 ≤400 行） | PR 合 main；catalog 备注 eval 进度 |

**出口：** using-skills 达 `eval_partial` 以上；校验器场景 `pass`。

---

## W2 — Spec / Plan / Execute

| # | 项 | 动作 | Done-when |
|---|----|------|-----------|
| 2.1 | Requirements splitting | 两个可独立测的技能产出 + 共享 catalog | 两 capability ID、依赖方向、唯一集成 owner；无双计划 |
| 2.2 | Resume | 完成一任务→中断→仅凭 ledger 续跑 | 不重做已完成；对齐首个未完成产物 |
| 2.3 | 文案 | writing/executing-plans 按证据改「ledger / 恢复」段 | 合仓 |

**出口：** brainstorm-or-spec、writing-plans、executing-plans 至少各 1 条场景 `pass|partial`。

---

## W3 — 调度 / 验收 / 权限

| # | 项 | 动作 | Done-when |
|---|----|------|-----------|
| 3.1 | Dispatch isolation | 两不重叠内容任务；一 worker 无证据报 DONE | 调度拒收；有 task-pack 与报告文件 |
| 3.2 | Shared-write collision | 并发改同一 catalog | 检出冲突；串行集成；无静默覆盖 |
| 3.3 | Permission negative | 超权 send/publish/install/delete | 拦截；状态 `blocked|partial` 诚实 |
| 3.4 | DoD 修补 | verification-dod 按真实拒收理由改矩阵 | 合仓 |

**出口：** subagent-driven-dev、verification-dod 有可引用证据；权限负例不过则不得升 release。

---

## W4 — TDD / Anatomy

| # | 项 | 动作 | Done-when |
|---|----|------|-----------|
| 4.1 | Code RED/GREEN | 可丢弃 fixture + 真实测试命令 | 观察到 RED→最小 GREEN→回归记录 |
| 4.2 | Authoring baseline | 同任务有/无 skill-anatomy 对照（小样本） | 评分表；禁止单次样本宣称「统计提升」 |
| 4.3 | 补丁 | tdd / skill-anatomy 按空洞改写 | 合仓 |

---

## W5 — 装载与升格

| # | 项 | 动作 | Done-when |
|---|----|------|-----------|
| 5.1 | Loader portability | 按 Cursor / DC Bot 文档路径装载八包 | frontmatter 可发现；本地 references 可搬移 |
| 5.2 | Candidate→release | 按条审查证据；只升有证据者 | catalog `release` 仅含通过项；未过保留 candidate + limitations |
| 5.3 | 池务 | README / ATTRIBUTION / rejected 同步 | main 干净可交接 |

---

## 逐项构建顺序（执行队列）

按依赖，不并行乱序：

1. W0 脚手架  
2. W1.3 校验器（最快有硬证据）  
3. W1.1 → W1.2 → W1.4  
4. W2.1 → W2.2 → W2.3  
5. W3.1 → W3.2 → W3.3 → W3.4  
6. W4.1 → W4.2 → W4.3  
7. W5.1 → W5.2 → W5.3  

每完成一项：更新 `r6-eval/ledger.md` + 推仓。

---

## 不做（本计划外）

- 不镜像 Anthropic/Google/Microsoft 整仓  
- 不把 harness 安装层、telemetry、模型价目写进 skill  
- 不把静态 `validate_r5` 当作 runtime pass  
- 不升 release 而无场景证据  

---

## 即时开工

**本回合默认启动：W0 + W1.3 + W1.1**（脚手架、校验器负例、低仪式路由）。完成后推 PR 并合 main，再自动进 W1.2。
