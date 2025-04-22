import pytest
from utils_methods import UtilsMethods
from api_methods import ApiMethod
import data

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
    payload = user.create_user()
    response = user.auth_user(payload["email"], payload["password"])
    token = response.json()['accessToken']

    yield token, payload

    if "email" in payload and "password" in payload:
        ApiMethod.api_method_delete_user(token)

@pytest.fixture
def ingredient():
    ingredient = data.INGREDIENT_DATA
    return ingredient

