<p align="center">
  <img src="./assets/banner.png" alt="Cross Platform Guard Banner" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/QA-Automation-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-Review-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/GitHub-Actions-black?style=for-the-badge" />
</p>

<p align="center">
  <b>Reusable QA Engine for Cross-Repository Code Quality</b>
</p>

---

## 🧠 Overview

**Cross Platform Guard** is a reusable QA engine built on top of GitHub Actions that enables automated testing and intelligent Pull Request analysis across multiple repositories and technologies.

It decouples **quality logic** from business code, allowing teams to apply a standardized QA pipeline everywhere.

---

## 🏗️ Architecture

```text
cross-platform-guard/
│
├── .github/workflows/     # Reusable QA and governance workflows
├── lib/ai_review/         # AI analysis engine
├── docs/                  # Documentation
├── examples/              # Usage examples
├── README.md
```

---

## 🚀 Usage

### Reusable workflow invocation

From another repository:

```yaml
name: QA

on:
  pull_request:

jobs:
  qa-guard:
    uses: PlatformUnityCI/cross-platform-guard/.github/workflows/qa-engine.yml@v1
    with:
      language: python
      pytest_mark: regression
```

### Versioning strategy for consumers

You can invoke this reusable workflow in different ways depending on your stability needs:

* **Recommended for consumers:** use a stable tag

  * `@v1`
  * `@v1.0.0`
* **Recommended for development/testing only:** use `@main`

Examples:

```yaml
uses: PlatformUnityCI/cross-platform-guard/.github/workflows/qa-engine.yml@v1
```

```yaml
uses: PlatformUnityCI/cross-platform-guard/.github/workflows/qa-engine.yml@v1.0.0
```

```yaml
uses: PlatformUnityCI/cross-platform-guard/.github/workflows/qa-engine.yml@main
```

---

## 📋 Consumer Repository Requirements

A repository that wants to consume **Cross Platform Guard** should provide the following minimum setup:

### Required

* A valid GitHub Actions workflow that invokes the reusable workflow
* A repository with pull requests enabled
* Proper workflow permissions for PR interaction
* The language/test stack expected by the invoked workflow

### Recommended

* Clear test commands and deterministic CI setup
* Stable dependency installation process
* Reusable branch strategy (`main`, feature branches, PR-based flow)

### Typical permissions

```yaml
permissions:
  contents: read
  pull-requests: write
  checks: write
  issues: write
```

---

## 🧪 Release Governance Consumer Requirements

If a repository also consumes a reusable **release governance** workflow, it should include the expected semantic-release configuration in the repository root.

### Required file

```text
.releaserc.json
```

### Example

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

### Common pitfalls

* ❌ Missing `.releaserc.json`
* ❌ Empty `.releaserc.json`
* ❌ `.releaserc.json` outside repository root

### Why this matters

Without a valid release config, `semantic-release` may fall back to defaults and try to behave like an npm package release, which can fail if the repository is not Node/npm-based.

### Where to validate this

This validation is best enforced inside the **reusable release governance workflow**, so every consumer gets the same contract and error handling automatically.

Example pre-check inside the reusable workflow:

```yaml
- name: Validate release config
  run: |
    if [ ! -f ".releaserc.json" ]; then
      echo "Missing .releaserc.json"
      exit 1
    fi
```

---

## 🧪 Current Capabilities

| Feature                 | Status |
| ----------------------- | ------ |
| Python Testing (pytest) | ✅      |
| PR Diff Analysis        | ✅      |
| Inline Comments         | ✅      |
| Severity Classification | ✅      |
| Issue Generation        | ✅      |
| Auto Issue Closing      | ✅      |
| Multi-language Support  | 🚧     |

---

## 🔮 Roadmap

* 🌐 Playwright (Web testing)
* ⚡ Node.js / TypeScript support
* 🧠 Advanced AI suggestions (refactoring, naming, logic)
* 📊 QA Metrics Dashboard
* 🔌 Plugin-based rule engine

---

## 📦 Versioning

This project uses automated semantic versioning.

📄 [View Versioning Guide](./docs/VERSIONING.md)

---

## 🧩 Philosophy

<p align="center">
  <i>
    "Quality should be portable, not duplicated."<br><br>
    A centralized approach where quality logic lives in one place,<br>
    repositories stay clean, and standards scale naturally across systems.
  </i>
</p>

---

## 🤝 Contributing

<p align="center">
  <i>
    This is a private experimental project —<br>
    but collaboration ideas are welcome.
  </i>
</p>

---

## ⚡ Final Thought

<p align="center">
  <i>
    This is not just a pipeline —<br>
    it’s the foundation of a QA Platform as Code.
  </i>
</p>

---

## 👤 Author

<p align="center">
  <img src="https://img.shields.io/badge/Built%20by-Sebas%20Couto-0A66C2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Role-QA%20Engineer-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Automation-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Approach-AI%20Driven-black?style=for-the-badge" />
</p>

