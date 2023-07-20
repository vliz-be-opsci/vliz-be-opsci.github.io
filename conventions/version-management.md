---
title: version-management
author: "João Pinto"
layout: default
permalink: /conventions/version-management
---

# Conventions relating to _version management_

## Naming and Messages

### Repositories

- Names should use dashes and lower case. ([kebab case](<[http://example.com](https://en.wikipedia.org/wiki/Letter_case#Kebab_case)>) -> name-of-repo
- They should be accompanied by topics in the about section (e.g. python, docker-compose, react, ...), these topics can be filtered on when looking for a repo.
- Releases should make use of git tag and conform to semantic versioning (`major.minor.patch`, not prefixed with v)
- each repo should contain a LICENSE:
  - MIT for source code
  - CC-BY for datasets

Specific Rules for naming:

- python packages: short names without any delimiter (e.g. pyhello), longer names delimited by dashes (e.g. py-hello-world)
- github actions: \*-action
- github pages actions: \*-to-pages
- ro-crates: \*-crate
- web components: \*-widget

### Branches

There should be two default branchs on each repo:

- main (release ready code)
- gh-pages (documentation) -> this branch is maintained automatically by a documentation workflow

Other branches should be open whenever a change is required and the name should fit the change.

{category}/{description} -> example: fix/connection_bug

The description should be a short summary of the branch intent using [snake case](https://en.wikipedia.org/wiki/Letter_case#Snake_case)
The category should fall into:

- fix
- feature
- refactor
- chore
- docs
- (add more if needed)

### Commits

Commits messages should follow [these convention rules](https://www.conventionalcommits.org/en/v1.0.0/)

The commit message should follow:

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

You can check more option on the allowed convention on the website, it also allows for a body and a footer in the message.

## Rules

### Pull Request

A new PR from a new branch should be made on every code change.

- There is not direct push to main

When opening a PR a name should be given (Can be like the branch name), and a description explaining the goal of the PR, and also using [GitHub keywords](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/using-keywords-in-issues-and-pull-requests#linking-a-pull-request-to-an-issue) if available.

To be able to merge a PR it needs to:

- Have at least one approval
- Passed checker actions
  - Linting
  - Testing
  - Test Coverage

The commits inside the PR should follow a story driven history, modulated and simple and straight-forward for the action at hands.

### Python Projects

For a coockiecutter/template on python projects you can go [here](https://gitlab.vliz.be/datac/templating/cookiecutter-py-module) # Change this to github

Projects should use [poetry](https://python-poetry.org/docs/) as the dependency manager

The linting will follow the default [flake8](https://github.com/PyCQA/flake8) settings.
The checker will test for the usage of [black](https://github.com/psf/black) and [isort](https://github.com/PyCQA/isort), only change from default is the line-lenght set to 79.

The checker will also run pytest, and check for test coverage. The default setting is 85% coverage on single files and 90% for the porject.

If you are using the cookiecutter there is a command to do the linting:

    make lint-fix

Otherwise you can run the commands:

    black .
    isort .
    flake8

Documentation is build using [Sphinx](https://www.sphinx-doc.org/en/master/) and docstrings should follow the [Sphinx Markup](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#python-signatures)
