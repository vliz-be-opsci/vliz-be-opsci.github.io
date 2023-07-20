---
title: python
author: "João Pinto"
layout: default
permalink: /conventions/python
---

# Conventions relating to _Python Projects_

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
