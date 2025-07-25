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

class NodeConnectionInfo(object):
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
        'from_index': 'int',
        'to_index': 'int',
        'type': 'str'
    }

    attribute_map = {
        'from_index': 'fromIndex',
        'to_index': 'toIndex',
        'type': 'type'
    }

    def __init__(self, from_index=None, to_index=None, type=None):  # noqa: E501
        """NodeConnectionInfo - a model defined in Swagger"""  # noqa: E501
        self._from_index = None
        self._to_index = None
        self._type = None
        self.discriminator = None
        self.from_index = from_index
        self.to_index = to_index
        self.type = type

    @property
    def from_index(self):
        """Gets the from_index of this NodeConnectionInfo.  # noqa: E501

        Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'from' part of the connection.  # noqa: E501

        :return: The from_index of this NodeConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._from_index

    @from_index.setter
    def from_index(self, from_index):
        """Sets the from_index of this NodeConnectionInfo.

        Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'from' part of the connection.  # noqa: E501

        :param from_index: The from_index of this NodeConnectionInfo.  # noqa: E501
        :type: int
        """
        if from_index is None:
            raise ValueError("Invalid value for `from_index`, must not be `None`")  # noqa: E501

        self._from_index = from_index

    @property
    def to_index(self):
        """Gets the to_index of this NodeConnectionInfo.  # noqa: E501

        Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'to' part of the connection.  # noqa: E501

        :return: The to_index of this NodeConnectionInfo.  # noqa: E501
        :rtype: int
        """
        return self._to_index

    @to_index.setter
    def to_index(self, to_index):
        """Sets the to_index of this NodeConnectionInfo.

        Index of rule node in the 'nodes' array of the RuleChainMetaData. Indicates the 'to' part of the connection.  # noqa: E501

        :param to_index: The to_index of this NodeConnectionInfo.  # noqa: E501
        :type: int
        """
        if to_index is None:
            raise ValueError("Invalid value for `to_index`, must not be `None`")  # noqa: E501

        self._to_index = to_index

    @property
    def type(self):
        """Gets the type of this NodeConnectionInfo.  # noqa: E501

        Type of the relation. Typically indicated the result of processing by the 'from' rule node. For example, 'Success' or 'Failure'  # noqa: E501

        :return: The type of this NodeConnectionInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NodeConnectionInfo.

        Type of the relation. Typically indicated the result of processing by the 'from' rule node. For example, 'Success' or 'Failure'  # noqa: E501

        :param type: The type of this NodeConnectionInfo.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

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
        if issubclass(NodeConnectionInfo, dict):
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
        if not isinstance(other, NodeConnectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
