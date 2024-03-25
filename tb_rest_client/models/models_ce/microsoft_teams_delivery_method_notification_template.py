# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.3
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

class MicrosoftTeamsDeliveryMethodNotificationTemplate(object):
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
        'body': 'str',
        'button': 'Button',
        'enabled': 'bool',
        'subject': 'str',
        'theme_color': 'str'
    }

    attribute_map = {
        'body': 'body',
        'button': 'button',
        'enabled': 'enabled',
        'subject': 'subject',
        'theme_color': 'themeColor'
    }

    def __init__(self, body=None, button=None, enabled=None, subject=None, theme_color=None):  # noqa: E501
        """MicrosoftTeamsDeliveryMethodNotificationTemplate - a model defined in Swagger"""  # noqa: E501
        self._body = None
        self._button = None
        self._enabled = None
        self._subject = None
        self._theme_color = None
        self.discriminator = None
        if body is not None:
            self.body = body
        if button is not None:
            self.button = button
        if enabled is not None:
            self.enabled = enabled
        if subject is not None:
            self.subject = subject
        if theme_color is not None:
            self.theme_color = theme_color

    @property
    def body(self):
        """Gets the body of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501


        :return: The body of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this MicrosoftTeamsDeliveryMethodNotificationTemplate.


        :param body: The body of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501
        :type: str
        """

        self._body = body

    @property
    def button(self):
        """Gets the button of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501


        :return: The button of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501
        :rtype: Button
        """
        return self._button

    @button.setter
    def button(self, button):
        """Sets the button of this MicrosoftTeamsDeliveryMethodNotificationTemplate.


        :param button: The button of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501
        :type: Button
        """

        self._button = button

    @property
    def enabled(self):
        """Gets the enabled of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501


        :return: The enabled of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this MicrosoftTeamsDeliveryMethodNotificationTemplate.


        :param enabled: The enabled of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def subject(self):
        """Gets the subject of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501


        :return: The subject of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this MicrosoftTeamsDeliveryMethodNotificationTemplate.


        :param subject: The subject of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def theme_color(self):
        """Gets the theme_color of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501


        :return: The theme_color of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._theme_color

    @theme_color.setter
    def theme_color(self, theme_color):
        """Sets the theme_color of this MicrosoftTeamsDeliveryMethodNotificationTemplate.


        :param theme_color: The theme_color of this MicrosoftTeamsDeliveryMethodNotificationTemplate.  # noqa: E501
        :type: str
        """

        self._theme_color = theme_color

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
        if issubclass(MicrosoftTeamsDeliveryMethodNotificationTemplate, dict):
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
        if not isinstance(other, MicrosoftTeamsDeliveryMethodNotificationTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
