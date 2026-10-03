#!/usr/bin/env python3
"""Validate local Markdown links and basic course-module structure."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")
errors: list[str] = []

for document in sorted(ROOT.rglob("*.md")):
    text = document.read_text(encoding="utf-8")
    for raw_target in LINK.findall(text):
        target = raw_target.split("#", 1)[0]
        if not target or "://" in target or target.startswith("mailto:"):
            continue
        decoded = target.replace("%20", " ")
        if not (document.parent / decoded).resolve().exists():
            errors.append(f"{document.relative_to(ROOT)}: broken link {raw_target}")

module_dirs = (ROOT / "01-foundation", ROOT / "02-practitioner")
for directory in module_dirs:
    for module in directory.glob("[0-9][0-9]-*.md"):
        text = module.read_text(encoding="utf-8").lower()
        if "outcome" not in text:
            errors.append(f"{module.relative_to(ROOT)}: missing outcomes section")
        if not any(word in text for word in ("exercise", "hands-on", "mock")):
            errors.append(f"{module.relative_to(ROOT)}: missing practical activity")
        # Theory should offer an immediate bridge from definition to application.
        if "../examples/" not in text:
            errors.append(f"{module.relative_to(ROOT)}: missing worked-example link")

# A worked example must let learners return to its source theory.
for example in (ROOT / "examples").rglob("*.md"):
    if example.name in {"README.md", "AGENTS.md"}:
        continue
    text = example.read_text(encoding="utf-8")
    if "Back to theory:" not in text:
        errors.append(f"{example.relative_to(ROOT)}: missing theory backlink")

if errors:
    print("Documentation checks failed:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

count = len(list(ROOT.rglob("*.md")))
print(f"Documentation checks passed for {count} Markdown files.")
