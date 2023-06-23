# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2023. ThingsBoard
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

class IntegrationLifecycleEventNotificationRuleTriggerConfig(object):
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
        'integration_types': 'list[str]',
        'integrations': 'list[str]',
        'notify_on': 'list[str]',
        'only_on_error': 'bool',
        'trigger_type': 'str'
    }

    attribute_map = {
        'integration_types': 'integrationTypes',
        'integrations': 'integrations',
        'notify_on': 'notifyOn',
        'only_on_error': 'onlyOnError',
        'trigger_type': 'triggerType'
    }

    def __init__(self, integration_types=None, integrations=None, notify_on=None, only_on_error=None, trigger_type=None):  # noqa: E501
        """IntegrationLifecycleEventNotificationRuleTriggerConfig - a model defined in Swagger"""  # noqa: E501
        self._integration_types = None
        self._integrations = None
        self._notify_on = None
        self._only_on_error = None
        self._trigger_type = None
        self.discriminator = None
        if integration_types is not None:
            self.integration_types = integration_types
        if integrations is not None:
            self.integrations = integrations
        if notify_on is not None:
            self.notify_on = notify_on
        if only_on_error is not None:
            self.only_on_error = only_on_error
        if trigger_type is not None:
            self.trigger_type = trigger_type

    @property
    def integration_types(self):
        """Gets the integration_types of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The integration_types of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._integration_types

    @integration_types.setter
    def integration_types(self, integration_types):
        """Sets the integration_types of this IntegrationLifecycleEventNotificationRuleTriggerConfig.


        :param integration_types: The integration_types of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["APACHE_PULSAR", "AWS_IOT", "AWS_KINESIS", "AWS_SQS", "AZURE_EVENT_HUB", "AZURE_IOT_HUB", "AZURE_SERVICE_BUS", "CHIRPSTACK", "COAP", "CUSTOM", "HTTP", "IBM_WATSON_IOT", "KAFKA", "LORIOT", "MQTT", "OCEANCONNECT", "OPC_UA", "PUB_SUB", "RABBITMQ", "SIGFOX", "TCP", "THINGPARK", "TMOBILE_IOT_CDP", "TPE", "TTI", "TTN", "TUYA", "UDP"]  # noqa: E501
        if not set(integration_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `integration_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(integration_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._integration_types = integration_types

    @property
    def integrations(self):
        """Gets the integrations of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The integrations of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this IntegrationLifecycleEventNotificationRuleTriggerConfig.


        :param integrations: The integrations of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """

        self._integrations = integrations

    @property
    def notify_on(self):
        """Gets the notify_on of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The notify_on of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._notify_on

    @notify_on.setter
    def notify_on(self, notify_on):
        """Sets the notify_on of this IntegrationLifecycleEventNotificationRuleTriggerConfig.


        :param notify_on: The notify_on of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ACTIVATED", "CREATED", "DELETED", "FAILED", "STARTED", "STOPPED", "SUSPENDED", "UPDATED"]  # noqa: E501
        if not set(notify_on).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `notify_on` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(notify_on) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._notify_on = notify_on

    @property
    def only_on_error(self):
        """Gets the only_on_error of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The only_on_error of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._only_on_error

    @only_on_error.setter
    def only_on_error(self, only_on_error):
        """Sets the only_on_error of this IntegrationLifecycleEventNotificationRuleTriggerConfig.


        :param only_on_error: The only_on_error of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: bool
        """

        self._only_on_error = only_on_error

    @property
    def trigger_type(self):
        """Gets the trigger_type of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501


        :return: The trigger_type of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this IntegrationLifecycleEventNotificationRuleTriggerConfig.


        :param trigger_type: The trigger_type of this IntegrationLifecycleEventNotificationRuleTriggerConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "ALARM_ASSIGNMENT", "ALARM_COMMENT", "API_USAGE_LIMIT", "DEVICE_ACTIVITY", "ENTITIES_LIMIT", "ENTITY_ACTION", "INTEGRATION_LIFECYCLE_EVENT", "NEW_PLATFORM_VERSION", "RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT"]  # noqa: E501
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
        if issubclass(IntegrationLifecycleEventNotificationRuleTriggerConfig, dict):
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
        if not isinstance(other, IntegrationLifecycleEventNotificationRuleTriggerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
