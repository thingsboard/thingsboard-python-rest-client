# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.3
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2024. ThingsBoard
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

class MqttDeviceProfileTransportConfiguration(object):
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
        'device_attributes_subscribe_topic': 'str',
        'device_attributes_topic': 'str',
        'device_telemetry_topic': 'str',
        'send_ack_on_validation_exception': 'bool',
        'sparkplug': 'bool',
        'sparkplug_attributes_metric_names': 'list[str]',
        'transport_payload_type_configuration': 'TransportPayloadTypeConfiguration'
    }

    attribute_map = {
        'device_attributes_subscribe_topic': 'deviceAttributesSubscribeTopic',
        'device_attributes_topic': 'deviceAttributesTopic',
        'device_telemetry_topic': 'deviceTelemetryTopic',
        'send_ack_on_validation_exception': 'sendAckOnValidationException',
        'sparkplug': 'sparkplug',
        'sparkplug_attributes_metric_names': 'sparkplugAttributesMetricNames',
        'transport_payload_type_configuration': 'transportPayloadTypeConfiguration'
    }

    def __init__(self, device_attributes_subscribe_topic=None, device_attributes_topic=None, device_telemetry_topic=None, send_ack_on_validation_exception=None, sparkplug=None, sparkplug_attributes_metric_names=None, transport_payload_type_configuration=None):  # noqa: E501
        """MqttDeviceProfileTransportConfiguration - a model defined in Swagger"""  # noqa: E501
        self._device_attributes_subscribe_topic = None
        self._device_attributes_topic = None
        self._device_telemetry_topic = None
        self._send_ack_on_validation_exception = None
        self._sparkplug = None
        self._sparkplug_attributes_metric_names = None
        self._transport_payload_type_configuration = None
        self.discriminator = None
        if device_attributes_subscribe_topic is not None:
            self.device_attributes_subscribe_topic = device_attributes_subscribe_topic
        if device_attributes_topic is not None:
            self.device_attributes_topic = device_attributes_topic
        if device_telemetry_topic is not None:
            self.device_telemetry_topic = device_telemetry_topic
        if send_ack_on_validation_exception is not None:
            self.send_ack_on_validation_exception = send_ack_on_validation_exception
        if sparkplug is not None:
            self.sparkplug = sparkplug
        if sparkplug_attributes_metric_names is not None:
            self.sparkplug_attributes_metric_names = sparkplug_attributes_metric_names
        if transport_payload_type_configuration is not None:
            self.transport_payload_type_configuration = transport_payload_type_configuration

    @property
    def device_attributes_subscribe_topic(self):
        """Gets the device_attributes_subscribe_topic of this MqttDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The device_attributes_subscribe_topic of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._device_attributes_subscribe_topic

    @device_attributes_subscribe_topic.setter
    def device_attributes_subscribe_topic(self, device_attributes_subscribe_topic):
        """Sets the device_attributes_subscribe_topic of this MqttDeviceProfileTransportConfiguration.


        :param device_attributes_subscribe_topic: The device_attributes_subscribe_topic of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._device_attributes_subscribe_topic = device_attributes_subscribe_topic

    @property
    def device_attributes_topic(self):
        """Gets the device_attributes_topic of this MqttDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The device_attributes_topic of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._device_attributes_topic

    @device_attributes_topic.setter
    def device_attributes_topic(self, device_attributes_topic):
        """Sets the device_attributes_topic of this MqttDeviceProfileTransportConfiguration.


        :param device_attributes_topic: The device_attributes_topic of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._device_attributes_topic = device_attributes_topic

    @property
    def device_telemetry_topic(self):
        """Gets the device_telemetry_topic of this MqttDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The device_telemetry_topic of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._device_telemetry_topic

    @device_telemetry_topic.setter
    def device_telemetry_topic(self, device_telemetry_topic):
        """Sets the device_telemetry_topic of this MqttDeviceProfileTransportConfiguration.


        :param device_telemetry_topic: The device_telemetry_topic of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :type: str
        """

        self._device_telemetry_topic = device_telemetry_topic

    @property
    def send_ack_on_validation_exception(self):
        """Gets the send_ack_on_validation_exception of this MqttDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The send_ack_on_validation_exception of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._send_ack_on_validation_exception

    @send_ack_on_validation_exception.setter
    def send_ack_on_validation_exception(self, send_ack_on_validation_exception):
        """Sets the send_ack_on_validation_exception of this MqttDeviceProfileTransportConfiguration.


        :param send_ack_on_validation_exception: The send_ack_on_validation_exception of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :type: bool
        """

        self._send_ack_on_validation_exception = send_ack_on_validation_exception

    @property
    def sparkplug(self):
        """Gets the sparkplug of this MqttDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The sparkplug of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: bool
        """
        return self._sparkplug

    @sparkplug.setter
    def sparkplug(self, sparkplug):
        """Sets the sparkplug of this MqttDeviceProfileTransportConfiguration.


        :param sparkplug: The sparkplug of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :type: bool
        """

        self._sparkplug = sparkplug

    @property
    def sparkplug_attributes_metric_names(self):
        """Gets the sparkplug_attributes_metric_names of this MqttDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The sparkplug_attributes_metric_names of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: list[str]
        """
        return self._sparkplug_attributes_metric_names

    @sparkplug_attributes_metric_names.setter
    def sparkplug_attributes_metric_names(self, sparkplug_attributes_metric_names):
        """Sets the sparkplug_attributes_metric_names of this MqttDeviceProfileTransportConfiguration.


        :param sparkplug_attributes_metric_names: The sparkplug_attributes_metric_names of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :type: list[str]
        """

        self._sparkplug_attributes_metric_names = sparkplug_attributes_metric_names

    @property
    def transport_payload_type_configuration(self):
        """Gets the transport_payload_type_configuration of this MqttDeviceProfileTransportConfiguration.  # noqa: E501


        :return: The transport_payload_type_configuration of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
        :rtype: TransportPayloadTypeConfiguration
        """
        return self._transport_payload_type_configuration

    @transport_payload_type_configuration.setter
    def transport_payload_type_configuration(self, transport_payload_type_configuration):
        """Sets the transport_payload_type_configuration of this MqttDeviceProfileTransportConfiguration.


        :param transport_payload_type_configuration: The transport_payload_type_configuration of this MqttDeviceProfileTransportConfiguration.  # noqa: E501
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
        if issubclass(MqttDeviceProfileTransportConfiguration, dict):
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
        if not isinstance(other, MqttDeviceProfileTransportConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
