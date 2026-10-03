# Practitioner example: rank four plausible answers

[Back to theory: Scenario workshop](../../02-practitioner/09-scenario-workshop.md)

## Scenario

Northstar has completed target domain architectures. A pilot deadline is fixed. Gap analysis shows inconsistent product identifiers enable no reliable reservation service, while executives want the customer app released first for visibility. What should the architect recommend during migration planning?

**A.** Release the app first because visible value is the primary prioritization criterion.

**B.** Rank work using value, dependencies, risk, cost, and readiness; make identifier alignment an enabling increment and agree transition states with portfolio stakeholders.

**C.** Repeat all domain architecture work until executives stop requesting the app first.

**D.** Ask the application vendor to choose the project sequence because it knows its product.

## Pass 1: locate the question

“During migration planning” points to Phase F. Domain work and gaps already exist, so answers that restart without new evidence are suspicious.

## Pass 2: mark decisive evidence

- Fixed deadline is a constraint, not permission to ignore dependencies.
- Identifier inconsistency blocks reliable reservation.
- Executives care about visible value.
- The recommendation needs integrated prioritization and agreement.

## Pass 3: rank with BEST

| Rank | Choice | Reasoning |
|---:|:---:|---|
| 1 | B | balances business value with explicit dependency/risk and creates governed transition decisions |
| 2 | A | responds to executive value but ignores an enabling dependency and reliability |
| 3 | C | preserves architecture concern but is disproportionate; the given problem is migration priority, not missing domain work |
| 4 | D | outsources an enterprise portfolio decision to a product supplier and ignores stakeholders/dependencies |

Middle choices earn their rank for what they get partly right. Do not label every non-best response equally bad.

## Reference strategy

If uncertain, search the provided reference for Migration Planning objectives or prioritization factors. Do not browse whole chapters. The scenario already tells you the relevant phase.

## Try it first: change one fact

Suppose identifiers are already governed and the app can release independently with validated customer value. Re-rank.

**Debrief:** A becomes more plausible, but B may remain strongest because Phase F still considers the full set of factors and gains portfolio agreement. If A were rewritten to include those controls, its rank could change. Rank the actual wording, not an improved version imagined by you.
