<a id="top"></a>

<h1 align="center">
  <img src="assets/banner.png" alt="AIOPC Skills — AI skills, MCP servers and tools for one-person companies" width="100%" />
</h1>

<p align="center">
  <a href="README.zh.md">中文</a> · <a href="#contents">Full contents</a> · <a href="#getting-started">Getting started</a> · <a href="#contributing">Contribute</a>
</p>

An AI resource index for independent developers, consultants, creators and small service businesses. Covers demand discovery, product, acquisition, sales, delivery and operations. Both the focused collections and the extended catalog are expanded on this page and searchable in your browser.

**{{UNIQUE_URLS}} resource and reference URLs · Including {{SKILL_URLS}} skill listing pages · English and Chinese.** Counts use unique full URLs; platform and topic views reuse resources. Machine-readable version: [catalog.json](catalog.json).

<a id="contents"></a>
## Contents

[Start with your task](#start-here) · [Installation & use](#getting-started) · [Starter kit](#starter-kit) · [Curation & maintenance](#curation)

{{TOC}}

<a id="start-here"></a>
## Start with your task

| Current task | On this page | First deliverable |
|---|---|---|
| An idea without evidence of paying demand | [Starting up](#startup) · [Operating playbooks](#operator-playbook) | A customer, a problem and a small paid deliverable |
| Turning a service into a product | [Product & engineering](#product) · [Design](#design) | An acceptance scope and a minimum deliverable version |
| A launched product with little traffic | [Marketing & growth](#marketing) · [Platforms](#platforms) | One channel and one content or landing-page experiment |
| Inquiries that do not reliably become paid work | [Sales & operations](#ops) · [Operating playbooks](#operator-playbook) | A quote, scope, payment milestones and acceptance agreement |
| More work than delivery capacity | [Operating playbooks](#operator-playbook) | Capacity, change records, handover notes and margin per job |
| Software serving real customers | [Operating tools & guides](#operating-resources) | Payment-event handling, alerts and a recovery drill |
| Content, courses or digital goods | [Content production](#content) · [Platforms](#platforms) | A product that can be bought, delivered and refunded |
| Reducing dependence on platforms and constant availability | [Operating playbooks](#operator-playbook) · [Operating tools](#operating-resources) | Exportable customer/content assets, absence cover and a handover checklist |

<a id="getting-started"></a>
## Installation & use

| Type | What it provides | How to use it |
|---|---|---|
| Skill | Task instructions, optionally with scripts, templates and references | Follow the source instructions for a compatible agent |
| MCP | Data and actions from an external system | Configure the server and permissions in an MCP client |
| Tool / official guide | A running service, CLI or operating instructions | Deploy, sign up or follow the project's documentation |

Format references: [Agent Skills](https://agentskills.io/home) · [MCP architecture](https://modelcontextprotocol.io/docs/learn/architecture). Format support alone does not provide dependencies, account permissions or a matching runtime.

For example, install a copywriting skill with the [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add coreyhaines31/marketingskills --skill copywriting
```

The CLI currently requires Node.js 22.20 or later and lets you select a target agent. This command does not install MCP servers or ordinary tools. Start with resources for one current task, evaluate the output on real work and keep what helps.

<a id="starter-kit"></a>
## Starter kit

| Task | Resource | Use |
|---|---|---|
| Refine an idea | [idea-refine](https://www.skills.sh/addyosmani/agent-skills/idea-refine) | Turn an idea into a concept to validate |
| Define the customer job | [define-jtbd-canvas](https://www.skills.sh/product-on-purpose/pm-skills/define-jtbd-canvas) | Describe the customer task and its context |
| Write requirements | [prd-development](https://www.skills.sh/deanpeters/product-manager-skills/prd-development) | Structure scope, needs and acceptance requirements |
| Build an interface | [frontend-design](https://www.skills.sh/anthropics/skills/frontend-design) | Design and implement a frontend interface |
| Write a sales page | [copywriting](https://www.skills.sh/coreyhaines31/marketingskills/copywriting) | Organize benefits, evidence and the next action |
| Review search visibility | [seo-audit](https://www.skills.sh/coreyhaines31/marketingskills/seo-audit) | Inspect issues affecting site discoverability |
| Founder sales | [founder-sales](https://www.skills.sh/refoundai/lenny-skills/founder-sales) | Structure direct customer contact and sales work |
| User onboarding | [user-onboarding](https://www.skills.sh/refoundai/lenny-skills/user-onboarding) | Design the path from first use to initial value |
| Pricing | [pricing](https://www.skills.sh/coreyhaines31/marketingskills/pricing) | Consider pricing, packaging and revenue models |
| Unit economics | [unit-economics](https://www.skills.sh/anthropics/financial-services/unit-economics) | Examine revenue and cost assumptions per unit |
| Browser operations | [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Let an MCP-compatible agent operate and inspect web pages |
| Backup recovery | [restic restore guide](https://restic.readthedocs.io/en/stable/050_restore.html) | Restore a backup to a target directory and verify the result |

{{CATALOG}}

<a id="curation"></a>
## Curation & maintenance

- Organize by concrete tasks, with source links and short descriptions. Full instructions, dependencies and licenses live upstream.
- Focused collections include use descriptions. The extended index groups entries by source pack; individual entries can cross domains, so a pack's section is not an item-level classification.
- A reachable page, an existing upstream skill, a successful installation and a useful real-task result are different checks. New operating guides were checked against first-party descriptions. The entire catalog has not been installed or tested; a cached page returning 200 does not establish current installability.
- READMEs and the machine catalog are generated from source documents. Checks enforce complete resource exposure, matching bilingual external-link sets, valid local links and anchors, and GitHub's README size limit.
- See [CHANGELOG](CHANGELOG.md) for changes and [NOTICE](NOTICE.md) for attribution.

<a id="contributing"></a>
## Contributing

Contribute missing tasks, correct descriptions or replace unavailable resources. Include the original source, its specific use and the level of verification performed. Update both languages and rebuild the catalog; see [CONTRIBUTING](CONTRIBUTING.md).

[Back to top](#top) · [中文](README.zh.md)
