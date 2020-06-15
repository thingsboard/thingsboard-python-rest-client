# coding: utf-8
#      Copyright 2020. ThingsBoard
#  #
#      Licensed under the Apache License, Version 2.0 (the "License");
#      you may not use this file except in compliance with the License.
#      You may obtain a copy of the License at
#  #
#          http://www.apache.org/licenses/LICENSE-2.0
#  #
#      Unless required by applicable law or agreed to in writing, software
#      distributed under the License is distributed on an "AS IS" BASIS,
#      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#      See the License for the specific language governing permissions and
#      limitations under the License.
#

import pprint
import re  # noqa: F401

import six

from tb_rest_client.models.models_ce import AuditLog


class AuditLog(AuditLog):

    def __init__(self, action_data=None, action_failure_details=None, action_status=None, action_type=None, created_time=None, customer_id=None, entity_id=None, entity_name=None, id=None, tenant_id=None, user_id=None, user_name=None):  # noqa: E501
        super().__init__(action_data, action_failure_details, action_status, action_type, created_time, customer_id, entity_id, entity_name, id, tenant_id, user_id, user_name)
        self._action_data = None
        if action_data is not None:
            self.action_data = action_data

    @property
    def action_type(self):
        """Gets the action_type of this AuditLog.  # noqa: E501


        :return: The action_type of this AuditLog.  # noqa: E501
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this AuditLog.


        :param action_type: The action_type of this AuditLog.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADDED", "DELETED", "UPDATED", "ATTRIBUTES_UPDATED", "ATTRIBUTES_DELETED", "TIMESERIES_DELETED", "RPC_CALL", "CREDENTIALS_UPDATED", "ASSIGNED_TO_CUSTOMER", "UNASSIGNED_FROM_CUSTOMER", "CHANGE_OWNER", "ACTIVATED", "SUSPENDED", "CREDENTIALS_READ", "ATTRIBUTES_READ", "RELATION_ADD_OR_UPDATE", "RELATION_DELETED", "RELATIONS_DELETED", "ALARM_ACK", "ALARM_CLEAR", "ADDED_TO_ENTITY_GROUP", "REMOVED_FROM_ENTITY_GROUP", "REST_API_RULE_ENGINE_CALL", "MADE_PUBLIC", "MADE_PRIVATE", "LOGIN", "LOGOUT", "LOCKOUT"]  # noqa: E501
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_type, allowed_values)
            )

        self._action_type = action_type
