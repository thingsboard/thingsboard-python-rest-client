# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.3PE
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

class FilterPredicateValueint(object):
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
        'default_value': 'int',
        'dynamic_value': 'DynamicValueint',
        'user_value': 'int'
    }

    attribute_map = {
        'default_value': 'defaultValue',
        'dynamic_value': 'dynamicValue',
        'user_value': 'userValue'
    }

    def __init__(self, default_value=None, dynamic_value=None, user_value=None):  # noqa: E501
        """FilterPredicateValueint - a model defined in Swagger"""  # noqa: E501
        self._default_value = None
        self._dynamic_value = None
        self._user_value = None
        self.discriminator = None
        if default_value is not None:
            self.default_value = default_value
        if dynamic_value is not None:
            self.dynamic_value = dynamic_value
        if user_value is not None:
            self.user_value = user_value

    @property
    def default_value(self):
        """Gets the default_value of this FilterPredicateValueint.  # noqa: E501


        :return: The default_value of this FilterPredicateValueint.  # noqa: E501
        :rtype: int
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this FilterPredicateValueint.


        :param default_value: The default_value of this FilterPredicateValueint.  # noqa: E501
        :type: int
        """

        self._default_value = default_value

    @property
    def dynamic_value(self):
        """Gets the dynamic_value of this FilterPredicateValueint.  # noqa: E501


        :return: The dynamic_value of this FilterPredicateValueint.  # noqa: E501
        :rtype: DynamicValueint
        """
        return self._dynamic_value

    @dynamic_value.setter
    def dynamic_value(self, dynamic_value):
        """Sets the dynamic_value of this FilterPredicateValueint.


        :param dynamic_value: The dynamic_value of this FilterPredicateValueint.  # noqa: E501
        :type: DynamicValueint
        """

        self._dynamic_value = dynamic_value

    @property
    def user_value(self):
        """Gets the user_value of this FilterPredicateValueint.  # noqa: E501


        :return: The user_value of this FilterPredicateValueint.  # noqa: E501
        :rtype: int
        """
        return self._user_value

    @user_value.setter
    def user_value(self, user_value):
        """Sets the user_value of this FilterPredicateValueint.


        :param user_value: The user_value of this FilterPredicateValueint.  # noqa: E501
        :type: int
        """

        self._user_value = user_value

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
        if issubclass(FilterPredicateValueint, dict):
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
        if not isinstance(other, FilterPredicateValueint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
