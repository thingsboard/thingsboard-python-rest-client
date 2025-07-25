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

class LoginWhiteLabelingParams(object):
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
        'logo_image_url': 'str',
        'logo_image_height': 'int',
        'app_title': 'str',
        'favicon': 'Favicon',
        'palette_settings': 'PaletteSettings',
        'help_link_base_url': 'str',
        'ui_help_base_url': 'str',
        'enable_help_links': 'bool',
        'white_labeling_enabled': 'bool',
        'show_name_version': 'bool',
        'platform_name': 'str',
        'platform_version': 'str',
        'custom_css': 'str',
        'hide_connectivity_dialog': 'bool',
        'page_background_color': 'str',
        'dark_foreground': 'bool',
        'domain_name': 'str',
        'base_url': 'str',
        'prohibit_different_url': 'bool',
        'admin_settings_id': 'str',
        'show_name_bottom': 'bool'
    }

    attribute_map = {
        'logo_image_url': 'logoImageUrl',
        'logo_image_height': 'logoImageHeight',
        'app_title': 'appTitle',
        'favicon': 'favicon',
        'palette_settings': 'paletteSettings',
        'help_link_base_url': 'helpLinkBaseUrl',
        'ui_help_base_url': 'uiHelpBaseUrl',
        'enable_help_links': 'enableHelpLinks',
        'white_labeling_enabled': 'whiteLabelingEnabled',
        'show_name_version': 'showNameVersion',
        'platform_name': 'platformName',
        'platform_version': 'platformVersion',
        'custom_css': 'customCss',
        'hide_connectivity_dialog': 'hideConnectivityDialog',
        'page_background_color': 'pageBackgroundColor',
        'dark_foreground': 'darkForeground',
        'domain_name': 'domainName',
        'base_url': 'baseUrl',
        'prohibit_different_url': 'prohibitDifferentUrl',
        'admin_settings_id': 'adminSettingsId',
        'show_name_bottom': 'showNameBottom'
    }

    def __init__(self, logo_image_url=None, logo_image_height=None, app_title=None, favicon=None, palette_settings=None, help_link_base_url=None, ui_help_base_url=None, enable_help_links=None, white_labeling_enabled=None, show_name_version=None, platform_name=None, platform_version=None, custom_css=None, hide_connectivity_dialog=None, page_background_color=None, dark_foreground=None, domain_name=None, base_url=None, prohibit_different_url=None, admin_settings_id=None, show_name_bottom=None):  # noqa: E501
        """LoginWhiteLabelingParams - a model defined in Swagger"""  # noqa: E501
        self._logo_image_url = None
        self._logo_image_height = None
        self._app_title = None
        self._favicon = None
        self._palette_settings = None
        self._help_link_base_url = None
        self._ui_help_base_url = None
        self._enable_help_links = None
        self._white_labeling_enabled = None
        self._show_name_version = None
        self._platform_name = None
        self._platform_version = None
        self._custom_css = None
        self._hide_connectivity_dialog = None
        self._page_background_color = None
        self._dark_foreground = None
        self._domain_name = None
        self._base_url = None
        self._prohibit_different_url = None
        self._admin_settings_id = None
        self._show_name_bottom = None
        self.discriminator = None
        if logo_image_url is not None:
            self.logo_image_url = logo_image_url
        if logo_image_height is not None:
            self.logo_image_height = logo_image_height
        if app_title is not None:
            self.app_title = app_title
        if favicon is not None:
            self.favicon = favicon
        if palette_settings is not None:
            self.palette_settings = palette_settings
        if help_link_base_url is not None:
            self.help_link_base_url = help_link_base_url
        if ui_help_base_url is not None:
            self.ui_help_base_url = ui_help_base_url
        if enable_help_links is not None:
            self.enable_help_links = enable_help_links
        if white_labeling_enabled is not None:
            self.white_labeling_enabled = white_labeling_enabled
        if show_name_version is not None:
            self.show_name_version = show_name_version
        if platform_name is not None:
            self.platform_name = platform_name
        if platform_version is not None:
            self.platform_version = platform_version
        if custom_css is not None:
            self.custom_css = custom_css
        if hide_connectivity_dialog is not None:
            self.hide_connectivity_dialog = hide_connectivity_dialog
        if page_background_color is not None:
            self.page_background_color = page_background_color
        if dark_foreground is not None:
            self.dark_foreground = dark_foreground
        if domain_name is not None:
            self.domain_name = domain_name
        if base_url is not None:
            self.base_url = base_url
        if prohibit_different_url is not None:
            self.prohibit_different_url = prohibit_different_url
        if admin_settings_id is not None:
            self.admin_settings_id = admin_settings_id
        if show_name_bottom is not None:
            self.show_name_bottom = show_name_bottom

    @property
    def logo_image_url(self):
        """Gets the logo_image_url of this LoginWhiteLabelingParams.  # noqa: E501

        Logo image URL  # noqa: E501

        :return: The logo_image_url of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._logo_image_url

    @logo_image_url.setter
    def logo_image_url(self, logo_image_url):
        """Sets the logo_image_url of this LoginWhiteLabelingParams.

        Logo image URL  # noqa: E501

        :param logo_image_url: The logo_image_url of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._logo_image_url = logo_image_url

    @property
    def logo_image_height(self):
        """Gets the logo_image_height of this LoginWhiteLabelingParams.  # noqa: E501

        The height of a logo container. Logo image will be automatically scaled.  # noqa: E501

        :return: The logo_image_height of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: int
        """
        return self._logo_image_height

    @logo_image_height.setter
    def logo_image_height(self, logo_image_height):
        """Sets the logo_image_height of this LoginWhiteLabelingParams.

        The height of a logo container. Logo image will be automatically scaled.  # noqa: E501

        :param logo_image_height: The logo_image_height of this LoginWhiteLabelingParams.  # noqa: E501
        :type: int
        """

        self._logo_image_height = logo_image_height

    @property
    def app_title(self):
        """Gets the app_title of this LoginWhiteLabelingParams.  # noqa: E501

        White-labeled name of the platform  # noqa: E501

        :return: The app_title of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._app_title

    @app_title.setter
    def app_title(self, app_title):
        """Sets the app_title of this LoginWhiteLabelingParams.

        White-labeled name of the platform  # noqa: E501

        :param app_title: The app_title of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._app_title = app_title

    @property
    def favicon(self):
        """Gets the favicon of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The favicon of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: Favicon
        """
        return self._favicon

    @favicon.setter
    def favicon(self, favicon):
        """Sets the favicon of this LoginWhiteLabelingParams.


        :param favicon: The favicon of this LoginWhiteLabelingParams.  # noqa: E501
        :type: Favicon
        """

        self._favicon = favicon

    @property
    def palette_settings(self):
        """Gets the palette_settings of this LoginWhiteLabelingParams.  # noqa: E501


        :return: The palette_settings of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: PaletteSettings
        """
        return self._palette_settings

    @palette_settings.setter
    def palette_settings(self, palette_settings):
        """Sets the palette_settings of this LoginWhiteLabelingParams.


        :param palette_settings: The palette_settings of this LoginWhiteLabelingParams.  # noqa: E501
        :type: PaletteSettings
        """

        self._palette_settings = palette_settings

    @property
    def help_link_base_url(self):
        """Gets the help_link_base_url of this LoginWhiteLabelingParams.  # noqa: E501

        Base URL for help link  # noqa: E501

        :return: The help_link_base_url of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._help_link_base_url

    @help_link_base_url.setter
    def help_link_base_url(self, help_link_base_url):
        """Sets the help_link_base_url of this LoginWhiteLabelingParams.

        Base URL for help link  # noqa: E501

        :param help_link_base_url: The help_link_base_url of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._help_link_base_url = help_link_base_url

    @property
    def ui_help_base_url(self):
        """Gets the ui_help_base_url of this LoginWhiteLabelingParams.  # noqa: E501

        Base URL for the repository with the UI help components (markdown)  # noqa: E501

        :return: The ui_help_base_url of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._ui_help_base_url

    @ui_help_base_url.setter
    def ui_help_base_url(self, ui_help_base_url):
        """Sets the ui_help_base_url of this LoginWhiteLabelingParams.

        Base URL for the repository with the UI help components (markdown)  # noqa: E501

        :param ui_help_base_url: The ui_help_base_url of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._ui_help_base_url = ui_help_base_url

    @property
    def enable_help_links(self):
        """Gets the enable_help_links of this LoginWhiteLabelingParams.  # noqa: E501

        Enable or Disable help links  # noqa: E501

        :return: The enable_help_links of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._enable_help_links

    @enable_help_links.setter
    def enable_help_links(self, enable_help_links):
        """Sets the enable_help_links of this LoginWhiteLabelingParams.

        Enable or Disable help links  # noqa: E501

        :param enable_help_links: The enable_help_links of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._enable_help_links = enable_help_links

    @property
    def white_labeling_enabled(self):
        """Gets the white_labeling_enabled of this LoginWhiteLabelingParams.  # noqa: E501

        Enable white-labeling  # noqa: E501

        :return: The white_labeling_enabled of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._white_labeling_enabled

    @white_labeling_enabled.setter
    def white_labeling_enabled(self, white_labeling_enabled):
        """Sets the white_labeling_enabled of this LoginWhiteLabelingParams.

        Enable white-labeling  # noqa: E501

        :param white_labeling_enabled: The white_labeling_enabled of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._white_labeling_enabled = white_labeling_enabled

    @property
    def show_name_version(self):
        """Gets the show_name_version of this LoginWhiteLabelingParams.  # noqa: E501

        Show platform name and version on UI and login screen  # noqa: E501

        :return: The show_name_version of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._show_name_version

    @show_name_version.setter
    def show_name_version(self, show_name_version):
        """Sets the show_name_version of this LoginWhiteLabelingParams.

        Show platform name and version on UI and login screen  # noqa: E501

        :param show_name_version: The show_name_version of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._show_name_version = show_name_version

    @property
    def platform_name(self):
        """Gets the platform_name of this LoginWhiteLabelingParams.  # noqa: E501

        White-labeled platform name  # noqa: E501

        :return: The platform_name of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._platform_name

    @platform_name.setter
    def platform_name(self, platform_name):
        """Sets the platform_name of this LoginWhiteLabelingParams.

        White-labeled platform name  # noqa: E501

        :param platform_name: The platform_name of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._platform_name = platform_name

    @property
    def platform_version(self):
        """Gets the platform_version of this LoginWhiteLabelingParams.  # noqa: E501

        White-labeled platform version  # noqa: E501

        :return: The platform_version of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._platform_version

    @platform_version.setter
    def platform_version(self, platform_version):
        """Sets the platform_version of this LoginWhiteLabelingParams.

        White-labeled platform version  # noqa: E501

        :param platform_version: The platform_version of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._platform_version = platform_version

    @property
    def custom_css(self):
        """Gets the custom_css of this LoginWhiteLabelingParams.  # noqa: E501

        Custom CSS content  # noqa: E501

        :return: The custom_css of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._custom_css

    @custom_css.setter
    def custom_css(self, custom_css):
        """Sets the custom_css of this LoginWhiteLabelingParams.

        Custom CSS content  # noqa: E501

        :param custom_css: The custom_css of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._custom_css = custom_css

    @property
    def hide_connectivity_dialog(self):
        """Gets the hide_connectivity_dialog of this LoginWhiteLabelingParams.  # noqa: E501

        Hide device connectivity dialog  # noqa: E501

        :return: The hide_connectivity_dialog of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._hide_connectivity_dialog

    @hide_connectivity_dialog.setter
    def hide_connectivity_dialog(self, hide_connectivity_dialog):
        """Sets the hide_connectivity_dialog of this LoginWhiteLabelingParams.

        Hide device connectivity dialog  # noqa: E501

        :param hide_connectivity_dialog: The hide_connectivity_dialog of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._hide_connectivity_dialog = hide_connectivity_dialog

    @property
    def page_background_color(self):
        """Gets the page_background_color of this LoginWhiteLabelingParams.  # noqa: E501

        Login page background color  # noqa: E501

        :return: The page_background_color of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._page_background_color

    @page_background_color.setter
    def page_background_color(self, page_background_color):
        """Sets the page_background_color of this LoginWhiteLabelingParams.

        Login page background color  # noqa: E501

        :param page_background_color: The page_background_color of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._page_background_color = page_background_color

    @property
    def dark_foreground(self):
        """Gets the dark_foreground of this LoginWhiteLabelingParams.  # noqa: E501

        Enable/Disable dark foreground  # noqa: E501

        :return: The dark_foreground of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._dark_foreground

    @dark_foreground.setter
    def dark_foreground(self, dark_foreground):
        """Sets the dark_foreground of this LoginWhiteLabelingParams.

        Enable/Disable dark foreground  # noqa: E501

        :param dark_foreground: The dark_foreground of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._dark_foreground = dark_foreground

    @property
    def domain_name(self):
        """Gets the domain_name of this LoginWhiteLabelingParams.  # noqa: E501

        Domain name of the login page  # noqa: E501

        :return: The domain_name of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this LoginWhiteLabelingParams.

        Domain name of the login page  # noqa: E501

        :param domain_name: The domain_name of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def base_url(self):
        """Gets the base_url of this LoginWhiteLabelingParams.  # noqa: E501

        Base URL for the activation link, etc  # noqa: E501

        :return: The base_url of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this LoginWhiteLabelingParams.

        Base URL for the activation link, etc  # noqa: E501

        :param base_url: The base_url of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def prohibit_different_url(self):
        """Gets the prohibit_different_url of this LoginWhiteLabelingParams.  # noqa: E501

        Prohibit use of other URLs. It is recommended to enable this setting  # noqa: E501

        :return: The prohibit_different_url of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._prohibit_different_url

    @prohibit_different_url.setter
    def prohibit_different_url(self, prohibit_different_url):
        """Sets the prohibit_different_url of this LoginWhiteLabelingParams.

        Prohibit use of other URLs. It is recommended to enable this setting  # noqa: E501

        :param prohibit_different_url: The prohibit_different_url of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._prohibit_different_url = prohibit_different_url

    @property
    def admin_settings_id(self):
        """Gets the admin_settings_id of this LoginWhiteLabelingParams.  # noqa: E501

        Id of the settings object that store this parameters  # noqa: E501

        :return: The admin_settings_id of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: str
        """
        return self._admin_settings_id

    @admin_settings_id.setter
    def admin_settings_id(self, admin_settings_id):
        """Sets the admin_settings_id of this LoginWhiteLabelingParams.

        Id of the settings object that store this parameters  # noqa: E501

        :param admin_settings_id: The admin_settings_id of this LoginWhiteLabelingParams.  # noqa: E501
        :type: str
        """

        self._admin_settings_id = admin_settings_id

    @property
    def show_name_bottom(self):
        """Gets the show_name_bottom of this LoginWhiteLabelingParams.  # noqa: E501

        Show platform name and version on login page  # noqa: E501

        :return: The show_name_bottom of this LoginWhiteLabelingParams.  # noqa: E501
        :rtype: bool
        """
        return self._show_name_bottom

    @show_name_bottom.setter
    def show_name_bottom(self, show_name_bottom):
        """Sets the show_name_bottom of this LoginWhiteLabelingParams.

        Show platform name and version on login page  # noqa: E501

        :param show_name_bottom: The show_name_bottom of this LoginWhiteLabelingParams.  # noqa: E501
        :type: bool
        """

        self._show_name_bottom = show_name_bottom

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
        if issubclass(LoginWhiteLabelingParams, dict):
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
        if not isinstance(other, LoginWhiteLabelingParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
