# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PageDataRuleChain(object):
    """NOTE: This class is auto generated by the swagger code generator program.
from tb_rest_client.api_client import ApiClient
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
        'data': 'list[RuleChain]',
        'total_pages': 'int',
        'total_elements': 'int',
        'has_next': 'bool'
    }

    attribute_map = {
        'data': 'data',
        'total_pages': 'totalPages',
        'total_elements': 'totalElements',
        'has_next': 'hasNext'
    }

    def __init__(self, data=None, total_pages=None, total_elements=None, has_next=None):  # noqa: E501
        """PageDataRuleChain - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._total_pages = None
        self._total_elements = None
        self._has_next = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if total_pages is not None:
            self.total_pages = total_pages
        if total_elements is not None:
            self.total_elements = total_elements
        if has_next is not None:
            self.has_next = has_next

    @property
    def data(self):
        """Gets the data of this PageDataRuleChain.  # noqa: E501

        Array of the entities  # noqa: E501

        :return: The data of this PageDataRuleChain.  # noqa: E501
        :rtype: list[RuleChain]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PageDataRuleChain.

        Array of the entities  # noqa: E501

        :param data: The data of this PageDataRuleChain.  # noqa: E501
        :type: list[RuleChain]
        """

        self._data = data

    @property
    def total_pages(self):
        """Gets the total_pages of this PageDataRuleChain.  # noqa: E501

        Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria  # noqa: E501

        :return: The total_pages of this PageDataRuleChain.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this PageDataRuleChain.

        Total number of available pages. Calculated based on the 'pageSize' request parameter and total number of entities that match search criteria  # noqa: E501

        :param total_pages: The total_pages of this PageDataRuleChain.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def total_elements(self):
        """Gets the total_elements of this PageDataRuleChain.  # noqa: E501

        Total number of elements in all available pages  # noqa: E501

        :return: The total_elements of this PageDataRuleChain.  # noqa: E501
        :rtype: int
        """
        return self._total_elements

    @total_elements.setter
    def total_elements(self, total_elements):
        """Sets the total_elements of this PageDataRuleChain.

        Total number of elements in all available pages  # noqa: E501

        :param total_elements: The total_elements of this PageDataRuleChain.  # noqa: E501
        :type: int
        """

        self._total_elements = total_elements

    @property
    def has_next(self):
        """Gets the has_next of this PageDataRuleChain.  # noqa: E501

        'false' value indicates the end of the result set  # noqa: E501

        :return: The has_next of this PageDataRuleChain.  # noqa: E501
        :rtype: bool
        """
        return self._has_next

    @has_next.setter
    def has_next(self, has_next):
        """Sets the has_next of this PageDataRuleChain.

        'false' value indicates the end of the result set  # noqa: E501

        :param has_next: The has_next of this PageDataRuleChain.  # noqa: E501
        :type: bool
        """

        self._has_next = has_next

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
        if issubclass(PageDataRuleChain, dict):
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
        if not isinstance(other, PageDataRuleChain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
