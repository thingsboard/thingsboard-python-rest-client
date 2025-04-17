# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.0.0
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

class SystemInfo(object):
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
        'system_data': 'list[SystemInfoData]',
        'monolith': 'bool'
    }

    attribute_map = {
        'system_data': 'systemData',
        'monolith': 'monolith'
    }

    def __init__(self, system_data=None, monolith=None):  # noqa: E501
        """SystemInfo - a model defined in Swagger"""  # noqa: E501
        self._system_data = None
        self._monolith = None
        self.discriminator = None
        if system_data is not None:
            self.system_data = system_data
        if monolith is not None:
            self.monolith = monolith

    @property
    def system_data(self):
        """Gets the system_data of this SystemInfo.  # noqa: E501

        System data.  # noqa: E501

        :return: The system_data of this SystemInfo.  # noqa: E501
        :rtype: list[SystemInfoData]
        """
        return self._system_data

    @system_data.setter
    def system_data(self, system_data):
        """Sets the system_data of this SystemInfo.

        System data.  # noqa: E501

        :param system_data: The system_data of this SystemInfo.  # noqa: E501
        :type: list[SystemInfoData]
        """

        self._system_data = system_data

    @property
    def monolith(self):
        """Gets the monolith of this SystemInfo.  # noqa: E501


        :return: The monolith of this SystemInfo.  # noqa: E501
        :rtype: bool
        """
        return self._monolith

    @monolith.setter
    def monolith(self, monolith):
        """Sets the monolith of this SystemInfo.


        :param monolith: The monolith of this SystemInfo.  # noqa: E501
        :type: bool
        """

        self._monolith = monolith

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
        if issubclass(SystemInfo, dict):
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
        if not isinstance(other, SystemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
