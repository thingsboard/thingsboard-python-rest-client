# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.1.0PE
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

class EntityDataPageLink(object):
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
        'page_size': 'int',
        'page': 'int',
        'text_search': 'str',
        'sort_order': 'EntityDataSortOrder',
        'dynamic': 'bool'
    }

    attribute_map = {
        'page_size': 'pageSize',
        'page': 'page',
        'text_search': 'textSearch',
        'sort_order': 'sortOrder',
        'dynamic': 'dynamic'
    }

    def __init__(self, page_size=None, page=None, text_search=None, sort_order=None, dynamic=None):  # noqa: E501
        """EntityDataPageLink - a model defined in Swagger"""  # noqa: E501
        self._page_size = None
        self._page = None
        self._text_search = None
        self._sort_order = None
        self._dynamic = None
        self.discriminator = None
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
    def page_size(self):
        """Gets the page_size of this EntityDataPageLink.  # noqa: E501


        :return: The page_size of this EntityDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this EntityDataPageLink.


        :param page_size: The page_size of this EntityDataPageLink.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def page(self):
        """Gets the page of this EntityDataPageLink.  # noqa: E501


        :return: The page of this EntityDataPageLink.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this EntityDataPageLink.


        :param page: The page of this EntityDataPageLink.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def text_search(self):
        """Gets the text_search of this EntityDataPageLink.  # noqa: E501


        :return: The text_search of this EntityDataPageLink.  # noqa: E501
        :rtype: str
        """
        return self._text_search

    @text_search.setter
    def text_search(self, text_search):
        """Sets the text_search of this EntityDataPageLink.


        :param text_search: The text_search of this EntityDataPageLink.  # noqa: E501
        :type: str
        """

        self._text_search = text_search

    @property
    def sort_order(self):
        """Gets the sort_order of this EntityDataPageLink.  # noqa: E501


        :return: The sort_order of this EntityDataPageLink.  # noqa: E501
        :rtype: EntityDataSortOrder
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this EntityDataPageLink.


        :param sort_order: The sort_order of this EntityDataPageLink.  # noqa: E501
        :type: EntityDataSortOrder
        """

        self._sort_order = sort_order

    @property
    def dynamic(self):
        """Gets the dynamic of this EntityDataPageLink.  # noqa: E501


        :return: The dynamic of this EntityDataPageLink.  # noqa: E501
        :rtype: bool
        """
        return self._dynamic

    @dynamic.setter
    def dynamic(self, dynamic):
        """Sets the dynamic of this EntityDataPageLink.


        :param dynamic: The dynamic of this EntityDataPageLink.  # noqa: E501
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
        if issubclass(EntityDataPageLink, dict):
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
        if not isinstance(other, EntityDataPageLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
