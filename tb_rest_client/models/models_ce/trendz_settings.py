# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.1.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TrendzSettings(object):
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
        'enabled': 'bool',
        'base_url': 'str',
        'api_key': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'base_url': 'baseUrl',
        'api_key': 'apiKey'
    }

    def __init__(self, enabled=None, base_url=None, api_key=None):  # noqa: E501
        """TrendzSettings - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._base_url = None
        self._api_key = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if base_url is not None:
            self.base_url = base_url
        if api_key is not None:
            self.api_key = api_key

    @property
    def enabled(self):
        """Gets the enabled of this TrendzSettings.  # noqa: E501


        :return: The enabled of this TrendzSettings.  # noqa: E501
        :rtype: object
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this TrendzSettings.


        :param enabled: The enabled of this TrendzSettings.  # noqa: E501
        :type: object
        """

        self._enabled = enabled

    @property
    def base_url(self):
        """Gets the base_url of this TrendzSettings.  # noqa: E501


        :return: The base_url of this TrendzSettings.  # noqa: E501
        :rtype: object
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this TrendzSettings.


        :param base_url: The base_url of this TrendzSettings.  # noqa: E501
        :type: object
        """

        self._base_url = base_url

    @property
    def api_key(self):
        """Gets the api_key of this TrendzSettings.  # noqa: E501


        :return: The api_key of this TrendzSettings.  # noqa: E501
        :rtype: object
        """
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        """Sets the api_key of this TrendzSettings.


        :param api_key: The api_key of this TrendzSettings.  # noqa: E501
        :type: object
        """

        self._api_key = api_key

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
        if issubclass(TrendzSettings, dict):
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
        if not isinstance(other, TrendzSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
