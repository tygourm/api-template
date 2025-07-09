from uuid import uuid4

from playwright.sync_api import APIRequestContext

from src.api_template.injector import injector
from src.api_template.settings import settings


def test_auth(api_request_context: APIRequestContext) -> None:
    # Sign up 201
    response = api_request_context.post("/auth/sign-up", data={"username": "username", "password": "P@ssW0rd1234"})
    assert response.status == 201

    # Sign up with existing username 422
    response = api_request_context.post("/auth/sign-up", data={"username": "username", "password": "P@ssW0rd1234"})
    assert response.status == 422

    # Sign in with non-existing username 400
    response = api_request_context.post("/auth/sign-in", data={"username": "uzername", "password": "P@ssW0rd1234"})
    assert response.status == 400

    # Sign in with bad password 400
    response = api_request_context.post("/auth/sign-in", data={"username": "username", "password": "P@zzW0rd1234"})
    assert response.status == 400

    # Sign in 200
    response = api_request_context.post("/auth/sign-in", data={"username": "username", "password": "P@ssW0rd1234"})
    assert response.status == 200
    token = response.text()

    # Get user without token 401
    response = api_request_context.get("/auth/user")
    assert response.status == 401

    # Get user with non-existing user id 401
    bad_token = injector.jwt_service.encode({"sub": str(uuid4())}, settings.jwt_key, settings.jwt_expires_in_seconds)
    response = api_request_context.get("/auth/user", headers={"Authorization": f"Bearer {bad_token}"})
    assert response.status == 401

    # Get user 200
    response = api_request_context.get("/auth/user", headers={"Authorization": f"Bearer {token}"})
    assert response.status == 200
    user = response.json()
    assert user["id"] is not None
    assert user["created_at"] is not None
    assert user["updated_at"] is not None
    assert user["username"] == "username"
