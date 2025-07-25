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
from tb_rest_client.models.models_pe.menu_item import MenuItem  # noqa: F401,E501

class HomeMenuItem(MenuItem):
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
        'name': 'str',
        'icon': 'str',
        'visible': 'bool',
        'pages': 'list[DefaultMenuItem]',
        'home_type': 'str',
        'dashboard_id': 'str',
        'hide_dashboard_toolbar': 'bool'
    }
    if hasattr(MenuItem, "swagger_types"):
        swagger_types.update(MenuItem.swagger_types)

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'icon': 'icon',
        'visible': 'visible',
        'pages': 'pages',
        'home_type': 'homeType',
        'dashboard_id': 'dashboardId',
        'hide_dashboard_toolbar': 'hideDashboardToolbar'
    }
    if hasattr(MenuItem, "attribute_map"):
        attribute_map.update(MenuItem.attribute_map)

    def __init__(self, id=None, name=None, icon=None, visible=None, pages=None, home_type=None, dashboard_id=None, hide_dashboard_toolbar=None, *args, **kwargs):  # noqa: E501
        """HomeMenuItem - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._icon = None
        self._visible = None
        self._pages = None
        self._home_type = None
        self._dashboard_id = None
        self._hide_dashboard_toolbar = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if icon is not None:
            self.icon = icon
        if visible is not None:
            self.visible = visible
        if pages is not None:
            self.pages = pages
        if home_type is not None:
            self.home_type = home_type
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if hide_dashboard_toolbar is not None:
            self.hide_dashboard_toolbar = hide_dashboard_toolbar
        MenuItem.__init__(self, *args, **kwargs)

    @property
    def id(self):
        """Gets the id of this HomeMenuItem.  # noqa: E501

        Unique identifier for predefined menu items  # noqa: E501

        :return: The id of this HomeMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this HomeMenuItem.

        Unique identifier for predefined menu items  # noqa: E501

        :param id: The id of this HomeMenuItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this HomeMenuItem.  # noqa: E501

        Name of the menu item  # noqa: E501

        :return: The name of this HomeMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this HomeMenuItem.

        Name of the menu item  # noqa: E501

        :param name: The name of this HomeMenuItem.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def icon(self):
        """Gets the icon of this HomeMenuItem.  # noqa: E501

        URL of the menu item icon. Overrides 'materialIcon'  # noqa: E501

        :return: The icon of this HomeMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this HomeMenuItem.

        URL of the menu item icon. Overrides 'materialIcon'  # noqa: E501

        :param icon: The icon of this HomeMenuItem.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def visible(self):
        """Gets the visible of this HomeMenuItem.  # noqa: E501

        Mark if menu item is visible for user  # noqa: E501

        :return: The visible of this HomeMenuItem.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this HomeMenuItem.

        Mark if menu item is visible for user  # noqa: E501

        :param visible: The visible of this HomeMenuItem.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    @property
    def pages(self):
        """Gets the pages of this HomeMenuItem.  # noqa: E501

        List of child menu items  # noqa: E501

        :return: The pages of this HomeMenuItem.  # noqa: E501
        :rtype: list[DefaultMenuItem]
        """
        return self._pages

    @pages.setter
    def pages(self, pages):
        """Sets the pages of this HomeMenuItem.

        List of child menu items  # noqa: E501

        :param pages: The pages of this HomeMenuItem.  # noqa: E501
        :type: list[DefaultMenuItem]
        """

        self._pages = pages

    @property
    def home_type(self):
        """Gets the home_type of this HomeMenuItem.  # noqa: E501

        DEFAULT or DASHBOARD. DASHBOARD means default home page presentation changed to refer to dashboard  # noqa: E501

        :return: The home_type of this HomeMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._home_type

    @home_type.setter
    def home_type(self, home_type):
        """Sets the home_type of this HomeMenuItem.

        DEFAULT or DASHBOARD. DASHBOARD means default home page presentation changed to refer to dashboard  # noqa: E501

        :param home_type: The home_type of this HomeMenuItem.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT", "DASHBOARD"]  # noqa: E501
        if home_type not in allowed_values:
            raise ValueError(
                "Invalid value for `home_type` ({0}), must be one of {1}"  # noqa: E501
                .format(home_type, allowed_values)
            )

        self._home_type = home_type

    @property
    def dashboard_id(self):
        """Gets the dashboard_id of this HomeMenuItem.  # noqa: E501

        Id of the Dashboard to open, when user clicks the menu item  # noqa: E501

        :return: The dashboard_id of this HomeMenuItem.  # noqa: E501
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        """Sets the dashboard_id of this HomeMenuItem.

        Id of the Dashboard to open, when user clicks the menu item  # noqa: E501

        :param dashboard_id: The dashboard_id of this HomeMenuItem.  # noqa: E501
        :type: str
        """

        self._dashboard_id = dashboard_id

    @property
    def hide_dashboard_toolbar(self):
        """Gets the hide_dashboard_toolbar of this HomeMenuItem.  # noqa: E501

        Hide the dashboard toolbar  # noqa: E501

        :return: The hide_dashboard_toolbar of this HomeMenuItem.  # noqa: E501
        :rtype: bool
        """
        return self._hide_dashboard_toolbar

    @hide_dashboard_toolbar.setter
    def hide_dashboard_toolbar(self, hide_dashboard_toolbar):
        """Sets the hide_dashboard_toolbar of this HomeMenuItem.

        Hide the dashboard toolbar  # noqa: E501

        :param hide_dashboard_toolbar: The hide_dashboard_toolbar of this HomeMenuItem.  # noqa: E501
        :type: bool
        """

        self._hide_dashboard_toolbar = hide_dashboard_toolbar

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
        if issubclass(HomeMenuItem, dict):
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
        if not isinstance(other, HomeMenuItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
