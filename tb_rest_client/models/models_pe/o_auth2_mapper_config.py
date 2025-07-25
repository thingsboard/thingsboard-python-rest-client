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

class OAuth2MapperConfig(object):
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
        'allow_user_creation': 'bool',
        'activate_user': 'bool',
        'type': 'str',
        'basic': 'OAuth2BasicMapperConfig',
        'custom': 'OAuth2CustomMapperConfig'
    }

    attribute_map = {
        'allow_user_creation': 'allowUserCreation',
        'activate_user': 'activateUser',
        'type': 'type',
        'basic': 'basic',
        'custom': 'custom'
    }

    def __init__(self, allow_user_creation=None, activate_user=None, type=None, basic=None, custom=None):  # noqa: E501
        """OAuth2MapperConfig - a model defined in Swagger"""  # noqa: E501
        self._allow_user_creation = None
        self._activate_user = None
        self._type = None
        self._basic = None
        self._custom = None
        self.discriminator = None
        if allow_user_creation is not None:
            self.allow_user_creation = allow_user_creation
        if activate_user is not None:
            self.activate_user = activate_user
        self.type = type
        if basic is not None:
            self.basic = basic
        if custom is not None:
            self.custom = custom

    @property
    def allow_user_creation(self):
        """Gets the allow_user_creation of this OAuth2MapperConfig.  # noqa: E501

        Whether user should be created if not yet present on the platform after successful authentication  # noqa: E501

        :return: The allow_user_creation of this OAuth2MapperConfig.  # noqa: E501
        :rtype: bool
        """
        return self._allow_user_creation

    @allow_user_creation.setter
    def allow_user_creation(self, allow_user_creation):
        """Sets the allow_user_creation of this OAuth2MapperConfig.

        Whether user should be created if not yet present on the platform after successful authentication  # noqa: E501

        :param allow_user_creation: The allow_user_creation of this OAuth2MapperConfig.  # noqa: E501
        :type: bool
        """

        self._allow_user_creation = allow_user_creation

    @property
    def activate_user(self):
        """Gets the activate_user of this OAuth2MapperConfig.  # noqa: E501

        Whether user credentials should be activated when user is created after successful authentication  # noqa: E501

        :return: The activate_user of this OAuth2MapperConfig.  # noqa: E501
        :rtype: bool
        """
        return self._activate_user

    @activate_user.setter
    def activate_user(self, activate_user):
        """Sets the activate_user of this OAuth2MapperConfig.

        Whether user credentials should be activated when user is created after successful authentication  # noqa: E501

        :param activate_user: The activate_user of this OAuth2MapperConfig.  # noqa: E501
        :type: bool
        """

        self._activate_user = activate_user

    @property
    def type(self):
        """Gets the type of this OAuth2MapperConfig.  # noqa: E501

        Type of OAuth2 mapper. Depending on this param, different mapper config fields must be specified  # noqa: E501

        :return: The type of this OAuth2MapperConfig.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OAuth2MapperConfig.

        Type of OAuth2 mapper. Depending on this param, different mapper config fields must be specified  # noqa: E501

        :param type: The type of this OAuth2MapperConfig.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["BASIC", "CUSTOM", "GITHUB", "APPLE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def basic(self):
        """Gets the basic of this OAuth2MapperConfig.  # noqa: E501


        :return: The basic of this OAuth2MapperConfig.  # noqa: E501
        :rtype: OAuth2BasicMapperConfig
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        """Sets the basic of this OAuth2MapperConfig.


        :param basic: The basic of this OAuth2MapperConfig.  # noqa: E501
        :type: OAuth2BasicMapperConfig
        """

        self._basic = basic

    @property
    def custom(self):
        """Gets the custom of this OAuth2MapperConfig.  # noqa: E501


        :return: The custom of this OAuth2MapperConfig.  # noqa: E501
        :rtype: OAuth2CustomMapperConfig
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """Sets the custom of this OAuth2MapperConfig.


        :param custom: The custom of this OAuth2MapperConfig.  # noqa: E501
        :type: OAuth2CustomMapperConfig
        """

        self._custom = custom

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
        if issubclass(OAuth2MapperConfig, dict):
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
        if not isinstance(other, OAuth2MapperConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
