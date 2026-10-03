# Practitioner example: handle a late regulatory change

[Back to theory: Change Management](../../02-practitioner/06-change.md) · [Back to theory: Requirements Management](../../02-practitioner/07-requirements.md)

## Situation

Two weeks before pilot, a new rule requires explicit customer consent before sending collection notifications through a third-party channel. The roadmap is approved and testing is underway.

## Weak reactions

- Ignore it until after pilot: bypasses a legal requirement.
- Cancel the whole program: acts before impact/options analysis.
- Let a developer add a checkbox: assumes business, data, legal, and evidence impacts are trivial.

## Traceable response

1. Capture requirement `R-PRIV-07`, source, effective date, owner, measure, and affected concern.
2. Assess current reservation journey, customer-contact data, notification service, supplier, controls, tests, training, and roadmap.
3. Involve legal/privacy authority, product owner, business process owner, security, and delivery.
4. Compare options: first-party channel, consent capture, pilot scope adjustment, or schedule change.
5. Assess value, compliance, cost, risk, and dependency; obtain authorized decision.
6. Update architecture, requirements, contract, work packages, test evidence, and communications.
7. Monitor effectiveness and residual risk.

## Phase H classification

If the change affects only the notification interaction inside the accepted vision, bounded architecture work may suffice. If it invalidates the whole customer-contact strategy or target operating model, initiate a broader ADM cycle. “Late” does not determine classification; strategic scope and impact do.

## Try it first

Write a measurable requirement and acceptance evidence for consent.

**Possible answer:** “Before transmitting a collection notification to the third-party channel, the service shall verify an unexpired consent record for that customer, purpose, and channel; automated tests and an audit sample must show no transmission without a valid record.” Legal review must validate actual wording.

## Learner variation

If the rule takes effect six months after pilot, options change, but traceability and an authorized compliance roadmap are still necessary. A future date is not permission to ignore it.
