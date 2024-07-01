# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.7.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2024. ThingsBoard
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

class ResetPasswordRequest(object):
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
        'reset_token': 'str',
        'password': 'str'
    }

    attribute_map = {
        'reset_token': 'resetToken',
        'password': 'password'
    }

    def __init__(self, reset_token=None, password=None):  # noqa: E501
        """ResetPasswordRequest - a model defined in Swagger"""  # noqa: E501
        self._reset_token = None
        self._password = None
        self.discriminator = None
        if reset_token is not None:
            self.reset_token = reset_token
        if password is not None:
            self.password = password

    @property
    def reset_token(self):
        """Gets the reset_token of this ResetPasswordRequest.  # noqa: E501

        The reset token to verify  # noqa: E501

        :return: The reset_token of this ResetPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._reset_token

    @reset_token.setter
    def reset_token(self, reset_token):
        """Sets the reset_token of this ResetPasswordRequest.

        The reset token to verify  # noqa: E501

        :param reset_token: The reset_token of this ResetPasswordRequest.  # noqa: E501
        :type: str
        """

        self._reset_token = reset_token

    @property
    def password(self):
        """Gets the password of this ResetPasswordRequest.  # noqa: E501

        The new password to set  # noqa: E501

        :return: The password of this ResetPasswordRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this ResetPasswordRequest.

        The new password to set  # noqa: E501

        :param password: The password of this ResetPasswordRequest.  # noqa: E501
        :type: str
        """

        self._password = password

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
        if issubclass(ResetPasswordRequest, dict):
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
        if not isinstance(other, ResetPasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
