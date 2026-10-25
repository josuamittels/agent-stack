# Target package setup

Prepare only the requested target's measuring instrument. This is local setup, not another evaluation mode or permission to launch agents.

Maintain `evals/<skill-name>/suite.json`, a frozen versioned rubric, and `cases.json`. The manifest identifies schema version 1, target slug, active rubric, and relevant production resources. A rubric has 3–6 criteria with positive integer weights totaling 100, `check` or `judge` kinds, critical flags, explicit 0/1/2 anchors, categories, and abstract improvement guidance. Preserve immutable rubric versions; a changed quality bar needs a new version.

For live evaluation, use or prepare the rubric and inspect the completed output once. Do not run synthetic cases. No existing suite marker is required.

For an authorized post-edit evaluation, select exactly three cases: normal, boundary, and failure. Prepare synthetic fixtures and organic requests with observable requirements. In legacy packages, only the first three maintained cases are active; additional regressions and calibrations remain historical and are never scheduled. New packages contain exactly three cases and no calibrations.

Freeze setup before dispatch. Apollo, Athena, and Prometheus each receive one case in a fresh temporary production context, without rubric, expected outcomes, prior scores, or evaluation awareness. Remove validation and delegation handoffs from temporary copies. Each producer has one attempt and may not invoke other skills as agents or execute external effects. One fresh Betabert grades all three outputs in a single call. A missing output stays failed; do not replace its producer.

Keep check evidence and model evidence distinct. Missing evidence never proves success. Do not run calibrations, broaden cases, refresh upstream packages, or tune the rubric after seeing outputs. If setup or criteria prove unusable, report not good—unable to verify and stop. Preserve past abstract records without rewriting them.
