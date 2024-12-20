# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.product_input import ProductInput  # noqa: F401,E501
from swagger_server import util


class OrderInput(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, products: List[ProductInput]=None):  # noqa: E501
        """OrderInput - a model defined in Swagger

        :param products: The products of this OrderInput.  # noqa: E501
        :type products: List[ProductInput]
        """
        self.swagger_types = {
            'products': List[ProductInput]
        }

        self.attribute_map = {
            'products': 'products'
        }
        self._products = products

    @classmethod
    def from_dict(cls, dikt) -> 'OrderInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OrderInput of this OrderInput.  # noqa: E501
        :rtype: OrderInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def products(self) -> List[ProductInput]:
        """Gets the products of this OrderInput.


        :return: The products of this OrderInput.
        :rtype: List[ProductInput]
        """
        return self._products

    @products.setter
    def products(self, products: List[ProductInput]):
        """Sets the products of this OrderInput.


        :param products: The products of this OrderInput.
        :type products: List[ProductInput]
        """
        if products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products
