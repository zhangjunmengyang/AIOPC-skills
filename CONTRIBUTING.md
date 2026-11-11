# Contributing / 贡献指南

[English](#english) · [中文](#中文)

## 中文

在 `docs/zh/` 和 `docs/en/` 同步修改源文件，保持资源链接与分类对应。`README.md`、`README.zh.md` 和 `catalog.json` 由脚本生成，请勿手工修改。

首屏介绍、固定导航和使用说明在 `templates/README.zh.md` 与 `templates/README.en.md` 中修改。新增双语源文档后，在 `scripts/build_readme.py` 的 `GROUPS` 中登记路径和展示顺序，再重新生成目录。

新增或修改资源时：

- 提供原项目、作者仓库或官方文档的链接。
- 用一句话说明具体用途，并放入对应任务分类。
- 区分技能、工具和指南；确有使用限制时简短说明。
- 保留原作者归属，不复制第三方教程全文。参见 [索引说明](NOTICE.md)。

在 PR 中说明修改原因和检查范围：

| 检查 | 应提供的信息 |
|---|---|
| 链接核对 | 访问过哪些链接，是否重定向或失效 |
| 来源阅读 | 阅读了哪份原始说明，确认了什么用途或限制 |
| 实际测试 | 使用的环境、任务、预期和实际结果 |

只做了链接核对就写链接核对；不要将部分检查表述为全部资源已验收。

使用 Python 3.12 运行：

```sh
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
python3 scripts/check_catalog.py
```

一并提交修改后的源文件与生成结果。CI 检查生成结果是否一致，以及本地链接、锚点、双语资源对应和目录完整性；不探测外部网站，也不验证第三方工具的运行效果。

## English

Update source files in `docs/zh/` and `docs/en/` together, keeping resource links and categories aligned. `README.md`, `README.zh.md` and `catalog.json` are generated; do not edit them by hand.

Edit the introduction, fixed navigation and usage instructions in `templates/README.zh.md` and `templates/README.en.md`. After adding a bilingual document pair, register its path and display order in `GROUPS` in `scripts/build_readme.py`, then regenerate the catalog.

When adding or changing a resource:

- Link to the original project, author repository or official documentation.
- Describe its specific use in one sentence and place it under the relevant task.
- Distinguish skills, tools and guides; mention material usage limits briefly.
- Preserve attribution and avoid copying entire third-party tutorials. See the [index notice](NOTICE.md).

Explain the change and the scope of your checks in the PR:

| Check | Evidence to include |
|---|---|
| Link check | Which URLs you visited, including redirects or failures |
| Source review | Which original documentation you read and what use or limitation it supports |
| Hands-on test | Environment, task, expected result and actual result |

Report link checks as link checks. Do not describe partial checks as validation of the entire collection.

Run with Python 3.12:

```sh
python3 scripts/build_readme.py
python3 scripts/build_readme.py --check
python3 scripts/check_catalog.py
```

Commit the changed source files and generated outputs together. CI checks generated-file consistency, local links, anchors, bilingual resource alignment and catalog completeness. It does not probe external sites or verify third-party tools in use.
