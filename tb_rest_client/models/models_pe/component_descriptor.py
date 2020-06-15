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

from tb_rest_client.models.models_ce import ComponentDescriptor

class ComponentDescriptor(ComponentDescriptor):
    def __init__(self, actions=None, clazz=None, configuration_descriptor=None, created_time=None, id=None, name=None, scope=None, type=None):  # noqa: E501
        super().__init(actions, clazz, configuration_descriptor, created_time, id, name, scope, type)
        self._type = None
        if type is not None:
            self.type = type

    @property
    def type(self):
        """Gets the type of this ComponentDescriptor.  # noqa: E501


        :return: The type of this ComponentDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComponentDescriptor.


        :param type: The type of this ComponentDescriptor.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENRICHMENT", "FILTER", "TRANSFORMATION", "ACTION", "ANALYTICS", "EXTERNAL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type
