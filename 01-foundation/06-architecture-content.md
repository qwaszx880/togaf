# F6 — Architecture content

## Outcomes

Distinguish deliverables, artifacts, and building blocks; understand catalogs, matrices, diagrams, and the Content Metamodel.

> **See it in practice:** Classify the principle, building blocks, artifact, deliverable, and contract in [one governed exception](../examples/foundation/05-governance-and-content.md).

## Content hierarchy

| Term | Meaning | Example |
|---|---|---|
| Deliverable | Formally reviewed/approved contractual work product | Architecture Definition Document |
| Artifact | Description of an aspect of architecture; may be a catalog, matrix, or diagram | Application communication diagram |
| Building block | Potentially reusable package of capability | Customer identity service |

A deliverable may contain many artifacts. Artifacts describe building blocks. An **Architecture Building Block (ABB)** specifies required capability; a **Solution Building Block (SBB)** represents a component that implements capability. Avoid treating ABB as “logical diagram” and SBB as “product name” in every circumstance—the core distinction is requirement versus realization.

## Artifact forms

- **Catalog:** lists like kinds of things (actors, applications, requirements).
- **Matrix:** shows relationships between two or more kinds (roles to processes).
- **Diagram:** presents a visual slice for concerns (application communication).

The **Content Metamodel** defines entities, attributes, and relationships to keep architecture content consistent. Views select relevant material for stakeholder concerns.

## Hands-on: classify

Classify each: a signed Architecture Contract; a table of applications; a target “order orchestration capability”; a selected order platform; a matrix connecting data entities to applications. Then identify which might be embedded in a larger deliverable.

**Suggested answer:** deliverable; catalog artifact; ABB; SBB; matrix artifact. Any artifacts and building-block descriptions can appear within a deliverable.

## Knowledge check

1. Can one artifact occur in several deliverables? 2. ABB versus SBB? 3. Why use a metamodel?

**Answers:** 1. Yes, subject to configuration/control. 2. Required capability versus its realization. 3. Consistent structure, relationships, traceability, and reuse.
