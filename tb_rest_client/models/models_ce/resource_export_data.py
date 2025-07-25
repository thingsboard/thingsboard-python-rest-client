# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.1.0
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

class ResourceExportData(object):
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
        'link': 'str',
        'title': 'str',
        'type': 'str',
        'sub_type': 'str',
        'resource_key': 'str',
        'file_name': 'str',
        'public_resource_key': 'str',
        'is_public': 'bool',
        'media_type': 'str',
        'data': 'object',
        'public': 'bool'
    }

    attribute_map = {
        'link': 'link',
        'title': 'title',
        'type': 'type',
        'sub_type': 'subType',
        'resource_key': 'resourceKey',
        'file_name': 'fileName',
        'public_resource_key': 'publicResourceKey',
        'is_public': 'isPublic',
        'media_type': 'mediaType',
        'data': 'data',
        'public': 'public'
    }

    def __init__(self, link=None, title=None, type=None, sub_type=None, resource_key=None, file_name=None, public_resource_key=None, is_public=None, media_type=None, data=None, public=None):  # noqa: E501
        """ResourceExportData - a model defined in Swagger"""  # noqa: E501
        self._link = None
        self._title = None
        self._type = None
        self._sub_type = None
        self._resource_key = None
        self._file_name = None
        self._public_resource_key = None
        self._is_public = None
        self._media_type = None
        self._data = None
        self._public = None
        self.discriminator = None
        if link is not None:
            self.link = link
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if sub_type is not None:
            self.sub_type = sub_type
        if resource_key is not None:
            self.resource_key = resource_key
        if file_name is not None:
            self.file_name = file_name
        if public_resource_key is not None:
            self.public_resource_key = public_resource_key
        if is_public is not None:
            self.is_public = is_public
        if media_type is not None:
            self.media_type = media_type
        if data is not None:
            self.data = data
        if public is not None:
            self.public = public

    @property
    def link(self):
        """Gets the link of this ResourceExportData.  # noqa: E501


        :return: The link of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ResourceExportData.


        :param link: The link of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._link = link

    @property
    def title(self):
        """Gets the title of this ResourceExportData.  # noqa: E501


        :return: The title of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ResourceExportData.


        :param title: The title of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this ResourceExportData.  # noqa: E501


        :return: The type of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ResourceExportData.


        :param type: The type of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._type = type

    @property
    def sub_type(self):
        """Gets the sub_type of this ResourceExportData.  # noqa: E501


        :return: The sub_type of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._sub_type

    @sub_type.setter
    def sub_type(self, sub_type):
        """Sets the sub_type of this ResourceExportData.


        :param sub_type: The sub_type of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._sub_type = sub_type

    @property
    def resource_key(self):
        """Gets the resource_key of this ResourceExportData.  # noqa: E501


        :return: The resource_key of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._resource_key

    @resource_key.setter
    def resource_key(self, resource_key):
        """Sets the resource_key of this ResourceExportData.


        :param resource_key: The resource_key of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._resource_key = resource_key

    @property
    def file_name(self):
        """Gets the file_name of this ResourceExportData.  # noqa: E501


        :return: The file_name of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ResourceExportData.


        :param file_name: The file_name of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._file_name = file_name

    @property
    def public_resource_key(self):
        """Gets the public_resource_key of this ResourceExportData.  # noqa: E501


        :return: The public_resource_key of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._public_resource_key

    @public_resource_key.setter
    def public_resource_key(self, public_resource_key):
        """Sets the public_resource_key of this ResourceExportData.


        :param public_resource_key: The public_resource_key of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._public_resource_key = public_resource_key

    @property
    def is_public(self):
        """Gets the is_public of this ResourceExportData.  # noqa: E501


        :return: The is_public of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        """Sets the is_public of this ResourceExportData.


        :param is_public: The is_public of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._is_public = is_public

    @property
    def media_type(self):
        """Gets the media_type of this ResourceExportData.  # noqa: E501


        :return: The media_type of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this ResourceExportData.


        :param media_type: The media_type of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._media_type = media_type

    @property
    def data(self):
        """Gets the data of this ResourceExportData.  # noqa: E501


        :return: The data of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ResourceExportData.


        :param data: The data of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def public(self):
        """Gets the public of this ResourceExportData.  # noqa: E501


        :return: The public of this ResourceExportData.  # noqa: E501
        :rtype: object
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ResourceExportData.


        :param public: The public of this ResourceExportData.  # noqa: E501
        :type: object
        """

        self._public = public

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
        if issubclass(ResourceExportData, dict):
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
        if not isinstance(other, ResourceExportData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
