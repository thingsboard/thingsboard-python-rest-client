# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2023. ThingsBoard
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import pprint
import re  # noqa: F401

import six

class JWTSettings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'token_expiration_time': 'int',
        'refresh_token_exp_time': 'int',
        'token_issuer': 'str',
        'token_signing_key': 'str'
    }

    attribute_map = {
        'token_expiration_time': 'tokenExpirationTime',
        'refresh_token_exp_time': 'refreshTokenExpTime',
        'token_issuer': 'tokenIssuer',
        'token_signing_key': 'tokenSigningKey'
    }

    def __init__(self, token_expiration_time=None, refresh_token_exp_time=None, token_issuer=None, token_signing_key=None):  # noqa: E501
        """JWTSettings - a model defined in Swagger"""  # noqa: E501
        self._token_expiration_time = None
        self._refresh_token_exp_time = None
        self._token_issuer = None
        self._token_signing_key = None
        self.discriminator = None
        if token_expiration_time is not None:
            self.token_expiration_time = token_expiration_time
        if refresh_token_exp_time is not None:
            self.refresh_token_exp_time = refresh_token_exp_time
        if token_issuer is not None:
            self.token_issuer = token_issuer
        if token_signing_key is not None:
            self.token_signing_key = token_signing_key

    @property
    def token_expiration_time(self):
        """Gets the token_expiration_time of this JWTSettings.  # noqa: E501

        The JWT will expire after seconds.  # noqa: E501

        :return: The token_expiration_time of this JWTSettings.  # noqa: E501
        :rtype: int
        """
        return self._token_expiration_time

    @token_expiration_time.setter
    def token_expiration_time(self, token_expiration_time):
        """Sets the token_expiration_time of this JWTSettings.

        The JWT will expire after seconds.  # noqa: E501

        :param token_expiration_time: The token_expiration_time of this JWTSettings.  # noqa: E501
        :type: int
        """

        self._token_expiration_time = token_expiration_time

    @property
    def refresh_token_exp_time(self):
        """Gets the refresh_token_exp_time of this JWTSettings.  # noqa: E501

        The JWT can be refreshed during seconds.  # noqa: E501

        :return: The refresh_token_exp_time of this JWTSettings.  # noqa: E501
        :rtype: int
        """
        return self._refresh_token_exp_time

    @refresh_token_exp_time.setter
    def refresh_token_exp_time(self, refresh_token_exp_time):
        """Sets the refresh_token_exp_time of this JWTSettings.

        The JWT can be refreshed during seconds.  # noqa: E501

        :param refresh_token_exp_time: The refresh_token_exp_time of this JWTSettings.  # noqa: E501
        :type: int
        """

        self._refresh_token_exp_time = refresh_token_exp_time

    @property
    def token_issuer(self):
        """Gets the token_issuer of this JWTSettings.  # noqa: E501

        The JWT issuer.  # noqa: E501

        :return: The token_issuer of this JWTSettings.  # noqa: E501
        :rtype: str
        """
        return self._token_issuer

    @token_issuer.setter
    def token_issuer(self, token_issuer):
        """Sets the token_issuer of this JWTSettings.

        The JWT issuer.  # noqa: E501

        :param token_issuer: The token_issuer of this JWTSettings.  # noqa: E501
        :type: str
        """

        self._token_issuer = token_issuer

    @property
    def token_signing_key(self):
        """Gets the token_signing_key of this JWTSettings.  # noqa: E501

        The JWT key is used to sing token. Base64 encoded.  # noqa: E501

        :return: The token_signing_key of this JWTSettings.  # noqa: E501
        :rtype: str
        """
        return self._token_signing_key

    @token_signing_key.setter
    def token_signing_key(self, token_signing_key):
        """Sets the token_signing_key of this JWTSettings.

        The JWT key is used to sing token. Base64 encoded.  # noqa: E501

        :param token_signing_key: The token_signing_key of this JWTSettings.  # noqa: E501
        :type: str
        """

        self._token_signing_key = token_signing_key

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(JWTSettings, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JWTSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
