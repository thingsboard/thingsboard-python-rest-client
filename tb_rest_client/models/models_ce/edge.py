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


class Edge(object):
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
        'cloud_endpoint': 'str',
        'created_time': 'int',
        'customer_id': 'CustomerId',
        'edge_license_key': 'str',
        'id': 'EdgeId',
        'label': 'str',
        'name': 'str',
        'root_rule_chain_id': 'RuleChainId',
        'routing_key': 'str',
        'secret': 'str',
        'tenant_id': 'TenantId',
        'type': 'str'
    }

    attribute_map = {
        'additional_info': 'additionalInfo',
        'cloud_endpoint': 'cloudEndpoint',
        'created_time': 'createdTime',
        'customer_id': 'customerId',
        'edge_license_key': 'edgeLicenseKey',
        'id': 'id',
        'label': 'label',
        'name': 'name',
        'root_rule_chain_id': 'rootRuleChainId',
        'routing_key': 'routingKey',
        'secret': 'secret',
        'tenant_id': 'tenantId',
        'type': 'type'
    }

    def __init__(self, additional_info=None, cloud_endpoint=None, created_time=None, customer_id=None, edge_license_key=None, id=None, label=None, name=None, root_rule_chain_id=None, routing_key=None, secret=None, tenant_id=None, type=None, _configuration=None):  # noqa: E501
        """Edge - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._additional_info = None
        self._cloud_endpoint = None
        self._created_time = None
        self._customer_id = None
        self._edge_license_key = None
        self._id = None
        self._label = None
        self._name = None
        self._root_rule_chain_id = None
        self._routing_key = None
        self._secret = None
        self._tenant_id = None
        self._type = None
        self.discriminator = None

        if additional_info is not None:
            self.additional_info = additional_info
        if cloud_endpoint is not None:
            self.cloud_endpoint = cloud_endpoint
        if created_time is not None:
            self.created_time = created_time
        if customer_id is not None:
            self.customer_id = customer_id
        if edge_license_key is not None:
            self.edge_license_key = edge_license_key
        if id is not None:
            self.id = id
        if label is not None:
            self.label = label
        if name is not None:
            self.name = name
        if root_rule_chain_id is not None:
            self.root_rule_chain_id = root_rule_chain_id
        if routing_key is not None:
            self.routing_key = routing_key
        if secret is not None:
            self.secret = secret
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if type is not None:
            self.type = type

    @property
    def additional_info(self):
        """Gets the additional_info of this Edge.  # noqa: E501


        :return: The additional_info of this Edge.  # noqa: E501
        :rtype: str
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """Sets the additional_info of this Edge.


        :param additional_info: The additional_info of this Edge.  # noqa: E501
        :type: str
        """

        self._additional_info = additional_info

    @property
    def cloud_endpoint(self):
        """Gets the cloud_endpoint of this Edge.  # noqa: E501


        :return: The cloud_endpoint of this Edge.  # noqa: E501
        :rtype: str
        """
        return self._cloud_endpoint

    @cloud_endpoint.setter
    def cloud_endpoint(self, cloud_endpoint):
        """Sets the cloud_endpoint of this Edge.


        :param cloud_endpoint: The cloud_endpoint of this Edge.  # noqa: E501
        :type: str
        """

        self._cloud_endpoint = cloud_endpoint

    @property
    def created_time(self):
        """Gets the created_time of this Edge.  # noqa: E501


        :return: The created_time of this Edge.  # noqa: E501
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        """Sets the created_time of this Edge.


        :param created_time: The created_time of this Edge.  # noqa: E501
        :type: int
        """

        self._created_time = created_time

    @property
    def customer_id(self):
        """Gets the customer_id of this Edge.  # noqa: E501


        :return: The customer_id of this Edge.  # noqa: E501
        :rtype: CustomerId
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Edge.


        :param customer_id: The customer_id of this Edge.  # noqa: E501
        :type: CustomerId
        """

        self._customer_id = customer_id

    @property
    def edge_license_key(self):
        """Gets the edge_license_key of this Edge.  # noqa: E501


        :return: The edge_license_key of this Edge.  # noqa: E501
        :rtype: str
        """
        return self._edge_license_key

    @edge_license_key.setter
    def edge_license_key(self, edge_license_key):
        """Sets the edge_license_key of this Edge.


        :param edge_license_key: The edge_license_key of this Edge.  # noqa: E501
        :type: str
        """

        self._edge_license_key = edge_license_key

    @property
    def id(self):
        """Gets the id of this Edge.  # noqa: E501


        :return: The id of this Edge.  # noqa: E501
        :rtype: EdgeId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Edge.


        :param id: The id of this Edge.  # noqa: E501
        :type: EdgeId
        """

        self._id = id

    @property
    def label(self):
        """Gets the label of this Edge.  # noqa: E501


        :return: The label of this Edge.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Edge.


        :param label: The label of this Edge.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this Edge.  # noqa: E501


        :return: The name of this Edge.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Edge.


        :param name: The name of this Edge.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def root_rule_chain_id(self):
        """Gets the root_rule_chain_id of this Edge.  # noqa: E501


        :return: The root_rule_chain_id of this Edge.  # noqa: E501
        :rtype: RuleChainId
        """
        return self._root_rule_chain_id

    @root_rule_chain_id.setter
    def root_rule_chain_id(self, root_rule_chain_id):
        """Sets the root_rule_chain_id of this Edge.


        :param root_rule_chain_id: The root_rule_chain_id of this Edge.  # noqa: E501
        :type: RuleChainId
        """

        self._root_rule_chain_id = root_rule_chain_id

    @property
    def routing_key(self):
        """Gets the routing_key of this Edge.  # noqa: E501


        :return: The routing_key of this Edge.  # noqa: E501
        :rtype: str
        """
        return self._routing_key

    @routing_key.setter
    def routing_key(self, routing_key):
        """Sets the routing_key of this Edge.


        :param routing_key: The routing_key of this Edge.  # noqa: E501
        :type: str
        """

        self._routing_key = routing_key

    @property
    def secret(self):
        """Gets the secret of this Edge.  # noqa: E501


        :return: The secret of this Edge.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this Edge.


        :param secret: The secret of this Edge.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Edge.  # noqa: E501


        :return: The tenant_id of this Edge.  # noqa: E501
        :rtype: TenantId
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Edge.


        :param tenant_id: The tenant_id of this Edge.  # noqa: E501
        :type: TenantId
        """

        self._tenant_id = tenant_id

    @property
    def type(self):
        """Gets the type of this Edge.  # noqa: E501


        :return: The type of this Edge.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Edge.


        :param type: The type of this Edge.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(Edge, dict):
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
        if not isinstance(other, Edge):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Edge):
            return True

        return self.to_dict() != other.to_dict()