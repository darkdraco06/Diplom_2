import allure
import pytest
from api_methods import ApiMethod
import error_message
import data


class TestEditUser:
    @allure.title('Проверяем изменение информации email или name пользователя')
    @allure.description('Отправляем запрос на изменение email или name пользователя. Проверяем что данные выбранного параметра изменились')
    @pytest.mark.parametrize("key, value", [
        [data.TEST_NEM_NAME_KEY, data.TEST_NEW_EMAIL_VALUE],
        [data.TEST_NEM_NAME_KEY, data.TEST_NEW_NAME_VALUE]
    ])
    def test_user_edit_one_parametr_user_info_edited(self, user_auth, key, value):
        token,user = user_auth
        ApiMethod.api_method_create_user(user)
        response_edit = ApiMethod.api_method_user_edit_with_auth(token, f'{key}', f'{value}')
        response_get_info_user = ApiMethod.api_method_get_info_user(token)
        user[f"{key}"] = f"{value}"
        assert response_edit.status_code == 200
        assert response_edit.json()["success"] == True and response_get_info_user.json()["user"][f"{key}"] == f"{value}"

    @allure.title('Проверяем изменение информации email или name пользователя без авторизации')
    @allure.description('Отправляем запрос на изменение email и name пользователя без предварительной авторизации. Проверяем что при выполнении запроса возвращается код 401 и текст ошибки соотвествует документации')
    def test_user_edit_no_auth_one_parametr_error_edited(self):
        response_edit = ApiMethod.api_method_user_edit_no_auth( 'email@mail.ru', 'new_name_test')
        assert response_edit.json()["message"] == error_message.ERROR_MESSAGE_EDIT_USER and response_edit.status_code == 401