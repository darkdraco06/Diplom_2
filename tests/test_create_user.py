import error_message
from api_methods import ApiMethod
import allure
import pytest


class TestCreateUser:

    @allure.title('Проверяем создание пользователя')
    @allure.description('Отправляем запрос на создание пользователя. Проверяем что при создании пользователя получаем код ответа 200')
    def test_create_user_one_user_user_created(self, user):
        response = ApiMethod.api_method_create_user(user)
        assert response.json()['success'] == True and response.status_code == 200

    @allure.title('Проверяем создание пользователя c email который уже зарегистрирован')
    @allure.description('Отправляем запрос на создание пользователя. Затем повторяем запрос еще раз с теми же данными. Проверяем что при создании пользователя получаем код ответа 403 и текст ответа ошибки соовтетвует документации')
    def test_create_user_two_identical_user_error_create(self, user):
        response_user1 = ApiMethod.api_method_create_user(user)
        response_user2 = ApiMethod.api_method_create_user(user)
        assert response_user2.status_code == 403 and response_user2.json()['message'] == error_message.ERROR_MESSAGE_CREATE_USER_ALREADY

    @allure.title('Проверяем создание пользователя без логина и пароля')
    @allure.description('Отправляем запрос на создание пользователя не указав логин или пароль. Проверяем что при создании пользователя получаем код ответа 403 и текст ответа ошибки соовтетвует документации')
    @pytest.mark.parametrize("no_data_for_create", [
                                    {"email": "", "password": "test_password", "name": "test_name"},
                                    {"email": "test_mail@test.com", "password": "", "name": "test_name"}])
    def test_create_user_no_mail_password_error_create(self, no_data_for_create):
        response = ApiMethod.api_method_create_user(no_data_for_create)
        assert response.status_code == 403 and response.json()['message'] == error_message.ERROR_MESSAGE_CREATE_USER_NO_DATA