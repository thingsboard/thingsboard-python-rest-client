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
from swagger_client.models.sms_provider_configuration import SmsProviderConfiguration  # noqa: F401,E501

class SmppSmsProviderConfiguration(SmsProviderConfiguration):
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
        'address_range': 'str',
        'bind_type': 'str',
        'coding_scheme': 'str',
        'destination_npi': 'str',
        'destination_ton': 'str',
        'host': 'str',
        'password': 'str',
        'port': 'int',
        'protocol_version': 'str',
        'service_type': 'str',
        'source_address': 'str',
        'source_npi': 'str',
        'source_ton': 'str',
        'system_id': 'str',
        'system_type': 'str'
    }
    if hasattr(SmsProviderConfiguration, "swagger_types"):
        swagger_types.update(SmsProviderConfiguration.swagger_types)

    attribute_map = {
        'address_range': 'addressRange',
        'bind_type': 'bindType',
        'coding_scheme': 'codingScheme',
        'destination_npi': 'destinationNpi',
        'destination_ton': 'destinationTon',
        'host': 'host',
        'password': 'password',
        'port': 'port',
        'protocol_version': 'protocolVersion',
        'service_type': 'serviceType',
        'source_address': 'sourceAddress',
        'source_npi': 'sourceNpi',
        'source_ton': 'sourceTon',
        'system_id': 'systemId',
        'system_type': 'systemType'
    }
    if hasattr(SmsProviderConfiguration, "attribute_map"):
        attribute_map.update(SmsProviderConfiguration.attribute_map)

    def __init__(self, address_range=None, bind_type=None, coding_scheme=None, destination_npi=None, destination_ton=None, host=None, password=None, port=None, protocol_version=None, service_type=None, source_address=None, source_npi=None, source_ton=None, system_id=None, system_type=None, *args, **kwargs):  # noqa: E501
        """SmppSmsProviderConfiguration - a model defined in Swagger"""  # noqa: E501
        self._address_range = None
        self._bind_type = None
        self._coding_scheme = None
        self._destination_npi = None
        self._destination_ton = None
        self._host = None
        self._password = None
        self._port = None
        self._protocol_version = None
        self._service_type = None
        self._source_address = None
        self._source_npi = None
        self._source_ton = None
        self._system_id = None
        self._system_type = None
        self.discriminator = None
        if address_range is not None:
            self.address_range = address_range
        if bind_type is not None:
            self.bind_type = bind_type
        if coding_scheme is not None:
            self.coding_scheme = coding_scheme
        if destination_npi is not None:
            self.destination_npi = destination_npi
        if destination_ton is not None:
            self.destination_ton = destination_ton
        self.host = host
        self.password = password
        self.port = port
        self.protocol_version = protocol_version
        if service_type is not None:
            self.service_type = service_type
        if source_address is not None:
            self.source_address = source_address
        if source_npi is not None:
            self.source_npi = source_npi
        if source_ton is not None:
            self.source_ton = source_ton
        self.system_id = system_id
        if system_type is not None:
            self.system_type = system_type
        SmsProviderConfiguration.__init__(self, *args, **kwargs)

    @property
    def address_range(self):
        """Gets the address_range of this SmppSmsProviderConfiguration.  # noqa: E501

        Address range  # noqa: E501

        :return: The address_range of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._address_range

    @address_range.setter
    def address_range(self, address_range):
        """Sets the address_range of this SmppSmsProviderConfiguration.

        Address range  # noqa: E501

        :param address_range: The address_range of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._address_range = address_range

    @property
    def bind_type(self):
        """Gets the bind_type of this SmppSmsProviderConfiguration.  # noqa: E501

        TX - Transmitter, RX - Receiver, TRX - Transciever. By default TX is used  # noqa: E501

        :return: The bind_type of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._bind_type

    @bind_type.setter
    def bind_type(self, bind_type):
        """Sets the bind_type of this SmppSmsProviderConfiguration.

        TX - Transmitter, RX - Receiver, TRX - Transciever. By default TX is used  # noqa: E501

        :param bind_type: The bind_type of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """
        allowed_values = ["RX", "TRX", "TX"]  # noqa: E501
        if bind_type not in allowed_values:
            raise ValueError(
                "Invalid value for `bind_type` ({0}), must be one of {1}"  # noqa: E501
                .format(bind_type, allowed_values)
            )

        self._bind_type = bind_type

    @property
    def coding_scheme(self):
        """Gets the coding_scheme of this SmppSmsProviderConfiguration.  # noqa: E501

        0 - SMSC Default Alphabet (ASCII for short and long code and to GSM for toll-free, used as default) 1 - IA5 (ASCII for short and long code, Latin 9 for toll-free (ISO-8859-9)) 2 - Octet Unspecified (8-bit binary) 3 - Latin 1 (ISO-8859-1) 4 - Octet Unspecified (8-bit binary) 5 - JIS (X 0208-1990) 6 - Cyrillic (ISO-8859-5) 7 - Latin/Hebrew (ISO-8859-8) 8 - UCS2/UTF-16 (ISO/IEC-10646) 9 - Pictogram Encoding 10 - Music Codes (ISO-2022-JP) 13 - Extended Kanji JIS (X 0212-1990) 14 - Korean Graphic Character Set (KS C 5601/KS X 1001)  # noqa: E501

        :return: The coding_scheme of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._coding_scheme

    @coding_scheme.setter
    def coding_scheme(self, coding_scheme):
        """Sets the coding_scheme of this SmppSmsProviderConfiguration.

        0 - SMSC Default Alphabet (ASCII for short and long code and to GSM for toll-free, used as default) 1 - IA5 (ASCII for short and long code, Latin 9 for toll-free (ISO-8859-9)) 2 - Octet Unspecified (8-bit binary) 3 - Latin 1 (ISO-8859-1) 4 - Octet Unspecified (8-bit binary) 5 - JIS (X 0208-1990) 6 - Cyrillic (ISO-8859-5) 7 - Latin/Hebrew (ISO-8859-8) 8 - UCS2/UTF-16 (ISO/IEC-10646) 9 - Pictogram Encoding 10 - Music Codes (ISO-2022-JP) 13 - Extended Kanji JIS (X 0212-1990) 14 - Korean Graphic Character Set (KS C 5601/KS X 1001)  # noqa: E501

        :param coding_scheme: The coding_scheme of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._coding_scheme = coding_scheme

    @property
    def destination_npi(self):
        """Gets the destination_npi of this SmppSmsProviderConfiguration.  # noqa: E501

        Destination NPI (Numbering Plan Identification). 0 by default. 0 - Unknown 1 - ISDN/telephone numbering plan (E163/E164) 3 - Data numbering plan (X.121) 4 - Telex numbering plan (F.69) 6 - Land Mobile (E.212) =6 8 - National numbering plan 9 - Private numbering plan 10 - ERMES numbering plan (ETSI DE/PS 3 01-3) 13 - Internet (IP) 18 - WAP Client Id (to be defined by WAP Forum)  # noqa: E501

        :return: The destination_npi of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._destination_npi

    @destination_npi.setter
    def destination_npi(self, destination_npi):
        """Sets the destination_npi of this SmppSmsProviderConfiguration.

        Destination NPI (Numbering Plan Identification). 0 by default. 0 - Unknown 1 - ISDN/telephone numbering plan (E163/E164) 3 - Data numbering plan (X.121) 4 - Telex numbering plan (F.69) 6 - Land Mobile (E.212) =6 8 - National numbering plan 9 - Private numbering plan 10 - ERMES numbering plan (ETSI DE/PS 3 01-3) 13 - Internet (IP) 18 - WAP Client Id (to be defined by WAP Forum)  # noqa: E501

        :param destination_npi: The destination_npi of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._destination_npi = destination_npi

    @property
    def destination_ton(self):
        """Gets the destination_ton of this SmppSmsProviderConfiguration.  # noqa: E501

        Destination TON (Type of Number). 5 by default. 0 - Unknown 1 - International 2 - National 3 - Network Specific 4 - Subscriber Number 5 - Alphanumeric 6 - Abbreviated  # noqa: E501

        :return: The destination_ton of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._destination_ton

    @destination_ton.setter
    def destination_ton(self, destination_ton):
        """Sets the destination_ton of this SmppSmsProviderConfiguration.

        Destination TON (Type of Number). 5 by default. 0 - Unknown 1 - International 2 - National 3 - Network Specific 4 - Subscriber Number 5 - Alphanumeric 6 - Abbreviated  # noqa: E501

        :param destination_ton: The destination_ton of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._destination_ton = destination_ton

    @property
    def host(self):
        """Gets the host of this SmppSmsProviderConfiguration.  # noqa: E501

        SMPP host  # noqa: E501

        :return: The host of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this SmppSmsProviderConfiguration.

        SMPP host  # noqa: E501

        :param host: The host of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """
        if host is None:
            raise ValueError("Invalid value for `host`, must not be `None`")  # noqa: E501

        self._host = host

    @property
    def password(self):
        """Gets the password of this SmppSmsProviderConfiguration.  # noqa: E501

        Password  # noqa: E501

        :return: The password of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SmppSmsProviderConfiguration.

        Password  # noqa: E501

        :param password: The password of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def port(self):
        """Gets the port of this SmppSmsProviderConfiguration.  # noqa: E501

        SMPP port  # noqa: E501

        :return: The port of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this SmppSmsProviderConfiguration.

        SMPP port  # noqa: E501

        :param port: The port of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def protocol_version(self):
        """Gets the protocol_version of this SmppSmsProviderConfiguration.  # noqa: E501

        SMPP version  # noqa: E501

        :return: The protocol_version of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this SmppSmsProviderConfiguration.

        SMPP version  # noqa: E501

        :param protocol_version: The protocol_version of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """
        if protocol_version is None:
            raise ValueError("Invalid value for `protocol_version`, must not be `None`")  # noqa: E501
        allowed_values = ["3.3", "3.4"]  # noqa: E501
        if protocol_version not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol_version` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol_version, allowed_values)
            )

        self._protocol_version = protocol_version

    @property
    def service_type(self):
        """Gets the service_type of this SmppSmsProviderConfiguration.  # noqa: E501

        Service type  # noqa: E501

        :return: The service_type of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this SmppSmsProviderConfiguration.

        Service type  # noqa: E501

        :param service_type: The service_type of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._service_type = service_type

    @property
    def source_address(self):
        """Gets the source_address of this SmppSmsProviderConfiguration.  # noqa: E501

        Source address  # noqa: E501

        :return: The source_address of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._source_address

    @source_address.setter
    def source_address(self, source_address):
        """Sets the source_address of this SmppSmsProviderConfiguration.

        Source address  # noqa: E501

        :param source_address: The source_address of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._source_address = source_address

    @property
    def source_npi(self):
        """Gets the source_npi of this SmppSmsProviderConfiguration.  # noqa: E501

        Source NPI (Numbering Plan Identification). Needed is source address is set. 0 by default. 0 - Unknown 1 - ISDN/telephone numbering plan (E163/E164) 3 - Data numbering plan (X.121) 4 - Telex numbering plan (F.69) 6 - Land Mobile (E.212) =6 8 - National numbering plan 9 - Private numbering plan 10 - ERMES numbering plan (ETSI DE/PS 3 01-3) 13 - Internet (IP) 18 - WAP Client Id (to be defined by WAP Forum)  # noqa: E501

        :return: The source_npi of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._source_npi

    @source_npi.setter
    def source_npi(self, source_npi):
        """Sets the source_npi of this SmppSmsProviderConfiguration.

        Source NPI (Numbering Plan Identification). Needed is source address is set. 0 by default. 0 - Unknown 1 - ISDN/telephone numbering plan (E163/E164) 3 - Data numbering plan (X.121) 4 - Telex numbering plan (F.69) 6 - Land Mobile (E.212) =6 8 - National numbering plan 9 - Private numbering plan 10 - ERMES numbering plan (ETSI DE/PS 3 01-3) 13 - Internet (IP) 18 - WAP Client Id (to be defined by WAP Forum)  # noqa: E501

        :param source_npi: The source_npi of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._source_npi = source_npi

    @property
    def source_ton(self):
        """Gets the source_ton of this SmppSmsProviderConfiguration.  # noqa: E501

        Source TON (Type of Number). Needed is source address is set. 5 by default. 0 - Unknown 1 - International 2 - National 3 - Network Specific 4 - Subscriber Number 5 - Alphanumeric 6 - Abbreviated  # noqa: E501

        :return: The source_ton of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._source_ton

    @source_ton.setter
    def source_ton(self, source_ton):
        """Sets the source_ton of this SmppSmsProviderConfiguration.

        Source TON (Type of Number). Needed is source address is set. 5 by default. 0 - Unknown 1 - International 2 - National 3 - Network Specific 4 - Subscriber Number 5 - Alphanumeric 6 - Abbreviated  # noqa: E501

        :param source_ton: The source_ton of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._source_ton = source_ton

    @property
    def system_id(self):
        """Gets the system_id of this SmppSmsProviderConfiguration.  # noqa: E501

        System ID  # noqa: E501

        :return: The system_id of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SmppSmsProviderConfiguration.

        System ID  # noqa: E501

        :param system_id: The system_id of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """
        if system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

    @property
    def system_type(self):
        """Gets the system_type of this SmppSmsProviderConfiguration.  # noqa: E501

        System type  # noqa: E501

        :return: The system_type of this SmppSmsProviderConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._system_type

    @system_type.setter
    def system_type(self, system_type):
        """Sets the system_type of this SmppSmsProviderConfiguration.

        System type  # noqa: E501

        :param system_type: The system_type of this SmppSmsProviderConfiguration.  # noqa: E501
        :type: str
        """

        self._system_type = system_type

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
        if issubclass(SmppSmsProviderConfiguration, dict):
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
        if not isinstance(other, SmppSmsProviderConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other