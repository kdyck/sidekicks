# Sidekick Skills

A collection of structured review and safety gate skills for coding agent workflows. Sidekicks don't write your code — they review it after you're done, catching what you missed before it ships.

## How It Works

When your implementation is complete, invoke a sidekick skill to review the changed files. The skill doesn't just skim your diff — it classifies the change, assembles the right panel of reviewers, and applies each lens independently before synthesizing a final recommendation.

The workflow is simple:

1. You finish your work.
2. The sidekick classifies what kind of change it is.
3. A panel of domain-specific lenses inspects the change.
4. Each lens produces a verdict: **APPROVE**, **FLAG**, or **BLOCK**.
5. A final recommendation is synthesized: **SHIP**, **SHIP WITH CONDITIONS**, or **HOLD**.
6. If the recommendation is HOLD, work stops until all blockers are resolved.

No change ships with an unresolved BLOCK.

## Installation

Clone the repository:

```text
git clone https://github.com/kdyck/sidekicks.git
```

Or add it as a submodule in an existing project:

```text
git submodule add https://github.com/kdyck/sidekicks.git sidekicks
```

That's it. No dependencies beyond Python 3 (for the validation script).

## What's Inside

### Review

- **review-board** — Multi-lens review gate. Classifies changes into one of nine types (Feature, Architecture, Security, Performance, UX/Accessibility, AI/ML, Legal/Compliance, Agent, or Full), selects an ordered panel of review lenses, and produces a structured report with a final recommendation. The Security lens includes secret scanning — no separate step needed.

### Lenses

The review-board selects from these lenses based on the change type:

- **Engineering** — correctness, error handling, edge cases, testability, dependency hygiene
- **Architecture** — separation of concerns, coupling, scalability, migration safety
- **Security** — auth, input validation, injection vectors, secrets and credential exposure
- **Performance** — response time, resource consumption, caching, query complexity
- **UX/Accessibility** — interaction clarity, WCAG AA compliance, error/empty/loading states
- **AI/ML** — model necessity, prompt quality, eval coverage, cost proportionality
- **Compliance** — data privacy (GDPR/CCPA), licensing, retention policy, audit trail
- **Finance** — infrastructure cost, API/model cost proportionality, budget alignment
- **Agent Governance** — domain ownership, handoff protocols, agent drift detection

## File Contracts

Every skill defines its inputs, outputs, and hard-stop conditions. The contracts are documented, schema-validated, and backed by example output:

- `docs/review-board-report.schema.json` — schema defining the structured report
- `docs/examples/` — reference report and summary output
- `docs/skills-authoring.md` — authoring guide for writing new skills
- `docs/architecture/sidekick-system.md` — system architecture and control flow

## Writing New Skills

Each skill lives in `skills/<skill-name>/SKILL.md` with YAML frontmatter. Skills must be tool-agnostic, OS-neutral, and deterministic. See `docs/skills-authoring.md` for the full authoring guide.

## Validation

Run the repo validation with Python 3:

```text
python tests/validate_sidekicks.py
```

The validation script checks:

- required skills exist with correct frontmatter
- contract schemas and example outputs are present and valid
- workflow documentation is complete
- all skill and doc files are OS-neutral (no shell-specific language)

## Rules

- No finalization when the review-board recommendation is HOLD.
- All UI assets must use wire or outline-style SVG icons only (Lucide, Feather, or Heroicons outline set).
- Skill instructions must stay tool-agnostic and OS-neutral.

## License

MIT
