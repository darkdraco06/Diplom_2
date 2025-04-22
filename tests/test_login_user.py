from api_methods import ApiMethod
import allure
import pytest
import error_message
import data


class TestLoginUser:
    @allure.title('Проверяем успешную авторизацию пользователя')
    @allure.description('Отправляем запрос на авторизацию пользователя с верным логином и паролем. Проверяем что в ответе мы получаем success True и код ответа 200')
    def test_user_auth_correct_credential_auth_success(self, user_auth):
        token, user = user_auth
        ApiMethod.api_method_create_user(user)
        response_auth = ApiMethod.api_method_login_user(user['email'], user['password'])
        assert response_auth.json()['success'] == True and response_auth.status_code == 200

    @allure.title('Проверяем создание пользователя без логина и пароля')
    @allure.description('Отправляем запрос на создание пользователя не указав логин или пароль. Проверяем что при создании пользователя получаем код ответа 401 и текст ответа ошибки соовтетвует документации')
    @pytest.mark.parametrize("data_user", [
                                    data.NO_VALID_EMAIL_REGISTRATION,
                                    data.NO_VALID_PASSWORD_REGISTRATION
                                    ])
    def test_user_auth_incorrect_credential_error_auth(self, data_user):
        response_auth = ApiMethod.api_method_login_user(data_user['email'], data_user['password'])
        assert response_auth.status_code == 401 and response_auth.json()['message'] == error_message.ERROR_MESSAGE_LOGIN_USER_INCORRECT