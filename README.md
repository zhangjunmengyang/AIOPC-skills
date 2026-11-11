# AIOPC Skills

> 给 AI 用的技能、MCP 与工具索引。按「要干的活」分类，不按厂商分类。

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#贡献)
[![Last Updated](https://img.shields.io/badge/updated-2026--11--11-blue.svg)](#)

一人公司 / 超级个体的 AI 工具箱。这里收集能直接装进 Claude Code、Cursor、n8n 等工具里的 **Skills**、**MCP servers** 和开源项目。

每条只保留「名称 + 一句话 + 链接」，不写长评测。**先收藏超级大全，再按当前任务拿一个，跑通后再加第二个。**

链接核验于 **2026-11-11**；star 数不写，避免过时。欢迎 PR，格式见[文末](#贡献)。

---

## 目录

- [🧭 先收藏：超级大全](#-先收藏超级大全)
- [🧩 Skills：按任务找](#-skills按任务找)
  - [产品与研发](#产品与研发)
  - [营销与获客](#营销与获客)
  - [内容与设计](#内容与设计)
  - [数据与研究](#数据与研究)
  - [销售、客服与运营](#销售客服与运营)
  - [OPC / 一人公司专用](#opc--一人公司专用)
- [🔌 MCP：按接入对象找](#-mcp按接入对象找)
  - [大全与注册表](#大全与注册表)
  - [文件、代码、终端](#文件代码终端)
  - [浏览器与网页](#浏览器与网页)
  - [数据库与数据](#数据库与数据)
  - [协作与办公](#协作与办公)
  - [客户端与开发框架](#客户端与开发框架)
- [⚙️ 自动化与工作流](#️-自动化与工作流)
- [🤖 Agent 框架与编程 Agent](#-agent-框架与编程-agent)
- [📚 知识库 / RAG](#-知识库--rag)
- [🧪 评测、可观测与安全](#-评测可观测与安全)
- [🎓 学习 / 课程 / Cookbook](#-学习--课程--cookbook)
- [🇨🇳 中文资源与工具导航](#-中文资源与工具导航)
- [🎯 选型原则](#-选型原则)
- [🤝 贡献](#贡献)

**类型标记：** `Skill` 可装进 Claude Code / Cursor 等 · `MCP` Model Context Protocol server · `Tool` 独立工具 / 平台 · `List` 合集 · `Framework` 开发框架 · `Course` 课程。

---

## 🧭 先收藏：超级大全

- **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** `List` — MCP 服务器总目录，按用途分几十类。
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** `List` — 官方参考 server：文件、fetch、git、memory、sqlite。
- **[anthropics/skills](https://github.com/anthropics/skills)** `List` — 官方 Agent Skills 仓库，格式与示例。
- **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** `List` — 目前最大的 Claude 技能清单之一。
- **[agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** `List` — 近 3000 个技能的总目录，适合按关键词搜。
- **[awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** `List` — 官方与社区技能合集，偏工程。
- **[skills.sh](https://skills.sh)** `List` — 技能目录与安装排行。
- **[awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** `List` — Claude Code 的 commands、hooks、skills、工具大全。
- **[superpowers](https://github.com/obra/superpowers)** `Skill` — 一套很火的 Claude Code 技能框架。
- **[awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)** `List` — 上百个专业子代理，按角色分。
- **[awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)** `List` — AI Agent 项目大全。
- **[awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)** `List` — 100+ 可运行的 Agent / RAG 应用示例。
- **[Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM)** `List` — 大模型论文、模型、工具总览。
- **[awesome-rag](https://github.com/awesome-rag/awesome-rag)** `List` — RAG 论文、框架、评测合集。
- **[awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)** `List` — 最大的通用提示词库。
- **[awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)** `List` — Cursor 规则大全。
- **[superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)** `List` — superpowers 中文版。
- **[AI-Coding-Guide-Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh)** `List` — 中文 AI 编程教程与资源合集。

> 大全只用来「搜关键词」，不要从头读到尾。找到一个能解决当前任务的仓库，立刻拿真实材料试一次。

---

## 🧩 Skills：按任务找

> 每条是「一个具体任务 → 一个能直接用的 Skill / 仓库」。先挑最接近的一行；没有完全匹配的，去上面的超级大全搜关键词。

### 产品与研发

- **[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)** `Skill` — 多角色需求拆解与 PRD。
- **[GitHub Spec Kit](https://github.com/github/spec-kit)** `Skill` — 规格驱动开发。
- **[DeepWiki](https://github.com/AsyncFuncAI/deepwiki-open)** `Tool` — 自动生成仓库文档，快速读懂代码库。
- **[PR-Agent](https://github.com/qodo-ai/pr-agent)** `Tool` — 自动审 PR、给修改建议。
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** `MCP` — 浏览器自动化与测试。
- **[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)** `MCP` — 调试真实浏览器、看网络与性能。
- **[Context7](https://github.com/upstash/context7)** `MCP` — 给 AI 注入最新库文档，减少过时 API。
- **[Next.js SaaS Starter](https://github.com/nextjs/saas-starter)** `Tool` — 全栈 SaaS 起步模板。
- **[Open SaaS](https://github.com/wasp-lang/open-saas)** `Tool` — 开源 SaaS 模板。
- **[Superdesign](https://github.com/superdesigndev/superdesign)** `Tool` — AI 设计画布，适合做页面与组件。
- **[Coolify](https://github.com/coollabsio/coolify)** `Tool` — 自托管 PaaS，部署自己的服务。
- **[Dokploy](https://github.com/Dokploy/dokploy)** `Tool` — 轻量 PaaS，Heroku 替代。

### 营销与获客

#### GEO / AI 搜索优化

- **[llms.txt](https://llmstxt.org/)** `Tool` — 给 AI 爬虫的站点索引。
- **[GEO 原始论文](https://arxiv.org/abs/2311.09735)** `List` — 生成式引擎优化（KDD 2024）的方法与实验。
- **[Google AI Features](https://developers.google.com/search/docs/appearance/ai-features)** `Tool` — AI 搜索/摘要的抓取与展示规则。
- **[Profound](https://www.tryprofound.com/)** `Tool` — AI 搜索可见度监测。
- **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** `Skill` — 搜 `geo` / `seo`，拿现成技能。

#### SEO

- **[Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)** `Tool` — 官方入门，先把基础做对。
- **[Unlighthouse](https://github.com/harlan-zw/unlighthouse)** `Tool` — 全站跑 Lighthouse，找性能与 SEO 问题。
- **[Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)** `Tool` — 把性能检查放进 CI。
- **[Screaming Frog](https://www.screamingfrog.co.uk/seo-spider/)** `Tool` — 爬站审计标题、描述、链接与错误。
- **[Google Search Console](https://search.google.com/search-console/about)** `Tool` — 收录、曝光、关键词数据。
- **[Ahrefs: Programmatic SEO](https://ahrefs.com/blog/programmatic-seo/)** `List` — 模板 × 数据 × 独特价值。

#### 落地页 / 营销页

- **[Danny Postma: Landing Page Pipeline](https://www.dannypostma.com/landing-page)** `List` — 研究 → 文案 → 设计 → 上线。
- **[Julian Shapiro: Landing Page Copywriting](https://www.julian.com/guide/startup/landing-pages)** `List` — 首屏结构与文案长文。
- **[Marketing Examples](https://marketingexamples.com/)** `List` — 真实落地页与表达案例。
- **[Framer](https://www.framer.com/)** `Tool` — 快速搭营销页。
- **[Carrd](https://carrd.co/)** `Tool` — 极简单页。

#### 文案 / 品牌语气

- **[Copyhackers: Review Mining](https://copyhackers.com/write-copy-amazon-review-mining/)** `List` — 从评论里挖客户原话。
- **[Mailchimp: Voice & Tone](https://styleguide.mailchimp.com/voice-and-tone/)** `List` — 品牌语气与场景化表达。
- **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** `Skill` — 搜 `copywriting`。
- **[agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** `Skill` — 搜 `editing`。

#### 社媒 / 邮件 / 广告 / PR

- **[Postiz](https://github.com/gitroomhq/postiz-app)** `Tool` — 开源社媒排期与多平台发布。
- **[Mixpost](https://github.com/inovector/mixpost)** `Tool` — 自托管社媒管理。
- **[React Email](https://github.com/resend/react-email)** `Tool` — 用 React 写邮件模板。
- **[Resend](https://github.com/resend/resend-node)** `Tool` — 发邮件 API。
- **[Listmonk](https://github.com/knadh/listmonk)** `Tool` — 开源自托管 newsletter。
- **[Mautic](https://github.com/mautic/mautic)** `Tool` — 开源邮件自动化。
- **[Really Good Emails](https://www.reallygoodemails.com/)** `List` — 按生命周期找邮件样本。
- **[Google Skillshop](https://skillshop.withgoogle.com/)** `Course` — Google Ads 官方免费课程。
- **[Meta Blueprint](https://www.facebook.com/business/learn)** `Course` — Meta 广告官方课程。
- **[Featured News 标准](https://news.featured.com/standards)** `List` — 媒体采纳专家观点的标准。

### 内容与设计

- **[ComfyUI](https://github.com/comfyanonymous/ComfyUI)** `Tool` — 节点式图片生成/编辑工作流。
- **[Remotion](https://github.com/remotion-dev/remotion)** `Tool` — 用 React 做视频。
- **[OpenCut](https://github.com/OpenCut-app/OpenCut)** `Tool` — 开源剪映替代。
- **[WhisperX](https://github.com/m-bain/whisperX)** `Tool` — 转写、对齐与说话人分离。
- **[Slidev](https://github.com/slidevjs/slidev)** `Tool` — Markdown 做幻灯片。
- **[Marp](https://github.com/marp-team/marp)** `Tool` — Markdown 转 PPT。
- **[PptxGenJS](https://github.com/gitbrent/PptxGenJS)** `Tool` — 代码生成 PPTX。
- **[Lucide](https://github.com/lucide-icons/lucide)** `Tool` — 开源图标集。
- **[awesome-design-systems](https://github.com/alexpate/awesome-design-systems)** `List` — 设计系统参考。
- **[agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** `Skill` — 搜 `design` / `ui`。

### 数据与研究

- **[Exa](https://github.com/exa-labs/exa-py)** `Tool` — 语义搜索 API。
- **[Tavily](https://github.com/tavily-ai/tavily-python)** `Tool` — 为 Agent 设计的搜索 API。
- **[SearXNG](https://github.com/searxng/searxng)** `Tool` — 开源元搜索引擎。
- **[Firecrawl](https://github.com/firecrawl/firecrawl)** `Tool` — 网页抓取、爬站、深度研究。
- **[Crawl4AI](https://github.com/unclecode/crawl4ai)** `Tool` — 开源 LLM 爬虫。
- **[Jina Reader](https://github.com/jina-ai/reader)** `Tool` — 网页转 Markdown。
- **[Crawlee](https://github.com/apify/crawlee)** `Tool` — 爬虫框架。
- **[changedetection.io](https://github.com/dgtlmoon/changedetection.io)** `Tool` — 竞品/页面变化监控。
- **[Serper](https://serper.dev)** `Tool` — Google 搜索 API。
- **[DuckDB](https://github.com/duckdb/duckdb)** `Tool` — 本地分析型数据库。
- **[PandasAI](https://github.com/Sinaptik-AI/pandas-ai)** `Tool` — 用自然语言分析表格。
- **[NocoDB](https://github.com/nocodb/nocodb)** `Tool` — Airtable 开源替代。
- **[Teable](https://github.com/teableio/teable)** `Tool` — 多维表格/数据库。
- **[awesome-web-scraping](https://github.com/lorien/awesome-web-scraping)** `List` — 抓取资源大全。

### 销售、客服与运营

- **[Twenty](https://github.com/twentyhq/twenty)** `Tool` — 开源 CRM。
- **[Chatwoot](https://github.com/chatwoot/chatwoot)** `Tool` — 开源客服/工单。
- **[Invoice Ninja](https://github.com/invoiceninja/invoiceninja)** `Tool` — 开源发票与账单。
- **[DocuSeal](https://github.com/docusealco/docuseal)** `Tool` — 开源电子签。
- **[Documenso](https://github.com/documenso/documenso)** `Tool` — 开源 DocuSign 替代。
- **[Plane](https://github.com/makeplane/plane)** `Tool` — 开源项目管理。
- **[Cal.com](https://github.com/calcom/cal.com)** `Tool` — 开源预约/日程。
- **[Outline](https://github.com/outline/outline)** `Tool` — 团队知识库。
- **[Docmost](https://github.com/docmost/docmost)** `Tool` — 开源文档协作。

### OPC / 一人公司专用

- **[Easy Chen 一人企业方法论](https://github.com/easychen/opc-methodology)** `Skill` — 赛道、资产池、画布与 9 个业务 Skill。
- **[iamtouchskyer/opc](https://github.com/iamtouchskyer/opc)** `Skill` — 21 个角色、6 种流程、脚本化 gate 的评审流水线。
- **[validate-opc-project](https://github.com/luqi67677/validate-opc-project)** `Skill` — 五角色审查 + 正反证 + 停止线。
- **[opcspace/opcstartup-skill](https://github.com/opcspace/opcstartup-skill)** `Skill` — 0-6 阶段、百日计划、12 个模板。
- **[slavingia/skills](https://github.com/slavingia/skills)** `Skill` — 《极简创业》的 9 步技能库。

---

## 🔌 MCP：按接入对象找

> MCP 是给 AI 接工具的通用接口。先装 1 个文件 / 浏览器 / 数据库 server，跑通一个真实任务，再加第二个。

### 大全与注册表

- **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** `List` — 最大的 MCP 服务器合集。
- **[官方参考 servers](https://github.com/modelcontextprotocol/servers)** `List` — 文件、fetch、git、memory、sqlite 官方实现。
- **[MCP 官方文档](https://modelcontextprotocol.io)** `List` — 协议规范与接入指南。
- **[官方 Registry](https://registry.modelcontextprotocol.io)** `List` — 官方服务器注册与发现。
- **[Glama](https://glama.ai/mcp/servers)** `List` — 超大规模 MCP 注册表。
- **[PulseMCP](https://www.pulsemcp.com)** `List` — 每日更新的全量目录。
- **[mcp.so](https://mcp.so)** `List` — 老牌 MCP 目录站。
- **[Smithery](https://smithery.ai)** `List` — 一键安装托管 MCP，现已并入 Arcade。
- **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** `List` — 中文 MCP 资源精选。
- **[MCP 中文入门](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** `Course` — 从 0 搭第一个 MCP server。

### 文件、代码、终端

- **[Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** `MCP` — 受控读写本地文件。
- **[Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** `MCP` — 读取、搜索、操作 Git 仓库。
- **[GitHub](https://github.com/github/github-mcp-server)** `MCP` — Issue、PR、代码搜索、Actions。
- **[Serena](https://github.com/oraios/serena)** `MCP` — 语义检索与代码编辑，适合大仓库。
- **[Desktop Commander](https://github.com/wonderwhy-er/DesktopCommanderMCP)** `MCP` — 终端命令与文件编辑控制。
- **[Context7](https://github.com/upstash/context7)** `MCP` — 注入最新库文档。
- **[Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** `MCP` — 分步反思式推理。

### 浏览器与网页

- **[Playwright](https://github.com/microsoft/playwright-mcp)** `MCP` — 浏览器自动化、点击、截图、跑测试。
- **[Chrome DevTools](https://github.com/ChromeDevTools/chrome-devtools-mcp)** `MCP` — 调试真实浏览器。
- **[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** `MCP` — 抓网页转 Markdown。
- **[Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server)** `MCP` — 网页抓取、爬站、深度研究。
- **[Browserbase](https://github.com/browserbase/mcp-server-browserbase)** `MCP` — 云端浏览器，适合大规模/反爬场景。

### 数据库与数据

- **[Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp)** `MCP` — Postgres 读写、索引与调优建议。
- **[DBHub](https://github.com/bytebase/dbhub)** `MCP` — 通用数据库网关，支持 SQLite/MySQL/Postgres。
- **[Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** `MCP` — 知识图谱式持久记忆。
- **[AntV Chart](https://github.com/antvis/mcp-server-chart)** `MCP` — 25+ 种图表生成。

### 协作与办公

- **[Slack](https://github.com/korotovsky/slack-mcp-server)** `MCP` — 读频道、搜消息、发消息。
- **[Notion](https://github.com/makenotion/notion-mcp-server)** `MCP` — 读写页面、数据库、评论。
- **[Figma](https://github.com/GLips/Figma-Context-MCP)** `MCP` — 把 Figma 布局、组件和样式给 AI。
- **[飞书 OpenAPI](https://github.com/larksuite/lark-openapi-mcp)** `MCP` — 飞书文档/表格/消息接入。

### 客户端与开发框架

- **[Python SDK](https://github.com/modelcontextprotocol/python-sdk)** `Framework` — 官方 Python 开发包。
- **[TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)** `Framework` — 官方 TypeScript 开发包。
- **[FastMCP](https://github.com/PrefectHQ/fastmcp)** `Framework` — Python 快速构建 MCP server。
- **[mcp-use](https://github.com/mcp-use/mcp-use)** `Framework` — 全栈 MCP 应用框架。
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)** `Tool` — 调试、测试 MCP server。
- **[Cherry Studio](https://github.com/CherryHQ/cherry-studio)** `Tool` — 支持 MCP 的桌面客户端。

---

## ⚙️ 自动化与工作流

> 先把一个重复流程手工跑通，再考虑自动化；不要用工具掩盖一个本来就不该做的流程。

- **[n8n](https://github.com/n8n-io/n8n)** `Tool` — 开源可视化工作流，可自托管、接 MCP。
- **[n8n-workflows](https://github.com/Zie619/n8n-workflows)** `List` — 几千个现成 n8n 工作流模板。
- **[awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates)** `List` — 按场景分类的 n8n 模板合集。
- **[n8n 官方模板](https://n8n.io/workflows/)** `List` — 官方工作流模板社区。
- **[Make 模板](https://www.make.com/en/templates)** `List` — 3500+ 应用集成模板。
- **[Zapier 模板](https://zapier.com/templates)** `List` — 海量集成工作流模板。
- **[Activepieces](https://github.com/activepieces/activepieces)** `Tool` — 开源 Zapier 替代。
- **[Windmill](https://github.com/windmill-labs/windmill)** `Tool` — 代码优先的工作流/脚本平台。
- **[Dify](https://github.com/langgenius/dify)** `Tool` — 可视化 LLM 应用与工作流。
- **[Coze Studio](https://github.com/coze-dev/coze-studio)** `Tool` — 字节开源的低代码 Bot/Agent 平台。
- **[Flowise](https://github.com/FlowiseAI/Flowise)** `Tool` — 拖拽式 LLM 流程与 Agent。
- **[Langflow](https://github.com/langflow-ai/langflow)** `Tool` — 可视化 LangChain 流程编排。
- **[Botpress](https://github.com/botpress/botpress)** `Tool` — 对话式 Bot 平台。

---

## 🤖 Agent 框架与编程 Agent

> 先用现成的编程 Agent，再考虑自己搭框架；大多数人不需要从零写 Agent。

### 通用框架

- **[LangGraph](https://github.com/langchain-ai/langgraph)** `Framework` — 状态图编排可恢复、可人工介入的 Agent。
- **[CrewAI](https://github.com/crewAIInc/crewAI)** `Framework` — 角色扮演式多智能体协作。
- **[AutoGen](https://github.com/microsoft/autogen)** `Framework` — 微软多智能体对话与编程框架。
- **[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)** `Framework` — 轻量多智能体工作流。
- **[Google ADK](https://github.com/google/adk-python)** `Framework` — 谷歌代码优先 Agent 工具包。
- **[Mastra](https://github.com/mastra-ai/mastra)** `Framework` — TypeScript 优先的 Agent 框架。
- **[Pydantic AI](https://github.com/pydantic/pydantic-ai)** `Framework` — 类型安全的 Python Agent。
- **[Agno](https://github.com/agno-agi/agno)** `Framework` — 高性能全栈 Agent 平台。
- **[Vercel AI SDK](https://github.com/vercel/ai)** `Framework` — 前端友好的 AI 工具包。
- **[LangChain](https://github.com/langchain-ai/langchain)** `Framework` — 最主流的 LLM 应用框架。
- **[Semantic Kernel](https://github.com/microsoft/semantic-kernel)** `Framework` — 微软企业级 LLM 集成。

### 编程 Agent / IDE

- **[Claude Code](https://github.com/anthropics/claude-code)** `Tool` — 终端 Agent，读代码、改代码、跑命令。
- **[Codex CLI](https://github.com/openai/codex)** `Tool` — OpenAI 终端编码 Agent。
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** `Tool` — 谷歌终端 Agent。
- **[OpenHands](https://github.com/All-Hands-AI/OpenHands)** `Tool` — 开源 AI 软件开发智能体，可自托管。
- **[Cline](https://github.com/cline/cline)** `Tool` — IDE 内自主编码 Agent。
- **[Roo Code](https://github.com/RooCodeInc/Roo-Code)** `Tool` — 多角色/多模式开发团队。
- **[Aider](https://github.com/Aider-AI/aider)** `Tool` — 终端 AI 结对编程，git 集成好。
- **[Continue](https://github.com/continuedev/continue)** `Tool` — 可定制的开源编码助手。
- **[SWE-agent](https://github.com/SWE-agent/SWE-agent)** `Tool` — 自动修复 GitHub Issue。
- **[Goose](https://github.com/block/goose)** `Tool` — 可扩展本地自动化 Agent。

### 浏览器 / 电脑操作

- **[browser-use](https://github.com/browser-use/browser-use)** `Tool` — 让 AI 直接操作浏览器。
- **[Stagehand](https://github.com/browserbase/stagehand)** `Tool` — 自然语言驱动网页自动化。
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** `MCP` — 用 MCP 控制 Playwright。
- **[Skyvern](https://github.com/Skyvern-AI/skyvern)** `Tool` — 视觉驱动浏览器工作流。
- **[E2B](https://github.com/e2b-dev/E2B)** `Tool` — Agent 安全沙箱。
- **[Anthropic Quickstarts](https://github.com/anthropics/anthropic-quickstarts)** `Tool` — Claude 控制桌面/电脑示例。

---

## 📚 知识库 / RAG

- **[RAGFlow](https://github.com/infiniflow/ragflow)** `Tool` — 深度文档理解 RAG 引擎，适合中文文档。
- **[Dify](https://github.com/langgenius/dify)** `Tool` — 可视化 LLM 应用/知识库平台。
- **[FastGPT](https://github.com/labring/FastGPT)** `Tool` — 知识库问答与工作流编排。
- **[LlamaIndex](https://github.com/run-llama/llama_index)** `Framework` — 文档处理与 RAG 框架。
- **[LightRAG](https://github.com/HKUDS/LightRAG)** `Framework` — 轻量图增强检索。
- **[GraphRAG](https://github.com/microsoft/graphrag)** `Framework` — 微软图结构 RAG。
- **[Milvus](https://github.com/milvus-io/milvus)** `Tool` — 云原生向量数据库。
- **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)** `Tool` — 开箱即用的本地知识库/桌面 Agent。
- **[Khoj](https://github.com/khoj-ai/khoj)** `Tool` — 可自托管的个人 AI 第二大脑。
- **[Haystack](https://github.com/deepset-ai/haystack)** `Framework` — 生产级 RAG/搜索框架。

---

## 🧪 评测、可观测与安全

- **[Promptfoo](https://github.com/promptfoo/promptfoo)** `Tool` — 比较提示词/模型输出，可做红队。
- **[Langfuse](https://github.com/langfuse/langfuse)** `Tool` — 开源 LLM 可观测、评测与提示管理。
- **[DeepEval](https://github.com/confident-ai/deepeval)** `Tool` — 像写单测一样评测 LLM 输出。
- **[Braintrust](https://github.com/braintrustdata/braintrust-sdk)** `Tool` — 评测、数据集、实验追踪。
- **[Helicone](https://github.com/Helicone/helicone)** `Tool` — LLM 请求日志、成本与延迟监控。
- **[OpenAI Evals](https://github.com/openai/evals)** `Tool` — 官方评测框架与样例。
- **[Arize Phoenix](https://github.com/Arize-ai/phoenix)** `Tool` — 开源 LLM 追踪、评测与可视化。

---

## 🎓 学习 / 课程 / Cookbook

- **[ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)** `Course` — 微软 18 课 Agent 入门，带代码。
- **[generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** `Course` — 微软 21 课生成式 AI 入门。
- **[OpenAI Cookbook](https://github.com/openai/openai-cookbook)** `Course` — OpenAI API 官方示例与配方。
- **[Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)** `Course` — Claude 用法、工具调用、RAG 示例。
- **[HF Agents Course](https://github.com/huggingface/agents-course)** `Course` — HuggingFace 智能体课程。
- **[LangChain Academy](https://github.com/langchain-ai/langchain-academy)** `Course` — LangGraph 官方课程。
- **[Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** `Course` — 提示工程权威指南。
- **[Anthropic 提示词教程](https://github.com/anthropics/prompt-eng-interactive-tutorial)** `Course` — 官方互动式提示词教程。

---

## 🇨🇳 中文资源与工具导航

### 中文资源

- **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** `List` — 中文 MCP 服务器与教程精选。
- **[MCP 中文入门](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** `Course` — 从 0 搭第一个 MCP server。
- **[superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)** `List` — superpowers 技能框架中文版。
- **[AI-Coding-Guide-Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh)** `List` — 中文 AI 编程教程与工具合集。
- **[claude-howto-zh-cn](https://github.com/lhfer/claude-howto-zh-cn)** `List` — Claude Code 中文指南。
- **[everything-claude-code-zh](https://github.com/xu-xiang/everything-claude-code-zh)** `List` — Claude Code 生态中文翻译。
- **[飞书 OpenAPI MCP](https://github.com/larksuite/lark-openapi-mcp)** `MCP` — 飞书文档/表格/消息接入。
- **[ModelScope MCP 广场](https://modelscope.cn/mcp)** `List` — 魔搭中文 MCP 市场。
- **[awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)** `List` — 中文 Agent 学习地图。
- **[Awesome-Chinese-LLM](https://github.com/AiHubCN/Awesome-Chinese-LLM)** `List` — 中文大模型资源大全。
- **[中文提示词大全](https://github.com/L1Xu4n/Awesome-ChatGPT-prompts-ZH_CN)** `List` — 中文提示词合集。
- **[WaytoAGI](https://waytoagi.com)** `List` — 中文 AI 知识库社区。
- **[AI 工具集](https://www.ai-bot.cn)** `List` — 中文 AI 工具导航。

### AI 工具导航站

- **[Futurepedia](https://futurepedia.io)** `List` — 老牌 AI 工具目录。
- **[There's An AI For That](https://theresanaiforthat.com)** `List` — 按任务描述找 AI 工具。
- **[Toolify](https://www.toolify.ai)** `List` — 海量 AI 工具目录与排行。
- **[FutureTools](https://www.futuretools.io)** `List` — 工具收录与测评。
- **[AI Tools Directory](https://aitoolsdirectory.com)** `List` — 分类式 AI 工具目录。
- **[awesome-ai-tools](https://github.com/mahseema/awesome-ai-tools)** `List` — GitHub 上的 AI 工具清单。
- **[awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai)** `List` — 生成式 AI 资源大全。

---

## 🎯 选型原则

1. **先写任务，再搜工具。** 输入是什么、产物是什么、怎么验收，三句话写不清，就不要装。
2. **一次只装一个。** 用真实材料跑一遍，记录失败和人工修改；跑不通就换，不要堆。
3. **能 MCP 不写代码。** 优先现成 server；需要定制再用 FastMCP / Python SDK 写一个最小版。
4. **权限最小化。** 文件只给需要的目录，数据库只给只读账号，浏览器用独立 profile；对外发送、付款、删除必须人工确认。
5. **每月清理。** 一个月没用到的 Skill / MCP 就删；装得越多，上下文越脏、出错越难查。

---

## 🤝 贡献

欢迎 PR 补充。格式尽量保持一致：

```markdown
- **[名称](链接)** `类型` — 一句话说明。
```

- 类型：`Skill` / `MCP` / `Tool` / `List` / `Framework` / `Course`
- 一句话控制在 20 字左右，说清「解决什么问题」，不写营销语。
- 优先收录原始仓库、官方文档、可直接运行的项目；不收录纯引流页和镜像站。
- 提交前请自己打开链接确认可访问，并在 PR 里说明它补了哪个场景。

> 本清单只做索引，版权归各项目作者。链接与项目状态会变化，使用前请自行核验。
