# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.0.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConvertersInfo(object):
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
        'library': 'bool',
        'existing': 'bool'
    }

    attribute_map = {
        'library': 'library',
        'existing': 'existing'
    }

    def __init__(self, library=None, existing=None):  # noqa: E501
        """ConvertersInfo - a model defined in Swagger"""  # noqa: E501
        self._library = None
        self._existing = None
        self.discriminator = None
        if library is not None:
            self.library = library
        if existing is not None:
            self.existing = existing

    @property
    def library(self):
        """Gets the library of this ConvertersInfo.  # noqa: E501


        :return: The library of this ConvertersInfo.  # noqa: E501
        :rtype: bool
        """
        return self._library

    @library.setter
    def library(self, library):
        """Sets the library of this ConvertersInfo.


        :param library: The library of this ConvertersInfo.  # noqa: E501
        :type: bool
        """

        self._library = library

    @property
    def existing(self):
        """Gets the existing of this ConvertersInfo.  # noqa: E501


        :return: The existing of this ConvertersInfo.  # noqa: E501
        :rtype: bool
        """
        return self._existing

    @existing.setter
    def existing(self, existing):
        """Sets the existing of this ConvertersInfo.


        :param existing: The existing of this ConvertersInfo.  # noqa: E501
        :type: bool
        """

        self._existing = existing

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
        if issubclass(ConvertersInfo, dict):
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
        if not isinstance(other, ConvertersInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
