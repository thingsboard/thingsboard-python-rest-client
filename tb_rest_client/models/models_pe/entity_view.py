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

class EntityView(object):
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
        'entity_id': 'EntityId',
        'tenant_id': 'TenantId',
        'customer_id': 'CustomerId',
        'name': 'str',
        'type': 'str',
        'keys': 'TelemetryEntityView',
        'start_time_ms': 'int',
        'end_time_ms': 'int',
        'version': 'int',
        'id': 'EntityViewId',
        'created_time': 'int',
        'additional_info': 'JsonNode',
        'owner_id': 'EntityId'
    }

    attribute_map = {
        'entity_id': 'entityId',
        'tenant_id': 'tenantId',
        'customer_id': 'customerId',
        'name': 'name',
        'type': 'type',
        'keys': 'keys',
        'start_time_ms': 'startTimeMs',
        'end_time_ms': 'endTimeMs',
        'version': 'version',
        'id': 'id',
        'created_time': 'createdTime',
        'additional_info': 'additionalInfo',
        'owner_id': 'ownerId'
    }

    def __init__(self, entity_id=None, tenant_id=None, customer_id=None, name=None, type=None, keys=None, start_time_ms=None, end_time_ms=None, version=None, id=None, created_time=None, additional_info=None, owner_id=None):  # noqa: E501
        """EntityView - a model defined in Swagger"""  # noqa: E501
        self._entity_id = None
        self._tenant_id = None
        self._customer_id = None
        self._name = None
        self._type = None
        self._keys = None
        self._start_time_ms = None
        self._end_time_ms = None
        self._version = None
        self._id = None
        self._created_time = None
        self._additional_info = None
        self._owner_id = None
        self.discriminator = None
        self.entity_id = entity_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if customer_id is not None:
            self.customer_id = customer_id
        self.name = name
        self.type = type
        if keys is not None:
            self.keys = keys
        if start_time_ms is not None:
            self.start_time_ms = start_time_ms
        if end_time_ms is not None:
            self.end_time_ms = end_time_ms
        if version is not None:
            self.version = version
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if additional_info is not None:
            self.additional_info = additional_info
        if owner_id is not None:
            self.owner_id = owner_id

    @property
    def entity_id(self):
        """Gets the entity_id of this EntityView.  # noqa: E501


        :return: The entity_id of this EntityView.  # noqa: E501
        :rtype: EntityId
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this EntityView.


        :param entity_id: The entity_id of this EntityView.  # noqa: E501
        :type: EntityId
        """
        if entity_id is None:
            raise ValueError("Invalid value for `entity_id`, must not be `None`")  # noqa: E501

        self._entity_id = entity_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this EntityView.  # noqa: E501


        :return: The tenant_id of this EntityView.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this EntityView.


        :param tenant_id: The tenant_id of this EntityView.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def customer_id(self):
        """Gets the customer_id of this EntityView.  # noqa: E501


        :return: The customer_id of this EntityView.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this EntityView.


        :param customer_id: The customer_id of this EntityView.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def name(self):
        """Gets the name of this EntityView.  # noqa: E501

        Entity View name  # noqa: E501

        :return: The name of this EntityView.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EntityView.

        Entity View name  # noqa: E501

        :param name: The name of this EntityView.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this EntityView.  # noqa: E501

        Device Profile Name  # noqa: E501

        :return: The type of this EntityView.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityView.

        Device Profile Name  # noqa: E501

        :param type: The type of this EntityView.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def keys(self):
        """Gets the keys of this EntityView.  # noqa: E501


        :return: The keys of this EntityView.  # noqa: E501
        :rtype: TelemetryEntityView
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this EntityView.


        :param keys: The keys of this EntityView.  # noqa: E501
        :type: TelemetryEntityView
        """

        self._keys = keys

    @property
    def start_time_ms(self):
        """Gets the start_time_ms of this EntityView.  # noqa: E501

        Represents the start time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval;  # noqa: E501

        :return: The start_time_ms of this EntityView.  # noqa: E501
        :rtype: int
        """
        return self._start_time_ms

    @start_time_ms.setter
    def start_time_ms(self, start_time_ms):
        """Sets the start_time_ms of this EntityView.

        Represents the start time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval;  # noqa: E501

        :param start_time_ms: The start_time_ms of this EntityView.  # noqa: E501
        :type: int
        """

        self._start_time_ms = start_time_ms

    @property
    def end_time_ms(self):
        """Gets the end_time_ms of this EntityView.  # noqa: E501

        Represents the end time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval;  # noqa: E501

        :return: The end_time_ms of this EntityView.  # noqa: E501
        :rtype: int
        """
        return self._end_time_ms

    @end_time_ms.setter
    def end_time_ms(self, end_time_ms):
        """Sets the end_time_ms of this EntityView.

        Represents the end time of the interval that is used to limit access to target device telemetry. Customer will not be able to see entity telemetry that is outside the specified interval;  # noqa: E501

        :param end_time_ms: The end_time_ms of this EntityView.  # noqa: E501
        :type: int
        """

        self._end_time_ms = end_time_ms

    @property
    def version(self):
        """Gets the version of this EntityView.  # noqa: E501


        :return: The version of this EntityView.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this EntityView.


        :param version: The version of this EntityView.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def id(self):
        """Gets the id of this EntityView.  # noqa: E501


        :return: The id of this EntityView.  # noqa: E501
        :rtype: EntityViewId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EntityView.


        :param id: The id of this EntityView.  # noqa: E501
        :type: EntityViewId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this EntityView.  # noqa: E501

        Timestamp of the Entity View creation, in milliseconds  # noqa: E501

        :return: The created_time of this EntityView.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EntityView.

        Timestamp of the Entity View creation, in milliseconds  # noqa: E501

        :param created_time: The created_time of this EntityView.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def additional_info(self):
        """Gets the additional_info of this EntityView.  # noqa: E501


        :return: The additional_info of this EntityView.  # noqa: E501
        :rtype: JsonNode
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this EntityView.


        :param additional_info: The additional_info of this EntityView.  # noqa: E501
        :type: JsonNode
        """

        self._additional_info = additional_info

    @property
    def owner_id(self):
        """Gets the owner_id of this EntityView.  # noqa: E501


        :return: The owner_id of this EntityView.  # noqa: E501
        :rtype: EntityId
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this EntityView.


        :param owner_id: The owner_id of this EntityView.  # noqa: E501
        :type: EntityId
        """

        self._owner_id = owner_id

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
        if issubclass(EntityView, dict):
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
        if not isinstance(other, EntityView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
