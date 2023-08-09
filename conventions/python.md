---
title: python
author: "João dos Santos"
layout: default
permalink: /conventions/python
---

# Conventions relating to _Python Projects_

## Creating a project


### Dependency Manager <a name="dependency-manager"></a>

We recommend using [poetry](https://python-poetry.org/docs/) as the dependency manager for Python projects. Poetry helps to manage project dependencies and environments effectively, which can improve productivity and reduce conflicts between dependencies.

### Linting Rules <a name="linting-rules"></a>

Our projects adhere to the default settings provided by [Flake8](https://github.com/PyCQA/flake8).
We also use [Black](https://github.com/psf/black) and [isort](https://github.com/PyCQA/isort) for code formatting.
The only deviation from the default settings is that we set the maximum line length to 79 characters. These tools help maintain code quality and consistency across the project.
### Testing <a name="testing"></a>

Maintaining a high test coverage is crucial for ensuring code quality and catching bugs early. We aim for an overall test coverage of at least 90% and a minimum of 85% test coverage for each file. Test coverage reports can help identify areas of the code that are not adequately tested and need more attention.

### Project Template <a name="project-template"></a>

We provide a cookiecutter/template for new Python projects, available [here](https://github.com/vliz-be-opsci/cookiecutter-py-module).
This template helps to set up new projects quickly and ensures they follow our conventions.


### Committing and Adhering to Standards <a name="contribuiting"></a>

Our project template includes a Makefile that helps developers adhere to these conventions. The Makefile provides commands for setting up the development environment, applying and checking linting rules, and running tests and checking test coverage.

To start using the project (as a developer), run:

    make init-dev

This command installs all necessary tools for working on the project and sets up a pre-commit hook.
The pre-commit hook ensures that you can't commit changes that do not adhere to these conventions.

To apply the linting rules, run:

    make lint-fix


To check the linting rules, run:

    make lint-check

To run the tests and check test coverage, run:

    make test-coverage



If you are not using the cookiecutter, you can run the linting commands manually:
    black .
    isort .
    flake8

### Documentation <a name="documentation"></a>

We use [Sphinx](https://www.sphinx-doc.org/en/master/) to build project documentation. Docstrings should follow the [Sphinx Markup](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#python-signatures) conventions. Good documentation is crucial for maintaining and understanding the codebase, especially as projects grow and more developers contribute.

Remember, these conventions are in place to help maintain high-quality, consistent code across all our Python projects. They are not meant to be restrictive, but rather to provide a guide for best practices and consistency.

Sources:
- docs.python-guide.org
-    realpython.com
-    blog.pronus.io
-    sourcery.ai
-    about.gitlab.com
-    conventionalcommits.org/en/v1.0.0/