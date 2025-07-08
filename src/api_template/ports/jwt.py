from abc import ABC, abstractmethod


class JwtService(ABC):
    @abstractmethod
    def encode(self, payload: dict, key: str, expires_in_seconds: int) -> str:
        pass  # pragma: no cover

    @abstractmethod
    def decode(self, token: str, key: str) -> dict:
        pass  # pragma: no cover
