# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_login import UserLogin  # noqa: E501
from swagger_server.models.user_registration import UserRegistration  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_users_login_post(self):
        """Test case for users_login_post

        Логин пользователя
        """
        body = UserLogin()
        response = self.client.open(
            '/v1/users/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_users_register_post(self):
        """Test case for users_register_post

        Регистрация нового пользователя
        """
        body = UserRegistration()
        response = self.client.open(
            '/v1/users/register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
