# F1 — Core concepts

## Outcomes

You will be able to explain Enterprise Architecture (EA), distinguish architecture domains, describe the TOGAF document structure, and relate stakeholders, concerns, views, and viewpoints.

> **See it in practice:** [Scope a three-shop coffee enterprise](../examples/foundation/01-concepts-coffee-shop.md), then compare its four domains and stakeholder view with Northstar.

## The big idea

EA aligns enterprise change with strategy. It gives decision-makers coherent descriptions of the current situation, intended future situation, and governed route between them. TOGAF supplies a **method**, reusable **content concepts**, and guidance for building an **architecture capability**; it is not a finished architecture or a mandatory one-size process.

## Four architecture domains

| Domain | Focus | Northstar example question |
|---|---|---|
| Business | Strategy, governance, organization, processes | How should click-and-collect operate? |
| Data | Logical/physical data assets and management | What is the trusted inventory record? |
| Application | Applications and their interactions | Which services reserve store stock? |
| Technology | Infrastructure and platforms | What platform supports peak demand? |

“Information Systems Architecture” commonly covers Data and Application Architectures.

## Essential relationship

A **stakeholder** has one or more **concerns**. A **viewpoint** defines conventions for constructing and using a **view**. The view represents the architecture to address particular concerns. Think: audience → question → recipe → prepared presentation.

## Enterprise and scope

“Enterprise” means any collection of organizations with common goals; it can be a whole company, partnership, agency, or bounded division. Scope has four useful dimensions: breadth, depth, time period, and architecture domains. State boundaries explicitly to prevent invisible assumptions.

## Hands-on: scope Northstar

Northstar wants click-and-collect in 60 stores within nine months. Write one sentence for each scope dimension. Identify one stakeholder, two concerns, a suitable viewpoint, and the view it would create. Compare with the [worked case](../case-study/01-vision-and-scope.md).

## Knowledge check

1. Why is TOGAF not itself an enterprise architecture?
2. Which domain owns a canonical definition of “available inventory”?
3. A CFO asks how investment supports outcomes. Which is the concern, and which is the stakeholder?

**Answers:** 1. It is a framework/method and guidance used to create and govern organization-specific architecture. 2. Data, although other domains contribute. 3. The CFO is stakeholder; investment-to-outcome traceability is the concern.
