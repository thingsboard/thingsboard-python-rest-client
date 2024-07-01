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
from tb_rest_client.models.models_ce.sms_provider_configuration import SmsProviderConfiguration  # noqa: F401,E501

class TwilioSmsProviderConfiguration(SmsProviderConfiguration):
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
        'account_sid': 'str',
        'account_token': 'str',
        'number_from': 'str'
    }
    if hasattr(SmsProviderConfiguration, "swagger_types"):
        swagger_types.update(SmsProviderConfiguration.swagger_types)

    attribute_map = {
        'account_sid': 'accountSid',
        'account_token': 'accountToken',
        'number_from': 'numberFrom'
    }
    if hasattr(SmsProviderConfiguration, "attribute_map"):
        attribute_map.update(SmsProviderConfiguration.attribute_map)

    def __init__(self, account_sid=None, account_token=None, number_from=None, *args, **kwargs):  # noqa: E501
        """TwilioSmsProviderConfiguration - a model defined in Swagger"""  # noqa: E501
        self._account_sid = None
        self._account_token = None
        self._number_from = None
        self.discriminator = None
        if account_sid is not None:
            self.account_sid = account_sid
        if account_token is not None:
            self.account_token = account_token
        if number_from is not None:
            self.number_from = number_from
        SmsProviderConfiguration.__init__(self, *args, **kwargs)

    @property
    def account_sid(self):
        """Gets the account_sid of this TwilioSmsProviderConfiguration.  # noqa: E501

        Twilio account Sid.  # noqa: E501

        :return: The account_sid of this TwilioSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._account_sid

    @account_sid.setter
    def account_sid(self, account_sid):
        """Sets the account_sid of this TwilioSmsProviderConfiguration.

        Twilio account Sid.  # noqa: E501

        :param account_sid: The account_sid of this TwilioSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._account_sid = account_sid

    @property
    def account_token(self):
        """Gets the account_token of this TwilioSmsProviderConfiguration.  # noqa: E501

        Twilio account Token.  # noqa: E501

        :return: The account_token of this TwilioSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._account_token

    @account_token.setter
    def account_token(self, account_token):
        """Sets the account_token of this TwilioSmsProviderConfiguration.

        Twilio account Token.  # noqa: E501

        :param account_token: The account_token of this TwilioSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._account_token = account_token

    @property
    def number_from(self):
        """Gets the number_from of this TwilioSmsProviderConfiguration.  # noqa: E501

        The number/id of a sender.  # noqa: E501

        :return: The number_from of this TwilioSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._number_from

    @number_from.setter
    def number_from(self, number_from):
        """Sets the number_from of this TwilioSmsProviderConfiguration.

        The number/id of a sender.  # noqa: E501

        :param number_from: The number_from of this TwilioSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._number_from = number_from

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
        if issubclass(TwilioSmsProviderConfiguration, dict):
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
        if not isinstance(other, TwilioSmsProviderConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
