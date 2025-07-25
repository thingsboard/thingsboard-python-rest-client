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

class RuleChainImportResult(object):
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
        'rule_chain_id': 'RuleChainId',
        'rule_chain_name': 'str',
        'updated': 'bool',
        'error': 'str'
    }

    attribute_map = {
        'rule_chain_id': 'ruleChainId',
        'rule_chain_name': 'ruleChainName',
        'updated': 'updated',
        'error': 'error'
    }

    def __init__(self, rule_chain_id=None, rule_chain_name=None, updated=None, error=None):  # noqa: E501
        """RuleChainImportResult - a model defined in Swagger"""  # noqa: E501
        self._rule_chain_id = None
        self._rule_chain_name = None
        self._updated = None
        self._error = None
        self.discriminator = None
        if rule_chain_id is not None:
            self.rule_chain_id = rule_chain_id
        if rule_chain_name is not None:
            self.rule_chain_name = rule_chain_name
        if updated is not None:
            self.updated = updated
        if error is not None:
            self.error = error

    @property
    def rule_chain_id(self):
        """Gets the rule_chain_id of this RuleChainImportResult.  # noqa: E501


        :return: The rule_chain_id of this RuleChainImportResult.  # noqa: E501
        :rtype: RuleChainId
        """
        return self._rule_chain_id

    @rule_chain_id.setter
    def rule_chain_id(self, rule_chain_id):
        """Sets the rule_chain_id of this RuleChainImportResult.


        :param rule_chain_id: The rule_chain_id of this RuleChainImportResult.  # noqa: E501
        :type: RuleChainId
        """

        self._rule_chain_id = rule_chain_id

    @property
    def rule_chain_name(self):
        """Gets the rule_chain_name of this RuleChainImportResult.  # noqa: E501


        :return: The rule_chain_name of this RuleChainImportResult.  # noqa: E501
        :rtype: str
        """
        return self._rule_chain_name

    @rule_chain_name.setter
    def rule_chain_name(self, rule_chain_name):
        """Sets the rule_chain_name of this RuleChainImportResult.


        :param rule_chain_name: The rule_chain_name of this RuleChainImportResult.  # noqa: E501
        :type: str
        """

        self._rule_chain_name = rule_chain_name

    @property
    def updated(self):
        """Gets the updated of this RuleChainImportResult.  # noqa: E501


        :return: The updated of this RuleChainImportResult.  # noqa: E501
        :rtype: bool
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this RuleChainImportResult.


        :param updated: The updated of this RuleChainImportResult.  # noqa: E501
        :type: bool
        """

        self._updated = updated

    @property
    def error(self):
        """Gets the error of this RuleChainImportResult.  # noqa: E501


        :return: The error of this RuleChainImportResult.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this RuleChainImportResult.


        :param error: The error of this RuleChainImportResult.  # noqa: E501
        :type: str
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
        if issubclass(RuleChainImportResult, dict):
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
        if not isinstance(other, RuleChainImportResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
