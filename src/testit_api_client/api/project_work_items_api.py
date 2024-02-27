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
from testit_api_client.model.api_v2_projects_project_id_work_items_search_grouped_post_request import ApiV2ProjectsProjectIdWorkItemsSearchGroupedPostRequest
from testit_api_client.model.api_v2_projects_project_id_work_items_search_post_request import ApiV2ProjectsProjectIdWorkItemsSearchPostRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.tag_model import TagModel
from testit_api_client.model.work_item_group_model import WorkItemGroupModel
from testit_api_client.model.work_item_short_model import WorkItemShortModel


class ProjectWorkItemsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.api_v2_projects_project_id_work_items_search_grouped_post_endpoint = _Endpoint(
            settings={
                'response_type': ([WorkItemGroupModel],),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/projects/{projectId}/workItems/search/grouped',
                'operation_id': 'api_v2_projects_project_id_work_items_search_grouped_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'skip',
                    'take',
                    'order_by',
                    'search_field',
                    'search_value',
                    'api_v2_projects_project_id_work_items_search_grouped_post_request',
                ],
                'required': [
                    'project_id',
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
                    'project_id':
                        (str,),
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
                    'api_v2_projects_project_id_work_items_search_grouped_post_request':
                        (ApiV2ProjectsProjectIdWorkItemsSearchGroupedPostRequest,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'skip': 'Skip',
                    'take': 'Take',
                    'order_by': 'OrderBy',
                    'search_field': 'SearchField',
                    'search_value': 'SearchValue',
                },
                'location_map': {
                    'project_id': 'path',
                    'skip': 'query',
                    'take': 'query',
                    'order_by': 'query',
                    'search_field': 'query',
                    'search_value': 'query',
                    'api_v2_projects_project_id_work_items_search_grouped_post_request': 'body',
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
        self.api_v2_projects_project_id_work_items_search_id_post_endpoint = _Endpoint(
            settings={
                'response_type': ([str],),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/projects/{projectId}/workItems/search/id',
                'operation_id': 'api_v2_projects_project_id_work_items_search_id_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'skip',
                    'take',
                    'order_by',
                    'search_field',
                    'search_value',
                    'api_v2_projects_project_id_work_items_search_post_request',
                ],
                'required': [
                    'project_id',
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
                    'project_id':
                        (str,),
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
                    'api_v2_projects_project_id_work_items_search_post_request':
                        (ApiV2ProjectsProjectIdWorkItemsSearchPostRequest,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'skip': 'Skip',
                    'take': 'Take',
                    'order_by': 'OrderBy',
                    'search_field': 'SearchField',
                    'search_value': 'SearchValue',
                },
                'location_map': {
                    'project_id': 'path',
                    'skip': 'query',
                    'take': 'query',
                    'order_by': 'query',
                    'search_field': 'query',
                    'search_value': 'query',
                    'api_v2_projects_project_id_work_items_search_post_request': 'body',
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
        self.api_v2_projects_project_id_work_items_search_post_endpoint = _Endpoint(
            settings={
                'response_type': ([WorkItemShortModel],),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/projects/{projectId}/workItems/search',
                'operation_id': 'api_v2_projects_project_id_work_items_search_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'skip',
                    'take',
                    'order_by',
                    'search_field',
                    'search_value',
                    'api_v2_projects_project_id_work_items_search_post_request',
                ],
                'required': [
                    'project_id',
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
                    'project_id':
                        (str,),
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
                    'api_v2_projects_project_id_work_items_search_post_request':
                        (ApiV2ProjectsProjectIdWorkItemsSearchPostRequest,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'skip': 'Skip',
                    'take': 'Take',
                    'order_by': 'OrderBy',
                    'search_field': 'SearchField',
                    'search_value': 'SearchValue',
                },
                'location_map': {
                    'project_id': 'path',
                    'skip': 'query',
                    'take': 'query',
                    'order_by': 'query',
                    'search_field': 'query',
                    'search_value': 'query',
                    'api_v2_projects_project_id_work_items_search_post_request': 'body',
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
        self.api_v2_projects_project_id_work_items_tags_get_endpoint = _Endpoint(
            settings={
                'response_type': ([TagModel],),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/projects/{projectId}/workItems/tags',
                'operation_id': 'api_v2_projects_project_id_work_items_tags_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'is_deleted',
                ],
                'required': [
                    'project_id',
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
                    'project_id':
                        (str,),
                    'is_deleted':
                        (bool,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'is_deleted': 'isDeleted',
                },
                'location_map': {
                    'project_id': 'path',
                    'is_deleted': 'query',
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
        self.get_work_items_by_project_id_endpoint = _Endpoint(
            settings={
                'response_type': ([WorkItemShortModel],),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/projects/{projectId}/workItems',
                'operation_id': 'get_work_items_by_project_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'is_deleted',
                    'tag_names',
                    'include_iterations',
                    'skip',
                    'take',
                    'order_by',
                    'search_field',
                    'search_value',
                ],
                'required': [
                    'project_id',
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
                    'project_id':
                        (str,),
                    'is_deleted':
                        (bool,),
                    'tag_names':
                        ([str],),
                    'include_iterations':
                        (bool,),
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
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'is_deleted': 'isDeleted',
                    'tag_names': 'tagNames',
                    'include_iterations': 'includeIterations',
                    'skip': 'Skip',
                    'take': 'Take',
                    'order_by': 'OrderBy',
                    'search_field': 'SearchField',
                    'search_value': 'SearchValue',
                },
                'location_map': {
                    'project_id': 'path',
                    'is_deleted': 'query',
                    'tag_names': 'query',
                    'include_iterations': 'query',
                    'skip': 'query',
                    'take': 'query',
                    'order_by': 'query',
                    'search_field': 'query',
                    'search_value': 'query',
                },
                'collection_format_map': {
                    'tag_names': 'multi',
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

    def api_v2_projects_project_id_work_items_search_grouped_post(
        self,
        project_id,
        **kwargs
    ):
        """Search for work items and group results by attribute  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_projects_project_id_work_items_search_grouped_post(project_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str): Unique or global ID of the project

        Keyword Args:
            skip (int): Amount of items to be skipped (offset). [optional]
            take (int): Amount of items to be taken (limit). [optional]
            order_by (str): SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC). [optional]
            search_field (str): Property name for searching. [optional]
            search_value (str): Value for searching. [optional]
            api_v2_projects_project_id_work_items_search_grouped_post_request (ApiV2ProjectsProjectIdWorkItemsSearchGroupedPostRequest): [optional]
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
            [WorkItemGroupModel]
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
        kwargs['project_id'] = \
            project_id
        return self.api_v2_projects_project_id_work_items_search_grouped_post_endpoint.call_with_http_info(**kwargs)

    def api_v2_projects_project_id_work_items_search_id_post(
        self,
        project_id,
        **kwargs
    ):
        """Search for work items and extract IDs only  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_projects_project_id_work_items_search_id_post(project_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str): Unique or global ID of the project

        Keyword Args:
            skip (int): Amount of items to be skipped (offset). [optional]
            take (int): Amount of items to be taken (limit). [optional]
            order_by (str): SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC). [optional]
            search_field (str): Property name for searching. [optional]
            search_value (str): Value for searching. [optional]
            api_v2_projects_project_id_work_items_search_post_request (ApiV2ProjectsProjectIdWorkItemsSearchPostRequest): [optional]
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
        kwargs['project_id'] = \
            project_id
        return self.api_v2_projects_project_id_work_items_search_id_post_endpoint.call_with_http_info(**kwargs)

    def api_v2_projects_project_id_work_items_search_post(
        self,
        project_id,
        **kwargs
    ):
        """Search for work items  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_projects_project_id_work_items_search_post(project_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str): Unique or global ID of the project

        Keyword Args:
            skip (int): Amount of items to be skipped (offset). [optional]
            take (int): Amount of items to be taken (limit). [optional]
            order_by (str): SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC). [optional]
            search_field (str): Property name for searching. [optional]
            search_value (str): Value for searching. [optional]
            api_v2_projects_project_id_work_items_search_post_request (ApiV2ProjectsProjectIdWorkItemsSearchPostRequest): [optional]
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
            [WorkItemShortModel]
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
        kwargs['project_id'] = \
            project_id
        return self.api_v2_projects_project_id_work_items_search_post_endpoint.call_with_http_info(**kwargs)

    def api_v2_projects_project_id_work_items_tags_get(
        self,
        project_id,
        **kwargs
    ):
        """Get WorkItems Tags  # noqa: E501

        <br>Use case  <br>User sets project internal identifier   <br>User runs method execution  <br>System returns work items tags  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v2_projects_project_id_work_items_tags_get(project_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str): Project internal (UUID) identifier

        Keyword Args:
            is_deleted (bool): [optional]
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
            [TagModel]
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
        kwargs['project_id'] = \
            project_id
        return self.api_v2_projects_project_id_work_items_tags_get_endpoint.call_with_http_info(**kwargs)

    def get_work_items_by_project_id(
        self,
        project_id,
        **kwargs
    ):
        """Get project work items  # noqa: E501

        <br>Use case  <br>User sets project internal or global identifier  <br>[Optional] User sets isDeleted field value  <br>User runs method execution  <br>System search project  <br>[Optional] If User sets isDeleted field value as true, System search all deleted workitems related to project  <br>[Optional] If User sets isDeleted field value as false, System search all workitems related to project which are not deleted  <br>If User did not set isDeleted field value, System search all  workitems related to project  <br>System returns array of found workitems (listed in response model)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_work_items_by_project_id(project_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str): Project internal (UUID) or global (integer) identifier

        Keyword Args:
            is_deleted (bool): If result must consist of only actual/deleted work items. [optional] if omitted the server will use the default value of False
            tag_names ([str]): List of tags to filter by. [optional]
            include_iterations (bool): [optional] if omitted the server will use the default value of True
            skip (int): Amount of items to be skipped (offset). [optional]
            take (int): Amount of items to be taken (limit). [optional]
            order_by (str): SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC). [optional]
            search_field (str): Property name for searching. [optional]
            search_value (str): Value for searching. [optional]
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
            [WorkItemShortModel]
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
        kwargs['project_id'] = \
            project_id
        return self.get_work_items_by_project_id_endpoint.call_with_http_info(**kwargs)

