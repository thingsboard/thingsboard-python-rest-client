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

class EntityTypeVersionLoadConfig(object):
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
        'find_existing_entity_by_name': 'bool',
        'load_attributes': 'bool',
        'load_credentials': 'bool',
        'load_relations': 'bool',
        'remove_other_entities': 'bool'
    }

    attribute_map = {
        'find_existing_entity_by_name': 'findExistingEntityByName',
        'load_attributes': 'loadAttributes',
        'load_credentials': 'loadCredentials',
        'load_relations': 'loadRelations',
        'remove_other_entities': 'removeOtherEntities'
    }

    def __init__(self, find_existing_entity_by_name=None, load_attributes=None, load_credentials=None, load_relations=None, remove_other_entities=None):  # noqa: E501
        """EntityTypeVersionLoadConfig - a model defined in Swagger"""  # noqa: E501
        self._find_existing_entity_by_name = None
        self._load_attributes = None
        self._load_credentials = None
        self._load_relations = None
        self._remove_other_entities = None
        self.discriminator = None
        if find_existing_entity_by_name is not None:
            self.find_existing_entity_by_name = find_existing_entity_by_name
        if load_attributes is not None:
            self.load_attributes = load_attributes
        if load_credentials is not None:
            self.load_credentials = load_credentials
        if load_relations is not None:
            self.load_relations = load_relations
        if remove_other_entities is not None:
            self.remove_other_entities = remove_other_entities

    @property
    def find_existing_entity_by_name(self):
        """Gets the find_existing_entity_by_name of this EntityTypeVersionLoadConfig.  # noqa: E501


        :return: The find_existing_entity_by_name of this EntityTypeVersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._find_existing_entity_by_name

    @find_existing_entity_by_name.setter
    def find_existing_entity_by_name(self, find_existing_entity_by_name):
        """Sets the find_existing_entity_by_name of this EntityTypeVersionLoadConfig.


        :param find_existing_entity_by_name: The find_existing_entity_by_name of this EntityTypeVersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._find_existing_entity_by_name = find_existing_entity_by_name

    @property
    def load_attributes(self):
        """Gets the load_attributes of this EntityTypeVersionLoadConfig.  # noqa: E501


        :return: The load_attributes of this EntityTypeVersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_attributes

    @load_attributes.setter
    def load_attributes(self, load_attributes):
        """Sets the load_attributes of this EntityTypeVersionLoadConfig.


        :param load_attributes: The load_attributes of this EntityTypeVersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_attributes = load_attributes

    @property
    def load_credentials(self):
        """Gets the load_credentials of this EntityTypeVersionLoadConfig.  # noqa: E501


        :return: The load_credentials of this EntityTypeVersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_credentials

    @load_credentials.setter
    def load_credentials(self, load_credentials):
        """Sets the load_credentials of this EntityTypeVersionLoadConfig.


        :param load_credentials: The load_credentials of this EntityTypeVersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_credentials = load_credentials

    @property
    def load_relations(self):
        """Gets the load_relations of this EntityTypeVersionLoadConfig.  # noqa: E501


        :return: The load_relations of this EntityTypeVersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._load_relations

    @load_relations.setter
    def load_relations(self, load_relations):
        """Sets the load_relations of this EntityTypeVersionLoadConfig.


        :param load_relations: The load_relations of this EntityTypeVersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._load_relations = load_relations

    @property
    def remove_other_entities(self):
        """Gets the remove_other_entities of this EntityTypeVersionLoadConfig.  # noqa: E501


        :return: The remove_other_entities of this EntityTypeVersionLoadConfig.  # noqa: E501
        :rtype: bool
        """
        return self._remove_other_entities

    @remove_other_entities.setter
    def remove_other_entities(self, remove_other_entities):
        """Sets the remove_other_entities of this EntityTypeVersionLoadConfig.


        :param remove_other_entities: The remove_other_entities of this EntityTypeVersionLoadConfig.  # noqa: E501
        :type: bool
        """

        self._remove_other_entities = remove_other_entities

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
        if issubclass(EntityTypeVersionLoadConfig, dict):
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
        if not isinstance(other, EntityTypeVersionLoadConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
