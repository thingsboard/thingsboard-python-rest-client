# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0PE-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DeviceProfileInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.
from tb_rest_client.api_client import ApiClient
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
        'id': 'EntityId',
        'name': 'str',
        'image': 'str',
        'default_dashboard_id': 'DashboardId',
        'type': 'str',
        'transport_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'image': 'image',
        'default_dashboard_id': 'defaultDashboardId',
        'type': 'type',
        'transport_type': 'transportType'
    }

    def __init__(self, id=None, name=None, image=None, default_dashboard_id=None, type=None, transport_type=None):  # noqa: E501
        """DeviceProfileInfo - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._image = None
        self._default_dashboard_id = None
        self._type = None
        self._transport_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if image is not None:
            self.image = image
        if default_dashboard_id is not None:
            self.default_dashboard_id = default_dashboard_id
        if type is not None:
            self.type = type
        if transport_type is not None:
            self.transport_type = transport_type

    @property
    def id(self):
        """Gets the id of this DeviceProfileInfo.  # noqa: E501


        :return: The id of this DeviceProfileInfo.  # noqa: E501
        :rtype: EntityId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceProfileInfo.


        :param id: The id of this DeviceProfileInfo.  # noqa: E501
        :type: EntityId
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DeviceProfileInfo.  # noqa: E501

        Entity Name  # noqa: E501

        :return: The name of this DeviceProfileInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeviceProfileInfo.

        Entity Name  # noqa: E501

        :param name: The name of this DeviceProfileInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def image(self):
        """Gets the image of this DeviceProfileInfo.  # noqa: E501

        Either URL or Base64 data of the icon. Used in the mobile application to visualize set of device profiles in the grid view.   # noqa: E501

        :return: The image of this DeviceProfileInfo.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this DeviceProfileInfo.

        Either URL or Base64 data of the icon. Used in the mobile application to visualize set of device profiles in the grid view.   # noqa: E501

        :param image: The image of this DeviceProfileInfo.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def default_dashboard_id(self):
        """Gets the default_dashboard_id of this DeviceProfileInfo.  # noqa: E501


        :return: The default_dashboard_id of this DeviceProfileInfo.  # noqa: E501
        :rtype: DashboardId
        """
        return self._default_dashboard_id

    @default_dashboard_id.setter
    def default_dashboard_id(self, default_dashboard_id):
        """Sets the default_dashboard_id of this DeviceProfileInfo.


        :param default_dashboard_id: The default_dashboard_id of this DeviceProfileInfo.  # noqa: E501
        :type: DashboardId
        """

        self._default_dashboard_id = default_dashboard_id

    @property
    def type(self):
        """Gets the type of this DeviceProfileInfo.  # noqa: E501

        Type of the profile. Always 'DEFAULT' for now. Reserved for future use.  # noqa: E501

        :return: The type of this DeviceProfileInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DeviceProfileInfo.

        Type of the profile. Always 'DEFAULT' for now. Reserved for future use.  # noqa: E501

        :param type: The type of this DeviceProfileInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["DEFAULT"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def transport_type(self):
        """Gets the transport_type of this DeviceProfileInfo.  # noqa: E501

        Type of the transport used to connect the device. Default transport supports HTTP, CoAP and MQTT.  # noqa: E501

        :return: The transport_type of this DeviceProfileInfo.  # noqa: E501
        :rtype: str
        """
        return self._transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        """Sets the transport_type of this DeviceProfileInfo.

        Type of the transport used to connect the device. Default transport supports HTTP, CoAP and MQTT.  # noqa: E501

        :param transport_type: The transport_type of this DeviceProfileInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["COAP", "DEFAULT", "LWM2M", "MQTT", "SNMP"]  # noqa: E501
        if transport_type not in allowed_values:
            raise ValueError(
                "Invalid value for `transport_type` ({0}), must be one of {1}"  # noqa: E501
                .format(transport_type, allowed_values)
            )

        self._transport_type = transport_type

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
        if issubclass(DeviceProfileInfo, dict):
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
        if not isinstance(other, DeviceProfileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
