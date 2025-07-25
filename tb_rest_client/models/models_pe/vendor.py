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

class Vendor(object):
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
        'name': 'object',
        'logo': 'object'
    }

    attribute_map = {
        'name': 'name',
        'logo': 'logo'
    }

    def __init__(self, name=None, logo=None):  # noqa: E501
        """Vendor - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._logo = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if logo is not None:
            self.logo = logo

    @property
    def name(self):
        """Gets the name of this Vendor.  # noqa: E501


        :return: The name of this Vendor.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Vendor.


        :param name: The name of this Vendor.  # noqa: E501
        :type: object
        """

        self._name = name

    @property
    def logo(self):
        """Gets the logo of this Vendor.  # noqa: E501


        :return: The logo of this Vendor.  # noqa: E501
        :rtype: object
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Vendor.


        :param logo: The logo of this Vendor.  # noqa: E501
        :type: object
        """

        self._logo = logo

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
        if issubclass(Vendor, dict):
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
        if not isinstance(other, Vendor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
