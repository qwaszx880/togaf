# Foundation example: one customer promise through the ADM

[Back to theory: ADM fundamentals](../../01-foundation/02-adm-fundamentals.md)

## Situation

Northstar promises: “Reserve online and receive confirmation within two minutes.” Follow that single promise through the Architecture Development Method (ADM).

## Try it first

Write the ADM phases from memory. Next to each, write the decision that this promise would require.

## Walkthrough

| ADM part | Question about the promise | Example action/output |
|---|---|---|
| Preliminary | How will Northstar practice and govern architecture? | Establish regional decision rights, common modeling terms, principles, and Architecture Board mandate. |
| Phase A | Is this the right promise, for whom, within what boundary? | Agree 60-store scope, cancellation target, sponsor, risks, and authority to proceed. |
| Phase B | How must work and responsibility change? | Design reserve–pick–notify–collect flow and exception ownership. |
| Phase C | What information and application behavior enable it? | Define availability semantics and reservation/notification services. |
| Phase D | What platform qualities enable it? | Define resilient integration, identity, monitoring, and peak capacity. |
| Phase E | What coherent packages can deliver it? | Group data foundation, reservation service, store operating model, and observability work. |
| Phase F | In what sequence can it safely happen? | Put semantic alignment before integration; pilot before scale; allocate resources. |
| Phase G | Is implementation honoring the promise? | Review confirmation-time tests, approved controls, and deviations. |
| Phase H | Is the promise and architecture still fit? | Monitor cancellations, exceptions, new rules, and service behavior; trigger change when needed. |
| Requirements Management | What must remain traceable throughout? | Maintain the two-minute requirement, its source, architecture links, test evidence, and approved changes. |

## Why this is not a waterfall

During Phase C, the team discovers some stores cannot emit stock changes. That finding affects the Business Architecture promise and the Technology approach. The architects iterate across B, C, and D, update risk and requirements, and may revise the pilot scope in Phase A terms. Iteration is controlled learning, not restarting blindly.

## A useful memory model

**Prepare → agree → describe → group → plan → govern → adapt**, with requirements always connected. This memory model aids recall; use the proper phase names in exam answers.

## Learner variation

The sponsor reduces the pilot from 60 stores to 10 without changing the two-minute promise. Which work changes, and which must remain?

**Debrief:** breadth, roadmap, resources, and perhaps risk change. The outcome measure, required cross-domain reasoning, governance, and requirements traceability remain. A smaller scope does not justify skipping necessary domains.
