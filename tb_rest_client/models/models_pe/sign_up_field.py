# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.9.0PE
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

class SignUpField(object):
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
        'id': 'str',
        'label': 'str',
        'required': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'label': 'label',
        'required': 'required'
    }

    def __init__(self, id=None, label=None, required=None):  # noqa: E501
        """SignUpField - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._label = None
        self._required = None
        self.discriminator = None
        self.id = id
        self.label = label
        if required is not None:
            self.required = required

    @property
    def id(self):
        """Gets the id of this SignUpField.  # noqa: E501

        Signup field id  # noqa: E501

        :return: The id of this SignUpField.  # noqa: E501
        :rtype: object
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SignUpField.

        Signup field id  # noqa: E501

        :param id: The id of this SignUpField.  # noqa: E501
        :type: object
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def label(self):
        """Gets the label of this SignUpField.  # noqa: E501

        Signup field label  # noqa: E501

        :return: The label of this SignUpField.  # noqa: E501
        :rtype: object
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this SignUpField.

        Signup field label  # noqa: E501

        :param label: The label of this SignUpField.  # noqa: E501
        :type: object
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def required(self):
        """Gets the required of this SignUpField.  # noqa: E501

        Indicates if field is required  # noqa: E501

        :return: The required of this SignUpField.  # noqa: E501
        :rtype: object
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this SignUpField.

        Indicates if field is required  # noqa: E501

        :param required: The required of this SignUpField.  # noqa: E501
        :type: object
        """

        self._required = required

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
        if issubclass(SignUpField, dict):
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
        if not isinstance(other, SignUpField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other