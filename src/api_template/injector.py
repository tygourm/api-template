from typing import TYPE_CHECKING

from src.api_template.adapters.api.jwt import HS256JwtService
from src.api_template.adapters.db.hash import BcryptHashService
from src.api_template.adapters.db.user import DBUserRepository
from src.api_template.use_cases.auth import AuthUseCase

if TYPE_CHECKING:  # pragma: no cover
    from src.api_template.ports.hash import HashService
    from src.api_template.ports.jwt import JwtService
    from src.api_template.ports.user import UserRepository


class Injector:
    def __init__(self) -> None:
        # Repositories
        self.user_repository: UserRepository = DBUserRepository()

        # Services
        self.hash_service: HashService = BcryptHashService()
        self.jwt_service: JwtService = HS256JwtService()

        # Use cases
        self.auth_use_case = AuthUseCase(
            self.user_repository,
            self.hash_service,
            self.jwt_service,
        )


injector = Injector()
