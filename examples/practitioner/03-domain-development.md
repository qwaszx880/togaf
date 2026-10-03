# Practitioner example: trace one promise across Phases B–D

[Back to theory: Architecture development](../../02-practitioner/04-development.md)

## Situation

The requirement is: “For 99.5% of accepted reservations during trading hours, the customer receives confirmation within two minutes.”

## Trace the promise

| Domain | Baseline evidence | Target decision | Gap | Validation |
|---|---|---|---|---|
| Business | staff notice phone holds inconsistently | assign pick task and exception owner | standard workflow/training absent | timed store simulation |
| Data | “available” ignores unpicked sales | governed available-to-reserve rule | semantics and stewardship absent | reconciliation/quality test |
| Application | web cannot hold store stock | reservation lifecycle and notification services | service interactions absent | end-to-end acceptance test |
| Technology | hourly batch; limited monitoring | event/API runtime with service measures | latency, resilience, observability | peak/load/failure test |

No single row satisfies the requirement. The business workflow must act before the promise expires; information must be trustworthy; applications must coordinate state; technology must perform and expose failure.

## Iteration caused by evidence

Technology analysis finds 15 stores cannot publish events. Options include exclude them, add an adapter, or use a conservative stock buffer. Architects return to Business and Data decisions to compare customer value, operational effort, and data confidence. The result updates scope or target—not just Technology documentation.

## Avoid over-modeling

The decision needs current latency, interface feasibility, ownership, and quality. It does not require documenting every store server. Baseline depth follows decision need.

## Try it first

Add a security requirement: “Only authorized store staff can mark an order collected.” Trace one impact through all four domains.

**Possible path:** Business defines accountable role; Data records collection/audit event; Application enforces role and lifecycle; Technology supplies identity and protected logging.

## Learner variation

If confirmation changes from two minutes to two hours, reassess—not automatically remove—the event platform. The relaxed quality may permit simpler options, but cancellation and concurrency evidence still matter.
