<p align="center">
  <img src="https://img.shields.io/badge/Versioning-Semantic-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Strategy-Conventional%20Commits-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Automation-semantic--release-black?style=for-the-badge" />
</p>

<p align="center">
  <b>Automated versioning strategy for Cross Platform Guard</b>
</p>

---

## 🧠 Overview

This repository uses:

* **semantic-release**
* **Conventional Commits**
* **Pull Request driven versioning**

👉 Versions are **fully automated**
👉 No manual versioning is required

---

## 🔢 Version format

```
MAJOR.MINOR.PATCH
```

Example:

```
1.2.3
│ │ └── Patch (fixes)
│ └──── Minor (features)
└────── Major (breaking changes)
```

---

## 🎯 Version impact

### 🟡 Patch → Bug fixes

<p align="center">
  <img src="https://img.shields.io/badge/1.1.0-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/%E2%9E%9C-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/1.1.1-green?style=for-the-badge" />
</p>

Used when:

* Fixing bugs
* Improving workflows
* Internal refactors
* No visible behavior changes

---

### 🔵 Minor → New features

<p align="center">
  <img src="https://img.shields.io/badge/1.1.2-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/%E2%9E%9C-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/1.2.0-green?style=for-the-badge" />
</p>

Used when:

* Adding new QA rules
* Enhancing analysis capabilities
* Adding integrations
* Non-breaking improvements

---

### 🔴 Major → Breaking changes

<p align="center">
  <img src="https://img.shields.io/badge/1.2.0-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/%E2%9E%9C-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/2.0.0-green?style=for-the-badge" />
</p>

Used when:

* Changing output formats
* Modifying contracts between repos
* Introducing incompatible changes
* Breaking integrations

---

## 🏷️ Commit / PR rules

### Patch

```
fix:
```

Example:

```
fix: handle missing token in checkout step
```

---

### Minor

```
feat:
```

Example:

```
feat: add radon complexity analysis
```

---

### Major

```
feat!:
```

or:

```
BREAKING CHANGE:
```

Example:

```
feat!: redesign AI findings schema
```

---

## 📊 Quick reference

| Change type     | Prefix   | Version |
| --------------- | -------- | ------- |
| Bug fix         | `fix:`   | Patch   |
| New feature     | `feat:`  | Minor   |
| Breaking change | `feat!:` | Major   |

---

## ⚙️ How versioning works

```text
1. Developer creates a branch
2. Opens a Pull Request
3. System:
   - detects changed files
   - suggests prefix
   - validates PR title
4. PR is merged (squash)
5. semantic-release:
   - calculates next version
   - creates GitHub Release
   - generates release notes
   - comments on PR
```

---

## 🤖 Important behavior

* Version is calculated from **PR title**
* Not from commits inside the branch
* Not from GitHub Copilot suggestions
* Not manually

👉 The PR title is the **single source of truth**

---

## ⚠️ Common mistakes

❌ Using default GitHub titles:

```
Update README.md
Create pipeline.yml
```

✔ Correct versioned title:

```
fix: update README with versioning guide
feat: add CI pipeline
```

---

## 💡 Examples

### Patch example

```
fix: avoid duplicate PR comments
```

<p align="center">
  <img src="https://img.shields.io/badge/1.1.1-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/%E2%9E%9C-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/1.1.2-green?style=for-the-badge" />
</p>

---

### Minor example

```
feat: add pylint integration
```

<p align="center">
  <img src="https://img.shields.io/badge/1.1.2-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/%E2%9E%9C-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/1.2.0-green?style=for-the-badge" />
</p>

---

### Major example

```
feat!: change comments.json schema
```

<p align="center">
  <img src="https://img.shields.io/badge/1.2.0-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/%E2%9E%9C-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/2.0.0-green?style=for-the-badge" />
</p>

---

## 🧭 Decision guide

If you're unsure:

* Bug fix → `fix:`
* New capability → `feat:`
* Breaking change → `feat!:`

---

## 🧩 Philosophy

<p align="center">
  <i>
    "Versioning should be automatic, predictable, and invisible to developers."<br><br>
    Focus on the change — not the number.
  </i>
</p>

---

## 🚀 Final takeaway

<p align="center">
  <b>Think in changes, not in versions</b><br><br>
  semantic-release handles everything 🚀
</p>
