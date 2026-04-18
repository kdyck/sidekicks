from __future__ import annotations

import json
import re
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def read_text(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def read_json(relative_path: str) -> object:
    return json.loads(read_text(relative_path))


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def assert_path_exists(relative_path: str) -> None:
    assert_true((REPO_ROOT / relative_path).exists(), f"Expected required file: {relative_path}")


def assert_file_contains(relative_path: str, pattern: str, message: str) -> None:
    content = read_text(relative_path)
    assert_true(re.search(pattern, content, re.MULTILINE) is not None, message)


def assert_os_neutral_content(relative_path: str, message_prefix: str) -> None:
    content = read_text(relative_path)
    banned_patterns = [
        r"(?im)^```(powershell|bash|sh)\s*$",
        r"(?i)\bpowershell\b",
        r"(?i)\bpwsh\b",
        r"(?i)\bbash\b",
        r"(?i)\bcmd /c\b",
        r"(?i)\bGet-ChildItem\b",
        r"(?i)\bSelect-String\b",
        r"(?i)\bgrep\b",
        r"(?i)\brg\b",
        r"(?i)\bnpm\b",
        r"(?i)\bpytest\b",
        r"(?i)\bcargo\b",
    ]
    for pattern in banned_patterns:
        assert_true(
            re.search(pattern, content, re.MULTILINE) is None,
            f"{message_prefix} must stay OS-neutral and avoid shell-specific instructions.",
        )


def assert_review_board_shape(report: dict[str, object], message_prefix: str) -> None:
    required_fields = {"runId", "reviewType", "classificationRationale", "panel", "lensVerdicts", "summary"}
    assert_true(required_fields.issubset(report), f"{message_prefix} must include required fields.")

    valid_types = {"Feature", "Architecture", "Security", "Performance", "UX/Accessibility", "AI/ML", "Legal/Compliance", "Agent", "Full"}
    assert_true(report["reviewType"] in valid_types, f"{message_prefix} has an invalid reviewType.")

    assert_true(isinstance(report["panel"], list) and len(report["panel"]) > 0, f"{message_prefix} panel must be a non-empty array.")

    verdicts = report["lensVerdicts"]
    assert_true(isinstance(verdicts, list), f"{message_prefix} lensVerdicts must be an array.")
    for verdict in verdicts:
        assert_true(isinstance(verdict, dict), f"{message_prefix} lensVerdicts entries must be objects.")
        assert_true(
            {"lens", "verdict", "assessment", "concerns", "handoffs"}.issubset(verdict),
            f"{message_prefix} lensVerdicts entries must include lens, verdict, assessment, concerns, and handoffs.",
        )
        assert_true(verdict["verdict"] in {"APPROVE", "FLAG", "BLOCK"}, f"{message_prefix} has an invalid verdict value.")
        assert_true(isinstance(verdict["concerns"], list), f"{message_prefix} concerns must be an array.")
        assert_true(isinstance(verdict["handoffs"], list), f"{message_prefix} handoffs must be an array.")

    summary = report["summary"]
    assert_true(isinstance(summary, dict), f"{message_prefix} summary must be an object.")
    assert_true(
        {"blockers", "flags", "approvals", "unresolvedHandoffs", "recommendation"}.issubset(summary),
        f"{message_prefix} summary must include blockers, flags, approvals, unresolvedHandoffs, and recommendation.",
    )
    assert_true(
        summary["recommendation"] in {"SHIP", "SHIP WITH CONDITIONS", "HOLD"},
        f"{message_prefix} has an invalid recommendation.",
    )

    has_block = any(v["verdict"] == "BLOCK" for v in verdicts)
    has_flag = any(v["verdict"] == "FLAG" for v in verdicts)
    if has_block:
        assert_true(summary["recommendation"] == "HOLD", f"{message_prefix} must HOLD when any verdict is BLOCK.")
    elif has_flag:
        assert_true(summary["recommendation"] == "SHIP WITH CONDITIONS", f"{message_prefix} must SHIP WITH CONDITIONS when FLAG exists and no BLOCK.")
    else:
        assert_true(summary["recommendation"] == "SHIP", f"{message_prefix} must SHIP when all verdicts APPROVE.")


def main() -> None:
    skill_names = [
        "review-board",
        "commit-often",
        "writing-discipline",
    ]

    assert_path_exists(".gitignore")

    for skill_name in skill_names:
        skill_path = f"skills/{skill_name}/SKILL.md"
        assert_path_exists(skill_path)
        assert_file_contains(
            skill_path,
            rf"^---\s*\r?\nname:\s+{re.escape(skill_name)}\s*\r?\ndescription:\s+Use when",
            f"Expected frontmatter for {skill_name}.",
        )
        assert_os_neutral_content(skill_path, f"Skill {skill_name}")

    assert_os_neutral_content("docs/skills-authoring.md", "Skill authoring guide")

    required_files = [
        "README.md",
        "docs/architecture/sidekick-system.md",
        "docs/skills-authoring.md",
        "docs/review-board-report.schema.json",
        "docs/examples/review-board-report.json",
        "docs/examples/review-board-summary.md",
    ]
    for relative_path in required_files:
        assert_path_exists(relative_path)

    assert_file_contains("README.md", r"review-board", "README must document the review-board skill.")
    assert_file_contains("README.md", r"commit-often", "README must document the commit-often skill.")
    assert_file_contains("README.md", r"writing-discipline", "README must document the writing-discipline skill.")
    assert_file_contains("README.md", r"outline", "README must mention the outline SVG icon rule.")
    assert_file_contains("docs/architecture/sidekick-system.md", r"review-board", "Architecture doc must describe review-board.")
    assert_file_contains("docs/architecture/sidekick-system.md", r"commit-often", "Architecture doc must describe commit-often.")
    assert_file_contains(
        "docs/architecture/sidekick-system.md",
        r"writing-discipline",
        "Architecture doc must describe writing-discipline.",
    )
    assert_file_contains(
        "docs/architecture/sidekick-system.md",
        r"review-board-report\.schema\.json",
        "Architecture doc must reference the review report schema.",
    )

    for skill_name in skill_names:
        skill_path = f"skills/{skill_name}/SKILL.md"
        assert_file_contains(skill_path, r"^## Output", f"Skill {skill_name} must document its output contract.")
        assert_file_contains(skill_path, r"^## Hard Stop", f"Skill {skill_name} must document hard-stop behavior.")

    report_schema = read_json("docs/review-board-report.schema.json")
    assert_true("reviewType" in report_schema["properties"], "Report schema must define reviewType.")
    assert_true("lensVerdicts" in report_schema["properties"], "Report schema must define lensVerdicts.")

    example_report = read_json("docs/examples/review-board-report.json")
    assert_review_board_shape(example_report, "Example review report")
    assert_true(example_report["summary"]["recommendation"] == "SHIP", "Expected example report to recommend SHIP.")

    print("Sidekick validation passed.")


if __name__ == "__main__":
    main()
