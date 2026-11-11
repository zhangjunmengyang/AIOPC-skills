[← 返回总览](../../README.zh.md) · [English](../en/03-product.md)

# 🛠️ 三、产品与研发

从需求到上线，按工程阶段拆。

---

## ⭐ 先试这几个

**[bmad-prd · 仓库入口](https://github.com/bmad-code-org/BMAD-METHOD)**

- *为什么:* 多角色把需求拆成可执行 PRD。
- *第一次怎么用:* 拿一个真实需求跑一遍，输出 PRD 和验收标准。

**[spec-driven-development](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/spec-driven-development/SKILL.md)**

- *为什么:* 先写规格再写代码，减少返工。
- *第一次怎么用:* 选一个小功能，先写 1 页规格再让 AI 实现。

**[test-driven-development](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/test-driven-development/SKILL.md)**

- *为什么:* 先写失败测试，防止 AI 写歪。
- *第一次怎么用:* 给一个核心函数补 3 个测试，再改实现。

**[code-review-and-quality](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/code-review-and-quality/SKILL.md)**

- *为什么:* 多维度审查，不只看语法。
- *第一次怎么用:* 让 AI 审一个真实 PR，按严重级别列问题。

---

## 全部技能

[需求 / PRD](#s1) · [架构](#s2) · [测试](#s3) · [审查 / 安全](#s4) · [部署 / CI](#s5) · [调试 / 性能](#s6) · [文档 / 上下文](#s7) · [发布 / 设计协作](#s8) · [代码命名](#s9)

<a id="s1"></a>
### 需求 / PRD

- **[bmad-prd · 仓库入口](https://github.com/bmad-code-org/BMAD-METHOD)** — 多角色 PRD 工作流。
- **[bmad-spec · 仓库入口](https://github.com/bmad-code-org/BMAD-METHOD)** — 规格内核。
- **[prd-development](https://github.com/deanpeters/Product-Manager-Skills/blob/HEAD/skills/prd-development/SKILL.md)** — 结构化 PRD 流程。
- **[spec-driven-development](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/spec-driven-development/SKILL.md)** — 先写规格再写代码。
- **[deliver-prd](https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/deliver-prd/SKILL.md)** — PRD。
- **[deliver-user-stories](https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/deliver-user-stories/SKILL.md)** — 用户故事。
- **[deliver-acceptance-criteria](https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/deliver-acceptance-criteria/SKILL.md)** — 验收标准。

<a id="s2"></a>
### 架构

- **[bmad-architecture](https://github.com/bmad-code-org/BMAD-METHOD/blob/HEAD/skills/bmad-architecture/SKILL.md)** — 架构 spine。
- **[architecture-blueprint-generator](https://github.com/github/awesome-copilot/blob/HEAD/skills/architecture-blueprint-generator/SKILL.md)** — 项目架构蓝图。
- **[system-design](https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/engineering/skills/system-design/SKILL.md)** — 系统设计与架构决策。
- **[api-design](https://github.com/affaan-m/ECC/blob/HEAD/skills/api-design/SKILL.md)** — API 设计约定。
- **[documenting-contracts](https://github.com/riekelt/technical-writer/blob/HEAD/plugins/technical-writer/skills/documenting-contracts/SKILL.md)** — 记录 REST/RPC、Webhook、CLI 与文件格式的接口契约。
- **[bmad-agent-architect](https://github.com/bmad-code-org/BMAD-METHOD/blob/HEAD/skills/bmad-agent-architect/SKILL.md)** — 架构师角色。
- **[bmad-agent-dev](https://github.com/bmad-code-org/BMAD-METHOD/blob/HEAD/skills/bmad-agent-dev/SKILL.md)** — 开发角色。

<a id="s3"></a>
### 测试

- **[webapp-testing](https://github.com/anthropics/skills/blob/HEAD/skills/webapp-testing/SKILL.md)** — Web 应用测试。
- **[test-driven-development](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/test-driven-development/SKILL.md)** — 先写失败测试。
- **[browser-testing-with-devtools](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/browser-testing-with-devtools/SKILL.md)** — 用 DevTools 做浏览器测试。
- **[vitest](https://github.com/antfu/skills/blob/HEAD/skills/vitest/SKILL.md)** — Vite 原生测试框架。
- **[testing-strategy](https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/engineering/skills/testing-strategy/SKILL.md)** — 设计测试策略与覆盖。
- **[web-quality-audit](https://github.com/addyosmani/web-quality-skills/blob/HEAD/skills/web-quality-audit/SKILL.md)** — 浏览器实测 + 质量审计。
- **[bmad-qa-generate-e2e-tests](https://github.com/bmad-code-org/BMAD-METHOD/blob/HEAD/skills/bmad-qa-generate-e2e-tests/SKILL.md)** — 生成 E2E。
- **[deliver-edge-cases](https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/deliver-edge-cases/SKILL.md)** — 边界情况。

<a id="s4"></a>
### 审查 / 安全

- **[code-review-and-quality](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/code-review-and-quality/SKILL.md)** — 多维度代码审查。
- **[security-and-hardening](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/security-and-hardening/SKILL.md)** — 安全优先的开发。
- **[security-audit](https://github.com/cloudflare/security-audit-skill/blob/HEAD/skills/security-audit/SKILL.md)** — 找真实信任边界漏洞。
- **[bmad-code-review](https://github.com/bmad-code-org/BMAD-METHOD/blob/HEAD/skills/bmad-code-review/SKILL.md)** — BMad 代码审查流程。
- **[ponytail-audit](https://github.com/DietrichGebert/ponytail/blob/HEAD/skills/ponytail-audit/SKILL.md)** — 像接手项目的资深工程师一样审全仓。
- **[bmad-review](https://github.com/bmad-code-org/BMAD-METHOD/blob/HEAD/skills/bmad-review/SKILL.md)** — 代码评审。

<a id="s5"></a>
### 部署 / CI

- **[ci-cd-and-automation](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/ci-cd-and-automation/SKILL.md)** — CI/CD 质量门禁。
- **[deploy-checklist](https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/engineering/skills/deploy-checklist/SKILL.md)** — 部署前检查。
- **[docker-patterns](https://github.com/affaan-m/ECC/blob/HEAD/skills/docker-patterns/SKILL.md)** — Docker/Compose 生产实践。
- **[aws-deployment](https://github.com/aws/agent-toolkit-for-aws/blob/HEAD/skills/core-skills/aws-deployment/SKILL.md)** — AWS CI/CD 部署。

<a id="s6"></a>
### 调试 / 性能

- **[debugging-and-error-recovery](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/debugging-and-error-recovery/SKILL.md)** — 系统化调试。
- **[performance-optimization](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/performance-optimization/SKILL.md)** — 先测量再优化。
- **[debug](https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/engineering/skills/debug/SKILL.md)** — 结构化调试流程。
- **[debug-optimize-lcp](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/HEAD/skills/debug-optimize-lcp/SKILL.md)** — 定位并优化 LCP。

<a id="s7"></a>
### 文档 / 上下文

- **[documentation-and-adrs](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/documentation-and-adrs/SKILL.md)** — 文档与 ADR。
- **[documentation](https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/engineering/skills/documentation/SKILL.md)** — 文档写作。
- **[tech-debt](https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/engineering/skills/tech-debt/SKILL.md)** — 技术债。
- **[incident-response](https://github.com/anthropics/knowledge-work-plugins/blob/HEAD/engineering/skills/incident-response/SKILL.md)** — 事故响应。
- **[context-engineering](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/context-engineering/SKILL.md)** — 上下文工程。
- **[incremental-implementation](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/incremental-implementation/SKILL.md)** — 增量实现。
- **[source-driven-development](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/source-driven-development/SKILL.md)** — 源码驱动。
- **[interview-me](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/interview-me/SKILL.md)** — 需求访谈。
- **[doubt-driven-development](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/doubt-driven-development/SKILL.md)** — 怀疑驱动。
- **[constraint-driven-development](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/constraint-driven-development/SKILL.md)** — 约束驱动。
- **[observability-and-instrumentation](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/observability-and-instrumentation/SKILL.md)** — 可观测与埋点。
- **[measure-instrumentation-spec](https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/measure-instrumentation-spec/SKILL.md)** — 埋点规格。

<a id="s8"></a>
### 发布 / 设计协作

- **[develop-design-rationale](https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/develop-design-rationale/SKILL.md)** — 设计理由。
- **[deliver-release-notes](https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/deliver-release-notes/SKILL.md)** — 发布说明。


<a id="s9"></a>
### 代码命名

- **[naming-analyzer](https://github.com/softaworks/agent-toolkit/blob/HEAD/skills/naming-analyzer/SKILL.md)** — 按上下文和约定改进变量、函数、类、文件及 API 名称。

> 索引页：摘要为整理，版权归原作者；完整内容请回原链接。

---

[← 返回总览](../../README.zh.md)
