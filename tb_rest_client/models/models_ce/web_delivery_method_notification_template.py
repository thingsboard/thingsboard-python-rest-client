# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.0.0
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
from tb_rest_client.models.models_ce.delivery_method_notification_template import DeliveryMethodNotificationTemplate  # noqa: F401,E501

class WebDeliveryMethodNotificationTemplate(DeliveryMethodNotificationTemplate):
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
        'subject': 'str',
        'additional_config': 'object'
    }
    if hasattr(DeliveryMethodNotificationTemplate, "swagger_types"):
        swagger_types.update(DeliveryMethodNotificationTemplate.swagger_types)

    attribute_map = {
        'subject': 'subject',
        'additional_config': 'additionalConfig'
    }
    if hasattr(DeliveryMethodNotificationTemplate, "attribute_map"):
        attribute_map.update(DeliveryMethodNotificationTemplate.attribute_map)

    def __init__(self, subject=None, additional_config=None, *args, **kwargs):  # noqa: E501
        """WebDeliveryMethodNotificationTemplate - a model defined in Swagger"""  # noqa: E501
        self._subject = None
        self._additional_config = None
        self.discriminator = None
        self.subject = subject
        if additional_config is not None:
            self.additional_config = additional_config
        DeliveryMethodNotificationTemplate.__init__(self, *args, **kwargs)

    @property
    def subject(self):
        """Gets the subject of this WebDeliveryMethodNotificationTemplate.  # noqa: E501


        :return: The subject of this WebDeliveryMethodNotificationTemplate.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this WebDeliveryMethodNotificationTemplate.


        :param subject: The subject of this WebDeliveryMethodNotificationTemplate.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def additional_config(self):
        """Gets the additional_config of this WebDeliveryMethodNotificationTemplate.  # noqa: E501


        :return: The additional_config of this WebDeliveryMethodNotificationTemplate.  # noqa: E501
        :rtype: object
        """
        return self._additional_config

    @additional_config.setter
    def additional_config(self, additional_config):
        """Sets the additional_config of this WebDeliveryMethodNotificationTemplate.


        :param additional_config: The additional_config of this WebDeliveryMethodNotificationTemplate.  # noqa: E501
        :type: object
        """

        self._additional_config = additional_config

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
        if issubclass(WebDeliveryMethodNotificationTemplate, dict):
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
        if not isinstance(other, WebDeliveryMethodNotificationTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
