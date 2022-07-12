# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.4.0-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.device_transport_configuration import DeviceTransportConfiguration  # noqa: F401,E501

class Lwm2mDeviceTransportConfiguration(DeviceTransportConfiguration):
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
        'edrx_cycle': 'int',
        'paging_transmission_window': 'int',
        'power_mode': 'str',
        'psm_activity_timer': 'int'
    }
    if hasattr(DeviceTransportConfiguration, "swagger_types"):
        swagger_types.update(DeviceTransportConfiguration.swagger_types)

    attribute_map = {
        'edrx_cycle': 'edrxCycle',
        'paging_transmission_window': 'pagingTransmissionWindow',
        'power_mode': 'powerMode',
        'psm_activity_timer': 'psmActivityTimer'
    }
    if hasattr(DeviceTransportConfiguration, "attribute_map"):
        attribute_map.update(DeviceTransportConfiguration.attribute_map)

    def __init__(self, edrx_cycle=None, paging_transmission_window=None, power_mode=None, psm_activity_timer=None, *args, **kwargs):  # noqa: E501
        """Lwm2mDeviceTransportConfiguration - a model defined in Swagger"""  # noqa: E501
        self._edrx_cycle = None
        self._paging_transmission_window = None
        self._power_mode = None
        self._psm_activity_timer = None
        self.discriminator = None
        if edrx_cycle is not None:
            self.edrx_cycle = edrx_cycle
        if paging_transmission_window is not None:
            self.paging_transmission_window = paging_transmission_window
        if power_mode is not None:
            self.power_mode = power_mode
        if psm_activity_timer is not None:
            self.psm_activity_timer = psm_activity_timer
        DeviceTransportConfiguration.__init__(self, *args, **kwargs)

    @property
    def edrx_cycle(self):
        """Gets the edrx_cycle of this Lwm2mDeviceTransportConfiguration.  # noqa: E501


        :return: The edrx_cycle of this Lwm2mDeviceTransportConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._edrx_cycle

    @edrx_cycle.setter
    def edrx_cycle(self, edrx_cycle):
        """Sets the edrx_cycle of this Lwm2mDeviceTransportConfiguration.


        :param edrx_cycle: The edrx_cycle of this Lwm2mDeviceTransportConfiguration.  # noqa: E501
        :type: int
        """

        self._edrx_cycle = edrx_cycle

    @property
    def paging_transmission_window(self):
        """Gets the paging_transmission_window of this Lwm2mDeviceTransportConfiguration.  # noqa: E501


        :return: The paging_transmission_window of this Lwm2mDeviceTransportConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._paging_transmission_window

    @paging_transmission_window.setter
    def paging_transmission_window(self, paging_transmission_window):
        """Sets the paging_transmission_window of this Lwm2mDeviceTransportConfiguration.


        :param paging_transmission_window: The paging_transmission_window of this Lwm2mDeviceTransportConfiguration.  # noqa: E501
        :type: int
        """

        self._paging_transmission_window = paging_transmission_window

    @property
    def power_mode(self):
        """Gets the power_mode of this Lwm2mDeviceTransportConfiguration.  # noqa: E501


        :return: The power_mode of this Lwm2mDeviceTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._power_mode

    @power_mode.setter
    def power_mode(self, power_mode):
        """Sets the power_mode of this Lwm2mDeviceTransportConfiguration.


        :param power_mode: The power_mode of this Lwm2mDeviceTransportConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["DRX", "E_DRX", "PSM"]  # noqa: E501
        if power_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `power_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(power_mode, allowed_values)
            )

        self._power_mode = power_mode

    @property
    def psm_activity_timer(self):
        """Gets the psm_activity_timer of this Lwm2mDeviceTransportConfiguration.  # noqa: E501


        :return: The psm_activity_timer of this Lwm2mDeviceTransportConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._psm_activity_timer

    @psm_activity_timer.setter
    def psm_activity_timer(self, psm_activity_timer):
        """Sets the psm_activity_timer of this Lwm2mDeviceTransportConfiguration.


        :param psm_activity_timer: The psm_activity_timer of this Lwm2mDeviceTransportConfiguration.  # noqa: E501
        :type: int
        """

        self._psm_activity_timer = psm_activity_timer

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
        if issubclass(Lwm2mDeviceTransportConfiguration, dict):
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
        if not isinstance(other, Lwm2mDeviceTransportConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
