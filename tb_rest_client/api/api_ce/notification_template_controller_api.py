# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.0.0
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

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from tb_rest_client.api_client import ApiClient


class NotificationTemplateControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_notification_template_by_id_using_delete(self, id, **kwargs):  # noqa: E501
        """Delete notification template by id (deleteNotificationTemplateById  # noqa: E501

        Deletes notification template by its id.  This template cannot be referenced by existing scheduled notification requests or any notification rules.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_notification_template_by_id_using_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_notification_template_by_id_using_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_notification_template_by_id_using_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_notification_template_by_id_using_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """Delete notification template by id (deleteNotificationTemplateById  # noqa: E501

        Deletes notification template by its id.  This template cannot be referenced by existing scheduled notification requests or any notification rules.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_notification_template_by_id_using_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_notification_template_by_id_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_notification_template_by_id_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/notification/template/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_notification_template_by_id_using_get(self, id, **kwargs):  # noqa: E501
        """Get notification template by id (getNotificationTemplateById)  # noqa: E501

        Fetches notification template by id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_template_by_id_using_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :return: NotificationTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_notification_template_by_id_using_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_notification_template_by_id_using_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_notification_template_by_id_using_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get notification template by id (getNotificationTemplateById)  # noqa: E501

        Fetches notification template by id.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_template_by_id_using_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: id (required)
        :return: NotificationTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notification_template_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_notification_template_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/notification/template/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotificationTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_notification_templates_using_get(self, page_size, page, **kwargs):  # noqa: E501
        """Get notification templates (getNotificationTemplates)  # noqa: E501

        Returns the page of notification templates owned by sysadmin or tenant.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_templates_using_get(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: Case-insensitive 'substring' filter based on template's name and notification type
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param str notification_types: Comma-separated list of notification types to filter the templates
        :return: PageDataNotificationTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_notification_templates_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_notification_templates_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_notification_templates_using_get_with_http_info(self, page_size, page, **kwargs):  # noqa: E501
        """Get notification templates (getNotificationTemplates)  # noqa: E501

        Returns the page of notification templates owned by sysadmin or tenant.  You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_notification_templates_using_get_with_http_info(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str text_search: Case-insensitive 'substring' filter based on template's name and notification type
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param str notification_types: Comma-separated list of notification types to filter the templates
        :return: PageDataNotificationTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', 'text_search', 'sort_property', 'sort_order', 'notification_types']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_notification_templates_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_notification_templates_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_notification_templates_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'notification_types' in params:
            query_params.append(('notificationTypes', params['notification_types']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/notification/templates{?notificationTypes,page,pageSize,sortOrder,sortProperty,textSearch}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataNotificationTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_slack_conversations_using_get(self, type, **kwargs):  # noqa: E501
        """List Slack conversations (listSlackConversations)  # noqa: E501

        List available Slack conversations by type.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_slack_conversations_using_get(type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: type (required)
        :param str token: Slack bot token. If absent - system Slack settings will be used
        :return: list[SlackConversation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_slack_conversations_using_get_with_http_info(type, **kwargs)  # noqa: E501
        else:
            (data) = self.list_slack_conversations_using_get_with_http_info(type, **kwargs)  # noqa: E501
            return data

    def list_slack_conversations_using_get_with_http_info(self, type, **kwargs):  # noqa: E501
        """List Slack conversations (listSlackConversations)  # noqa: E501

        List available Slack conversations by type.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_slack_conversations_using_get_with_http_info(type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: type (required)
        :param str token: Slack bot token. If absent - system Slack settings will be used
        :return: list[SlackConversation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_slack_conversations_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `list_slack_conversations_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'token' in params:
            query_params.append(('token', params['token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/notification/slack/conversations{?token,type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[SlackConversation]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def save_notification_template_using_post(self, **kwargs):  # noqa: E501
        """Save notification template (saveNotificationTemplate)  # noqa: E501

        Creates or updates notification template.  Here is an example of template to send notification via Web, SMS and Slack: ```json {   \"name\": \"Greetings\",   \"notificationType\": \"GENERAL\",   \"configuration\": {     \"deliveryMethodsTemplates\": {       \"WEB\": {         \"enabled\": true,         \"subject\": \"Greetings\",         \"body\": \"Hi there, ${recipientTitle}\",         \"additionalConfig\": {           \"icon\": {             \"enabled\": true,             \"icon\": \"back_hand\",             \"color\": \"#757575\"           },           \"actionButtonConfig\": {             \"enabled\": false           }         },         \"method\": \"WEB\"       },       \"SMS\": {         \"enabled\": true,         \"body\": \"Hi there, ${recipientTitle}\",         \"method\": \"SMS\"       },       \"SLACK\": {         \"enabled\": true,         \"body\": \"Hi there, @${recipientTitle}\",         \"method\": \"SLACK\"       }     }   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_notification_template_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NotificationTemplate body:
        :return: NotificationTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_notification_template_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.save_notification_template_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def save_notification_template_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Save notification template (saveNotificationTemplate)  # noqa: E501

        Creates or updates notification template.  Here is an example of template to send notification via Web, SMS and Slack: ```json {   \"name\": \"Greetings\",   \"notificationType\": \"GENERAL\",   \"configuration\": {     \"deliveryMethodsTemplates\": {       \"WEB\": {         \"enabled\": true,         \"subject\": \"Greetings\",         \"body\": \"Hi there, ${recipientTitle}\",         \"additionalConfig\": {           \"icon\": {             \"enabled\": true,             \"icon\": \"back_hand\",             \"color\": \"#757575\"           },           \"actionButtonConfig\": {             \"enabled\": false           }         },         \"method\": \"WEB\"       },       \"SMS\": {         \"enabled\": true,         \"body\": \"Hi there, ${recipientTitle}\",         \"method\": \"SMS\"       },       \"SLACK\": {         \"enabled\": true,         \"body\": \"Hi there, @${recipientTitle}\",         \"method\": \"SLACK\"       }     }   } } ```  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_notification_template_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NotificationTemplate body:
        :return: NotificationTemplate
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_notification_template_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/notification/template', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NotificationTemplate',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
