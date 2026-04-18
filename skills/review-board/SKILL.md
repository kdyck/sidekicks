---
name: review-board
description: Use when any phase of work is done — brainstorm, plan, design, architecture decision, or implementation — before moving to the next phase
---

# Review Board

## Overview

Single-pass multi-lens review of completed work output at any phase — brainstorming, planning, design, architecture, or implementation. Classifies the work, selects an ordered panel of review lenses, applies each lens to produce a verdict, then synthesizes a final recommendation.

## Inputs

- work artifact: brainstorm output, plan, design doc, architecture decision, spec, or changed files
- task description or acceptance criteria

## Step 1: Classify

Inspect the work artifact and task context. Select the single best-fit review type:

| Type | When |
|---|---|
| Feature | New user-facing capability, flow, or interaction |
| Architecture | Structural change, service boundary, data model redesign |
| Security | Auth, encryption, secrets, input handling, dependency changes |
| Performance | Latency-sensitive path, caching, query optimization, load change |
| UX/Accessibility | UI change, interaction pattern, WCAG concern, error/empty states |
| AI/ML | Model selection, prompt design, eval coverage, cost, hallucination risk |
| Legal/Compliance | Data handling, privacy, licensing, terms of service, retention |
| Agent | Multi-agent coordination, handoff protocols, domain ownership, agent drift |
| Full | Cross-cutting change touching 3+ types, or explicitly requested |

If three or more types apply equally, select Full. Record the rationale.

## Step 2: Select Panel

Each review type maps to an ordered panel of lenses:

| Type | Panel |
|---|---|
| Feature | Engineering, UX/Accessibility, Security, Performance, Finance |
| Architecture | Architecture, Engineering, Security, Performance, Finance |
| Security | Security, Engineering, Architecture, Compliance |
| Performance | Performance, Engineering, Architecture, Security, Finance |
| UX/Accessibility | UX/Accessibility, Engineering, Security, Performance |
| AI/ML | AI/ML, Engineering, Security, Finance, Performance |
| Legal/Compliance | Compliance, Security, Engineering, Architecture, Finance |
| Agent | Agent Governance, Engineering, Architecture, Security |
| Full | Engineering, Architecture, Security, Performance, UX/Accessibility, AI/ML, Compliance, Finance, Agent Governance |

## Step 3: Apply Each Lens

If subagents are available, dispatch one per selected lens and run them in parallel. Only dispatch lenses from the selected panel — do not spin up lenses not in the panel. If subagents are unavailable, apply each lens in order within the current session.

For each lens, inspect the work artifact and produce:

- **verdict**: APPROVE, FLAG, or BLOCK
- **assessment**: concise evaluation of what was reviewed and what is adequate
- **concerns**: specific issues with file paths and lines when possible (empty if APPROVE)
- **handoffs**: topics the next lens should pay attention to

### Lens Criteria

**Engineering** — correctness, error handling, edge cases, testability, dependency hygiene, API contract stability

**Architecture** — separation of concerns, coupling, scalability, data flow, migration safety, backward compatibility

**Security** — authentication, authorization, input validation, injection vectors, secrets and credential exposure, dependency vulnerabilities, encryption at rest and in transit. Scan work artifacts for hardcoded keys, tokens, passwords, API secrets, and connection strings.

**Performance** — response time impact, resource consumption, caching strategy, query complexity, concurrency safety

**UX/Accessibility** — interaction clarity, error/empty/loading states, WCAG AA compliance, keyboard navigation, screen reader support

**AI/ML** — model necessity, prompt quality, eval coverage, cost proportionality, hallucination guardrails, fallback behavior

**Compliance** — data privacy patterns (GDPR/CCPA), licensing, terms of service alignment, retention policy, audit trail

**Finance** — infrastructure and service cost impact, API/model cost proportionality, budget alignment, pricing implications, resource allocation efficiency

**Agent Governance** — multi-agent domain ownership clarity, handoff protocol compliance, context preservation across agent boundaries, agent drift detection, conflict resolution between overlapping agent responsibilities

## Step 4: Synthesize

Collect verdicts into a summary:

- **blockers**: all BLOCK verdicts with lens, concern, and required action
- **flags**: all FLAG verdicts with lens, concern, and recommended action
- **approvals**: all APPROVE verdicts with lens
- **unresolved handoffs**: topics handed off but never addressed by a subsequent lens

Final recommendation:

- **HOLD** if any BLOCK exists
- **SHIP WITH CONDITIONS** if any FLAG exists and no BLOCK
- **SHIP** if all lenses APPROVE

## Output

Produce a structured report conforming to `docs/review-board-report.schema.json` and a human-readable summary. See `docs/examples/` for reference output.

## Hard Stop

Block finalization if the recommendation is HOLD. Work must not move forward until all BLOCKs are resolved.

## Rules

- Evaluate only the submitted work artifact and its immediate contracts
- Do not speculate about work not inspected
- Each lens must cite specific files, lines, or sections when raising concerns
- Keep assessments factual and deterministic
- The Security lens must scan for hardcoded secrets as part of its evaluation
