import allure
import pytest
from api_methods import ApiMethod
import error_message


class TestEditUser:
    @allure.title('Проверяем изменение информации email или name пользователя')
    @allure.description('Отправляем запрос на изменение email или name пользователя. Проверяем что данные выбранного параметра изменились')
    @pytest.mark.parametrize("key, value", [
        ["email","test_new_email@newemail.com"],
        ["name","test_new_name"]
    ])
    def test_user_edit_one_parametr_user_info_edited(self, user, key, value):
        ApiMethod.api_method_create_user(user)
        response_auth = ApiMethod.api_method_login_user(user['email'], user['password'])
        response_edit = ApiMethod.api_method_user_edit_with_auth(response_auth.json()["accessToken"], f'{key}', f'{value}')
        response_get_info_user = ApiMethod.api_method_get_info_user(response_auth.json()["accessToken"])
        user[f"{key}"] = f"{value}"
        assert response_edit.status_code == 200
        assert response_edit.json()["success"] == True and response_get_info_user.json()["user"][f"{key}"] == f"{value}"

    @allure.title('Проверяем изменение информации email или name пользователя без авторизации')
    @allure.description('Отправляем запрос на изменение email и name пользователя без предварительной авторизации. Проверяем что при выполнении запроса возвращается код 401 и текст ошибки соотвествует документации')
    def test_user_edit_no_auth_one_parametr_error_edited(self, user):
        ApiMethod.api_method_create_user(user)
        response_edit = ApiMethod.api_method_user_edit_no_auth( 'email@mail.ru', 'new_name_test')
        assert response_edit.json()["message"] == error_message.ERROR_MESSAGE_EDIT_USER and response_edit.status_code == 401