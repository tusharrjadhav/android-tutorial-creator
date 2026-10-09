#!/usr/bin/env python3
"""Create a lesson outline without overwriting existing lessons."""
import argparse
import json
from pathlib import Path
import re


def create_tutorial(topic, slug, level, output):
    if not topic.strip():
        raise ValueError("Topic must not be empty")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
        raise ValueError("Slug must contain lowercase words or numbers separated by hyphens")
    if level not in {"beginner", "intermediate", "advanced"}:
        raise ValueError("Unsupported audience level")
    template = Path(__file__).resolve().parents[1] / "assets" / "tutorial-template.md"
    content = template.read_text().replace("{{topic}}", topic.strip()).replace("{{level}}", level)
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    destination = output / slug
    destination.mkdir()  # Fails before writing when the lesson already exists.
    (destination / "README.md").write_text(content)
    (destination / "lesson.json").write_text(json.dumps({
        "topic": topic.strip(), "slug": slug, "level": level,
        "status": "outline", "sample_generated": False, "checks_run": []
    }, indent=2) + "\n")
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--level", choices=["beginner", "intermediate", "advanced"], default="beginner")
    parser.add_argument("--output", type=Path, default=Path("tutorials"))
    args = parser.parse_args()
    try:
        destination = create_tutorial(args.topic, args.slug, args.level, args.output)
    except (ValueError, OSError) as error:
        parser.exit(1, f"Could not create lesson: {error}\n")
    print(f"Created outline: {destination}. Complete the lesson and generate/verify any requested sample.")


if __name__ == "__main__":
    main()
