# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.order import Order  # noqa: E501
from swagger_server.models.order_input import OrderInput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOrdersController(BaseTestCase):
    """OrdersController integration test stubs"""

    def test_orders_get(self):
        """Test case for orders_get

        Получение списка заказов пользователя
        """
        response = self.client.open(
            '/v1/orders',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_orders_post(self):
        """Test case for orders_post

        Создание нового заказа
        """
        body = OrderInput()
        response = self.client.open(
            '/v1/orders',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
