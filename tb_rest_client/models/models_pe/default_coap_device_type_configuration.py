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
from swagger_client.models.coap_device_type_configuration import CoapDeviceTypeConfiguration  # noqa: F401,E501

class DefaultCoapDeviceTypeConfiguration(CoapDeviceTypeConfiguration):
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
        'transport_payload_type_configuration': 'TransportPayloadTypeConfiguration'
    }
    if hasattr(CoapDeviceTypeConfiguration, "swagger_types"):
        swagger_types.update(CoapDeviceTypeConfiguration.swagger_types)

    attribute_map = {
        'transport_payload_type_configuration': 'transportPayloadTypeConfiguration'
    }
    if hasattr(CoapDeviceTypeConfiguration, "attribute_map"):
        attribute_map.update(CoapDeviceTypeConfiguration.attribute_map)

    def __init__(self, transport_payload_type_configuration=None, *args, **kwargs):  # noqa: E501
        """DefaultCoapDeviceTypeConfiguration - a model defined in Swagger"""  # noqa: E501
        self._transport_payload_type_configuration = None
        self.discriminator = None
        if transport_payload_type_configuration is not None:
            self.transport_payload_type_configuration = transport_payload_type_configuration
        CoapDeviceTypeConfiguration.__init__(self, *args, **kwargs)

    @property
    def transport_payload_type_configuration(self):
        """Gets the transport_payload_type_configuration of this DefaultCoapDeviceTypeConfiguration.  # noqa: E501


        :return: The transport_payload_type_configuration of this DefaultCoapDeviceTypeConfiguration.  # noqa: E501
        :rtype: TransportPayloadTypeConfiguration
        """
        return self._transport_payload_type_configuration

    @transport_payload_type_configuration.setter
    def transport_payload_type_configuration(self, transport_payload_type_configuration):
        """Sets the transport_payload_type_configuration of this DefaultCoapDeviceTypeConfiguration.


        :param transport_payload_type_configuration: The transport_payload_type_configuration of this DefaultCoapDeviceTypeConfiguration.  # noqa: E501
        :type: TransportPayloadTypeConfiguration
        """

        self._transport_payload_type_configuration = transport_payload_type_configuration

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
        if issubclass(DefaultCoapDeviceTypeConfiguration, dict):
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
        if not isinstance(other, DefaultCoapDeviceTypeConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
