# Testing Tests

Project for showcasing pytest features.

## Setup

### Virtual Environment

This project uses [poetry](https://python-poetry.org/) for dependency management.

```shell
$ poetry install
```

### Git Hooks

Only relevant when developing on this project.

```shell
$ git config --local core.hooksPath .hooks/
```


## Run

Run all tests and include coverage report (configured in `pyproject.toml`):

```shell
$ # -x: stop on first failure, -v: verbose
$ poetry run python -m pytest -xv
```

Filter by test naming:

```shell
$ poetry run python -m pytest -xv -k "test_print_hi"
```

Filter by test parametrization values:

```shell
$ poetry run python -m pytest -xv -k "test_print_hi[bob-world]"
$ poetry run python -m pytest -xv -k "test_print_hi and alice-"
$ poetry run python -m pytest -xv -k "test_fibonacci and fibonacci_recursive-"
```
