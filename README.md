# Android Tutorial Creator

A reusable agent skill for turning an Android topic into a progressive tutorial, a runnable Kotlin/Jetpack Compose sample, and GitHub-ready learning material.

## Use the skill

The distributable skill lives in [skills/android-tutorial-creator](skills/android-tutorial-creator/SKILL.md). Copy that directory into your agent's skills location. For Codex, use `~/.codex/skills/android-tutorial-creator`, then start a new session.

Example request:

> Use $android-tutorial-creator to teach StateFlow vs SharedFlow to an intermediate Android developer. Create a Compose sample, explain lifecycle collection, add tests and exercises, and prepare the tutorial for GitHub.

The skill supports beginner roadmaps, focused modern Android tutorials, and interview preparation. It adapts the depth and architecture to the audience rather than imposing Clean Architecture on every sample.

## What it produces

- A lesson with prerequisites, learning outcomes, concept explanations and incremental implementation steps.
- A runnable sample when requested, with a Gradle wrapper and documented build versions.
- Exercises, common mistakes, interview questions and authoritative reference links.
- Appropriate tests, architecture diagrams when useful, and an honest validation record.
- Repository documentation and publishing when explicitly requested.

This repository contains the creator skill and its reusable templates; it is not itself an Android application. Android samples are generated for a chosen topic and checked in their target environment.

## Create a lesson scaffold

Requires Python 3.10 or newer; no third-party packages are needed.

```sh
python3 skills/android-tutorial-creator/scripts/create_tutorial.py   --topic 'StateFlow vs SharedFlow' --slug stateflow-vs-sharedflow   --level intermediate --output tutorials
```

This creates a lesson brief and an outline that the agent must complete. It does not generate Android code or claim to validate a build. Existing lesson directories are never overwritten.

## Verify this project

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_project.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidance and [the source references](skills/android-tutorial-creator/references/sources.md) for the primary materials used to design the skill.
