[← 返回总览](../../README.zh.md) · [English](../en/operating-resources.md)

# 经营工具与官方指南

补齐上线后的收款、监控、恢复、客服、迁移和数字产品交付。以下链接均为项目官方仓库或第一方文档；按当前任务选用，不需要全部安装。

来源核对：2026-11-11。已核对官方用途说明，未逐项完成部署或真实收款测试。支付与销售平台的开户资格、结算地区和费用，以各平台当前规则为准。

## 可靠运行与恢复

- **[Uptime Kuma](https://github.com/louislam/uptime-kuma)** — 自托管 HTTP、TCP、DNS 等可用性监控，配置告警并发布服务状态页。
- **[Healthchecks.io](https://healthchecks.io/docs/)** — 监控备份、报表和定时同步任务；任务未按时回报时发出告警。
- **[restic 恢复指南](https://restic.readthedocs.io/en/stable/050_restore.html)** — 从快照恢复全部或指定文件到目标目录，用实际恢复结果检验备份。
- **[Sentry Alerts](https://docs.sentry.io/product/monitors-and-alerts/alerts/)** — 按应用问题、触发条件和过滤规则发送通知、创建工单或调用 webhook。

## 收款与订阅

- **[Stripe 订阅事件](https://docs.stripe.com/billing/subscriptions/webhooks)** — 处理付款失败、试用结束和订阅状态变化，让产品访问权限与实际订阅状态保持一致。
- **[Stripe Customer Portal](https://docs.stripe.com/customer-management)** — 提供客户自助入口，更新账单信息、支付方式和订阅，减少人工客服操作。
- **[RevenueCat](https://www.revenuecat.com/docs/welcome/overview)** — 管理应用内购买的订阅状态与用户权益，并接入付费墙和收入分析。
- **[Paddle Webhooks](https://developer.paddle.com/webhooks/)** — 接收购买完成、续费、升级、暂停和取消等事件，更新交付与访问权限。

## 无障碍与数据保护

- **[W3C WAI Easy Checks](https://www.w3.org/WAI/test-evaluate/easy-checks/)** — 对键盘焦点、表单标签、替代文本和对比度做人工初筛；这套检查不覆盖全部无障碍要求。
- **[axe-core](https://github.com/dequelabs/axe-core)** — 将自动无障碍检查接入网页测试，同时保留工具无法判断部分的人工检查。
- **[OWASP 日志指南](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)** — 确定日志应记录的事件，以及如何排除或处理令牌、口令和敏感个人数据。

## 客服与预约

- **[Chatwoot](https://www.chatwoot.com/features)** — 将网站聊天、客服邮件等渠道汇入同一收件箱，统一处理客户会话。
- **[Cal.com](https://cal.com/scheduling)** — 为咨询、演示和交付会议开放可预约时段，结合日历冲突和客户时区安排预约。

## 导出与迁移

- **[PostgreSQL pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)** — 为迁移或交接导出单个数据库；角色等全局对象需另行处理，生产备份方案需单独设计。
- **[rclone](https://rclone.org/docs/)** — 在本地与云存储之间复制、校验和迁移文件；使用同步命令前核对目标端删除行为。
- **[Ghost 数据导出](https://ghost.org/help/exports/)** — 导出内容、会员和主题等出版资产；自托管站的媒体文件需另行复制。

## 数字产品与内容分发

- **[Gumroad 创作者帮助](https://gumroad.com/help)** — 查询数字商品上架、测试购买、退款和会员管理的官方操作说明。
- **[itch.io 创作者入门](https://itch.io/docs/creators/getting-started)** — 为游戏、素材、书籍和音轨建立商品页，上传交付文件并发布更新。
- **[Shopify Digital Products](https://help.shopify.com/en/manual/products/digital-service-product/digital-downloads)** — 在 Shopify 店铺销售文件或内容访问链接，并管理购买后的数字交付。
- **[listmonk](https://listmonk.app/)** — 自托管邮件名单与 newsletter，管理订阅分组和邮件活动；邮件发送服务需另行配置。
