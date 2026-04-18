# writing-discipline Skill Design

**Date:** 2026-04-18
**Author:** Kaci Dyck

## Problem

Coding agents waste tokens and reduce readability by applying unnecessary formatting and decoration when writing docs, specs, plans, implementation instructions, and code comments. Common offenders: decorative dividers, nested bullet lists, bold overuse, and headers on content too short to need navigation. The output looks structured but the formatting carries no information — it just adds noise and token cost.

## Audience

Coding agents writing any prose for a human to read: documentation, specs, plans, implementation instructions, code comments.

## Goal

A proactive skill agents internalize before writing, so the first draft is already clean. Not a reactive editing pass.

## Approach

Option C: principle + quick reference.

One core principle ("signal over decoration") explained in plain English, followed by a compact banned-patterns table with acceptable alternatives, followed by short rules for when structure is actually earned.

## Core Principle

**Signal over decoration.** Signal is content that carries meaning. Decoration is formatting that makes something *look* structured without adding information. If removing a formatting element loses no information, remove it.

## Skill Design

**Name:** `writing-discipline`

**Routing description:** Triggers whenever an agent is about to write documentation, specs, plans, implementation instructions, or code comments — any prose intended for a human to read.

**Content sections:**

1. **Principle** — plain-English explanation of signal over decoration (2-3 sentences)
2. **Banned patterns table** — common offenders with acceptable alternatives:
   - Decorative dividers (`═══`, `---` used as decoration, `***`)
   - Nested bullet lists (more than one level deep)
   - Bold overuse (bolding non-critical words for visual weight)
   - Headers on short content (header + 1-2 lines = just write prose)
   - Redundant parenthetical labels ("(unchanged)", "(see above)", "(optional)")
   - Properties as sub-bullets when they fit on one line
3. **When structure is earned** — short rules for bullets, headers, bold, tables:
   - Bullets: 3+ genuinely parallel, discrete items with no natural prose flow
   - Headers: content long enough that a reader needs to navigate or skip sections
   - Bold: terms so critical that missing them breaks understanding
   - Tables: comparison across 2+ dimensions where the grid IS the content
   - IMPORTANT/NOTE callouts: genuinely critical information the reader must not miss

**Tone:** The skill must practice what it preaches — no decorative dividers, no nested bullets, no unnecessary headers.

## Out of Scope

- Prose quality rules (covered by `writing-clearly-and-concisely`)
- Before/after examples (adds length; the principle + table is sufficient)
- Commit message formatting (separate concern)

## Success Criteria

- Agents produce clean first drafts without decorative dividers, excessive nesting, or structure that carries no information
- The skill file itself is a model of the principle it teaches
