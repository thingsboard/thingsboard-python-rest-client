# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.0.0PE
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

class AlarmCountQuery(object):
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
        'start_ts': 'int',
        'end_ts': 'int',
        'time_window': 'int',
        'type_list': 'list[str]',
        'status_list': 'list[str]',
        'severity_list': 'list[str]',
        'search_propagated_alarms': 'bool',
        'assignee_id': 'UserId',
        'entity_filter': 'OneOfAlarmCountQueryEntityFilter',
        'key_filters': 'list[KeyFilter]'
    }

    attribute_map = {
        'start_ts': 'startTs',
        'end_ts': 'endTs',
        'time_window': 'timeWindow',
        'type_list': 'typeList',
        'status_list': 'statusList',
        'severity_list': 'severityList',
        'search_propagated_alarms': 'searchPropagatedAlarms',
        'assignee_id': 'assigneeId',
        'entity_filter': 'entityFilter',
        'key_filters': 'keyFilters'
    }

    def __init__(self, start_ts=None, end_ts=None, time_window=None, type_list=None, status_list=None, severity_list=None, search_propagated_alarms=None, assignee_id=None, entity_filter=None, key_filters=None):  # noqa: E501
        """AlarmCountQuery - a model defined in Swagger"""  # noqa: E501
        self._start_ts = None
        self._end_ts = None
        self._time_window = None
        self._type_list = None
        self._status_list = None
        self._severity_list = None
        self._search_propagated_alarms = None
        self._assignee_id = None
        self._entity_filter = None
        self._key_filters = None
        self.discriminator = None
        if start_ts is not None:
            self.start_ts = start_ts
        if end_ts is not None:
            self.end_ts = end_ts
        if time_window is not None:
            self.time_window = time_window
        if type_list is not None:
            self.type_list = type_list
        if status_list is not None:
            self.status_list = status_list
        if severity_list is not None:
            self.severity_list = severity_list
        if search_propagated_alarms is not None:
            self.search_propagated_alarms = search_propagated_alarms
        if assignee_id is not None:
            self.assignee_id = assignee_id
        if entity_filter is not None:
            self.entity_filter = entity_filter
        if key_filters is not None:
            self.key_filters = key_filters

    @property
    def start_ts(self):
        """Gets the start_ts of this AlarmCountQuery.  # noqa: E501


        :return: The start_ts of this AlarmCountQuery.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this AlarmCountQuery.


        :param start_ts: The start_ts of this AlarmCountQuery.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def end_ts(self):
        """Gets the end_ts of this AlarmCountQuery.  # noqa: E501


        :return: The end_ts of this AlarmCountQuery.  # noqa: E501
        :rtype: int
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this AlarmCountQuery.


        :param end_ts: The end_ts of this AlarmCountQuery.  # noqa: E501
        :type: int
        """

        self._end_ts = end_ts

    @property
    def time_window(self):
        """Gets the time_window of this AlarmCountQuery.  # noqa: E501


        :return: The time_window of this AlarmCountQuery.  # noqa: E501
        :rtype: int
        """
        return self._time_window

    @time_window.setter
    def time_window(self, time_window):
        """Sets the time_window of this AlarmCountQuery.


        :param time_window: The time_window of this AlarmCountQuery.  # noqa: E501
        :type: int
        """

        self._time_window = time_window

    @property
    def type_list(self):
        """Gets the type_list of this AlarmCountQuery.  # noqa: E501


        :return: The type_list of this AlarmCountQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._type_list

    @type_list.setter
    def type_list(self, type_list):
        """Sets the type_list of this AlarmCountQuery.


        :param type_list: The type_list of this AlarmCountQuery.  # noqa: E501
        :type: list[str]
        """

        self._type_list = type_list

    @property
    def status_list(self):
        """Gets the status_list of this AlarmCountQuery.  # noqa: E501


        :return: The status_list of this AlarmCountQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        """Sets the status_list of this AlarmCountQuery.


        :param status_list: The status_list of this AlarmCountQuery.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ANY", "ACTIVE", "CLEARED", "ACK", "UNACK"]  # noqa: E501
        if not set(status_list).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `status_list` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(status_list) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._status_list = status_list

    @property
    def severity_list(self):
        """Gets the severity_list of this AlarmCountQuery.  # noqa: E501


        :return: The severity_list of this AlarmCountQuery.  # noqa: E501
        :rtype: list[str]
        """
        return self._severity_list

    @severity_list.setter
    def severity_list(self, severity_list):
        """Sets the severity_list of this AlarmCountQuery.


        :param severity_list: The severity_list of this AlarmCountQuery.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["CRITICAL", "MAJOR", "MINOR", "WARNING", "INDETERMINATE"]  # noqa: E501
        if not set(severity_list).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `severity_list` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(severity_list) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._severity_list = severity_list

    @property
    def search_propagated_alarms(self):
        """Gets the search_propagated_alarms of this AlarmCountQuery.  # noqa: E501


        :return: The search_propagated_alarms of this AlarmCountQuery.  # noqa: E501
        :rtype: bool
        """
        return self._search_propagated_alarms

    @search_propagated_alarms.setter
    def search_propagated_alarms(self, search_propagated_alarms):
        """Sets the search_propagated_alarms of this AlarmCountQuery.


        :param search_propagated_alarms: The search_propagated_alarms of this AlarmCountQuery.  # noqa: E501
        :type: bool
        """

        self._search_propagated_alarms = search_propagated_alarms

    @property
    def assignee_id(self):
        """Gets the assignee_id of this AlarmCountQuery.  # noqa: E501


        :return: The assignee_id of this AlarmCountQuery.  # noqa: E501
        :rtype: UserId
        """
        return self._assignee_id

    @assignee_id.setter
    def assignee_id(self, assignee_id):
        """Sets the assignee_id of this AlarmCountQuery.


        :param assignee_id: The assignee_id of this AlarmCountQuery.  # noqa: E501
        :type: UserId
        """

        self._assignee_id = assignee_id

    @property
    def entity_filter(self):
        """Gets the entity_filter of this AlarmCountQuery.  # noqa: E501


        :return: The entity_filter of this AlarmCountQuery.  # noqa: E501
        :rtype: OneOfAlarmCountQueryEntityFilter
        """
        return self._entity_filter

    @entity_filter.setter
    def entity_filter(self, entity_filter):
        """Sets the entity_filter of this AlarmCountQuery.


        :param entity_filter: The entity_filter of this AlarmCountQuery.  # noqa: E501
        :type: OneOfAlarmCountQueryEntityFilter
        """

        self._entity_filter = entity_filter

    @property
    def key_filters(self):
        """Gets the key_filters of this AlarmCountQuery.  # noqa: E501


        :return: The key_filters of this AlarmCountQuery.  # noqa: E501
        :rtype: list[KeyFilter]
        """
        return self._key_filters

    @key_filters.setter
    def key_filters(self, key_filters):
        """Sets the key_filters of this AlarmCountQuery.


        :param key_filters: The key_filters of this AlarmCountQuery.  # noqa: E501
        :type: list[KeyFilter]
        """

        self._key_filters = key_filters

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
        if issubclass(AlarmCountQuery, dict):
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
        if not isinstance(other, AlarmCountQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
