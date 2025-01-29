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
[**api_v2_projects_id_purge_post**](ProjectsApi.md#api_v2_projects_id_purge_post) | **POST** /api/v2/projects/{id}/purge | Purge the project
[**api_v2_projects_id_restore_post**](ProjectsApi.md#api_v2_projects_id_restore_post) | **POST** /api/v2/projects/{id}/restore | Restore archived project
[**api_v2_projects_id_test_plans_attribute_attribute_id_delete**](ProjectsApi.md#api_v2_projects_id_test_plans_attribute_attribute_id_delete) | **DELETE** /api/v2/projects/{id}/testPlans/attribute/{attributeId} | Delete attribute from project&#39;s test plans
[**api_v2_projects_id_test_plans_attribute_put**](ProjectsApi.md#api_v2_projects_id_test_plans_attribute_put) | **PUT** /api/v2/projects/{id}/testPlans/attribute | Update attribute of project&#39;s test plans
[**api_v2_projects_id_test_runs_active_get**](ProjectsApi.md#api_v2_projects_id_test_runs_active_get) | **GET** /api/v2/projects/{id}/testRuns/active | Get active Project TestRuns
[**api_v2_projects_id_test_runs_full_get**](ProjectsApi.md#api_v2_projects_id_test_runs_full_get) | **GET** /api/v2/projects/{id}/testRuns/full | Get Project TestRuns full models
[**api_v2_projects_name_name_exists_get**](ProjectsApi.md#api_v2_projects_name_name_exists_get) | **GET** /api/v2/projects/name/{name}/exists | 
[**api_v2_projects_purge_bulk_post**](ProjectsApi.md#api_v2_projects_purge_bulk_post) | **POST** /api/v2/projects/purge/bulk | Purge multiple projects
[**api_v2_projects_restore_bulk_post**](ProjectsApi.md#api_v2_projects_restore_bulk_post) | **POST** /api/v2/projects/restore/bulk | Restore multiple projects
[**api_v2_projects_search_post**](ProjectsApi.md#api_v2_projects_search_post) | **POST** /api/v2/projects/search | Search for projects
[**create_project**](ProjectsApi.md#create_project) | **POST** /api/v2/projects | Create project
[**delete_project_auto_tests**](ProjectsApi.md#delete_project_auto_tests) | **DELETE** /api/v2/projects/{id}/autoTests | Delete all autotests from project
[**get_all_projects**](ProjectsApi.md#get_all_projects) | **GET** /api/v2/projects | Get all projects
[**get_auto_tests_namespaces**](ProjectsApi.md#get_auto_tests_namespaces) | **GET** /api/v2/projects/{id}/autoTestsNamespaces | Get namespaces of autotests in project
[**get_project_by_id**](ProjectsApi.md#get_project_by_id) | **GET** /api/v2/projects/{id} | Get project by ID
[**get_test_plans_by_project_id**](ProjectsApi.md#get_test_plans_by_project_id) | **GET** /api/v2/projects/{id}/testPlans | Get project test plans
[**get_test_runs_by_project_id**](ProjectsApi.md#get_test_runs_by_project_id) | **GET** /api/v2/projects/{id}/testRuns | Get project test runs
[**update_project**](ProjectsApi.md#update_project) | **PUT** /api/v2/projects | Update project


# **add_globa_attributes_to_project**
> add_globa_attributes_to_project(id, request_body=request_body)

Add global attributes to project

 Use case   User sets project internal or global identifier and attributes identifiers   System search project   System relates global attributes with project   System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Add global attributes to project
        api_instance.add_globa_attributes_to_project(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_globa_attributes_to_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

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
**400** |   Attributes must be global  |  -  |
**401** | Unauthorized |  -  |
**403** | Project admin permission for project settings is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_demo_post**
> ProjectModel api_v2_projects_demo_post(project_post_model=project_post_model)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.project_model import ProjectModel
from testit_api_client.models.project_post_model import ProjectPostModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    project_post_model = testit_api_client.ProjectPostModel() # ProjectPostModel |  (optional)

    try:
        api_response = api_instance.api_v2_projects_demo_post(project_post_model=project_post_model)
        print("The response of ProjectsApi->api_v2_projects_demo_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_demo_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_post_model** | [**ProjectPostModel**](ProjectPostModel.md)|  | [optional] 

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
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_delete**
> api_v2_projects_id_delete(id)

Archive project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Unique or global ID of the project

    try:
        # Archive project
        api_instance.api_v2_projects_id_delete(id)
    except Exception as e:
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Project manager or admin system role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_failure_classes_get**
> List[FailureClassModel] api_v2_projects_id_failure_classes_get(id, is_deleted=is_deleted)

Get failure classes

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.failure_class_model import FailureClassModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Unique or global ID of the project
    is_deleted = True # bool |  (optional)

    try:
        # Get failure classes
        api_response = api_instance.api_v2_projects_id_failure_classes_get(id, is_deleted=is_deleted)
        print("The response of ProjectsApi->api_v2_projects_id_failure_classes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_failure_classes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the project | 
 **is_deleted** | **bool**|  | [optional] 

### Return type

[**List[FailureClassModel]**](FailureClassModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_favorite_put**
> api_v2_projects_id_favorite_put(id)

Mark Project as favorite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier

    try:
        # Mark Project as favorite
        api_instance.api_v2_projects_id_favorite_put(id)
    except Exception as e:
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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_filters_get**
> List[FilterModel] api_v2_projects_id_filters_get(id)

Get Project filters

 Use case   User sets project internal or global identifier    User runs method execution   System returns project filters

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.filter_model import FilterModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier

    try:
        # Get Project filters
        api_response = api_instance.api_v2_projects_id_filters_get(id)
        print("The response of ProjectsApi->api_v2_projects_id_filters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_filters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier | 

### Return type

[**List[FilterModel]**](FilterModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_patch**
> api_v2_projects_id_patch(id, operation=operation)

Patch project

See <a href=\"https://www.rfc-editor.org/rfc/rfc6902\" target=\"_blank\">RFC 6902: JavaScript Object Notation (JSON) Patch</a> for details

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.operation import Operation
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Unique or global Id of project
    operation = [testit_api_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch project
        api_instance.api_v2_projects_id_patch(id, operation=operation)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global Id of project | 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for projects is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_purge_post**
> api_v2_projects_id_purge_post(id)

Purge the project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Unique or global ID of the project

    try:
        # Purge the project
        api_instance.api_v2_projects_id_purge_post(id)
    except Exception as e:
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Admin system role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_restore_post**
> api_v2_projects_id_restore_post(id)

Restore archived project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Unique or global ID of the project

    try:
        # Restore archived project
        api_instance.api_v2_projects_id_restore_post(id)
    except Exception as e:
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Project manager or admin system role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_plans_attribute_attribute_id_delete**
> api_v2_projects_id_test_plans_attribute_attribute_id_delete(id, attribute_id)

Delete attribute from project's test plans

 Use case   User sets project internal or global identifier and attribute identifier   User runs method execution   System updates project and delete attribute from project for test plans   System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier
    attribute_id = 'attribute_id_example' # str | 

    try:
        # Delete attribute from project's test plans
        api_instance.api_v2_projects_id_test_plans_attribute_attribute_id_delete(id, attribute_id)
    except Exception as e:
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for project settings is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_plans_attribute_put**
> api_v2_projects_id_test_plans_attribute_put(id, custom_attribute_test_plan_project_relation_put_model=custom_attribute_test_plan_project_relation_put_model)

Update attribute of project's test plans

 Use case   User sets project internal or global identifier and attribute model   User runs method execution   System updates project and project attribute for test plan   System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.custom_attribute_test_plan_project_relation_put_model import CustomAttributeTestPlanProjectRelationPutModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier
    custom_attribute_test_plan_project_relation_put_model = testit_api_client.CustomAttributeTestPlanProjectRelationPutModel() # CustomAttributeTestPlanProjectRelationPutModel |  (optional)

    try:
        # Update attribute of project's test plans
        api_instance.api_v2_projects_id_test_plans_attribute_put(id, custom_attribute_test_plan_project_relation_put_model=custom_attribute_test_plan_project_relation_put_model)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_attribute_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **custom_attribute_test_plan_project_relation_put_model** | [**CustomAttributeTestPlanProjectRelationPutModel**](CustomAttributeTestPlanProjectRelationPutModel.md)|  | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for project settings is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_runs_active_get**
> List[PublicTestRunModel] api_v2_projects_id_test_runs_active_get(id)

Get active Project TestRuns

 Use case   User sets project internal or global identifier    User runs method execution   System returns active testruns

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.public_test_run_model import PublicTestRunModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier

    try:
        # Get active Project TestRuns
        api_response = api_instance.api_v2_projects_id_test_runs_active_get(id)
        print("The response of ProjectsApi->api_v2_projects_id_test_runs_active_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_runs_active_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier | 

### Return type

[**List[PublicTestRunModel]**](PublicTestRunModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_runs_full_get**
> List[TestRunApiResult] api_v2_projects_id_test_runs_full_get(id, include_test_results=include_test_results, must_aggregate_test_results=must_aggregate_test_results, not_started=not_started, in_progress=in_progress, stopped=stopped, completed=completed, created_date_from=created_date_from, created_date_to=created_date_to, test_plan_id=test_plan_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get Project TestRuns full models

 Use case   User sets project internal or global identifier    User sets query params    User runs method execution   System returns project test runs full models

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_run_api_result import TestRunApiResult
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier
    include_test_results = True # bool |  (optional)
    must_aggregate_test_results = True # bool |  (optional)
    not_started = True # bool |  (optional)
    in_progress = True # bool |  (optional)
    stopped = True # bool |  (optional)
    completed = True # bool |  (optional)
    created_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    test_plan_id = 'test_plan_id_example' # str |  (optional)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get Project TestRuns full models
        api_response = api_instance.api_v2_projects_id_test_runs_full_get(id, include_test_results=include_test_results, must_aggregate_test_results=must_aggregate_test_results, not_started=not_started, in_progress=in_progress, stopped=stopped, completed=completed, created_date_from=created_date_from, created_date_to=created_date_to, test_plan_id=test_plan_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of ProjectsApi->api_v2_projects_id_test_runs_full_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_runs_full_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **include_test_results** | **bool**|  | [optional] 
 **must_aggregate_test_results** | **bool**|  | [optional] 
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

[**List[TestRunApiResult]**](TestRunApiResult.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_name_name_exists_get**
> bool api_v2_projects_name_name_exists_get(name)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    name = 'name_example' # str | 

    try:
        api_response = api_instance.api_v2_projects_name_name_exists_get(name)
        print("The response of ProjectsApi->api_v2_projects_name_name_exists_get:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_purge_bulk_post**
> int api_v2_projects_purge_bulk_post(project_select_model=project_select_model)

Purge multiple projects

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.project_select_model import ProjectSelectModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    project_select_model = testit_api_client.ProjectSelectModel() # ProjectSelectModel |  (optional)

    try:
        # Purge multiple projects
        api_response = api_instance.api_v2_projects_purge_bulk_post(project_select_model=project_select_model)
        print("The response of ProjectsApi->api_v2_projects_purge_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_purge_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_select_model** | [**ProjectSelectModel**](ProjectSelectModel.md)|  | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Admin system role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_restore_bulk_post**
> int api_v2_projects_restore_bulk_post(project_select_model=project_select_model)

Restore multiple projects

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.project_select_model import ProjectSelectModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    project_select_model = testit_api_client.ProjectSelectModel() # ProjectSelectModel |  (optional)

    try:
        # Restore multiple projects
        api_response = api_instance.api_v2_projects_restore_bulk_post(project_select_model=project_select_model)
        print("The response of ProjectsApi->api_v2_projects_restore_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->api_v2_projects_restore_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_select_model** | [**ProjectSelectModel**](ProjectSelectModel.md)|  | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Project manager or admin system role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_search_post**
> List[ProjectShortModel] api_v2_projects_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, projects_filter_model=projects_filter_model)

Search for projects

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.project_short_model import ProjectShortModel
from testit_api_client.models.projects_filter_model import ProjectsFilterModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    projects_filter_model = testit_api_client.ProjectsFilterModel() # ProjectsFilterModel |  (optional)

    try:
        # Search for projects
        api_response = api_instance.api_v2_projects_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, projects_filter_model=projects_filter_model)
        print("The response of ProjectsApi->api_v2_projects_search_post:\n")
        pprint(api_response)
    except Exception as e:
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
 **projects_filter_model** | [**ProjectsFilterModel**](ProjectsFilterModel.md)|  | [optional] 

### Return type

[**List[ProjectShortModel]**](ProjectShortModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> ProjectModel create_project(project_post_model=project_post_model)

Create project

 Use case   User sets project parameters (listed in request example) and runs method execution   System creates project   System returns project model (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.project_model import ProjectModel
from testit_api_client.models.project_post_model import ProjectPostModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    project_post_model = testit_api_client.ProjectPostModel() # ProjectPostModel |  (optional)

    try:
        # Create project
        api_response = api_instance.create_project(project_post_model=project_post_model)
        print("The response of ProjectsApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_post_model** | [**ProjectPostModel**](ProjectPostModel.md)|  | [optional] 

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
**401** | Unauthorized |  -  |
**403** | Project creator or admin system role is required |  -  |
**404** | Not Found |  -  |
**409** | Project with the same name already exists |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_auto_tests**
> delete_project_auto_tests(id)

Delete all autotests from project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Unique or global ID of the project

    try:
        # Delete all autotests from project
        api_instance.delete_project_auto_tests(id)
    except Exception as e:
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Delete permission for AutoTest is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> List[ProjectShortModel] get_all_projects(is_deleted=is_deleted, project_name=project_name, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get all projects

 Use case   [Optional] User sets isDeleted field value   [Optional] If User sets isDeleted field value as true, System search all deleted projects   [Optional] If User sets isDeleted field value as false, System search all projects which are not deleted   If User did not set isDeleted field value, System search all projects   System returns array of all found projects(listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.project_short_model import ProjectShortModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    is_deleted = True # bool | If result must consist of only actual/deleted parameters (optional)
    project_name = 'project_name_example' # str |  (optional)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get all projects
        api_response = api_instance.get_all_projects(is_deleted=is_deleted, project_name=project_name, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of ProjectsApi->get_all_projects:\n")
        pprint(api_response)
    except Exception as e:
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

[**List[ProjectShortModel]**](ProjectShortModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Invalid user permissions |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_tests_namespaces**
> List[AutoTestNamespaceModel] get_auto_tests_namespaces(id)

Get namespaces of autotests in project

 Use case   User sets project internal or global identifier and runs method execution   System search project   System search all autotest related to the project   System returns array of autotest with namespaces and classnames (listed in response)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_namespace_model import AutoTestNamespaceModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier

    try:
        # Get namespaces of autotests in project
        api_response = api_instance.get_auto_tests_namespaces(id)
        print("The response of ProjectsApi->get_auto_tests_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_auto_tests_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier | 

### Return type

[**List[AutoTestNamespaceModel]**](AutoTestNamespaceModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_id**
> ProjectModel get_project_by_id(id)

Get project by ID

 Use case   User sets project internal or global identifier and runs method execution   System search project   System returns project (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.project_model import ProjectModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier

    try:
        # Get project by ID
        api_response = api_instance.get_project_by_id(id)
        print("The response of ProjectsApi->get_project_by_id:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | OK |  -  |
**404** | Project with provided ID was not found |  -  |
**400** | ID is invalid |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for projects is required |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_plans_by_project_id**
> List[TestPlanModel] get_test_plans_by_project_id(id, is_deleted=is_deleted)

Get project test plans

 Use case   User sets project internal or global identifier   [Optional] User sets isDeleted field value   User runs method execution   System search project   [Optional] If User sets isDeleted field value as true, System search all deleted test plans related to project   [Optional] If User sets isDeleted field value as false, System search all test plans related to project which are not deleted   [Optional] If User did not set isDeleted field value, System search all v related to project   System returns array of found test plans (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_plan_model import TestPlanModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier
    is_deleted = True # bool | If result must consist of only actual/archived test plans (optional)

    try:
        # Get project test plans
        api_response = api_instance.get_test_plans_by_project_id(id, is_deleted=is_deleted)
        print("The response of ProjectsApi->get_test_plans_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_test_plans_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **is_deleted** | **bool**| If result must consist of only actual/archived test plans | [optional] 

### Return type

[**List[TestPlanModel]**](TestPlanModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_runs_by_project_id**
> List[TestRunV2ApiResult] get_test_runs_by_project_id(id, not_started, in_progress, stopped, completed, created_date_from=created_date_from, created_date_to=created_date_to, test_plan_id=test_plan_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get project test runs

 Use case   User sets project internal or global identifier   User runs method execution   System search project   System search all test runs related to project   System returns array of found test runs (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_run_v2_api_result import TestRunV2ApiResult
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    id = 'id_example' # str | Project internal (UUID) or global (integer) identifier
    not_started = True # bool | 
    in_progress = True # bool | 
    stopped = True # bool | 
    completed = True # bool | 
    created_date_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_date_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    test_plan_id = 'test_plan_id_example' # str |  (optional)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get project test runs
        api_response = api_instance.get_test_runs_by_project_id(id, not_started, in_progress, stopped, completed, created_date_from=created_date_from, created_date_to=created_date_to, test_plan_id=test_plan_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of ProjectsApi->get_test_runs_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_test_runs_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **not_started** | **bool**|  | 
 **in_progress** | **bool**|  | 
 **stopped** | **bool**|  | 
 **completed** | **bool**|  | 
 **created_date_from** | **datetime**|  | [optional] 
 **created_date_to** | **datetime**|  | [optional] 
 **test_plan_id** | **str**|  | [optional] 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 

### Return type

[**List[TestRunV2ApiResult]**](TestRunV2ApiResult.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test result is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> update_project(project_put_model=project_put_model)

Update project

 Use case   User sets project parameters (listed in request example) and runs method execution   System updates project   System returns updated project model (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.project_put_model import ProjectPutModel
from testit_api_client.rest import ApiException
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
configuration.api_key['Bearer or PrivateToken'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer or PrivateToken'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = testit_api_client.ProjectsApi(api_client)
    project_put_model = testit_api_client.ProjectPutModel() # ProjectPutModel |  (optional)

    try:
        # Update project
        api_instance.update_project(project_put_model=project_put_model)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_put_model** | [**ProjectPutModel**](ProjectPutModel.md)|  | [optional] 

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
**400** |  - ID is invalid   - Field is required |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for projects is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Project with the same name already exists |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

