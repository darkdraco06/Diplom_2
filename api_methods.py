import requests
import curl
import allure


class ApiMethod:

    @staticmethod
    @allure.step('Выполняем запрос на создание пользователя')
    def api_method_create_user(payload):
        return requests.post(f'{curl.CREATE_USER}', data=payload)

    @staticmethod
    @allure.step('Выполняем запрос на удаление пользователя')
    def api_method_delete_user(token):
        return requests.delete(f'{curl.GET_AND_PATH_USER_DATA}', headers={'Authorization': f'{token}'})

    @staticmethod
    @allure.step('Выполняем авторизацию пользователя')
    def api_method_login_user(email, password):
        return requests.post(f'{curl.LOGIN_USER}', json={'email': email, 'password': password})

    @staticmethod
    @allure.step('Выполняем обновление данных для пользователя с авторизацией')
    def api_method_user_edit_with_auth(token, parametr_key, parametr_new_value):
        return requests.patch(f'{curl.GET_AND_PATH_USER_DATA}', json={f'{parametr_key}': f'{parametr_new_value}'}, headers={'Authorization': f'{token}'})

    @staticmethod
    @allure.step('Выполняем обновление данных для пользователя без авторизации')
    def api_method_user_edit_no_auth(parametr_key, parametr_new_value):
        return requests.patch(f'{curl.GET_AND_PATH_USER_DATA}', json={f'{parametr_key}': f'{parametr_new_value}'})

    @staticmethod
    @allure.step('Получаем информацию о пользователе')
    def api_method_get_info_user(token):
        return requests.get(f'{curl.GET_AND_PATH_USER_DATA}', headers={'Authorization': f'{token}'})

    @staticmethod
    @allure.step('Получаем информацию об ингредиентах')
    def api_method_get_ingredients():
        return requests.get(f'{curl.GET_INGREDIENTS}')

    @staticmethod
    @allure.step('Создаем заказ с ингридиентами под авторизованным пользователем')
    def api_method_create_order_auth(token, ingredient_1, ingredient_2):
        return requests.post(f'{curl.CREATE_ORDER}', json={"ingredients": [f"{ingredient_1}",f"{ingredient_2}"]}, headers={'Authorization': f'{token}'})

    @staticmethod
    @allure.step('Создаем заказ с ингридиентами без авторизации')
    def api_method_create_order_no_auth(ingredient_1, ingredient_2):
        return requests.post(f'{curl.CREATE_ORDER}', json={"ingredients": [f"{ingredient_1}",f"{ingredient_2}"]})

    @staticmethod
    @allure.step('Создаем заказ под авторизованным пользователем без ингридентов')
    def api_method_create_order_auth_no_ingredients(token):
        return requests.post(f'{curl.CREATE_ORDER}', headers={'Authorization': f'{token}'})

    @staticmethod
    @allure.step('Выполняем запрос на получение заказов авторизованного пользователя')
    def api_method_get_user_orders_auth(token):
        return requests.get(f'{curl.USER_ORDER}', headers={'Authorization': f'{token}'})

    @staticmethod
    @allure.step('Выполняем запрос на получение заказов не авторизованного пользователя')
    def api_method_get_user_orders_no_auth():
        return requests.get(f'{curl.USER_ORDER}')