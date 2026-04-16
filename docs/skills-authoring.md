# Sidekick Authoring Guide

## Skill Format

Each sidekick skill lives in `skills/<skill-name>/SKILL.md`.

Required frontmatter:

```yaml
---
name: skill-name
description: Use when ...
---
```

Descriptions should describe when the skill applies, not summarize the workflow.

## Writing Rules

- keep instructions tool-agnostic and deterministic
- keep language OS-neutral and shell-neutral
- define required inputs, outputs, and hard-stop conditions
- prefer file contracts over hidden memory or implicit state
- keep one skill per directory with a single `SKILL.md`

Prefer verbs like:

- read
- inspect
- search
- write
- update
- validate
- record

Avoid naming shells, package managers, or command flags in the skill body unless the skill is explicitly about a specific tool.

## Contract Discipline

When adding or changing a skill:

1. update any affected template, schema, or example file
2. update the architecture docs if the workflow, interfaces, or responsibilities changed
3. update `README.md` if the public skill inventory or usage contract changed
4. keep mutable runtime state out of git
5. if the skill emits an artifact, document the exact per-run output path

For mutable execution outputs, prefer `runs/<runId>/...` over tracked documentation directories.

## Asset Rule

If the skill system later adds UI assets, use wire or outline-style SVG icons only, consistent with Lucide, Feather, or Heroicons outline sets.

## Validation

Execute the repository validation script at `tests/validate_sidekicks.py` using Python 3.

The validation script is the baseline repo check for skill presence, frontmatter, workflow docs, contract artifacts, and OS-neutral wording.
