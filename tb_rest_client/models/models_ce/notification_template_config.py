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

class NotificationTemplateConfig(object):
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
        'delivery_methods_templates': 'dict(str, DeliveryMethodNotificationTemplate)'
    }

    attribute_map = {
        'delivery_methods_templates': 'deliveryMethodsTemplates'
    }

    def __init__(self, delivery_methods_templates=None):  # noqa: E501
        """NotificationTemplateConfig - a model defined in Swagger"""  # noqa: E501
        self._delivery_methods_templates = None
        self.discriminator = None
        if delivery_methods_templates is not None:
            self.delivery_methods_templates = delivery_methods_templates

    @property
    def delivery_methods_templates(self):
        """Gets the delivery_methods_templates of this NotificationTemplateConfig.  # noqa: E501


        :return: The delivery_methods_templates of this NotificationTemplateConfig.  # noqa: E501
        :rtype: dict(str, DeliveryMethodNotificationTemplate)
        """
        return self._delivery_methods_templates

    @delivery_methods_templates.setter
    def delivery_methods_templates(self, delivery_methods_templates):
        """Sets the delivery_methods_templates of this NotificationTemplateConfig.


        :param delivery_methods_templates: The delivery_methods_templates of this NotificationTemplateConfig.  # noqa: E501
        :type: dict(str, DeliveryMethodNotificationTemplate)
        """

        self._delivery_methods_templates = delivery_methods_templates

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
        if issubclass(NotificationTemplateConfig, dict):
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
        if not isinstance(other, NotificationTemplateConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
