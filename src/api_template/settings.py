from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = False
    workers: int = 1

    # App
    debug: bool = False
    title: str = "API Template"
    version: str = "1.0.0"

    # Logs
    logs_backup_count: int = 10
    logs_max_bytes: int = 10 * 1024 * 1024  # 10 MB
    logs_filename: str = "api-template.log"
    logs_format: str = "%(asctime)s [%(name)s] %(levelname)s %(message)s"
    logs_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    # Auth
    jwt_key: str = "CHANGEME"
    jwt_expires_in_seconds: int = 60 * 60  # 1 hour

    # Data
    database_url: str = "postgresql://postgres:CHANGEME@localhost:5432/db"

    model_config = SettingsConfigDict()


settings = Settings()
