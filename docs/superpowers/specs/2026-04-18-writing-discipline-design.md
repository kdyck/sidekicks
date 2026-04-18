# writing-discipline Skill Design

**Date:** 2026-04-18
**Author:** Kaci Dyck

## Problem

Coding agents waste tokens and reduce readability by applying unnecessary formatting and decoration when writing docs, specs, plans, implementation instructions, and code comments. The output looks structured but the formatting carries no information — it just adds noise and token cost.

## Audience

Coding agents writing any prose a human will read.

## Goal

A proactive skill agents internalize before writing, so the first draft is already clean. Not a reactive editing pass.

## Approach

One core principle ("signal over decoration") explained in plain English, followed by prose-form rules for what to avoid and when structure is actually earned. No tables — a table listing banned formatting is the irony the skill exists to prevent.

## Core Principle

**Signal over decoration.** Signal is content that carries meaning. Decoration is formatting that makes something look structured without adding information. If removing a formatting element loses no information, remove it.

## Skill Design

**Name:** `writing-discipline`

**Routing description:** Triggers whenever an agent is about to write any prose a human will read — documentation, specs, plans, implementation instructions, or code comments.

**Content:**

- Principle: plain-English explanation of signal over decoration (2-3 sentences)
- What to avoid: prose-form list of banned patterns — decorative dividers, nested bullets beyond one level, bold used for visual weight rather than critical terms, headers on content too short to need navigation, redundant parenthetical labels, properties as sub-bullets when they fit inline
- When structure is earned: bullets for 3+ genuinely parallel items with no natural prose flow; headers when content is long enough to need navigation; bold only for terms so critical that missing them breaks understanding; tables only when the grid IS the content (comparison across 2+ dimensions); IMPORTANT/NOTE callouts for genuinely critical information the reader must not miss

**Output section:** No structured output. This skill shapes how prose is written.

**Hard Stop section:** None. Guidance is internalized, not a gate.

**Tone:** The skill must be a model of the principle it teaches — written in prose, no decorative dividers, no unnecessary headers.

## Contract Discipline

Shipping this skill requires updating all of the following in the same commit:
- `skills/writing-discipline/SKILL.md`
- `tests/validate_sidekicks.py` — add `"writing-discipline"` to `skill_names`
- `README.md` — add entry under Workflow section
- `docs/architecture/sidekick-system.md` — add description under Current Skills

## Out of Scope

- Prose quality rules (covered by `writing-clearly-and-concisely`)
- Commit message formatting (separate concern)
- Before/after examples (the principle and rules are sufficient)

## Success Criteria

- Agents produce clean first drafts without decorative formatting that carries no information
- The skill file itself is a model of the principle it teaches
