<a id="top"></a>

<p align="center">
  <img src="assets/banner.png" alt="AIOPC Skills — AI skills, MCP servers and tools for one-person companies" width="100%" />
</p>

<p align="center">
  <a href="README.zh.md">中文</a> · <a href="#contents">Browse</a> · <a href="#start-here">Quick start</a> · <a href="#contributing">Contribute</a>
</p>

AI skills, tools and practical guides for building and running a one-person business.

{{UNIQUE_URLS}} source links · English & Chinese · Fully expanded below

<a id="contents"></a>
## Contents

{{TOC}}

{{CATALOG}}

<a id="start-here"></a>
## Start with your task

| Current task | First deliverable |
|---|---|
| [Validate paying demand](#startup) | A customer, a problem and a small paid deliverable |
| [Turn a service into a product](#product) | An acceptance scope and a minimum deliverable version |
| [Find the first users](#marketing) | One channel and one content or landing-page experiment |
| [Close sales and collect payments](#ops) | A quote, scope, payment milestones and acceptance agreement |
| [Manage delivery capacity](#operator-playbook) | Capacity, change records, handover notes and margin per job |
| [Keep a live service reliable](#operating-resources) | Payment-event handling, alerts and a recovery drill |
| [Sell content or digital goods](#content) | A product that can be bought, delivered and refunded |
| [Reduce platform and availability dependence](#operator-playbook) | Exportable assets, absence cover and a handover checklist |

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
| Refine an idea | [idea-refine](https://github.com/addyosmani/agent-skills/blob/HEAD/skills/idea-refine/SKILL.md) | Turn an idea into a concept to validate |
| Define the customer job | [define-jtbd-canvas](https://github.com/product-on-purpose/pm-skills/blob/HEAD/skills/define-jtbd-canvas/SKILL.md) | Describe the customer task and its context |
| Write requirements | [prd-development](https://github.com/deanpeters/Product-Manager-Skills/blob/HEAD/skills/prd-development/SKILL.md) | Structure scope, needs and acceptance requirements |
| Build an interface | [frontend-design](https://github.com/anthropics/skills/blob/HEAD/skills/frontend-design/SKILL.md) | Design and implement a frontend interface |
| Write a sales page | [copywriting](https://github.com/coreyhaines31/marketingskills/blob/HEAD/skills/copywriting/SKILL.md) | Organize benefits, evidence and the next action |
| Review search visibility | [seo-audit](https://github.com/coreyhaines31/marketingskills/blob/HEAD/skills/seo-audit/SKILL.md) | Inspect issues affecting site discoverability |
| Founder sales | [founder-sales](https://github.com/refoundai/lenny-skills/blob/HEAD/skills/founder-sales/SKILL.md) | Structure direct customer contact and sales work |
| Onboarding & retention | [retention](https://github.com/whawkinsiv/solo-founder-skills/blob/HEAD/skills/retention/SKILL.md) | Plan first use, welcome emails, follow-ups and cancellation |
| Pricing | [pricing](https://github.com/coreyhaines31/marketingskills/blob/HEAD/skills/pricing/SKILL.md) | Consider pricing, packaging and revenue models |
| Unit economics | [unit-economics](https://github.com/anthropics/financial-services/blob/HEAD/plugins/vertical-plugins/private-equity/skills/unit-economics/SKILL.md) | Examine revenue and cost assumptions per unit |
| Browser operations | [Playwright MCP](https://github.com/microsoft/playwright-mcp) | Let an MCP-compatible agent operate and inspect web pages |
| Backup recovery | [restic restore guide](https://restic.readthedocs.io/en/stable/050_restore.html) | Restore a backup to a target directory and verify the result |

<a id="curation"></a>
## Curation & maintenance

- Organize by concrete tasks, with source links and short descriptions. Full instructions, dependencies and licenses live upstream.
- Prefer specific source files. Entries marked "repository entry" have no confirmed file match; check the author's repository for current content. Collection names link to repositories. See [upstream-links.json](data/upstream-links.json) for the link audit.
- Focused collections include use descriptions. The extended index groups entries by source pack; individual entries can cross domains, so a pack's section is not an item-level classification.
- A reachable page, an existing upstream skill, a successful installation and a useful real-task result are different checks. New operating guides were checked against first-party descriptions. The entire catalog has not been installed or tested; a cached page returning 200 does not establish current installability.
- READMEs and the machine catalog are generated from source documents. Checks enforce complete resource exposure, matching bilingual external-link sets, valid local links and anchors, and GitHub's README size limit.
- Counts use unique full URLs; topic and platform sections can reuse a resource. Download [catalog.json](catalog.json) for structured data, see [CHANGELOG](CHANGELOG.md) for changes and [NOTICE](NOTICE.md) for attribution.

<a id="contributing"></a>
## Contributing

Contribute missing tasks, correct descriptions or replace unavailable resources. Include the original source, its specific use and the level of verification performed. Update both languages and rebuild the catalog; see [CONTRIBUTING](CONTRIBUTING.md).

[Back to top](#top) · [中文](README.zh.md)
