from bcrypt import checkpw, gensalt, hashpw

from src.api_template.ports.hash import HashService


class BcryptHashService(HashService):
    def hash(self, value: str) -> str:
        hashed = hashpw(value.encode(), gensalt())
        return hashed.decode()

    def check(self, value: str, hashed: str) -> bool:
        return checkpw(value.encode(), hashed.encode())
