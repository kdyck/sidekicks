# Sidekick Skills

Your personal review board for coding agent workflows. Sidekicks review your work at any phase — brainstorming, planning, design, or implementation — catching gaps before you move forward.

## How It Works

When you finish a phase of work, invoke a sidekick skill to review the output. It doesn't matter if the output is a brainstorm, a plan, an architecture decision, or a code change — the review board adapts.

1. You complete a phase of work.
2. The sidekick classifies what kind of work it is.
3. A panel of domain-specific lenses reviews the output.
4. Each lens produces a verdict: **APPROVE**, **FLAG**, or **BLOCK**.
5. A final recommendation is synthesized: **SHIP**, **SHIP WITH CONDITIONS**, or **HOLD**.
6. If the recommendation is HOLD, work stops until all blockers are resolved.

No work moves forward with an unresolved BLOCK.

## Installation

### Claude Code

```text
/install-github-skill kdyck/sidekicks
```

### GitHub Copilot CLI

```text
copilot plugin install kdyck/sidekicks
```

### Gemini CLI

```text
gemini extensions install https://github.com/kdyck/sidekicks
```

### OpenAI Codex CLI

```text
codex /plugins
```

Search for "sidekicks" and select "Install plugin".

### Manual

Clone the repository and symlink or copy the `skills/` directory into your project:

```text
git clone https://github.com/kdyck/sidekicks.git
```

## What's Inside

### Review

- **review-board** — Multi-lens review gate. Classifies your work into one of nine types (Feature, Architecture, Security, Performance, UX/Accessibility, AI/ML, Legal/Compliance, Agent, or Full), selects an ordered panel of review lenses, and produces a structured report with a final recommendation. Works on brainstorms, plans, designs, and code alike. The Security lens includes secret scanning.

### Workflow

- **commit-often** — Lightweight nudge that instructs agents to commit at natural stopping points throughout a session rather than only at the end. Agent uses its own judgment on cadence unless the user specifies otherwise.

### Lenses

The review board selects from these lenses based on what you're reviewing:

- **Engineering** — correctness, error handling, edge cases, testability, dependency hygiene
- **Architecture** — separation of concerns, coupling, scalability, migration safety
- **Security** — auth, input validation, injection vectors, secrets and credential exposure
- **Performance** — response time, resource consumption, caching, query complexity
- **UX/Accessibility** — interaction clarity, WCAG AA compliance, error/empty/loading states
- **AI/ML** — model necessity, prompt quality, eval coverage, cost proportionality
- **Compliance** — data privacy (GDPR/CCPA), licensing, retention policy, audit trail
- **Finance** — infrastructure cost, API/model cost proportionality, budget alignment
- **Agent Governance** — domain ownership, handoff protocols, agent drift detection

## Philosophy

- Review early, review often — don't wait until code is written
- Structured over ad-hoc — every review follows the same disciplined process
- Evidence over opinions — lenses cite specific concerns, not vague feelings
- No work ships with an unresolved BLOCK
- Future UI assets use wire or outline-style SVG icons only

## Contributing

See `docs/skills-authoring.md` for the authoring guide on writing new skills.

## License

[MIT](LICENSE)
