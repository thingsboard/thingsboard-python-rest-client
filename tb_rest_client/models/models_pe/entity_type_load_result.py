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

class EntityTypeLoadResult(object):
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
        'created': 'int',
        'deleted': 'int',
        'entity_type': 'str',
        'groups_created': 'int',
        'groups_deleted': 'int',
        'groups_updated': 'int',
        'updated': 'int'
    }

    attribute_map = {
        'created': 'created',
        'deleted': 'deleted',
        'entity_type': 'entityType',
        'groups_created': 'groupsCreated',
        'groups_deleted': 'groupsDeleted',
        'groups_updated': 'groupsUpdated',
        'updated': 'updated'
    }

    def __init__(self, created=None, deleted=None, entity_type=None, groups_created=None, groups_deleted=None, groups_updated=None, updated=None):  # noqa: E501
        """EntityTypeLoadResult - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._deleted = None
        self._entity_type = None
        self._groups_created = None
        self._groups_deleted = None
        self._groups_updated = None
        self._updated = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if deleted is not None:
            self.deleted = deleted
        if entity_type is not None:
            self.entity_type = entity_type
        if groups_created is not None:
            self.groups_created = groups_created
        if groups_deleted is not None:
            self.groups_deleted = groups_deleted
        if groups_updated is not None:
            self.groups_updated = groups_updated
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this EntityTypeLoadResult.  # noqa: E501


        :return: The created of this EntityTypeLoadResult.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EntityTypeLoadResult.


        :param created: The created of this EntityTypeLoadResult.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def deleted(self):
        """Gets the deleted of this EntityTypeLoadResult.  # noqa: E501


        :return: The deleted of this EntityTypeLoadResult.  # noqa: E501
        :rtype: int
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this EntityTypeLoadResult.


        :param deleted: The deleted of this EntityTypeLoadResult.  # noqa: E501
        :type: int
        """

        self._deleted = deleted

    @property
    def entity_type(self):
        """Gets the entity_type of this EntityTypeLoadResult.  # noqa: E501


        :return: The entity_type of this EntityTypeLoadResult.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this EntityTypeLoadResult.


        :param entity_type: The entity_type of this EntityTypeLoadResult.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "API_USAGE_STATE", "ASSET", "ASSET_PROFILE", "BLOB_ENTITY", "CONVERTER", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_GROUP", "ENTITY_VIEW", "GROUP_PERMISSION", "INTEGRATION", "NOTIFICATION", "NOTIFICATION_REQUEST", "NOTIFICATION_RULE", "NOTIFICATION_TARGET", "NOTIFICATION_TEMPLATE", "OTA_PACKAGE", "QUEUE", "ROLE", "RPC", "RULE_CHAIN", "RULE_NODE", "SCHEDULER_EVENT", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def groups_created(self):
        """Gets the groups_created of this EntityTypeLoadResult.  # noqa: E501


        :return: The groups_created of this EntityTypeLoadResult.  # noqa: E501
        :rtype: int
        """
        return self._groups_created

    @groups_created.setter
    def groups_created(self, groups_created):
        """Sets the groups_created of this EntityTypeLoadResult.


        :param groups_created: The groups_created of this EntityTypeLoadResult.  # noqa: E501
        :type: int
        """

        self._groups_created = groups_created

    @property
    def groups_deleted(self):
        """Gets the groups_deleted of this EntityTypeLoadResult.  # noqa: E501


        :return: The groups_deleted of this EntityTypeLoadResult.  # noqa: E501
        :rtype: int
        """
        return self._groups_deleted

    @groups_deleted.setter
    def groups_deleted(self, groups_deleted):
        """Sets the groups_deleted of this EntityTypeLoadResult.


        :param groups_deleted: The groups_deleted of this EntityTypeLoadResult.  # noqa: E501
        :type: int
        """

        self._groups_deleted = groups_deleted

    @property
    def groups_updated(self):
        """Gets the groups_updated of this EntityTypeLoadResult.  # noqa: E501


        :return: The groups_updated of this EntityTypeLoadResult.  # noqa: E501
        :rtype: int
        """
        return self._groups_updated

    @groups_updated.setter
    def groups_updated(self, groups_updated):
        """Sets the groups_updated of this EntityTypeLoadResult.


        :param groups_updated: The groups_updated of this EntityTypeLoadResult.  # noqa: E501
        :type: int
        """

        self._groups_updated = groups_updated

    @property
    def updated(self):
        """Gets the updated of this EntityTypeLoadResult.  # noqa: E501


        :return: The updated of this EntityTypeLoadResult.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this EntityTypeLoadResult.


        :param updated: The updated of this EntityTypeLoadResult.  # noqa: E501
        :type: int
        """

        self._updated = updated

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
        if issubclass(EntityTypeLoadResult, dict):
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
        if not isinstance(other, EntityTypeLoadResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
