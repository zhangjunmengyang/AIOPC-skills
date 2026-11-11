[← Back to index](../../README.md) · [中文](../zh/operating-resources.md)

# Operating tools & official guides

Resources for payments, monitoring, recovery, support, migration and digital delivery after launch. Every link below points to a project's own repository or first-party documentation. Choose for the task at hand; this is not an installation checklist.

Sources reviewed: 2026-11-11. Official descriptions were checked; deployment and live-payment tests were not completed for every resource. Account eligibility, payout regions and fees depend on each payment or sales platform's current rules.

## Reliability & recovery

- **[Uptime Kuma](https://github.com/louislam/uptime-kuma)** — Self-host availability checks for HTTP, TCP, DNS and other services, with alerts and public status pages.
- **[Healthchecks.io](https://healthchecks.io/docs/)** — Monitor backups, reports and scheduled sync jobs; receive an alert when a job fails to report on time.
- **[restic restore guide](https://restic.readthedocs.io/en/stable/050_restore.html)** — Restore entire snapshots or selected files to a target directory and verify backups through an actual recovery.
- **[Sentry Alerts](https://docs.sentry.io/product/monitors-and-alerts/alerts/)** — Send notifications, create tickets or call webhooks using issue sources, triggers and filtering rules.

## Payments & subscriptions

- **[Stripe subscription events](https://docs.stripe.com/billing/subscriptions/webhooks)** — Handle failed payments, trial endings and subscription changes so product access follows the actual subscription state.
- **[Stripe Customer Portal](https://docs.stripe.com/customer-management)** — Let customers update billing details, payment methods and subscriptions through a self-service portal.
- **[RevenueCat](https://www.revenuecat.com/docs/welcome/overview)** — Manage in-app subscription status and entitlements, with paywalls and revenue analytics.
- **[Paddle Webhooks](https://developer.paddle.com/webhooks/)** — Receive completed purchases, renewals, upgrades, pauses and cancellations to update fulfillment and access.

## Accessibility & data protection

- **[W3C WAI Easy Checks](https://www.w3.org/WAI/test-evaluate/easy-checks/)** — Manually review keyboard focus, form labels, alternative text and contrast; these checks do not cover all accessibility requirements.
- **[axe-core](https://github.com/dequelabs/axe-core)** — Add automated accessibility checks to web tests while retaining manual review for issues the tool cannot determine.
- **[OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)** — Decide which events to log and how to exclude or handle tokens, passwords and sensitive personal data.

## Support & scheduling

- **[Chatwoot](https://www.chatwoot.com/features)** — Bring website chat, support email and other channels into one inbox for handling customer conversations.
- **[Cal.com](https://cal.com/scheduling)** — Offer booking slots for consultations, demos and delivery meetings while accounting for calendar conflicts and customer time zones.

## Export & migration

- **[PostgreSQL pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)** — Export a single database for migration or handover; handle global objects such as roles separately and design production backups independently.
- **[rclone](https://rclone.org/docs/)** — Copy, verify and migrate files between local and cloud storage; check destination-deletion behavior before using sync commands.
- **[Ghost data exports](https://ghost.org/help/exports/)** — Export publishing assets including content, members and themes; copy media separately for self-hosted sites.

## Digital products & distribution

- **[Gumroad creator help](https://gumroad.com/help)** — Find official instructions for publishing digital products, testing purchases, issuing refunds and managing memberships.
- **[itch.io creator guide](https://itch.io/docs/creators/getting-started)** — Create product pages for games, assets, books and soundtracks, upload deliverables and publish updates.
- **[Shopify Digital Products](https://help.shopify.com/en/manual/products/digital-service-product/digital-downloads)** — Sell files or content-access links through a Shopify store and manage delivery after purchase.
- **[listmonk](https://listmonk.app/)** — Self-host mailing lists and newsletters with subscriber segmentation and campaigns; configure a separate email delivery service.
