# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.7.0PE
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

class AlarmDataPageLink(object):
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
        'page_size': 'int',
        'page': 'int',
        'text_search': 'str',
        'sort_order': 'EntityDataSortOrder',
        'dynamic': 'bool'
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
        'page_size': 'pageSize',
        'page': 'page',
        'text_search': 'textSearch',
        'sort_order': 'sortOrder',
        'dynamic': 'dynamic'
    }

    def __init__(self, start_ts=None, end_ts=None, time_window=None, type_list=None, status_list=None, severity_list=None, search_propagated_alarms=None, assignee_id=None, page_size=None, page=None, text_search=None, sort_order=None, dynamic=None):  # noqa: E501
        """AlarmDataPageLink - a model defined in Swagger"""  # noqa: E501
        self._start_ts = None
        self._end_ts = None
        self._time_window = None
        self._type_list = None
        self._status_list = None
        self._severity_list = None
        self._search_propagated_alarms = None
        self._assignee_id = None
        self._page_size = None
        self._page = None
        self._text_search = None
        self._sort_order = None
        self._dynamic = None
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
        if page_size is not None:
            self.page_size = page_size
        if page is not None:
            self.page = page
        if text_search is not None:
            self.text_search = text_search
        if sort_order is not None:
            self.sort_order = sort_order
        if dynamic is not None:
            self.dynamic = dynamic

    @property
    def start_ts(self):
        """Gets the start_ts of this AlarmDataPageLink.  # noqa: E501


        :return: The start_ts of this AlarmDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._start_ts

    @start_ts.setter
    def start_ts(self, start_ts):
        """Sets the start_ts of this AlarmDataPageLink.


        :param start_ts: The start_ts of this AlarmDataPageLink.  # noqa: E501
        :type: int
        """

        self._start_ts = start_ts

    @property
    def end_ts(self):
        """Gets the end_ts of this AlarmDataPageLink.  # noqa: E501


        :return: The end_ts of this AlarmDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._end_ts

    @end_ts.setter
    def end_ts(self, end_ts):
        """Sets the end_ts of this AlarmDataPageLink.


        :param end_ts: The end_ts of this AlarmDataPageLink.  # noqa: E501
        :type: int
        """

        self._end_ts = end_ts

    @property
    def time_window(self):
        """Gets the time_window of this AlarmDataPageLink.  # noqa: E501


        :return: The time_window of this AlarmDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._time_window

    @time_window.setter
    def time_window(self, time_window):
        """Sets the time_window of this AlarmDataPageLink.


        :param time_window: The time_window of this AlarmDataPageLink.  # noqa: E501
        :type: int
        """

        self._time_window = time_window

    @property
    def type_list(self):
        """Gets the type_list of this AlarmDataPageLink.  # noqa: E501


        :return: The type_list of this AlarmDataPageLink.  # noqa: E501
        :rtype: list[str]
        """
        return self._type_list

    @type_list.setter
    def type_list(self, type_list):
        """Sets the type_list of this AlarmDataPageLink.


        :param type_list: The type_list of this AlarmDataPageLink.  # noqa: E501
        :type: list[str]
        """

        self._type_list = type_list

    @property
    def status_list(self):
        """Gets the status_list of this AlarmDataPageLink.  # noqa: E501


        :return: The status_list of this AlarmDataPageLink.  # noqa: E501
        :rtype: list[str]
        """
        return self._status_list

    @status_list.setter
    def status_list(self, status_list):
        """Sets the status_list of this AlarmDataPageLink.


        :param status_list: The status_list of this AlarmDataPageLink.  # noqa: E501
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
        """Gets the severity_list of this AlarmDataPageLink.  # noqa: E501


        :return: The severity_list of this AlarmDataPageLink.  # noqa: E501
        :rtype: list[str]
        """
        return self._severity_list

    @severity_list.setter
    def severity_list(self, severity_list):
        """Sets the severity_list of this AlarmDataPageLink.


        :param severity_list: The severity_list of this AlarmDataPageLink.  # noqa: E501
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
        """Gets the search_propagated_alarms of this AlarmDataPageLink.  # noqa: E501


        :return: The search_propagated_alarms of this AlarmDataPageLink.  # noqa: E501
        :rtype: bool
        """
        return self._search_propagated_alarms

    @search_propagated_alarms.setter
    def search_propagated_alarms(self, search_propagated_alarms):
        """Sets the search_propagated_alarms of this AlarmDataPageLink.


        :param search_propagated_alarms: The search_propagated_alarms of this AlarmDataPageLink.  # noqa: E501
        :type: bool
        """

        self._search_propagated_alarms = search_propagated_alarms

    @property
    def assignee_id(self):
        """Gets the assignee_id of this AlarmDataPageLink.  # noqa: E501


        :return: The assignee_id of this AlarmDataPageLink.  # noqa: E501
        :rtype: UserId
        """
        return self._assignee_id

    @assignee_id.setter
    def assignee_id(self, assignee_id):
        """Sets the assignee_id of this AlarmDataPageLink.


        :param assignee_id: The assignee_id of this AlarmDataPageLink.  # noqa: E501
        :type: UserId
        """

        self._assignee_id = assignee_id

    @property
    def page_size(self):
        """Gets the page_size of this AlarmDataPageLink.  # noqa: E501


        :return: The page_size of this AlarmDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this AlarmDataPageLink.


        :param page_size: The page_size of this AlarmDataPageLink.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def page(self):
        """Gets the page of this AlarmDataPageLink.  # noqa: E501


        :return: The page of this AlarmDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this AlarmDataPageLink.


        :param page: The page of this AlarmDataPageLink.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def text_search(self):
        """Gets the text_search of this AlarmDataPageLink.  # noqa: E501


        :return: The text_search of this AlarmDataPageLink.  # noqa: E501
        :rtype: str
        """
        return self._text_search

    @text_search.setter
    def text_search(self, text_search):
        """Sets the text_search of this AlarmDataPageLink.


        :param text_search: The text_search of this AlarmDataPageLink.  # noqa: E501
        :type: str
        """

        self._text_search = text_search

    @property
    def sort_order(self):
        """Gets the sort_order of this AlarmDataPageLink.  # noqa: E501


        :return: The sort_order of this AlarmDataPageLink.  # noqa: E501
        :rtype: EntityDataSortOrder
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this AlarmDataPageLink.


        :param sort_order: The sort_order of this AlarmDataPageLink.  # noqa: E501
        :type: EntityDataSortOrder
        """

        self._sort_order = sort_order

    @property
    def dynamic(self):
        """Gets the dynamic of this AlarmDataPageLink.  # noqa: E501


        :return: The dynamic of this AlarmDataPageLink.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic

    @dynamic.setter
    def dynamic(self, dynamic):
        """Sets the dynamic of this AlarmDataPageLink.


        :param dynamic: The dynamic of this AlarmDataPageLink.  # noqa: E501
        :type: bool
        """

        self._dynamic = dynamic

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
        if issubclass(AlarmDataPageLink, dict):
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
        if not isinstance(other, AlarmDataPageLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
