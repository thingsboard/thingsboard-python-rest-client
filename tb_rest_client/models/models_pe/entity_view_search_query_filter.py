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
from tb_rest_client.models.models_pe.entity_filter import EntityFilter  # noqa: F401,E501

class EntityViewSearchQueryFilter(EntityFilter):
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
        'direction': 'str',
        'entity_view_types': 'list[str]',
        'fetch_last_level_only': 'bool',
        'max_level': 'int',
        'relation_type': 'str',
        'root_entity': 'EntityId'
    }
    if hasattr(EntityFilter, "swagger_types"):
        swagger_types.update(EntityFilter.swagger_types)

    attribute_map = {
        'direction': 'direction',
        'entity_view_types': 'entityViewTypes',
        'fetch_last_level_only': 'fetchLastLevelOnly',
        'max_level': 'maxLevel',
        'relation_type': 'relationType',
        'root_entity': 'rootEntity'
    }
    if hasattr(EntityFilter, "attribute_map"):
        attribute_map.update(EntityFilter.attribute_map)

    def __init__(self, direction=None, entity_view_types=None, fetch_last_level_only=None, max_level=None, relation_type=None, root_entity=None, *args, **kwargs):  # noqa: E501
        """EntityViewSearchQueryFilter - a model defined in Swagger"""  # noqa: E501
        self._direction = None
        self._entity_view_types = None
        self._fetch_last_level_only = None
        self._max_level = None
        self._relation_type = None
        self._root_entity = None
        self.discriminator = None
        if direction is not None:
            self.direction = direction
        if entity_view_types is not None:
            self.entity_view_types = entity_view_types
        if fetch_last_level_only is not None:
            self.fetch_last_level_only = fetch_last_level_only
        if max_level is not None:
            self.max_level = max_level
        if relation_type is not None:
            self.relation_type = relation_type
        if root_entity is not None:
            self.root_entity = root_entity
        EntityFilter.__init__(self, *args, **kwargs)

    @property
    def direction(self):
        """Gets the direction of this EntityViewSearchQueryFilter.  # noqa: E501


        :return: The direction of this EntityViewSearchQueryFilter.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this EntityViewSearchQueryFilter.


        :param direction: The direction of this EntityViewSearchQueryFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["FROM", "TO"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def entity_view_types(self):
        """Gets the entity_view_types of this EntityViewSearchQueryFilter.  # noqa: E501


        :return: The entity_view_types of this EntityViewSearchQueryFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._entity_view_types

    @entity_view_types.setter
    def entity_view_types(self, entity_view_types):
        """Sets the entity_view_types of this EntityViewSearchQueryFilter.


        :param entity_view_types: The entity_view_types of this EntityViewSearchQueryFilter.  # noqa: E501
        :type: list[str]
        """

        self._entity_view_types = entity_view_types

    @property
    def fetch_last_level_only(self):
        """Gets the fetch_last_level_only of this EntityViewSearchQueryFilter.  # noqa: E501


        :return: The fetch_last_level_only of this EntityViewSearchQueryFilter.  # noqa: E501
        :rtype: bool
        """
        return self._fetch_last_level_only

    @fetch_last_level_only.setter
    def fetch_last_level_only(self, fetch_last_level_only):
        """Sets the fetch_last_level_only of this EntityViewSearchQueryFilter.


        :param fetch_last_level_only: The fetch_last_level_only of this EntityViewSearchQueryFilter.  # noqa: E501
        :type: bool
        """

        self._fetch_last_level_only = fetch_last_level_only

    @property
    def max_level(self):
        """Gets the max_level of this EntityViewSearchQueryFilter.  # noqa: E501


        :return: The max_level of this EntityViewSearchQueryFilter.  # noqa: E501
        :rtype: int
        """
        return self._max_level

    @max_level.setter
    def max_level(self, max_level):
        """Sets the max_level of this EntityViewSearchQueryFilter.


        :param max_level: The max_level of this EntityViewSearchQueryFilter.  # noqa: E501
        :type: int
        """

        self._max_level = max_level

    @property
    def relation_type(self):
        """Gets the relation_type of this EntityViewSearchQueryFilter.  # noqa: E501


        :return: The relation_type of this EntityViewSearchQueryFilter.  # noqa: E501
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this EntityViewSearchQueryFilter.


        :param relation_type: The relation_type of this EntityViewSearchQueryFilter.  # noqa: E501
        :type: str
        """

        self._relation_type = relation_type

    @property
    def root_entity(self):
        """Gets the root_entity of this EntityViewSearchQueryFilter.  # noqa: E501


        :return: The root_entity of this EntityViewSearchQueryFilter.  # noqa: E501
        :rtype: EntityId
        """
        return self._root_entity

    @root_entity.setter
    def root_entity(self, root_entity):
        """Sets the root_entity of this EntityViewSearchQueryFilter.


        :param root_entity: The root_entity of this EntityViewSearchQueryFilter.  # noqa: E501
        :type: EntityId
        """

        self._root_entity = root_entity

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
        if issubclass(EntityViewSearchQueryFilter, dict):
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
        if not isinstance(other, EntityViewSearchQueryFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
