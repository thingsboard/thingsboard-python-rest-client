# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.1.0
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


class ComponentDescriptorControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_component_descriptor_by_clazz_using_get(self, component_descriptor_clazz, **kwargs):  # noqa: E501
        """Get Component Descriptor (getComponentDescriptorByClazz)  # noqa: E501

        Gets the Component Descriptor object using class name from the path parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptor_by_clazz_using_get(component_descriptor_clazz, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_descriptor_clazz: Component Descriptor class name (required)
        :return: ComponentDescriptor
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_descriptor_by_clazz_using_get_with_http_info(component_descriptor_clazz, **kwargs)  # noqa: E501
        else:
            (data) = self.get_component_descriptor_by_clazz_using_get_with_http_info(component_descriptor_clazz, **kwargs)  # noqa: E501
            return data

    def get_component_descriptor_by_clazz_using_get_with_http_info(self, component_descriptor_clazz, **kwargs):  # noqa: E501
        """Get Component Descriptor (getComponentDescriptorByClazz)  # noqa: E501

        Gets the Component Descriptor object using class name from the path parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptor_by_clazz_using_get_with_http_info(component_descriptor_clazz, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_descriptor_clazz: Component Descriptor class name (required)
        :return: ComponentDescriptor
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_descriptor_clazz']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_component_descriptor_by_clazz_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'component_descriptor_clazz' is set
        if ('component_descriptor_clazz' not in params or
                params['component_descriptor_clazz'] is None):
            raise ValueError("Missing the required parameter `component_descriptor_clazz` when calling `get_component_descriptor_by_clazz_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'component_descriptor_clazz' in params:
            path_params['componentDescriptorClazz'] = params['component_descriptor_clazz']  # noqa: E501

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
            '/api/component/{componentDescriptorClazz}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComponentDescriptor',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_component_descriptors_by_type_using_get(self, component_type, **kwargs):  # noqa: E501
        """Get Component Descriptors (getComponentDescriptorsByType)  # noqa: E501

        Gets the Component Descriptors using rule node type and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptors_by_type_using_get(component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: Type of the Rule Node (required)
        :param str rule_chain_type: Type of the Rule Chain
        :return: list[ComponentDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_descriptors_by_type_using_get_with_http_info(component_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_component_descriptors_by_type_using_get_with_http_info(component_type, **kwargs)  # noqa: E501
            return data

    def get_component_descriptors_by_type_using_get_with_http_info(self, component_type, **kwargs):  # noqa: E501
        """Get Component Descriptors (getComponentDescriptorsByType)  # noqa: E501

        Gets the Component Descriptors using rule node type and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptors_by_type_using_get_with_http_info(component_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_type: Type of the Rule Node (required)
        :param str rule_chain_type: Type of the Rule Chain
        :return: list[ComponentDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_type', 'rule_chain_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_component_descriptors_by_type_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'component_type' is set
        if ('component_type' not in params or
                params['component_type'] is None):
            raise ValueError("Missing the required parameter `component_type` when calling `get_component_descriptors_by_type_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'component_type' in params:
            path_params['componentType'] = params['component_type']  # noqa: E501

        query_params = []
        if 'rule_chain_type' in params:
            query_params.append(('ruleChainType', params['rule_chain_type']))  # noqa: E501

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
            '/api/components/{componentType}{?ruleChainType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ComponentDescriptor]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_component_descriptors_by_types_using_get(self, component_types, **kwargs):  # noqa: E501
        """Get Component Descriptors (getComponentDescriptorsByTypes)  # noqa: E501

        Gets the Component Descriptors using coma separated list of rule node types and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptors_by_types_using_get(component_types, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_types: List of types of the Rule Nodes, (ENRICHMENT, FILTER, TRANSFORMATION, ACTION or EXTERNAL) (required)
        :param str rule_chain_type: Type of the Rule Chain
        :return: list[ComponentDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_component_descriptors_by_types_using_get_with_http_info(component_types, **kwargs)  # noqa: E501
        else:
            (data) = self.get_component_descriptors_by_types_using_get_with_http_info(component_types, **kwargs)  # noqa: E501
            return data

    def get_component_descriptors_by_types_using_get_with_http_info(self, component_types, **kwargs):  # noqa: E501
        """Get Component Descriptors (getComponentDescriptorsByTypes)  # noqa: E501

        Gets the Component Descriptors using coma separated list of rule node types and optional rule chain type request parameters. Each Component Descriptor represents configuration of specific rule node (e.g. 'Save Timeseries' or 'Send Email'.). The Component Descriptors are used by the rule chain Web UI to build the configuration forms for the rule nodes. The Component Descriptors are discovered at runtime by scanning the class path and searching for @RuleNode annotation. Once discovered, the up to date list of descriptors is persisted to the database.  Available for users with 'SYS_ADMIN' or 'TENANT_ADMIN' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_component_descriptors_by_types_using_get_with_http_info(component_types, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str component_types: List of types of the Rule Nodes, (ENRICHMENT, FILTER, TRANSFORMATION, ACTION or EXTERNAL) (required)
        :param str rule_chain_type: Type of the Rule Chain
        :return: list[ComponentDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['component_types', 'rule_chain_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_component_descriptors_by_types_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'component_types' is set
        if ('component_types' not in params or
                params['component_types'] is None):
            raise ValueError("Missing the required parameter `component_types` when calling `get_component_descriptors_by_types_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'component_types' in params:
            query_params.append(('componentTypes', params['component_types']))  # noqa: E501
        if 'rule_chain_type' in params:
            query_params.append(('ruleChainType', params['rule_chain_type']))  # noqa: E501

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
            '/api/components{?componentTypes,ruleChainType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ComponentDescriptor]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
