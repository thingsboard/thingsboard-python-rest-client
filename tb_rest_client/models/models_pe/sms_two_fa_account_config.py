# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.1.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2025. ThingsBoard
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
from tb_rest_client.models.models_pe.two_fa_account_config import TwoFaAccountConfig  # noqa: F401,E501

class SmsTwoFaAccountConfig(TwoFaAccountConfig):
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
        'phone_number': 'str'
    }
    if hasattr(TwoFaAccountConfig, "swagger_types"):
        swagger_types.update(TwoFaAccountConfig.swagger_types)

    attribute_map = {
        'phone_number': 'phoneNumber'
    }
    if hasattr(TwoFaAccountConfig, "attribute_map"):
        attribute_map.update(TwoFaAccountConfig.attribute_map)

    def __init__(self, phone_number=None, *args, **kwargs):  # noqa: E501
        """SmsTwoFaAccountConfig - a model defined in Swagger"""  # noqa: E501
        self._phone_number = None
        self.discriminator = None
        self.phone_number = phone_number
        TwoFaAccountConfig.__init__(self, *args, **kwargs)

    @property
    def phone_number(self):
        """Gets the phone_number of this SmsTwoFaAccountConfig.  # noqa: E501


        :return: The phone_number of this SmsTwoFaAccountConfig.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this SmsTwoFaAccountConfig.


        :param phone_number: The phone_number of this SmsTwoFaAccountConfig.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

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
        if issubclass(SmsTwoFaAccountConfig, dict):
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
        if not isinstance(other, SmsTwoFaAccountConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
