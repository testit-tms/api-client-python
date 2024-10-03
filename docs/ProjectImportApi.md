# testit_api_client.ProjectImportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**background_import_to_existing_project**](ProjectImportApi.md#background_import_to_existing_project) | **POST** /api/v2/projects/{projectId}/import/json | Import project from JSON file into existing project in background job
[**background_import_zip_to_existing_project**](ProjectImportApi.md#background_import_zip_to_existing_project) | **POST** /api/v2/projects/{projectId}/import/zip | Import project from Zip file into existing project in background job
[**import_to_existing_project**](ProjectImportApi.md#import_to_existing_project) | **POST** /api/v2/projects/{projectId}/import | Import project from JSON file into existing project


# **background_import_to_existing_project**
> str background_import_to_existing_project(project_id)

Import project from JSON file into existing project in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_import_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
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
    api_instance = project_import_api.ProjectImportApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    file = open('/path/to/file', 'rb') # file_type | Select file (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import project from JSON file into existing project in background job
        api_response = api_instance.background_import_to_existing_project(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectImportApi->background_import_to_existing_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from JSON file into existing project in background job
        api_response = api_instance.background_import_to_existing_project(project_id, file=file)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectImportApi->background_import_to_existing_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **file** | **file_type**| Select file | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for project settings required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **background_import_zip_to_existing_project**
> str background_import_zip_to_existing_project(project_id)

Import project from Zip file into existing project in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_import_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
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
    api_instance = project_import_api.ProjectImportApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    file = open('/path/to/file', 'rb') # file_type | Select file (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import project from Zip file into existing project in background job
        api_response = api_instance.background_import_zip_to_existing_project(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectImportApi->background_import_zip_to_existing_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from Zip file into existing project in background job
        api_response = api_instance.background_import_zip_to_existing_project(project_id, file=file)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectImportApi->background_import_zip_to_existing_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **file** | **file_type**| Select file | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for project settings required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_to_existing_project**
> import_to_existing_project(project_id)

Import project from JSON file into existing project

 Use case   User attaches project as json file taken from export or export-by-testPlans method   User runs method execution   System updates project   System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_import_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
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
    api_instance = project_import_api.ProjectImportApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    include_attachments = True # bool |  (optional)
    file = open('/path/to/file', 'rb') # file_type | Select file (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import project from JSON file into existing project
        api_instance.import_to_existing_project(project_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectImportApi->import_to_existing_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from JSON file into existing project
        api_instance.import_to_existing_project(project_id, include_attachments=include_attachments, file=file)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectImportApi->import_to_existing_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **include_attachments** | **bool**|  | [optional]
 **file** | **file_type**| Select file | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**413** | Multipart body length limit exceeded |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for project settings required |  -  |
**404** | File not found |  -  |
**409** | Entity with same id already imported in other project |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

