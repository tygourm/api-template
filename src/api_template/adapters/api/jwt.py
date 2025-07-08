from datetime import UTC, datetime, timedelta

import jwt

from src.api_template.ports.jwt import JwtService


class HS256JwtService(JwtService):
    def encode(self, payload: dict, key: str, expires_in_seconds: int) -> str:
        payload["exp"] = datetime.now(UTC) + timedelta(seconds=expires_in_seconds)
        return jwt.encode(payload, key, "HS256")

    def decode(self, token: str, key: str) -> dict:
        return jwt.decode(token, key, ["HS256"])
