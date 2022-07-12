# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ByteBuffer(object):
    """NOTE: This class is auto generated by the swagger code generator program.
from tb_rest_client.api_client import ApiClient
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
        'char': 'str',
        'direct': 'bool',
        'double': 'float',
        '_float': 'float',
        '_int': 'int',
        'long': 'int',
        'read_only': 'bool',
        'short': 'int'
    }

    attribute_map = {
        'char': 'char',
        'direct': 'direct',
        'double': 'double',
        '_float': 'float',
        '_int': 'int',
        'long': 'long',
        'read_only': 'readOnly',
        'short': 'short'
    }

    def __init__(self, char=None, direct=None, double=None, _float=None, _int=None, long=None, read_only=None, short=None):  # noqa: E501
        """ByteBuffer - a model defined in Swagger"""  # noqa: E501
        self._char = None
        self._direct = None
        self._double = None
        self.__float = None
        self.__int = None
        self._long = None
        self._read_only = None
        self._short = None
        self.discriminator = None
        if char is not None:
            self.char = char
        if direct is not None:
            self.direct = direct
        if double is not None:
            self.double = double
        if _float is not None:
            self._float = _float
        if _int is not None:
            self._int = _int
        if long is not None:
            self.long = long
        if read_only is not None:
            self.read_only = read_only
        if short is not None:
            self.short = short

    @property
    def char(self):
        """Gets the char of this ByteBuffer.  # noqa: E501


        :return: The char of this ByteBuffer.  # noqa: E501
        :rtype: str
        """
        return self._char

    @char.setter
    def char(self, char):
        """Sets the char of this ByteBuffer.


        :param char: The char of this ByteBuffer.  # noqa: E501
        :type: str
        """

        self._char = char

    @property
    def direct(self):
        """Gets the direct of this ByteBuffer.  # noqa: E501


        :return: The direct of this ByteBuffer.  # noqa: E501
        :rtype: bool
        """
        return self._direct

    @direct.setter
    def direct(self, direct):
        """Sets the direct of this ByteBuffer.


        :param direct: The direct of this ByteBuffer.  # noqa: E501
        :type: bool
        """

        self._direct = direct

    @property
    def double(self):
        """Gets the double of this ByteBuffer.  # noqa: E501


        :return: The double of this ByteBuffer.  # noqa: E501
        :rtype: float
        """
        return self._double

    @double.setter
    def double(self, double):
        """Sets the double of this ByteBuffer.


        :param double: The double of this ByteBuffer.  # noqa: E501
        :type: float
        """

        self._double = double

    @property
    def _float(self):
        """Gets the _float of this ByteBuffer.  # noqa: E501


        :return: The _float of this ByteBuffer.  # noqa: E501
        :rtype: float
        """
        return self.__float

    @_float.setter
    def _float(self, _float):
        """Sets the _float of this ByteBuffer.


        :param _float: The _float of this ByteBuffer.  # noqa: E501
        :type: float
        """

        self.__float = _float

    @property
    def _int(self):
        """Gets the _int of this ByteBuffer.  # noqa: E501


        :return: The _int of this ByteBuffer.  # noqa: E501
        :rtype: int
        """
        return self.__int

    @_int.setter
    def _int(self, _int):
        """Sets the _int of this ByteBuffer.


        :param _int: The _int of this ByteBuffer.  # noqa: E501
        :type: int
        """

        self.__int = _int

    @property
    def long(self):
        """Gets the long of this ByteBuffer.  # noqa: E501


        :return: The long of this ByteBuffer.  # noqa: E501
        :rtype: int
        """
        return self._long

    @long.setter
    def long(self, long):
        """Sets the long of this ByteBuffer.


        :param long: The long of this ByteBuffer.  # noqa: E501
        :type: int
        """

        self._long = long

    @property
    def read_only(self):
        """Gets the read_only of this ByteBuffer.  # noqa: E501


        :return: The read_only of this ByteBuffer.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this ByteBuffer.


        :param read_only: The read_only of this ByteBuffer.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def short(self):
        """Gets the short of this ByteBuffer.  # noqa: E501


        :return: The short of this ByteBuffer.  # noqa: E501
        :rtype: int
        """
        return self._short

    @short.setter
    def short(self, short):
        """Sets the short of this ByteBuffer.


        :param short: The short of this ByteBuffer.  # noqa: E501
        :type: int
        """

        self._short = short

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
        if issubclass(ByteBuffer, dict):
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
        if not isinstance(other, ByteBuffer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
