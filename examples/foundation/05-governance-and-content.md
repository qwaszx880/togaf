# Foundation example: from principle to governed exception

[Back to theory: Architecture governance](../../01-foundation/05-governance.md) · [Back to theory: Architecture content](../../01-foundation/06-architecture-content.md)

## Situation

Northstar has an architecture principle: **Shared customer-facing services must be observable against their service objectives.** A regional delivery team says the approved monitoring component cannot support its older store platform before the pilot.

## Content in plain language

| Item | Example | Why it is that type |
|---|---|---|
| Principle | observable shared services | enduring decision guidance |
| Architecture Building Block (ABB) | operational-observability capability with alerting and measures | states required capability |
| Solution Building Block (SBB) | selected monitoring agent and hosted dashboard | realizes capability |
| Artifact | service-to-measure matrix | describes relationships |
| Deliverable | approved Architecture Definition Document containing target views and matrix | formal reviewed package |
| Contract | pilot Architecture Contract | agrees responsibilities and evidence |

## A governable exception

1. The team records the incompatible platform, affected service objective, alternatives, delivery impact, and risk.
2. The architect checks whether a different Solution Building Block can satisfy the ABB and principle.
3. Operations and the accountable risk owner assess a temporary log-forwarding control.
4. The Architecture Board approves a time-bound exception for ten pilot stores, with expiry, owner, monitoring measure, and replacement work package.
5. The repository stores the decision and links it to affected requirements, roadmap, and compliance review.

The board did not waive the principle casually. It preserved its intent with a temporary control and explicit debt. Nor did it insist on a specific SBB when another realization could satisfy the ABB.

## Try it first

Rank these responses: secretly disable monitoring; delay everything indefinitely; assess an alternative realization and govern residual risk; rename the requirement so implementation appears compliant.

**Debrief:** governed alternative is best. Indefinite delay at least avoids silent risk but is disproportionate without options analysis. Renaming hides non-conformance. Secret disabling is worst.

## Learner variation

The workaround cannot detect customer-data leakage. Would the same exception remain reasonable?

**Debrief:** likely not. Changed impact and control effectiveness change risk acceptance. Escalate to the right security/risk authority and explore scope, schedule, or solution alternatives.
