# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.7.0
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
from tb_rest_client.models.models_ce.event_filter import EventFilter  # noqa: F401,E501

class RuleNodeDebugEventFilter(EventFilter):
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
        'server': 'str',
        'is_error': 'bool',
        'error_str': 'str',
        'msg_direction_type': 'str',
        'entity_id': 'str',
        'entity_type': 'str',
        'msg_id': 'str',
        'msg_type': 'str',
        'relation_type': 'str',
        'data_search': 'str',
        'metadata_search': 'str',
        'error': 'bool'
    }
    if hasattr(EventFilter, "swagger_types"):
        swagger_types.update(EventFilter.swagger_types)

    attribute_map = {
        'server': 'server',
        'is_error': 'isError',
        'error_str': 'errorStr',
        'msg_direction_type': 'msgDirectionType',
        'entity_id': 'entityId',
        'entity_type': 'entityType',
        'msg_id': 'msgId',
        'msg_type': 'msgType',
        'relation_type': 'relationType',
        'data_search': 'dataSearch',
        'metadata_search': 'metadataSearch',
        'error': 'error'
    }
    if hasattr(EventFilter, "attribute_map"):
        attribute_map.update(EventFilter.attribute_map)

    def __init__(self, server=None, is_error=None, error_str=None, msg_direction_type=None, entity_id=None, entity_type=None, msg_id=None, msg_type=None, relation_type=None, data_search=None, metadata_search=None, error=None, *args, **kwargs):  # noqa: E501
        """RuleNodeDebugEventFilter - a model defined in Swagger"""  # noqa: E501
        self._server = None
        self._is_error = None
        self._error_str = None
        self._msg_direction_type = None
        self._entity_id = None
        self._entity_type = None
        self._msg_id = None
        self._msg_type = None
        self._relation_type = None
        self._data_search = None
        self._metadata_search = None
        self._error = None
        self.discriminator = None
        if server is not None:
            self.server = server
        if is_error is not None:
            self.is_error = is_error
        if error_str is not None:
            self.error_str = error_str
        if msg_direction_type is not None:
            self.msg_direction_type = msg_direction_type
        if entity_id is not None:
            self.entity_id = entity_id
        if entity_type is not None:
            self.entity_type = entity_type
        if msg_id is not None:
            self.msg_id = msg_id
        if msg_type is not None:
            self.msg_type = msg_type
        if relation_type is not None:
            self.relation_type = relation_type
        if data_search is not None:
            self.data_search = data_search
        if metadata_search is not None:
            self.metadata_search = metadata_search
        if error is not None:
            self.error = error
        EventFilter.__init__(self, *args, **kwargs)

    @property
    def server(self):
        """Gets the server of this RuleNodeDebugEventFilter.  # noqa: E501

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :return: The server of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this RuleNodeDebugEventFilter.

        String value representing the server name, identifier or ip address where the platform is running  # noqa: E501

        :param server: The server of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def is_error(self):
        """Gets the is_error of this RuleNodeDebugEventFilter.  # noqa: E501


        :return: The is_error of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._is_error

    @is_error.setter
    def is_error(self, is_error):
        """Sets the is_error of this RuleNodeDebugEventFilter.


        :param is_error: The is_error of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: bool
        """

        self._is_error = is_error

    @property
    def error_str(self):
        """Gets the error_str of this RuleNodeDebugEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :return: The error_str of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._error_str

    @error_str.setter
    def error_str(self, error_str):
        """Sets the error_str of this RuleNodeDebugEventFilter.

        The case insensitive 'contains' filter based on error message  # noqa: E501

        :param error_str: The error_str of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: str
        """

        self._error_str = error_str

    @property
    def msg_direction_type(self):
        """Gets the msg_direction_type of this RuleNodeDebugEventFilter.  # noqa: E501

        String value representing msg direction type (incoming to entity or outcoming from entity)  # noqa: E501

        :return: The msg_direction_type of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._msg_direction_type

    @msg_direction_type.setter
    def msg_direction_type(self, msg_direction_type):
        """Sets the msg_direction_type of this RuleNodeDebugEventFilter.

        String value representing msg direction type (incoming to entity or outcoming from entity)  # noqa: E501

        :param msg_direction_type: The msg_direction_type of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["IN", "OUT"]  # noqa: E501
        if msg_direction_type not in allowed_values:
            raise ValueError(
                "Invalid value for `msg_direction_type` ({0}), must be one of {1}"  # noqa: E501
                .format(msg_direction_type, allowed_values)
            )

        self._msg_direction_type = msg_direction_type

    @property
    def entity_id(self):
        """Gets the entity_id of this RuleNodeDebugEventFilter.  # noqa: E501

        String value representing the entity id in the event body (originator of the message)  # noqa: E501

        :return: The entity_id of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this RuleNodeDebugEventFilter.

        String value representing the entity id in the event body (originator of the message)  # noqa: E501

        :param entity_id: The entity_id of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def entity_type(self):
        """Gets the entity_type of this RuleNodeDebugEventFilter.  # noqa: E501

        String value representing the entity type  # noqa: E501

        :return: The entity_type of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this RuleNodeDebugEventFilter.

        String value representing the entity type  # noqa: E501

        :param entity_type: The entity_type of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEVICE"]  # noqa: E501
        if entity_type not in allowed_values:
            raise ValueError(
                "Invalid value for `entity_type` ({0}), must be one of {1}"  # noqa: E501
                .format(entity_type, allowed_values)
            )

        self._entity_type = entity_type

    @property
    def msg_id(self):
        """Gets the msg_id of this RuleNodeDebugEventFilter.  # noqa: E501

        String value representing the message id in the rule engine  # noqa: E501

        :return: The msg_id of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._msg_id

    @msg_id.setter
    def msg_id(self, msg_id):
        """Sets the msg_id of this RuleNodeDebugEventFilter.

        String value representing the message id in the rule engine  # noqa: E501

        :param msg_id: The msg_id of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: str
        """

        self._msg_id = msg_id

    @property
    def msg_type(self):
        """Gets the msg_type of this RuleNodeDebugEventFilter.  # noqa: E501

        String value representing the message type  # noqa: E501

        :return: The msg_type of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._msg_type

    @msg_type.setter
    def msg_type(self, msg_type):
        """Sets the msg_type of this RuleNodeDebugEventFilter.

        String value representing the message type  # noqa: E501

        :param msg_type: The msg_type of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: str
        """

        self._msg_type = msg_type

    @property
    def relation_type(self):
        """Gets the relation_type of this RuleNodeDebugEventFilter.  # noqa: E501

        String value representing the type of message routing  # noqa: E501

        :return: The relation_type of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._relation_type

    @relation_type.setter
    def relation_type(self, relation_type):
        """Sets the relation_type of this RuleNodeDebugEventFilter.

        String value representing the type of message routing  # noqa: E501

        :param relation_type: The relation_type of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: str
        """

        self._relation_type = relation_type

    @property
    def data_search(self):
        """Gets the data_search of this RuleNodeDebugEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on data (key and value) for the message.  # noqa: E501

        :return: The data_search of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._data_search

    @data_search.setter
    def data_search(self, data_search):
        """Sets the data_search of this RuleNodeDebugEventFilter.

        The case insensitive 'contains' filter based on data (key and value) for the message.  # noqa: E501

        :param data_search: The data_search of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: str
        """

        self._data_search = data_search

    @property
    def metadata_search(self):
        """Gets the metadata_search of this RuleNodeDebugEventFilter.  # noqa: E501

        The case insensitive 'contains' filter based on metadata (key and value) for the message.  # noqa: E501

        :return: The metadata_search of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: str
        """
        return self._metadata_search

    @metadata_search.setter
    def metadata_search(self, metadata_search):
        """Sets the metadata_search of this RuleNodeDebugEventFilter.

        The case insensitive 'contains' filter based on metadata (key and value) for the message.  # noqa: E501

        :param metadata_search: The metadata_search of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: str
        """

        self._metadata_search = metadata_search

    @property
    def error(self):
        """Gets the error of this RuleNodeDebugEventFilter.  # noqa: E501


        :return: The error of this RuleNodeDebugEventFilter.  # noqa: E501
        :rtype: bool
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RuleNodeDebugEventFilter.


        :param error: The error of this RuleNodeDebugEventFilter.  # noqa: E501
        :type: bool
        """

        self._error = error

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
        if issubclass(RuleNodeDebugEventFilter, dict):
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
        if not isinstance(other, RuleNodeDebugEventFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
