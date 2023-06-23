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

class TwoFaProviderInfo(object):
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
        'contact': 'str',
        'default': 'bool',
        'min_verification_code_send_period': 'int',
        'type': 'str'
    }

    attribute_map = {
        'contact': 'contact',
        'default': 'default',
        'min_verification_code_send_period': 'minVerificationCodeSendPeriod',
        'type': 'type'
    }

    def __init__(self, contact=None, default=None, min_verification_code_send_period=None, type=None):  # noqa: E501
        """TwoFaProviderInfo - a model defined in Swagger"""  # noqa: E501
        self._contact = None
        self._default = None
        self._min_verification_code_send_period = None
        self._type = None
        self.discriminator = None
        if contact is not None:
            self.contact = contact
        if default is not None:
            self.default = default
        if min_verification_code_send_period is not None:
            self.min_verification_code_send_period = min_verification_code_send_period
        if type is not None:
            self.type = type

    @property
    def contact(self):
        """Gets the contact of this TwoFaProviderInfo.  # noqa: E501


        :return: The contact of this TwoFaProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this TwoFaProviderInfo.


        :param contact: The contact of this TwoFaProviderInfo.  # noqa: E501
        :type: str
        """

        self._contact = contact

    @property
    def default(self):
        """Gets the default of this TwoFaProviderInfo.  # noqa: E501


        :return: The default of this TwoFaProviderInfo.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this TwoFaProviderInfo.


        :param default: The default of this TwoFaProviderInfo.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def min_verification_code_send_period(self):
        """Gets the min_verification_code_send_period of this TwoFaProviderInfo.  # noqa: E501


        :return: The min_verification_code_send_period of this TwoFaProviderInfo.  # noqa: E501
        :rtype: int
        """
        return self._min_verification_code_send_period

    @min_verification_code_send_period.setter
    def min_verification_code_send_period(self, min_verification_code_send_period):
        """Sets the min_verification_code_send_period of this TwoFaProviderInfo.


        :param min_verification_code_send_period: The min_verification_code_send_period of this TwoFaProviderInfo.  # noqa: E501
        :type: int
        """

        self._min_verification_code_send_period = min_verification_code_send_period

    @property
    def type(self):
        """Gets the type of this TwoFaProviderInfo.  # noqa: E501


        :return: The type of this TwoFaProviderInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TwoFaProviderInfo.


        :param type: The type of this TwoFaProviderInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["BACKUP_CODE", "EMAIL", "SMS", "TOTP"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(TwoFaProviderInfo, dict):
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
        if not isinstance(other, TwoFaProviderInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
