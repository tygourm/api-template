from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles

from src.api_template.adapters.api.auth import router as auth_router
from src.api_template.logger import get_logger
from src.api_template.settings import settings

logger = get_logger("main")
app = FastAPI(
    debug=settings.debug,
    title=settings.title,
    version=settings.version,
    docs_url=None,
    redoc_url=None,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/api-docs", include_in_schema=False)
async def api_docs() -> HTMLResponse:
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=settings.title,
        swagger_js_url="/static/docs/swagger-ui-bundle.js",
        swagger_css_url="/static/docs/swagger-ui.css",
        swagger_favicon_url="/static/site/img/favicon.svg",
    )


@app.get("/", include_in_schema=False)
async def redirect() -> RedirectResponse:
    return RedirectResponse(url="/app-docs/index.html")


@app.get("/app-docs", include_in_schema=False)
async def app_docs_root() -> RedirectResponse:
    return RedirectResponse(url="/app-docs/index.html")


@app.get("/app-docs/{path:path}", include_in_schema=False)
async def app_docs(path: str | None) -> Response:
    file = Path.cwd() / "static" / "site" / path
    if not file.is_file():
        return RedirectResponse(url="/app-docs/index.html")
    return FileResponse(file)


def main() -> None:
    import uvicorn  # noqa: PLC0415 import-outside-top-level

    logger.info("Starting application...")
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        workers=settings.workers,
        log_level=settings.logs_level.lower(),
    )


if __name__ == "__main__":
    main()  # pragma: no cover
