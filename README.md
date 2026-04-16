# Sidekick Skills

Structured review and safety gate skills for coding agent workflows.

## Skills

- `review-board`: multi-lens review gate that classifies changes, applies domain-specific lenses, and produces a verdict before finalization

## How It Works

After implementation is complete, invoke `review-board` to review the changed files. The skill:

1. Classifies the change (Feature, Architecture, Security, Performance, UX/Accessibility, AI/ML, Legal/Compliance, Agent, or Full).
2. Selects an ordered panel of review lenses based on the type.
3. Applies each lens and collects verdicts (APPROVE / FLAG / BLOCK).
4. Synthesizes a final recommendation: SHIP, SHIP WITH CONDITIONS, or HOLD.

The Security lens includes secret scanning — no separate secret-scanning step is needed.

## File Contracts

- `docs/review-board-report.schema.json`: schema defining the report structure
- `docs/examples/`: reference output examples
- `docs/skills-authoring.md`: authoring guide for new skills
- `docs/architecture/sidekick-system.md`: system architecture

## Rules

- No finalization when the review-board recommendation is HOLD.
- Future UI assets must use wire or outline-style SVG icons only.

## Validation

Run the repo validation with:

```text
Use Python 3 to run `tests/validate_sidekicks.py`.
```

The validation script checks:

- required skills and frontmatter
- contract schemas and example outputs
- workflow documentation
