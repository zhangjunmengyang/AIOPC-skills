# Changes / 更新记录

## 2026-11-11 — Reading layout / 阅读排版

- 总目录改为五个清晰入口，分类与长章节使用短名称分列导航；较短章节直接展开。
- 五个主栏目使用统一的 Lucide 线条图标，随仓库保存 SVG 与许可证，不使用 emoji。
- 首屏缩短介绍，安装说明、任务选择和入门组合移至资源正文之后，保留顶部快捷入口。
- 资源链接取消统一加粗，「仓库入口」移到链接外；修正标题层级，合并工作流表格中的重复「打开」列。
- 保留全部来源链接、资源正文和已定稿图片，无折叠内容。

Simplified the main contents to five entries with Lucide line icons, aligned short category links, reduced the preface and moved usage guides after the catalog. Resource links use normal weight with source-status labels outside the link. Corrected heading hierarchy and removed repetitive "Open" table columns. All resource links, expanded content and approved artwork remain available. Original icon SVGs and their license are bundled locally; no emoji are used.

## 2026-11-11 — Direct sources / 资源直达源码

- 中英文 README、源文档和机器目录改为直链作者仓库、具体源码或官方文档，不再以 skills.sh 聚合页作为资源入口。
- 核对 172 个仓库：2,682 个旧条目定位到具体源码，316 个暂未定位文件的条目标注为「仓库入口」，10 个合集直链仓库。移除 54 个明确失效、已删除、空模板或名称损坏的条目；核对依据保存在 [upstream-links.json](data/upstream-links.json)。
- 按官方迁移记录更新 Figma、Lark 名称并合并重复条目。`catalog.json` 升级到 schema 2，用 `entries` 保留同一网址下的多个名称和用途。
- 贡献规则要求原始来源优先；CI 拦截重新加入的 skills.sh 资源链接。

Both READMEs, source documents and the machine catalog now link directly to author repositories, source files or official documentation. The audit covers 172 repositories: 2,682 old entries resolved to files, 316 are marked repository entries, and 10 collections link to repositories. Removed 54 unavailable, explicitly deleted, empty-template or malformed entries. Figma/Lark migrations follow upstream records. Catalog schema 2 preserves multiple named entries per URL, and CI rejects aggregator resource links.

## 2026-11-11 — Expanded catalog / 首页完整展开

- 中英文 README 展开职能、平台、创始人专题和扩展条目；目录锚点都留在当前页面，没有折叠清单。
- 新增 12 条经营路线，补齐付费服务试点、报价范围、回款、产能与外包、实物履约、订阅取消、资产迁移、AI 成本、恢复演练、离岗与退出交接。
- 新增 20 个经营工具与官方指南；工具、协议与技能分开说明，来源阅读与实际部署测试分开记录。
- 根据 [marketingskills v2 迁移表](https://github.com/coreyhaines31/marketingskills#full-rename-map)更新旧技能名，合并迁移后重复的条目。
- 修正软件接口契约、代码命名、员工解雇审查等用途错配；移除空白技能模板及已不可用的精选上游引用。
- `solo-founder-skills` 按[上游源码快照](https://github.com/whawkinsiv/solo-founder-skills/tree/01bd10f79a4b6a741be78e3184612a90ecbd54ef)保留当前 21 项技能，移除旧目录中已找不到的 50 项；删除没有出处的能力强弱比较与排他性宣传。
- 新增自动生成的 `catalog.json`、贡献说明和 CI：检查内容漂移、双语链接、完整展开、本地链接、锚点和 GitHub README 体积。
- 保留已确定的浅色头图和圆形精简工作流。

新增官方资源的用途已核对第一方文档；被修正的精选技能已检查相关上游内容。扩展索引未逐条完成安装或真实业务验证，HTTP 页面可达也不代表技能仍可安装。

### English

- Expanded all functional, platform, founder and supplementary collections in both READMEs, with same-page anchors and no collapsed lists.
- Added 12 operating playbooks and 20 tools/official guides for the work between the first paid pilot and reliable delivery, operations and handover.
- Migrated old marketingskills names, removed resulting duplicates, corrected misleading resource classifications and removed unavailable or empty selected resources.
- Matched `solo-founder-skills` to its [upstream source snapshot](https://github.com/whawkinsiv/solo-founder-skills/tree/01bd10f79a4b6a741be78e3184612a90ecbd54ef): retained the current 21 skills and removed 50 unavailable entries. Removed unsupported competitive rankings.
- Added a generated `catalog.json`, contributor instructions and CI for output drift, bilingual URLs, complete exposure, local links, anchors and README size.
- Preserved the approved light banner and simplified circular workflow artwork.

First-party descriptions were checked for the new operating resources, and relevant upstream content was inspected for corrected selected skills. The extended index has not been installed or tested in full; reachable pages alone do not establish installability.
