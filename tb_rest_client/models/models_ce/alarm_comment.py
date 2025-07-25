# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.1.0
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

class AlarmComment(object):
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
        'alarm_id': 'AlarmId',
        'user_id': 'UserId',
        'type': 'str',
        'comment': 'JsonNode',
        'id': 'AlarmCommentId',
        'created_time': 'int',
        'name': 'str'
    }

    attribute_map = {
        'alarm_id': 'alarmId',
        'user_id': 'userId',
        'type': 'type',
        'comment': 'comment',
        'id': 'id',
        'created_time': 'createdTime',
        'name': 'name'
    }

    def __init__(self, alarm_id=None, user_id=None, type=None, comment=None, id=None, created_time=None, name=None):  # noqa: E501
        """AlarmComment - a model defined in Swagger"""  # noqa: E501
        self._alarm_id = None
        self._user_id = None
        self._type = None
        self._comment = None
        self._id = None
        self._created_time = None
        self._name = None
        self.discriminator = None
        if alarm_id is not None:
            self.alarm_id = alarm_id
        if user_id is not None:
            self.user_id = user_id
        if type is not None:
            self.type = type
        if comment is not None:
            self.comment = comment
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if name is not None:
            self.name = name

    @property
    def alarm_id(self):
        """Gets the alarm_id of this AlarmComment.  # noqa: E501


        :return: The alarm_id of this AlarmComment.  # noqa: E501
        :rtype: AlarmId
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this AlarmComment.


        :param alarm_id: The alarm_id of this AlarmComment.  # noqa: E501
        :type: AlarmId
        """

        self._alarm_id = alarm_id

    @property
    def user_id(self):
        """Gets the user_id of this AlarmComment.  # noqa: E501


        :return: The user_id of this AlarmComment.  # noqa: E501
        :rtype: UserId
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AlarmComment.


        :param user_id: The user_id of this AlarmComment.  # noqa: E501
        :type: UserId
        """

        self._user_id = user_id

    @property
    def type(self):
        """Gets the type of this AlarmComment.  # noqa: E501

        Defines origination of comment. System type means comment was created by TB. OTHER type means comment was created by user.  # noqa: E501

        :return: The type of this AlarmComment.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AlarmComment.

        Defines origination of comment. System type means comment was created by TB. OTHER type means comment was created by user.  # noqa: E501

        :param type: The type of this AlarmComment.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYSTEM", "OTHER"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def comment(self):
        """Gets the comment of this AlarmComment.  # noqa: E501


        :return: The comment of this AlarmComment.  # noqa: E501
        :rtype: JsonNode
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this AlarmComment.


        :param comment: The comment of this AlarmComment.  # noqa: E501
        :type: JsonNode
        """

        self._comment = comment

    @property
    def id(self):
        """Gets the id of this AlarmComment.  # noqa: E501


        :return: The id of this AlarmComment.  # noqa: E501
        :rtype: AlarmCommentId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AlarmComment.


        :param id: The id of this AlarmComment.  # noqa: E501
        :type: AlarmCommentId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this AlarmComment.  # noqa: E501

        Timestamp of the alarm comment creation, in milliseconds  # noqa: E501

        :return: The created_time of this AlarmComment.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this AlarmComment.

        Timestamp of the alarm comment creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this AlarmComment.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def name(self):
        """Gets the name of this AlarmComment.  # noqa: E501

        representing comment text  # noqa: E501

        :return: The name of this AlarmComment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AlarmComment.

        representing comment text  # noqa: E501

        :param name: The name of this AlarmComment.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(AlarmComment, dict):
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
        if not isinstance(other, AlarmComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
