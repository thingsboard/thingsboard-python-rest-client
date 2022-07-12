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
from swagger_client.models.two_fa_account_config import TwoFaAccountConfig  # noqa: F401,E501

class SmsTwoFaAccountConfig(TwoFaAccountConfig):
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
        'phone_number': 'str',
        'use_by_default': 'bool'
    }
    if hasattr(TwoFaAccountConfig, "swagger_types"):
        swagger_types.update(TwoFaAccountConfig.swagger_types)

    attribute_map = {
        'phone_number': 'phoneNumber',
        'use_by_default': 'useByDefault'
    }
    if hasattr(TwoFaAccountConfig, "attribute_map"):
        attribute_map.update(TwoFaAccountConfig.attribute_map)

    def __init__(self, phone_number=None, use_by_default=None, *args, **kwargs):  # noqa: E501
        """SmsTwoFaAccountConfig - a model defined in Swagger"""  # noqa: E501
        self._phone_number = None
        self._use_by_default = None
        self.discriminator = None
        self.phone_number = phone_number
        if use_by_default is not None:
            self.use_by_default = use_by_default
        TwoFaAccountConfig.__init__(self, *args, **kwargs)

    @property
    def phone_number(self):
        """Gets the phone_number of this SmsTwoFaAccountConfig.  # noqa: E501


        :return: The phone_number of this SmsTwoFaAccountConfig.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this SmsTwoFaAccountConfig.


        :param phone_number: The phone_number of this SmsTwoFaAccountConfig.  # noqa: E501
        :type: str
        """
        if phone_number is None:
            raise ValueError("Invalid value for `phone_number`, must not be `None`")  # noqa: E501

        self._phone_number = phone_number

    @property
    def use_by_default(self):
        """Gets the use_by_default of this SmsTwoFaAccountConfig.  # noqa: E501


        :return: The use_by_default of this SmsTwoFaAccountConfig.  # noqa: E501
        :rtype: bool
        """
        return self._use_by_default

    @use_by_default.setter
    def use_by_default(self, use_by_default):
        """Sets the use_by_default of this SmsTwoFaAccountConfig.


        :param use_by_default: The use_by_default of this SmsTwoFaAccountConfig.  # noqa: E501
        :type: bool
        """

        self._use_by_default = use_by_default

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
        if issubclass(SmsTwoFaAccountConfig, dict):
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
        if not isinstance(other, SmsTwoFaAccountConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other