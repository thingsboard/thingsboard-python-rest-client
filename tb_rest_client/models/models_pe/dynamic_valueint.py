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

class DynamicValueint(object):
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
        'inherit': 'bool',
        'source_attribute': 'str',
        'source_type': 'str'
    }

    attribute_map = {
        'inherit': 'inherit',
        'source_attribute': 'sourceAttribute',
        'source_type': 'sourceType'
    }

    def __init__(self, inherit=None, source_attribute=None, source_type=None):  # noqa: E501
        """DynamicValueint - a model defined in Swagger"""  # noqa: E501
        self._inherit = None
        self._source_attribute = None
        self._source_type = None
        self.discriminator = None
        if inherit is not None:
            self.inherit = inherit
        if source_attribute is not None:
            self.source_attribute = source_attribute
        if source_type is not None:
            self.source_type = source_type

    @property
    def inherit(self):
        """Gets the inherit of this DynamicValueint.  # noqa: E501


        :return: The inherit of this DynamicValueint.  # noqa: E501
        :rtype: bool
        """
        return self._inherit

    @inherit.setter
    def inherit(self, inherit):
        """Sets the inherit of this DynamicValueint.


        :param inherit: The inherit of this DynamicValueint.  # noqa: E501
        :type: bool
        """

        self._inherit = inherit

    @property
    def source_attribute(self):
        """Gets the source_attribute of this DynamicValueint.  # noqa: E501


        :return: The source_attribute of this DynamicValueint.  # noqa: E501
        :rtype: str
        """
        return self._source_attribute

    @source_attribute.setter
    def source_attribute(self, source_attribute):
        """Sets the source_attribute of this DynamicValueint.


        :param source_attribute: The source_attribute of this DynamicValueint.  # noqa: E501
        :type: str
        """

        self._source_attribute = source_attribute

    @property
    def source_type(self):
        """Gets the source_type of this DynamicValueint.  # noqa: E501


        :return: The source_type of this DynamicValueint.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DynamicValueint.


        :param source_type: The source_type of this DynamicValueint.  # noqa: E501
        :type: str
        """
        allowed_values = ["CURRENT_CUSTOMER", "CURRENT_DEVICE", "CURRENT_TENANT", "CURRENT_USER"]  # noqa: E501
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

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
        if issubclass(DynamicValueint, dict):
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
        if not isinstance(other, DynamicValueint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
