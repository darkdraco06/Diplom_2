import random
import string
from api_methods import ApiMethod
import allure


class UtilsMethods:

    @allure.step('Генерируем случаныйе данные пользователя: email, password, name')
    def generate_random_data_user_json(self):

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        email = generate_random_string(7) + "@yandex.ru"
        password = generate_random_string(7)
        name = generate_random_string(7)

        payload = {
        "email": email,
        "password": password,
        "name": name
        }
        return payload

    @allure.step('Регистрация пользователя со случайными данными: email, password, name')
    def create_user(self):
        payload = self.generate_random_data_user_json()
        ApiMethod.api_method_create_user(payload)
        return payload

    @allure.step('Авторизация пользователя в системе и получение токена')
    def auth_user(self, email, password):
        return ApiMethod.api_method_login_user(email, password)

    @allure.step('Удаляем пользователя')
    def delete_user(self, email, password):
        response_auth = self.auth_user(email, password)
        return ApiMethod.api_method_delete_user(response_auth.json()['accessToken'])