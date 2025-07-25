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

class ProcessingStrategy(object):
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
        'type': 'str',
        'retries': 'int',
        'failure_percentage': 'float',
        'pause_between_retries': 'int',
        'max_pause_between_retries': 'int'
    }

    attribute_map = {
        'type': 'type',
        'retries': 'retries',
        'failure_percentage': 'failurePercentage',
        'pause_between_retries': 'pauseBetweenRetries',
        'max_pause_between_retries': 'maxPauseBetweenRetries'
    }

    def __init__(self, type=None, retries=None, failure_percentage=None, pause_between_retries=None, max_pause_between_retries=None):  # noqa: E501
        """ProcessingStrategy - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._retries = None
        self._failure_percentage = None
        self._pause_between_retries = None
        self._max_pause_between_retries = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if retries is not None:
            self.retries = retries
        if failure_percentage is not None:
            self.failure_percentage = failure_percentage
        if pause_between_retries is not None:
            self.pause_between_retries = pause_between_retries
        if max_pause_between_retries is not None:
            self.max_pause_between_retries = max_pause_between_retries

    @property
    def type(self):
        """Gets the type of this ProcessingStrategy.  # noqa: E501


        :return: The type of this ProcessingStrategy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProcessingStrategy.


        :param type: The type of this ProcessingStrategy.  # noqa: E501
        :type: str
        """
        allowed_values = ["SKIP_ALL_FAILURES", "SKIP_ALL_FAILURES_AND_TIMED_OUT", "RETRY_ALL", "RETRY_FAILED", "RETRY_TIMED_OUT", "RETRY_FAILED_AND_TIMED_OUT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def retries(self):
        """Gets the retries of this ProcessingStrategy.  # noqa: E501


        :return: The retries of this ProcessingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this ProcessingStrategy.


        :param retries: The retries of this ProcessingStrategy.  # noqa: E501
        :type: int
        """

        self._retries = retries

    @property
    def failure_percentage(self):
        """Gets the failure_percentage of this ProcessingStrategy.  # noqa: E501


        :return: The failure_percentage of this ProcessingStrategy.  # noqa: E501
        :rtype: float
        """
        return self._failure_percentage

    @failure_percentage.setter
    def failure_percentage(self, failure_percentage):
        """Sets the failure_percentage of this ProcessingStrategy.


        :param failure_percentage: The failure_percentage of this ProcessingStrategy.  # noqa: E501
        :type: float
        """

        self._failure_percentage = failure_percentage

    @property
    def pause_between_retries(self):
        """Gets the pause_between_retries of this ProcessingStrategy.  # noqa: E501


        :return: The pause_between_retries of this ProcessingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._pause_between_retries

    @pause_between_retries.setter
    def pause_between_retries(self, pause_between_retries):
        """Sets the pause_between_retries of this ProcessingStrategy.


        :param pause_between_retries: The pause_between_retries of this ProcessingStrategy.  # noqa: E501
        :type: int
        """

        self._pause_between_retries = pause_between_retries

    @property
    def max_pause_between_retries(self):
        """Gets the max_pause_between_retries of this ProcessingStrategy.  # noqa: E501


        :return: The max_pause_between_retries of this ProcessingStrategy.  # noqa: E501
        :rtype: int
        """
        return self._max_pause_between_retries

    @max_pause_between_retries.setter
    def max_pause_between_retries(self, max_pause_between_retries):
        """Sets the max_pause_between_retries of this ProcessingStrategy.


        :param max_pause_between_retries: The max_pause_between_retries of this ProcessingStrategy.  # noqa: E501
        :type: int
        """

        self._max_pause_between_retries = max_pause_between_retries

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
        if issubclass(ProcessingStrategy, dict):
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
        if not isinstance(other, ProcessingStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
