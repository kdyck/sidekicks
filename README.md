# Sidekick Skills

Skills for coding agent workflows — structured review, commit hygiene, and writing discipline.

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

## Skills

### Review

- **review-board** — Multi-lens review gate. Triggers at the end of any phase — brainstorm, plan, design, architecture decision, or implementation. Classifies the work, selects a panel of domain-specific lenses, and produces a structured report with a final recommendation: SHIP, SHIP WITH CONDITIONS, or HOLD. No work moves forward with an unresolved BLOCK.

### Workflow

- **commit-often** — Lightweight nudge that instructs agents to commit at natural stopping points throughout a session rather than only at the end. Agent uses its own judgment on cadence unless the user specifies otherwise.
- **writing-discipline** — Instructs agents to apply "signal over decoration" when writing any prose. Avoid decorative dividers, nested bullets, bold overuse, and headers on content too short to need navigation. Structure only when it earns its place.

## Review Lenses

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
- UI assets use wire or outline-style SVG icons only

## Contributing

See `docs/skills-authoring.md` for the authoring guide on writing new skills.

## License

[MIT](LICENSE)
