# Worked example: architecture and roadmap

## Target direction

- **Business:** a consistent reserve–pick–notify–collect value stream with controlled regional variants and explicit exception ownership.
- **Data:** governed product, location, stock, reservation, and customer-contact concepts; stewards and freshness measures.
- **Application:** reservation orchestration and notification services behind versioned interfaces, integrated with regional inventory sources.
- **Technology:** resilient event/API capability, observability, approved identity, and scalable runtime.

This is direction, not product selection. Evidence gathered in development and procurement refines Solution Building Blocks.

## Gap-to-work trace

| Gap | Requirement | Work package | Evidence |
|---|---|---|---|
| inconsistent availability meaning | one governed definition and quality threshold | data foundation | reconciliation report |
| no reservation orchestration | confirmation within two minutes | reservation service | performance/functional tests |
| variable store procedure | consistent controlled process | pilot operating model | observed pilot completion/adoption |
| limited operational insight | detect failures before promise breach | observability | alert exercise and service measures |

## Transition states

1. **Prove:** define semantics, test regional event feasibility, co-design store process.
2. **Pilot:** deploy services and controls to a diverse 10-store cohort; measure results.
3. **Expand:** remediate findings and reach 60 stores in waves.
4. **Scale:** approve later regional roadmap based on outcomes and fitness review.

## Governance

The Architecture Board approves common contracts and material exceptions. Regional architects govern compliant local realization. Compliance gates occur before pilot, before each scale wave, and after material change. Phase H monitors outcome drift, exceptions, regulation, and technology fitness.

## Reflection

What fact would invalidate this target? Which decision is centralized, and why? Which artifact would each stakeholder need? What new information would justify returning to Phase A rather than making a minor change?

