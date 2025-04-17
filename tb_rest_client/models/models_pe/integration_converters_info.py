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

class IntegrationConvertersInfo(object):
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
        'uplink': 'ConvertersInfo',
        'downlink': 'ConvertersInfo'
    }

    attribute_map = {
        'uplink': 'uplink',
        'downlink': 'downlink'
    }

    def __init__(self, uplink=None, downlink=None):  # noqa: E501
        """IntegrationConvertersInfo - a model defined in Swagger"""  # noqa: E501
        self._uplink = None
        self._downlink = None
        self.discriminator = None
        if uplink is not None:
            self.uplink = uplink
        if downlink is not None:
            self.downlink = downlink

    @property
    def uplink(self):
        """Gets the uplink of this IntegrationConvertersInfo.  # noqa: E501


        :return: The uplink of this IntegrationConvertersInfo.  # noqa: E501
        :rtype: ConvertersInfo
        """
        return self._uplink

    @uplink.setter
    def uplink(self, uplink):
        """Sets the uplink of this IntegrationConvertersInfo.


        :param uplink: The uplink of this IntegrationConvertersInfo.  # noqa: E501
        :type: ConvertersInfo
        """

        self._uplink = uplink

    @property
    def downlink(self):
        """Gets the downlink of this IntegrationConvertersInfo.  # noqa: E501


        :return: The downlink of this IntegrationConvertersInfo.  # noqa: E501
        :rtype: ConvertersInfo
        """
        return self._downlink

    @downlink.setter
    def downlink(self, downlink):
        """Sets the downlink of this IntegrationConvertersInfo.


        :param downlink: The downlink of this IntegrationConvertersInfo.  # noqa: E501
        :type: ConvertersInfo
        """

        self._downlink = downlink

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
        if issubclass(IntegrationConvertersInfo, dict):
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
        if not isinstance(other, IntegrationConvertersInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
