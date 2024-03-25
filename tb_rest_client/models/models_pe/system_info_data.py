# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.3PE
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

class SystemInfoData(object):
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
        'service_id': 'str',
        'service_type': 'str',
        'cpu_usage': 'int',
        'cpu_count': 'int',
        'memory_usage': 'int',
        'total_memory': 'int',
        'disc_usage': 'int',
        'total_disc_space': 'int'
    }

    attribute_map = {
        'service_id': 'serviceId',
        'service_type': 'serviceType',
        'cpu_usage': 'cpuUsage',
        'cpu_count': 'cpuCount',
        'memory_usage': 'memoryUsage',
        'total_memory': 'totalMemory',
        'disc_usage': 'discUsage',
        'total_disc_space': 'totalDiscSpace'
    }

    def __init__(self, service_id=None, service_type=None, cpu_usage=None, cpu_count=None, memory_usage=None, total_memory=None, disc_usage=None, total_disc_space=None):  # noqa: E501
        """SystemInfoData - a model defined in Swagger"""  # noqa: E501
        self._service_id = None
        self._service_type = None
        self._cpu_usage = None
        self._cpu_count = None
        self._memory_usage = None
        self._total_memory = None
        self._disc_usage = None
        self._total_disc_space = None
        self.discriminator = None
        if service_id is not None:
            self.service_id = service_id
        if service_type is not None:
            self.service_type = service_type
        if cpu_usage is not None:
            self.cpu_usage = cpu_usage
        if cpu_count is not None:
            self.cpu_count = cpu_count
        if memory_usage is not None:
            self.memory_usage = memory_usage
        if total_memory is not None:
            self.total_memory = total_memory
        if disc_usage is not None:
            self.disc_usage = disc_usage
        if total_disc_space is not None:
            self.total_disc_space = total_disc_space

    @property
    def service_id(self):
        """Gets the service_id of this SystemInfoData.  # noqa: E501

        Service Id.  # noqa: E501

        :return: The service_id of this SystemInfoData.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this SystemInfoData.

        Service Id.  # noqa: E501

        :param service_id: The service_id of this SystemInfoData.  # noqa: E501
        :type: str
        """

        self._service_id = service_id

    @property
    def service_type(self):
        """Gets the service_type of this SystemInfoData.  # noqa: E501

        Service type.  # noqa: E501

        :return: The service_type of this SystemInfoData.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this SystemInfoData.

        Service type.  # noqa: E501

        :param service_type: The service_type of this SystemInfoData.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

    @property
    def cpu_usage(self):
        """Gets the cpu_usage of this SystemInfoData.  # noqa: E501

        CPU usage, in percent.  # noqa: E501

        :return: The cpu_usage of this SystemInfoData.  # noqa: E501
        :rtype: int
        """
        return self._cpu_usage

    @cpu_usage.setter
    def cpu_usage(self, cpu_usage):
        """Sets the cpu_usage of this SystemInfoData.

        CPU usage, in percent.  # noqa: E501

        :param cpu_usage: The cpu_usage of this SystemInfoData.  # noqa: E501
        :type: int
        """

        self._cpu_usage = cpu_usage

    @property
    def cpu_count(self):
        """Gets the cpu_count of this SystemInfoData.  # noqa: E501

        Total CPU usage.  # noqa: E501

        :return: The cpu_count of this SystemInfoData.  # noqa: E501
        :rtype: int
        """
        return self._cpu_count

    @cpu_count.setter
    def cpu_count(self, cpu_count):
        """Sets the cpu_count of this SystemInfoData.

        Total CPU usage.  # noqa: E501

        :param cpu_count: The cpu_count of this SystemInfoData.  # noqa: E501
        :type: int
        """

        self._cpu_count = cpu_count

    @property
    def memory_usage(self):
        """Gets the memory_usage of this SystemInfoData.  # noqa: E501

        Memory usage, in percent.  # noqa: E501

        :return: The memory_usage of this SystemInfoData.  # noqa: E501
        :rtype: int
        """
        return self._memory_usage

    @memory_usage.setter
    def memory_usage(self, memory_usage):
        """Sets the memory_usage of this SystemInfoData.

        Memory usage, in percent.  # noqa: E501

        :param memory_usage: The memory_usage of this SystemInfoData.  # noqa: E501
        :type: int
        """

        self._memory_usage = memory_usage

    @property
    def total_memory(self):
        """Gets the total_memory of this SystemInfoData.  # noqa: E501

        Total memory in bytes.  # noqa: E501

        :return: The total_memory of this SystemInfoData.  # noqa: E501
        :rtype: int
        """
        return self._total_memory

    @total_memory.setter
    def total_memory(self, total_memory):
        """Sets the total_memory of this SystemInfoData.

        Total memory in bytes.  # noqa: E501

        :param total_memory: The total_memory of this SystemInfoData.  # noqa: E501
        :type: int
        """

        self._total_memory = total_memory

    @property
    def disc_usage(self):
        """Gets the disc_usage of this SystemInfoData.  # noqa: E501

        Disk usage, in percent.  # noqa: E501

        :return: The disc_usage of this SystemInfoData.  # noqa: E501
        :rtype: int
        """
        return self._disc_usage

    @disc_usage.setter
    def disc_usage(self, disc_usage):
        """Sets the disc_usage of this SystemInfoData.

        Disk usage, in percent.  # noqa: E501

        :param disc_usage: The disc_usage of this SystemInfoData.  # noqa: E501
        :type: int
        """

        self._disc_usage = disc_usage

    @property
    def total_disc_space(self):
        """Gets the total_disc_space of this SystemInfoData.  # noqa: E501

        Total disc space in bytes.  # noqa: E501

        :return: The total_disc_space of this SystemInfoData.  # noqa: E501
        :rtype: int
        """
        return self._total_disc_space

    @total_disc_space.setter
    def total_disc_space(self, total_disc_space):
        """Sets the total_disc_space of this SystemInfoData.

        Total disc space in bytes.  # noqa: E501

        :param total_disc_space: The total_disc_space of this SystemInfoData.  # noqa: E501
        :type: int
        """

        self._total_disc_space = total_disc_space

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
        if issubclass(SystemInfoData, dict):
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
        if not isinstance(other, SystemInfoData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
