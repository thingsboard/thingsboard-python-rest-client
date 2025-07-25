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
from tb_rest_client.models.models_pe.users_filter import UsersFilter  # noqa: F401,E501

class UserListFilter(UsersFilter):
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
        'users_ids': 'list[str]'
    }
    if hasattr(UsersFilter, "swagger_types"):
        swagger_types.update(UsersFilter.swagger_types)

    attribute_map = {
        'users_ids': 'usersIds'
    }
    if hasattr(UsersFilter, "attribute_map"):
        attribute_map.update(UsersFilter.attribute_map)

    def __init__(self, users_ids=None, *args, **kwargs):  # noqa: E501
        """UserListFilter - a model defined in Swagger"""  # noqa: E501
        self._users_ids = None
        self.discriminator = None
        self.users_ids = users_ids
        UsersFilter.__init__(self, *args, **kwargs)

    @property
    def users_ids(self):
        """Gets the users_ids of this UserListFilter.  # noqa: E501


        :return: The users_ids of this UserListFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._users_ids

    @users_ids.setter
    def users_ids(self, users_ids):
        """Sets the users_ids of this UserListFilter.


        :param users_ids: The users_ids of this UserListFilter.  # noqa: E501
        :type: list[str]
        """
        if users_ids is None:
            raise ValueError("Invalid value for `users_ids`, must not be `None`")  # noqa: E501

        self._users_ids = users_ids

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
        if issubclass(UserListFilter, dict):
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
        if not isinstance(other, UserListFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
