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

class RuleNode(object):
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
        'external_id': 'RuleNodeId',
        'id': 'RuleNodeId',
        'created_time': 'int',
        'rule_chain_id': 'RuleChainId',
        'type': 'str',
        'name': 'str',
        'debug_mode': 'bool',
        'singleton_mode': 'bool',
        'additional_info': 'JsonNode',
        'configuration': 'JsonNode'
    }

    attribute_map = {
        'external_id': 'externalId',
        'id': 'id',
        'created_time': 'createdTime',
        'rule_chain_id': 'ruleChainId',
        'type': 'type',
        'name': 'name',
        'debug_mode': 'debugMode',
        'singleton_mode': 'singletonMode',
        'additional_info': 'additionalInfo',
        'configuration': 'configuration'
    }

    def __init__(self, external_id=None, id=None, created_time=None, rule_chain_id=None, type=None, name=None, debug_mode=None, singleton_mode=None, additional_info=None, configuration=None):  # noqa: E501
        """RuleNode - a model defined in Swagger"""  # noqa: E501
        self._external_id = None
        self._id = None
        self._created_time = None
        self._rule_chain_id = None
        self._type = None
        self._name = None
        self._debug_mode = None
        self._singleton_mode = None
        self._additional_info = None
        self._configuration = None
        self.discriminator = None
        if external_id is not None:
            self.external_id = external_id
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if rule_chain_id is not None:
            self.rule_chain_id = rule_chain_id
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if debug_mode is not None:
            self.debug_mode = debug_mode
        if singleton_mode is not None:
            self.singleton_mode = singleton_mode
        if additional_info is not None:
            self.additional_info = additional_info
        if configuration is not None:
            self.configuration = configuration

    @property
    def external_id(self):
        """Gets the external_id of this RuleNode.  # noqa: E501


        :return: The external_id of this RuleNode.  # noqa: E501
        :rtype: RuleNodeId
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this RuleNode.


        :param external_id: The external_id of this RuleNode.  # noqa: E501
        :type: RuleNodeId
        """

        self._external_id = external_id

    @property
    def id(self):
        """Gets the id of this RuleNode.  # noqa: E501


        :return: The id of this RuleNode.  # noqa: E501
        :rtype: RuleNodeId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RuleNode.


        :param id: The id of this RuleNode.  # noqa: E501
        :type: RuleNodeId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this RuleNode.  # noqa: E501

        Timestamp of the rule node creation, in milliseconds  # noqa: E501

        :return: The created_time of this RuleNode.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this RuleNode.

        Timestamp of the rule node creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this RuleNode.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def rule_chain_id(self):
        """Gets the rule_chain_id of this RuleNode.  # noqa: E501


        :return: The rule_chain_id of this RuleNode.  # noqa: E501
        :rtype: RuleChainId
        """
        return self._rule_chain_id

    @rule_chain_id.setter
    def rule_chain_id(self, rule_chain_id):
        """Sets the rule_chain_id of this RuleNode.


        :param rule_chain_id: The rule_chain_id of this RuleNode.  # noqa: E501
        :type: RuleChainId
        """

        self._rule_chain_id = rule_chain_id

    @property
    def type(self):
        """Gets the type of this RuleNode.  # noqa: E501

        Full Java Class Name of the rule node implementation.   # noqa: E501

        :return: The type of this RuleNode.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleNode.

        Full Java Class Name of the rule node implementation.   # noqa: E501

        :param type: The type of this RuleNode.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this RuleNode.  # noqa: E501

        User defined name of the rule node. Used on UI and for logging.   # noqa: E501

        :return: The name of this RuleNode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuleNode.

        User defined name of the rule node. Used on UI and for logging.   # noqa: E501

        :param name: The name of this RuleNode.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def debug_mode(self):
        """Gets the debug_mode of this RuleNode.  # noqa: E501

        Enable/disable debug.   # noqa: E501

        :return: The debug_mode of this RuleNode.  # noqa: E501
        :rtype: bool
        """
        return self._debug_mode

    @debug_mode.setter
    def debug_mode(self, debug_mode):
        """Sets the debug_mode of this RuleNode.

        Enable/disable debug.   # noqa: E501

        :param debug_mode: The debug_mode of this RuleNode.  # noqa: E501
        :type: bool
        """

        self._debug_mode = debug_mode

    @property
    def singleton_mode(self):
        """Gets the singleton_mode of this RuleNode.  # noqa: E501

        Enable/disable singleton mode.   # noqa: E501

        :return: The singleton_mode of this RuleNode.  # noqa: E501
        :rtype: bool
        """
        return self._singleton_mode

    @singleton_mode.setter
    def singleton_mode(self, singleton_mode):
        """Sets the singleton_mode of this RuleNode.

        Enable/disable singleton mode.   # noqa: E501

        :param singleton_mode: The singleton_mode of this RuleNode.  # noqa: E501
        :type: bool
        """

        self._singleton_mode = singleton_mode

    @property
    def additional_info(self):
        """Gets the additional_info of this RuleNode.  # noqa: E501


        :return: The additional_info of this RuleNode.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this RuleNode.


        :param additional_info: The additional_info of this RuleNode.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def configuration(self):
        """Gets the configuration of this RuleNode.  # noqa: E501


        :return: The configuration of this RuleNode.  # noqa: E501
        :rtype: JsonNode
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this RuleNode.


        :param configuration: The configuration of this RuleNode.  # noqa: E501
        :type: JsonNode
        """

        self._configuration = configuration

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
        if issubclass(RuleNode, dict):
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
        if not isinstance(other, RuleNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
