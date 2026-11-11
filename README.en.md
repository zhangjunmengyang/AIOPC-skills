<a id="top"></a>

<div align="center">

# 🧰 AIOPC Skills

**A curated index of Skills, MCP servers & tools for AI agents**
*Organized by the job to be done — not by vendor.*

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contribute)
[![Last Updated](https://img.shields.io/badge/updated-2026--11--11-blue.svg)](#)
[![中文](https://img.shields.io/badge/中文-README.md-red)](README.md)

</div>

A toolbox for one-person companies and solo builders. Everything here can be plugged into **Claude Code**, **Cursor**, **n8n** or a similar agent runtime.

One line per item: **name + what it does + link**. No long reviews. Start with the mega-lists, pick one tool for your current job, and only add a second one after the first works.

Links verified on **2026-11-11**. Star counts are intentionally omitted to avoid stale numbers. PRs are welcome — see [Contributing](#contribute).

---

## 🗺️ Quick Nav

| | Section | What you'll find |
|---|---|---|
| 🧭 | [Mega Lists](#mega) | 18 master indexes to bookmark first |
| 🧩 | [Skills by Task](#skills) | Product, marketing, content, data, sales, OPC |
| 🔌 | [MCP by Integration](#mcp) | Files, browser, databases, collaboration, SDKs |
| ⚙️ | [Automation](#automation) | n8n, Dify, Coze, workflow templates |
| 🤖 | [Agent Frameworks](#agent) | Frameworks, coding agents, browser agents |
| 📚 | [Knowledge / RAG](#rag) | RAGFlow, Dify, LlamaIndex |
| 🧪 | [Evals & Observability](#eval) | Promptfoo, Langfuse |
| 🎓 | [Learning](#learn) | Microsoft, OpenAI, Anthropic |
| 🇨🇳 | [Chinese Resources](#cn) | Chinese MCP, Skills, directories |

**Type tags:** `Skill` installable in Claude Code / Cursor · `MCP` Model Context Protocol server · `Tool` standalone tool / platform · `List` collection · `Framework` dev framework · `Course` course.

---

<a id="mega"></a>
## 🧭 Mega Lists · 超级大全

- **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** `List` — The largest MCP server directory, organized by use case.
- **[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)** `List` — Official reference servers: filesystem, fetch, git, memory, sqlite.
- **[anthropics/skills](https://github.com/anthropics/skills)** `List` — Official Agent Skills repo with format and examples.
- **[awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)** `List` — One of the largest Claude skill collections.
- **[agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills)** `List` — Nearly 3,000 skills, searchable by keyword.
- **[awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills)** `List` — Official and community skills, engineering-heavy.
- **[skills.sh](https://skills.sh)** `List` — Skill directory with install rankings.
- **[awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code)** `List` — Commands, hooks, skills and tools for Claude Code.
- **[superpowers](https://github.com/obra/superpowers)** `Skill` — A popular Claude Code skill framework.
- **[awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents)** `List` — Hundreds of specialized subagents by role.
- **[awesome-ai-agents](https://github.com/e2b-dev/awesome-ai-agents)** `List` — A catalog of AI agent projects.
- **[awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)** `List` — 100+ runnable agent and RAG examples.
- **[Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM)** `List` — Papers, models and tools for LLMs.
- **[awesome-rag](https://github.com/awesome-rag/awesome-rag)** `List` — RAG papers, frameworks and evaluations.
- **[awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)** `List` — The largest general prompt library.
- **[awesome-cursorrules](https://github.com/PatrickJS/awesome-cursorrules)** `List` — Cursor rules collection.
- **[superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)** `List` — Chinese edition of superpowers.
- **[AI-Coding-Guide-Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh)** `List` — Chinese AI coding guides and resources.

> Use these lists to search for keywords — don't read them end to end. Pick one repo that solves your current job and test it with real material.

[↑ Back to top](#top)

---

<a id="skills"></a>
## 🧩 Skills by Task · 按任务找

> Each entry maps one concrete job to a skill or repo you can use today. Pick the closest row; if nothing fits, search the mega-lists above.

<a id="product"></a>
### Product & Engineering · 产品与研发

- **[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)** `Skill` — Multi-role requirement breakdown and PRD.
- **[GitHub Spec Kit](https://github.com/github/spec-kit)** `Skill` — Spec-driven development.
- **[DeepWiki](https://github.com/AsyncFuncAI/deepwiki-open)** `Tool` — Auto-generate repo docs and understand a codebase fast.
- **[PR-Agent](https://github.com/qodo-ai/pr-agent)** `Tool` — Automated PR review and suggestions.
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** `MCP` — Browser automation and testing.
- **[Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)** `MCP` — Debug a real browser, network and performance.
- **[Context7](https://github.com/upstash/context7)** `MCP` — Inject up-to-date library docs into the agent.
- **[Next.js SaaS Starter](https://github.com/nextjs/saas-starter)** `Tool` — Full-stack SaaS starter template.
- **[Open SaaS](https://github.com/wasp-lang/open-saas)** `Tool` — Open-source SaaS template.
- **[Superdesign](https://github.com/superdesigndev/superdesign)** `Tool` — AI design canvas for pages and components.
- **[Coolify](https://github.com/coollabsio/coolify)** `Tool` — Self-hosted PaaS for deploying your services.
- **[Dokploy](https://github.com/Dokploy/dokploy)** `Tool` — Lightweight PaaS and Heroku alternative.

<a id="marketing"></a>
### Marketing & Growth · 营销与获客

<a id="geo"></a>
#### GEO / AI Search Optimization · AI 搜索优化

- **[gtm-engineer-skills](https://github.com/onvoyage-ai/gtm-engineer-skills)** `Skill` — AEO / GEO optimization skill pack.
- **[geo-optimizer-skill](https://github.com/Auriti-Labs/geo-optimizer-skill)** `Skill` — GEO audit and optimization engine.
- **[GEO-Content-Optimizer-Skill](https://github.com/liangdabiao/GEO-Content-Optimizer-Skill)** `Skill` — Chinese GEO content optimizer.
- **[GEOInflow](https://github.com/yaojingang/GEOInflow)** `Tool` — AI crawler and citation analysis.
- **[elmo](https://github.com/elmohq/elmo)** `Tool` — Open-source AEO / GEO monitoring.
- **[llms.txt](https://llmstxt.org/)** `Tool` — A site index for AI crawlers.
- **[GEO paper](https://arxiv.org/abs/2311.09735)** `List` — Generative Engine Optimization (KDD 2024).
- **[Google AI Features](https://developers.google.com/search/docs/appearance/ai-features)** `Tool` — Official rules for AI search and summaries.
- **[Profound](https://www.tryprofound.com/)** `Tool` — AI search visibility monitoring.

<a id="seo"></a>
#### SEO

- **[claude-seo](https://github.com/AgriciDaniel/claude-seo)** `Skill` — 26 sub-skills covering the SEO workflow.
- **[open-seo-mcp-skills](https://github.com/Ryze-AI-Adgent/open-seo-mcp-skills)** `MCP` — Free SEO MCP and skills.
- **[backlink_skills](https://github.com/flaqai/backlink_skills)** `Skill` — Free backlink submission skill pack.
- **[pseo-next](https://github.com/agamm/pseo-next)** `Tool` — Programmatic SEO page template.
- **[bisibility](https://github.com/CorgiCorner/bisibility)** `Tool` — Open-source SEO rankings and keywords.
- **[Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)** `Tool` — Official starting point.
- **[Unlighthouse](https://github.com/harlan-zw/unlighthouse)** `Tool` — Run Lighthouse across an entire site.
- **[Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)** `Tool` — Put performance checks in CI.
- **[Screaming Frog](https://www.screamingfrog.co.uk/seo-spider/)** `Tool` — Crawl and audit titles, descriptions and links.
- **[Google Search Console](https://search.google.com/search-console/about)** `Tool` — Indexing, impressions and query data.
- **[Ahrefs: Programmatic SEO](https://ahrefs.com/blog/programmatic-seo/)** `List` — Template × data × unique value.

<a id="landing"></a>
#### Landing Pages · 落地页

- **[aipage.dev](https://github.com/zinedkaloc/aipage.dev)** `Tool` — Open-source AI landing page generator.
- **[uitripled](https://github.com/moumen-soliman/uitripled)** `Tool` — Reusable landing page UI blocks.
- **[StarFunnel](https://github.com/unfolding-io/StarFunnel)** `Tool` — Astro landing page builder.
- **[OpenUI](https://github.com/wandb/openui)** `Tool` — Generate UI from a description.
- **[local-business-builder](https://github.com/savvity/local-business-builder)** `Skill` — Claude plugin for local business sites.
- **[Danny Postma: Landing Page Pipeline](https://www.dannypostma.com/landing-page)** `List` — Research → copy → design → launch.
- **[Julian Shapiro: Landing Page Copywriting](https://www.julian.com/guide/startup/landing-pages)** `List` — Hero structure and copywriting guide.
- **[Marketing Examples](https://marketingexamples.com/)** `List` — Real landing page and copy examples.
- **[Framer](https://www.framer.com/)** `Tool` — Fast marketing pages.
- **[Carrd](https://carrd.co/)** `Tool` — Minimal one-page sites.

<a id="copy"></a>
#### Copy & Brand Voice · 文案与品牌语气

- **[marketingskills](https://github.com/coreyhaines31/marketingskills)** `Skill` — Marketing copy and CRO skill set.
- **[ai-copywriter](https://github.com/mikiarlo3/ai-copywriter)** `Tool` — AI copywriting with a methodology.
- **[Brand-building-skills](https://github.com/arnabbagxd/Brand-building-skills)** `Skill` — Brand positioning and tone skills.
- **[Vale](https://github.com/vale-cli/vale)** `Tool` — Prose linter for brand style rules.
- **[Chinese Copywriting Guidelines](https://github.com/sparanoid/chinese-copywriting-guidelines)** `List` — Chinese typography conventions.
- **[Copyhackers: Review Mining](https://copyhackers.com/write-copy-amazon-review-mining/)** `List` — Mine customer language from reviews.
- **[Mailchimp: Voice & Tone](https://styleguide.mailchimp.com/voice-and-tone/)** `List` — Brand voice with situational examples.

<a id="social"></a>
#### Social, Email, Ads & PR · 社媒、邮件、广告与公关

- **[Postiz](https://github.com/gitroomhq/postiz-app)** `Tool` — Open-source multi-platform social scheduling.
- **[Mixpost](https://github.com/inovector/mixpost)** `Tool` — Self-hosted social media manager.
- **[social-media-agent](https://github.com/langchain-ai/social-media-agent)** `Tool` — Social content curation agent.
- **[xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)** `MCP` — Xiaohongshu publishing MCP.
- **[apify-mcp-server](https://github.com/apify/apify-mcp-server)** `MCP` — Social data scraping MCP.
- **[BillionMail](https://github.com/Billionmail/BillionMail)** `Tool` — Self-hosted email marketing server.
- **[Dittofeed](https://github.com/dittofeed/dittofeed)** `Tool` — Lifecycle messaging automation.
- **[Sendportal](https://github.com/mettle/sendportal)** `Tool` — Self-hosted newsletter platform.
- **[sellbird](https://github.com/ethanplusai/sellbird)** `Tool` — Open-source cold email outreach.
- **[coldoutboundskills](https://github.com/growthenginenowoslawski/coldoutboundskills)** `Skill` — Cold email scoring and writing skills.
- **[React Email](https://github.com/resend/react-email)** `Tool` — Build email templates with React.
- **[Resend](https://github.com/resend/resend-node)** `Tool` — Email sending API.
- **[Listmonk](https://github.com/knadh/listmonk)** `Tool` — Open-source self-hosted newsletter.
- **[Mautic](https://github.com/mautic/mautic)** `Tool` — Open-source marketing automation.
- **[Really Good Emails](https://www.reallygoodemails.com/)** `List` — Email examples by lifecycle stage.
- **[google-ads-mcp](https://github.com/googleads/google-ads-mcp)** `MCP` — Official Google Ads MCP.
- **[meta-ads-mcp](https://github.com/pipeboard-co/meta-ads-mcp)** `MCP` — Meta ads management MCP.
- **[google-analytics-mcp](https://github.com/googleanalytics/google-analytics-mcp)** `MCP` — Official GA4 data MCP.
- **[meta-ads-analyzer](https://github.com/mathiaschu/meta-ads-analyzer)** `MCP` — Meta ads diagnostic skill.
- **[adloop](https://github.com/kLOsk/adloop)** `MCP` — Cross-platform ad optimization MCP.
- **[Google Skillshop](https://skillshop.withgoogle.com/)** `Course` — Free official Google Ads courses.
- **[Meta Blueprint](https://www.facebook.com/business/learn)** `Course` — Official Meta ads courses.
- **[Featured News standards](https://news.featured.com/standards)** `List` — What editors look for in expert commentary.

<a id="content"></a>
### Content & Design · 内容与设计

- **[ComfyUI](https://github.com/Comfy-Org/ComfyUI)** `Tool` — Node-based image generation and editing.
- **[Penpot](https://github.com/penpot/penpot)** `Tool` — Open-source UI and brand design platform.
- **[Penpot MCP](https://github.com/penpot/penpot-mcp)** `MCP` — Official Penpot design MCP.
- **[Figma Context MCP](https://github.com/GLips/Figma-Context-MCP)** `MCP` — Give Figma layouts to coding agents.
- **[MiniMax MCP](https://github.com/MiniMax-AI/MiniMax-MCP)** `MCP` — Official image and video generation MCP.
- **[Remotion](https://github.com/remotion-dev/remotion)** `Tool` — Make videos with React.
- **[video-use](https://github.com/browser-use/video-use)** `Tool` — Edit video with a coding agent.
- **[OpenCut](https://github.com/OpenCut-app/OpenCut)** `Tool` — Open-source CapCut alternative.
- **[VideoLingo](https://github.com/Huanshere/VideoLingo)** `Tool` — Subtitle translation, dubbing and alignment.
- **[VideoCaptioner](https://github.com/WEIFENG2333/VideoCaptioner)** `Tool` — LLM subtitle generation and correction.
- **[Duix-Avatar](https://github.com/duixcom/Duix-Avatar)** `Tool` — Open-source digital human video.
- **[WhisperX](https://github.com/m-bain/whisperX)** `Tool` — Transcription, alignment and speaker diarization.
- **[presenton](https://github.com/presenton/presenton)** `Tool` — Open-source AI PPT generator.
- **[Presentation AI](https://github.com/allweonedev/presentation-ai)** `Tool` — Open-source Gamma alternative.
- **[Office PowerPoint MCP](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server)** `MCP` — Read and write PPT files.
- **[Slidev](https://github.com/slidevjs/slidev)** `Tool` — Markdown-powered slides.
- **[Marp](https://github.com/marp-team/marp)** `Tool` — Markdown to PPT.
- **[PptxGenJS](https://github.com/gitbrent/PptxGenJS)** `Tool` — Generate PPTX with code.
- **[docxtemplater](https://github.com/open-xml-templating/docxtemplater)** `Tool` — Batch-generate Word and PPT from templates.
- **[Carbone](https://github.com/carboneio/carbone)** `Tool` — JSON to PDF / Word reports.
- **[Lucide](https://github.com/lucide-icons/lucide)** `Tool` — Open-source icon set.
- **[awesome-design-systems](https://github.com/alexpate/awesome-design-systems)** `List` — Design system references.

<a id="data"></a>
### Data & Research · 数据与研究

- **[Exa](https://github.com/exa-labs/exa-py)** `Tool` — Semantic search API.
- **[Tavily](https://github.com/tavily-ai/tavily-python)** `Tool` — Search API built for agents.
- **[tavily-mcp](https://github.com/tavily-ai/tavily-mcp)** `MCP` — Real-time search and scraping MCP.
- **[SearXNG](https://github.com/searxng/searxng)** `Tool` — Open-source meta search engine.
- **[Firecrawl](https://github.com/firecrawl/firecrawl)** `Tool` — Web scraping, crawling and deep research.
- **[firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)** `MCP` — Official scraping and search MCP.
- **[Crawl4AI](https://github.com/unclecode/crawl4ai)** `Tool` — LLM-friendly crawler.
- **[Scrapling](https://github.com/D4Vinci/Scrapling)** `Tool` — High-resistance scraping framework.
- **[Jina Reader](https://github.com/jina-ai/reader)** `Tool` — Web page to Markdown.
- **[Crawlee](https://github.com/apify/crawlee)** `Tool` — Crawler framework.
- **[changedetection.io](https://github.com/dgtlmoon/changedetection.io)** `Tool` — Page change monitoring and alerts.
- **[Serper](https://serper.dev)** `Tool` — Google Search API.
- **[Metabase](https://github.com/metabase/metabase)** `Tool` — Open-source BI and dashboards.
- **[Vanna](https://github.com/vanna-ai/vanna)** `Tool` — Natural language to SQL.
- **[WrenAI](https://github.com/Canner/WrenAI)** `Tool` — Governed text-to-SQL platform.
- **[SQLBot](https://github.com/dataease/SQLBot)** `Tool` — Chinese natural language analytics.
- **[Evidence](https://github.com/evidence-dev/evidence)** `Tool` — SQL-driven BI reports.
- **[DuckDB](https://github.com/duckdb/duckdb)** `Tool` — Local analytical database.
- **[PandasAI](https://github.com/Sinaptik-AI/pandas-ai)** `Tool` — Analyze tables in natural language.
- **[NocoDB](https://github.com/nocodb/nocodb)** `Tool` — Open-source Airtable alternative.
- **[Teable](https://github.com/teableio/teable)** `Tool` — Multi-dimensional tables and database.
- **[awesome-web-scraping](https://github.com/lorien/awesome-web-scraping)** `List` — Web scraping resources.

<a id="sales"></a>
### Sales, Support & Ops · 销售、客服与运营

- **[Twenty](https://github.com/twentyhq/twenty)** `Tool` — AI-native open-source CRM.
- **[twenty-crm-mcp-server](https://github.com/mhenry3164/twenty-crm-mcp-server)** `MCP` — MCP for Twenty CRM.
- **[Krayin](https://github.com/krayin/laravel-crm)** `Tool` — Laravel open-source CRM.
- **[Chatwoot](https://github.com/chatwoot/chatwoot)** `Tool` — Omnichannel support desk.
- **[Zammad](https://github.com/zammad/zammad)** `Tool` — Open-source ticketing helpdesk.
- **[Invoice Ninja](https://github.com/invoiceninja/invoiceninja)** `Tool` — Open-source invoicing and billing.
- **[Crater](https://github.com/crater-invoice-inc/crater)** `Tool` — Open-source invoicing and billing.
- **[InvoicePlane](https://github.com/InvoicePlane/InvoicePlane)** `Tool` — Self-hosted invoice management.
- **[DocuSeal](https://github.com/docusealco/docuseal)** `Tool` — Open-source e-signature.
- **[Documenso](https://github.com/documenso/documenso)** `Tool` — Open-source DocuSign alternative.
- **[ai-legal-claude](https://github.com/zubair-trabzada/ai-legal-claude)** `Skill` — Contract review and risk skills.
- **[claude-legal-skill](https://github.com/evolsb/claude-legal-skill)** `Skill` — CUAD contract risk review.
- **[devnors-data-mcp](https://github.com/DevnorsAI/devnors-data-mcp)** `MCP` — Chinese legal data MCP.
- **[Plane](https://github.com/makeplane/plane)** `Tool` — Open-source project management.
- **[OpenProject](https://github.com/opf/openproject)** `Tool` — Open-source project management platform.
- **[Cal.com](https://github.com/calcom/cal.com)** `Tool` — Open-source scheduling.
- **[OpenCATS](https://github.com/opencats/OpenCATS)** `Tool` — Open-source recruiting ATS.
- **[nueno](https://github.com/nueno-co/nueno)** `Tool` — Modern open-source ATS.
- **[OpenResume](https://github.com/xitanggg/open-resume)** `Tool` — Resume builder and parser.
- **[Outline](https://github.com/outline/outline)** `Tool` — Team knowledge base.
- **[Docmost](https://github.com/docmost/docmost)** `Tool` — Open-source collaborative docs.

<a id="opc"></a>
### OPC · 一人公司专用

- **[easychen/opc-methodology](https://github.com/easychen/opc-methodology)** `Skill` — Niche selection, asset pool, canvas and 9 business skills.
- **[iamtouchskyer/opc](https://github.com/iamtouchskyer/opc)** `Skill` — 21 roles, 6 flows and scripted gates for review pipelines.
- **[validate-opc-project](https://github.com/luqi67677/validate-opc-project)** `Skill` — Five-role review, counter-evidence and stop lines.
- **[opcspace/opcstartup-skill](https://github.com/opcspace/opcstartup-skill)** `Skill` — 0-6 stages, 100-day plan and 12 templates.
- **[slavingia/skills](https://github.com/slavingia/skills)** `Skill` — Nine-step skills from The Minimalist Entrepreneur.

[↑ Back to top](#top)

---

<a id="mcp"></a>
## 🔌 MCP by Integration · 按接入对象找

> MCP is the common interface for giving agents tools. Install one filesystem / browser / database server, finish a real task, then add the next one.

<a id="mcp-registry"></a>
### Directories · 大全与注册表

- **[awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)** `List` — The largest MCP server collection.
- **[Official servers](https://github.com/modelcontextprotocol/servers)** `List` — Reference filesystem, fetch, git, memory and sqlite servers.
- **[MCP docs](https://modelcontextprotocol.io)** `List` — Protocol spec and integration guide.
- **[Official Registry](https://registry.modelcontextprotocol.io)** `List` — Official server registry and discovery.
- **[Glama](https://glama.ai/mcp/servers)** `List` — Very large MCP registry.
- **[PulseMCP](https://www.pulsemcp.com)** `List` — Daily-updated full directory.
- **[mcp.so](https://mcp.so)** `List` — Long-running MCP directory.
- **[Smithery](https://smithery.ai)** `List` — One-click hosted MCP, now part of Arcade.
- **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** `List` — Chinese MCP resources.
- **[MCP Chinese Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** `Course` — Build your first MCP server in Chinese.

<a id="mcp-code"></a>
### Files, Code & Terminal · 文件、代码、终端

- **[Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** `MCP` — Controlled local file access.
- **[Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** `MCP` — Read, search and operate Git repos.
- **[GitHub](https://github.com/github/github-mcp-server)** `MCP` — Issues, PRs, code search and Actions.
- **[Serena](https://github.com/oraios/serena)** `MCP` — Semantic code retrieval and editing for large repos.
- **[Desktop Commander](https://github.com/wonderwhy-er/DesktopCommanderMCP)** `MCP` — Terminal commands and file editing.
- **[Context7](https://github.com/upstash/context7)** `MCP` — Up-to-date library docs.
- **[Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** `MCP` — Step-by-step reflective reasoning.

<a id="mcp-browser"></a>
### Browser & Web · 浏览器与网页

- **[Playwright](https://github.com/microsoft/playwright-mcp)** `MCP` — Browser automation, clicks, screenshots and tests.
- **[Chrome DevTools](https://github.com/ChromeDevTools/chrome-devtools-mcp)** `MCP` — Debug a real browser.
- **[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** `MCP` — Fetch pages as Markdown.
- **[Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server)** `MCP` — Scraping, crawling and deep research.
- **[Browserbase](https://github.com/browserbase/mcp-server-browserbase)** `MCP` — Cloud browsers for scale and anti-bot cases.

<a id="mcp-db"></a>
### Databases · 数据库与数据

- **[Postgres MCP Pro](https://github.com/crystaldba/postgres-mcp)** `MCP` — Postgres reads, writes, indexes and tuning.
- **[DBHub](https://github.com/bytebase/dbhub)** `MCP` — Universal DB gateway: SQLite, MySQL, Postgres.
- **[Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** `MCP` — Knowledge-graph persistent memory.
- **[AntV Chart](https://github.com/antvis/mcp-server-chart)** `MCP` — 25+ chart types.

<a id="mcp-collab"></a>
### Collaboration · 协作与办公

- **[Slack](https://github.com/korotovsky/slack-mcp-server)** `MCP` — Read channels, search and send messages.
- **[Notion](https://github.com/makenotion/notion-mcp-server)** `MCP` — Read and write pages, databases and comments.
- **[Figma](https://github.com/GLips/Figma-Context-MCP)** `MCP` — Give Figma layouts, components and styles to agents.
- **[Lark OpenAPI](https://github.com/larksuite/lark-openapi-mcp)** `MCP` — Feishu/Lark docs, sheets and messages.

<a id="mcp-dev"></a>
### Clients & SDKs · 客户端与开发框架

- **[Python SDK](https://github.com/modelcontextprotocol/python-sdk)** `Framework` — Official Python SDK.
- **[TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)** `Framework` — Official TypeScript SDK.
- **[FastMCP](https://github.com/PrefectHQ/fastmcp)** `Framework` — Build MCP servers fast in Python.
- **[mcp-use](https://github.com/mcp-use/mcp-use)** `Framework` — Full-stack MCP app framework.
- **[MCP Inspector](https://github.com/modelcontextprotocol/inspector)** `Tool` — Debug and test MCP servers.
- **[Cherry Studio](https://github.com/CherryHQ/cherry-studio)** `Tool` — Desktop client with MCP support.

[↑ Back to top](#top)

---

<a id="automation"></a>
## ⚙️ Automation · 自动化与工作流

> Make a repeated process work by hand first, then automate it. Don't use tools to hide a process that shouldn't exist.

- **[n8n](https://github.com/n8n-io/n8n)** `Tool` — Open-source visual workflows, self-hostable, MCP-ready.
- **[n8n-workflows](https://github.com/Zie619/n8n-workflows)** `List` — Thousands of ready-made n8n workflows.
- **[awesome-n8n-templates](https://github.com/enescingoz/awesome-n8n-templates)** `List` — n8n templates by scenario.
- **[n8n templates](https://n8n.io/workflows/)** `List` — Official workflow template community.
- **[Make templates](https://www.make.com/en/templates)** `List` — 3,500+ app integration templates.
- **[Zapier templates](https://zapier.com/templates)** `List` — Large library of integration workflows.
- **[Activepieces](https://github.com/activepieces/activepieces)** `Tool` — Open-source Zapier alternative.
- **[Windmill](https://github.com/windmill-labs/windmill)** `Tool` — Code-first workflow and script platform.
- **[Dify](https://github.com/langgenius/dify)** `Tool` — Visual LLM apps and workflows.
- **[Coze Studio](https://github.com/coze-dev/coze-studio)** `Tool` — ByteDance's open-source low-code agent platform.
- **[Flowise](https://github.com/FlowiseAI/Flowise)** `Tool` — Drag-and-drop LLM flows and agents.
- **[Langflow](https://github.com/langflow-ai/langflow)** `Tool` — Visual LangChain orchestration.
- **[Botpress](https://github.com/botpress/botpress)** `Tool` — Conversational bot platform.

[↑ Back to top](#top)

---

<a id="agent"></a>
## 🤖 Agent Frameworks · Agent 框架与编程 Agent

> Start with an off-the-shelf coding agent. Build a framework only when you actually need one.

<a id="agent-framework"></a>
### Frameworks · 通用框架

- **[LangGraph](https://github.com/langchain-ai/langgraph)** `Framework` — Stateful, resumable graphs with human-in-the-loop.
- **[CrewAI](https://github.com/crewAIInc/crewAI)** `Framework` — Role-playing multi-agent collaboration.
- **[AutoGen](https://github.com/microsoft/autogen)** `Framework` — Microsoft multi-agent conversation and coding.
- **[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)** `Framework` — Lightweight multi-agent workflows.
- **[Google ADK](https://github.com/google/adk-python)** `Framework` — Google's code-first agent toolkit.
- **[Mastra](https://github.com/mastra-ai/mastra)** `Framework` — TypeScript-first agent framework.
- **[Pydantic AI](https://github.com/pydantic/pydantic-ai)** `Framework` — Type-safe Python agents.
- **[Agno](https://github.com/agno-agi/agno)** `Framework` — High-performance full-stack agent platform.
- **[Vercel AI SDK](https://github.com/vercel/ai)** `Framework` — Frontend-friendly AI toolkit.
- **[LangChain](https://github.com/langchain-ai/langchain)** `Framework` — The most widely used LLM app framework.
- **[Semantic Kernel](https://github.com/microsoft/semantic-kernel)** `Framework` — Microsoft enterprise LLM integration.

<a id="agent-coding"></a>
### Coding Agents · 编程 Agent / IDE

- **[Claude Code](https://github.com/anthropics/claude-code)** `Tool` — Terminal agent that reads, edits and runs code.
- **[Codex CLI](https://github.com/openai/codex)** `Tool` — OpenAI's terminal coding agent.
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** `Tool` — Google's terminal agent.
- **[OpenHands](https://github.com/All-Hands-AI/OpenHands)** `Tool` — Open-source AI software engineer, self-hostable.
- **[Cline](https://github.com/cline/cline)** `Tool` — Autonomous coding agent in the IDE.
- **[Roo Code](https://github.com/RooCodeInc/Roo-Code)** `Tool` — Multi-role, multi-mode dev team.
- **[Aider](https://github.com/Aider-AI/aider)** `Tool` — Terminal pair programming with good git integration.
- **[Continue](https://github.com/continuedev/continue)** `Tool` — Customizable open-source coding assistant.
- **[SWE-agent](https://github.com/SWE-agent/SWE-agent)** `Tool` — Automatically fixes GitHub issues.
- **[Goose](https://github.com/block/goose)** `Tool` — Extensible local automation agent.

<a id="agent-browser"></a>
### Browser & Computer Use · 浏览器 / 电脑操作

- **[browser-use](https://github.com/browser-use/browser-use)** `Tool` — Let AI operate a browser.
- **[Stagehand](https://github.com/browserbase/stagehand)** `Tool` — Natural-language web automation.
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp)** `MCP` — Control Playwright through MCP.
- **[Skyvern](https://github.com/Skyvern-AI/skyvern)** `Tool` — Vision-driven browser workflows.
- **[E2B](https://github.com/e2b-dev/E2B)** `Tool` — Secure sandbox for agents.
- **[Anthropic Quickstarts](https://github.com/anthropics/anthropic-quickstarts)** `Tool` — Claude computer-use examples.

[↑ Back to top](#top)

---

<a id="rag"></a>
## 📚 Knowledge / RAG · 知识库

- **[RAGFlow](https://github.com/infiniflow/ragflow)** `Tool` — Deep document understanding, strong for Chinese docs.
- **[Dify](https://github.com/langgenius/dify)** `Tool` — Visual LLM app and knowledge base platform.
- **[FastGPT](https://github.com/labring/FastGPT)** `Tool` — Knowledge-base Q&A and workflow orchestration.
- **[LlamaIndex](https://github.com/run-llama/llama_index)** `Framework` — Document processing and RAG framework.
- **[LightRAG](https://github.com/HKUDS/LightRAG)** `Framework` — Lightweight graph-enhanced retrieval.
- **[GraphRAG](https://github.com/microsoft/graphrag)** `Framework` — Microsoft graph-structured RAG.
- **[Milvus](https://github.com/milvus-io/milvus)** `Tool` — Cloud-native vector database.
- **[AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)** `Tool` — Turnkey local knowledge base and desktop agent.
- **[Khoj](https://github.com/khoj-ai/khoj)** `Tool` — Self-hosted personal AI second brain.
- **[Haystack](https://github.com/deepset-ai/haystack)** `Framework` — Production RAG and search framework.

[↑ Back to top](#top)

---

<a id="eval"></a>
## 🧪 Evals & Observability · 评测与可观测

- **[Promptfoo](https://github.com/promptfoo/promptfoo)** `Tool` — Compare prompts and models, plus red teaming.
- **[Langfuse](https://github.com/langfuse/langfuse)** `Tool` — Open-source LLM observability, evals and prompt management.
- **[DeepEval](https://github.com/confident-ai/deepeval)** `Tool` — Unit tests for LLM outputs.
- **[Braintrust](https://github.com/braintrustdata/braintrust-sdk)** `Tool` — Evals, datasets and experiment tracking.
- **[Helicone](https://github.com/Helicone/helicone)** `Tool` — LLM logs, cost and latency monitoring.
- **[OpenAI Evals](https://github.com/openai/evals)** `Tool` — Official eval framework and examples.
- **[Arize Phoenix](https://github.com/Arize-ai/phoenix)** `Tool` — Open-source LLM tracing, evals and visualization.

[↑ Back to top](#top)

---

<a id="learn"></a>
## 🎓 Learning · 学习与课程

- **[ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners)** `Course` — Microsoft's 18-lesson agent course with code.
- **[generative-ai-for-beginners](https://github.com/microsoft/generative-ai-for-beginners)** `Course` — Microsoft's 21-lesson generative AI course.
- **[OpenAI Cookbook](https://github.com/openai/openai-cookbook)** `Course` — Official OpenAI API examples and recipes.
- **[Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)** `Course` — Claude, tool use and RAG recipes.
- **[HF Agents Course](https://github.com/huggingface/agents-course)** `Course` — HuggingFace agents course from zero to deployment.
- **[LangChain Academy](https://github.com/langchain-ai/langchain-academy)** `Course` — Official LangGraph course.
- **[Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)** `Course` — Authoritative prompt engineering guide.
- **[Anthropic Prompt Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)** `Course` — Official interactive prompt tutorial.

[↑ Back to top](#top)

---

<a id="cn"></a>
## 🇨🇳 Chinese Resources · 中文资源与导航

<a id="cn-resources"></a>
### Chinese · 中文资源

- **[Awesome-MCP-ZH](https://github.com/yzfly/Awesome-MCP-ZH)** `List` — Chinese MCP servers and tutorials.
- **[MCP Chinese Guide](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide)** `Course` — Build your first MCP server.
- **[superpowers-zh](https://github.com/jnMetaCode/superpowers-zh)** `List` — Chinese edition of the superpowers framework.
- **[AI-Coding-Guide-Zh](https://github.com/KimYx0207/AI-Coding-Guide-Zh)** `List` — Chinese AI coding guides and tools.
- **[claude-howto-zh-cn](https://github.com/lhfer/claude-howto-zh-cn)** `List` — Claude Code guide in Chinese.
- **[everything-claude-code-zh](https://github.com/xu-xiang/everything-claude-code-zh)** `List` — Chinese translation of the Claude Code ecosystem.
- **[Lark OpenAPI MCP](https://github.com/larksuite/lark-openapi-mcp)** `MCP` — Feishu/Lark docs, sheets and messages.
- **[ModelScope MCP](https://modelscope.cn/mcp)** `List` — ModelScope's Chinese MCP marketplace.
- **[awesome-agentic-ai-zh](https://github.com/WenyuChiou/awesome-agentic-ai-zh)** `List` — Chinese agent learning map.
- **[Awesome-Chinese-LLM](https://github.com/AiHubCN/Awesome-Chinese-LLM)** `List` — Chinese LLM resources.
- **[Chinese Prompt Library](https://github.com/L1Xu4n/Awesome-ChatGPT-prompts-ZH_CN)** `List` — Chinese prompt collection.
- **[WaytoAGI](https://waytoagi.com)** `List` — Chinese AI knowledge community.
- **[AI Tool Collection](https://www.ai-bot.cn)** `List` — Chinese AI tool directory.

<a id="cn-directories"></a>
### AI Directories · 工具导航站

- **[Futurepedia](https://futurepedia.io)** `List` — Long-running AI tool directory.
- **[There's An AI For That](https://theresanaiforthat.com)** `List` — Find AI tools by task description.
- **[Toolify](https://www.toolify.ai)** `List` — Large AI tool directory and rankings.
- **[FutureTools](https://www.futuretools.io)** `List` — AI tool collection and reviews.
- **[AI Tools Directory](https://aitoolsdirectory.com)** `List` — Categorized AI tool directory.
- **[awesome-ai-tools](https://github.com/mahseema/awesome-ai-tools)** `List` — GitHub AI tool list.
- **[awesome-generative-ai](https://github.com/steven2358/awesome-generative-ai)** `List` — Generative AI resource collection.

[↑ Back to top](#top)

---

<a id="contribute"></a>
## 🤝 Contributing · 贡献

PRs are welcome. Keep the format consistent:

```markdown
- **[Name](link)** `Type` — One line on what it solves.
```

- Types: `Skill` / `MCP` / `Tool` / `List` / `Framework` / `Course`
- Keep the description to one short sentence: what problem it solves, no marketing copy.
- Prefer original repos, official docs and runnable projects; skip landing pages and mirrors.
- Open the link yourself before submitting, and say which use case it covers in the PR.

> This list is an index only. Copyright belongs to each project's authors. Links and project status change; verify before use.

---

<div align="center">

**[⬆ Back to top](#top)** · [中文](README.md)

</div>
