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
from swagger_client.models.snmp_communication_config import SnmpCommunicationConfig  # noqa: F401,E501

class TelemetryQueryingSnmpCommunicationConfig(SnmpCommunicationConfig):
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
        'mappings': 'list[SnmpMapping]',
        'querying_frequency_ms': 'int',
        'spec': 'str'
    }
    if hasattr(SnmpCommunicationConfig, "swagger_types"):
        swagger_types.update(SnmpCommunicationConfig.swagger_types)

    attribute_map = {
        'mappings': 'mappings',
        'querying_frequency_ms': 'queryingFrequencyMs',
        'spec': 'spec'
    }
    if hasattr(SnmpCommunicationConfig, "attribute_map"):
        attribute_map.update(SnmpCommunicationConfig.attribute_map)

    def __init__(self, mappings=None, querying_frequency_ms=None, spec=None, *args, **kwargs):  # noqa: E501
        """TelemetryQueryingSnmpCommunicationConfig - a model defined in Swagger"""  # noqa: E501
        self._mappings = None
        self._querying_frequency_ms = None
        self._spec = None
        self.discriminator = None
        if mappings is not None:
            self.mappings = mappings
        if querying_frequency_ms is not None:
            self.querying_frequency_ms = querying_frequency_ms
        if spec is not None:
            self.spec = spec
        SnmpCommunicationConfig.__init__(self, *args, **kwargs)

    @property
    def mappings(self):
        """Gets the mappings of this TelemetryQueryingSnmpCommunicationConfig.  # noqa: E501


        :return: The mappings of this TelemetryQueryingSnmpCommunicationConfig.  # noqa: E501
        :rtype: list[SnmpMapping]
        """
        return self._mappings

    @mappings.setter
    def mappings(self, mappings):
        """Sets the mappings of this TelemetryQueryingSnmpCommunicationConfig.


        :param mappings: The mappings of this TelemetryQueryingSnmpCommunicationConfig.  # noqa: E501
        :type: list[SnmpMapping]
        """

        self._mappings = mappings

    @property
    def querying_frequency_ms(self):
        """Gets the querying_frequency_ms of this TelemetryQueryingSnmpCommunicationConfig.  # noqa: E501


        :return: The querying_frequency_ms of this TelemetryQueryingSnmpCommunicationConfig.  # noqa: E501
        :rtype: int
        """
        return self._querying_frequency_ms

    @querying_frequency_ms.setter
    def querying_frequency_ms(self, querying_frequency_ms):
        """Sets the querying_frequency_ms of this TelemetryQueryingSnmpCommunicationConfig.


        :param querying_frequency_ms: The querying_frequency_ms of this TelemetryQueryingSnmpCommunicationConfig.  # noqa: E501
        :type: int
        """

        self._querying_frequency_ms = querying_frequency_ms

    @property
    def spec(self):
        """Gets the spec of this TelemetryQueryingSnmpCommunicationConfig.  # noqa: E501


        :return: The spec of this TelemetryQueryingSnmpCommunicationConfig.  # noqa: E501
        :rtype: str
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this TelemetryQueryingSnmpCommunicationConfig.


        :param spec: The spec of this TelemetryQueryingSnmpCommunicationConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLIENT_ATTRIBUTES_QUERYING", "SHARED_ATTRIBUTES_SETTING", "TELEMETRY_QUERYING", "TO_DEVICE_RPC_REQUEST"]  # noqa: E501
        if spec not in allowed_values:
            raise ValueError(
                "Invalid value for `spec` ({0}), must be one of {1}"  # noqa: E501
                .format(spec, allowed_values)
            )

        self._spec = spec

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
        if issubclass(TelemetryQueryingSnmpCommunicationConfig, dict):
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
        if not isinstance(other, TelemetryQueryingSnmpCommunicationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
