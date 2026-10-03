# Foundation example: from symptoms to a safe migration

[Back to theory: ADM techniques](../../01-foundation/03-adm-techniques.md)

## Situation

Northstar knows cancellations are high but does not know whether the main cause is stale stock, inconsistent store work, or application failure. A leader asks for a technology roadmap immediately.

## Try it first

Choose and order four techniques. Explain what each contributes before a roadmap can be credible.

## Walkthrough

### 1. Business scenario frames the problem

The team records environment, actors, current behavior, desired outcomes, and initial requirements. It learns that staff sometimes sell an item after an online request but before picking it. The problem is wider than data latency.

### 2. Stakeholder management exposes different concerns

Customers need a trustworthy promise; managers need manageable workload; security needs minimal customer data; regions need controlled autonomy. These concerns determine viewpoints and acceptance evidence.

### 3. Gap analysis makes change explicit

| Baseline | Target | Gap treatment |
|---|---|---|
| hourly inventory copies | updates visible within 60 seconds | add event capability |
| informal phone hold | controlled reservation lifecycle | replace process and application behavior |
| local product codes | governed shared identifiers | harmonize and retain valid mappings |

### 4. Readiness and risk prevent a paper solution

Readiness interviews reveal seasonal staff receive little training. Risk analysis records adoption failure, owner, likelihood/impact, pilot training response, and a measure. A technically correct Target Architecture would still fail without this action.

### 5. Migration planning creates testable transitions

First prove data semantics and event feasibility; then pilot the entire value stream in ten stores; then expand in waves. Each state provides value or evidence and has entry/exit criteria.

## Why technique order matters

The techniques may overlap and iterate, but jumping straight to migration would turn an untested diagnosis into expensive commitments. Each step reduces a different uncertainty.

## Learner variation

Suppose analysis proves stock latency is already under 10 seconds, but cancellations remain high. Revise the gap list and roadmap.

**Debrief:** remove or downgrade the event gap. Investigate reservation locking, process, ownership, and customer behavior. Evidence should change the architecture; it should not be forced to justify a preferred platform.
