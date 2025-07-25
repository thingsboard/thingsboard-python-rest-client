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

class EdgeEvent(object):
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
        'id': 'EdgeEventId',
        'created_time': 'int',
        'seq_id': 'int',
        'tenant_id': 'TenantId',
        'edge_id': 'EdgeId',
        'action': 'str',
        'entity_id': 'str',
        'uid': 'str',
        'type': 'str',
        'entity_group_id': 'str',
        'body': 'JsonNode'
    }

    attribute_map = {
        'id': 'id',
        'created_time': 'createdTime',
        'seq_id': 'seqId',
        'tenant_id': 'tenantId',
        'edge_id': 'edgeId',
        'action': 'action',
        'entity_id': 'entityId',
        'uid': 'uid',
        'type': 'type',
        'entity_group_id': 'entityGroupId',
        'body': 'body'
    }

    def __init__(self, id=None, created_time=None, seq_id=None, tenant_id=None, edge_id=None, action=None, entity_id=None, uid=None, type=None, entity_group_id=None, body=None):  # noqa: E501
        """EdgeEvent - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_time = None
        self._seq_id = None
        self._tenant_id = None
        self._edge_id = None
        self._action = None
        self._entity_id = None
        self._uid = None
        self._type = None
        self._entity_group_id = None
        self._body = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if created_time is not None:
            self.created_time = created_time
        if seq_id is not None:
            self.seq_id = seq_id
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if edge_id is not None:
            self.edge_id = edge_id
        if action is not None:
            self.action = action
        if entity_id is not None:
            self.entity_id = entity_id
        if uid is not None:
            self.uid = uid
        if type is not None:
            self.type = type
        if entity_group_id is not None:
            self.entity_group_id = entity_group_id
        if body is not None:
            self.body = body

    @property
    def id(self):
        """Gets the id of this EdgeEvent.  # noqa: E501


        :return: The id of this EdgeEvent.  # noqa: E501
        :rtype: EdgeEventId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EdgeEvent.


        :param id: The id of this EdgeEvent.  # noqa: E501
        :type: EdgeEventId
        """

        self._id = id

    @property
    def created_time(self):
        """Gets the created_time of this EdgeEvent.  # noqa: E501


        :return: The created_time of this EdgeEvent.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this EdgeEvent.


        :param created_time: The created_time of this EdgeEvent.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def seq_id(self):
        """Gets the seq_id of this EdgeEvent.  # noqa: E501


        :return: The seq_id of this EdgeEvent.  # noqa: E501
        :rtype: int
        """
        return self._seq_id

    @seq_id.setter
    def seq_id(self, seq_id):
        """Sets the seq_id of this EdgeEvent.


        :param seq_id: The seq_id of this EdgeEvent.  # noqa: E501
        :type: int
        """

        self._seq_id = seq_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this EdgeEvent.  # noqa: E501


        :return: The tenant_id of this EdgeEvent.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this EdgeEvent.


        :param tenant_id: The tenant_id of this EdgeEvent.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def edge_id(self):
        """Gets the edge_id of this EdgeEvent.  # noqa: E501


        :return: The edge_id of this EdgeEvent.  # noqa: E501
        :rtype: EdgeId
        """
        return self._edge_id

    @edge_id.setter
    def edge_id(self, edge_id):
        """Sets the edge_id of this EdgeEvent.


        :param edge_id: The edge_id of this EdgeEvent.  # noqa: E501
        :type: EdgeId
        """

        self._edge_id = edge_id

    @property
    def action(self):
        """Gets the action of this EdgeEvent.  # noqa: E501


        :return: The action of this EdgeEvent.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this EdgeEvent.


        :param action: The action of this EdgeEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADDED", "UPDATED", "DELETED", "POST_ATTRIBUTES", "ATTRIBUTES_UPDATED", "ATTRIBUTES_DELETED", "TIMESERIES_UPDATED", "CREDENTIALS_UPDATED", "RELATION_ADD_OR_UPDATE", "RELATION_DELETED", "RPC_CALL", "ALARM_ACK", "ALARM_CLEAR", "ALARM_DELETE", "ALARM_ASSIGNED", "ALARM_UNASSIGNED", "ADDED_COMMENT", "UPDATED_COMMENT", "DELETED_COMMENT", "ASSIGNED_TO_EDGE", "UNASSIGNED_FROM_EDGE", "CREDENTIALS_REQUEST", "ADDED_TO_ENTITY_GROUP", "REMOVED_FROM_ENTITY_GROUP", "CHANGE_OWNER", "ENTITY_MERGE_REQUEST"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def entity_id(self):
        """Gets the entity_id of this EdgeEvent.  # noqa: E501


        :return: The entity_id of this EdgeEvent.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this EdgeEvent.


        :param entity_id: The entity_id of this EdgeEvent.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def uid(self):
        """Gets the uid of this EdgeEvent.  # noqa: E501


        :return: The uid of this EdgeEvent.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this EdgeEvent.


        :param uid: The uid of this EdgeEvent.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def type(self):
        """Gets the type of this EdgeEvent.  # noqa: E501


        :return: The type of this EdgeEvent.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EdgeEvent.


        :param type: The type of this EdgeEvent.  # noqa: E501
        :type: str
        """
        allowed_values = ["DASHBOARD", "ASSET", "DEVICE", "DEVICE_PROFILE", "ASSET_PROFILE", "ENTITY_VIEW", "ALARM", "ALARM_COMMENT", "RULE_CHAIN", "RULE_CHAIN_METADATA", "EDGE", "USER", "CUSTOMER", "RELATION", "TENANT", "TENANT_PROFILE", "WIDGETS_BUNDLE", "WIDGET_TYPE", "ADMIN_SETTINGS", "OTA_PACKAGE", "QUEUE", "ENTITY_GROUP", "SCHEDULER_EVENT", "WHITE_LABELING", "LOGIN_WHITE_LABELING", "MAIL_TEMPLATES", "CUSTOM_TRANSLATION", "CUSTOM_MENU", "ROLE", "GROUP_PERMISSION", "CONVERTER", "INTEGRATION", "NOTIFICATION_RULE", "NOTIFICATION_TARGET", "NOTIFICATION_TEMPLATE", "TB_RESOURCE", "DEVICE_GROUP_OTA", "OAUTH2_CLIENT", "DOMAIN"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def entity_group_id(self):
        """Gets the entity_group_id of this EdgeEvent.  # noqa: E501


        :return: The entity_group_id of this EdgeEvent.  # noqa: E501
        :rtype: str
        """
        return self._entity_group_id

    @entity_group_id.setter
    def entity_group_id(self, entity_group_id):
        """Sets the entity_group_id of this EdgeEvent.


        :param entity_group_id: The entity_group_id of this EdgeEvent.  # noqa: E501
        :type: str
        """

        self._entity_group_id = entity_group_id

    @property
    def body(self):
        """Gets the body of this EdgeEvent.  # noqa: E501


        :return: The body of this EdgeEvent.  # noqa: E501
        :rtype: JsonNode
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this EdgeEvent.


        :param body: The body of this EdgeEvent.  # noqa: E501
        :type: JsonNode
        """

        self._body = body

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
        if issubclass(EdgeEvent, dict):
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
        if not isinstance(other, EdgeEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
