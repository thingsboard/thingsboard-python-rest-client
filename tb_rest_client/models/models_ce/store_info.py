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

class StoreInfo(object):
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
        'app_id': 'str',
        'sha256_cert_fingerprints': 'str',
        'store_link': 'str'
    }

    attribute_map = {
        'app_id': 'appId',
        'sha256_cert_fingerprints': 'sha256CertFingerprints',
        'store_link': 'storeLink'
    }

    def __init__(self, app_id=None, sha256_cert_fingerprints=None, store_link=None):  # noqa: E501
        """StoreInfo - a model defined in Swagger"""  # noqa: E501
        self._app_id = None
        self._sha256_cert_fingerprints = None
        self._store_link = None
        self.discriminator = None
        if app_id is not None:
            self.app_id = app_id
        if sha256_cert_fingerprints is not None:
            self.sha256_cert_fingerprints = sha256_cert_fingerprints
        if store_link is not None:
            self.store_link = store_link

    @property
    def app_id(self):
        """Gets the app_id of this StoreInfo.  # noqa: E501


        :return: The app_id of this StoreInfo.  # noqa: E501
        :rtype: object
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this StoreInfo.


        :param app_id: The app_id of this StoreInfo.  # noqa: E501
        :type: object
        """

        self._app_id = app_id

    @property
    def sha256_cert_fingerprints(self):
        """Gets the sha256_cert_fingerprints of this StoreInfo.  # noqa: E501


        :return: The sha256_cert_fingerprints of this StoreInfo.  # noqa: E501
        :rtype: object
        """
        return self._sha256_cert_fingerprints

    @sha256_cert_fingerprints.setter
    def sha256_cert_fingerprints(self, sha256_cert_fingerprints):
        """Sets the sha256_cert_fingerprints of this StoreInfo.


        :param sha256_cert_fingerprints: The sha256_cert_fingerprints of this StoreInfo.  # noqa: E501
        :type: object
        """

        self._sha256_cert_fingerprints = sha256_cert_fingerprints

    @property
    def store_link(self):
        """Gets the store_link of this StoreInfo.  # noqa: E501


        :return: The store_link of this StoreInfo.  # noqa: E501
        :rtype: object
        """
        return self._store_link

    @store_link.setter
    def store_link(self, store_link):
        """Sets the store_link of this StoreInfo.


        :param store_link: The store_link of this StoreInfo.  # noqa: E501
        :type: object
        """

        self._store_link = store_link

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
        if issubclass(StoreInfo, dict):
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
        if not isinstance(other, StoreInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
