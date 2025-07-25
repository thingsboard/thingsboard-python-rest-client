# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 4.1.0PE
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


class BlobEntityControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_blob_entity_using_delete(self, blob_entity_id, **kwargs):  # noqa: E501
        """Delete Blob Entity (deleteBlobEntity)  # noqa: E501

        Delete Blob entity based on the provided Blob entity Id. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_blob_entity_using_delete(blob_entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str blob_entity_id: A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_blob_entity_using_delete_with_http_info(blob_entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_blob_entity_using_delete_with_http_info(blob_entity_id, **kwargs)  # noqa: E501
            return data

    def delete_blob_entity_using_delete_with_http_info(self, blob_entity_id, **kwargs):  # noqa: E501
        """Delete Blob Entity (deleteBlobEntity)  # noqa: E501

        Delete Blob entity based on the provided Blob entity Id. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority.   Security check is performed to verify that the user has 'DELETE' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_blob_entity_using_delete_with_http_info(blob_entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str blob_entity_id: A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['blob_entity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_blob_entity_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'blob_entity_id' is set
        if ('blob_entity_id' not in params or
                params['blob_entity_id'] is None):
            raise ValueError("Missing the required parameter `blob_entity_id` when calling `delete_blob_entity_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'blob_entity_id' in params:
            path_params['blobEntityId'] = params['blob_entity_id']  # noqa: E501

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
            '/api/blobEntity/{blobEntityId}', 'DELETE',
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

    def download_blob_entity_using_get(self, blob_entity_id, **kwargs):  # noqa: E501
        """Download Blob Entity By Id (downloadBlobEntity)  # noqa: E501

        Download report file based on the provided Blob entity Id. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_blob_entity_using_get(blob_entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str blob_entity_id: A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: Resource
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.download_blob_entity_using_get_with_http_info(blob_entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.download_blob_entity_using_get_with_http_info(blob_entity_id, **kwargs)  # noqa: E501
            return data

    def download_blob_entity_using_get_with_http_info(self, blob_entity_id, **kwargs):  # noqa: E501
        """Download Blob Entity By Id (downloadBlobEntity)  # noqa: E501

        Download report file based on the provided Blob entity Id. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_blob_entity_using_get_with_http_info(blob_entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str blob_entity_id: A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: Resource
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['blob_entity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_blob_entity_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'blob_entity_id' is set
        if ('blob_entity_id' not in params or
                params['blob_entity_id'] is None):
            raise ValueError("Missing the required parameter `blob_entity_id` when calling `download_blob_entity_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'blob_entity_id' in params:
            path_params['blobEntityId'] = params['blob_entity_id']  # noqa: E501

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
            '/api/blobEntity/{blobEntityId}/download', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Resource',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_blob_entities_by_ids_using_get(self, blob_entity_ids, **kwargs):  # noqa: E501
        """Get Blob Entities By Ids (getBlobEntitiesByIds)  # noqa: E501

        Requested blob entities must be owned by tenant or assigned to customer which user is performing the request. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.). See the 'Model' tab of the Response Class for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_blob_entities_by_ids_using_get(blob_entity_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str blob_entity_ids: A list of blob entity ids, separated by comma ',' (required)
        :return: list[BlobEntityInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_blob_entities_by_ids_using_get_with_http_info(blob_entity_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_blob_entities_by_ids_using_get_with_http_info(blob_entity_ids, **kwargs)  # noqa: E501
            return data

    def get_blob_entities_by_ids_using_get_with_http_info(self, blob_entity_ids, **kwargs):  # noqa: E501
        """Get Blob Entities By Ids (getBlobEntitiesByIds)  # noqa: E501

        Requested blob entities must be owned by tenant or assigned to customer which user is performing the request. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.). See the 'Model' tab of the Response Class for more details.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_blob_entities_by_ids_using_get_with_http_info(blob_entity_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str blob_entity_ids: A list of blob entity ids, separated by comma ',' (required)
        :return: list[BlobEntityInfo]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['blob_entity_ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_blob_entities_by_ids_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'blob_entity_ids' is set
        if ('blob_entity_ids' not in params or
                params['blob_entity_ids'] is None):
            raise ValueError("Missing the required parameter `blob_entity_ids` when calling `get_blob_entities_by_ids_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'blob_entity_ids' in params:
            query_params.append(('blobEntityIds', params['blob_entity_ids']))  # noqa: E501

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
            '/api/blobEntities{?blobEntityIds}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BlobEntityInfo]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_blob_entities_using_get(self, page_size, page, **kwargs):  # noqa: E501
        """Get Blob Entities (getBlobEntities)  # noqa: E501

        Returns a page of BlobEntityWithCustomerInfo object that are available for the current user. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityWithCustomerInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.) and info about the customer(customerTitle, customerIsPublic) of the user that scheduled generation of the dashboard report. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_blob_entities_using_get(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str type: A string value representing the blob entity type. For example, 'report'
        :param str text_search: The case insensitive 'startsWith' filter based on the blob entity name.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param int start_time: The start timestamp in milliseconds of the search time range over the BlobEntityWithCustomerInfo class field: 'createdTime'.
        :param int end_time: The end timestamp in milliseconds of the search time range over the BlobEntityWithCustomerInfo class field: 'createdTime'.
        :return: PageDataBlobEntityWithCustomerInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_blob_entities_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
        else:
            (data) = self.get_blob_entities_using_get_with_http_info(page_size, page, **kwargs)  # noqa: E501
            return data

    def get_blob_entities_using_get_with_http_info(self, page_size, page, **kwargs):  # noqa: E501
        """Get Blob Entities (getBlobEntities)  # noqa: E501

        Returns a page of BlobEntityWithCustomerInfo object that are available for the current user. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityWithCustomerInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.) and info about the customer(customerTitle, customerIsPublic) of the user that scheduled generation of the dashboard report. You can specify parameters to filter the results. The result is wrapped with PageData object that allows you to iterate over result set using pagination. See the 'Model' tab of the Response Class for more details.   Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_blob_entities_using_get_with_http_info(page_size, page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page_size: Maximum amount of entities in a one page (required)
        :param int page: Sequence number of page starting from 0 (required)
        :param str type: A string value representing the blob entity type. For example, 'report'
        :param str text_search: The case insensitive 'startsWith' filter based on the blob entity name.
        :param str sort_property: Property of entity to sort by
        :param str sort_order: Sort order. ASC (ASCENDING) or DESC (DESCENDING)
        :param int start_time: The start timestamp in milliseconds of the search time range over the BlobEntityWithCustomerInfo class field: 'createdTime'.
        :param int end_time: The end timestamp in milliseconds of the search time range over the BlobEntityWithCustomerInfo class field: 'createdTime'.
        :return: PageDataBlobEntityWithCustomerInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page_size', 'page', 'type', 'text_search', 'sort_property', 'sort_order', 'start_time', 'end_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_blob_entities_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'page_size' is set
        if ('page_size' not in params or
                params['page_size'] is None):
            raise ValueError("Missing the required parameter `page_size` when calling `get_blob_entities_using_get`")  # noqa: E501
        # verify the required parameter 'page' is set
        if ('page' not in params or
                params['page'] is None):
            raise ValueError("Missing the required parameter `page` when calling `get_blob_entities_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'text_search' in params:
            query_params.append(('textSearch', params['text_search']))  # noqa: E501
        if 'sort_property' in params:
            query_params.append(('sortProperty', params['sort_property']))  # noqa: E501
        if 'sort_order' in params:
            query_params.append(('sortOrder', params['sort_order']))  # noqa: E501
        if 'start_time' in params:
            query_params.append(('startTime', params['start_time']))  # noqa: E501
        if 'end_time' in params:
            query_params.append(('endTime', params['end_time']))  # noqa: E501

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
            '/api/blobEntities{?endTime,page,pageSize,sortOrder,sortProperty,startTime,textSearch,type}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageDataBlobEntityWithCustomerInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_blob_entity_info_by_id_using_get(self, blob_entity_id, **kwargs):  # noqa: E501
        """Get Blob Entity With Customer Info (getBlobEntityInfoById)  # noqa: E501

        Fetch the BlobEntityWithCustomerInfo object based on the provided Blob entity Id. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityWithCustomerInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.) and info about the customer(customerTitle, customerIsPublic) of the user that scheduled generation of the dashboard report. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_blob_entity_info_by_id_using_get(blob_entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str blob_entity_id: A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: BlobEntityWithCustomerInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_blob_entity_info_by_id_using_get_with_http_info(blob_entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_blob_entity_info_by_id_using_get_with_http_info(blob_entity_id, **kwargs)  # noqa: E501
            return data

    def get_blob_entity_info_by_id_using_get_with_http_info(self, blob_entity_id, **kwargs):  # noqa: E501
        """Get Blob Entity With Customer Info (getBlobEntityInfoById)  # noqa: E501

        Fetch the BlobEntityWithCustomerInfo object based on the provided Blob entity Id. The platform uses Blob(binary large object) entities in the reporting feature, in order to store Dashboard states snapshots of different content types in base64 format. BlobEntityWithCustomerInfo represents an object that contains base info about the blob entity(name, type, contentType, etc.) and info about the customer(customerTitle, customerIsPublic) of the user that scheduled generation of the dashboard report. Referencing non-existing Blob entity Id will cause an error.  Available for users with 'TENANT_ADMIN' or 'CUSTOMER_USER' authority. Security check is performed to verify that the user has 'READ' permission for the entity (entities).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_blob_entity_info_by_id_using_get_with_http_info(blob_entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str blob_entity_id: A string value representing the blob entity id. For example, '784f394c-42b6-435a-983c-b7beff2784f9' (required)
        :return: BlobEntityWithCustomerInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['blob_entity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_blob_entity_info_by_id_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'blob_entity_id' is set
        if ('blob_entity_id' not in params or
                params['blob_entity_id'] is None):
            raise ValueError("Missing the required parameter `blob_entity_id` when calling `get_blob_entity_info_by_id_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'blob_entity_id' in params:
            path_params['blobEntityId'] = params['blob_entity_id']  # noqa: E501

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
            '/api/blobEntity/info/{blobEntityId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BlobEntityWithCustomerInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
