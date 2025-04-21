from api_methods import ApiMethod
import allure
import error_message


class TestUserOrders:

    @allure.title('Проверяем получение заказов авторизованного пользователя')
    @allure.description('Авторизовываемся и отправляем запрос на получение заказов пользователя. Проверяем что возвращается код 200 и что список заказов получен')
    def test_user_order_auth_user_orders_received(self, user_auth):
        response = ApiMethod.api_method_get_user_orders_auth(user_auth)
        assert response.json()['success'] == True and response.status_code == 200

    @allure.title('Проверяем получение заказов без авторизации пользователя')
    @allure.description('Не авторизовываемся и отправляем запрос на получение заказов. Проверяем что возвращается код 401 и что текст ошибки соответсвует документации')
    def test_user_order_no_auth_user_error_code(self):
        response = ApiMethod.api_method_get_user_orders_no_auth()
        assert response.json()['success'] == False and response.status_code == 401
        assert response.json()['message'] == error_message.ERROR_MESSAGE_USER_ORDER_NO_AUTH