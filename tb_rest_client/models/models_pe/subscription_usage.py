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


class SubscriptionUsage(object):
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
        'assets': 'int',
        'converters': 'int',
        'customers': 'int',
        'dashboards': 'int',
        'devices': 'int',
        'dp_storage_days': 'int',
        'emails': 'int',
        'integrations': 'int',
        'js_executions': 'int',
        're_executions': 'int',
        'rule_chains': 'int',
        'scheduler_events': 'int',
        'sms': 'int',
        'transport_data_points': 'int',
        'transport_messages': 'int',
        'users': 'int'
    }

    attribute_map = {
        'assets': 'assets',
        'converters': 'converters',
        'customers': 'customers',
        'dashboards': 'dashboards',
        'devices': 'devices',
        'dp_storage_days': 'dpStorageDays',
        'emails': 'emails',
        'integrations': 'integrations',
        'js_executions': 'jsExecutions',
        're_executions': 'reExecutions',
        'rule_chains': 'ruleChains',
        'scheduler_events': 'schedulerEvents',
        'sms': 'sms',
        'transport_data_points': 'transportDataPoints',
        'transport_messages': 'transportMessages',
        'users': 'users'
    }

    def __init__(self, assets=None, converters=None, customers=None, dashboards=None, devices=None, dp_storage_days=None, emails=None, integrations=None, js_executions=None, re_executions=None, rule_chains=None, scheduler_events=None, sms=None, transport_data_points=None, transport_messages=None, users=None, _configuration=None):  # noqa: E501
        """SubscriptionUsage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._assets = None
        self._converters = None
        self._customers = None
        self._dashboards = None
        self._devices = None
        self._dp_storage_days = None
        self._emails = None
        self._integrations = None
        self._js_executions = None
        self._re_executions = None
        self._rule_chains = None
        self._scheduler_events = None
        self._sms = None
        self._transport_data_points = None
        self._transport_messages = None
        self._users = None
        self.discriminator = None

        if assets is not None:
            self.assets = assets
        if converters is not None:
            self.converters = converters
        if customers is not None:
            self.customers = customers
        if dashboards is not None:
            self.dashboards = dashboards
        if devices is not None:
            self.devices = devices
        if dp_storage_days is not None:
            self.dp_storage_days = dp_storage_days
        if emails is not None:
            self.emails = emails
        if integrations is not None:
            self.integrations = integrations
        if js_executions is not None:
            self.js_executions = js_executions
        if re_executions is not None:
            self.re_executions = re_executions
        if rule_chains is not None:
            self.rule_chains = rule_chains
        if scheduler_events is not None:
            self.scheduler_events = scheduler_events
        if sms is not None:
            self.sms = sms
        if transport_data_points is not None:
            self.transport_data_points = transport_data_points
        if transport_messages is not None:
            self.transport_messages = transport_messages
        if users is not None:
            self.users = users

    @property
    def assets(self):
        """Gets the assets of this SubscriptionUsage.  # noqa: E501


        :return: The assets of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this SubscriptionUsage.


        :param assets: The assets of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._assets = assets

    @property
    def converters(self):
        """Gets the converters of this SubscriptionUsage.  # noqa: E501


        :return: The converters of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._converters

    @converters.setter
    def converters(self, converters):
        """Sets the converters of this SubscriptionUsage.


        :param converters: The converters of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._converters = converters

    @property
    def customers(self):
        """Gets the customers of this SubscriptionUsage.  # noqa: E501


        :return: The customers of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._customers

    @customers.setter
    def customers(self, customers):
        """Sets the customers of this SubscriptionUsage.


        :param customers: The customers of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._customers = customers

    @property
    def dashboards(self):
        """Gets the dashboards of this SubscriptionUsage.  # noqa: E501


        :return: The dashboards of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """Sets the dashboards of this SubscriptionUsage.


        :param dashboards: The dashboards of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._dashboards = dashboards

    @property
    def devices(self):
        """Gets the devices of this SubscriptionUsage.  # noqa: E501


        :return: The devices of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this SubscriptionUsage.


        :param devices: The devices of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._devices = devices

    @property
    def dp_storage_days(self):
        """Gets the dp_storage_days of this SubscriptionUsage.  # noqa: E501


        :return: The dp_storage_days of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._dp_storage_days

    @dp_storage_days.setter
    def dp_storage_days(self, dp_storage_days):
        """Sets the dp_storage_days of this SubscriptionUsage.


        :param dp_storage_days: The dp_storage_days of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._dp_storage_days = dp_storage_days

    @property
    def emails(self):
        """Gets the emails of this SubscriptionUsage.  # noqa: E501


        :return: The emails of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this SubscriptionUsage.


        :param emails: The emails of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._emails = emails

    @property
    def integrations(self):
        """Gets the integrations of this SubscriptionUsage.  # noqa: E501


        :return: The integrations of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._integrations

    @integrations.setter
    def integrations(self, integrations):
        """Sets the integrations of this SubscriptionUsage.


        :param integrations: The integrations of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._integrations = integrations

    @property
    def js_executions(self):
        """Gets the js_executions of this SubscriptionUsage.  # noqa: E501


        :return: The js_executions of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._js_executions

    @js_executions.setter
    def js_executions(self, js_executions):
        """Sets the js_executions of this SubscriptionUsage.


        :param js_executions: The js_executions of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._js_executions = js_executions

    @property
    def re_executions(self):
        """Gets the re_executions of this SubscriptionUsage.  # noqa: E501


        :return: The re_executions of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._re_executions

    @re_executions.setter
    def re_executions(self, re_executions):
        """Sets the re_executions of this SubscriptionUsage.


        :param re_executions: The re_executions of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._re_executions = re_executions

    @property
    def rule_chains(self):
        """Gets the rule_chains of this SubscriptionUsage.  # noqa: E501


        :return: The rule_chains of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._rule_chains

    @rule_chains.setter
    def rule_chains(self, rule_chains):
        """Sets the rule_chains of this SubscriptionUsage.


        :param rule_chains: The rule_chains of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._rule_chains = rule_chains

    @property
    def scheduler_events(self):
        """Gets the scheduler_events of this SubscriptionUsage.  # noqa: E501


        :return: The scheduler_events of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._scheduler_events

    @scheduler_events.setter
    def scheduler_events(self, scheduler_events):
        """Sets the scheduler_events of this SubscriptionUsage.


        :param scheduler_events: The scheduler_events of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._scheduler_events = scheduler_events

    @property
    def sms(self):
        """Gets the sms of this SubscriptionUsage.  # noqa: E501


        :return: The sms of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this SubscriptionUsage.


        :param sms: The sms of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._sms = sms

    @property
    def transport_data_points(self):
        """Gets the transport_data_points of this SubscriptionUsage.  # noqa: E501


        :return: The transport_data_points of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._transport_data_points

    @transport_data_points.setter
    def transport_data_points(self, transport_data_points):
        """Sets the transport_data_points of this SubscriptionUsage.


        :param transport_data_points: The transport_data_points of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._transport_data_points = transport_data_points

    @property
    def transport_messages(self):
        """Gets the transport_messages of this SubscriptionUsage.  # noqa: E501


        :return: The transport_messages of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._transport_messages

    @transport_messages.setter
    def transport_messages(self, transport_messages):
        """Sets the transport_messages of this SubscriptionUsage.


        :param transport_messages: The transport_messages of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._transport_messages = transport_messages

    @property
    def users(self):
        """Gets the users of this SubscriptionUsage.  # noqa: E501


        :return: The users of this SubscriptionUsage.  # noqa: E501
        :rtype: int
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this SubscriptionUsage.


        :param users: The users of this SubscriptionUsage.  # noqa: E501
        :type: int
        """

        self._users = users

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
        if issubclass(SubscriptionUsage, dict):
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
        if not isinstance(other, SubscriptionUsage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriptionUsage):
            return True

        return self.to_dict() != other.to_dict()