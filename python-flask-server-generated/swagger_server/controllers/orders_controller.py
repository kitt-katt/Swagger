import connexion
import six

from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.order_input import OrderInput  # noqa: E501
from swagger_server import util


def orders_get():  # noqa: E501
    """Получение списка заказов пользователя

     # noqa: E501


    :rtype: List[Order]
    """
    return 'do some magic!'


def orders_post(body):  # noqa: E501
    """Создание нового заказа

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Order
    """
    if connexion.request.is_json:
        body = OrderInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
