#!/usr/bin/env python3
"""Validate the distributable skill and local Markdown links, without dependencies."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
skill = root / "skills" / "android-tutorial-creator" / "SKILL.md"
text = skill.read_text()
errors = []
if not text.startswith("---\n") or "\n---\n" not in text[4:]:
    errors.append("Missing YAML frontmatter")
else:
    front = text.split("---", 2)[1]
    if not re.search(r"^name: android-tutorial-creator$", front, re.M):
        errors.append("Incorrect skill name")
    if not re.search(r"^description: .+", front, re.M):
        errors.append("Missing skill description")
for path in root.rglob("*.md"):
    for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
        if "://" in link or link.startswith("#"):
            continue
        target = link.split("#", 1)[0]
        if not (path.parent / target).exists():
            errors.append(f"Broken link in {path.relative_to(root)}: {link}")
if errors:
    raise SystemExit("\n".join(errors))
print("Skill metadata and local Markdown links passed.")
