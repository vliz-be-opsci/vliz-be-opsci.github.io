---
title: github-management
author: "João dos Santos"
layout: default
permalink: /conventions/github-management
---

# Conventions relating to _github management_

This document outlines the conventions for github management, repository naming, branch naming, commit messages, and pull requests.

## Naming and Messages

### Repositories

- Repository names should use kebab-case, which consists of all lowercase letters and dashes. For example, `name-of-repo`. Refer to [Kebab case](https://en.wikipedia.org/wiki/Letter_case#Kebab_case) for more details.
- Repositories should be tagged with appropriate topics in the about section (e.g., python, docker-compose, react, etc.). These topics can be used to filter repositories.
- Releases should use git tags and conform to Semantic Versioning, using the format `major.minor.patch` without a 'v' prefix.
- Each repository should include a LICENSE file. For source code, use the MIT license. For datasets, use the CC-BY license.

Specific rules for naming:

- Python packages: Use short, undelimited names for short package names (e.g., `pyhello`). For longer names, use dashes as delimiters (e.g., `py-hello-world`)
- GitHub Actions: Append `\*-action` to the name.
- GitHub Pages Actions: Append  `\*-to-pages` to the name.
- RO-Crates: Append `\*-crate` to the name.
- Web components: Append `\*-widget` to the name.

### Branches

Each repository should have two default branches:

- `main`: For release-ready code.
- `gh-pages`: For documentation. This branch is automatically maintained by a documentation workflow.

Additional branches should be created for each change. The branch name should reflect the change, using the format `{category}/{description}`. For example, `fix/connection_bug`. The description should be a short summary of the change, using [snake case](https://en.wikipedia.org/wiki/Letter_case#Snake_case)

The category should be one of the following:

- fix
- feature
- refactor
- chore
- docs
- (add more if needed)

### Commits

Commit messages should follow the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/).
The commit message should follow this format:

    "<type>: {action} {what} {where} {why} "
    ex: refactor: change args in funcA to allow tipehinting

The allowed types are:

- build
- chore
- ci
- docs
- feat
- fix
- perf
- refactor
- revert
- style
- test

The Conventional Commits specification allows for additional information in the body and footer of the commit message.
## Rules

### Pull Request

Every code change should be made on a new branch and submitted as a pull request (PR). Direct pushes to the `main` branch are not allowed.

When opening a PR, provide a descriptive name (which can be similar to the branch name) and a description explaining the purpose of the PR. Use [GitHub keywords](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests#linking-a-pull-request-to-an-issue) if applicable.

Before a PR can be merged, it must:
- Receive at least one approval.
- Pass all checks, including:
  - Linting
  - Testing
  - Test Coverage

The commits within the PR should tell a cohesive story. Each commit should be clear, concise, and focused on a single change.
### Language-Specifics

#### [Python Projects](python.md)  
