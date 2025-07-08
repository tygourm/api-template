from uuid import UUID

from sqlmodel import select

from src.api_template.core.models import UserModel
from src.api_template.core.session import get_session
from src.api_template.ports.user import User, UserRepository


class DBUserRepository(UserRepository):
    def create(self, username: str, password: str) -> User:
        model = UserModel(username=username, password=password)
        with next(get_session()) as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return User(**model.model_dump())

    def read_by_id(self, user_id: UUID) -> User | None:
        statement = select(UserModel).where(UserModel.id == user_id)
        with next(get_session()) as session:
            if model := session.exec(statement).first():
                return User(**model.model_dump())
            return None

    def read_by_username(self, username: str) -> User | None:
        statement = select(UserModel).where(UserModel.username == username)
        with next(get_session()) as session:
            if model := session.exec(statement).first():
                return User(**model.model_dump())
            return None
