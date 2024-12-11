# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.product import Product  # noqa: F401,E501
from swagger_server import util


class Order(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, user_id: str=None, products: List[Product]=None, total_price: float=None):  # noqa: E501
        """Order - a model defined in Swagger

        :param id: The id of this Order.  # noqa: E501
        :type id: str
        :param user_id: The user_id of this Order.  # noqa: E501
        :type user_id: str
        :param products: The products of this Order.  # noqa: E501
        :type products: List[Product]
        :param total_price: The total_price of this Order.  # noqa: E501
        :type total_price: float
        """
        self.swagger_types = {
            'id': str,
            'user_id': str,
            'products': List[Product],
            'total_price': float
        }

        self.attribute_map = {
            'id': 'id',
            'user_id': 'userId',
            'products': 'products',
            'total_price': 'totalPrice'
        }
        self._id = id
        self._user_id = user_id
        self._products = products
        self._total_price = total_price

    @classmethod
    def from_dict(cls, dikt) -> 'Order':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Order of this Order.  # noqa: E501
        :rtype: Order
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Order.


        :return: The id of this Order.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Order.


        :param id: The id of this Order.
        :type id: str
        """

        self._id = id

    @property
    def user_id(self) -> str:
        """Gets the user_id of this Order.


        :return: The user_id of this Order.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: str):
        """Sets the user_id of this Order.


        :param user_id: The user_id of this Order.
        :type user_id: str
        """

        self._user_id = user_id

    @property
    def products(self) -> List[Product]:
        """Gets the products of this Order.


        :return: The products of this Order.
        :rtype: List[Product]
        """
        return self._products

    @products.setter
    def products(self, products: List[Product]):
        """Sets the products of this Order.


        :param products: The products of this Order.
        :type products: List[Product]
        """

        self._products = products

    @property
    def total_price(self) -> float:
        """Gets the total_price of this Order.


        :return: The total_price of this Order.
        :rtype: float
        """
        return self._total_price

    @total_price.setter
    def total_price(self, total_price: float):
        """Sets the total_price of this Order.


        :param total_price: The total_price of this Order.
        :type total_price: float
        """

        self._total_price = total_price