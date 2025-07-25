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

class PaletteSettings(object):
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
        'primary_palette': 'Palette',
        'accent_palette': 'Palette'
    }

    attribute_map = {
        'primary_palette': 'primaryPalette',
        'accent_palette': 'accentPalette'
    }

    def __init__(self, primary_palette=None, accent_palette=None):  # noqa: E501
        """PaletteSettings - a model defined in Swagger"""  # noqa: E501
        self._primary_palette = None
        self._accent_palette = None
        self.discriminator = None
        self.primary_palette = primary_palette
        self.accent_palette = accent_palette

    @property
    def primary_palette(self):
        """Gets the primary_palette of this PaletteSettings.  # noqa: E501


        :return: The primary_palette of this PaletteSettings.  # noqa: E501
        :rtype: Palette
        """
        return self._primary_palette

    @primary_palette.setter
    def primary_palette(self, primary_palette):
        """Sets the primary_palette of this PaletteSettings.


        :param primary_palette: The primary_palette of this PaletteSettings.  # noqa: E501
        :type: Palette
        """
        if primary_palette is None:
            raise ValueError("Invalid value for `primary_palette`, must not be `None`")  # noqa: E501

        self._primary_palette = primary_palette

    @property
    def accent_palette(self):
        """Gets the accent_palette of this PaletteSettings.  # noqa: E501


        :return: The accent_palette of this PaletteSettings.  # noqa: E501
        :rtype: Palette
        """
        return self._accent_palette

    @accent_palette.setter
    def accent_palette(self, accent_palette):
        """Sets the accent_palette of this PaletteSettings.


        :param accent_palette: The accent_palette of this PaletteSettings.  # noqa: E501
        :type: Palette
        """
        if accent_palette is None:
            raise ValueError("Invalid value for `accent_palette`, must not be `None`")  # noqa: E501

        self._accent_palette = accent_palette

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
        if issubclass(PaletteSettings, dict):
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
        if not isinstance(other, PaletteSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
