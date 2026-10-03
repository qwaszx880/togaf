# P7 — Requirements Management

## Outcomes

Operate requirements as a continuous, traceable process and handle conflicts and changes.

> **See it in practice:** Follow a privacy requirement [from new rule through impact, decision, architecture, and acceptance evidence](../examples/practitioner/05-change-and-requirements.md).

Requirements are inputs to and outputs from every ADM phase. A practical lifecycle is identify → baseline → prioritize → trace → communicate → validate → manage change → dispose/archive. The repository needs identifiers, source, rationale, priority, owner, acceptance measure, status, dependencies, and links to architecture and implementation.

| Weak statement | Improved requirement |
|---|---|
| “Inventory must be fast.” | Availability updates for pilot stores shall be visible to reservation decisions within 60 seconds for 99.5% of updates during trading hours. |
| “The system is secure.” | Reservation access shall use approved customer authentication and log privileged access according to the control baseline. |

When requirements conflict, expose the trade-off to accountable stakeholders. Do not silently weaken one. Assess implications across domains, risks, and outcomes; record the decision and update traceability.

## Exercise

Use the [requirements register](../case-study/templates/requirements-register.md). Write five measurable requirements; trace each to concern, architecture element, work package, and acceptance evidence. Submit one change request and analyze its impact.

## Check

**Scenario:** A late legal requirement conflicts with time-to-market. Best response? **Answer:** record and analyze it, involve legal and accountable decision-makers, examine compliant options and roadmap impacts, approve the decision through governance, and maintain traceability.
