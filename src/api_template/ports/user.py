from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID


@dataclass
class User:
    id: UUID
    created_at: datetime
    updated_at: datetime
    username: str
    password: str


class UserRepository(ABC):
    @abstractmethod
    def create(self, username: str, password: str) -> User:
        pass

    @abstractmethod
    def read_by_id(self, user_id: UUID) -> User | None:
        pass

    @abstractmethod
    def read_by_username(self, username: str) -> User | None:
        pass
