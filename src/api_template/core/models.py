from datetime import UTC, datetime
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class Model(SQLModel):
    id: UUID = Field(uuid4(), primary_key=True)
    created_at: datetime = Field(datetime.now(UTC), nullable=False)
    updated_at: datetime = Field(datetime.now(UTC), nullable=False)


class UserModel(Model, table=True):
    __tablename__ = "users"
    username: str = Field(max_length=16, nullable=False, unique=True, index=True)
    password: str = Field(min_length=60, max_length=60, nullable=False)
