# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.7.0PE
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2024. ThingsBoard
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


class RuleEngineControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def handle_rule_engine_request_using_post(self, entity_type, entity_id, timeout, **kwargs):  # noqa: E501
        """Push entity message with timeout to the rule engine (handleRuleEngineRequest)  # noqa: E501

        Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The platform expects the timeout value in milliseconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_rule_engine_request_using_post(entity_type, entity_id, timeout, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int timeout: Timeout to process the request in milliseconds (required)
        :param str body:
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_rule_engine_request_using_post_with_http_info(entity_type, entity_id, timeout, **kwargs)  # noqa: E501
        else:
            (data) = self.handle_rule_engine_request_using_post_with_http_info(entity_type, entity_id, timeout, **kwargs)  # noqa: E501
            return data

    def handle_rule_engine_request_using_post_with_http_info(self, entity_type, entity_id, timeout, **kwargs):  # noqa: E501
        """Push entity message with timeout to the rule engine (handleRuleEngineRequest)  # noqa: E501

        Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The platform expects the timeout value in milliseconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_rule_engine_request_using_post_with_http_info(entity_type, entity_id, timeout, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param int timeout: Timeout to process the request in milliseconds (required)
        :param str body:
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'timeout', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handle_rule_engine_request_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `handle_rule_engine_request_using_post`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `handle_rule_engine_request_using_post`")  # noqa: E501
        # verify the required parameter 'timeout' is set
        if ('timeout' not in params or
                params['timeout'] is None):
            raise ValueError("Missing the required parameter `timeout` when calling `handle_rule_engine_request_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501
        if 'timeout' in params:
            path_params['timeout'] = params['timeout']  # noqa: E501

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
            '/api/rule-engine/{entityType}/{entityId}/{timeout}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def handle_rule_engine_request_using_post1(self, entity_type, entity_id, queue_name, timeout, **kwargs):  # noqa: E501
        """Push entity message with timeout and specified queue to the rule engine (handleRuleEngineRequest)  # noqa: E501

        Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. If request sent for Device/Device Profile or Asset/Asset Profile entity, specified queue will be used instead of the queue selected in the device or asset profile. The platform expects the timeout value in milliseconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_rule_engine_request_using_post1(entity_type, entity_id, queue_name, timeout, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param str queue_name: Queue name to process the request in the rule engine (required)
        :param int timeout: Timeout to process the request in milliseconds (required)
        :param str body:
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_rule_engine_request_using_post1_with_http_info(entity_type, entity_id, queue_name, timeout, **kwargs)  # noqa: E501
        else:
            (data) = self.handle_rule_engine_request_using_post1_with_http_info(entity_type, entity_id, queue_name, timeout, **kwargs)  # noqa: E501
            return data

    def handle_rule_engine_request_using_post1_with_http_info(self, entity_type, entity_id, queue_name, timeout, **kwargs):  # noqa: E501
        """Push entity message with timeout and specified queue to the rule engine (handleRuleEngineRequest)  # noqa: E501

        Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. If request sent for Device/Device Profile or Asset/Asset Profile entity, specified queue will be used instead of the queue selected in the device or asset profile. The platform expects the timeout value in milliseconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_rule_engine_request_using_post1_with_http_info(entity_type, entity_id, queue_name, timeout, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param str queue_name: Queue name to process the request in the rule engine (required)
        :param int timeout: Timeout to process the request in milliseconds (required)
        :param str body:
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'queue_name', 'timeout', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handle_rule_engine_request_using_post1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `handle_rule_engine_request_using_post1`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `handle_rule_engine_request_using_post1`")  # noqa: E501
        # verify the required parameter 'queue_name' is set
        if ('queue_name' not in params or
                params['queue_name'] is None):
            raise ValueError("Missing the required parameter `queue_name` when calling `handle_rule_engine_request_using_post1`")  # noqa: E501
        # verify the required parameter 'timeout' is set
        if ('timeout' not in params or
                params['timeout'] is None):
            raise ValueError("Missing the required parameter `timeout` when calling `handle_rule_engine_request_using_post1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501
        if 'queue_name' in params:
            path_params['queueName'] = params['queue_name']  # noqa: E501
        if 'timeout' in params:
            path_params['timeout'] = params['timeout']  # noqa: E501

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
            '/api/rule-engine/{entityType}/{entityId}/{queueName}/{timeout}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def handle_rule_engine_request_using_post2(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """Push entity message to the rule engine (handleRuleEngineRequest)  # noqa: E501

        Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The default timeout of the request processing is 10 seconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_rule_engine_request_using_post2(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param str body:
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_rule_engine_request_using_post2_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.handle_rule_engine_request_using_post2_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
            return data

    def handle_rule_engine_request_using_post2_with_http_info(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """Push entity message to the rule engine (handleRuleEngineRequest)  # noqa: E501

        Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses specified Entity Id as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The default timeout of the request processing is 10 seconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_rule_engine_request_using_post2_with_http_info(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: A string value representing the entity type. For example, 'DEVICE' (required)
        :param str entity_id: A string value representing the entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :param str body:
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method handle_rule_engine_request_using_post2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `handle_rule_engine_request_using_post2`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `handle_rule_engine_request_using_post2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entityType'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entityId'] = params['entity_id']  # noqa: E501

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
            '/api/rule-engine/{entityType}/{entityId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def handle_rule_engine_request_using_post3(self, **kwargs):  # noqa: E501
        """Push user message to the rule engine (handleRuleEngineRequest)  # noqa: E501

        Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses current User Id ( the one which credentials is used to perform the request) as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The default timeout of the request processing is 10 seconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_rule_engine_request_using_post3(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body:
        :return: DeferredResultResponseEntity
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.handle_rule_engine_request_using_post3_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.handle_rule_engine_request_using_post3_with_http_info(**kwargs)  # noqa: E501
            return data

    def handle_rule_engine_request_using_post3_with_http_info(self, **kwargs):  # noqa: E501
        """Push user message to the rule engine (handleRuleEngineRequest)  # noqa: E501

        Creates the Message with type 'REST_API_REQUEST' and payload taken from the request body. Uses current User Id ( the one which credentials is used to perform the request) as the Rule Engine message originator. This method allows you to extend the regular platform API with the power of Rule Engine. You may use default and custom rule nodes to handle the message. The generated message contains two important metadata fields:   * **'serviceId'** to identify the platform server that received the request;  * **'requestUUID'** to identify the request and route possible response from the Rule Engine;  Use **'rest call reply'** rule node to push the reply from rule engine back as a REST API call response. The default timeout of the request processing is 10 seconds.   Security check is performed to verify that the user has 'WRITE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.handle_rule_engine_request_using_post3_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body:
        :return: DeferredResultResponseEntity
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
                    " to method handle_rule_engine_request_using_post3" % key
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
            '/api/rule-engine/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeferredResultResponseEntity',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
