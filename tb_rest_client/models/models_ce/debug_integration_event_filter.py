# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.4.7PAAS
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
from tb_rest_client.models.models_ce.event_filter import EventFilter  # noqa: F401,E501

class DebugIntegrationEventFilter(EventFilter):
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
        'error': 'bool',
        'message': 'str',
        'not_empty': 'bool',
        'status_integration': 'str',
        'type': 'str',
        'event_type': 'str',
        'server': 'str',
        'error_str': 'str'
    }
    if hasattr(EventFilter, "swagger_types"):
        swagger_types.update(EventFilter.swagger_types)

    attribute_map = {
        'error': 'error',
        'message': 'message',
        'not_empty': 'notEmpty',
        'status_integration': 'statusIntegration',
        'type': 'type',
        'event_type': 'eventType',
        'server': 'server',
        'error_str': 'errorStr'
    }
    if hasattr(EventFilter, "attribute_map"):
        attribute_map.update(EventFilter.attribute_map)

    def __init__(self, error=None, message=None, not_empty=None, status_integration=None, type=None, event_type=None, server=None, error_str=None, *args, **kwargs):  # noqa: E501
        """DebugIntegrationEventFilter - a model defined in Swagger"""  # noqa: E501
        self._error = None
        self._message = None
        self._not_empty = None
        self._status_integration = None
        self._type = None
        self._event_type = None
        self._server = None
        self._error_str = None
        self.discriminator = None
        if error is not None:
            self.error = error
        if message is not None:
            self.message = message
        if not_empty is not None:
            self.not_empty = not_empty
        if status_integration is not None:
            self.status_integration = status_integration
        if type is not None:
            self.type = type
        self.event_type = event_type
        if server is not None:
            self.server = server
        if error_str is not None:
            self.error_str = error_str
        EventFilter.__init__(self, *args, **kwargs)

    @property
    def error(self):
        """Gets the error of this DebugIntegrationEventFilter.  # noqa: E501


        :return: The error of this DebugIntegrationEventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DebugIntegrationEventFilter.


        :param error: The error of this DebugIntegrationEventFilter.  # noqa: E501
        :type: bool
        """

        self._error = error

    @property
    def message(self):
        """Gets the message of this DebugIntegrationEventFilter.  # noqa: E501


        :return: The message of this DebugIntegrationEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DebugIntegrationEventFilter.


        :param message: The message of this DebugIntegrationEventFilter.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def not_empty(self):
        """Gets the not_empty of this DebugIntegrationEventFilter.  # noqa: E501


        :return: The not_empty of this DebugIntegrationEventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._not_empty

    @not_empty.setter
    def not_empty(self, not_empty):
        """Sets the not_empty of this DebugIntegrationEventFilter.


        :param not_empty: The not_empty of this DebugIntegrationEventFilter.  # noqa: E501
        :type: bool
        """

        self._not_empty = not_empty

    @property
    def status_integration(self):
        """Gets the status_integration of this DebugIntegrationEventFilter.  # noqa: E501


        :return: The status_integration of this DebugIntegrationEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._status_integration

    @status_integration.setter
    def status_integration(self, status_integration):
        """Sets the status_integration of this DebugIntegrationEventFilter.


        :param status_integration: The status_integration of this DebugIntegrationEventFilter.  # noqa: E501
        :type: str
        """

        self._status_integration = status_integration

    @property
    def type(self):
        """Gets the type of this DebugIntegrationEventFilter.  # noqa: E501


        :return: The type of this DebugIntegrationEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DebugIntegrationEventFilter.


        :param type: The type of this DebugIntegrationEventFilter.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def event_type(self):
        """Gets the event_type of this DebugIntegrationEventFilter.  # noqa: E501

        String value representing the event type  # noqa: E501

        :return: The event_type of this DebugIntegrationEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this DebugIntegrationEventFilter.

        String value representing the event type  # noqa: E501

        :param event_type: The event_type of this DebugIntegrationEventFilter.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DEBUG_CONVERTER", "DEBUG_INTEGRATION", "DEBUG_RULE_CHAIN", "DEBUG_RULE_NODE", "ERROR", "LC_EVENT", "RAW_DATA", "STATS"]  # noqa: E501
        if event_type not in allowed_values:
            raise ValueError(
                "Invalid value for `event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(event_type, allowed_values)
            )

        self._event_type = event_type

    @property
    def server(self):
        """Gets the server of this DebugIntegrationEventFilter.  # noqa: E501

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :return: The server of this DebugIntegrationEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this DebugIntegrationEventFilter.

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :param server: The server of this DebugIntegrationEventFilter.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def error_str(self):
        """Gets the error_str of this DebugIntegrationEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :return: The error_str of this DebugIntegrationEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._error_str

    @error_str.setter
    def error_str(self, error_str):
        """Sets the error_str of this DebugIntegrationEventFilter.

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :param error_str: The error_str of this DebugIntegrationEventFilter.  # noqa: E501
        :type: str
        """

        self._error_str = error_str

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
        if issubclass(DebugIntegrationEventFilter, dict):
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
        if not isinstance(other, DebugIntegrationEventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
