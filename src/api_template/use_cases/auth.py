from uuid import UUID

from src.api_template.core.errors import (
    BadCredentialsError,
    UserDoesNotExistError,
    UsernameAlreadyExistsError,
)
from src.api_template.ports.hash import HashService
from src.api_template.ports.jwt import JwtService
from src.api_template.ports.user import User, UserRepository
from src.api_template.settings import settings


class AuthUseCase:
    def __init__(
        self,
        user_repository: UserRepository,
        hash_service: HashService,
        jwt_service: JwtService,
    ) -> None:
        self.user_repository = user_repository
        self.hash_service = hash_service
        self.jwt_service = jwt_service

    def sign_up(self, username: str, password: str) -> str:
        if self.user_repository.read_by_username(username) is not None:
            raise UsernameAlreadyExistsError
        user = self.user_repository.create(username, self.hash_service.hash(password))
        return self.jwt_service.encode(
            {"sub": str(user.id)}, settings.jwt_key, settings.jwt_expires_in_seconds
        )

    def sign_in(self, username: str, password: str) -> str:
        user = self.user_repository.read_by_username(username)
        if user is None:
            raise BadCredentialsError
        if not self.hash_service.check(password, user.password):
            raise BadCredentialsError
        return self.jwt_service.encode(
            {"sub": str(user.id)}, settings.jwt_key, settings.jwt_expires_in_seconds
        )

    def get_user(self, token: str) -> User:
        payload = self.jwt_service.decode(token, settings.jwt_key)
        user = self.user_repository.read_by_id(UUID(payload["sub"]))
        if user is None:
            raise UserDoesNotExistError
        return user
