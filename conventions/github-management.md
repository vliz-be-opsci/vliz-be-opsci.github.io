---
author: "João dos Santos / Decruw Cedric"
graph_logo_bg: false
layout: default
permalink: /conventions/github-management
description: "Conventions relating to github management, repository naming, branch naming, commit messages, and pull requests."
---

# Conventions relating to _github management_

This document outlines the conventions for GitHub management, including:

- [Repository Naming](#repositories)
- [Branch Naming](#branches)
- [Commit Messages](#commits)
- [Pull Requests](#pull-request)
- [Language-Specifics](#python-projects)

## Naming and Messages <a name="naming-messages"></a>

### Repositories <a name="repositories"></a>

- Repository names should use kebab-case, which consists of all lowercase letters and dashes. For example, `name-of-repo`. Refer to [Kebab case](https://en.wikipedia.org/wiki/Letter_case#Kebab_case){:target=”\_blank”} for more details.
- Repositories should be tagged with appropriate topics in the about section (e.g., python, docker-compose, react, etc.). These topics can be used to filter repositories.
- Releases should use git tags and conform to [Semantic Versioning](https://semver.org/){:target=”\_blank”}, using the format `major.minor.patch` without a 'v' prefix.
- Each repository should include a LICENSE file. For source code, use the MIT license. For datasets, use the CC-BY license.

##### Specific rules for naming

| Application          | Example                                                                           | Regex Rule             |
| -------------------- | --------------------------------------------------------------------------------- | ---------------------- |
| Python packages      | [py-sema](https://github.com/vliz-be-opsci/py-sema)                               | `^py-[a-z0-9\-]+$`     |
| GitHub Actions       | [rohub-sync-action](https://github.com/vliz-be-opsci/rohub-sync-action)           | `^[a-z0-9\-]+-action$` |
| GitHub Pages Actions | [space-to-pages](https://github.com/vliz-be-opsci/space-to-pages)                 | `^[a-z0-9\-]+-pages$`  |
| RO-Crates            | [observatory-bpns-crate](https://github.com/emo-bon/observatory-bpns-crate)       | `^[a-z0-9\-]+-crate$`  |
| Web components       | [rocrate-preview-widget](https://github.com/vliz-be-opsci/rocrate-preview-widget) | `^[a-z0-9\-]+-widget$` |

### Branches <a name="branches"></a>

Each repository should have two default branches:

- `main`: For release-ready code.
- `gh-pages`: For documentation. This branch is automatically maintained by a documentation workflow.

Additional branches should be created for each change. The branch name should reflect the change, using the format `{category}/{description}`. For example, `fix/connection_bug`. The description should be a short summary of the change, using [snake case](https://en.wikipedia.org/wiki/Letter_case#Snake_case){:target=”\_blank”}

The category should be one of the following:

- fix
- feature
- refactor
- chore
- docs
- (add more if needed)

### Commits <a name="commits"></a>

Commit messages should follow the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/){:target=”\_blank”}.
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

## Rules <a name="rules"></a>

### Pull Request <a name="pull-request"></a>

Every code change should be made on a new branch and submitted as a pull request (PR). Direct pushes to the `main` branch are not allowed.

When opening a PR, provide a descriptive name (which can be similar to the branch name) and a description explaining the purpose of the PR. Use [GitHub keywords](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests#linking-a-pull-request-to-an-issue){:target=”\_blank”} if applicable.

Before a PR can be merged, it must:

- Receive at least one approval.
- Pass all checks, including:
  - Linting
  - Testing
  - Test Coverage

The commits within the PR should tell a cohesive story. Each commit should be clear, concise, and focused on a single change.

### Language-Specifics

##### [Python Projects](python) <a name="python-projects"></a>

##### [Typescript Projects](typescript) <a name="typescript-projects"></a>
