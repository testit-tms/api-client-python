# testit_api_client.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_globa_attributes_to_project**](ProjectsApi.md#add_globa_attributes_to_project) | **POST** /api/v2/projects/{id}/globalAttributes | Add global attributes to project
[**api_v2_projects_demo_post**](ProjectsApi.md#api_v2_projects_demo_post) | **POST** /api/v2/projects/demo | 
[**api_v2_projects_id_delete**](ProjectsApi.md#api_v2_projects_id_delete) | **DELETE** /api/v2/projects/{id} | Archive project
[**api_v2_projects_id_failure_classes_get**](ProjectsApi.md#api_v2_projects_id_failure_classes_get) | **GET** /api/v2/projects/{id}/failureClasses | Get failure classes
[**api_v2_projects_id_favorite_put**](ProjectsApi.md#api_v2_projects_id_favorite_put) | **PUT** /api/v2/projects/{id}/favorite | Mark Project as favorite
[**api_v2_projects_id_filters_get**](ProjectsApi.md#api_v2_projects_id_filters_get) | **GET** /api/v2/projects/{id}/filters | Get Project filters
[**api_v2_projects_id_patch**](ProjectsApi.md#api_v2_projects_id_patch) | **PATCH** /api/v2/projects/{id} | Patch project
[**api_v2_projects_id_purge_post**](ProjectsApi.md#api_v2_projects_id_purge_post) | **POST** /api/v2/projects/{id}/purge | Purge archived project
[**api_v2_projects_id_restore_post**](ProjectsApi.md#api_v2_projects_id_restore_post) | **POST** /api/v2/projects/{id}/restore | Restore archived project
[**api_v2_projects_id_test_plans_attribute_attribute_id_delete**](ProjectsApi.md#api_v2_projects_id_test_plans_attribute_attribute_id_delete) | **DELETE** /api/v2/projects/{id}/testPlans/attribute/{attributeId} | Delete attribute from project&#39;s test plans
[**api_v2_projects_id_test_plans_attribute_put**](ProjectsApi.md#api_v2_projects_id_test_plans_attribute_put) | **PUT** /api/v2/projects/{id}/testPlans/attribute | Update attribute of project&#39;s test plans
[**api_v2_projects_id_test_runs_active_get**](ProjectsApi.md#api_v2_projects_id_test_runs_active_get) | **GET** /api/v2/projects/{id}/testRuns/active | Get active Project TestRuns
[**api_v2_projects_id_test_runs_full_get**](ProjectsApi.md#api_v2_projects_id_test_runs_full_get) | **GET** /api/v2/projects/{id}/testRuns/full | Get Project TestRuns full models
[**api_v2_projects_name_name_exists_get**](ProjectsApi.md#api_v2_projects_name_name_exists_get) | **GET** /api/v2/projects/name/{name}/exists | 
[**api_v2_projects_purge_bulk_post**](ProjectsApi.md#api_v2_projects_purge_bulk_post) | **POST** /api/v2/projects/purge/bulk | Purge multiple projects
[**api_v2_projects_restore_bulk_post**](ProjectsApi.md#api_v2_projects_restore_bulk_post) | **POST** /api/v2/projects/restore/bulk | Restore multiple projects
[**api_v2_projects_search_post**](ProjectsApi.md#api_v2_projects_search_post) | **POST** /api/v2/projects/search | Search for projects
[**background_import_project**](ProjectsApi.md#background_import_project) | **POST** /api/v2/projects/import/json | Import project from JSON file in background job
[**background_import_zip_project**](ProjectsApi.md#background_import_zip_project) | **POST** /api/v2/projects/import/zip | Import project from Zip file in background job
[**call_import**](ProjectsApi.md#call_import) | **POST** /api/v2/projects/import | Import project from JSON file
[**create_project**](ProjectsApi.md#create_project) | **POST** /api/v2/projects | Create project
[**delete_project_auto_tests**](ProjectsApi.md#delete_project_auto_tests) | **DELETE** /api/v2/projects/{id}/autoTests | Delete all autotests from project
[**export_with_test_plans_and_configurations**](ProjectsApi.md#export_with_test_plans_and_configurations) | **POST** /api/v2/projects/{id}/export-by-testPlans | Export project with test plans, test suites and test points as JSON file
[**get_all_projects**](ProjectsApi.md#get_all_projects) | **GET** /api/v2/projects | Get all projects
[**get_auto_tests_namespaces**](ProjectsApi.md#get_auto_tests_namespaces) | **GET** /api/v2/projects/{id}/autoTestsNamespaces | Get namespaces of autotests in project
[**get_project_by_id**](ProjectsApi.md#get_project_by_id) | **GET** /api/v2/projects/{id} | Get project by ID
[**get_test_plans_by_project_id**](ProjectsApi.md#get_test_plans_by_project_id) | **GET** /api/v2/projects/{id}/testPlans | Get project test plans
[**get_test_runs_by_project_id**](ProjectsApi.md#get_test_runs_by_project_id) | **GET** /api/v2/projects/{id}/testRuns | Get project test runs
[**update_project**](ProjectsApi.md#update_project) | **PUT** /api/v2/projects | Update project


# **add_globa_attributes_to_project**
> add_globa_attributes_to_project(id)

Add global attributes to project

<br>Use case  <br>User sets project internal or global identifier and attributes identifiers  <br>System search project  <br>System relates global attributes with project  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add global attributes to project
        api_instance.add_globa_attributes_to_project(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->add_globa_attributes_to_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add global attributes to project
        api_instance.add_globa_attributes_to_project(id, request_body=request_body)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->add_globa_attributes_to_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **request_body** | **[str]**|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | &lt;br&gt; Attributes must be global  |  -  |
**403** | Project admin permission for project settings is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Client Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_demo_post**
> ProjectModel api_v2_projects_demo_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_model import ProjectModel
from testit_api_client.model.create_project_request import CreateProjectRequest
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
    api_instance = projects_api.ProjectsApi(api_client)
    create_project_request = CreateProjectRequest(None) # CreateProjectRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_projects_demo_post(create_project_request=create_project_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_demo_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | [optional]

### Return type

[**ProjectModel**](ProjectModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_delete**
> api_v2_projects_id_delete(id)

Archive project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global ID of the project

    # example passing only required values which don't have defaults set
    try:
        # Archive project
        api_instance.api_v2_projects_id_delete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the project |

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Project manager or admin system role is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_failure_classes_get**
> [FailureClassModel] api_v2_projects_id_failure_classes_get(id)

Get failure classes

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.failure_class_model import FailureClassModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global ID of the project
    is_deleted = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get failure classes
        api_response = api_instance.api_v2_projects_id_failure_classes_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_failure_classes_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get failure classes
        api_response = api_instance.api_v2_projects_id_failure_classes_get(id, is_deleted=is_deleted)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_failure_classes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the project |
 **is_deleted** | **bool**|  | [optional]

### Return type

[**[FailureClassModel]**](FailureClassModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Read permission for test library is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_favorite_put**
> api_v2_projects_id_favorite_put(id)

Mark Project as favorite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Mark Project as favorite
        api_instance.api_v2_projects_id_favorite_put(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_favorite_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_filters_get**
> [FilterModel] api_v2_projects_id_filters_get(id)

Get Project filters

<br>Use case  <br>User sets project internal or global identifier   <br>User runs method execution  <br>System returns project filters

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.filter_model import FilterModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get Project filters
        api_response = api_instance.api_v2_projects_id_filters_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_filters_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**[FilterModel]**](FilterModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_patch**
> api_v2_projects_id_patch(id)

Patch project

See <a href=\"https://www.rfc-editor.org/rfc/rfc6902\" target=\"_blank\">RFC 6902: JavaScript Object Notation (JSON) Patch</a> for details

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.operation import Operation
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global Id of project
    operation = [
        Operation(
            value=None,
            path="path_example",
            op="op_example",
            _from="_from_example",
        ),
    ] # [Operation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch project
        api_instance.api_v2_projects_id_patch(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch project
        api_instance.api_v2_projects_id_patch(id, operation=operation)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global Id of project |
 **operation** | [**[Operation]**](Operation.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Update permission for projects is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_purge_post**
> api_v2_projects_id_purge_post(id)

Purge archived project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global ID of the project

    # example passing only required values which don't have defaults set
    try:
        # Purge archived project
        api_instance.api_v2_projects_id_purge_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_purge_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the project |

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**403** | Admin system role is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_restore_post**
> api_v2_projects_id_restore_post(id)

Restore archived project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global ID of the project

    # example passing only required values which don't have defaults set
    try:
        # Restore archived project
        api_instance.api_v2_projects_id_restore_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_restore_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the project |

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Project manager or admin system role is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_plans_attribute_attribute_id_delete**
> api_v2_projects_id_test_plans_attribute_attribute_id_delete(id, attribute_id)

Delete attribute from project's test plans

<br>Use case  <br>User sets project internal or global identifier and attribute identifier  <br>User runs method execution  <br>System updates project and delete attribute from project for test plans  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    attribute_id = "attributeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete attribute from project's test plans
        api_instance.api_v2_projects_id_test_plans_attribute_attribute_id_delete(id, attribute_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_attribute_attribute_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **attribute_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_plans_attribute_put**
> api_v2_projects_id_test_plans_attribute_put(id)

Update attribute of project's test plans

<br>Use case  <br>User sets project internal or global identifier and attribute model  <br>User runs method execution  <br>System updates project and project attribute for test plan  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.update_custom_attribute_test_plan_project_relations_request import UpdateCustomAttributeTestPlanProjectRelationsRequest
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    update_custom_attribute_test_plan_project_relations_request = UpdateCustomAttributeTestPlanProjectRelationsRequest(None) # UpdateCustomAttributeTestPlanProjectRelationsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update attribute of project's test plans
        api_instance.api_v2_projects_id_test_plans_attribute_put(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_attribute_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update attribute of project's test plans
        api_instance.api_v2_projects_id_test_plans_attribute_put(id, update_custom_attribute_test_plan_project_relations_request=update_custom_attribute_test_plan_project_relations_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_attribute_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **update_custom_attribute_test_plan_project_relations_request** | [**UpdateCustomAttributeTestPlanProjectRelationsRequest**](UpdateCustomAttributeTestPlanProjectRelationsRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_runs_active_get**
> [PublicTestRunModel] api_v2_projects_id_test_runs_active_get(id)

Get active Project TestRuns

<br>Use case  <br>User sets project internal or global identifier   <br>User runs method execution  <br>System returns active testruns

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.public_test_run_model import PublicTestRunModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get active Project TestRuns
        api_response = api_instance.api_v2_projects_id_test_runs_active_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_runs_active_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**[PublicTestRunModel]**](PublicTestRunModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_runs_full_get**
> [TestRunModel] api_v2_projects_id_test_runs_full_get(id)

Get Project TestRuns full models

<br>Use case  <br>User sets project internal or global identifier   <br>User sets query params   <br>User runs method execution  <br>System returns project test runs full models

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.test_run_model import TestRunModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    include_test_results = False # bool |  (optional) if omitted the server will use the default value of False
    must_aggregate_test_results = True # bool |  (optional) if omitted the server will use the default value of True
    not_started = True # bool |  (optional)
    in_progress = True # bool |  (optional)
    stopped = True # bool |  (optional)
    completed = True # bool |  (optional)
    created_date_from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    created_date_to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    test_plan_id = "testPlanId_example" # str |  (optional)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Project TestRuns full models
        api_response = api_instance.api_v2_projects_id_test_runs_full_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_runs_full_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project TestRuns full models
        api_response = api_instance.api_v2_projects_id_test_runs_full_get(id, include_test_results=include_test_results, must_aggregate_test_results=must_aggregate_test_results, not_started=not_started, in_progress=in_progress, stopped=stopped, completed=completed, created_date_from=created_date_from, created_date_to=created_date_to, test_plan_id=test_plan_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_runs_full_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **include_test_results** | **bool**|  | [optional] if omitted the server will use the default value of False
 **must_aggregate_test_results** | **bool**|  | [optional] if omitted the server will use the default value of True
 **not_started** | **bool**|  | [optional]
 **in_progress** | **bool**|  | [optional]
 **stopped** | **bool**|  | [optional]
 **completed** | **bool**|  | [optional]
 **created_date_from** | **datetime**|  | [optional]
 **created_date_to** | **datetime**|  | [optional]
 **test_plan_id** | **str**|  | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestRunModel]**](TestRunModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_name_name_exists_get**
> bool api_v2_projects_name_name_exists_get(name)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_projects_name_name_exists_get(name)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_name_name_exists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

**bool**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_purge_bulk_post**
> int api_v2_projects_purge_bulk_post()

Purge multiple projects

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.api_v2_projects_restore_bulk_post_request import ApiV2ProjectsRestoreBulkPostRequest
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
    api_instance = projects_api.ProjectsApi(api_client)
    api_v2_projects_restore_bulk_post_request = ApiV2ProjectsRestoreBulkPostRequest(None) # ApiV2ProjectsRestoreBulkPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Purge multiple projects
        api_response = api_instance.api_v2_projects_purge_bulk_post(api_v2_projects_restore_bulk_post_request=api_v2_projects_restore_bulk_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_purge_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_projects_restore_bulk_post_request** | [**ApiV2ProjectsRestoreBulkPostRequest**](ApiV2ProjectsRestoreBulkPostRequest.md)|  | [optional]

### Return type

**int**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Admin system role is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_restore_bulk_post**
> int api_v2_projects_restore_bulk_post()

Restore multiple projects

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.api_v2_projects_restore_bulk_post_request import ApiV2ProjectsRestoreBulkPostRequest
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
    api_instance = projects_api.ProjectsApi(api_client)
    api_v2_projects_restore_bulk_post_request = ApiV2ProjectsRestoreBulkPostRequest(None) # ApiV2ProjectsRestoreBulkPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restore multiple projects
        api_response = api_instance.api_v2_projects_restore_bulk_post(api_v2_projects_restore_bulk_post_request=api_v2_projects_restore_bulk_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_restore_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_projects_restore_bulk_post_request** | [**ApiV2ProjectsRestoreBulkPostRequest**](ApiV2ProjectsRestoreBulkPostRequest.md)|  | [optional]

### Return type

**int**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Project manager or admin system role is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_search_post**
> [ProjectModel] api_v2_projects_search_post()

Search for projects

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_model import ProjectModel
from testit_api_client.model.api_v2_projects_search_post_request import ApiV2ProjectsSearchPostRequest
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
    api_instance = projects_api.ProjectsApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    api_v2_projects_search_post_request = ApiV2ProjectsSearchPostRequest(None) # ApiV2ProjectsSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for projects
        api_response = api_instance.api_v2_projects_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, api_v2_projects_search_post_request=api_v2_projects_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **api_v2_projects_search_post_request** | [**ApiV2ProjectsSearchPostRequest**](ApiV2ProjectsSearchPostRequest.md)|  | [optional]

### Return type

[**[ProjectModel]**](ProjectModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **background_import_project**
> str background_import_project()

Import project from JSON file in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from JSON file in background job
        api_response = api_instance.background_import_project(file=file)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->background_import_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **background_import_zip_project**
> str background_import_zip_project()

Import project from Zip file in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from Zip file in background job
        api_response = api_instance.background_import_zip_project(file=file)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->background_import_zip_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_import**
> call_import()

Import project from JSON file

<br>    <b>A project can only be exported to another TMS instance, different from the one it was imported from.</b>    <br>This method imports a `.json` file with a project to the test management system.  <br>In the body of the request, send the `.json` file received by the `POST /api/v2/projects/export` method:  <br>    ```              curl -X POST \"http://{domain.com}/api/v2/projects/import\" \\              -H \"accept: /\" -H \"Authorization: PrivateToken {token}\" -H \"Content-Type: multipart/form-data\" \\              -F \"file=@import.txt;type=text/plain\"              ```    <br>              In the second instance, a project with the name of the imported one is created.              User attributes and the test library (along with content and structure) are imported.                <br>Test plan execution history from the first instance of TMS cannot be transferred.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    include_attachments = False # bool | Enables attachment import. (optional) if omitted the server will use the default value of False
    file = open('/path/to/file', 'rb') # file_type | Select file (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from JSON file
        api_instance.call_import(include_attachments=include_attachments, file=file)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->call_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_attachments** | **bool**| Enables attachment import. | [optional] if omitted the server will use the default value of False
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
**400** | Bad Request |  -  |
**403** | Project creator or admin system role is required |  -  |
**409** | Entity with the same ID was already imported in other project |  -  |
**413** | Multipart body length limit exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> ProjectModel create_project()

Create project

<br>Use case  <br>User sets project parameters (listed in request example) and runs method execution  <br>System creates project  <br>System returns project model (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_model import ProjectModel
from testit_api_client.model.create_project_request import CreateProjectRequest
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
    api_instance = projects_api.ProjectsApi(api_client)
    create_project_request = CreateProjectRequest(None) # CreateProjectRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create project
        api_response = api_instance.create_project(create_project_request=create_project_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project_request** | [**CreateProjectRequest**](CreateProjectRequest.md)|  | [optional]

### Return type

[**ProjectModel**](ProjectModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Project creator or admin system role is required |  -  |
**409** | Project with the same name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_auto_tests**
> delete_project_auto_tests(id)

Delete all autotests from project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global ID of the project

    # example passing only required values which don't have defaults set
    try:
        # Delete all autotests from project
        api_instance.delete_project_auto_tests(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->delete_project_auto_tests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the project |

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Delete permission for AutoTest is required |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_with_test_plans_and_configurations**
> file_type export_with_test_plans_and_configurations(id)

Export project with test plans, test suites and test points as JSON file

<br>    <b>You cannot export test cases execution history.</b>    <br>This method exports the project with the test library and specified test plans to another TMS instance.  <br>              After sending a correct request, the project is exported to a `.json` file.              If you enable attachment export, the `.json` file and the attachments are placed in a `.zip` file.              You can import such a project by using the `POST /api/v2/projects/import` method.              

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.export_project_with_test_plans_json_request import ExportProjectWithTestPlansJsonRequest
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Specifies the ID of the project you want to export.
    include_attachments = False # bool | Enables attachment export. (optional) if omitted the server will use the default value of False
    export_project_with_test_plans_json_request = ExportProjectWithTestPlansJsonRequest(None) # ExportProjectWithTestPlansJsonRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project with test plans, test suites and test points as JSON file
        api_response = api_instance.export_with_test_plans_and_configurations(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_with_test_plans_and_configurations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project with test plans, test suites and test points as JSON file
        api_response = api_instance.export_with_test_plans_and_configurations(id, include_attachments=include_attachments, export_project_with_test_plans_json_request=export_project_with_test_plans_json_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_with_test_plans_and_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the ID of the project you want to export. |
 **include_attachments** | **bool**| Enables attachment export. | [optional] if omitted the server will use the default value of False
 **export_project_with_test_plans_json_request** | [**ExportProjectWithTestPlansJsonRequest**](ExportProjectWithTestPlansJsonRequest.md)|  | [optional]

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
**400** | Root section was not found |  -  |
**403** | Update permission for project settings is required |  -  |
**404** | Project with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> [ProjectModel] get_all_projects()

Get all projects

<br>Use case  <br>[Optional] User sets isDeleted field value  <br>[Optional] If User sets isDeleted field value as true, System search all deleted projects  <br>[Optional] If User sets isDeleted field value as false, System search all projects which are not deleted  <br>If User did not set isDeleted field value, System search all projects  <br>System returns array of all found projects(listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_model import ProjectModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    is_deleted = True # bool | If result must consist of only actual/deleted parameters (optional)
    project_name = "projectName_example" # str |  (optional)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all projects
        api_response = api_instance.get_all_projects(is_deleted=is_deleted, project_name=project_name, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_all_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_deleted** | **bool**| If result must consist of only actual/deleted parameters | [optional]
 **project_name** | **str**|  | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[ProjectModel]**](ProjectModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**403** | Invalid user permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_tests_namespaces**
> [AutoTestNamespaceModel] get_auto_tests_namespaces(id)

Get namespaces of autotests in project

<br>Use case  <br>User sets project internal or global identifier and runs method execution  <br>System search project  <br>System search all autotest related to the project  <br>System returns array of autotest with namespaces and classnames (listed in response)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.auto_test_namespace_model import AutoTestNamespaceModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get namespaces of autotests in project
        api_response = api_instance.get_auto_tests_namespaces(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_auto_tests_namespaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**[AutoTestNamespaceModel]**](AutoTestNamespaceModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Project with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_id**
> ProjectModel get_project_by_id(id)

Get project by ID

<br>Use case  <br>User sets project internal or global identifier and runs method execution  <br>System search project  <br>System returns project (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_model import ProjectModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get project by ID
        api_response = api_instance.get_project_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**ProjectModel**](ProjectModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | ID is invalid |  -  |
**403** | Read permission for projects is required |  -  |
**404** | Project with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_plans_by_project_id**
> [TestPlanModel] get_test_plans_by_project_id(id)

Get project test plans

<br>Use case  <br>User sets project internal or global identifier  <br>[Optional] User sets isDeleted field value  <br>User runs method execution  <br>System search project  <br>[Optional] If User sets isDeleted field value as true, System search all deleted test plans related to project  <br>[Optional] If User sets isDeleted field value as false, System search all test plans related to project which are not deleted  <br>[Optional] If User did not set isDeleted field value, System search all v related to project  <br>System returns array of found test plans (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_plan_model import TestPlanModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    is_deleted = True # bool | If result must consist of only actual/archived test plans (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get project test plans
        api_response = api_instance.get_test_plans_by_project_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_test_plans_by_project_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get project test plans
        api_response = api_instance.get_test_plans_by_project_id(id, is_deleted=is_deleted)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_test_plans_by_project_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **is_deleted** | **bool**| If result must consist of only actual/archived test plans | [optional]

### Return type

[**[TestPlanModel]**](TestPlanModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Project with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_runs_by_project_id**
> [TestRunV2GetModel] get_test_runs_by_project_id(id)

Get project test runs

<br>Use case  <br>User sets project internal or global identifier  <br>User runs method execution  <br>System search project  <br>System search all test runs related to project  <br>System returns array of found test runs (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.test_run_v2_get_model import TestRunV2GetModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    not_started = True # bool |  (optional)
    in_progress = True # bool |  (optional)
    stopped = True # bool |  (optional)
    completed = True # bool |  (optional)
    created_date_from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    created_date_to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    test_plan_id = "testPlanId_example" # str |  (optional)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get project test runs
        api_response = api_instance.get_test_runs_by_project_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_test_runs_by_project_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get project test runs
        api_response = api_instance.get_test_runs_by_project_id(id, not_started=not_started, in_progress=in_progress, stopped=stopped, completed=completed, created_date_from=created_date_from, created_date_to=created_date_to, test_plan_id=test_plan_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_test_runs_by_project_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **not_started** | **bool**|  | [optional]
 **in_progress** | **bool**|  | [optional]
 **stopped** | **bool**|  | [optional]
 **completed** | **bool**|  | [optional]
 **created_date_from** | **datetime**|  | [optional]
 **created_date_to** | **datetime**|  | [optional]
 **test_plan_id** | **str**|  | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestRunV2GetModel]**](TestRunV2GetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**403** | Read permission for test result is required |  -  |
**404** | Project with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> update_project()

Update project

<br>Use case  <br>User sets project parameters (listed in request example) and runs method execution  <br>System updates project  <br>System returns updated project model (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.update_project_request import UpdateProjectRequest
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
    api_instance = projects_api.ProjectsApi(api_client)
    update_project_request = UpdateProjectRequest(None) # UpdateProjectRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update project
        api_instance.update_project(update_project_request=update_project_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_project_request** | [**UpdateProjectRequest**](UpdateProjectRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | &lt;br&gt;- ID is invalid  &lt;br&gt;- Field is required |  -  |
**403** | Update permission for projects is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Project with the same name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

