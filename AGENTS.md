# Agents

Instructions for AI agents working in this repository.

## Skill Authoring

- Each skill lives in `skills/<skill-name>/SKILL.md` with required frontmatter:
  ```yaml
  ---
  name: skill-name
  description: Use when ...
  ---
  ```
- Descriptions state when the skill applies, not what it does
- Use tool-agnostic verbs: read, inspect, search, write, update, validate, record
- Never reference specific shells, package managers, or command flags in skill body

## Review Workflow

After completing a phase of work (brainstorming, planning, design, or implementation), invoke the `review-board` skill. It:

1. Classifies the change into one of: Feature, Architecture, Security, Performance, UX/Accessibility, AI/ML, Legal/Compliance, Agent, Full
2. Selects an ordered panel of review lenses
3. Applies each lens producing APPROVE / FLAG / BLOCK verdicts
4. Synthesizes a recommendation: SHIP, SHIP WITH CONDITIONS, or HOLD

**Hard stop**: Do not finalize or move forward when the recommendation is HOLD. Resolve all BLOCKs first.

## Output Contracts

- Review reports must conform to `docs/review-board-report.schema.json`
- Example outputs are in `docs/examples/`
- The Security lens includes secret scanning — no separate step needed

## Validation

Run `tests/validate_sidekicks.py` with Python 3 after making changes. All checks must pass before finalization.

## OS Neutrality

All documentation and skill files must avoid shell-specific or OS-specific language. The validation script enforces this by rejecting references to bash, powershell, npm, pytest, cargo, grep, rg, and similar.

## Icons

Any future UI assets must use wire/outline-style SVG icons only (Lucide, Feather, or Heroicons outline set).
