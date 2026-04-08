<p align="center">
  <img src="./assets/banner.png" alt="Cross Platform Guard Banner" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/GitHub-Actions-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-PR%20Review-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/PR-Governance-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Versioning-Semantic-green?style=for-the-badge" />
</p>

<p align="center">
  <b>Reusable GitHub Actions workflows for PR governance, AI-powered code review, and automated release management.</b>
</p>

> Part of the sebco-labs / PlatformUnityCI ecosystem.

---

## What it does

Cross Platform Guard is a centralized workflow library that consumer repositories invoke via `workflow_call`. It provides three reusable capabilities out of the box:

- **AI-powered PR diff analysis** — detects quality signals (TODOs, debug prints, severity classification) and posts inline review comments
- **PR governance** — auto-labels PRs by changed files, suggests Conventional Commit prefixes, and validates PR title rules
- **Release governance** — runs `semantic-release` to produce GitHub Releases and changelogs automatically

---

## Architecture

```
cross-platform-guard/
├── .github/
│   ├── labeler.yml                  ← File-pattern → label mapping
│   └── workflows/
│       ├── ai-review.yml            ← Reusable: AI diff analysis + inline comments
│       ├── pr-governance.yml        ← Reusable: labels, title suggestion, title validation
│       ├── pr-labeler.yml           ← Internal: applies labels via actions/labeler
│       ├── pr-title-check.yml       ← Internal: validates PR title by label
│       ├── release-governance.yml   ← Reusable: semantic-release pipeline
│       └── release.yml              ← Internal: triggers release on push to main
├── lib/
│   └── ai_review/
│       ├── analyze_pr.py            ← Diff parser — produces comments.json
│       ├── summarize_pr.py          ← Diff summarizer — produces summary.md
│       └── test_qa_rules.py         ← Test fixture for QA rule validation
├── docs/
│   └── VERSIONING.md                ← Versioning strategy guide
├── assets/
│   └── banner.png
└── .releaserc.json                  ← semantic-release configuration
```

---

## Reusable workflows

### `ai-review.yml` — AI PR Review

Analyzes the diff of a pull request and produces:

- A **Markdown summary** injected into the PR description (upserted on every push)
- **Inline review comments** with severity classification and score
- **GitHub Issues** grouped by file for medium/high severity findings
- **Auto-close** of previously created issues when the related findings are resolved

**Triggers:** `workflow_call` or `pull_request` → `main`

**Inputs:**

| Input | Required | Default | Description |
|---|---|---|---|
| `language` | No | — | Target language hint |
| `pytest_mark` | No | `regression` | Test mark to run (future use) |

---

### `pr-governance.yml` — PR Governance

Enforces PR conventions in consumer repositories. On every pull request event it:

1. Detects changed files and classifies them (`engine`, `workflow`, `documentation`)
2. Applies the corresponding labels to the PR
3. Posts (or upserts) a comment suggesting the correct Conventional Commit prefix
4. Validates that the PR title starts with the expected prefix — fails CI if not

**Trigger:** `workflow_call`

**Label → prefix mapping:**

| Label | Expected prefix | Triggered by |
|---|---|---|
| `engine` | `feat:` | Changes in `lib/ai_review/**` |
| `workflow` | `chore:` | Changes in `.github/workflows/**` |
| `documentation` | `docs:` | Changes in `README.md` or `docs/**` |

---

### `release-governance.yml` — Release Governance

Runs `semantic-release` to automate versioning and GitHub Releases. Consumer repositories call this workflow on push to `main`.

**Trigger:** `workflow_call`

**Required permissions in the calling repository:**

```yaml
permissions:
  contents: write
  issues: write
  pull-requests: write
```

**Consumer requirement:** a valid `.releaserc.json` in the repository root (see [Consumer requirements](#consumer-requirements)).

---

## Using from another repository

### AI Review

```yaml
name: QA

on:
  pull_request:
    branches: [main]

jobs:
  ai-review:
    uses: PlatformUnityCI/cross-platform-guard/.github/workflows/ai-review.yml@v1
    secrets:
      CROSS_PLATFORM_GUARD_TOKEN: ${{ secrets.CROSS_PLATFORM_GUARD_TOKEN }}
```

### PR Governance

```yaml
name: PR Governance

on:
  pull_request:
    types: [opened, synchronize, reopened, edited, labeled, unlabeled]

jobs:
  governance:
    uses: PlatformUnityCI/cross-platform-guard/.github/workflows/pr-governance.yml@v1
```

### Release Governance

```yaml
name: Release

on:
  push:
    branches: [main]

jobs:
  release:
    uses: PlatformUnityCI/cross-platform-guard/.github/workflows/release-governance.yml@v1
```

### Versioning strategy for consumers

| Reference | Recommended for |
|---|---|
| `@v1` | Production — tracks the latest stable minor/patch in the v1 line |
| `@v1.0.0` | Pinned — exact reproducibility |
| `@main` | Development / testing only |

---

## Consumer requirements

### Required

- A GitHub Actions workflow that invokes the desired reusable workflow
- Pull requests enabled on the repository
- Workflow permissions matching the ones listed per workflow above

### For release governance

A `.releaserc.json` file must exist in the repository root:

```json
{
  "branches": ["main"],
  "tagFormat": "v${version}",
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",
    "@semantic-release/github"
  ]
}
```

**Common pitfalls:**

- ❌ Missing `.releaserc.json`
- ❌ Empty or malformed `.releaserc.json`
- ❌ File placed outside the repository root
- ❌ Non-npm repository without explicit plugin config — `semantic-release` may default to npm behavior

---

## AI Review engine

The analysis engine lives in `lib/ai_review/` and is composed of two Python scripts invoked directly by the workflow.

### `analyze_pr.py`

Parses the raw git diff line by line and emits a structured JSON array (`comments.json`) where each entry represents a quality finding.

**Detected signals:**

| Signal | Severity | Score | Description |
|---|---|---|---|
| `TODO` without context | `medium` | 3 | TODO without parentheses — must be detailed or resolved before merge |
| `TODO` with context | `low` | 1 | TODO with explanation |
| `print(` call | `low` | 1 | Debug print — should use `logging` instead |

**Output schema (`comments.json`):**

```json
[
  {
    "path": "lib/ai_review/example.py",
    "line": 42,
    "body": "TODO sin contexto — debería detallarse o resolverse antes del merge",
    "severity": "medium",
    "score": 3,
    "icon": "🟡"
  }
]
```

### `summarize_pr.py`

Reads the diff and produces a Markdown summary (`summary.md`) with:

- Added / removed line counts
- QA impact checklist
- Estimated risk level

The summary is injected into the PR description between `<!-- AI SUMMARY START -->` and `<!-- AI SUMMARY END -->` markers, and upserted on every push.

---

## Inline comments and issue lifecycle

### Inline comments

For each finding in `comments.json` where both `path` and `line` are present, the workflow posts an inline review comment with the format:

```
{icon} {SEVERITY}({score}) → {body}
```

If any finding has `severity: "high"`, the workflow step fails (`core.setFailed`).

### Issue creation

Issues are created grouped by file for findings with severity `medium` or `high` (test files excluded). If an issue with the same title already exists, it is not duplicated.

Issue title format: `[QA] Issues en {filepath}`

### Auto-close

On every workflow run, issues whose file no longer has active findings in the current diff are automatically closed.

---

## PR governance detail

The governance workflow runs four steps in sequence:

1. **Read PR context** — extracts PR number and title
2. **List changed files** — classifies files into `engine_changed`, `workflow_changed`, `docs_changed`
3. **Apply labels** — adds matching labels to the PR
4. **Suggest PR title** — posts or upserts a bot comment with the suggested prefix and an example title
5. **Validate PR title** — fails the CI check if the title does not start with the expected prefix

The title suggestion comment is idempotent — it updates the same comment on every push.

---

## Internal workflows

These workflows run on this repository itself and are not meant for consumers to call directly.

| Workflow | Trigger | Purpose |
|---|---|---|
| `pr-labeler.yml` | `pull_request` (opened, sync, reopened) | Applies labels using `actions/labeler` and `labeler.yml` |
| `pr-title-check.yml` | `pull_request` (opened, edited, sync, labeled) | Validates PR title by inspecting current labels |
| `release.yml` | `push` → `main` | Runs `semantic-release` to publish GitHub Releases |

---

## Versioning

This project uses fully automated semantic versioning driven by Conventional Commits and `semantic-release`.

The PR title is the **single source of truth** for version bumps — not individual commits.

| Commit prefix | Version bump | Example |
|---|---|---|
| `fix:` | Patch | `fix: handle missing token in checkout` |
| `feat:` | Minor | `feat: add severity classification` |
| `feat!:` / `BREAKING CHANGE:` | Major | `feat!: redesign comments.json schema` |

📄 [View full Versioning Guide](./docs/VERSIONING.md)

---

## Roadmap

| Capability | Status |
|---|---|
| AI diff analysis (TODO, print detection) | ✅ Done |
| Inline review comments | ✅ Done |
| Severity classification + scoring | ✅ Done |
| PR description summary | ✅ Done |
| Issue creation + auto-close lifecycle | ✅ Done |
| PR governance (labels, title validation) | ✅ Done |
| Automated release governance | ✅ Done |
| Multi-language rule engine | ✅ Done |
| LLM-powered diff analysis (OpenAI / Gemini) | 🔲 Planned |
| Rule configuration via YAML | 🔲 Planned |
| QA metrics dashboard | 🔲 Planned |

---

## Philosophy

<p align="center">
  <i>
    "Quality governance should be portable, not duplicated."<br><br>
    A centralized approach where PR standards, review logic, and release rules<br>
    live in one place — and every repository inherits them automatically.
  </i>
</p>

---

## License

MIT — see [LICENSE](LICENSE).