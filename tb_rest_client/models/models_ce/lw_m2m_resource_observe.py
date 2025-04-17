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

class LwM2mResourceObserve(object):
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
        'id': 'int',
        'name': 'str',
        'observe': 'bool',
        'attribute': 'bool',
        'telemetry': 'bool',
        'key_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'observe': 'observe',
        'attribute': 'attribute',
        'telemetry': 'telemetry',
        'key_name': 'keyName'
    }

    def __init__(self, id=None, name=None, observe=None, attribute=None, telemetry=None, key_name=None):  # noqa: E501
        """LwM2mResourceObserve - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._observe = None
        self._attribute = None
        self._telemetry = None
        self._key_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if observe is not None:
            self.observe = observe
        if attribute is not None:
            self.attribute = attribute
        if telemetry is not None:
            self.telemetry = telemetry
        if key_name is not None:
            self.key_name = key_name

    @property
    def id(self):
        """Gets the id of this LwM2mResourceObserve.  # noqa: E501

        LwM2M Resource Observe id.  # noqa: E501

        :return: The id of this LwM2mResourceObserve.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LwM2mResourceObserve.

        LwM2M Resource Observe id.  # noqa: E501

        :param id: The id of this LwM2mResourceObserve.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this LwM2mResourceObserve.  # noqa: E501

        LwM2M Resource Observe name.  # noqa: E501

        :return: The name of this LwM2mResourceObserve.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LwM2mResourceObserve.

        LwM2M Resource Observe name.  # noqa: E501

        :param name: The name of this LwM2mResourceObserve.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def observe(self):
        """Gets the observe of this LwM2mResourceObserve.  # noqa: E501

        LwM2M Resource Observe observe.  # noqa: E501

        :return: The observe of this LwM2mResourceObserve.  # noqa: E501
        :rtype: bool
        """
        return self._observe

    @observe.setter
    def observe(self, observe):
        """Sets the observe of this LwM2mResourceObserve.

        LwM2M Resource Observe observe.  # noqa: E501

        :param observe: The observe of this LwM2mResourceObserve.  # noqa: E501
        :type: bool
        """

        self._observe = observe

    @property
    def attribute(self):
        """Gets the attribute of this LwM2mResourceObserve.  # noqa: E501

        LwM2M Resource Observe attribute.  # noqa: E501

        :return: The attribute of this LwM2mResourceObserve.  # noqa: E501
        :rtype: bool
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        """Sets the attribute of this LwM2mResourceObserve.

        LwM2M Resource Observe attribute.  # noqa: E501

        :param attribute: The attribute of this LwM2mResourceObserve.  # noqa: E501
        :type: bool
        """

        self._attribute = attribute

    @property
    def telemetry(self):
        """Gets the telemetry of this LwM2mResourceObserve.  # noqa: E501

        LwM2M Resource Observe telemetry.  # noqa: E501

        :return: The telemetry of this LwM2mResourceObserve.  # noqa: E501
        :rtype: bool
        """
        return self._telemetry

    @telemetry.setter
    def telemetry(self, telemetry):
        """Sets the telemetry of this LwM2mResourceObserve.

        LwM2M Resource Observe telemetry.  # noqa: E501

        :param telemetry: The telemetry of this LwM2mResourceObserve.  # noqa: E501
        :type: bool
        """

        self._telemetry = telemetry

    @property
    def key_name(self):
        """Gets the key_name of this LwM2mResourceObserve.  # noqa: E501

        LwM2M Resource Observe key name.  # noqa: E501

        :return: The key_name of this LwM2mResourceObserve.  # noqa: E501
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        """Sets the key_name of this LwM2mResourceObserve.

        LwM2M Resource Observe key name.  # noqa: E501

        :param key_name: The key_name of this LwM2mResourceObserve.  # noqa: E501
        :type: str
        """

        self._key_name = key_name

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
        if issubclass(LwM2mResourceObserve, dict):
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
        if not isinstance(other, LwM2mResourceObserve):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
