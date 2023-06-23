# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard open-source IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.5.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

#  Copyright 2023. ThingsBoard
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


class Lwm2mControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_lwm2m_bootstrap_security_info_using_get(self, is_bootstrap_server, **kwargs):  # noqa: E501
        """Get Lwm2m Bootstrap SecurityInfo (getLwm2mBootstrapSecurityInfo)  # noqa: E501

        Get the Lwm2m Bootstrap SecurityInfo object (of the current server) based on the provided isBootstrapServer parameter. If isBootstrapServer == true, get the parameters of the current Bootstrap Server. If isBootstrapServer == false, get the parameters of the current Lwm2m Server. Used for client settings when starting the client in Bootstrap mode.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lwm2m_bootstrap_security_info_using_get(is_bootstrap_server, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_bootstrap_server: A Boolean value representing the Server SecurityInfo for future Bootstrap client mode settings. Values: 'true' for Bootstrap Server; 'false' for Lwm2m Server.  (required)
        :return: LwM2MServerSecurityConfigDefault
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_lwm2m_bootstrap_security_info_using_get_with_http_info(is_bootstrap_server, **kwargs)  # noqa: E501
        else:
            (data) = self.get_lwm2m_bootstrap_security_info_using_get_with_http_info(is_bootstrap_server, **kwargs)  # noqa: E501
            return data

    def get_lwm2m_bootstrap_security_info_using_get_with_http_info(self, is_bootstrap_server, **kwargs):  # noqa: E501
        """Get Lwm2m Bootstrap SecurityInfo (getLwm2mBootstrapSecurityInfo)  # noqa: E501

        Get the Lwm2m Bootstrap SecurityInfo object (of the current server) based on the provided isBootstrapServer parameter. If isBootstrapServer == true, get the parameters of the current Bootstrap Server. If isBootstrapServer == false, get the parameters of the current Lwm2m Server. Used for client settings when starting the client in Bootstrap mode.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_lwm2m_bootstrap_security_info_using_get_with_http_info(is_bootstrap_server, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool is_bootstrap_server: A Boolean value representing the Server SecurityInfo for future Bootstrap client mode settings. Values: 'true' for Bootstrap Server; 'false' for Lwm2m Server.  (required)
        :return: LwM2MServerSecurityConfigDefault
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['is_bootstrap_server']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_lwm2m_bootstrap_security_info_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'is_bootstrap_server' is set
        if ('is_bootstrap_server' not in params or
                params['is_bootstrap_server'] is None):
            raise ValueError("Missing the required parameter `is_bootstrap_server` when calling `get_lwm2m_bootstrap_security_info_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'is_bootstrap_server' in params:
            path_params['isBootstrapServer'] = params['is_bootstrap_server']  # noqa: E501

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
            '/api/lwm2m/deviceProfile/bootstrap/{isBootstrapServer}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LwM2MServerSecurityConfigDefault',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
