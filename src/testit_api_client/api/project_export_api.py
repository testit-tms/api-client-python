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
from testit_api_client.model.export_project_json_request import ExportProjectJsonRequest
from testit_api_client.model.export_project_with_test_plans_json_request import ExportProjectWithTestPlansJsonRequest
from testit_api_client.model.problem_details import ProblemDetails


class ProjectExportApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.export_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/projects/{projectId}/export',
                'operation_id': 'export',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'include_attachments',
                    'export_project_json_request',
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
                    'include_attachments':
                        (bool,),
                    'export_project_json_request':
                        (ExportProjectJsonRequest,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'include_attachments': 'includeAttachments',
                },
                'location_map': {
                    'project_id': 'path',
                    'include_attachments': 'query',
                    'export_project_json_request': 'body',
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
        self.export_project_json_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/projects/{projectId}/export/json',
                'operation_id': 'export_project_json',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'time_zone_offset_in_minutes',
                    'export_project_json_request',
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
                    'time_zone_offset_in_minutes':
                        (int,),
                    'export_project_json_request':
                        (ExportProjectJsonRequest,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'time_zone_offset_in_minutes': 'time-Zone-Offset-In-Minutes',
                },
                'location_map': {
                    'project_id': 'path',
                    'time_zone_offset_in_minutes': 'header',
                    'export_project_json_request': 'body',
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
        self.export_project_with_test_plans_json_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/projects/{projectId}/export/testPlans/json',
                'operation_id': 'export_project_with_test_plans_json',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'time_zone_offset_in_minutes',
                    'export_project_with_test_plans_json_request',
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
                    'time_zone_offset_in_minutes':
                        (int,),
                    'export_project_with_test_plans_json_request':
                        (ExportProjectWithTestPlansJsonRequest,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'time_zone_offset_in_minutes': 'time-Zone-Offset-In-Minutes',
                },
                'location_map': {
                    'project_id': 'path',
                    'time_zone_offset_in_minutes': 'header',
                    'export_project_with_test_plans_json_request': 'body',
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
        self.export_project_with_test_plans_zip_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/projects/{projectId}/export/testPlans/zip',
                'operation_id': 'export_project_with_test_plans_zip',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'time_zone_offset_in_minutes',
                    'export_project_with_test_plans_json_request',
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
                    'time_zone_offset_in_minutes':
                        (int,),
                    'export_project_with_test_plans_json_request':
                        (ExportProjectWithTestPlansJsonRequest,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'time_zone_offset_in_minutes': 'time-Zone-Offset-In-Minutes',
                },
                'location_map': {
                    'project_id': 'path',
                    'time_zone_offset_in_minutes': 'header',
                    'export_project_with_test_plans_json_request': 'body',
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
        self.export_project_zip_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'Bearer or PrivateToken'
                ],
                'endpoint_path': '/api/v2/projects/{projectId}/export/zip',
                'operation_id': 'export_project_zip',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'time_zone_offset_in_minutes',
                    'export_project_json_request',
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
                    'time_zone_offset_in_minutes':
                        (int,),
                    'export_project_json_request':
                        (ExportProjectJsonRequest,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'time_zone_offset_in_minutes': 'time-Zone-Offset-In-Minutes',
                },
                'location_map': {
                    'project_id': 'path',
                    'time_zone_offset_in_minutes': 'header',
                    'export_project_json_request': 'body',
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

    def export(
        self,
        project_id,
        **kwargs
    ):
        """Export project as JSON file  # noqa: E501

        <br>This method exports the selected project or its part (sections, work items) to a `.json` file.  <br>In the request body, you can specify sections and test cases to be exported.  <br>Example of a request to export two sections and two test cases:  <br>    ```              curl -X POST \"http://{domain}.com/api/v2/projects/27a32ce6-d972-4ef8-bef5-51be4bf9e468/export\" \\              -H \"accept: application/json\" -H \"Authorization: PrivateToken {token}\" -H \"Content-Type: application/json-patch+json\" \\              -d \"{\\\"sectionIds\\\":[\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"9fa85f64-5717-4562-b3fc-2c963f66a000\\\"],\\\"workItemIds\\\":[\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"90085f64-5717-4562-b3fc-2c963f66a000\\\"]}\"              ```    <br>In the response, you get:  <br>              - A `.zip` file with attachments and a.json file if you enable attachments export.<br />              - A `.json` file with the project if you do not enable attachments export.                # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export(project_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str): Specifies the ID of the project you want to export.

        Keyword Args:
            include_attachments (bool): Enables attachment export.. [optional] if omitted the server will use the default value of False
            export_project_json_request (ExportProjectJsonRequest): [optional]
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
            file_type
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
        return self.export_endpoint.call_with_http_info(**kwargs)

    def export_project_json(
        self,
        project_id,
        **kwargs
    ):
        """Export project as JSON file in background job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export_project_json(project_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str): Project internal (UUID) or global (integer) identifier

        Keyword Args:
            time_zone_offset_in_minutes (int): [optional]
            export_project_json_request (ExportProjectJsonRequest): [optional]
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
            str
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
        return self.export_project_json_endpoint.call_with_http_info(**kwargs)

    def export_project_with_test_plans_json(
        self,
        project_id,
        **kwargs
    ):
        """Export project as JSON file with test plans in background job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export_project_with_test_plans_json(project_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str): Project internal (UUID) or global (integer) identifier

        Keyword Args:
            time_zone_offset_in_minutes (int): [optional]
            export_project_with_test_plans_json_request (ExportProjectWithTestPlansJsonRequest): [optional]
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
            str
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
        return self.export_project_with_test_plans_json_endpoint.call_with_http_info(**kwargs)

    def export_project_with_test_plans_zip(
        self,
        project_id,
        **kwargs
    ):
        """Export project as Zip file with test plans in background job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export_project_with_test_plans_zip(project_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str): Project internal (UUID) or global (integer) identifier

        Keyword Args:
            time_zone_offset_in_minutes (int): [optional]
            export_project_with_test_plans_json_request (ExportProjectWithTestPlansJsonRequest): [optional]
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
            str
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
        return self.export_project_with_test_plans_zip_endpoint.call_with_http_info(**kwargs)

    def export_project_zip(
        self,
        project_id,
        **kwargs
    ):
        """Export project as Zip file in background job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.export_project_zip(project_id, async_req=True)
        >>> result = thread.get()

        Args:
            project_id (str): Project internal (UUID) or global (integer) identifier

        Keyword Args:
            time_zone_offset_in_minutes (int): [optional]
            export_project_json_request (ExportProjectJsonRequest): [optional]
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
            str
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
        return self.export_project_zip_endpoint.call_with_http_info(**kwargs)
