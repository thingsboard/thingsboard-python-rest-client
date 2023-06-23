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

class BackupCodeTwoFaProviderConfig(object):
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
        'codes_quantity': 'int'
    }

    attribute_map = {
        'codes_quantity': 'codesQuantity'
    }

    def __init__(self, codes_quantity=None):  # noqa: E501
        """BackupCodeTwoFaProviderConfig - a model defined in Swagger"""  # noqa: E501
        self._codes_quantity = None
        self.discriminator = None
        if codes_quantity is not None:
            self.codes_quantity = codes_quantity

    @property
    def codes_quantity(self):
        """Gets the codes_quantity of this BackupCodeTwoFaProviderConfig.  # noqa: E501


        :return: The codes_quantity of this BackupCodeTwoFaProviderConfig.  # noqa: E501
        :rtype: int
        """
        return self._codes_quantity

    @codes_quantity.setter
    def codes_quantity(self, codes_quantity):
        """Sets the codes_quantity of this BackupCodeTwoFaProviderConfig.


        :param codes_quantity: The codes_quantity of this BackupCodeTwoFaProviderConfig.  # noqa: E501
        :type: int
        """

        self._codes_quantity = codes_quantity

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
        if issubclass(BackupCodeTwoFaProviderConfig, dict):
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
        if not isinstance(other, BackupCodeTwoFaProviderConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
