# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.1.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MobileAppSettings(object):
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
        'id': 'MobileAppSettingsId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'use_system_settings': 'bool',
        'use_default_app': 'bool',
        'android_config': 'AndroidConfig',
        'ios_config': 'IosConfig',
        'qr_code_config': 'QRCodeConfig',
        'default_google_play_link': 'str',
        'default_app_store_link': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'use_system_settings': 'useSystemSettings',
        'use_default_app': 'useDefaultApp',
        'android_config': 'androidConfig',
        'ios_config': 'iosConfig',
        'qr_code_config': 'qrCodeConfig',
        'default_google_play_link': 'defaultGooglePlayLink',
        'default_app_store_link': 'defaultAppStoreLink'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, use_system_settings=None, use_default_app=None, android_config=None, ios_config=None, qr_code_config=None, default_google_play_link=None, default_app_store_link=None):  # noqa: E501
        """MobileAppSettings - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._use_system_settings = None
        self._use_default_app = None
        self._android_config = None
        self._ios_config = None
        self._qr_code_config = None
        self._default_google_play_link = None
        self._default_app_store_link = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if use_system_settings is not None:
            self.use_system_settings = use_system_settings
        self.use_default_app = use_default_app
        self.android_config = android_config
        self.ios_config = ios_config
        self.qr_code_config = qr_code_config
        if default_google_play_link is not None:
            self.default_google_play_link = default_google_play_link
        if default_app_store_link is not None:
            self.default_app_store_link = default_app_store_link

    @property
    def id(self):
        """Gets the id of this MobileAppSettings.  # noqa: E501


        :return: The id of this MobileAppSettings.  # noqa: E501
        :rtype: MobileAppSettingsId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MobileAppSettings.


        :param id: The id of this MobileAppSettings.  # noqa: E501
        :type: MobileAppSettingsId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this MobileAppSettings.  # noqa: E501


        :return: The created_time of this MobileAppSettings.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this MobileAppSettings.


        :param created_time: The created_time of this MobileAppSettings.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this MobileAppSettings.  # noqa: E501


        :return: The tenant_id of this MobileAppSettings.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this MobileAppSettings.


        :param tenant_id: The tenant_id of this MobileAppSettings.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def use_system_settings(self):
        """Gets the use_system_settings of this MobileAppSettings.  # noqa: E501

        Use settings from system level  # noqa: E501

        :return: The use_system_settings of this MobileAppSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_system_settings

    @use_system_settings.setter
    def use_system_settings(self, use_system_settings):
        """Sets the use_system_settings of this MobileAppSettings.

        Use settings from system level  # noqa: E501

        :param use_system_settings: The use_system_settings of this MobileAppSettings.  # noqa: E501
        :type: bool
        """

        self._use_system_settings = use_system_settings

    @property
    def use_default_app(self):
        """Gets the use_default_app of this MobileAppSettings.  # noqa: E501

        Type of application: true means use default Thingsboard app  # noqa: E501

        :return: The use_default_app of this MobileAppSettings.  # noqa: E501
        :rtype: bool
        """
        return self._use_default_app

    @use_default_app.setter
    def use_default_app(self, use_default_app):
        """Sets the use_default_app of this MobileAppSettings.

        Type of application: true means use default Thingsboard app  # noqa: E501

        :param use_default_app: The use_default_app of this MobileAppSettings.  # noqa: E501
        :type: bool
        """
        if use_default_app is None:
            raise ValueError("Invalid value for `use_default_app`, must not be `None`")  # noqa: E501

        self._use_default_app = use_default_app

    @property
    def android_config(self):
        """Gets the android_config of this MobileAppSettings.  # noqa: E501


        :return: The android_config of this MobileAppSettings.  # noqa: E501
        :rtype: AndroidConfig
        """
        return self._android_config

    @android_config.setter
    def android_config(self, android_config):
        """Sets the android_config of this MobileAppSettings.


        :param android_config: The android_config of this MobileAppSettings.  # noqa: E501
        :type: AndroidConfig
        """
        if android_config is None:
            raise ValueError("Invalid value for `android_config`, must not be `None`")  # noqa: E501

        self._android_config = android_config

    @property
    def ios_config(self):
        """Gets the ios_config of this MobileAppSettings.  # noqa: E501


        :return: The ios_config of this MobileAppSettings.  # noqa: E501
        :rtype: IosConfig
        """
        return self._ios_config

    @ios_config.setter
    def ios_config(self, ios_config):
        """Sets the ios_config of this MobileAppSettings.


        :param ios_config: The ios_config of this MobileAppSettings.  # noqa: E501
        :type: IosConfig
        """
        if ios_config is None:
            raise ValueError("Invalid value for `ios_config`, must not be `None`")  # noqa: E501

        self._ios_config = ios_config

    @property
    def qr_code_config(self):
        """Gets the qr_code_config of this MobileAppSettings.  # noqa: E501


        :return: The qr_code_config of this MobileAppSettings.  # noqa: E501
        :rtype: QRCodeConfig
        """
        return self._qr_code_config

    @qr_code_config.setter
    def qr_code_config(self, qr_code_config):
        """Sets the qr_code_config of this MobileAppSettings.


        :param qr_code_config: The qr_code_config of this MobileAppSettings.  # noqa: E501
        :type: QRCodeConfig
        """
        if qr_code_config is None:
            raise ValueError("Invalid value for `qr_code_config`, must not be `None`")  # noqa: E501

        self._qr_code_config = qr_code_config

    @property
    def default_google_play_link(self):
        """Gets the default_google_play_link of this MobileAppSettings.  # noqa: E501


        :return: The default_google_play_link of this MobileAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_google_play_link

    @default_google_play_link.setter
    def default_google_play_link(self, default_google_play_link):
        """Sets the default_google_play_link of this MobileAppSettings.


        :param default_google_play_link: The default_google_play_link of this MobileAppSettings.  # noqa: E501
        :type: str
        """

        self._default_google_play_link = default_google_play_link

    @property
    def default_app_store_link(self):
        """Gets the default_app_store_link of this MobileAppSettings.  # noqa: E501


        :return: The default_app_store_link of this MobileAppSettings.  # noqa: E501
        :rtype: str
        """
        return self._default_app_store_link

    @default_app_store_link.setter
    def default_app_store_link(self, default_app_store_link):
        """Sets the default_app_store_link of this MobileAppSettings.


        :param default_app_store_link: The default_app_store_link of this MobileAppSettings.  # noqa: E501
        :type: str
        """

        self._default_app_store_link = default_app_store_link

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
        if issubclass(MobileAppSettings, dict):
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
        if not isinstance(other, MobileAppSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
