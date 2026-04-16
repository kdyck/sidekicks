# Sidekick Skills

Structured review and safety gate skills for coding agent workflows.

## Project Structure

```
skills/<skill-name>/SKILL.md   — one skill per directory
docs/architecture/              — system architecture docs
docs/examples/                  — reference output examples
docs/review-board-report.schema.json — report schema contract
docs/skills-authoring.md        — authoring guide for new skills
tests/validate_sidekicks.py     — repo validation script
```

## Current Skills

- **review-board**: multi-lens review gate that classifies changes, applies domain-specific lenses (Engineering, Architecture, Security, Performance, UX/Accessibility, AI/ML, Compliance, Finance, Agent Governance), and produces a verdict (SHIP / SHIP WITH CONDITIONS / HOLD)

## Rules

- No finalization when the review-board recommendation is HOLD
- All UI assets must use wire/outline-style SVG icons (Lucide, Feather, or Heroicons outline set)
- Skill instructions must be tool-agnostic, OS-neutral, and shell-neutral
- No shell-specific language (bash, powershell, npm, pytest, cargo, grep, rg) in skill files or authoring docs
- Prefer file contracts over hidden memory or implicit state

## Validation

Run `tests/validate_sidekicks.py` with Python 3 to validate the repo. It checks:

- required skills and frontmatter format (`name:` and `description: Use when ...`)
- contract schemas and example outputs
- workflow documentation references
- OS-neutral wording in skills and docs

## Contract Discipline

When adding or changing a skill:

1. Update any affected template, schema, or example file
2. Update `docs/architecture/sidekick-system.md` if workflow, interfaces, or responsibilities changed
3. Update `README.md` if the public skill inventory or usage contract changed
4. Keep mutable runtime state out of git
