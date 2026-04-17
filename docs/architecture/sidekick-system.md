# Sidekick System Architecture

## Purpose

Sidekick skills provide structured review and safety gates for work output at any phase — brainstorming, planning, design, architecture, or implementation. Each skill applies domain-specific evaluation criteria and produces structured output.

## Current Skills

### review-board

Multi-lens review gate for any phase of work. Classifies the work output, selects a panel of review lenses, applies each lens to produce a verdict (APPROVE / FLAG / BLOCK), and synthesizes a final recommendation (SHIP / SHIP WITH CONDITIONS / HOLD).

The Security lens includes secret scanning — inspecting work artifacts for hardcoded keys, tokens, passwords, and credentials.

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
