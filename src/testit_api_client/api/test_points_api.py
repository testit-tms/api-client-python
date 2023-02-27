"""
    API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v2.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from testit_api_client.api_client import ApiClient, Endpoint as _Endpoint
from testit_api_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_point_filter_model import TestPointFilterModel
from testit_api_client.model.test_point_short_get_model import TestPointShortGetModel
from testit_api_client.model.test_run_model import TestRunModel
from testit_api_client.model.work_item_model import WorkItemModel


class TestPointsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.api_v2_test_points_id_test_runs_get_endpoint = _Endpoint(
            settings={
                'response_type': ([TestRunModel],),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/testPoints/{id}/testRuns',
                'operation_id': 'api_v2_test_points_id_test_runs_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.api_v2_test_points_id_work_item_get_endpoint = _Endpoint(
            settings={
                'response_type': (WorkItemModel,),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/testPoints/{id}/workItem',
                'operation_id': 'api_v2_test_points_id_work_item_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                ],
                'required': [
                    'id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'id':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                },
                'location_map': {
                    'id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.api_v2_test_points_search_id_post_endpoint = _Endpoint(
            settings={
                'response_type': ([str],),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/testPoints/search/id',
                'operation_id': 'api_v2_test_points_search_id_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'skip',
                    'take',
                    'order_by',
                    'search_field',
                    'search_value',
                    'test_point_filter_model',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'skip':
                        (int,),
                    'take':
                        (int,),
                    'order_by':
                        (str,),
                    'search_field':
                        (str,),
                    'search_value':
                        (str,),
                    'test_point_filter_model':
                        (TestPointFilterModel,),
                },
                'attribute_map': {
                    'skip': 'Skip',
                    'take': 'Take',
                    'order_by': 'OrderBy',
                    'search_field': 'SearchField',
                    'search_value': 'SearchValue',
                },
                'location_map': {
                    'skip': 'query',
                    'take': 'query',
                    'order_by': 'query',
                    'search_field': 'query',
                    'search_value': 'query',
                    'test_point_filter_model': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.api_v2_test_points_search_post_endpoint = _Endpoint(
            settings={
                'response_type': ([TestPointShortGetModel],),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/testPoints/search',
                'operation_id': 'api_v2_test_points_search_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'skip',
                    'take',
                    'order_by',
                    'search_field',
                    'search_value',
                    'test_point_filter_model',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'skip':
                        (int,),
                    'take':
                        (int,),
                    'order_by':
                        (str,),
                    'search_field':
                        (str,),
                    'search_value':
                        (str,),
                    'test_point_filter_model':
                        (TestPointFilterModel,),
                },
                'attribute_map': {
                    'skip': 'Skip',
                    'take': 'Take',
                    'order_by': 'OrderBy',
                    'search_field': 'SearchField',
                    'search_value': 'SearchValue',
                },
                'location_map': {
                    'skip': 'query',
                    'take': 'query',
                    'order_by': 'query',
                    'search_field': 'query',
                    'search_value': 'query',
                    'test_point_filter_model': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def api_v2_test_points_id_test_runs_get(
        self,
        id,
        **kwargs
    ):
        """Get all test runs which use test point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_test_points_id_test_runs_get(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): Test point unique ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [TestRunModel]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['id'] = \
            id
        return self.api_v2_test_points_id_test_runs_get_endpoint.call_with_http_info(**kwargs)

    def api_v2_test_points_id_work_item_get(
        self,
        id,
        **kwargs
    ):
        """Get work item represented by test point  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_test_points_id_work_item_get(id, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): Test point unique ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            WorkItemModel
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['id'] = \
            id
        return self.api_v2_test_points_id_work_item_get_endpoint.call_with_http_info(**kwargs)

    def api_v2_test_points_search_id_post(
        self,
        **kwargs
    ):
        """Search for test points and extract IDs only  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_test_points_search_id_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            skip (int): Amount of items to be skipped (offset). [optional]
            take (int): Amount of items to be taken (limit). [optional]
            order_by (str): SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC). [optional]
            search_field (str): Property name for searching. [optional]
            search_value (str): Value for searching. [optional]
            test_point_filter_model (TestPointFilterModel): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [str]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.api_v2_test_points_search_id_post_endpoint.call_with_http_info(**kwargs)

    def api_v2_test_points_search_post(
        self,
        **kwargs
    ):
        """Search for test points  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_test_points_search_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            skip (int): Amount of items to be skipped (offset). [optional]
            take (int): Amount of items to be taken (limit). [optional]
            order_by (str): SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC). [optional]
            search_field (str): Property name for searching. [optional]
            search_value (str): Value for searching. [optional]
            test_point_filter_model (TestPointFilterModel): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [TestPointShortGetModel]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.api_v2_test_points_search_post_endpoint.call_with_http_info(**kwargs)

