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
from swagger_client.models.two_fa_provider_config import TwoFaProviderConfig  # noqa: F401,E501

class EmailTwoFaProviderConfig(TwoFaProviderConfig):
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
        'verification_code_lifetime': 'int'
    }
    if hasattr(TwoFaProviderConfig, "swagger_types"):
        swagger_types.update(TwoFaProviderConfig.swagger_types)

    attribute_map = {
        'verification_code_lifetime': 'verificationCodeLifetime'
    }
    if hasattr(TwoFaProviderConfig, "attribute_map"):
        attribute_map.update(TwoFaProviderConfig.attribute_map)

    def __init__(self, verification_code_lifetime=None, *args, **kwargs):  # noqa: E501
        """EmailTwoFaProviderConfig - a model defined in Swagger"""  # noqa: E501
        self._verification_code_lifetime = None
        self.discriminator = None
        if verification_code_lifetime is not None:
            self.verification_code_lifetime = verification_code_lifetime
        TwoFaProviderConfig.__init__(self, *args, **kwargs)

    @property
    def verification_code_lifetime(self):
        """Gets the verification_code_lifetime of this EmailTwoFaProviderConfig.  # noqa: E501


        :return: The verification_code_lifetime of this EmailTwoFaProviderConfig.  # noqa: E501
        :rtype: int
        """
        return self._verification_code_lifetime

    @verification_code_lifetime.setter
    def verification_code_lifetime(self, verification_code_lifetime):
        """Sets the verification_code_lifetime of this EmailTwoFaProviderConfig.


        :param verification_code_lifetime: The verification_code_lifetime of this EmailTwoFaProviderConfig.  # noqa: E501
        :type: int
        """

        self._verification_code_lifetime = verification_code_lifetime

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
        if issubclass(EmailTwoFaProviderConfig, dict):
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
        if not isinstance(other, EmailTwoFaProviderConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
