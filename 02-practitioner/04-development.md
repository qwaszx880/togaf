# P4 — Architecture development: Phases B, C, and D

## Outcomes

Develop proportionate Baseline and Target domain architectures, perform gap analysis, and reconcile cross-domain dependencies.

> **See it in practice:** Trace a [two-minute customer promise across Business, Data, Application, and Technology](../examples/practitioner/03-domain-development.md).

Use a repeatable pattern for each domain:

1. Select reference material, viewpoints, and tools.
2. Develop Baseline only to the detail needed for decisions.
3. Develop a Target aligned to requirements and principles.
4. Analyze gaps and impacts.
5. Resolve issues across domains and validate with stakeholders.
6. Update roadmap candidates, requirements, risks, and definition content.

| Domain | Northstar Baseline | Target direction | Example gap |
|---|---|---|---|
| Business | manual phone reservations | consistent reserve/pick/notify flow | pickup exception process |
| Data | stock copied nightly | governed availability data | event timeliness/ownership |
| Application | separate web and store tools | orchestrated order and inventory services | reservation interface |
| Technology | fixed-capacity integration | resilient observable platform | event platform capability |

Completeness is fitness for purpose, not maximum detail. Reconcile dependencies: a business promise depends on data quality, application behavior, and technology service levels.

## Exercise

Use the [gap-analysis template](../case-study/templates/gap-analysis.md). Add at least one retained, new, and removed element in each domain. Link each gap to a requirement and candidate work package.

## Check

**Scenario:** The architect fully models Technology before the target business process is agreed. Better action? **Answer:** establish sufficient Business Architecture and iterate across dependent domains; do not lock enabling technology prematurely.
