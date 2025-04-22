from api_methods import ApiMethod
import allure
import error_message


class TestCreateOrder:

    @allure.title('Проверяем создание заказа под авторизованным пользователем')
    @allure.description('Под авторизованным пользователем отправляем запрос на создание заказа. Проверяем что заказ создан и код ответа 200')
    def test_create_order_two_ingredient_order_created(self, user_auth, ingredient):
        token, user = user_auth
        response_order = ApiMethod.api_method_create_order_auth(token, ingredient[0], ingredient[1])
        assert response_order.json()['success'] == True and response_order.status_code == 200

    @allure.title('Проверяем создание заказа без авторизации')
    @allure.description('Отправляем запрос на создание заказа без пользователя. Проверяем что заказ создан и код ответа 200')
    def test_create_order_two_ingredient_no_token_order_created(self, ingredient):
        response_order = ApiMethod.api_method_create_order_no_auth(ingredient[0], ingredient[1])
        assert response_order.json()['success'] == True and response_order.status_code == 200

    @allure.title('Проверяем создание заказа под авторизованным пользователем без ингридиентов')
    @allure.description('Под авторизованным пользователем отправляем запрос на создание заказа без ингридиентов. Проверяем что заказ не создался, код ответа 400 и текст ошибки соовтетсвует документации')
    def test_create_order_no_ingredient_order_error_response(self, user_auth):
        token, user = user_auth
        response_order = ApiMethod.api_method_create_order_auth_no_ingredients(token)
        assert response_order.json()['success'] == False and response_order.status_code == 400
        assert response_order.json()['message'] == error_message.ERROR_MESSAGE_NO_INGREDIENT

    @allure.title('Проверяем создание заказа под авторизованным пользователем и неверными хешами ингридиентов')
    @allure.description('Под авторизованным пользователем отправляем запрос на создание заказа указав не вреные хеши ингридиентов. Проверяем что заказ не создан и код ответа 500')
    def test_create_order_incorrect_two_hash_order_error_response(self, user_auth):
        token, user = user_auth
        response_order = ApiMethod.api_method_create_order_auth(token, "124", "123")
        assert response_order.status_code == 500
