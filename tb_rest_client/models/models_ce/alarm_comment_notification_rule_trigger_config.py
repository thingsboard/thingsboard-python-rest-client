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

class AlarmCommentNotificationRuleTriggerConfig(object):
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
        'alarm_severities': 'list[str]',
        'alarm_statuses': 'list[str]',
        'alarm_types': 'list[str]',
        'notify_on_comment_update': 'bool',
        'only_user_comments': 'bool',
        'trigger_type': 'str'
    }

    attribute_map = {
        'alarm_severities': 'alarmSeverities',
        'alarm_statuses': 'alarmStatuses',
        'alarm_types': 'alarmTypes',
        'notify_on_comment_update': 'notifyOnCommentUpdate',
        'only_user_comments': 'onlyUserComments',
        'trigger_type': 'triggerType'
    }

    def __init__(self, alarm_severities=None, alarm_statuses=None, alarm_types=None, notify_on_comment_update=None, only_user_comments=None, trigger_type=None):  # noqa: E501
        """AlarmCommentNotificationRuleTriggerConfig - a model defined in Swagger"""  # noqa: E501
        self._alarm_severities = None
        self._alarm_statuses = None
        self._alarm_types = None
        self._notify_on_comment_update = None
        self._only_user_comments = None
        self._trigger_type = None
        self.discriminator = None
        if alarm_severities is not None:
            self.alarm_severities = alarm_severities
        if alarm_statuses is not None:
            self.alarm_statuses = alarm_statuses
        if alarm_types is not None:
            self.alarm_types = alarm_types
        if notify_on_comment_update is not None:
            self.notify_on_comment_update = notify_on_comment_update
        if only_user_comments is not None:
            self.only_user_comments = only_user_comments
        if trigger_type is not None:
            self.trigger_type = trigger_type

    @property
    def alarm_severities(self):
        """Gets the alarm_severities of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501


        :return: The alarm_severities of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._alarm_severities

    @alarm_severities.setter
    def alarm_severities(self, alarm_severities):
        """Sets the alarm_severities of this AlarmCommentNotificationRuleTriggerConfig.


        :param alarm_severities: The alarm_severities of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["CRITICAL", "INDETERMINATE", "MAJOR", "MINOR", "WARNING"]  # noqa: E501
        if not set(alarm_severities).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `alarm_severities` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(alarm_severities) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._alarm_severities = alarm_severities

    @property
    def alarm_statuses(self):
        """Gets the alarm_statuses of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501


        :return: The alarm_statuses of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._alarm_statuses

    @alarm_statuses.setter
    def alarm_statuses(self, alarm_statuses):
        """Sets the alarm_statuses of this AlarmCommentNotificationRuleTriggerConfig.


        :param alarm_statuses: The alarm_statuses of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ACK", "ACTIVE", "ANY", "CLEARED", "UNACK"]  # noqa: E501
        if not set(alarm_statuses).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `alarm_statuses` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(alarm_statuses) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._alarm_statuses = alarm_statuses

    @property
    def alarm_types(self):
        """Gets the alarm_types of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501


        :return: The alarm_types of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._alarm_types

    @alarm_types.setter
    def alarm_types(self, alarm_types):
        """Sets the alarm_types of this AlarmCommentNotificationRuleTriggerConfig.


        :param alarm_types: The alarm_types of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """

        self._alarm_types = alarm_types

    @property
    def notify_on_comment_update(self):
        """Gets the notify_on_comment_update of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501


        :return: The notify_on_comment_update of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._notify_on_comment_update

    @notify_on_comment_update.setter
    def notify_on_comment_update(self, notify_on_comment_update):
        """Sets the notify_on_comment_update of this AlarmCommentNotificationRuleTriggerConfig.


        :param notify_on_comment_update: The notify_on_comment_update of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :type: bool
        """

        self._notify_on_comment_update = notify_on_comment_update

    @property
    def only_user_comments(self):
        """Gets the only_user_comments of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501


        :return: The only_user_comments of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._only_user_comments

    @only_user_comments.setter
    def only_user_comments(self, only_user_comments):
        """Sets the only_user_comments of this AlarmCommentNotificationRuleTriggerConfig.


        :param only_user_comments: The only_user_comments of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :type: bool
        """

        self._only_user_comments = only_user_comments

    @property
    def trigger_type(self):
        """Gets the trigger_type of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501


        :return: The trigger_type of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this AlarmCommentNotificationRuleTriggerConfig.


        :param trigger_type: The trigger_type of this AlarmCommentNotificationRuleTriggerConfig.  # noqa: E501
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
        if issubclass(AlarmCommentNotificationRuleTriggerConfig, dict):
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
        if not isinstance(other, AlarmCommentNotificationRuleTriggerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
