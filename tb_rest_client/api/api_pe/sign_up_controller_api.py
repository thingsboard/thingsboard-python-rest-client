# coding: utf-8

"""
    ThingsBoard REST API

     ThingsBoard Professional Edition IoT platform REST API documentation.  # noqa: E501

    OpenAPI spec version: 3.6.3PE
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


class SignUpControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def accept_privacy_policy_using_post(self, **kwargs):  # noqa: E501
        """Accept privacy policy (acceptPrivacyPolicy)  # noqa: E501

        Accept privacy policy by the current user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accept_privacy_policy_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: JsonNode
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.accept_privacy_policy_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.accept_privacy_policy_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def accept_privacy_policy_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Accept privacy policy (acceptPrivacyPolicy)  # noqa: E501

        Accept privacy policy by the current user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accept_privacy_policy_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: JsonNode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accept_privacy_policy_using_post" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/signup/acceptPrivacyPolicy', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonNode',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def accept_terms_of_use_using_post(self, **kwargs):  # noqa: E501
        """Accept Terms of Use (acceptTermsOfUse)  # noqa: E501

        Accept Terms of Use by the current user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accept_terms_of_use_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: JsonNode
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.accept_terms_of_use_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.accept_terms_of_use_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def accept_terms_of_use_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Accept Terms of Use (acceptTermsOfUse)  # noqa: E501

        Accept Terms of Use by the current user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.accept_terms_of_use_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: JsonNode
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method accept_terms_of_use_using_post" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/signup/acceptTermsOfUse', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JsonNode',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def activate_email_using_get(self, email_code, **kwargs):  # noqa: E501
        """Activate User using code from Email (activateEmail)  # noqa: E501

        Activate the user using code(link) from the activation email. Validates the code an redirects according to the signup flow. Checks that user was not activated yet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_email_using_get(email_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email_code: Activation token. (required)
        :param str pkg_name: Optional package name of the mobile application.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.activate_email_using_get_with_http_info(email_code, **kwargs)  # noqa: E501
        else:
            (data) = self.activate_email_using_get_with_http_info(email_code, **kwargs)  # noqa: E501
            return data

    def activate_email_using_get_with_http_info(self, email_code, **kwargs):  # noqa: E501
        """Activate User using code from Email (activateEmail)  # noqa: E501

        Activate the user using code(link) from the activation email. Validates the code an redirects according to the signup flow. Checks that user was not activated yet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_email_using_get_with_http_info(email_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email_code: Activation token. (required)
        :param str pkg_name: Optional package name of the mobile application.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email_code', 'pkg_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_email_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email_code' is set
        if ('email_code' not in params or
                params['email_code'] is None):
            raise ValueError("Missing the required parameter `email_code` when calling `activate_email_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'email_code' in params:
            query_params.append(('emailCode', params['email_code']))  # noqa: E501
        if 'pkg_name' in params:
            query_params.append(('pkgName', params['pkg_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/activateEmail{?emailCode,pkgName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def activate_user_by_email_code_using_post(self, email_code, **kwargs):  # noqa: E501
        """Activate and login using code from Email (activateUserByEmailCode)  # noqa: E501

        Activate the user using code(link) from the activation email and return the JWT Token. Sends the notification and email about user activation. Checks that user was not activated yet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_user_by_email_code_using_post(email_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email_code: Activation token. (required)
        :param str pkg_name: Optional package name of the mobile application.
        :return: JWTPair
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.activate_user_by_email_code_using_post_with_http_info(email_code, **kwargs)  # noqa: E501
        else:
            (data) = self.activate_user_by_email_code_using_post_with_http_info(email_code, **kwargs)  # noqa: E501
            return data

    def activate_user_by_email_code_using_post_with_http_info(self, email_code, **kwargs):  # noqa: E501
        """Activate and login using code from Email (activateUserByEmailCode)  # noqa: E501

        Activate the user using code(link) from the activation email and return the JWT Token. Sends the notification and email about user activation. Checks that user was not activated yet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_user_by_email_code_using_post_with_http_info(email_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email_code: Activation token. (required)
        :param str pkg_name: Optional package name of the mobile application.
        :return: JWTPair
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email_code', 'pkg_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_user_by_email_code_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email_code' is set
        if ('email_code' not in params or
                params['email_code'] is None):
            raise ValueError("Missing the required parameter `email_code` when calling `activate_user_by_email_code_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'email_code' in params:
            query_params.append(('emailCode', params['email_code']))  # noqa: E501
        if 'pkg_name' in params:
            query_params.append(('pkgName', params['pkg_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/activateByEmailCode{?emailCode,pkgName}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JWTPair',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def mobile_login_using_get(self, pkg_name, **kwargs):  # noqa: E501
        """Mobile Login redirect (mobileLogin)  # noqa: E501

        This method generates redirect to the special link that is handled by mobile application. Useful for email verification flow on mobile app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mobile_login_using_get(pkg_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pkg_name: Mobile app package name. Used to identify the application and build the redirect link. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.mobile_login_using_get_with_http_info(pkg_name, **kwargs)  # noqa: E501
        else:
            (data) = self.mobile_login_using_get_with_http_info(pkg_name, **kwargs)  # noqa: E501
            return data

    def mobile_login_using_get_with_http_info(self, pkg_name, **kwargs):  # noqa: E501
        """Mobile Login redirect (mobileLogin)  # noqa: E501

        This method generates redirect to the special link that is handled by mobile application. Useful for email verification flow on mobile app.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.mobile_login_using_get_with_http_info(pkg_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pkg_name: Mobile app package name. Used to identify the application and build the redirect link. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pkg_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mobile_login_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pkg_name' is set
        if ('pkg_name' not in params or
                params['pkg_name'] is None):
            raise ValueError("Missing the required parameter `pkg_name` when calling `mobile_login_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'pkg_name' in params:
            query_params.append(('pkgName', params['pkg_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/login{?pkgName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def privacy_policy_accepted_using_get(self, **kwargs):  # noqa: E501
        """Check privacy policy (privacyPolicyAccepted)  # noqa: E501

        Checks that current user accepted the privacy policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privacy_policy_accepted_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.privacy_policy_accepted_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.privacy_policy_accepted_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def privacy_policy_accepted_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Check privacy policy (privacyPolicyAccepted)  # noqa: E501

        Checks that current user accepted the privacy policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.privacy_policy_accepted_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method privacy_policy_accepted_using_get" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/signup/privacyPolicyAccepted', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def resend_email_activation_using_post(self, email, **kwargs):  # noqa: E501
        """Resend Activation Email (resendEmailActivation)  # noqa: E501

        Request to resend the activation email for the user. Checks that user was not activated yet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resend_email_activation_using_post(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: Email of the user. (required)
        :param str pkg_name: Optional package name of the mobile application.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.resend_email_activation_using_post_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.resend_email_activation_using_post_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def resend_email_activation_using_post_with_http_info(self, email, **kwargs):  # noqa: E501
        """Resend Activation Email (resendEmailActivation)  # noqa: E501

        Request to resend the activation email for the user. Checks that user was not activated yet.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resend_email_activation_using_post_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: Email of the user. (required)
        :param str pkg_name: Optional package name of the mobile application.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email', 'pkg_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resend_email_activation_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `resend_email_activation_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'email' in params:
            query_params.append(('email', params['email']))  # noqa: E501
        if 'pkg_name' in params:
            query_params.append(('pkgName', params['pkg_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/resendEmailActivation{?email,pkgName}', 'POST',
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

    def sign_up_using_post(self, **kwargs):  # noqa: E501
        """User Sign Up (signUp)  # noqa: E501

        Process user sign up request. Creates the Customer and corresponding User based on self Registration parameters for the domain. See [Self Registration Controller](/swagger-ui.html#/self-registration-controller) for more details.  The result is either 'SUCCESS' or 'INACTIVE_USER_EXISTS'. If Success, the user will receive an email with instruction to activate the account. The content of the email is customizable via the mail templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sign_up_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SignUpRequest body:
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.sign_up_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.sign_up_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def sign_up_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """User Sign Up (signUp)  # noqa: E501

        Process user sign up request. Creates the Customer and corresponding User based on self Registration parameters for the domain. See [Self Registration Controller](/swagger-ui.html#/self-registration-controller) for more details.  The result is either 'SUCCESS' or 'INACTIVE_USER_EXISTS'. If Success, the user will receive an email with instruction to activate the account. The content of the email is customizable via the mail templates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sign_up_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SignUpRequest body:
        :return: str
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
                    " to method sign_up_using_post" % key
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
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/noauth/signup', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def terms_of_use_accepted_using_get(self, **kwargs):  # noqa: E501
        """Check Terms Of User (termsOfUseAccepted)  # noqa: E501

        Checks that current user accepted the privacy policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.terms_of_use_accepted_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.terms_of_use_accepted_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.terms_of_use_accepted_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def terms_of_use_accepted_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Check Terms Of User (termsOfUseAccepted)  # noqa: E501

        Checks that current user accepted the privacy policy.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.terms_of_use_accepted_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method terms_of_use_accepted_using_get" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['X-Authorization']  # noqa: E501

        return self.api_client.call_api(
            '/api/signup/termsOfUseAccepted', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
