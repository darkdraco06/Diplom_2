import pytest
from utils_methods import UtilsMethods
from api_methods import ApiMethod


@pytest.fixture
def user():
    user = UtilsMethods()
    payload = user.generate_random_data_user_json()
    yield payload

    if "email" in payload and "password" in payload:
        user.delete_user(payload["email"], payload["password"])

@pytest.fixture
def user_auth():
    user = UtilsMethods()
    user_data = user.create_user()
    response = user.auth_user(user_data["email"], user_data["password"])
    token = response.json()['accessToken']
    yield token

    if "email" in user_data and "password" in user_data:
        ApiMethod.api_method_delete_user(token)

@pytest.fixture
def ingredient():
    ingredient = ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa72"]
    return ingredient

