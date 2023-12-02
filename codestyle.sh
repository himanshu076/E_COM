#!/bin/bash

# Code formatting - iporting pyproject.toml file all variale here.
black . --config=pyproject.toml

# Import sorting
isort --atomic **/*.py

# Linting
flake8 --config=.flake8
