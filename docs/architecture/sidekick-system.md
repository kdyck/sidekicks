# Sidekick System Architecture

## Purpose

Sidekick skills provide structured review and safety gates for work output at any phase — brainstorming, planning, design, architecture, or implementation. Skills apply domain-specific evaluation criteria; some produce structured output while others provide behavior-shaping guidance.

## Current Skills

### review-board

Multi-lens review gate for any phase of work. Classifies the work output, selects a panel of review lenses, applies each lens to produce a verdict (APPROVE / FLAG / BLOCK), and synthesizes a final recommendation (SHIP / SHIP WITH CONDITIONS / HOLD).

The Security lens includes secret scanning — inspecting work artifacts for hardcoded keys, tokens, passwords, and credentials.

### commit-often

Lightweight behavior-shaping skill. When loaded, instructs the agent to commit at natural stopping points during a session — subtask complete, test passes, context shifting to a different area, or before a risky structural change. Produces no structured output. Cadence is advisory; agent uses judgment unless the user specifies otherwise.

### writing-discipline

Proactive behavior-shaping skill. When loaded, instructs the agent to apply "signal over decoration" before writing any prose — documentation, specs, plans, implementation instructions, or code comments. Produces no structured output. No hard-stop condition; guidance is internalized, not a gate.

## Control Flow

1. Complete a phase of work (brainstorm, plan, design, or implementation).
2. `review-board` classifies the work output, applies the relevant lens panel, and produces a structured report and human-readable summary.
3. If the recommendation is HOLD, work stops until all BLOCKs are resolved.

## Contracts

- `docs/review-board-report.schema.json`: schema defining the report structure
- `docs/examples/`: reference output examples

## Hard Stops

The workflow must stop when:

- any review lens issues a BLOCK verdict
- the final recommendation is HOLD

## Compatibility Rules

- skill instructions are written in plain language, not tool-specific command sequences
- output format is defined by schema, not by prescribed file paths
- future architectural changes must update the relevant markdown docs in this repository
