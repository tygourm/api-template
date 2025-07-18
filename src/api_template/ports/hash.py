from abc import ABC, abstractmethod


class HashService(ABC):
    @abstractmethod
    def hash(self, value: str) -> str:
        pass

    @abstractmethod
    def check(self, value: str, hashed: str) -> bool:
        pass
