# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.3PE
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

class EntityRelationsQuery(object):
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
        'filters': 'list[RelationEntityTypeFilter]',
        'parameters': 'RelationsSearchParameters'
    }

    attribute_map = {
        'filters': 'filters',
        'parameters': 'parameters'
    }

    def __init__(self, filters=None, parameters=None):  # noqa: E501
        """EntityRelationsQuery - a model defined in Swagger"""  # noqa: E501
        self._filters = None
        self._parameters = None
        self.discriminator = None
        if filters is not None:
            self.filters = filters
        if parameters is not None:
            self.parameters = parameters

    @property
    def filters(self):
        """Gets the filters of this EntityRelationsQuery.  # noqa: E501

        Main filters.  # noqa: E501

        :return: The filters of this EntityRelationsQuery.  # noqa: E501
        :rtype: list[RelationEntityTypeFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this EntityRelationsQuery.

        Main filters.  # noqa: E501

        :param filters: The filters of this EntityRelationsQuery.  # noqa: E501
        :type: list[RelationEntityTypeFilter]
        """

        self._filters = filters

    @property
    def parameters(self):
        """Gets the parameters of this EntityRelationsQuery.  # noqa: E501


        :return: The parameters of this EntityRelationsQuery.  # noqa: E501
        :rtype: RelationsSearchParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this EntityRelationsQuery.


        :param parameters: The parameters of this EntityRelationsQuery.  # noqa: E501
        :type: RelationsSearchParameters
        """

        self._parameters = parameters

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
        if issubclass(EntityRelationsQuery, dict):
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
        if not isinstance(other, EntityRelationsQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
