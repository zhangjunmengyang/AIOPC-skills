<a id="top"></a>

<h1 align="center">
  <img src="assets/banner.png" alt="AIOPC Skills — 面向一人公司的 AI 技能、MCP 与工具索引" width="100%" />
</h1>

<p align="center">
  <a href="README.md">English</a> · <a href="#contents">完整目录</a> · <a href="#getting-started">开始使用</a> · <a href="#contributing">参与贡献</a>
</p>

面向独立开发者、咨询顾问、内容创作者和小型服务商的 AI 资源索引。覆盖找需求、做产品、获客、销售、交付和经营，精选条目与扩展目录都在本页展开，可直接用浏览器搜索。

**{{UNIQUE_URLS}} 个资源与参考链接 · 中英文同步。** 直接链接作者仓库、源码文件或官方文档。按完整 URL 去重；平台和专题会复用同一资源。机器可读版本：[catalog.json](catalog.json)。

<a id="contents"></a>
## 目录

[从当前任务开始](#start-here) · [安装与使用](#getting-started) · [入门组合](#starter-kit) · [收录与维护](#curation)

{{TOC}}

<a id="start-here"></a>
## 从当前任务开始

| 当前任务 | 本页入口 | 先做出什么 |
|---|---|---|
| 有想法，还没找到付费需求 | [创业起点](#startup) · [经营路线](#operator-playbook) | 明确客户、问题和一次可收费的小交付 |
| 想把服务做成产品 | [产品与研发](#product) · [设计](#design) | 可验收的范围与最小可交付版本 |
| 产品上线了，没人来 | [营销与增长](#marketing) · [平台目录](#platforms) | 一个渠道、一个内容或落地页实验 |
| 有咨询，成交和回款不稳定 | [销售与运营](#ops) · [经营路线](#operator-playbook) | 报价、范围、付款节点和交付验收约定 |
| 接单后忙不过来 | [经营路线](#operator-playbook) | 产能表、变更记录、交接说明和每单毛利 |
| 软件已经在服务真实客户 | [经营工具与指南](#operating-resources) | 付款事件处理、告警和一次恢复演练 |
| 做内容、课程或数字商品 | [内容生产](#content) · [平台目录](#platforms) | 一个可购买、可交付、能处理退款的商品 |
| 想降低对平台和个人在线时间的依赖 | [经营路线](#operator-playbook) · [经营工具](#operating-resources) | 可导出的客户与内容、离岗安排和交接清单 |

<a id="getting-started"></a>
## 安装与使用

| 类型 | 提供什么 | 怎么接入 |
|---|---|---|
| Skill | 任务指令，以及可选的脚本、模板和参考资料 | 交给支持该格式的 Agent，按原项目说明安装 |
| MCP | 外部系统的数据与操作接口 | 在支持 MCP 的客户端配置服务和相应权限 |
| 工具 / 官方指南 | 实际运行的服务、CLI 或操作文档 | 按项目文档部署、开通或照着执行 |

格式说明：[Agent Skills](https://agentskills.io/home) · [MCP 架构](https://modelcontextprotocol.io/docs/learn/architecture)。支持某种格式不代表具备同样的依赖、账号权限或运行环境。

例如，用 [Skills CLI](https://github.com/vercel-labs/skills) 安装一个文案技能：

```sh
npx skills add coreyhaines31/marketingskills --skill copywriting
```

CLI 当前要求 Node.js 22.20 或更高版本，安装时选择目标 Agent。MCP 服务与普通工具不使用这条命令。第一次只选当前任务需要的资源，用一个真实任务检查输出，再保留有效的组合。

<a id="starter-kit"></a>
## 入门组合

| 要做的事 | 资源 | 用途 |
|---|---|---|
| 打磨想法 | [idea-refine](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/idea-refine/SKILL.md) | 把想法写成可进一步验证的概念 |
| 定义客户任务 | [define-jtbd-canvas](https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/define-jtbd-canvas/SKILL.md) | 明确客户在什么情境下要完成什么 |
| 写产品需求 | [prd-development](https://github.com/deanpeters/Product-Manager-Skills/blob/HEAD/skills/prd-development/SKILL.md) | 梳理范围、用户需求与验收要求 |
| 做界面 | [frontend-design](https://github.com/anthropics/skills/blob/HEAD/skills/frontend-design/SKILL.md) | 设计并实现前端界面 |
| 写销售页面 | [copywriting](https://github.com/coreyhaines31/marketingskills/blob/HEAD/skills/copywriting/SKILL.md) | 组织卖点、证据与行动入口 |
| 检查搜索表现 | [seo-audit](https://github.com/coreyhaines31/marketingskills/blob/HEAD/skills/seo-audit/SKILL.md) | 检查站点的搜索可见性问题 |
| 创始人销售 | [founder-sales](https://github.com/refoundai/lenny-skills/blob/HEAD/skills/founder-sales/SKILL.md) | 梳理直接接触客户和推进销售的做法 |
| 用户上手与维护 | [retention](https://github.com/whawkinsiv/solo-founder-skills/blob/HEAD/skills/retention/SKILL.md) | 安排首次使用、欢迎邮件、回访与取消流程 |
| 定价 | [pricing](https://github.com/coreyhaines31/marketingskills/blob/HEAD/skills/pricing/SKILL.md) | 讨论定价、包装和收入方式 |
| 算清单笔生意 | [unit-economics](https://github.com/anthropics/financial-services/blob/HEAD/plugins/vertical-plugins/private-equity/skills/unit-economics/SKILL.md) | 检查单位收入与成本假设 |
| 浏览器操作 | [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 让支持 MCP 的 Agent 操作网页并检查界面 |
| 备份恢复 | [restic 恢复指南](https://restic.readthedocs.io/en/stable/050_restore.html) | 将备份恢复到目标目录并核对结果 |

{{CATALOG}}

<a id="curation"></a>
## 收录与维护

- 按具体任务整理，保留原始链接和简短用途；完整内容、依赖与许可证以原项目为准。
- 优先链接具体源码文件；标注「仓库入口」的条目尚未定位到对应文件，请在作者仓库确认当前内容。合集名称直接链接仓库。链接核对记录见 [upstream-links.json](data/upstream-links.json)。
- 精选专题提供用途说明，扩展目录按来源技能包归组；包内某项技能可能跨领域，分组不等于逐条用途判断。
- 页面可访问、上游内容存在、安装成功、真实任务有效是不同检查。新增经营指南已核对第一方用途说明；本仓库未对全部资源完成安装与任务实测，也不将旧页面的 200 响应当作现行安装保证。
- README 和机器目录由源文档生成。持续检查资源是否全部展开、两种语言的外链是否一致、本地链接与锚点是否有效，以及页面是否超过 GitHub 的展示限制。
- 更新记录见 [CHANGELOG](CHANGELOG.md)，内容归属见 [NOTICE](NOTICE.md)。

<a id="contributing"></a>
<a id="贡献"></a>
## 贡献

欢迎补充缺失任务、修正用途、替换失效资源。提交「原始来源＋具体用途＋检查到哪一步」，同步中英文后生成目录；操作方法见 [CONTRIBUTING](CONTRIBUTING.md)。

[回到顶部](#top) · [English](README.md)
