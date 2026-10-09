---
name: android-tutorial-creator
description: Create or revise Android learning tutorials with Kotlin and Jetpack Compose examples, exercises, tests, and GitHub-ready documentation. Use for Android lessons, learning roadmaps, or interview preparation with sample projects; ordinary Android bug fixes do not need this teaching workflow.
---

# Android Tutorial Creator

Turn the requested topic into learning material that a reader can follow and verify. Preserve the user's topic, audience, repository, format, and publication intent.

## Frame the lesson

Infer audience and scope from the request. If missing, default to a beginner-friendly focused lesson and state the assumption. Ask only when a missing choice would substantially change the deliverable. Choose one concrete outcome and identify prerequisites before introducing advanced concepts.

For a roadmap, order topics by prerequisite and give each lesson an observable learning outcome. For interview preparation, distinguish concise answers from runnable examples and include follow-up reasoning questions. Do not generate a whole curriculum when the user asks for one lesson.

Read [references/tutorial-design.md](references/tutorial-design.md) when designing a lesson. Use [assets/tutorial-template.md](assets/tutorial-template.md) as an adaptable outline. The optional scaffold helper is `scripts/create_tutorial.py`; its output is a draft that must be completed.

## Build and explain

Verify current Android and Kotlin APIs, dependency compatibility, and deprecations against primary documentation linked in [references/sources.md](references/sources.md). Record exact tool and dependency versions used by a generated sample. Use available Android tooling or skills when helpful; this skill does not depend on a specific CLI.

Read [references/android-samples.md](references/android-samples.md) before creating runnable samples. Keep the sample small enough to expose the lesson's behavior. Add architecture layers, Hilt, Room, Retrofit, or navigation only when the topic or existing project calls for them.

Explain each step with its file path, the reason for the change, and a visible or testable result. Keep snippets consistent with the final sample. Include imports or clearly identify omitted context. Avoid unexplained ellipses in code a learner should run. Distinguish pseudocode from runnable code.

Add a diagram only when it clarifies a relationship or sequence. Use a simple text or Mermaid diagram for source-controlled documentation; screenshots must come from the running sample. Do not fabricate outputs.

## Verify learning and implementation

Add exercises with hints and expected behavior, common mistakes tied to the demonstrated APIs, and interview questions at the learner's level. Verify that the lesson teaches the promised outcome without requiring concepts absent from its prerequisites.

Run appropriate build and test checks for generated code. For Android projects, use the sample's wrapper to assemble and run relevant unit tests; run UI tests when a configured device is available and the lesson depends on interaction. Report exact checks, their results, and device/environment limitations. A Markdown or scaffold check is not proof that an Android sample builds.

## Prepare and publish

Use numbered lesson folders for a course or a descriptive slug for a focused tutorial. Include setup, run instructions, expected behavior, exercises, references, and validation status. Exclude credentials, local SDK paths, caches, and build outputs.

Read [references/publishing.md](references/publishing.md) when preparing a repository or publishing. Creating material alone does not authorize publication. If publication is requested, use the named owner and repository, preserve unrelated work, and verify the resulting remote content. If access fails, finish the local deliverable and identify the exact remaining blocker.
