[← Back to index](../../README.md) · [中文](../zh/operator-playbook.md)

# 12 operating playbooks for a one-person company

Start with the job that is currently blocked. These playbooks and completion checks are editorial suggestions for independent software, professional services, content products and small ecommerce businesses.

## 1. Turn a skill into a first paid service

Use this for consulting, design, research, automation setup or training before you have paying customers.

- **Deliverable**: A one-page offer covering the customer, output, required inputs, exclusions, schedule and price, with a sample of the work.
- **Completion check**: Find a customer willing to pay the agreed price, deliver a paid pilot with a clear acceptance result, then decide whether to sell it again. Track interviews and likes separately from payments.
- **Resources**: [first-customers](https://www.skills.sh/whawkinsiv/solo-founder-skills/first-customers) for finding paying customers individually; [proposal-writer](https://www.skills.sh/ncklrs/startup-os-skills/proposal-writer) for a service proposal; [Stripe Payment Links documentation](https://docs.stripe.com/payment-links) for collecting payment through a link.

## 2. Agree on scope and confirm changes

Use this when added requests make the original quote unprofitable.

- **Deliverable**: A quote and scope of work covering milestones, revision rounds, acceptance, payment dates, intellectual property ownership and a change log.
- **Completion check**: Both parties confirm the same version; added work has written agreement on price and timing. A quote does not replace other contract terms that need separate agreement.
- **Resources**: [proposal-writer](https://www.skills.sh/ncklrs/startup-os-skills/proposal-writer) includes commercial statements of work (SOWs); [ip-clause-review](https://www.skills.sh/anthropics/claude-for-legal/ip-clause-review) reviews intellectual property clauses; [Stripe Quotes documentation](https://docs.stripe.com/quotes) covers the quotation workflow.

## 3. Track collections, failed payments and refunds

Use this when payment status, remaining balances or refunds are buried in chat histories.

- **Deliverable**: An order and collection ledger separating pending, paid, failed, overdue and refunded amounts, with due dates, evidence and next actions.
- **Completion check**: Run a test payment, a failed-payment follow-up and a refund record. Reconcile processor settlements with bank receipts before treating order value as available cash.
- **Resources**: [payments](https://www.skills.sh/whawkinsiv/solo-founder-skills/payments) for payment integration; [revenue-leakage](https://www.skills.sh/mbfinotti/revops-skills/revenue-leakage) for investigating missed billing and renewal losses; [Stripe automatic collection documentation](https://docs.stripe.com/invoicing/automatic-collection) for handling failed payments.

## 4. Decide with cash and delivery costs

Use this when revenue is growing but you cannot tell how long cash will last or which orders are worth accepting.

- **Deliverable**: A rolling weekly cash forecast and order cost sheet covering receipt dates, fixed expenses, refunds, tax reserves, purchasing, contractors, payment fees, model usage and your delivery hours. Separate actuals from assumptions.
- **Completion check**: Reconcile one completed week, model delayed receipts, cancellations and higher costs, and record when to cut spending, raise prices or stop investing.
- **Resources**: [finances](https://www.skills.sh/whawkinsiv/solo-founder-skills/finances) for cash runway; [founder-cfo](https://www.skills.sh/jakeschincariol/founder-skill/founder-cfo) for per-unit costs and break-even analysis; [unit-economics](https://www.skills.sh/anthropics/financial-services/unit-economics) for customer economics in subscriptions or recurring services. Its investment-screening benchmarks do not apply to every small business.

## 5. Accept work and delegate within capacity

Use this when the same person sells, produces and supports the work, and overlapping projects cause delays.

- **Deliverable**: A weekly capacity plan, active-project list and delivery SOP with time reserved for support and rework. Contractor tasks specify inputs, examples, quality criteria, the reviewer and access permissions.
- **Completion check**: Calibrate estimates against one real delivery and confirm a start date before accepting another order. Have someone else complete one standard task from the instructions and pass review.
- **Resources**: [sop-creator](https://www.skills.sh/ognjengt/founder-skills/sop-creator) for repeatable business procedures; [to-tickets](https://www.skills.sh/mattpocock/skills/to-tickets) for splitting software development work into verifiable tasks and dependencies.

## 6. Test physical fulfillment and returns

Use this for small ecommerce businesses, custom goods or offline delivery, where product-page conversion is only one part of the job.

- **Deliverable**: Sample acceptance records, supplier lead times, purchasing and freight costs, an inventory ledger, reorder conditions, shipping and returns procedures.
- **Completion check**: Complete one order from purchasing to receipt, then rehearse an out-of-stock case or a return. Include loss, packaging, shipping and support in the order cost.
- **Resources**: [inventory-planner](https://www.skills.sh/anthropics/knowledge-work-plugins/inventory-planner) for estimating stockouts and reorders from sales and inventory records; [Shopify inventory and locations documentation](https://help.shopify.com/en/manual/inventory-and-locations) for inventory operations.

## 7. Make renewal and cancellation predictable

Use this for subscriptions, memberships and ongoing services where renewal depends on last-minute reminders.

- **Deliverable**: Customer outcome records, renewal dates, next-period deliverables, and cancellation, export and refund routes. Distinguish voluntary cancellation from failed payment.
- **Completion check**: Use a test customer to complete onboarding, a renewal reminder and cancellation. Confirm that subsequent billing and access follow the agreed rules.
- **Resources**: [onboarding-specialist](https://www.skills.sh/ncklrs/startup-os-skills/onboarding-specialist) for customer activation and delivery handoffs; [renewal-manager](https://www.skills.sh/ncklrs/startup-os-skills/renewal-manager) for renewal planning; [Stripe customer portal documentation](https://docs.stripe.com/customer-management) for subscription management and cancellation.

## 8. Keep portable content and customer records

Use this when a platform outage or account restriction would prevent you from reaching customers.

- **Deliverable**: A domain you control, source content, and exports of customer and subscription records, preserving consent, unsubscribe status and permitted use.
- **Completion check**: Import a test export into an alternative system and verify key fields. Record what the original platform did not export. Do not reactivate unsubscribed people during migration.
- **Resources**: [Ghost content and member export documentation](https://ghost.org/help/exports/). For other platforms, check the fields and files included in their exports.

## 9. Bound AI costs and prepare degraded service

Use this when model failures, quality changes or usage spikes can affect paying customers.

- **Deliverable**: Task-level usage costs, representative acceptance examples, request timeouts, retry limits, a backup model and a manual handling path.
- **Completion check**: Simulate a primary-provider failure and an over-budget request in a test environment. Confirm that fallback output still meets acceptance criteria and errors cannot trigger endless retries. LiteLLM budget enforcement needs a database; test that the configured limits actually apply.
- **Resources**: [LiteLLM fallback documentation](https://docs.litellm.ai/docs/proxy/reliability), [LiteLLM budgets and rate limits documentation](https://docs.litellm.ai/docs/proxy/users).

## 10. Restore a backup in practice

Use this when losing a database, files, orders or a device would stop the business.

- **Deliverable**: A critical-data inventory, backup locations, restoration steps, account-recovery methods and an incident notice template. Record acceptable data loss and recovery time separately.
- **Completion check**: Restore a backup to an isolated location, verify its data and usability, and measure the time taken. Confirm that a backup failure generates a notification instead of relying only on a successful job status.
- **Resources**: [restic restoration documentation](https://restic.readthedocs.io/en/stable/050_restore.html) for recovery practice; [incident-response](https://www.skills.sh/anthropics/knowledge-work-plugins/incident-response) for incident triage, communication and postmortems.

## 11. Plan for rest and temporary absence

Use this when work consumes all available time and even a short absence would interrupt delivery.

- **Deliverable**: Service hours, order limits, time off, an automatic reply and an emergency contact. List obligations that still need attention while new orders are paused.
- **Completion check**: Rehearse a planned absence. Check that customers can learn when to expect a response and that critical matters are handled. Emergency help receives only the access agreed in advance.
- **Resources**: [time-energy-management](https://www.skills.sh/refoundai/lenny-skills/time-energy-management) for scheduling time and energy; [grow-sustainably](https://www.skills.sh/slavingia/skills/grow-sustainably) for assessing the cash and energy demands of growth; [sop-creator](https://www.skills.sh/ognjengt/founder-skills/sop-creator) for instructions used during an absence.

## 12. Prepare a sale, license or shutdown handover

Use this when selling a product, licensing content, transferring a client project or ending a business activity.

- **Deliverable**: An asset and rights register covering code, domains, brands, content licenses, customer contracts, vendor accounts, outstanding obligations and transfer conditions. Include customer notices and data-handling arrangements.
- **Completion check**: The recipient independently completes a key task in a test environment, and both sides confirm the handover checklist and unresolved items. A shutdown also needs explicit arrangements for remaining delivery, refunds and data retention.
- **Resources**: [ip-clause-review](https://www.skills.sh/anthropics/claude-for-legal/ip-clause-review) for reviewing IP clauses in assignments or licenses; [GitHub repository transfer documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository) for code repository handover. Check each other platform's account-transfer rules separately.

Choose payment services for your business location, settlement currency and account eligibility; check contracts, tax and data obligations for the applicable jurisdiction. The SaaS products above are implementation examples. Official documentation links were checked on 2026-11-11; this does not establish regional availability or hands-on validation of every listed skill.
