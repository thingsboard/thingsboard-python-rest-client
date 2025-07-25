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

class Resource(object):
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
        'description': 'str',
        'file': 'str',
        'filename': 'str',
        'input_stream': 'InputStream',
        'open': 'bool',
        'readable': 'bool',
        'uri': 'str',
        'url': 'str'
    }

    attribute_map = {
        'description': 'description',
        'file': 'file',
        'filename': 'filename',
        'input_stream': 'inputStream',
        'open': 'open',
        'readable': 'readable',
        'uri': 'uri',
        'url': 'url'
    }

    def __init__(self, description=None, file=None, filename=None, input_stream=None, open=None, readable=None, uri=None, url=None):  # noqa: E501
        """Resource - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._file = None
        self._filename = None
        self._input_stream = None
        self._open = None
        self._readable = None
        self._uri = None
        self._url = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if file is not None:
            self.file = file
        if filename is not None:
            self.filename = filename
        if input_stream is not None:
            self.input_stream = input_stream
        if open is not None:
            self.open = open
        if readable is not None:
            self.readable = readable
        if uri is not None:
            self.uri = uri
        if url is not None:
            self.url = url

    @property
    def description(self):
        """Gets the description of this Resource.  # noqa: E501


        :return: The description of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Resource.


        :param description: The description of this Resource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def file(self):
        """Gets the file of this Resource.  # noqa: E501


        :return: The file of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this Resource.


        :param file: The file of this Resource.  # noqa: E501
        :type: str
        """

        self._file = file

    @property
    def filename(self):
        """Gets the filename of this Resource.  # noqa: E501


        :return: The filename of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Resource.


        :param filename: The filename of this Resource.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def input_stream(self):
        """Gets the input_stream of this Resource.  # noqa: E501


        :return: The input_stream of this Resource.  # noqa: E501
        :rtype: InputStream
        """
        return self._input_stream

    @input_stream.setter
    def input_stream(self, input_stream):
        """Sets the input_stream of this Resource.


        :param input_stream: The input_stream of this Resource.  # noqa: E501
        :type: InputStream
        """

        self._input_stream = input_stream

    @property
    def open(self):
        """Gets the open of this Resource.  # noqa: E501


        :return: The open of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._open

    @open.setter
    def open(self, open):
        """Sets the open of this Resource.


        :param open: The open of this Resource.  # noqa: E501
        :type: bool
        """

        self._open = open

    @property
    def readable(self):
        """Gets the readable of this Resource.  # noqa: E501


        :return: The readable of this Resource.  # noqa: E501
        :rtype: bool
        """
        return self._readable

    @readable.setter
    def readable(self, readable):
        """Sets the readable of this Resource.


        :param readable: The readable of this Resource.  # noqa: E501
        :type: bool
        """

        self._readable = readable

    @property
    def uri(self):
        """Gets the uri of this Resource.  # noqa: E501


        :return: The uri of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Resource.


        :param uri: The uri of this Resource.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def url(self):
        """Gets the url of this Resource.  # noqa: E501


        :return: The url of this Resource.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Resource.


        :param url: The url of this Resource.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(Resource, dict):
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
        if not isinstance(other, Resource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
