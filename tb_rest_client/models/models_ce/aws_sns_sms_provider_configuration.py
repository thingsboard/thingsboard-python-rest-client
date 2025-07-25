# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.1.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2025. ThingsBoard
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
from tb_rest_client.models.models_ce.sms_provider_configuration import SmsProviderConfiguration  # noqa: F401,E501

class AwsSnsSmsProviderConfiguration(SmsProviderConfiguration):
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
        'access_key_id': 'str',
        'secret_access_key': 'str',
        'region': 'str'
    }
    if hasattr(SmsProviderConfiguration, "swagger_types"):
        swagger_types.update(SmsProviderConfiguration.swagger_types)

    attribute_map = {
        'access_key_id': 'accessKeyId',
        'secret_access_key': 'secretAccessKey',
        'region': 'region'
    }
    if hasattr(SmsProviderConfiguration, "attribute_map"):
        attribute_map.update(SmsProviderConfiguration.attribute_map)

    def __init__(self, access_key_id=None, secret_access_key=None, region=None, *args, **kwargs):  # noqa: E501
        """AwsSnsSmsProviderConfiguration - a model defined in Swagger"""  # noqa: E501
        self._access_key_id = None
        self._secret_access_key = None
        self._region = None
        self.discriminator = None
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if secret_access_key is not None:
            self.secret_access_key = secret_access_key
        if region is not None:
            self.region = region
        SmsProviderConfiguration.__init__(self, *args, **kwargs)

    @property
    def access_key_id(self):
        """Gets the access_key_id of this AwsSnsSmsProviderConfiguration.  # noqa: E501

        The AWS SNS Access Key ID.  # noqa: E501

        :return: The access_key_id of this AwsSnsSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this AwsSnsSmsProviderConfiguration.

        The AWS SNS Access Key ID.  # noqa: E501

        :param access_key_id: The access_key_id of this AwsSnsSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def secret_access_key(self):
        """Gets the secret_access_key of this AwsSnsSmsProviderConfiguration.  # noqa: E501

        The AWS SNS Access Key.  # noqa: E501

        :return: The secret_access_key of this AwsSnsSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._secret_access_key

    @secret_access_key.setter
    def secret_access_key(self, secret_access_key):
        """Sets the secret_access_key of this AwsSnsSmsProviderConfiguration.

        The AWS SNS Access Key.  # noqa: E501

        :param secret_access_key: The secret_access_key of this AwsSnsSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._secret_access_key = secret_access_key

    @property
    def region(self):
        """Gets the region of this AwsSnsSmsProviderConfiguration.  # noqa: E501

        The AWS region.  # noqa: E501

        :return: The region of this AwsSnsSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this AwsSnsSmsProviderConfiguration.

        The AWS region.  # noqa: E501

        :param region: The region of this AwsSnsSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._region = region

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
        if issubclass(AwsSnsSmsProviderConfiguration, dict):
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
        if not isinstance(other, AwsSnsSmsProviderConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
