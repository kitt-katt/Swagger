import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.models.user_login import UserLogin  # noqa: E501
from swagger_server.models.user_registration import UserRegistration  # noqa: E501
from swagger_server import util


def users_login_post(body):  # noqa: E501
    """Логин пользователя

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = UserLogin.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def users_register_post(body):  # noqa: E501
    """Регистрация нового пользователя

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        body = UserRegistration.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
