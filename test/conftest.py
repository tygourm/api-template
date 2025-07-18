import multiprocessing
from collections.abc import Generator
from pathlib import Path

import pytest
from playwright.sync_api import APIRequestContext, Playwright
from testcontainers.postgres import PostgresContainer

import main


@pytest.fixture(scope="session")
def postgres() -> Generator[PostgresContainer]:
    container = PostgresContainer(
        "postgres:17.5-alpine",
        5432,
        "postgres",
        "CHANGEME",
        "db",
    )
    container.with_bind_ports(5432, 5432)
    container.with_volume_mapping(
        Path.cwd() / "initdb.sql",
        "/docker-entrypoint-initdb.d/initdb.sql",
    )
    with container:
        yield container


@pytest.fixture(scope="session")
def app(postgres: PostgresContainer) -> Generator[str]:
    main.settings.database_url = postgres.get_connection_url()
    process = multiprocessing.Process(target=main.main)
    process.start()
    yield "http://localhost:8000"
    process.terminate()
    process.join()


@pytest.fixture
def api_request_context(
    app: str,
    playwright: Playwright,
) -> Generator[APIRequestContext]:
    context = playwright.request.new_context(base_url=app)
    yield context
    context.dispose()
