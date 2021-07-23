# coding: utf-8

"""
    ThingsBoard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OtaPackageInfo(object):
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
        'additional_info': 'str',
        'checksum': 'str',
        'checksum_algorithm': 'str',
        'content_type': 'str',
        'created_time': 'int',
        'data_size': 'int',
        'device_profile_id': 'DeviceProfileId',
        'file_name': 'str',
        'has_data': 'bool',
        'id': 'OtaPackageId',
        'tenant_id': 'TenantId',
        'title': 'str',
        'type': 'str',
        'url': 'str',
        'version': 'str'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'checksum': 'checksum',
        'checksum_algorithm': 'checksumAlgorithm',
        'content_type': 'contentType',
        'created_time': 'createdTime',
        'data_size': 'dataSize',
        'device_profile_id': 'deviceProfileId',
        'file_name': 'fileName',
        'has_data': 'hasData',
        'id': 'id',
        'tenant_id': 'tenantId',
        'title': 'title',
        'type': 'type',
        'url': 'url',
        'version': 'version'
    }

    def __init__(self, additional_info=None, checksum=None, checksum_algorithm=None, content_type=None, created_time=None, data_size=None, device_profile_id=None, file_name=None, has_data=None, id=None, tenant_id=None, title=None, type=None, url=None, version=None, _configuration=None):  # noqa: E501
        """OtaPackageInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._additional_info = None
        self._checksum = None
        self._checksum_algorithm = None
        self._content_type = None
        self._created_time = None
        self._data_size = None
        self._device_profile_id = None
        self._file_name = None
        self._has_data = None
        self._id = None
        self._tenant_id = None
        self._title = None
        self._type = None
        self._url = None
        self._version = None
        self.discriminator = None

        if additional_info is not None:
            self.additional_info = additional_info
        if checksum is not None:
            self.checksum = checksum
        if checksum_algorithm is not None:
            self.checksum_algorithm = checksum_algorithm
        if content_type is not None:
            self.content_type = content_type
        if created_time is not None:
            self.created_time = created_time
        if data_size is not None:
            self.data_size = data_size
        if device_profile_id is not None:
            self.device_profile_id = device_profile_id
        if file_name is not None:
            self.file_name = file_name
        if has_data is not None:
            self.has_data = has_data
        if id is not None:
            self.id = id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if url is not None:
            self.url = url
        if version is not None:
            self.version = version

    @property
    def additional_info(self):
        """Gets the additional_info of this OtaPackageInfo.  # noqa: E501


        :return: The additional_info of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this OtaPackageInfo.


        :param additional_info: The additional_info of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def checksum(self):
        """Gets the checksum of this OtaPackageInfo.  # noqa: E501


        :return: The checksum of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this OtaPackageInfo.


        :param checksum: The checksum of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def checksum_algorithm(self):
        """Gets the checksum_algorithm of this OtaPackageInfo.  # noqa: E501


        :return: The checksum_algorithm of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._checksum_algorithm

    @checksum_algorithm.setter
    def checksum_algorithm(self, checksum_algorithm):
        """Sets the checksum_algorithm of this OtaPackageInfo.


        :param checksum_algorithm: The checksum_algorithm of this OtaPackageInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["MD5", "SHA256", "SHA384", "SHA512", "CRC32", "MURMUR3_32", "MURMUR3_128"]  # noqa: E501
        if (self._configuration.client_side_validation and
                checksum_algorithm not in allowed_values):
            raise ValueError(
                "Invalid value for `checksum_algorithm` ({0}), must be one of {1}"  # noqa: E501
                .format(checksum_algorithm, allowed_values)
            )

        self._checksum_algorithm = checksum_algorithm

    @property
    def content_type(self):
        """Gets the content_type of this OtaPackageInfo.  # noqa: E501


        :return: The content_type of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this OtaPackageInfo.


        :param content_type: The content_type of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def created_time(self):
        """Gets the created_time of this OtaPackageInfo.  # noqa: E501


        :return: The created_time of this OtaPackageInfo.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this OtaPackageInfo.


        :param created_time: The created_time of this OtaPackageInfo.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def data_size(self):
        """Gets the data_size of this OtaPackageInfo.  # noqa: E501


        :return: The data_size of this OtaPackageInfo.  # noqa: E501
        :rtype: int
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        """Sets the data_size of this OtaPackageInfo.


        :param data_size: The data_size of this OtaPackageInfo.  # noqa: E501
        :type: int
        """

        self._data_size = data_size

    @property
    def device_profile_id(self):
        """Gets the device_profile_id of this OtaPackageInfo.  # noqa: E501


        :return: The device_profile_id of this OtaPackageInfo.  # noqa: E501
        :rtype: DeviceProfileId
        """
        return self._device_profile_id

    @device_profile_id.setter
    def device_profile_id(self, device_profile_id):
        """Sets the device_profile_id of this OtaPackageInfo.


        :param device_profile_id: The device_profile_id of this OtaPackageInfo.  # noqa: E501
        :type: DeviceProfileId
        """

        self._device_profile_id = device_profile_id

    @property
    def file_name(self):
        """Gets the file_name of this OtaPackageInfo.  # noqa: E501


        :return: The file_name of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this OtaPackageInfo.


        :param file_name: The file_name of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def has_data(self):
        """Gets the has_data of this OtaPackageInfo.  # noqa: E501


        :return: The has_data of this OtaPackageInfo.  # noqa: E501
        :rtype: bool
        """
        return self._has_data

    @has_data.setter
    def has_data(self, has_data):
        """Sets the has_data of this OtaPackageInfo.


        :param has_data: The has_data of this OtaPackageInfo.  # noqa: E501
        :type: bool
        """

        self._has_data = has_data

    @property
    def id(self):
        """Gets the id of this OtaPackageInfo.  # noqa: E501


        :return: The id of this OtaPackageInfo.  # noqa: E501
        :rtype: OtaPackageId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OtaPackageInfo.


        :param id: The id of this OtaPackageInfo.  # noqa: E501
        :type: OtaPackageId
        """

        self._id = id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this OtaPackageInfo.  # noqa: E501


        :return: The tenant_id of this OtaPackageInfo.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this OtaPackageInfo.


        :param tenant_id: The tenant_id of this OtaPackageInfo.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def title(self):
        """Gets the title of this OtaPackageInfo.  # noqa: E501


        :return: The title of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this OtaPackageInfo.


        :param title: The title of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this OtaPackageInfo.  # noqa: E501


        :return: The type of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OtaPackageInfo.


        :param type: The type of this OtaPackageInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["FIRMWARE", "SOFTWARE"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def url(self):
        """Gets the url of this OtaPackageInfo.  # noqa: E501


        :return: The url of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OtaPackageInfo.


        :param url: The url of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def version(self):
        """Gets the version of this OtaPackageInfo.  # noqa: E501


        :return: The version of this OtaPackageInfo.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OtaPackageInfo.


        :param version: The version of this OtaPackageInfo.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(OtaPackageInfo, dict):
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
        if not isinstance(other, OtaPackageInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OtaPackageInfo):
            return True

        return self.to_dict() != other.to_dict()