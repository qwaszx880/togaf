# Practitioner example: use supporting techniques together

[Back to theory: Supporting ADM work](../../02-practitioner/08-supporting-work.md)

## Situation

Northstar treats risk, readiness, capability maps, and value streams as separate workshop outputs. Leaders receive four documents that do not inform one decision.

## Start from stakeholder value

Value stream stage: **Collect the correct reserved product**. Desired outcome: customer completes pickup without substitution or delay.

## Connect the techniques

| Lens | Finding | Decision impact |
|---|---|---|
| Value stream | “prepare order” is where most failures occur | focus pilot measures and process design there |
| Capability | store fulfillment and inventory accuracy are weak | plan capability increments, not just an app release |
| Information mapping | staff use “on hand” while app needs “available to reserve” | govern definitions, ownership, transformation |
| Organization mapping | store manager owns labor; region owns inventory feed | assign actions and decision rights correctly |
| Readiness | peak-time staffing cannot absorb new picking task | change pilot timing/staffing and training |
| Risk/security | pickup fraud possible if identity evidence is weak | add proportionate verification/control requirement |

## Risk entry

**Risk:** unauthorized person collects an order. **Owner:** retail operations risk owner. **Response:** order token plus staff verification for higher-value items. **Evidence:** fraud simulation and pilot incidents. **Residual exposure:** explicitly assessed and accepted by authority.

The control affects the Business process, customer information, Application behavior, Technology logging, training, and measures. Risk is integrated into architecture rather than appended at the end.

## Try it first

Draw a six-box chain: value stage → capability → information → owner → risk/control → roadmap work package. If any arrow is unsupported, write the assumption to validate.

## Learner variation

Suppose customer research shows token verification causes abandonment. The architect should not silently remove the control. Reassess threat, alternatives, value impact, and residual risk with the accountable parties.
