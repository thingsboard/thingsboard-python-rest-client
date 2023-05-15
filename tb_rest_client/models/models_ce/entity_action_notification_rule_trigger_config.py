# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0-SNAPSHOT
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EntityActionNotificationRuleTriggerConfig(object):
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
        'created': 'bool',
        'deleted': 'bool',
        'entity_types': 'list[str]',
        'trigger_type': 'str',
        'updated': 'bool'
    }

    attribute_map = {
        'created': 'created',
        'deleted': 'deleted',
        'entity_types': 'entityTypes',
        'trigger_type': 'triggerType',
        'updated': 'updated'
    }

    def __init__(self, created=None, deleted=None, entity_types=None, trigger_type=None, updated=None):  # noqa: E501
        """EntityActionNotificationRuleTriggerConfig - a model defined in Swagger"""  # noqa: E501
        self._created = None
        self._deleted = None
        self._entity_types = None
        self._trigger_type = None
        self._updated = None
        self.discriminator = None
        if created is not None:
            self.created = created
        if deleted is not None:
            self.deleted = deleted
        if entity_types is not None:
            self.entity_types = entity_types
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501


        :return: The created of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this EntityActionNotificationRuleTriggerConfig.


        :param created: The created of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501
        :type: bool
        """

        self._created = created

    @property
    def deleted(self):
        """Gets the deleted of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501


        :return: The deleted of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this EntityActionNotificationRuleTriggerConfig.


        :param deleted: The deleted of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def entity_types(self):
        """Gets the entity_types of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501


        :return: The entity_types of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._entity_types

    @entity_types.setter
    def entity_types(self, entity_types):
        """Sets the entity_types of this EntityActionNotificationRuleTriggerConfig.


        :param entity_types: The entity_types of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ALARM", "API_USAGE_STATE", "ASSET", "ASSET_PROFILE", "CUSTOMER", "DASHBOARD", "DEVICE", "DEVICE_PROFILE", "EDGE", "ENTITY_VIEW", "NOTIFICATION", "NOTIFICATION_REQUEST", "NOTIFICATION_RULE", "NOTIFICATION_TARGET", "NOTIFICATION_TEMPLATE", "OTA_PACKAGE", "QUEUE", "RPC", "RULE_CHAIN", "RULE_NODE", "TB_RESOURCE", "TENANT", "TENANT_PROFILE", "USER", "WIDGETS_BUNDLE", "WIDGET_TYPE"]  # noqa: E501
        if not set(entity_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `entity_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(entity_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._entity_types = entity_types

    @property
    def trigger_type(self):
        """Gets the trigger_type of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501


        :return: The trigger_type of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this EntityActionNotificationRuleTriggerConfig.


        :param trigger_type: The trigger_type of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501
        :type: str
        """
        allowed_values = ["ALARM", "ALARM_ASSIGNMENT", "ALARM_COMMENT", "API_USAGE_LIMIT", "DEVICE_ACTIVITY", "ENTITIES_LIMIT", "ENTITY_ACTION", "NEW_PLATFORM_VERSION", "RULE_ENGINE_COMPONENT_LIFECYCLE_EVENT"]  # noqa: E501
        if trigger_type not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_type` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_type, allowed_values)
            )

        self._trigger_type = trigger_type

    @property
    def updated(self):
        """Gets the updated of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501


        :return: The updated of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501
        :rtype: bool
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this EntityActionNotificationRuleTriggerConfig.


        :param updated: The updated of this EntityActionNotificationRuleTriggerConfig.  # noqa: E501
        :type: bool
        """

        self._updated = updated

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
        if issubclass(EntityActionNotificationRuleTriggerConfig, dict):
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
        if not isinstance(other, EntityActionNotificationRuleTriggerConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other