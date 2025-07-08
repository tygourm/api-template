# api-template

Yet another template.

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
