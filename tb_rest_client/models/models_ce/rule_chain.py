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

class RuleChain(object):
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
        'additional_info': 'JsonNode',
        'id': 'RuleChainId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'name': 'str',
        'type': 'str',
        'first_rule_node_id': 'RuleNodeId',
        'root': 'bool',
        'debug_mode': 'bool',
        'configuration': 'JsonNode'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'name': 'name',
        'type': 'type',
        'first_rule_node_id': 'firstRuleNodeId',
        'root': 'root',
        'debug_mode': 'debugMode',
        'configuration': 'configuration'
    }

    def __init__(self, additional_info=None, id=None, created_time=None, tenant_id=None, name=None, type=None, first_rule_node_id=None, root=None, debug_mode=None, configuration=None):  # noqa: E501
        """RuleChain - a model defined in Swagger"""  # noqa: E501
        self._additional_info = None
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._name = None
        self._type = None
        self._first_rule_node_id = None
        self._root = None
        self._debug_mode = None
        self._configuration = None
        self.discriminator = None
        if additional_info is not None:
            self.additional_info = additional_info
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        self.tenant_id = tenant_id
        self.name = name
        if type is not None:
            self.type = type
        if first_rule_node_id is not None:
            self.first_rule_node_id = first_rule_node_id
        if root is not None:
            self.root = root
        if debug_mode is not None:
            self.debug_mode = debug_mode
        if configuration is not None:
            self.configuration = configuration

    @property
    def additional_info(self):
        """Gets the additional_info of this RuleChain.  # noqa: E501


        :return: The additional_info of this RuleChain.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this RuleChain.


        :param additional_info: The additional_info of this RuleChain.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def id(self):
        """Gets the id of this RuleChain.  # noqa: E501


        :return: The id of this RuleChain.  # noqa: E501
        :rtype: RuleChainId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RuleChain.


        :param id: The id of this RuleChain.  # noqa: E501
        :type: RuleChainId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this RuleChain.  # noqa: E501

        Timestamp of the rule chain creation, in milliseconds  # noqa: E501

        :return: The created_time of this RuleChain.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this RuleChain.

        Timestamp of the rule chain creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this RuleChain.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this RuleChain.  # noqa: E501


        :return: The tenant_id of this RuleChain.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this RuleChain.


        :param tenant_id: The tenant_id of this RuleChain.  # noqa: E501
        :type: TenantId
        """
        if tenant_id is None:
            raise ValueError("Invalid value for `tenant_id`, must not be `None`")  # noqa: E501

        self._tenant_id = tenant_id

    @property
    def name(self):
        """Gets the name of this RuleChain.  # noqa: E501

        Rule Chain name  # noqa: E501

        :return: The name of this RuleChain.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RuleChain.

        Rule Chain name  # noqa: E501

        :param name: The name of this RuleChain.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this RuleChain.  # noqa: E501

        Rule Chain type. 'EDGE' rule chains are processing messages on the edge devices only.  # noqa: E501

        :return: The type of this RuleChain.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RuleChain.

        Rule Chain type. 'EDGE' rule chains are processing messages on the edge devices only.  # noqa: E501

        :param type: The type of this RuleChain.  # noqa: E501
        :type: str
        """
        allowed_values = ["CORE", "EDGE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def first_rule_node_id(self):
        """Gets the first_rule_node_id of this RuleChain.  # noqa: E501


        :return: The first_rule_node_id of this RuleChain.  # noqa: E501
        :rtype: RuleNodeId
        """
        return self._first_rule_node_id

    @first_rule_node_id.setter
    def first_rule_node_id(self, first_rule_node_id):
        """Sets the first_rule_node_id of this RuleChain.


        :param first_rule_node_id: The first_rule_node_id of this RuleChain.  # noqa: E501
        :type: RuleNodeId
        """

        self._first_rule_node_id = first_rule_node_id

    @property
    def root(self):
        """Gets the root of this RuleChain.  # noqa: E501

        Indicates root rule chain. The root rule chain process messages from all devices and entities by default. User may configure default rule chain per device profile.  # noqa: E501

        :return: The root of this RuleChain.  # noqa: E501
        :rtype: bool
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this RuleChain.

        Indicates root rule chain. The root rule chain process messages from all devices and entities by default. User may configure default rule chain per device profile.  # noqa: E501

        :param root: The root of this RuleChain.  # noqa: E501
        :type: bool
        """

        self._root = root

    @property
    def debug_mode(self):
        """Gets the debug_mode of this RuleChain.  # noqa: E501

        Reserved for future usage.  # noqa: E501

        :return: The debug_mode of this RuleChain.  # noqa: E501
        :rtype: bool
        """
        return self._debug_mode

    @debug_mode.setter
    def debug_mode(self, debug_mode):
        """Sets the debug_mode of this RuleChain.

        Reserved for future usage.  # noqa: E501

        :param debug_mode: The debug_mode of this RuleChain.  # noqa: E501
        :type: bool
        """

        self._debug_mode = debug_mode

    @property
    def configuration(self):
        """Gets the configuration of this RuleChain.  # noqa: E501


        :return: The configuration of this RuleChain.  # noqa: E501
        :rtype: JsonNode
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this RuleChain.


        :param configuration: The configuration of this RuleChain.  # noqa: E501
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
        if issubclass(RuleChain, dict):
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
        if not isinstance(other, RuleChain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
