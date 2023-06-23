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

class AttributeExportData(object):
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
        'boolean_value': 'bool',
        'double_value': 'float',
        'json_value': 'str',
        'key': 'str',
        'last_update_ts': 'int',
        'long_value': 'int',
        'str_value': 'str'
    }

    attribute_map = {
        'boolean_value': 'booleanValue',
        'double_value': 'doubleValue',
        'json_value': 'jsonValue',
        'key': 'key',
        'last_update_ts': 'lastUpdateTs',
        'long_value': 'longValue',
        'str_value': 'strValue'
    }

    def __init__(self, boolean_value=None, double_value=None, json_value=None, key=None, last_update_ts=None, long_value=None, str_value=None):  # noqa: E501
        """AttributeExportData - a model defined in Swagger"""  # noqa: E501
        self._boolean_value = None
        self._double_value = None
        self._json_value = None
        self._key = None
        self._last_update_ts = None
        self._long_value = None
        self._str_value = None
        self.discriminator = None
        if boolean_value is not None:
            self.boolean_value = boolean_value
        if double_value is not None:
            self.double_value = double_value
        if json_value is not None:
            self.json_value = json_value
        if key is not None:
            self.key = key
        if last_update_ts is not None:
            self.last_update_ts = last_update_ts
        if long_value is not None:
            self.long_value = long_value
        if str_value is not None:
            self.str_value = str_value

    @property
    def boolean_value(self):
        """Gets the boolean_value of this AttributeExportData.  # noqa: E501


        :return: The boolean_value of this AttributeExportData.  # noqa: E501
        :rtype: bool
        """
        return self._boolean_value

    @boolean_value.setter
    def boolean_value(self, boolean_value):
        """Sets the boolean_value of this AttributeExportData.


        :param boolean_value: The boolean_value of this AttributeExportData.  # noqa: E501
        :type: bool
        """

        self._boolean_value = boolean_value

    @property
    def double_value(self):
        """Gets the double_value of this AttributeExportData.  # noqa: E501


        :return: The double_value of this AttributeExportData.  # noqa: E501
        :rtype: float
        """
        return self._double_value

    @double_value.setter
    def double_value(self, double_value):
        """Sets the double_value of this AttributeExportData.


        :param double_value: The double_value of this AttributeExportData.  # noqa: E501
        :type: float
        """

        self._double_value = double_value

    @property
    def json_value(self):
        """Gets the json_value of this AttributeExportData.  # noqa: E501


        :return: The json_value of this AttributeExportData.  # noqa: E501
        :rtype: str
        """
        return self._json_value

    @json_value.setter
    def json_value(self, json_value):
        """Sets the json_value of this AttributeExportData.


        :param json_value: The json_value of this AttributeExportData.  # noqa: E501
        :type: str
        """

        self._json_value = json_value

    @property
    def key(self):
        """Gets the key of this AttributeExportData.  # noqa: E501


        :return: The key of this AttributeExportData.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AttributeExportData.


        :param key: The key of this AttributeExportData.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def last_update_ts(self):
        """Gets the last_update_ts of this AttributeExportData.  # noqa: E501


        :return: The last_update_ts of this AttributeExportData.  # noqa: E501
        :rtype: int
        """
        return self._last_update_ts

    @last_update_ts.setter
    def last_update_ts(self, last_update_ts):
        """Sets the last_update_ts of this AttributeExportData.


        :param last_update_ts: The last_update_ts of this AttributeExportData.  # noqa: E501
        :type: int
        """

        self._last_update_ts = last_update_ts

    @property
    def long_value(self):
        """Gets the long_value of this AttributeExportData.  # noqa: E501


        :return: The long_value of this AttributeExportData.  # noqa: E501
        :rtype: int
        """
        return self._long_value

    @long_value.setter
    def long_value(self, long_value):
        """Sets the long_value of this AttributeExportData.


        :param long_value: The long_value of this AttributeExportData.  # noqa: E501
        :type: int
        """

        self._long_value = long_value

    @property
    def str_value(self):
        """Gets the str_value of this AttributeExportData.  # noqa: E501


        :return: The str_value of this AttributeExportData.  # noqa: E501
        :rtype: str
        """
        return self._str_value

    @str_value.setter
    def str_value(self, str_value):
        """Sets the str_value of this AttributeExportData.


        :param str_value: The str_value of this AttributeExportData.  # noqa: E501
        :type: str
        """

        self._str_value = str_value

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
        if issubclass(AttributeExportData, dict):
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
        if not isinstance(other, AttributeExportData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
