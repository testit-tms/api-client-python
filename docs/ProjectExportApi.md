# testit_api_client.ProjectExportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export**](ProjectExportApi.md#export) | **POST** /api/v2/projects/{projectId}/export | Export project as JSON file
[**export_project_json**](ProjectExportApi.md#export_project_json) | **POST** /api/v2/projects/{projectId}/export/json | Export project as JSON file in background job
[**export_project_with_test_plans_json**](ProjectExportApi.md#export_project_with_test_plans_json) | **POST** /api/v2/projects/{projectId}/export/testPlans/json | Export project as JSON file with test plans in background job
[**export_project_with_test_plans_zip**](ProjectExportApi.md#export_project_with_test_plans_zip) | **POST** /api/v2/projects/{projectId}/export/testPlans/zip | Export project as Zip file with test plans in background job
[**export_project_zip**](ProjectExportApi.md#export_project_zip) | **POST** /api/v2/projects/{projectId}/export/zip | Export project as Zip file in background job


# **export**
> file_type export(project_id)

Export project as JSON file

<br>This method exports the selected project or its part (sections, work items) to a `.json` file.  <br>In the request body, you can specify sections and test cases to be exported.  <br>Example of a request to export two sections and two test cases:  <br>    ```              curl -X POST \"http://{domain}.com/api/v2/projects/27a32ce6-d972-4ef8-bef5-51be4bf9e468/export\" \\              -H \"accept: application/json\" -H \"Authorization: PrivateToken {token}\" -H \"Content-Type: application/json-patch+json\" \\              -d \"{\\\"sectionIds\\\":[\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"9fa85f64-5717-4562-b3fc-2c963f66a000\\\"],\\\"workItemIds\\\":[\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"90085f64-5717-4562-b3fc-2c963f66a000\\\"]}\"              ```    <br>In the response, you get:  <br>              - A `.zip` file with attachments and a.json file if you enable attachments export.<br />              - A `.json` file with the project if you do not enable attachments export.              

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_export_api
from testit_api_client.model.export_project_json_request import ExportProjectJsonRequest
from testit_api_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = testit_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer or PrivateToken
configuration.api_key['Bearer or PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_export_api.ProjectExportApi(api_client)
    project_id = "projectId_example" # str | Specifies the ID of the project you want to export.
    include_attachments = False # bool | Enables attachment export. (optional) if omitted the server will use the default value of False
    export_project_json_request = ExportProjectJsonRequest(None) # ExportProjectJsonRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project as JSON file
        api_response = api_instance.export(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExportApi->export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project as JSON file
        api_response = api_instance.export(project_id, include_attachments=include_attachments, export_project_json_request=export_project_json_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExportApi->export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Specifies the ID of the project you want to export. |
 **include_attachments** | **bool**| Enables attachment export. | [optional] if omitted the server will use the default value of False
 **export_project_json_request** | [**ExportProjectJsonRequest**](ExportProjectJsonRequest.md)|  | [optional]

### Return type

**file_type**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings is required |  -  |
**400** | Root section was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_json**
> str export_project_json(project_id)

Export project as JSON file in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_export_api
from testit_api_client.model.export_project_json_request import ExportProjectJsonRequest
from testit_api_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = testit_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer or PrivateToken
configuration.api_key['Bearer or PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_export_api.ProjectExportApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    time_zone_offset_in_minutes = 1 # int |  (optional)
    export_project_json_request = ExportProjectJsonRequest(None) # ExportProjectJsonRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project as JSON file in background job
        api_response = api_instance.export_project_json(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExportApi->export_project_json: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project as JSON file in background job
        api_response = api_instance.export_project_json(project_id, time_zone_offset_in_minutes=time_zone_offset_in_minutes, export_project_json_request=export_project_json_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExportApi->export_project_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **time_zone_offset_in_minutes** | **int**|  | [optional]
 **export_project_json_request** | [**ExportProjectJsonRequest**](ExportProjectJsonRequest.md)|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_with_test_plans_json**
> str export_project_with_test_plans_json(project_id)

Export project as JSON file with test plans in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_export_api
from testit_api_client.model.export_project_with_test_plans_json_request import ExportProjectWithTestPlansJsonRequest
from testit_api_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = testit_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer or PrivateToken
configuration.api_key['Bearer or PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_export_api.ProjectExportApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    time_zone_offset_in_minutes = 1 # int |  (optional)
    export_project_with_test_plans_json_request = ExportProjectWithTestPlansJsonRequest(None) # ExportProjectWithTestPlansJsonRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project as JSON file with test plans in background job
        api_response = api_instance.export_project_with_test_plans_json(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExportApi->export_project_with_test_plans_json: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project as JSON file with test plans in background job
        api_response = api_instance.export_project_with_test_plans_json(project_id, time_zone_offset_in_minutes=time_zone_offset_in_minutes, export_project_with_test_plans_json_request=export_project_with_test_plans_json_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExportApi->export_project_with_test_plans_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **time_zone_offset_in_minutes** | **int**|  | [optional]
 **export_project_with_test_plans_json_request** | [**ExportProjectWithTestPlansJsonRequest**](ExportProjectWithTestPlansJsonRequest.md)|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_with_test_plans_zip**
> str export_project_with_test_plans_zip(project_id)

Export project as Zip file with test plans in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_export_api
from testit_api_client.model.export_project_with_test_plans_json_request import ExportProjectWithTestPlansJsonRequest
from testit_api_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = testit_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer or PrivateToken
configuration.api_key['Bearer or PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_export_api.ProjectExportApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    time_zone_offset_in_minutes = 1 # int |  (optional)
    export_project_with_test_plans_json_request = ExportProjectWithTestPlansJsonRequest(None) # ExportProjectWithTestPlansJsonRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project as Zip file with test plans in background job
        api_response = api_instance.export_project_with_test_plans_zip(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExportApi->export_project_with_test_plans_zip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project as Zip file with test plans in background job
        api_response = api_instance.export_project_with_test_plans_zip(project_id, time_zone_offset_in_minutes=time_zone_offset_in_minutes, export_project_with_test_plans_json_request=export_project_with_test_plans_json_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExportApi->export_project_with_test_plans_zip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **time_zone_offset_in_minutes** | **int**|  | [optional]
 **export_project_with_test_plans_json_request** | [**ExportProjectWithTestPlansJsonRequest**](ExportProjectWithTestPlansJsonRequest.md)|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_zip**
> str export_project_zip(project_id)

Export project as Zip file in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_export_api
from testit_api_client.model.export_project_json_request import ExportProjectJsonRequest
from testit_api_client.model.problem_details import ProblemDetails
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = testit_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer or PrivateToken
configuration.api_key['Bearer or PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_export_api.ProjectExportApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    time_zone_offset_in_minutes = 1 # int |  (optional)
    export_project_json_request = ExportProjectJsonRequest(None) # ExportProjectJsonRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project as Zip file in background job
        api_response = api_instance.export_project_zip(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExportApi->export_project_zip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project as Zip file in background job
        api_response = api_instance.export_project_zip(project_id, time_zone_offset_in_minutes=time_zone_offset_in_minutes, export_project_json_request=export_project_json_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExportApi->export_project_zip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **time_zone_offset_in_minutes** | **int**|  | [optional]
 **export_project_json_request** | [**ExportProjectJsonRequest**](ExportProjectJsonRequest.md)|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

