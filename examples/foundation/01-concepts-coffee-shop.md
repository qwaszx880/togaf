# Foundation example: from coffee shop to enterprise architecture

[Back to theory: Core concepts](../../01-foundation/01-concepts.md)

## Situation

A three-location coffee company introduces mobile ordering. Customers complain that the app accepts orders for pastries that a shop has sold out. The owner asks, “Can architecture really help with something this small?”

Yes. An **enterprise** can be any collection pursuing shared goals; it need not be a multinational company. Here the enterprise is the app team, shops, and shared operations involved in mobile fulfillment.

## Try it first

Before reading on, identify one question for each architecture domain, one stakeholder concern, and one useful view.

## Walkthrough: four domains, one promise

| Domain | Concrete question | Possible finding |
|---|---|---|
| Business | Who accepts, prepares, and resolves a mobile order? | Shops use different substitution processes. |
| Data | What does “available pastry” mean, and who owns it? | The app subtracts sales only every hour. |
| Application | Which software checks availability and accepts an order? | Ordering never requests a live stock check. |
| Technology | What runtime and network qualities support that interaction? | One shop has unreliable connectivity. |

The domains are different lenses on the same customer promise. “This is an app problem” would hide the process, meaning, and connectivity issues.

## Stakeholder → concern → viewpoint → view

- **Stakeholder:** shop manager.
- **Concern:** added work and what staff do when stock changes after acceptance.
- **Viewpoint:** conventions for showing roles, process steps, exception paths, and volumes.
- **View:** the actual mobile-order fulfillment diagram for this coffee company, annotated with peak volume and exceptions.

The viewpoint is the recipe; the view is the meal prepared for this concern. A technology topology would not adequately answer the manager’s operating concern.

## Scope without vagueness

| Dimension | Example boundary |
|---|---|
| Breadth | Three shops, central menu, ordering app, fulfillment process |
| Depth | Responsibilities, information, application interaction; not device configuration |
| Time | Four-week pilot and six-month target |
| Domains | All four, with lightweight Technology detail |

## What this teaches

Architecture connects decisions across boundaries. The value is not the number of diagrams; it is a consistent customer promise supported by aligned operations, information, applications, and technology.

## Learner variation

Suppose the app only shows a menu and never accepts payment or guarantees stock. Which domains still matter, and how would the concern and scope change?

**Debrief:** All domains may still matter, but the promise is weaker. Availability might become advisory, reducing real-time requirements and technology depth. Scope should follow the promised outcome, not a standard template.
