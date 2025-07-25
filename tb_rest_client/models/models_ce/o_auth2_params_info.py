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

class OAuth2ParamsInfo(object):
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
        'domain_infos': 'list[OAuth2DomainInfo]',
        'mobile_infos': 'list[OAuth2MobileInfo]',
        'client_registrations': 'list[OAuth2RegistrationInfo]'
    }

    attribute_map = {
        'domain_infos': 'domainInfos',
        'mobile_infos': 'mobileInfos',
        'client_registrations': 'clientRegistrations'
    }

    def __init__(self, domain_infos=None, mobile_infos=None, client_registrations=None):  # noqa: E501
        """OAuth2ParamsInfo - a model defined in Swagger"""  # noqa: E501
        self._domain_infos = None
        self._mobile_infos = None
        self._client_registrations = None
        self.discriminator = None
        self.domain_infos = domain_infos
        self.mobile_infos = mobile_infos
        self.client_registrations = client_registrations

    @property
    def domain_infos(self):
        """Gets the domain_infos of this OAuth2ParamsInfo.  # noqa: E501

        List of configured domains where OAuth2 platform will redirect a user after successful authentication. Cannot be empty. There have to be only one domain with specific name with scheme type 'MIXED'. Configured domains with the same name must have different scheme types  # noqa: E501

        :return: The domain_infos of this OAuth2ParamsInfo.  # noqa: E501
        :rtype: list[OAuth2DomainInfo]
        """
        return self._domain_infos

    @domain_infos.setter
    def domain_infos(self, domain_infos):
        """Sets the domain_infos of this OAuth2ParamsInfo.

        List of configured domains where OAuth2 platform will redirect a user after successful authentication. Cannot be empty. There have to be only one domain with specific name with scheme type 'MIXED'. Configured domains with the same name must have different scheme types  # noqa: E501

        :param domain_infos: The domain_infos of this OAuth2ParamsInfo.  # noqa: E501
        :type: list[OAuth2DomainInfo]
        """
        if domain_infos is None:
            raise ValueError("Invalid value for `domain_infos`, must not be `None`")  # noqa: E501

        self._domain_infos = domain_infos

    @property
    def mobile_infos(self):
        """Gets the mobile_infos of this OAuth2ParamsInfo.  # noqa: E501

        Mobile applications settings. Application package name must be unique within the list  # noqa: E501

        :return: The mobile_infos of this OAuth2ParamsInfo.  # noqa: E501
        :rtype: list[OAuth2MobileInfo]
        """
        return self._mobile_infos

    @mobile_infos.setter
    def mobile_infos(self, mobile_infos):
        """Sets the mobile_infos of this OAuth2ParamsInfo.

        Mobile applications settings. Application package name must be unique within the list  # noqa: E501

        :param mobile_infos: The mobile_infos of this OAuth2ParamsInfo.  # noqa: E501
        :type: list[OAuth2MobileInfo]
        """
        if mobile_infos is None:
            raise ValueError("Invalid value for `mobile_infos`, must not be `None`")  # noqa: E501

        self._mobile_infos = mobile_infos

    @property
    def client_registrations(self):
        """Gets the client_registrations of this OAuth2ParamsInfo.  # noqa: E501

        List of OAuth2 provider settings. Cannot be empty  # noqa: E501

        :return: The client_registrations of this OAuth2ParamsInfo.  # noqa: E501
        :rtype: list[OAuth2RegistrationInfo]
        """
        return self._client_registrations

    @client_registrations.setter
    def client_registrations(self, client_registrations):
        """Sets the client_registrations of this OAuth2ParamsInfo.

        List of OAuth2 provider settings. Cannot be empty  # noqa: E501

        :param client_registrations: The client_registrations of this OAuth2ParamsInfo.  # noqa: E501
        :type: list[OAuth2RegistrationInfo]
        """
        if client_registrations is None:
            raise ValueError("Invalid value for `client_registrations`, must not be `None`")  # noqa: E501

        self._client_registrations = client_registrations

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
        if issubclass(OAuth2ParamsInfo, dict):
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
        if not isinstance(other, OAuth2ParamsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
