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
from swagger_client.models.entity_filter import EntityFilter  # noqa: F401,E501

class RelationsQueryFilter(EntityFilter):
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
        'direction': 'str',
        'fetch_last_level_only': 'bool',
        'filters': 'list[RelationEntityTypeFilter]',
        'max_level': 'int',
        'multi_root': 'bool',
        'multi_root_entities_type': 'str',
        'multi_root_entity_ids': 'list[str]',
        'root_entity': 'EntityId'
    }
    if hasattr(EntityFilter, "swagger_types"):
        swagger_types.update(EntityFilter.swagger_types)

    attribute_map = {
        'direction': 'direction',
        'fetch_last_level_only': 'fetchLastLevelOnly',
        'filters': 'filters',
        'max_level': 'maxLevel',
        'multi_root': 'multiRoot',
        'multi_root_entities_type': 'multiRootEntitiesType',
        'multi_root_entity_ids': 'multiRootEntityIds',
        'root_entity': 'rootEntity'
    }
    if hasattr(EntityFilter, "attribute_map"):
        attribute_map.update(EntityFilter.attribute_map)

    def __init__(self, direction=None, fetch_last_level_only=None, filters=None, max_level=None, multi_root=None, multi_root_entities_type=None, multi_root_entity_ids=None, root_entity=None, *args, **kwargs):  # noqa: E501
        """RelationsQueryFilter - a model defined in Swagger"""  # noqa: E501
        self._direction = None
        self._fetch_last_level_only = None
        self._filters = None
        self._max_level = None
        self._multi_root = None
        self._multi_root_entities_type = None
        self._multi_root_entity_ids = None
        self._root_entity = None
        self.discriminator = None
        if direction is not None:
            self.direction = direction
        if fetch_last_level_only is not None:
            self.fetch_last_level_only = fetch_last_level_only
        if filters is not None:
            self.filters = filters
        if max_level is not None:
            self.max_level = max_level
        if multi_root is not None:
            self.multi_root = multi_root
        if multi_root_entities_type is not None:
            self.multi_root_entities_type = multi_root_entities_type
        if multi_root_entity_ids is not None:
            self.multi_root_entity_ids = multi_root_entity_ids
        if root_entity is not None:
            self.root_entity = root_entity
        EntityFilter.__init__(self, *args, **kwargs)

    @property
    def direction(self):
        """Gets the direction of this RelationsQueryFilter.  # noqa: E501


        :return: The direction of this RelationsQueryFilter.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this RelationsQueryFilter.


        :param direction: The direction of this RelationsQueryFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["FROM", "TO"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"  # noqa: E501
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def fetch_last_level_only(self):
        """Gets the fetch_last_level_only of this RelationsQueryFilter.  # noqa: E501


        :return: The fetch_last_level_only of this RelationsQueryFilter.  # noqa: E501
        :rtype: bool
        """
        return self._fetch_last_level_only

    @fetch_last_level_only.setter
    def fetch_last_level_only(self, fetch_last_level_only):
        """Sets the fetch_last_level_only of this RelationsQueryFilter.


        :param fetch_last_level_only: The fetch_last_level_only of this RelationsQueryFilter.  # noqa: E501
        :type: bool
        """

        self._fetch_last_level_only = fetch_last_level_only

    @property
    def filters(self):
        """Gets the filters of this RelationsQueryFilter.  # noqa: E501


        :return: The filters of this RelationsQueryFilter.  # noqa: E501
        :rtype: list[RelationEntityTypeFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this RelationsQueryFilter.


        :param filters: The filters of this RelationsQueryFilter.  # noqa: E501
        :type: list[RelationEntityTypeFilter]
        """

        self._filters = filters

    @property
    def max_level(self):
        """Gets the max_level of this RelationsQueryFilter.  # noqa: E501


        :return: The max_level of this RelationsQueryFilter.  # noqa: E501
        :rtype: int
        """
        return self._max_level

    @max_level.setter
    def max_level(self, max_level):
        """Sets the max_level of this RelationsQueryFilter.


        :param max_level: The max_level of this RelationsQueryFilter.  # noqa: E501
        :type: int
        """

        self._max_level = max_level

    @property
    def multi_root(self):
        """Gets the multi_root of this RelationsQueryFilter.  # noqa: E501


        :return: The multi_root of this RelationsQueryFilter.  # noqa: E501
        :rtype: bool
        """
        return self._multi_root

    @multi_root.setter
    def multi_root(self, multi_root):
        """Sets the multi_root of this RelationsQueryFilter.


        :param multi_root: The multi_root of this RelationsQueryFilter.  # noqa: E501
        :type: bool
        """

        self._multi_root = multi_root

    @property
    def multi_root_entities_type(self):
        """Gets the multi_root_entities_type of this RelationsQueryFilter.  # noqa: E501


        :return: The multi_root_entities_type of this RelationsQueryFilter.  # noqa: E501
        :rtype: str
        """
        return self._multi_root_entities_type

    @multi_root_entities_type.setter
    def multi_root_entities_type(self, multi_root_entities_type):
        """Sets the multi_root_entities_type of this RelationsQueryFilter.


        :param multi_root_entities_type: The multi_root_entities_type of this RelationsQueryFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "API_USAGE_STATE", "ASSET", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_VIEW", "OTA_PACKAGE", "QUEUE", "RPC", "RULE_CHAIN", "RULE_NODE", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if multi_root_entities_type not in allowed_values:
            raise ValueError(
                "Invalid value for `multi_root_entities_type` ({0}), must be one of {1}"  # noqa: E501
                .format(multi_root_entities_type, allowed_values)
            )

        self._multi_root_entities_type = multi_root_entities_type

    @property
    def multi_root_entity_ids(self):
        """Gets the multi_root_entity_ids of this RelationsQueryFilter.  # noqa: E501


        :return: The multi_root_entity_ids of this RelationsQueryFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._multi_root_entity_ids

    @multi_root_entity_ids.setter
    def multi_root_entity_ids(self, multi_root_entity_ids):
        """Sets the multi_root_entity_ids of this RelationsQueryFilter.


        :param multi_root_entity_ids: The multi_root_entity_ids of this RelationsQueryFilter.  # noqa: E501
        :type: list[str]
        """

        self._multi_root_entity_ids = multi_root_entity_ids

    @property
    def root_entity(self):
        """Gets the root_entity of this RelationsQueryFilter.  # noqa: E501


        :return: The root_entity of this RelationsQueryFilter.  # noqa: E501
        :rtype: EntityId
        """
        return self._root_entity

    @root_entity.setter
    def root_entity(self, root_entity):
        """Sets the root_entity of this RelationsQueryFilter.


        :param root_entity: The root_entity of this RelationsQueryFilter.  # noqa: E501
        :type: EntityId
        """

        self._root_entity = root_entity

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
        if issubclass(RelationsQueryFilter, dict):
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
        if not isinstance(other, RelationsQueryFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
