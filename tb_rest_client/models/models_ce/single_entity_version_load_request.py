# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.3
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
from tb_rest_client.models.models_ce.version_load_request import VersionLoadRequest  # noqa: F401,E501

class SingleEntityVersionLoadRequest(VersionLoadRequest):
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
        'config': 'VersionLoadConfig',
        'external_entity_id': 'EntityId',
        'type': 'str',
        'version_id': 'str'
    }
    if hasattr(VersionLoadRequest, "swagger_types"):
        swagger_types.update(VersionLoadRequest.swagger_types)

    attribute_map = {
        'config': 'config',
        'external_entity_id': 'externalEntityId',
        'type': 'type',
        'version_id': 'versionId'
    }
    if hasattr(VersionLoadRequest, "attribute_map"):
        attribute_map.update(VersionLoadRequest.attribute_map)

    def __init__(self, config=None, external_entity_id=None, type=None, version_id=None, *args, **kwargs):  # noqa: E501
        """SingleEntityVersionLoadRequest - a model defined in Swagger"""  # noqa: E501
        self._config = None
        self._external_entity_id = None
        self._type = None
        self._version_id = None
        self.discriminator = None
        if config is not None:
            self.config = config
        if external_entity_id is not None:
            self.external_entity_id = external_entity_id
        if type is not None:
            self.type = type
        if version_id is not None:
            self.version_id = version_id
        VersionLoadRequest.__init__(self, *args, **kwargs)

    @property
    def config(self):
        """Gets the config of this SingleEntityVersionLoadRequest.  # noqa: E501


        :return: The config of this SingleEntityVersionLoadRequest.  # noqa: E501
        :rtype: VersionLoadConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this SingleEntityVersionLoadRequest.


        :param config: The config of this SingleEntityVersionLoadRequest.  # noqa: E501
        :type: VersionLoadConfig
        """

        self._config = config

    @property
    def external_entity_id(self):
        """Gets the external_entity_id of this SingleEntityVersionLoadRequest.  # noqa: E501


        :return: The external_entity_id of this SingleEntityVersionLoadRequest.  # noqa: E501
        :rtype: EntityId
        """
        return self._external_entity_id

    @external_entity_id.setter
    def external_entity_id(self, external_entity_id):
        """Sets the external_entity_id of this SingleEntityVersionLoadRequest.


        :param external_entity_id: The external_entity_id of this SingleEntityVersionLoadRequest.  # noqa: E501
        :type: EntityId
        """

        self._external_entity_id = external_entity_id

    @property
    def type(self):
        """Gets the type of this SingleEntityVersionLoadRequest.  # noqa: E501


        :return: The type of this SingleEntityVersionLoadRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SingleEntityVersionLoadRequest.


        :param type: The type of this SingleEntityVersionLoadRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENTITY_TYPE", "SINGLE_ENTITY"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def version_id(self):
        """Gets the version_id of this SingleEntityVersionLoadRequest.  # noqa: E501


        :return: The version_id of this SingleEntityVersionLoadRequest.  # noqa: E501
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        """Sets the version_id of this SingleEntityVersionLoadRequest.


        :param version_id: The version_id of this SingleEntityVersionLoadRequest.  # noqa: E501
        :type: str
        """

        self._version_id = version_id

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
        if issubclass(SingleEntityVersionLoadRequest, dict):
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
        if not isinstance(other, SingleEntityVersionLoadRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
