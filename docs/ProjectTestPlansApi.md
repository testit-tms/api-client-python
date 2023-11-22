# testit_api_client.ProjectTestPlansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_project_id_test_plans_analytics_get**](ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_analytics_get) | **GET** /api/v2/projects/{projectId}/testPlans/analytics | Get TestPlans analytics
[**api_v2_projects_project_id_test_plans_delete_bulk_post**](ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_delete_bulk_post) | **POST** /api/v2/projects/{projectId}/testPlans/delete/bulk | Delete multiple test plans
[**api_v2_projects_project_id_test_plans_name_exists_get**](ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_name_exists_get) | **GET** /api/v2/projects/{projectId}/testPlans/{name}/exists | Checks if TestPlan exists with the specified name exists for the project
[**api_v2_projects_project_id_test_plans_purge_bulk_post**](ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_purge_bulk_post) | **POST** /api/v2/projects/{projectId}/testPlans/purge/bulk | Permanently delete multiple archived test plans
[**api_v2_projects_project_id_test_plans_restore_bulk_post**](ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_restore_bulk_post) | **POST** /api/v2/projects/{projectId}/testPlans/restore/bulk | Restore multiple test plans
[**api_v2_projects_project_id_test_plans_search_post**](ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_search_post) | **POST** /api/v2/projects/{projectId}/testPlans/search | Get Project TestPlans with analytics


# **api_v2_projects_project_id_test_plans_analytics_get**
> [TestPlanWithAnalyticModel] api_v2_projects_project_id_test_plans_analytics_get(project_id)

Get TestPlans analytics

<br>Use case  <br>User sets project internal identifier  <br>User sets query params  <br>User runs method execution  <br>System return analytics

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plans_api
from testit_api_client.model.test_plan_with_analytic_model import TestPlanWithAnalyticModel
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
    api_instance = project_test_plans_api.ProjectTestPlansApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) identifier
    is_deleted = True # bool |  (optional)
    must_update_cache = False # bool |  (optional) if omitted the server will use the default value of False
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TestPlans analytics
        api_response = api_instance.api_v2_projects_project_id_test_plans_analytics_get(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_analytics_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TestPlans analytics
        api_response = api_instance.api_v2_projects_project_id_test_plans_analytics_get(project_id, is_deleted=is_deleted, must_update_cache=must_update_cache, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_analytics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) identifier |
 **is_deleted** | **bool**|  | [optional]
 **must_update_cache** | **bool**|  | [optional] if omitted the server will use the default value of False
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestPlanWithAnalyticModel]**](TestPlanWithAnalyticModel.md)

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

# **api_v2_projects_project_id_test_plans_delete_bulk_post**
> [str] api_v2_projects_project_id_test_plans_delete_bulk_post(project_id)

Delete multiple test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_projects_project_id_test_plans_delete_bulk_post_request import ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest
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
    api_instance = project_test_plans_api.ProjectTestPlansApi(api_client)
    project_id = "projectId_example" # str | Unique or global ID of the project
    api_v2_projects_project_id_test_plans_delete_bulk_post_request = ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest(None) # ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete multiple test plans
        api_response = api_instance.api_v2_projects_project_id_test_plans_delete_bulk_post(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_delete_bulk_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete multiple test plans
        api_response = api_instance.api_v2_projects_project_id_test_plans_delete_bulk_post(project_id, api_v2_projects_project_id_test_plans_delete_bulk_post_request=api_v2_projects_project_id_test_plans_delete_bulk_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_delete_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global ID of the project |
 **api_v2_projects_project_id_test_plans_delete_bulk_post_request** | [**ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest**](ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest.md)|  | [optional]

### Return type

**[str]**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | - Read permission for the project is required  - Delete permission for test plans is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_test_plans_name_exists_get**
> bool api_v2_projects_project_id_test_plans_name_exists_get(project_id, name)

Checks if TestPlan exists with the specified name exists for the project

<br>Use case  <br>User sets project internal or global identifier   <br>User runs method execution  <br>System purge delete project workitems

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plans_api
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
    api_instance = project_test_plans_api.ProjectTestPlansApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    name = "name_example" # str | TestPlan name to check

    # example passing only required values which don't have defaults set
    try:
        # Checks if TestPlan exists with the specified name exists for the project
        api_response = api_instance.api_v2_projects_project_id_test_plans_name_exists_get(project_id, name)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_name_exists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **name** | **str**| TestPlan name to check |

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

# **api_v2_projects_project_id_test_plans_purge_bulk_post**
> api_v2_projects_project_id_test_plans_purge_bulk_post(project_id)

Permanently delete multiple archived test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_projects_project_id_test_plans_delete_bulk_post_request import ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest
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
    api_instance = project_test_plans_api.ProjectTestPlansApi(api_client)
    project_id = "projectId_example" # str | Unique or global ID of the project
    api_v2_projects_project_id_test_plans_delete_bulk_post_request = ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest(None) # ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Permanently delete multiple archived test plans
        api_instance.api_v2_projects_project_id_test_plans_purge_bulk_post(project_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_purge_bulk_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Permanently delete multiple archived test plans
        api_instance.api_v2_projects_project_id_test_plans_purge_bulk_post(project_id, api_v2_projects_project_id_test_plans_delete_bulk_post_request=api_v2_projects_project_id_test_plans_delete_bulk_post_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_purge_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global ID of the project |
 **api_v2_projects_project_id_test_plans_delete_bulk_post_request** | [**ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest**](ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest.md)|  | [optional]

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
**403** | Full access permission for the archive is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_test_plans_restore_bulk_post**
> api_v2_projects_project_id_test_plans_restore_bulk_post(project_id)

Restore multiple test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_projects_project_id_test_plans_delete_bulk_post_request import ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest
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
    api_instance = project_test_plans_api.ProjectTestPlansApi(api_client)
    project_id = "projectId_example" # str | Unique or global ID of the project
    api_v2_projects_project_id_test_plans_delete_bulk_post_request = ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest(None) # ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Restore multiple test plans
        api_instance.api_v2_projects_project_id_test_plans_restore_bulk_post(project_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_restore_bulk_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restore multiple test plans
        api_instance.api_v2_projects_project_id_test_plans_restore_bulk_post(project_id, api_v2_projects_project_id_test_plans_delete_bulk_post_request=api_v2_projects_project_id_test_plans_delete_bulk_post_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_restore_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global ID of the project |
 **api_v2_projects_project_id_test_plans_delete_bulk_post_request** | [**ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest**](ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest.md)|  | [optional]

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
**403** | Read permission for the archive is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_test_plans_search_post**
> [TestPlanWithAnalyticModel] api_v2_projects_project_id_test_plans_search_post(project_id)

Get Project TestPlans with analytics

<br>Use case  <br>User sets project internal or global identifier   <br>User sets request body   <br>User runs method execution  <br>System returns project testplans with analytics

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plans_api
from testit_api_client.model.test_plan_with_analytic_model import TestPlanWithAnalyticModel
from testit_api_client.model.api_v2_projects_project_id_test_plans_search_post_request import ApiV2ProjectsProjectIdTestPlansSearchPostRequest
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
    api_instance = project_test_plans_api.ProjectTestPlansApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    must_update_cache = False # bool |  (optional) if omitted the server will use the default value of False
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    api_v2_projects_project_id_test_plans_search_post_request = ApiV2ProjectsProjectIdTestPlansSearchPostRequest(None) # ApiV2ProjectsProjectIdTestPlansSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Project TestPlans with analytics
        api_response = api_instance.api_v2_projects_project_id_test_plans_search_post(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_search_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project TestPlans with analytics
        api_response = api_instance.api_v2_projects_project_id_test_plans_search_post(project_id, must_update_cache=must_update_cache, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, api_v2_projects_project_id_test_plans_search_post_request=api_v2_projects_project_id_test_plans_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **must_update_cache** | **bool**|  | [optional] if omitted the server will use the default value of False
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **api_v2_projects_project_id_test_plans_search_post_request** | [**ApiV2ProjectsProjectIdTestPlansSearchPostRequest**](ApiV2ProjectsProjectIdTestPlansSearchPostRequest.md)|  | [optional]

### Return type

[**[TestPlanWithAnalyticModel]**](TestPlanWithAnalyticModel.md)

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

