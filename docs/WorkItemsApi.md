# testit_api_client.WorkItemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_work_items_id_attachments_post**](WorkItemsApi.md#api_v2_work_items_id_attachments_post) | **POST** /api/v2/workItems/{id}/attachments | Upload and link attachment to WorkItem
[**api_v2_work_items_id_check_list_transform_to_test_case_post**](WorkItemsApi.md#api_v2_work_items_id_check_list_transform_to_test_case_post) | **POST** /api/v2/workItems/{id}/checkList/transformTo/testCase | Transform CheckList to TestCase
[**api_v2_work_items_id_history_get**](WorkItemsApi.md#api_v2_work_items_id_history_get) | **GET** /api/v2/workItems/{id}/history | Get change history of WorkItem
[**api_v2_work_items_id_like_delete**](WorkItemsApi.md#api_v2_work_items_id_like_delete) | **DELETE** /api/v2/workItems/{id}/like | Delete like from WorkItem
[**api_v2_work_items_id_like_post**](WorkItemsApi.md#api_v2_work_items_id_like_post) | **POST** /api/v2/workItems/{id}/like | Set like to WorkItem
[**api_v2_work_items_id_likes_count_get**](WorkItemsApi.md#api_v2_work_items_id_likes_count_get) | **GET** /api/v2/workItems/{id}/likes/count | Get likes count of WorkItem
[**api_v2_work_items_id_likes_get**](WorkItemsApi.md#api_v2_work_items_id_likes_get) | **GET** /api/v2/workItems/{id}/likes | Get likes of WorkItem
[**api_v2_work_items_id_test_results_history_get**](WorkItemsApi.md#api_v2_work_items_id_test_results_history_get) | **GET** /api/v2/workItems/{id}/testResults/history | Get test results history of WorkItem
[**api_v2_work_items_id_version_version_id_actual_post**](WorkItemsApi.md#api_v2_work_items_id_version_version_id_actual_post) | **POST** /api/v2/workItems/{id}/version/{versionId}/actual | Set WorkItem as actual
[**api_v2_work_items_move_post**](WorkItemsApi.md#api_v2_work_items_move_post) | **POST** /api/v2/workItems/move | Move WorkItem to another section
[**api_v2_work_items_search_post**](WorkItemsApi.md#api_v2_work_items_search_post) | **POST** /api/v2/workItems/search | Search for work items
[**api_v2_work_items_shared_step_id_references_sections_post**](WorkItemsApi.md#api_v2_work_items_shared_step_id_references_sections_post) | **POST** /api/v2/workItems/{sharedStepId}/references/sections | Get SharedStep references in sections
[**api_v2_work_items_shared_step_id_references_work_items_post**](WorkItemsApi.md#api_v2_work_items_shared_step_id_references_work_items_post) | **POST** /api/v2/workItems/{sharedStepId}/references/workItems | Get SharedStep references in work items
[**api_v2_work_items_shared_steps_shared_step_id_references_get**](WorkItemsApi.md#api_v2_work_items_shared_steps_shared_step_id_references_get) | **GET** /api/v2/workItems/sharedSteps/{sharedStepId}/references | Get SharedStep references
[**create_work_item**](WorkItemsApi.md#create_work_item) | **POST** /api/v2/workItems | Create Test Case, Checklist or Shared Step
[**delete_all_work_items_from_auto_test**](WorkItemsApi.md#delete_all_work_items_from_auto_test) | **DELETE** /api/v2/workItems/{id}/autoTests | Delete all links AutoTests from WorkItem by Id or GlobalId
[**delete_work_item**](WorkItemsApi.md#delete_work_item) | **DELETE** /api/v2/workItems/{id} | Delete Test Case, Checklist or Shared Step by Id or GlobalId
[**get_auto_tests_for_work_item**](WorkItemsApi.md#get_auto_tests_for_work_item) | **GET** /api/v2/workItems/{id}/autoTests | Get all AutoTests linked to WorkItem by Id or GlobalId
[**get_iterations**](WorkItemsApi.md#get_iterations) | **GET** /api/v2/workItems/{id}/iterations | Get iterations by work item Id or GlobalId
[**get_work_item_by_id**](WorkItemsApi.md#get_work_item_by_id) | **GET** /api/v2/workItems/{id} | Get Test Case, Checklist or Shared Step by Id or GlobalId
[**get_work_item_chronology**](WorkItemsApi.md#get_work_item_chronology) | **GET** /api/v2/workItems/{id}/chronology | Get WorkItem chronology by Id or GlobalId
[**get_work_item_versions**](WorkItemsApi.md#get_work_item_versions) | **GET** /api/v2/workItems/{id}/versions | Get WorkItem versions
[**purge_work_item**](WorkItemsApi.md#purge_work_item) | **POST** /api/v2/workItems/{id}/purge | Permanently delete test case, checklist or shared steps from archive
[**restore_work_item**](WorkItemsApi.md#restore_work_item) | **POST** /api/v2/workItems/{id}/restore | Restore test case, checklist or shared steps from archive
[**update_work_item**](WorkItemsApi.md#update_work_item) | **PUT** /api/v2/workItems | Update Test Case, Checklist or Shared Step


# **api_v2_work_items_id_attachments_post**
> api_v2_work_items_id_attachments_post(id, file=file)

Upload and link attachment to WorkItem

 Use case   User sets workItemId   User attaches a file   System creates attachment and links it to the work item   System returns attachment identifier

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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Work item internal identifier (guid format)
    file = None # bytearray | Select file (optional)

    try:
        # Upload and link attachment to WorkItem
        api_instance.api_v2_work_items_id_attachments_post(id, file=file)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_attachments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Work item internal identifier (guid format) | 
 **file** | **bytearray**| Select file | [optional] 

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
**413** | Multipart body length limit exceeded (default constraint is one gigabyte) |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** |  |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_check_list_transform_to_test_case_post**
> WorkItemModel api_v2_work_items_id_check_list_transform_to_test_case_post(id)

Transform CheckList to TestCase

 Use case   User sets checklist identifier   User runs method execution   System transform CheckList to TestCase

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_model import WorkItemModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Transform CheckList to TestCase
        api_response = api_instance.api_v2_work_items_id_check_list_transform_to_test_case_post(id)
        print("The response of WorkItemsApi->api_v2_work_items_id_check_list_transform_to_test_case_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_check_list_transform_to_test_case_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**WorkItemModel**](WorkItemModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library required |  -  |
**404** | Can&#39;t find CheckList with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_history_get**
> List[WorkItemChangeModel] api_v2_work_items_id_history_get(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get change history of WorkItem

 Use case   User sets work item identifier   User runs method execution   System return change history of WorkItem

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_change_model import WorkItemChangeModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | 
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get change history of WorkItem
        api_response = api_instance.api_v2_work_items_id_history_get(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of WorkItemsApi->api_v2_work_items_id_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 

### Return type

[**List[WorkItemChangeModel]**](WorkItemChangeModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | Can&#39;t find WorkItem with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_like_delete**
> api_v2_work_items_id_like_delete(id)

Delete like from WorkItem

 Use case   User sets WorkItem identifier   User runs method execution   System delete like from WorkItem

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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete like from WorkItem
        api_instance.api_v2_work_items_id_like_delete(id)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_like_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **api_v2_work_items_id_like_post**
> api_v2_work_items_id_like_post(id)

Set like to WorkItem

 Use case   User sets WorkItem identifier   User runs method execution   System set like to WorkItem

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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Set like to WorkItem
        api_instance.api_v2_work_items_id_like_post(id)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_like_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_likes_count_get**
> int api_v2_work_items_id_likes_count_get(id)

Get likes count of WorkItem

 Use case   User sets WorkItem identifier   User runs method execution   System return likes count of WorkItem

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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get likes count of WorkItem
        api_response = api_instance.api_v2_work_items_id_likes_count_get(id)
        print("The response of WorkItemsApi->api_v2_work_items_id_likes_count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_likes_count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**int**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_likes_get**
> List[WorkItemLikeModel] api_v2_work_items_id_likes_get(id)

Get likes of WorkItem

 Use case   User sets WorkItem identifier   User runs method execution   System return likes of WorkItem

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_like_model import WorkItemLikeModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get likes of WorkItem
        api_response = api_instance.api_v2_work_items_id_likes_get(id)
        print("The response of WorkItemsApi->api_v2_work_items_id_likes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_likes_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[WorkItemLikeModel]**](WorkItemLikeModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_test_results_history_get**
> List[TestResultHistoryResponse] api_v2_work_items_id_test_results_history_get(id, var_from=var_from, to=to, configuration_ids=configuration_ids, test_plan_ids=test_plan_ids, user_ids=user_ids, outcomes=outcomes, is_automated=is_automated, automated=automated, test_run_ids=test_run_ids, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get test results history of WorkItem

 Use case   User sets WorkItem identifier   User runs method execution   System return test results history of WorkItem

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_result_history_response import TestResultHistoryResponse
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | 
    var_from = '2013-10-20T19:20:30+01:00' # datetime | Take results from this date (optional)
    to = '2013-10-20T19:20:30+01:00' # datetime | Take results until this date (optional)
    configuration_ids = ['configuration_ids_example'] # List[str] | Identifiers of test result configurations (optional)
    test_plan_ids = ['test_plan_ids_example'] # List[str] | Identifiers of test plans which contain test results (optional)
    user_ids = ['user_ids_example'] # List[str] | Identifiers of users who set test results (optional)
    outcomes = ['outcomes_example'] # List[str] | List of outcomes of test results (optional)
    is_automated = True # bool | OBSOLETE: Use `Automated` instead (optional)
    automated = True # bool | If result must consist of only manual/automated test results (optional)
    test_run_ids = ['test_run_ids_example'] # List[str] | Identifiers of test runs which contain test results (optional)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get test results history of WorkItem
        api_response = api_instance.api_v2_work_items_id_test_results_history_get(id, var_from=var_from, to=to, configuration_ids=configuration_ids, test_plan_ids=test_plan_ids, user_ids=user_ids, outcomes=outcomes, is_automated=is_automated, automated=automated, test_run_ids=test_run_ids, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of WorkItemsApi->api_v2_work_items_id_test_results_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_test_results_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **var_from** | **datetime**| Take results from this date | [optional] 
 **to** | **datetime**| Take results until this date | [optional] 
 **configuration_ids** | [**List[str]**](str.md)| Identifiers of test result configurations | [optional] 
 **test_plan_ids** | [**List[str]**](str.md)| Identifiers of test plans which contain test results | [optional] 
 **user_ids** | [**List[str]**](str.md)| Identifiers of users who set test results | [optional] 
 **outcomes** | [**List[str]**](str.md)| List of outcomes of test results | [optional] 
 **is_automated** | **bool**| OBSOLETE: Use &#x60;Automated&#x60; instead | [optional] 
 **automated** | **bool**| If result must consist of only manual/automated test results | [optional] 
 **test_run_ids** | [**List[str]**](str.md)| Identifiers of test runs which contain test results | [optional] 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 

### Return type

[**List[TestResultHistoryResponse]**](TestResultHistoryResponse.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_version_version_id_actual_post**
> WorkItemModel api_v2_work_items_id_version_version_id_actual_post(id, version_id)

Set WorkItem as actual

 Use case   User sets work item identifier   User runs method execution   System set WorkItem as actual

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_model import WorkItemModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | 
    version_id = 'version_id_example' # str | 

    try:
        # Set WorkItem as actual
        api_response = api_instance.api_v2_work_items_id_version_version_id_actual_post(id, version_id)
        print("The response of WorkItemsApi->api_v2_work_items_id_version_version_id_actual_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_version_version_id_actual_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **version_id** | **str**|  | 

### Return type

[**WorkItemModel**](WorkItemModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library required |  -  |
**404** | Can&#39;t find WorkItem with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_move_post**
> WorkItemShortModel api_v2_work_items_move_post(work_item_move_post_model=work_item_move_post_model)

Move WorkItem to another section

 Use case   User sets WorkItem identifier   User runs method execution   System move WorkItem to another section

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_move_post_model import WorkItemMovePostModel
from testit_api_client.models.work_item_short_model import WorkItemShortModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    work_item_move_post_model = testit_api_client.WorkItemMovePostModel() # WorkItemMovePostModel |  (optional)

    try:
        # Move WorkItem to another section
        api_response = api_instance.api_v2_work_items_move_post(work_item_move_post_model=work_item_move_post_model)
        print("The response of WorkItemsApi->api_v2_work_items_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_move_post_model** | [**WorkItemMovePostModel**](WorkItemMovePostModel.md)|  | [optional] 

### Return type

[**WorkItemShortModel**](WorkItemShortModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_search_post**
> List[WorkItemShortModel] api_v2_work_items_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_select_model=work_item_select_model)

Search for work items

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_select_model import WorkItemSelectModel
from testit_api_client.models.work_item_short_model import WorkItemShortModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    work_item_select_model = testit_api_client.WorkItemSelectModel() # WorkItemSelectModel |  (optional)

    try:
        # Search for work items
        api_response = api_instance.api_v2_work_items_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_select_model=work_item_select_model)
        print("The response of WorkItemsApi->api_v2_work_items_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **work_item_select_model** | [**WorkItemSelectModel**](WorkItemSelectModel.md)|  | [optional] 

### Return type

[**List[WorkItemShortModel]**](WorkItemShortModel.md)

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
**403** | Test library read permission for all requested projects is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_shared_step_id_references_sections_post**
> List[SharedStepReferenceSectionModel] api_v2_work_items_shared_step_id_references_sections_post(shared_step_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, shared_step_reference_sections_query_filter_model=shared_step_reference_sections_query_filter_model)

Get SharedStep references in sections

 Use case   User sets SharedStep identifier   User runs method execution   System return SharedStep references

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.shared_step_reference_section_model import SharedStepReferenceSectionModel
from testit_api_client.models.shared_step_reference_sections_query_filter_model import SharedStepReferenceSectionsQueryFilterModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    shared_step_id = 'shared_step_id_example' # str | 
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    shared_step_reference_sections_query_filter_model = testit_api_client.SharedStepReferenceSectionsQueryFilterModel() # SharedStepReferenceSectionsQueryFilterModel |  (optional)

    try:
        # Get SharedStep references in sections
        api_response = api_instance.api_v2_work_items_shared_step_id_references_sections_post(shared_step_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, shared_step_reference_sections_query_filter_model=shared_step_reference_sections_query_filter_model)
        print("The response of WorkItemsApi->api_v2_work_items_shared_step_id_references_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_shared_step_id_references_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_step_id** | **str**|  | 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **shared_step_reference_sections_query_filter_model** | [**SharedStepReferenceSectionsQueryFilterModel**](SharedStepReferenceSectionsQueryFilterModel.md)|  | [optional] 

### Return type

[**List[SharedStepReferenceSectionModel]**](SharedStepReferenceSectionModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Can&#39;t find SharedStep with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_shared_step_id_references_work_items_post**
> List[SharedStepReferenceModel] api_v2_work_items_shared_step_id_references_work_items_post(shared_step_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, shared_step_references_query_filter_model=shared_step_references_query_filter_model)

Get SharedStep references in work items

 Use case   User sets SharedStep identifier   User runs method execution   System return SharedStep references

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.shared_step_reference_model import SharedStepReferenceModel
from testit_api_client.models.shared_step_references_query_filter_model import SharedStepReferencesQueryFilterModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    shared_step_id = 'shared_step_id_example' # str | 
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    shared_step_references_query_filter_model = testit_api_client.SharedStepReferencesQueryFilterModel() # SharedStepReferencesQueryFilterModel |  (optional)

    try:
        # Get SharedStep references in work items
        api_response = api_instance.api_v2_work_items_shared_step_id_references_work_items_post(shared_step_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, shared_step_references_query_filter_model=shared_step_references_query_filter_model)
        print("The response of WorkItemsApi->api_v2_work_items_shared_step_id_references_work_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_shared_step_id_references_work_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_step_id** | **str**|  | 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **shared_step_references_query_filter_model** | [**SharedStepReferencesQueryFilterModel**](SharedStepReferencesQueryFilterModel.md)|  | [optional] 

### Return type

[**List[SharedStepReferenceModel]**](SharedStepReferenceModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Can&#39;t find SharedStep with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_shared_steps_shared_step_id_references_get**
> List[SharedStepReferenceModel] api_v2_work_items_shared_steps_shared_step_id_references_get(shared_step_id)

Get SharedStep references

 Use case   User sets SharedStep identifier   User runs method execution   System return SharedStep references

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.shared_step_reference_model import SharedStepReferenceModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    shared_step_id = 'shared_step_id_example' # str | 

    try:
        # Get SharedStep references
        api_response = api_instance.api_v2_work_items_shared_steps_shared_step_id_references_get(shared_step_id)
        print("The response of WorkItemsApi->api_v2_work_items_shared_steps_shared_step_id_references_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_shared_steps_shared_step_id_references_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_step_id** | **str**|  | 

### Return type

[**List[SharedStepReferenceModel]**](SharedStepReferenceModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Can&#39;t find SharedStep with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_work_item**
> WorkItemModel create_work_item(work_item_post_model=work_item_post_model)

Create Test Case, Checklist or Shared Step

 Use case   User sets work item properties (listed in request parameters)   User runs method execution   System creates work item by identifier   System returns work item model (listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_model import WorkItemModel
from testit_api_client.models.work_item_post_model import WorkItemPostModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    work_item_post_model = testit_api_client.WorkItemPostModel() # WorkItemPostModel |  (optional)

    try:
        # Create Test Case, Checklist or Shared Step
        api_response = api_instance.create_work_item(work_item_post_model=work_item_post_model)
        print("The response of WorkItemsApi->create_work_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->create_work_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_post_model** | [**WorkItemPostModel**](WorkItemPostModel.md)|  | [optional] 

### Return type

[**WorkItemModel**](WorkItemModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** |  Field is required   Priority is not a valid   Tags must be set   Duration should be a positive number   Should be empty for CheckList   Attribute value must be a valid guid for user scheme   There is no option in ProjectAttributesScheme with such Id   Attribute value must be a valid guid for options scheme |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library required |  -  |
**404** |  Can&#39;t find section   Can&#39;t find project   Can&#39;t find attachmentIds   Project not found   Can&#39;t attributesScheme   Can&#39;t attribute   AutoTestIds not exist in project |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_work_items_from_auto_test**
> delete_all_work_items_from_auto_test(id)

Delete all links AutoTests from WorkItem by Id or GlobalId

 Use case   User sets work item identifier   User runs method execution   System search work item by identifier   System search and delete all autotests, related to found work item   System returns no content response

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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | WorkItem internal (guid format) or  global(integer format) identifier\"

    try:
        # Delete all links AutoTests from WorkItem by Id or GlobalId
        api_instance.delete_all_work_items_from_auto_test(id)
    except Exception as e:
        print("Exception when calling WorkItemsApi->delete_all_work_items_from_auto_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WorkItem internal (guid format) or  global(integer format) identifier\&quot; | 

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
**403** | Update permission for test library required |  -  |
**404** | Can&#39;t find a WorkItem with workItemId |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_item**
> delete_work_item(id)

Delete Test Case, Checklist or Shared Step by Id or GlobalId

 Use case   User sets work item identifier   User runs method execution   System deletes work item   System returns no content response

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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | WorkItem internal (guid format) or  global(integer format) identifier\"

    try:
        # Delete Test Case, Checklist or Shared Step by Id or GlobalId
        api_instance.delete_work_item(id)
    except Exception as e:
        print("Exception when calling WorkItemsApi->delete_work_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WorkItem internal (guid format) or  global(integer format) identifier\&quot; | 

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
**403** | Delete permission for test library required |  -  |
**404** | Can&#39;t find a WorkItem with id |  -  |
**409** | Conflict |  -  |
**422** | Could not delete Shared Step that has references |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_tests_for_work_item**
> List[AutoTestModel] get_auto_tests_for_work_item(id)

Get all AutoTests linked to WorkItem by Id or GlobalId

 Use case   User sets work item identifier   User runs method execution   System search work item by identifier   System search all autotests, related to found work item   System returns list of found autotests

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_model import AutoTestModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | WorkItem internal (guid format) or  global(integer format) identifier\"

    try:
        # Get all AutoTests linked to WorkItem by Id or GlobalId
        api_response = api_instance.get_auto_tests_for_work_item(id)
        print("The response of WorkItemsApi->get_auto_tests_for_work_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->get_auto_tests_for_work_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WorkItem internal (guid format) or  global(integer format) identifier\&quot; | 

### Return type

[**List[AutoTestModel]**](AutoTestModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | Can&#39;t find WorkItem with workItemId |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_iterations**
> List[IterationModel] get_iterations(id, version_id=version_id, version_number=version_number)

Get iterations by work item Id or GlobalId

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.iteration_model import IterationModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | WorkItem internal (guid format) or  global(integer format) identifier\"
    version_id = '00000000-0000-0000-0000-000000000000' # str | WorkItem version (guid format) identifier (optional)
    version_number = 0 # int | WorkItem version number (0 is the last version)\" (optional)

    try:
        # Get iterations by work item Id or GlobalId
        api_response = api_instance.get_iterations(id, version_id=version_id, version_number=version_number)
        print("The response of WorkItemsApi->get_iterations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->get_iterations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WorkItem internal (guid format) or  global(integer format) identifier\&quot; | 
 **version_id** | **str**| WorkItem version (guid format) identifier | [optional] 
 **version_number** | **int**| WorkItem version number (0 is the last version)\&quot; | [optional] 

### Return type

[**List[IterationModel]**](IterationModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | Can&#39;t find workItem with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_item_by_id**
> WorkItemModel get_work_item_by_id(id, version_id=version_id, version_number=version_number)

Get Test Case, Checklist or Shared Step by Id or GlobalId

 Use case   User sets work item identifier   [Optional] User sets work item version identifier   [Optional] User sets work item version number   User runs method execution   System search work item by identifier   [Optional] if User sets work item version identifier, system search work item version by identifier.   [Optional] if user sets work item version number, system search work item version by number   Otherwise, system search last work item version   System returns work item 

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_model import WorkItemModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | WorkItem internal (guid format) or  global(integer format) identifier\"
    version_id = '00000000-0000-0000-0000-000000000000' # str | WorkItem version (guid format) identifier\" (optional)
    version_number = 0 # int | WorkItem version number (0 is the last version)\" (optional)

    try:
        # Get Test Case, Checklist or Shared Step by Id or GlobalId
        api_response = api_instance.get_work_item_by_id(id, version_id=version_id, version_number=version_number)
        print("The response of WorkItemsApi->get_work_item_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->get_work_item_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WorkItem internal (guid format) or  global(integer format) identifier\&quot; | 
 **version_id** | **str**| WorkItem version (guid format) identifier\&quot; | [optional] 
 **version_number** | **int**| WorkItem version number (0 is the last version)\&quot; | [optional] 

### Return type

[**WorkItemModel**](WorkItemModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | Can&#39;t find workItem with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_item_chronology**
> List[TestResultChronologyModel] get_work_item_chronology(id)

Get WorkItem chronology by Id or GlobalId

 Use case   User sets work item identifier   User runs method execution   System search work item by identifier   System search test results of all autotests, related to found work item   System sort results by CompletedOn ascending, then by CreatedDate ascending   System returns sorted collection of test results

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_result_chronology_model import TestResultChronologyModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get WorkItem chronology by Id or GlobalId
        api_response = api_instance.get_work_item_chronology(id)
        print("The response of WorkItemsApi->get_work_item_chronology:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->get_work_item_chronology: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**List[TestResultChronologyModel]**](TestResultChronologyModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Not valid workItemId |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | Can&#39;t find WorkItem with workItemId |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_item_versions**
> List[WorkItemVersionModel] get_work_item_versions(id, work_item_version_id=work_item_version_id, version_number=version_number)

Get WorkItem versions

 Use case   User sets work item identifier   [Optional] User sets work item version identifier   User runs method execution   System search work item by identifier                         [Optional] If User set work item version identifier, System search work item version by version identifier                      Otherwise, system search all version of work item                     System returns array of work item version models (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_version_model import WorkItemVersionModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | WorkItem internal (guid format) or  global(integer format) identifier\"
    work_item_version_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | WorkItem version (guid format)  identifier\" (optional)
    version_number = 1 # int | WorkItem version (integer format)  number\" (optional)

    try:
        # Get WorkItem versions
        api_response = api_instance.get_work_item_versions(id, work_item_version_id=work_item_version_id, version_number=version_number)
        print("The response of WorkItemsApi->get_work_item_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkItemsApi->get_work_item_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WorkItem internal (guid format) or  global(integer format) identifier\&quot; | 
 **work_item_version_id** | **str**| WorkItem version (guid format)  identifier\&quot; | [optional] 
 **version_number** | **int**| WorkItem version (integer format)  number\&quot; | [optional] 

### Return type

[**List[WorkItemVersionModel]**](WorkItemVersionModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | Can&#39;t find WorkItem with workItemId |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purge_work_item**
> purge_work_item(id)

Permanently delete test case, checklist or shared steps from archive

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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | Unique or global ID of the work item

    try:
        # Permanently delete test case, checklist or shared steps from archive
        api_instance.purge_work_item(id)
    except Exception as e:
        print("Exception when calling WorkItemsApi->purge_work_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the work item | 

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
**403** | Delete permission for the archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_work_item**
> restore_work_item(id)

Restore test case, checklist or shared steps from archive

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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    id = 'id_example' # str | Unique or global ID of the work item

    try:
        # Restore test case, checklist or shared steps from archive
        api_instance.restore_work_item(id)
    except Exception as e:
        print("Exception when calling WorkItemsApi->restore_work_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the work item | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for the archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_work_item**
> update_work_item(work_item_put_model=work_item_put_model)

Update Test Case, Checklist or Shared Step

 Use case   User sets work item properties (listed in request parameters)   User runs method execution   System updates work item by identifier   System returns updated work item model (listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_put_model import WorkItemPutModel
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
    api_instance = testit_api_client.WorkItemsApi(api_client)
    work_item_put_model = testit_api_client.WorkItemPutModel() # WorkItemPutModel |  (optional)

    try:
        # Update Test Case, Checklist or Shared Step
        api_instance.update_work_item(work_item_put_model=work_item_put_model)
    except Exception as e:
        print("Exception when calling WorkItemsApi->update_work_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_put_model** | [**WorkItemPutModel**](WorkItemPutModel.md)|  | [optional] 

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
**204** | Successful operation |  -  |
**400** |  Field is required   Priority is not a valid   duration should be a positive number   should be empty for CheckList   There is no option in ProjectAttributesScheme with such Id   Attribute value must be a valid guid for options scheme |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library required |  -  |
**404** |  WorkItem not found   Can&#39;t find section   Can&#39;t attributesScheme   Can&#39;t attribute   AutoTestIds not exist in project |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

