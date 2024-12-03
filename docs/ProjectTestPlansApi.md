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
> List[TestPlanWithAnalyticModel] api_v2_projects_project_id_test_plans_analytics_get(project_id, is_deleted=is_deleted, must_update_cache=must_update_cache, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get TestPlans analytics

 Use case   User sets project internal identifier   User sets query params   User runs method execution   System return analytics

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_plan_with_analytic_model import TestPlanWithAnalyticModel
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
    api_instance = testit_api_client.ProjectTestPlansApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) identifier
    is_deleted = True # bool |  (optional)
    must_update_cache = False # bool |  (optional) (default to False)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get TestPlans analytics
        api_response = api_instance.api_v2_projects_project_id_test_plans_analytics_get(project_id, is_deleted=is_deleted, must_update_cache=must_update_cache, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of ProjectTestPlansApi->api_v2_projects_project_id_test_plans_analytics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_analytics_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) identifier | 
 **is_deleted** | **bool**|  | [optional] 
 **must_update_cache** | **bool**|  | [optional] [default to False]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 

### Return type

[**List[TestPlanWithAnalyticModel]**](TestPlanWithAnalyticModel.md)

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

# **api_v2_projects_project_id_test_plans_delete_bulk_post**
> List[str] api_v2_projects_project_id_test_plans_delete_bulk_post(project_id, test_plan_select_model=test_plan_select_model)

Delete multiple test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_plan_select_model import TestPlanSelectModel
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
    api_instance = testit_api_client.ProjectTestPlansApi(api_client)
    project_id = 'project_id_example' # str | Unique or global ID of the project
    test_plan_select_model = testit_api_client.TestPlanSelectModel() # TestPlanSelectModel |  (optional)

    try:
        # Delete multiple test plans
        api_response = api_instance.api_v2_projects_project_id_test_plans_delete_bulk_post(project_id, test_plan_select_model=test_plan_select_model)
        print("The response of ProjectTestPlansApi->api_v2_projects_project_id_test_plans_delete_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_delete_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global ID of the project | 
 **test_plan_select_model** | [**TestPlanSelectModel**](TestPlanSelectModel.md)|  | [optional] 

### Return type

**List[str]**

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
**403** | - Read permission for the project is required  - Delete permission for test plans is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_test_plans_name_exists_get**
> bool api_v2_projects_project_id_test_plans_name_exists_get(project_id, name)

Checks if TestPlan exists with the specified name exists for the project

 Use case   User sets project internal or global identifier    User runs method execution   System purge delete project workitems

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
    api_instance = testit_api_client.ProjectTestPlansApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier
    name = 'name_example' # str | TestPlan name to check

    try:
        # Checks if TestPlan exists with the specified name exists for the project
        api_response = api_instance.api_v2_projects_project_id_test_plans_name_exists_get(project_id, name)
        print("The response of ProjectTestPlansApi->api_v2_projects_project_id_test_plans_name_exists_get:\n")
        pprint(api_response)
    except Exception as e:
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_test_plans_purge_bulk_post**
> api_v2_projects_project_id_test_plans_purge_bulk_post(project_id, test_plan_select_model=test_plan_select_model)

Permanently delete multiple archived test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_plan_select_model import TestPlanSelectModel
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
    api_instance = testit_api_client.ProjectTestPlansApi(api_client)
    project_id = 'project_id_example' # str | Unique or global ID of the project
    test_plan_select_model = testit_api_client.TestPlanSelectModel() # TestPlanSelectModel |  (optional)

    try:
        # Permanently delete multiple archived test plans
        api_instance.api_v2_projects_project_id_test_plans_purge_bulk_post(project_id, test_plan_select_model=test_plan_select_model)
    except Exception as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_purge_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global ID of the project | 
 **test_plan_select_model** | [**TestPlanSelectModel**](TestPlanSelectModel.md)|  | [optional] 

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
**403** | Full access permission for the archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_test_plans_restore_bulk_post**
> List[str] api_v2_projects_project_id_test_plans_restore_bulk_post(project_id, test_plan_select_model=test_plan_select_model)

Restore multiple test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_plan_select_model import TestPlanSelectModel
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
    api_instance = testit_api_client.ProjectTestPlansApi(api_client)
    project_id = 'project_id_example' # str | Unique or global ID of the project
    test_plan_select_model = testit_api_client.TestPlanSelectModel() # TestPlanSelectModel |  (optional)

    try:
        # Restore multiple test plans
        api_response = api_instance.api_v2_projects_project_id_test_plans_restore_bulk_post(project_id, test_plan_select_model=test_plan_select_model)
        print("The response of ProjectTestPlansApi->api_v2_projects_project_id_test_plans_restore_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_restore_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global ID of the project | 
 **test_plan_select_model** | [**TestPlanSelectModel**](TestPlanSelectModel.md)|  | [optional] 

### Return type

**List[str]**

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
**403** | Read permission for the archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_test_plans_search_post**
> List[TestPlanWithAnalyticModel] api_v2_projects_project_id_test_plans_search_post(project_id, must_update_cache=must_update_cache, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, project_test_plans_filter_model=project_test_plans_filter_model)

Get Project TestPlans with analytics

 Use case   User sets project internal or global identifier    User sets request body    User runs method execution   System returns project testplans with analytics

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.project_test_plans_filter_model import ProjectTestPlansFilterModel
from testit_api_client.models.test_plan_with_analytic_model import TestPlanWithAnalyticModel
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
    api_instance = testit_api_client.ProjectTestPlansApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier
    must_update_cache = False # bool |  (optional) (default to False)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    project_test_plans_filter_model = testit_api_client.ProjectTestPlansFilterModel() # ProjectTestPlansFilterModel |  (optional)

    try:
        # Get Project TestPlans with analytics
        api_response = api_instance.api_v2_projects_project_id_test_plans_search_post(project_id, must_update_cache=must_update_cache, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, project_test_plans_filter_model=project_test_plans_filter_model)
        print("The response of ProjectTestPlansApi->api_v2_projects_project_id_test_plans_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTestPlansApi->api_v2_projects_project_id_test_plans_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **must_update_cache** | **bool**|  | [optional] [default to False]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **project_test_plans_filter_model** | [**ProjectTestPlansFilterModel**](ProjectTestPlansFilterModel.md)|  | [optional] 

### Return type

[**List[TestPlanWithAnalyticModel]**](TestPlanWithAnalyticModel.md)

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

