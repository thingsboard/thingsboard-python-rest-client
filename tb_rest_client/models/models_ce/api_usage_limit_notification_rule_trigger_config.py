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
from tb_rest_client.models.models_ce.notification_rule_trigger_config import NotificationRuleTriggerConfig  # noqa: F401,E501

class ApiUsageLimitNotificationRuleTriggerConfig(NotificationRuleTriggerConfig):
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
        'api_features': 'list[str]',
        'notify_on': 'list[str]',
        'trigger_type': 'str'
    }
    if hasattr(NotificationRuleTriggerConfig, "swagger_types"):
        swagger_types.update(NotificationRuleTriggerConfig.swagger_types)

    attribute_map = {
        'api_features': 'apiFeatures',
        'notify_on': 'notifyOn',
        'trigger_type': 'triggerType'
    }
    if hasattr(NotificationRuleTriggerConfig, "attribute_map"):
        attribute_map.update(NotificationRuleTriggerConfig.attribute_map)

    def __init__(self, api_features=None, notify_on=None, trigger_type=None, *args, **kwargs):  # noqa: E501
        """ApiUsageLimitNotificationRuleTriggerConfig - a model defined in Swagger"""  # noqa: E501
        self._api_features = None
        self._notify_on = None
        self._trigger_type = None
        self.discriminator = None
        if api_features is not None:
            self.api_features = api_features
        if notify_on is not None:
            self.notify_on = notify_on
        if trigger_type is not None:
            self.trigger_type = trigger_type
        NotificationRuleTriggerConfig.__init__(self, *args, **kwargs)

    @property
    def api_features(self):
        """Gets the api_features of this ApiUsageLimitNotificationRuleTriggerConfig.  # noqa: E501


        :return: The api_features of this ApiUsageLimitNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._api_features

    @api_features.setter
    def api_features(self, api_features):
        """Sets the api_features of this ApiUsageLimitNotificationRuleTriggerConfig.


        :param api_features: The api_features of this ApiUsageLimitNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ALARM", "DB", "EMAIL", "JS", "RE", "SMS", "TBEL", "TRANSPORT"]  # noqa: E501
        if not set(api_features).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `api_features` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(api_features) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._api_features = api_features

    @property
    def notify_on(self):
        """Gets the notify_on of this ApiUsageLimitNotificationRuleTriggerConfig.  # noqa: E501


        :return: The notify_on of this ApiUsageLimitNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._notify_on

    @notify_on.setter
    def notify_on(self, notify_on):
        """Sets the notify_on of this ApiUsageLimitNotificationRuleTriggerConfig.


        :param notify_on: The notify_on of this ApiUsageLimitNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["DISABLED", "ENABLED", "WARNING"]  # noqa: E501
        if not set(notify_on).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `notify_on` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(notify_on) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._notify_on = notify_on

    @property
    def trigger_type(self):
        """Gets the trigger_type of this ApiUsageLimitNotificationRuleTriggerConfig.  # noqa: E501


        :return: The trigger_type of this ApiUsageLimitNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this ApiUsageLimitNotificationRuleTriggerConfig.


        :param trigger_type: The trigger_type of this ApiUsageLimitNotificationRuleTriggerConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "ALARM_ASSIGNMENT", "ALARM_COMMENT", "API_USAGE_LIMIT", "DEVICE_ACTIVITY", "EDGE_COMMUNICATION_FAILURE", "EDGE_CONNECTION", "ENTITIES_LIMIT", "ENTITY_ACTION", "NEW_PLATFORM_VERSION", "RATE_LIMITS", "RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT"]  # noqa: E501
        if trigger_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_type, allowed_values)
            )

        self._trigger_type = trigger_type

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
        if issubclass(ApiUsageLimitNotificationRuleTriggerConfig, dict):
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
        if not isinstance(other, ApiUsageLimitNotificationRuleTriggerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
