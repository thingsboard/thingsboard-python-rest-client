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

class ShareGroupRequest(object):
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
        'owner_id': 'EntityId',
        'all_user_group': 'bool',
        'user_group_id': 'EntityGroupId',
        'read_else_write': 'bool',
        'role_ids': 'list[RoleId]'
    }

    attribute_map = {
        'owner_id': 'ownerId',
        'all_user_group': 'allUserGroup',
        'user_group_id': 'userGroupId',
        'read_else_write': 'readElseWrite',
        'role_ids': 'roleIds'
    }

    def __init__(self, owner_id=None, all_user_group=None, user_group_id=None, read_else_write=None, role_ids=None):  # noqa: E501
        """ShareGroupRequest - a model defined in Swagger"""  # noqa: E501
        self._owner_id = None
        self._all_user_group = None
        self._user_group_id = None
        self._read_else_write = None
        self._role_ids = None
        self.discriminator = None
        if owner_id is not None:
            self.owner_id = owner_id
        self.all_user_group = all_user_group
        if user_group_id is not None:
            self.user_group_id = user_group_id
        if read_else_write is not None:
            self.read_else_write = read_else_write
        if role_ids is not None:
            self.role_ids = role_ids

    @property
    def owner_id(self):
        """Gets the owner_id of this ShareGroupRequest.  # noqa: E501


        :return: The owner_id of this ShareGroupRequest.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ShareGroupRequest.


        :param owner_id: The owner_id of this ShareGroupRequest.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

    @property
    def all_user_group(self):
        """Gets the all_user_group of this ShareGroupRequest.  # noqa: E501

        Indicate that the group should be shared with user group 'All' that belongs to Tenant or Customer (see 'ownerId' property description).  # noqa: E501

        :return: The all_user_group of this ShareGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._all_user_group

    @all_user_group.setter
    def all_user_group(self, all_user_group):
        """Sets the all_user_group of this ShareGroupRequest.

        Indicate that the group should be shared with user group 'All' that belongs to Tenant or Customer (see 'ownerId' property description).  # noqa: E501

        :param all_user_group: The all_user_group of this ShareGroupRequest.  # noqa: E501
        :type: bool
        """
        if all_user_group is None:
            raise ValueError("Invalid value for `all_user_group`, must not be `None`")  # noqa: E501

        self._all_user_group = all_user_group

    @property
    def user_group_id(self):
        """Gets the user_group_id of this ShareGroupRequest.  # noqa: E501


        :return: The user_group_id of this ShareGroupRequest.  # noqa: E501
        :rtype: EntityGroupId
        """
        return self._user_group_id

    @user_group_id.setter
    def user_group_id(self, user_group_id):
        """Sets the user_group_id of this ShareGroupRequest.


        :param user_group_id: The user_group_id of this ShareGroupRequest.  # noqa: E501
        :type: EntityGroupId
        """

        self._user_group_id = user_group_id

    @property
    def read_else_write(self):
        """Gets the read_else_write of this ShareGroupRequest.  # noqa: E501

        Used if 'roleIds' property is not present. if the value is 'true', creates role with read-only permissions. If the value is 'false', creates role with write permissions.  # noqa: E501

        :return: The read_else_write of this ShareGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._read_else_write

    @read_else_write.setter
    def read_else_write(self, read_else_write):
        """Sets the read_else_write of this ShareGroupRequest.

        Used if 'roleIds' property is not present. if the value is 'true', creates role with read-only permissions. If the value is 'false', creates role with write permissions.  # noqa: E501

        :param read_else_write: The read_else_write of this ShareGroupRequest.  # noqa: E501
        :type: bool
        """

        self._read_else_write = read_else_write

    @property
    def role_ids(self):
        """Gets the role_ids of this ShareGroupRequest.  # noqa: E501

        List of group role Ids that should be used to share the entity group with the user group. If not set, the platform will create new role (see 'readElseWrite' property description)  # noqa: E501

        :return: The role_ids of this ShareGroupRequest.  # noqa: E501
        :rtype: list[RoleId]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """Sets the role_ids of this ShareGroupRequest.

        List of group role Ids that should be used to share the entity group with the user group. If not set, the platform will create new role (see 'readElseWrite' property description)  # noqa: E501

        :param role_ids: The role_ids of this ShareGroupRequest.  # noqa: E501
        :type: list[RoleId]
        """

        self._role_ids = role_ids

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
        if issubclass(ShareGroupRequest, dict):
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
        if not isinstance(other, ShareGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
