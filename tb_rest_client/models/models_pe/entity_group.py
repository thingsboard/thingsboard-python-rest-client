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

class EntityGroup(object):
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
        'id': 'EntityGroupId',
        'created_time': 'int',
        'owner_id': 'EntityId',
        'name': 'str',
        'type': 'str',
        'additional_info': 'JsonNode',
        'configuration': 'JsonNode',
        'group_all': 'bool',
        'edge_group_all': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'owner_id': 'ownerId',
        'name': 'name',
        'type': 'type',
        'additional_info': 'additionalInfo',
        'configuration': 'configuration',
        'group_all': 'groupAll',
        'edge_group_all': 'edgeGroupAll'
    }

    def __init__(self, id=None, created_time=None, owner_id=None, name=None, type=None, additional_info=None, configuration=None, group_all=None, edge_group_all=None):  # noqa: E501
        """EntityGroup - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._owner_id = None
        self._name = None
        self._type = None
        self._additional_info = None
        self._configuration = None
        self._group_all = None
        self._edge_group_all = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if owner_id is not None:
            self.owner_id = owner_id
        self.name = name
        self.type = type
        if additional_info is not None:
            self.additional_info = additional_info
        if configuration is not None:
            self.configuration = configuration
        if group_all is not None:
            self.group_all = group_all
        if edge_group_all is not None:
            self.edge_group_all = edge_group_all

    @property
    def id(self):
        """Gets the id of this EntityGroup.  # noqa: E501


        :return: The id of this EntityGroup.  # noqa: E501
        :rtype: EntityGroupId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityGroup.


        :param id: The id of this EntityGroup.  # noqa: E501
        :type: EntityGroupId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this EntityGroup.  # noqa: E501

        Timestamp of the entity group creation, in milliseconds  # noqa: E501

        :return: The created_time of this EntityGroup.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EntityGroup.

        Timestamp of the entity group creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this EntityGroup.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def owner_id(self):
        """Gets the owner_id of this EntityGroup.  # noqa: E501


        :return: The owner_id of this EntityGroup.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this EntityGroup.


        :param owner_id: The owner_id of this EntityGroup.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def name(self):
        """Gets the name of this EntityGroup.  # noqa: E501

        Name of the entity group  # noqa: E501

        :return: The name of this EntityGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityGroup.

        Name of the entity group  # noqa: E501

        :param name: The name of this EntityGroup.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this EntityGroup.  # noqa: E501


        :return: The type of this EntityGroup.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityGroup.


        :param type: The type of this EntityGroup.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ASSET", "CUSTOMER", "DASHBOARD", "DEVICE", "EDGE", "ENTITY_VIEW", "USER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def additional_info(self):
        """Gets the additional_info of this EntityGroup.  # noqa: E501


        :return: The additional_info of this EntityGroup.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this EntityGroup.


        :param additional_info: The additional_info of this EntityGroup.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def configuration(self):
        """Gets the configuration of this EntityGroup.  # noqa: E501


        :return: The configuration of this EntityGroup.  # noqa: E501
        :rtype: JsonNode
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this EntityGroup.


        :param configuration: The configuration of this EntityGroup.  # noqa: E501
        :type: JsonNode
        """

        self._configuration = configuration

    @property
    def group_all(self):
        """Gets the group_all of this EntityGroup.  # noqa: E501

        Indicates special group 'All' that contains all entities and can't be deleted.  # noqa: E501

        :return: The group_all of this EntityGroup.  # noqa: E501
        :rtype: bool
        """
        return self._group_all

    @group_all.setter
    def group_all(self, group_all):
        """Sets the group_all of this EntityGroup.

        Indicates special group 'All' that contains all entities and can't be deleted.  # noqa: E501

        :param group_all: The group_all of this EntityGroup.  # noqa: E501
        :type: bool
        """

        self._group_all = group_all

    @property
    def edge_group_all(self):
        """Gets the edge_group_all of this EntityGroup.  # noqa: E501

        Indicates special edge group 'All' that contains all entities and can't be deleted.  # noqa: E501

        :return: The edge_group_all of this EntityGroup.  # noqa: E501
        :rtype: bool
        """
        return self._edge_group_all

    @edge_group_all.setter
    def edge_group_all(self, edge_group_all):
        """Sets the edge_group_all of this EntityGroup.

        Indicates special edge group 'All' that contains all entities and can't be deleted.  # noqa: E501

        :param edge_group_all: The edge_group_all of this EntityGroup.  # noqa: E501
        :type: bool
        """

        self._edge_group_all = edge_group_all

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
        if issubclass(EntityGroup, dict):
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
        if not isinstance(other, EntityGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
