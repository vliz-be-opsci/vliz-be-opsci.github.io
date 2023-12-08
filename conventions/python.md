---
title: python
author: "João dos Santos"
graph_logo_bg: true
layout: default
permalink: /conventions/python
description: "Python is a popular programming language for building web applications. Learn about Python conventions and best practices."
---

# Conventions relating to _Python Projects_

## Creating a project


### Dependency Manager <a name="dependency-manager"></a>

We recommend using [poetry](https://python-poetry.org/docs/){:target=”_blank”} as the dependency manager for Python projects. Poetry helps to manage project dependencies and environments effectively, which can improve productivity and reduce conflicts between dependencies.

### Linting Rules <a name="linting-rules"></a>

Our projects adhere to the default settings provided by [Flake8](https://github.com/PyCQA/flake8){:target=”_blank”}.
We also use [Black](https://github.com/psf/black) and [isort](https://github.com/PyCQA/isort){:target=”_blank”} for code formatting.
The only deviation from the default settings is that we set the maximum line length to 79 characters. These tools help maintain code quality and consistency across the project.

### Testing <a name="testing"></a>

Maintaining a high test coverage is crucial for ensuring code quality and catching bugs early. We aim for an overall test coverage of at least 90% and a minimum of 85% test coverage for each file. Test coverage reports can help identify areas of the code that are not adequately tested and need more attention.

### Project Template <a name="project-template"></a>

We provide a cookiecutter/template for new Python projects, available [here](https://github.com/vliz-be-opsci/cookiecutter-py-module){:target=”_blank”}.
This template helps to set up new projects quickly and ensures they follow our conventions.


### Committing and Adhering to Standards <a name="contribuiting"></a>

Our project template includes a Makefile that helps developers adhere to these conventions. The Makefile provides commands for setting up the development environment, applying and checking linting rules, and running tests and checking test coverage.

To start using the project (as a developer), run:

```bash
    make init-dev
```

This command installs all necessary tools for working on the project and sets up a pre-commit hook.
The pre-commit hook ensures that you can't commit changes that do not adhere to these conventions.

To apply the linting rules, run:

```bash
    make lint-fix
```

To check the linting rules, run:

```bash
    make lint-check
```

To run the tests and check test coverage, run:

```bash
    make test-coverage
```

If you are not using the cookiecutter, you can run the linting commands manually:
```bash
    black .
    isort .
    flake8
```

### Documentation <a name="documentation"></a>

We use [Sphinx](https://www.sphinx-doc.org/en/master/) to build project documentation. Docstrings should follow the [Sphinx Markup](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html#python-signatures){:target=”_blank”} conventions. Good documentation is crucial for maintaining and understanding the codebase, especially as projects grow and more developers contribute.

Remember, these conventions are in place to help maintain high-quality, consistent code across all our Python projects. They are not meant to be restrictive, but rather to provide a guide for best practices and consistency.

Sources:
- docs.python-guide.org
-    realpython.com
-    blog.pronus.io
-    sourcery.ai
-    about.gitlab.com
-    conventionalcommits.org/en/v1.0.0/


### Code Authoring Style

We realise multiple valid solutions exist in coding, and we should be accepting a large variety of preference in expresiveness.  Still, a common style largely creates a shared ownership and affinity with the achievements we want to support as a group.  They also reduce the amount of "surprise" and thus needed time to learn yet another style.

There for we try to stick to these **strong** suggestions:

#### snake_case 

Names of variables and functions should use snake_case


#### `pathlib` over `os.path`

Targeting python3 we prefer using the pathlib.Path over the older os.path library.  We embrace the overloaded `/` construc allowing us to have platform-portable path joins from practically 'devision' between Path objects and their subpaths (provided as Path or string) 

#### `f"{var}"` string expansion over `"..." % ()` or `"...".format()` 

The instant semantic-role description and clarity of the variable replacement is what we prefer.

#### design by contract style

Modules and functions should be introduced in a well documented manner that focus on introducing some clear service "contract".  These contracts are captured through:
* well chosen names for both the functions and their arguments; and should be completed through:
* clear pre-conditions (expected prior state of system and arguments)
* clear postconditions (guaranteed state transitions completed by the service requests)
* useful invariants (documented overall guarantees that are always assured)
* declared exceptions indicating accepted failures to comply to the contract.

The sum of all these expose the 'contact surface' of our services, and account for our commitment towards backward compatibility: what we expose can be called upon by clients and thus, can not simply be changed in a non-compatible way - contract-changes leak through dependent clients needing to evolve with new versions.  Something which should be avoided at all times.

In practice these contracts are to be managed through:
* hiding implementation details in subclasses
* marking `private` parts of the implmentation through `_` (underscore) -prefixed members
* introducing (and only exposing) ABC classes that depict the method signatures
* introducing limited `__init__.py` exposure on the package level


#### type-hints about

One very specific element of the above is to provide type-hints where we can.
* Any introduction of a variable (potentially as function argument) should have a `: type` indication.
* Return types of functions should have an explicit `--> type :` indication.
