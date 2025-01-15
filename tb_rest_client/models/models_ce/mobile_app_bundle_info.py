# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.9.0
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

class MobileAppBundleInfo(object):
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
        'id': 'MobileAppBundleId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'title': 'str',
        'description': 'str',
        'android_app_id': 'MobileAppId',
        'ios_app_id': 'MobileAppId',
        'layout_config': 'MobileLayoutConfig',
        'oauth2_enabled': 'bool',
        'android_pkg_name': 'str',
        'ios_pkg_name': 'str',
        'oauth2_client_infos': 'object',
        'qr_code_enabled': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'title': 'title',
        'description': 'description',
        'android_app_id': 'androidAppId',
        'ios_app_id': 'iosAppId',
        'layout_config': 'layoutConfig',
        'oauth2_enabled': 'oauth2Enabled',
        'android_pkg_name': 'androidPkgName',
        'ios_pkg_name': 'iosPkgName',
        'oauth2_client_infos': 'oauth2ClientInfos',
        'qr_code_enabled': 'qrCodeEnabled',
        'name': 'name'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, title=None, description=None, android_app_id=None, ios_app_id=None, layout_config=None, oauth2_enabled=None, android_pkg_name=None, ios_pkg_name=None, oauth2_client_infos=None, qr_code_enabled=None, name=None):  # noqa: E501
        """MobileAppBundleInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._title = None
        self._description = None
        self._android_app_id = None
        self._ios_app_id = None
        self._layout_config = None
        self._oauth2_enabled = None
        self._android_pkg_name = None
        self._ios_pkg_name = None
        self._oauth2_client_infos = None
        self._qr_code_enabled = None
        self._name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        self.title = title
        if description is not None:
            self.description = description
        if android_app_id is not None:
            self.android_app_id = android_app_id
        if ios_app_id is not None:
            self.ios_app_id = ios_app_id
        if layout_config is not None:
            self.layout_config = layout_config
        if oauth2_enabled is not None:
            self.oauth2_enabled = oauth2_enabled
        if android_pkg_name is not None:
            self.android_pkg_name = android_pkg_name
        if ios_pkg_name is not None:
            self.ios_pkg_name = ios_pkg_name
        if oauth2_client_infos is not None:
            self.oauth2_client_infos = oauth2_client_infos
        if qr_code_enabled is not None:
            self.qr_code_enabled = qr_code_enabled
        if name is not None:
            self.name = name

    @property
    def id(self):
        """Gets the id of this MobileAppBundleInfo.  # noqa: E501


        :return: The id of this MobileAppBundleInfo.  # noqa: E501
        :rtype: MobileAppBundleId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MobileAppBundleInfo.


        :param id: The id of this MobileAppBundleInfo.  # noqa: E501
        :type: MobileAppBundleId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this MobileAppBundleInfo.  # noqa: E501


        :return: The created_time of this MobileAppBundleInfo.  # noqa: E501
        :rtype: object
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this MobileAppBundleInfo.


        :param created_time: The created_time of this MobileAppBundleInfo.  # noqa: E501
        :type: object
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this MobileAppBundleInfo.  # noqa: E501

        JSON object with Tenant Id  # noqa: E501

        :return: The tenant_id of this MobileAppBundleInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this MobileAppBundleInfo.

        JSON object with Tenant Id  # noqa: E501

        :param tenant_id: The tenant_id of this MobileAppBundleInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def title(self):
        """Gets the title of this MobileAppBundleInfo.  # noqa: E501

        Application bundle title. Cannot be empty  # noqa: E501

        :return: The title of this MobileAppBundleInfo.  # noqa: E501
        :rtype: object
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this MobileAppBundleInfo.

        Application bundle title. Cannot be empty  # noqa: E501

        :param title: The title of this MobileAppBundleInfo.  # noqa: E501
        :type: object
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this MobileAppBundleInfo.  # noqa: E501

        Application bundle description.  # noqa: E501

        :return: The description of this MobileAppBundleInfo.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MobileAppBundleInfo.

        Application bundle description.  # noqa: E501

        :param description: The description of this MobileAppBundleInfo.  # noqa: E501
        :type: object
        """

        self._description = description

    @property
    def android_app_id(self):
        """Gets the android_app_id of this MobileAppBundleInfo.  # noqa: E501

        Android application id  # noqa: E501

        :return: The android_app_id of this MobileAppBundleInfo.  # noqa: E501
        :rtype: MobileAppId
        """
        return self._android_app_id

    @android_app_id.setter
    def android_app_id(self, android_app_id):
        """Sets the android_app_id of this MobileAppBundleInfo.

        Android application id  # noqa: E501

        :param android_app_id: The android_app_id of this MobileAppBundleInfo.  # noqa: E501
        :type: MobileAppId
        """

        self._android_app_id = android_app_id

    @property
    def ios_app_id(self):
        """Gets the ios_app_id of this MobileAppBundleInfo.  # noqa: E501

        IOS application id  # noqa: E501

        :return: The ios_app_id of this MobileAppBundleInfo.  # noqa: E501
        :rtype: MobileAppId
        """
        return self._ios_app_id

    @ios_app_id.setter
    def ios_app_id(self, ios_app_id):
        """Sets the ios_app_id of this MobileAppBundleInfo.

        IOS application id  # noqa: E501

        :param ios_app_id: The ios_app_id of this MobileAppBundleInfo.  # noqa: E501
        :type: MobileAppId
        """

        self._ios_app_id = ios_app_id

    @property
    def layout_config(self):
        """Gets the layout_config of this MobileAppBundleInfo.  # noqa: E501

        Application layout configuration  # noqa: E501

        :return: The layout_config of this MobileAppBundleInfo.  # noqa: E501
        :rtype: MobileLayoutConfig
        """
        return self._layout_config

    @layout_config.setter
    def layout_config(self, layout_config):
        """Sets the layout_config of this MobileAppBundleInfo.

        Application layout configuration  # noqa: E501

        :param layout_config: The layout_config of this MobileAppBundleInfo.  # noqa: E501
        :type: MobileLayoutConfig
        """

        self._layout_config = layout_config

    @property
    def oauth2_enabled(self):
        """Gets the oauth2_enabled of this MobileAppBundleInfo.  # noqa: E501

        Whether OAuth2 settings are enabled or not  # noqa: E501

        :return: The oauth2_enabled of this MobileAppBundleInfo.  # noqa: E501
        :rtype: object
        """
        return self._oauth2_enabled

    @oauth2_enabled.setter
    def oauth2_enabled(self, oauth2_enabled):
        """Sets the oauth2_enabled of this MobileAppBundleInfo.

        Whether OAuth2 settings are enabled or not  # noqa: E501

        :param oauth2_enabled: The oauth2_enabled of this MobileAppBundleInfo.  # noqa: E501
        :type: object
        """

        self._oauth2_enabled = oauth2_enabled

    @property
    def android_pkg_name(self):
        """Gets the android_pkg_name of this MobileAppBundleInfo.  # noqa: E501

        Android package name  # noqa: E501

        :return: The android_pkg_name of this MobileAppBundleInfo.  # noqa: E501
        :rtype: object
        """
        return self._android_pkg_name

    @android_pkg_name.setter
    def android_pkg_name(self, android_pkg_name):
        """Sets the android_pkg_name of this MobileAppBundleInfo.

        Android package name  # noqa: E501

        :param android_pkg_name: The android_pkg_name of this MobileAppBundleInfo.  # noqa: E501
        :type: object
        """

        self._android_pkg_name = android_pkg_name

    @property
    def ios_pkg_name(self):
        """Gets the ios_pkg_name of this MobileAppBundleInfo.  # noqa: E501

        IOS package name  # noqa: E501

        :return: The ios_pkg_name of this MobileAppBundleInfo.  # noqa: E501
        :rtype: object
        """
        return self._ios_pkg_name

    @ios_pkg_name.setter
    def ios_pkg_name(self, ios_pkg_name):
        """Sets the ios_pkg_name of this MobileAppBundleInfo.

        IOS package name  # noqa: E501

        :param ios_pkg_name: The ios_pkg_name of this MobileAppBundleInfo.  # noqa: E501
        :type: object
        """

        self._ios_pkg_name = ios_pkg_name

    @property
    def oauth2_client_infos(self):
        """Gets the oauth2_client_infos of this MobileAppBundleInfo.  # noqa: E501

        List of available oauth2 clients  # noqa: E501

        :return: The oauth2_client_infos of this MobileAppBundleInfo.  # noqa: E501
        :rtype: object
        """
        return self._oauth2_client_infos

    @oauth2_client_infos.setter
    def oauth2_client_infos(self, oauth2_client_infos):
        """Sets the oauth2_client_infos of this MobileAppBundleInfo.

        List of available oauth2 clients  # noqa: E501

        :param oauth2_client_infos: The oauth2_client_infos of this MobileAppBundleInfo.  # noqa: E501
        :type: object
        """

        self._oauth2_client_infos = oauth2_client_infos

    @property
    def qr_code_enabled(self):
        """Gets the qr_code_enabled of this MobileAppBundleInfo.  # noqa: E501

        Indicates if qr code is available for bundle  # noqa: E501

        :return: The qr_code_enabled of this MobileAppBundleInfo.  # noqa: E501
        :rtype: object
        """
        return self._qr_code_enabled

    @qr_code_enabled.setter
    def qr_code_enabled(self, qr_code_enabled):
        """Sets the qr_code_enabled of this MobileAppBundleInfo.

        Indicates if qr code is available for bundle  # noqa: E501

        :param qr_code_enabled: The qr_code_enabled of this MobileAppBundleInfo.  # noqa: E501
        :type: object
        """

        self._qr_code_enabled = qr_code_enabled

    @property
    def name(self):
        """Gets the name of this MobileAppBundleInfo.  # noqa: E501

        Mobile app bundle title  # noqa: E501

        :return: The name of this MobileAppBundleInfo.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MobileAppBundleInfo.

        Mobile app bundle title  # noqa: E501

        :param name: The name of this MobileAppBundleInfo.  # noqa: E501
        :type: object
        """

        self._name = name

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
        if issubclass(MobileAppBundleInfo, dict):
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
        if not isinstance(other, MobileAppBundleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other