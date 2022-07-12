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

class Rpc(object):
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
        'id': 'RpcId',
        'created_time': 'int',
        'tenant_id': 'TenantId',
        'device_id': 'DeviceId',
        'expiration_time': 'int',
        'request': 'JsonNode',
        'response': 'JsonNode',
        'status': 'str',
        'additional_info': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'tenant_id': 'tenantId',
        'device_id': 'deviceId',
        'expiration_time': 'expirationTime',
        'request': 'request',
        'response': 'response',
        'status': 'status',
        'additional_info': 'additionalInfo'
    }

    def __init__(self, id=None, created_time=None, tenant_id=None, device_id=None, expiration_time=None, request=None, response=None, status=None, additional_info=None):  # noqa: E501
        """Rpc - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._tenant_id = None
        self._device_id = None
        self._expiration_time = None
        self._request = None
        self._response = None
        self._status = None
        self._additional_info = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if device_id is not None:
            self.device_id = device_id
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if request is not None:
            self.request = request
        if response is not None:
            self.response = response
        if status is not None:
            self.status = status
        if additional_info is not None:
            self.additional_info = additional_info

    @property
    def id(self):
        """Gets the id of this Rpc.  # noqa: E501


        :return: The id of this Rpc.  # noqa: E501
        :rtype: RpcId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Rpc.


        :param id: The id of this Rpc.  # noqa: E501
        :type: RpcId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this Rpc.  # noqa: E501

        Timestamp of the rpc creation, in milliseconds  # noqa: E501

        :return: The created_time of this Rpc.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Rpc.

        Timestamp of the rpc creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this Rpc.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Rpc.  # noqa: E501


        :return: The tenant_id of this Rpc.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Rpc.


        :param tenant_id: The tenant_id of this Rpc.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def device_id(self):
        """Gets the device_id of this Rpc.  # noqa: E501


        :return: The device_id of this Rpc.  # noqa: E501
        :rtype: DeviceId
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this Rpc.


        :param device_id: The device_id of this Rpc.  # noqa: E501
        :type: DeviceId
        """

        self._device_id = device_id

    @property
    def expiration_time(self):
        """Gets the expiration_time of this Rpc.  # noqa: E501

        Expiration time of the request.  # noqa: E501

        :return: The expiration_time of this Rpc.  # noqa: E501
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this Rpc.

        Expiration time of the request.  # noqa: E501

        :param expiration_time: The expiration_time of this Rpc.  # noqa: E501
        :type: int
        """

        self._expiration_time = expiration_time

    @property
    def request(self):
        """Gets the request of this Rpc.  # noqa: E501


        :return: The request of this Rpc.  # noqa: E501
        :rtype: JsonNode
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this Rpc.


        :param request: The request of this Rpc.  # noqa: E501
        :type: JsonNode
        """

        self._request = request

    @property
    def response(self):
        """Gets the response of this Rpc.  # noqa: E501


        :return: The response of this Rpc.  # noqa: E501
        :rtype: JsonNode
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this Rpc.


        :param response: The response of this Rpc.  # noqa: E501
        :type: JsonNode
        """

        self._response = response

    @property
    def status(self):
        """Gets the status of this Rpc.  # noqa: E501

        The current status of the RPC call.  # noqa: E501

        :return: The status of this Rpc.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Rpc.

        The current status of the RPC call.  # noqa: E501

        :param status: The status of this Rpc.  # noqa: E501
        :type: str
        """
        allowed_values = ["DELETED", "DELIVERED", "EXPIRED", "FAILED", "QUEUED", "SENT", "SUCCESSFUL", "TIMEOUT"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def additional_info(self):
        """Gets the additional_info of this Rpc.  # noqa: E501


        :return: The additional_info of this Rpc.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Rpc.


        :param additional_info: The additional_info of this Rpc.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

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
        if issubclass(Rpc, dict):
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
        if not isinstance(other, Rpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
