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

class AtomicInteger(object):
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
        'acquire': 'int',
        'and_decrement': 'int',
        'and_increment': 'int',
        'opaque': 'int',
        'plain': 'int'
    }

    attribute_map = {
        'acquire': 'acquire',
        'and_decrement': 'andDecrement',
        'and_increment': 'andIncrement',
        'opaque': 'opaque',
        'plain': 'plain'
    }

    def __init__(self, acquire=None, and_decrement=None, and_increment=None, opaque=None, plain=None):  # noqa: E501
        """AtomicInteger - a model defined in Swagger"""  # noqa: E501
        self._acquire = None
        self._and_decrement = None
        self._and_increment = None
        self._opaque = None
        self._plain = None
        self.discriminator = None
        if acquire is not None:
            self.acquire = acquire
        if and_decrement is not None:
            self.and_decrement = and_decrement
        if and_increment is not None:
            self.and_increment = and_increment
        if opaque is not None:
            self.opaque = opaque
        if plain is not None:
            self.plain = plain

    @property
    def acquire(self):
        """Gets the acquire of this AtomicInteger.  # noqa: E501


        :return: The acquire of this AtomicInteger.  # noqa: E501
        :rtype: int
        """
        return self._acquire

    @acquire.setter
    def acquire(self, acquire):
        """Sets the acquire of this AtomicInteger.


        :param acquire: The acquire of this AtomicInteger.  # noqa: E501
        :type: int
        """

        self._acquire = acquire

    @property
    def and_decrement(self):
        """Gets the and_decrement of this AtomicInteger.  # noqa: E501


        :return: The and_decrement of this AtomicInteger.  # noqa: E501
        :rtype: int
        """
        return self._and_decrement

    @and_decrement.setter
    def and_decrement(self, and_decrement):
        """Sets the and_decrement of this AtomicInteger.


        :param and_decrement: The and_decrement of this AtomicInteger.  # noqa: E501
        :type: int
        """

        self._and_decrement = and_decrement

    @property
    def and_increment(self):
        """Gets the and_increment of this AtomicInteger.  # noqa: E501


        :return: The and_increment of this AtomicInteger.  # noqa: E501
        :rtype: int
        """
        return self._and_increment

    @and_increment.setter
    def and_increment(self, and_increment):
        """Sets the and_increment of this AtomicInteger.


        :param and_increment: The and_increment of this AtomicInteger.  # noqa: E501
        :type: int
        """

        self._and_increment = and_increment

    @property
    def opaque(self):
        """Gets the opaque of this AtomicInteger.  # noqa: E501


        :return: The opaque of this AtomicInteger.  # noqa: E501
        :rtype: int
        """
        return self._opaque

    @opaque.setter
    def opaque(self, opaque):
        """Sets the opaque of this AtomicInteger.


        :param opaque: The opaque of this AtomicInteger.  # noqa: E501
        :type: int
        """

        self._opaque = opaque

    @property
    def plain(self):
        """Gets the plain of this AtomicInteger.  # noqa: E501


        :return: The plain of this AtomicInteger.  # noqa: E501
        :rtype: int
        """
        return self._plain

    @plain.setter
    def plain(self, plain):
        """Sets the plain of this AtomicInteger.


        :param plain: The plain of this AtomicInteger.  # noqa: E501
        :type: int
        """

        self._plain = plain

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
        if issubclass(AtomicInteger, dict):
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
        if not isinstance(other, AtomicInteger):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
