from dataclasses import asdict
from datetime import datetime
from uuid import UUID

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

from src.api_template.core.errors import BadCredentialsError, UserDoesNotExistError, UsernameAlreadyExistsError
from src.api_template.injector import injector
from src.api_template.logger import get_logger

router = APIRouter()
logger = get_logger("auth")
auth_use_case = injector.auth_use_case


class Credentials(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: UUID
    created_at: datetime
    updated_at: datetime
    username: str


@router.post("/sign-up")
async def sign_up(credentials: Credentials) -> PlainTextResponse:
    try:
        token = auth_use_case.sign_up(credentials.username, credentials.password)
        logger.info("User %s signed up", credentials.username)
        return PlainTextResponse(token, status.HTTP_201_CREATED)
    except UsernameAlreadyExistsError as e:
        logger.exception("Username %s already exists", credentials.username)
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY) from e
    except Exception as e:
        logger.exception("Internal server error")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR) from e


@router.post("/sign-in")
async def sign_in(credentials: Credentials) -> PlainTextResponse:
    try:
        token = auth_use_case.sign_in(credentials.username, credentials.password)
        logger.info("User %s signed in", credentials.username)
        return PlainTextResponse(token)
    except BadCredentialsError as e:
        logger.exception("Bad credentials for username %s", credentials.username)
        raise HTTPException(status.HTTP_400_BAD_REQUEST) from e
    except Exception as e:
        logger.exception("Internal server error")
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR) from e


@router.get("/user")
async def get_user(request: Request) -> UserResponse:
    if token := request.headers.get("Authorization"):
        try:
            user = auth_use_case.get_user(token.split(" ")[1])
            return UserResponse(**asdict(user))
        except UserDoesNotExistError as e:
            logger.exception("User does not exist for token %s", token)
            raise HTTPException(status.HTTP_401_UNAUTHORIZED) from e
        except Exception as e:
            logger.exception("Internal server error")
            raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR) from e
    raise HTTPException(status.HTTP_401_UNAUTHORIZED)
