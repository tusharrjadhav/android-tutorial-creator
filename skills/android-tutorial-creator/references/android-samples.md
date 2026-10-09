# Runnable Android samples

Use Kotlin and Jetpack Compose for new UI samples unless the user requests Views or an existing project dictates otherwise. Preserve the target project's conventions.

Pin compatible stable versions of the JDK, Gradle, Android Gradle Plugin, Kotlin, and Android libraries after checking their official compatibility guidance. Commit the Gradle wrapper scripts, properties, and wrapper JAR. Document SDK requirements. Do not commit `local.properties`, signing credentials, caches, or generated builds.

For state lessons, show ownership, immutability, and lifecycle-aware UI observation. Explain when `remember`, `rememberSaveable`, or a ViewModel fits. For coroutines, show structured scopes and cancellation. For Flow, distinguish replay, initial values, buffering, and subscriber lifetime using behavior that the sample exercises. Avoid presenting transient navigation events as universally reliable merely because they use SharedFlow.

Expose loading, success, empty, and error behavior when the topic includes asynchronous data. Prefer a deterministic fake repository for introductory examples. Add real networking only when needed, with a documented service and no committed keys. Scope dependencies and abstractions to the concept taught.

Verify pure logic with unit tests; verify interaction or lifecycle behavior with relevant Android tests when practical. Document the emulator/device and what was actually exercised. If unavailable, give runnable commands and mark device checks as unrun.
