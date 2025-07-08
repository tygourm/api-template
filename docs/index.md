# api-template

Yet another template.

!!! tip "Design principles"

    - **DRY** Don't Repeat Yourself
    - **KISS** Keep It Simple, Stupid
    - **YAGNI** You Ain't Gonna Need It
    - **SOLID** Single responsibility, Open/closed, Liskov substitution, Interface
    segregation, Dependency inversion

## Prerequisites

This project uses [uv](https://docs.astral.sh/uv) as a Python package and
project manager.

## Development

### Dependencies

Install Python dependencies.

```bash
uv sync --all-groups --frozen
```

Activate the virtual environment.

```bash
source .venv/bin/activate
```

!!! tip "Python & VS Code"

    - If dependencies are not recognized in VS Code, you can run the command
    `Ctrl+Shift+P > Python: Select Interpreter` and select `./.venv/bin/python`.
    - After updating the dependencies, you can run the command
    `Ctrl+Shift+P > Developer: Reload Window` to refresh the IDE.

### App

```bash
python main.py
```

### Test

This project uses [pytest](https://pypi.org/project/pytest) for testing and
[pytest-cov](https://pypi.org/project/pytest-cov) for code coverage.

```bash
pytest -p no:cacheprovider
```

!!! info "pytest cache"

    The `-p no:cacheprovider` option prevents pytest from using the cache, which
    makes the results more reliable. This is recommended for development but not
    mandatory, the CI will use it anyway.

## Deployment

Build the image.

```bash
docker build -t api-template .
```

Deploy the services.

```bash
docker compose up -d --build
```

## Miscellaneous

### Docs

This project uses
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material) as a
documentation framework.

```bash
mkdocs serve # Serve docs
mkdocs build -d static/site # Build docs
```

### Lint / Format

This project uses [Ruff](https://docs.astral.sh/ruff) as a Python linter and
code formatter.

```bash
ruff check --no-cache # Lint
ruff format --no-cache # Format
```

!!! info "Ruff cache"

    The `--no-cache` option prevents Ruff from using the cache, which makes the
    results more reliable. This is recommended for development but not mandatory,
    the CI will use it anyway.

!!! warning "Ruff version"

    The version of Ruff must match the one shipped with the `charliermarsh.ruff` VS
    Code extension.
