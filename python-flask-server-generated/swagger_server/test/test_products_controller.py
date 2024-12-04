# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.product import Product  # noqa: E501
from swagger_server.models.product_input import ProductInput  # noqa: E501
from swagger_server.test import BaseTestCase


class TestProductsController(BaseTestCase):
    """ProductsController integration test stubs"""

    def test_products_get(self):
        """Test case for products_get

        Получение списка товаров
        """
        response = self.client.open(
            '/v1/products',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_post(self):
        """Test case for products_post

        Добавление нового товара
        """
        body = ProductInput()
        response = self.client.open(
            '/v1/products',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_product_id_delete(self):
        """Test case for products_product_id_delete

        Удаление товара
        """
        response = self.client.open(
            '/v1/products/{productId}'.format(product_id='product_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_product_id_get(self):
        """Test case for products_product_id_get

        Получение информации о товаре
        """
        response = self.client.open(
            '/v1/products/{productId}'.format(product_id='product_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_products_product_id_put(self):
        """Test case for products_product_id_put

        Обновление товара
        """
        body = ProductInput()
        response = self.client.open(
            '/v1/products/{productId}'.format(product_id='product_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
