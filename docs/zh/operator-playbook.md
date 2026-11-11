[← 返回总览](../../README.zh.md) · [English](../en/operator-playbook.md)

# 一人公司的 12 条经营路线

从正在卡住的事情开始选资源。以下路线和完成条件是本仓库的编辑建议，适用于独立软件、专业服务、内容产品和小型电商。

## 1. 把专业能力卖成第一笔服务

适用：咨询、设计、研究、自动化搭建、培训等服务，还没有付费客户。

- **交付物**：一页服务说明，写清服务谁、交付什么、客户提供什么、不包含什么、时间和价格；附一份可展示的样例。
- **完成条件**：找到愿意按约付款的客户，完成一次有明确验收结果的付费试点，再判断是否重复销售。访谈和点赞单独记录，不当作付款。
- **资源**：[first-customers](https://www.skills.sh/whawkinsiv/solo-founder-skills/first-customers) 用于逐个寻找付费客户；[proposal-writer](https://www.skills.sh/ncklrs/startup-os-skills/proposal-writer) 用于服务提案；[Stripe Payment Links 官方指南](https://docs.stripe.com/payment-links) 用于收款链接。

## 2. 报价时约定范围，变更时重新确认

适用：客户频繁增加需求，原报价覆盖不了实际工作。

- **交付物**：报价与工作范围表，包含里程碑、修改次数、验收方式、付款节点、知识产权归属和变更记录。
- **完成条件**：双方确认同一版本；每次新增工作都有价格和交期的书面确认。报价单不能替代需要另行约定的合同条款。
- **资源**：[proposal-writer](https://www.skills.sh/ncklrs/startup-os-skills/proposal-writer) 包含商务工作说明书（SOW）；[ip-clause-review](https://www.skills.sh/anthropics/claude-for-legal/ip-clause-review) 用于知识产权条款审阅；[Stripe Quotes 官方指南](https://docs.stripe.com/quotes) 用于报价流程。

## 3. 把回款、失败支付和退款记清楚

适用：已经成交，但收款状态、尾款或退款处理混在聊天记录里。

- **交付物**：订单与回款台账，区分待付、已付、失败、逾期、退款；每项写明金额、到期日、凭证和下一步。
- **完成条件**：走通一次测试付款、失败支付跟进和退款记录；把平台结算金额与银行到账核对，避免把订单金额直接当作可用现金。
- **资源**：[payments](https://www.skills.sh/whawkinsiv/solo-founder-skills/payments) 用于支付接入；[revenue-leakage](https://www.skills.sh/mbfinotti/revops-skills/revenue-leakage) 用于排查漏收与续费流失；[Stripe 自动收款与重试](https://docs.stripe.com/invoicing/automatic-collection) 用于失败支付处理。

## 4. 用现金和交付成本决定下一步

适用：收入在增长，却不知道还能支撑多久、哪些订单值得继续接。

- **交付物**：按周滚动的现金表与订单成本表，列出到账时间、固定支出、退款、税费预留、采购、外包、支付手续费、模型调用和自己的交付工时；实际值与假设分开。
- **完成条件**：用已发生的一周核对一次，分别检查回款推迟、退单和成本上涨时的现金缺口，并写明何时降支出、提价或停止投入。
- **资源**：[finances](https://www.skills.sh/whawkinsiv/solo-founder-skills/finances) 用于测算现金能支撑多久；[founder-cfo](https://www.skills.sh/jakeschincariol/founder-skill/founder-cfo) 用于单笔成本与盈亏平衡；[unit-economics](https://www.skills.sh/anthropics/financial-services/unit-economics) 用于订阅或持续服务的客户经济分析，其投资评估指标不直接套用到所有小生意。

## 5. 按实际产能接单和外包

适用：同一人负责销售、制作和客服，项目一多就延期。

- **交付物**：一周产能表、在手项目表和交付 SOP，预留售后与返工时间；外包任务写清输入、样例、质量标准、验收人和权限范围。
- **完成条件**：用一次真实交付校准工时，确认新订单的开始日期；至少有一项标准任务能由他人按文档完成并通过验收。
- **资源**：[sop-creator](https://www.skills.sh/ognjengt/founder-skills/sop-creator) 用于可重复业务的操作文档；软件开发任务可用 [to-tickets](https://www.skills.sh/mattpocock/skills/to-tickets) 拆分可验收任务及依赖。

## 6. 实物生意先跑通履约和退货

适用：小型电商、定制商品或线下交付，不能只检查商品页转化。

- **交付物**：样品验收记录、供应商交期、采购与运费成本、库存台账、补货条件、发货和退换货流程。
- **完成条件**：走完一单从采购到签收的流程，再演练缺货或退货；将损耗、包装、运费和售后计入订单成本。
- **资源**：[inventory-planner](https://www.skills.sh/anthropics/knowledge-work-plugins/inventory-planner) 用于按销售与库存记录估算缺货及补货；[Shopify 库存与库位官方指南](https://help.shopify.com/en/manual/inventory-and-locations) 用于库存操作。

## 7. 让续费和退出都有明确流程

适用：订阅、会员、长期服务已经有人使用，续费只靠临时提醒。

- **交付物**：客户结果记录、续费日期、下期交付内容，以及取消、导出和退款入口；区分主动取消与支付失败。
- **完成条件**：用测试客户走通首次使用、续费提醒和取消流程；取消后账单及访问权限按已约定规则变化。
- **资源**：[onboarding-specialist](https://www.skills.sh/ncklrs/startup-os-skills/onboarding-specialist) 用于客户启用与交付衔接；[renewal-manager](https://www.skills.sh/ncklrs/startup-os-skills/renewal-manager) 用于续费计划；[Stripe 客户门户官方指南](https://docs.stripe.com/customer-management) 用于订阅管理与取消。

## 8. 保留能迁移的内容和客户记录

适用：收入依赖单个平台，平台停服或账号受限就无法继续联系客户。

- **交付物**：自己控制的域名、内容源文件、客户和订阅记录的导出副本；保留订阅同意、退订状态及使用范围。
- **完成条件**：将一份测试导出导入替代系统，核对关键字段；记录原平台没有导出的内容。迁移名单时不重新激活已退订的人。
- **资源**：[Ghost 内容与会员导出官方指南](https://ghost.org/help/exports/)。使用其他平台时，对照检查其导出字段和文件范围。

## 9. 管住 AI 成本，并准备服务降级

适用：产品或交付依赖模型 API，调用失败、质量变化或用量上涨会直接影响客户。

- **交付物**：按任务记录调用成本的小账本、代表性验收样例、请求超时与重试上限、替代模型和人工处理路径。
- **完成条件**：在测试环境模拟主供应商失败和超预算请求，确认降级后的结果仍满足验收要求，且异常不会无限重试。LiteLLM 的预算控制需要数据库支持，应实际验证配置生效。
- **资源**：[LiteLLM 故障切换官方指南](https://docs.litellm.ai/docs/proxy/reliability)、[LiteLLM 预算与限流官方指南](https://docs.litellm.ai/docs/proxy/users)。

## 10. 备份之后，实际恢复一次

适用：数据库、素材、订单或设备损坏会让业务停摆。

- **交付物**：关键数据清单、备份位置、恢复步骤、账号恢复方式和故障通知模板，分别记录可接受的数据损失与恢复时间。
- **完成条件**：在隔离位置恢复一份备份，核对数据和打开方式，记录真实耗时；确认备份失败时能收到通知，而不只检查任务显示成功。
- **资源**：[restic 恢复官方指南](https://restic.readthedocs.io/en/stable/050_restore.html) 用于恢复演练；[incident-response](https://www.skills.sh/anthropics/knowledge-work-plugins/incident-response) 用于故障分级、通知与复盘。

## 11. 为休息和临时离岗预留安排

适用：工作持续占满所有时间，创始人短暂离开就无法交付。

- **交付物**：明确服务时段、接单上限、休息时间、自动回复和紧急联系人；列出暂停新订单时仍必须履行的事项。
- **完成条件**：安排一次计划内离岗，检查客户能否获知响应时间、关键事项是否有人处理；应急协助只授予事先约定的权限。
- **资源**：[time-energy-management](https://www.skills.sh/refoundai/lenny-skills/time-energy-management) 用于时间与精力安排；[grow-sustainably](https://www.skills.sh/slavingia/skills/grow-sustainably) 用于评估扩张对资金与精力的消耗；[sop-creator](https://www.skills.sh/ognjengt/founder-skills/sop-creator) 用于离岗期间的操作说明。

## 12. 出售、授权或停止时能交接清楚

适用：准备出售产品、授权内容、转交客户项目，或结束一项业务。

- **交付物**：资产与权利清单，逐项记录代码、域名、品牌、内容授权、客户合同、供应商账户、未履行义务和可转移条件；另列客户通知与数据处理安排。
- **完成条件**：接手人能在测试环境独立完成一次关键操作，双方确认交接清单和未结事项。停止经营也要明确剩余交付、退款及数据保留安排。
- **资源**：[ip-clause-review](https://www.skills.sh/anthropics/claude-for-legal/ip-clause-review) 用于转让或授权中的知识产权条款审阅；[GitHub 仓库转移官方指南](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository) 用于代码仓库交接。其他账户按各平台的转移规则逐项确认。

支付产品按经营主体所在地、结算币种和平台资格选择；合同、税务与数据义务按适用地区核对。上面的 SaaS 产品是操作示例，官方文档链接核对于 2026-11-11，不代表所有地区均可开通，也不代表所列技能已逐项实测。
