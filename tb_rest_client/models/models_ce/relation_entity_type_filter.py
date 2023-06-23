# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0
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

class RelationEntityTypeFilter(object):
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
        'relation_type': 'str',
        'entity_types': 'list[str]'
    }

    attribute_map = {
        'relation_type': 'relationType',
        'entity_types': 'entityTypes'
    }

    def __init__(self, relation_type=None, entity_types=None):  # noqa: E501
        """RelationEntityTypeFilter - a model defined in Swagger"""  # noqa: E501
        self._relation_type = None
        self._entity_types = None
        self.discriminator = None
        if relation_type is not None:
            self.relation_type = relation_type
        if entity_types is not None:
            self.entity_types = entity_types

    @property
    def relation_type(self):
        """Gets the relation_type of this RelationEntityTypeFilter.  # noqa: E501

        Type of the relation between root entity and other entity (e.g. 'Contains' or 'Manages').  # noqa: E501

        :return: The relation_type of this RelationEntityTypeFilter.  # noqa: E501
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this RelationEntityTypeFilter.

        Type of the relation between root entity and other entity (e.g. 'Contains' or 'Manages').  # noqa: E501

        :param relation_type: The relation_type of this RelationEntityTypeFilter.  # noqa: E501
        :type: str
        """

        self._relation_type = relation_type

    @property
    def entity_types(self):
        """Gets the entity_types of this RelationEntityTypeFilter.  # noqa: E501

        Array of entity types to filter the related entities (e.g. 'DEVICE', 'ASSET').  # noqa: E501

        :return: The entity_types of this RelationEntityTypeFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._entity_types

    @entity_types.setter
    def entity_types(self, entity_types):
        """Sets the entity_types of this RelationEntityTypeFilter.

        Array of entity types to filter the related entities (e.g. 'DEVICE', 'ASSET').  # noqa: E501

        :param entity_types: The entity_types of this RelationEntityTypeFilter.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ALARM", "API_USAGE_STATE", "ASSET", "ASSET_PROFILE", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_VIEW", "NOTIFICATION", "NOTIFICATION_REQUEST", "NOTIFICATION_RULE", "NOTIFICATION_TARGET", "NOTIFICATION_TEMPLATE", "OTA_PACKAGE", "QUEUE", "RPC", "RULE_CHAIN", "RULE_NODE", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if not set(entity_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `entity_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(entity_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._entity_types = entity_types

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
        if issubclass(RelationEntityTypeFilter, dict):
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
        if not isinstance(other, RelationEntityTypeFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
