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

class OtaPackageData(object):
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
        'short': 'int',
        'char': 'str',
        '_int': 'int',
        'long': 'int',
        '_float': 'float',
        'double': 'float',
        'direct': 'bool',
        'read_only': 'bool'
    }

    attribute_map = {
        'short': 'short',
        'char': 'char',
        '_int': 'int',
        'long': 'long',
        '_float': 'float',
        'double': 'double',
        'direct': 'direct',
        'read_only': 'readOnly'
    }

    def __init__(self, short=None, char=None, _int=None, long=None, _float=None, double=None, direct=None, read_only=None):  # noqa: E501
        """OtaPackageData - a model defined in Swagger"""  # noqa: E501
        self._short = None
        self._char = None
        self.__int = None
        self._long = None
        self.__float = None
        self._double = None
        self._direct = None
        self._read_only = None
        self.discriminator = None
        if short is not None:
            self.short = short
        if char is not None:
            self.char = char
        if _int is not None:
            self._int = _int
        if long is not None:
            self.long = long
        if _float is not None:
            self._float = _float
        if double is not None:
            self.double = double
        if direct is not None:
            self.direct = direct
        if read_only is not None:
            self.read_only = read_only

    @property
    def short(self):
        """Gets the short of this OtaPackageData.  # noqa: E501


        :return: The short of this OtaPackageData.  # noqa: E501
        :rtype: int
        """
        return self._short

    @short.setter
    def short(self, short):
        """Sets the short of this OtaPackageData.


        :param short: The short of this OtaPackageData.  # noqa: E501
        :type: int
        """

        self._short = short

    @property
    def char(self):
        """Gets the char of this OtaPackageData.  # noqa: E501


        :return: The char of this OtaPackageData.  # noqa: E501
        :rtype: str
        """
        return self._char

    @char.setter
    def char(self, char):
        """Sets the char of this OtaPackageData.


        :param char: The char of this OtaPackageData.  # noqa: E501
        :type: str
        """

        self._char = char

    @property
    def _int(self):
        """Gets the _int of this OtaPackageData.  # noqa: E501


        :return: The _int of this OtaPackageData.  # noqa: E501
        :rtype: int
        """
        return self.__int

    @_int.setter
    def _int(self, _int):
        """Sets the _int of this OtaPackageData.


        :param _int: The _int of this OtaPackageData.  # noqa: E501
        :type: int
        """

        self.__int = _int

    @property
    def long(self):
        """Gets the long of this OtaPackageData.  # noqa: E501


        :return: The long of this OtaPackageData.  # noqa: E501
        :rtype: int
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this OtaPackageData.


        :param long: The long of this OtaPackageData.  # noqa: E501
        :type: int
        """

        self._long = long

    @property
    def _float(self):
        """Gets the _float of this OtaPackageData.  # noqa: E501


        :return: The _float of this OtaPackageData.  # noqa: E501
        :rtype: float
        """
        return self.__float

    @_float.setter
    def _float(self, _float):
        """Sets the _float of this OtaPackageData.


        :param _float: The _float of this OtaPackageData.  # noqa: E501
        :type: float
        """

        self.__float = _float

    @property
    def double(self):
        """Gets the double of this OtaPackageData.  # noqa: E501


        :return: The double of this OtaPackageData.  # noqa: E501
        :rtype: float
        """
        return self._double

    @double.setter
    def double(self, double):
        """Sets the double of this OtaPackageData.


        :param double: The double of this OtaPackageData.  # noqa: E501
        :type: float
        """

        self._double = double

    @property
    def direct(self):
        """Gets the direct of this OtaPackageData.  # noqa: E501


        :return: The direct of this OtaPackageData.  # noqa: E501
        :rtype: bool
        """
        return self._direct

    @direct.setter
    def direct(self, direct):
        """Sets the direct of this OtaPackageData.


        :param direct: The direct of this OtaPackageData.  # noqa: E501
        :type: bool
        """

        self._direct = direct

    @property
    def read_only(self):
        """Gets the read_only of this OtaPackageData.  # noqa: E501


        :return: The read_only of this OtaPackageData.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this OtaPackageData.


        :param read_only: The read_only of this OtaPackageData.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

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
        if issubclass(OtaPackageData, dict):
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
        if not isinstance(other, OtaPackageData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other