from uuid import uuid4

from playwright.sync_api import APIRequestContext


def test_api_docs(api_request_context: APIRequestContext) -> None:
    # Get api-docs 200
    reponse = api_request_context.get("/api-docs")
    assert reponse.status == 200


def test_app_docs(api_request_context: APIRequestContext) -> None:
    # Get root 200 redirects to app-docs index
    reponse = api_request_context.get("")
    assert reponse.status == 200
    assert reponse.url == "http://localhost:8000/app-docs/index.html"

    # Get app-docs 200 redirects to app-docs index
    reponse = api_request_context.get("/app-docs")
    assert reponse.status == 200
    assert reponse.url == "http://localhost:8000/app-docs/index.html"

    # Get app-docs with non-existing path 200 redirects to app-docs index
    reponse = api_request_context.get(f"/app-docs/{uuid4()}.html")
    assert reponse.status == 200
    assert reponse.url == "http://localhost:8000/app-docs/index.html"

    # Get app-docs 200
    reponse = api_request_context.get("/app-docs/index.html")
    assert reponse.status == 200
    assert reponse.url == "http://localhost:8000/app-docs/index.html"
