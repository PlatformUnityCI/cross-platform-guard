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
## 🎯 Purpose

- 🤖 Analyze Pull Request diffs using AI-driven rules
- 💬 Generate inline code review comments automatically
- 🚦 Classify issues by severity (Low / Medium / High)
- 🔒 Block PRs only when critical issues are detected
- 📊 Create and manage issues dynamically
- 🔌 Integrate with any testing pipeline (Python, Playwright, etc.)

---
## 🧠 Design Principles

- **Separation of Concerns** → Testing and quality analysis are decoupled
- **Reusability** → One engine, multiple repositories
- **Scalability** → Supports multi-language pipelines
- **Non-intrusive** → No need to modify business logic repositories

---
## ⚙️ How It Works

```text
Repository (consumer)
        │
        ├── 🧪 Run Tests (local pipeline)
        │
        ▼
Cross Platform Guard (this repo)
        │
        ├── 🤖 Analyze PR Diff
        ├── 💬 Inline Comments
        ├── 📊 Issue Generation
        └── 🚦 PR Validation
```

---
🏗️ Architecture
```text
cross-platform-guard/
│
├── .github/workflows/     # Reusable QA pipelines
├── lib/ai_review/         # AI analysis engine
├── docs/                  # Documentation
├── examples/              # Usage examples
├── README.md
```
---
🚀 Usage
```
From another repository:
name: QA

on:
  pull_request:

jobs:
  qa:
    uses: PlatformUnityCI/cross-platform-guard/.github/workflows/qa-engine.yml@main
    with:
      language: python
      pytest_mark: regression
```

---
🧪 Current Capabilities
```
| Feature                 | Status |
| ----------------------- | ------ |
| Python Testing (pytest) | ✅     |
| PR Diff Analysis        | ✅     |
| Inline Comments         | ✅     |
| Severity Classification | ✅     |
| Issue Generation        | ✅     |
| Auto Issue Closing      | ✅     |
| Multi-language Support  | 🚧     |
```
---
🔮 Roadmap

```
🌐 Playwright (Web testing)

⚡ Node.js / TypeScript support

🧠 Advanced AI suggestions (refactoring, naming, logic)

📊 QA Metrics Dashboard

🔌 Plugin-based rule engine
```
---
🧩 Philosophy

<p align="center">
  <i>
    "Quality should be portable, not duplicated."<br><br>
    A centralized approach where quality logic lives in one place,<br>
    repositories stay clean, and standards scale naturally across systems.
  </i>
</p>

---
🤝 Contributing

<p align="center">
  <i>
    This is a private experimental project,  —<br>
    but collaboration ideas are welcome.
  </i>
</p>

---
⚡ Final Thought

<p align="center">
  <i>
    This is not just a pipeline —<br>
    it’s the foundation of a QA Platform as Code.
  </i>
</p>

---
👤 Author

<p align="center">
  <img src="https://img.shields.io/badge/Built%20by-Sebas%20Couto-0A66C2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Role-QA%20Engineer-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Focus-Automation-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Approach-AI%20Driven-black?style=for-the-badge" />
</p>
