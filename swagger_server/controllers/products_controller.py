import connexion
import six

from swagger_server.models.product import Product  # noqa: E501
from swagger_server.models.product_input import ProductInput  # noqa: E501
from swagger_server import util


def products_get():  # noqa: E501
    """Получение списка товаров

     # noqa: E501


    :rtype: List[Product]
    """
    return 'do some magic!'


def products_post(body):  # noqa: E501
    """Добавление нового товара

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Product
    """
    if connexion.request.is_json:
        body = ProductInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def products_product_id_delete(product_id):  # noqa: E501
    """Удаление товара

     # noqa: E501

    :param product_id: 
    :type product_id: str

    :rtype: None
    """
    return 'do some magic!'


def products_product_id_get(product_id):  # noqa: E501
    """Получение информации о товаре

     # noqa: E501

    :param product_id: Идентификатор товара
    :type product_id: str

    :rtype: Product
    """
    return 'do some magic!'


def products_product_id_put(body, product_id):  # noqa: E501
    """Обновление товара

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param product_id: 
    :type product_id: str

    :rtype: Product
    """
    if connexion.request.is_json:
        body = ProductInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
