# testit_api_client.AutoTestsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_auto_tests_delete**](AutoTestsApi.md#api_v2_auto_tests_delete) | **DELETE** /api/v2/autoTests | Delete autotests
[**api_v2_auto_tests_flaky_bulk_post**](AutoTestsApi.md#api_v2_auto_tests_flaky_bulk_post) | **POST** /api/v2/autoTests/flaky/bulk | Set \&quot;Flaky\&quot; status for multiple autotests
[**api_v2_auto_tests_id_patch**](AutoTestsApi.md#api_v2_auto_tests_id_patch) | **PATCH** /api/v2/autoTests/{id} | Patch auto test
[**api_v2_auto_tests_id_test_results_search_post**](AutoTestsApi.md#api_v2_auto_tests_id_test_results_search_post) | **POST** /api/v2/autoTests/{id}/testResults/search | Get test results history for autotest
[**api_v2_auto_tests_id_work_items_changed_id_get**](AutoTestsApi.md#api_v2_auto_tests_id_work_items_changed_id_get) | **GET** /api/v2/autoTests/{id}/workItems/changed/id | Get identifiers of changed linked work items
[**api_v2_auto_tests_id_work_items_changed_work_item_id_approve_post**](AutoTestsApi.md#api_v2_auto_tests_id_work_items_changed_work_item_id_approve_post) | **POST** /api/v2/autoTests/{id}/workItems/changed/{workItemId}/approve | Approve changes to work items linked to autotest
[**api_v2_auto_tests_search_post**](AutoTestsApi.md#api_v2_auto_tests_search_post) | **POST** /api/v2/autoTests/search | Search for autotests
[**create_auto_test**](AutoTestsApi.md#create_auto_test) | **POST** /api/v2/autoTests | Create autotest
[**create_multiple**](AutoTestsApi.md#create_multiple) | **POST** /api/v2/autoTests/bulk | Create multiple autotests
[**delete_auto_test**](AutoTestsApi.md#delete_auto_test) | **DELETE** /api/v2/autoTests/{id} | Delete autotest
[**delete_auto_test_link_from_work_item**](AutoTestsApi.md#delete_auto_test_link_from_work_item) | **DELETE** /api/v2/autoTests/{id}/workItems | Unlink autotest from work item
[**get_all_auto_tests**](AutoTestsApi.md#get_all_auto_tests) | **GET** /api/v2/autoTests | 
[**get_auto_test_average_duration**](AutoTestsApi.md#get_auto_test_average_duration) | **GET** /api/v2/autoTests/{id}/averageDuration | Get average autotest duration
[**get_auto_test_by_id**](AutoTestsApi.md#get_auto_test_by_id) | **GET** /api/v2/autoTests/{id} | Get autotest by internal or global ID
[**get_auto_test_chronology**](AutoTestsApi.md#get_auto_test_chronology) | **GET** /api/v2/autoTests/{id}/chronology | Get autotest chronology
[**get_test_runs**](AutoTestsApi.md#get_test_runs) | **GET** /api/v2/autoTests/{id}/testRuns | Get completed tests runs for autotests
[**get_work_items_linked_to_auto_test**](AutoTestsApi.md#get_work_items_linked_to_auto_test) | **GET** /api/v2/autoTests/{id}/workItems | Get work items linked to autotest
[**link_auto_test_to_work_item**](AutoTestsApi.md#link_auto_test_to_work_item) | **POST** /api/v2/autoTests/{id}/workItems | Link autotest with work items
[**update_auto_test**](AutoTestsApi.md#update_auto_test) | **PUT** /api/v2/autoTests | Update autotest
[**update_multiple**](AutoTestsApi.md#update_multiple) | **PUT** /api/v2/autoTests/bulk | Update multiple autotests


# **api_v2_auto_tests_delete**
> AutoTestBulkDeleteApiResult api_v2_auto_tests_delete(auto_test_bulk_delete_api_model=auto_test_bulk_delete_api_model)

Delete autotests

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_bulk_delete_api_model import AutoTestBulkDeleteApiModel
from testit_api_client.models.auto_test_bulk_delete_api_result import AutoTestBulkDeleteApiResult
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    auto_test_bulk_delete_api_model = testit_api_client.AutoTestBulkDeleteApiModel() # AutoTestBulkDeleteApiModel |  (optional)

    try:
        # Delete autotests
        api_response = api_instance.api_v2_auto_tests_delete(auto_test_bulk_delete_api_model=auto_test_bulk_delete_api_model)
        print("The response of AutoTestsApi->api_v2_auto_tests_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->api_v2_auto_tests_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_test_bulk_delete_api_model** | [**AutoTestBulkDeleteApiModel**](AutoTestBulkDeleteApiModel.md)|  | [optional] 

### Return type

[**AutoTestBulkDeleteApiResult**](AutoTestBulkDeleteApiResult.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_auto_tests_flaky_bulk_post**
> api_v2_auto_tests_flaky_bulk_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, auto_test_flaky_bulk_api_model=auto_test_flaky_bulk_api_model)

Set \"Flaky\" status for multiple autotests

User permissions for project:  - Read only  - Execute  - Write  - Full control

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_flaky_bulk_api_model import AutoTestFlakyBulkApiModel
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    auto_test_flaky_bulk_api_model = testit_api_client.AutoTestFlakyBulkApiModel() # AutoTestFlakyBulkApiModel |  (optional)

    try:
        # Set \"Flaky\" status for multiple autotests
        api_instance.api_v2_auto_tests_flaky_bulk_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, auto_test_flaky_bulk_api_model=auto_test_flaky_bulk_api_model)
    except Exception as e:
        print("Exception when calling AutoTestsApi->api_v2_auto_tests_flaky_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **auto_test_flaky_bulk_api_model** | [**AutoTestFlakyBulkApiModel**](AutoTestFlakyBulkApiModel.md)|  | [optional] 

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
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Invalid user permissions |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Autotests with provided identifiers do not belong to the same project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_auto_tests_id_patch**
> api_v2_auto_tests_id_patch(id, operation=operation)

Patch auto test

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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | Global Id of auto test
    operation = [testit_api_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch auto test
        api_instance.api_v2_auto_tests_id_patch(id, operation=operation)
    except Exception as e:
        print("Exception when calling AutoTestsApi->api_v2_auto_tests_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Global Id of auto test | 
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
**403** | Update permission for auto tests is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_auto_tests_id_test_results_search_post**
> List[AutoTestResultHistoryApiResult] api_v2_auto_tests_id_test_results_search_post(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, auto_test_result_history_select_api_model=auto_test_result_history_select_api_model)

Get test results history for autotest

 Use case   User sets autotest internal (guid format) or global (integer format) identifier   User sets getTestResultHistoryReportQuery (listed in the example)   User runs method execution   System search for test results using filters set by user in getTestResultHistoryReportQuery and id   System returns the enumeration of test results

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_result_history_api_result import AutoTestResultHistoryApiResult
from testit_api_client.models.auto_test_result_history_select_api_model import AutoTestResultHistorySelectApiModel
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | Autotest identifier
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    auto_test_result_history_select_api_model = testit_api_client.AutoTestResultHistorySelectApiModel() # AutoTestResultHistorySelectApiModel |  (optional)

    try:
        # Get test results history for autotest
        api_response = api_instance.api_v2_auto_tests_id_test_results_search_post(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, auto_test_result_history_select_api_model=auto_test_result_history_select_api_model)
        print("The response of AutoTestsApi->api_v2_auto_tests_id_test_results_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->api_v2_auto_tests_id_test_results_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Autotest identifier | 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **auto_test_result_history_select_api_model** | [**AutoTestResultHistorySelectApiModel**](AutoTestResultHistorySelectApiModel.md)|  | [optional] 

### Return type

[**List[AutoTestResultHistoryApiResult]**](AutoTestResultHistoryApiResult.md)

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
**403** | Read permission for autotests required |  -  |
**404** | Autotest with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_auto_tests_id_work_items_changed_id_get**
> List[str] api_v2_auto_tests_id_work_items_changed_id_get(id)

Get identifiers of changed linked work items

User permissions for project:  - Read only  - Execute  - Write  - Full control

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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get identifiers of changed linked work items
        api_response = api_instance.api_v2_auto_tests_id_work_items_changed_id_get(id)
        print("The response of AutoTestsApi->api_v2_auto_tests_id_work_items_changed_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->api_v2_auto_tests_id_work_items_changed_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**List[str]**

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
**403** | Invalid user permissions |  -  |
**404** | Autotest with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_auto_tests_id_work_items_changed_work_item_id_approve_post**
> api_v2_auto_tests_id_work_items_changed_work_item_id_approve_post(id, work_item_id)

Approve changes to work items linked to autotest

User permissions for project:  - Read only  - Execute  - Write  - Full control

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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | 
    work_item_id = 'work_item_id_example' # str | 

    try:
        # Approve changes to work items linked to autotest
        api_instance.api_v2_auto_tests_id_work_items_changed_work_item_id_approve_post(id, work_item_id)
    except Exception as e:
        print("Exception when calling AutoTestsApi->api_v2_auto_tests_id_work_items_changed_work_item_id_approve_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **work_item_id** | **str**|  | 

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
**403** | Invalid user permissions |  -  |
**404** | Autotest with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_auto_tests_search_post**
> List[AutoTestApiResult] api_v2_auto_tests_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, auto_test_search_api_model=auto_test_search_api_model)

Search for autotests

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_api_result import AutoTestApiResult
from testit_api_client.models.auto_test_search_api_model import AutoTestSearchApiModel
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    auto_test_search_api_model = testit_api_client.AutoTestSearchApiModel() # AutoTestSearchApiModel |  (optional)

    try:
        # Search for autotests
        api_response = api_instance.api_v2_auto_tests_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, auto_test_search_api_model=auto_test_search_api_model)
        print("The response of AutoTestsApi->api_v2_auto_tests_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->api_v2_auto_tests_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **auto_test_search_api_model** | [**AutoTestSearchApiModel**](AutoTestSearchApiModel.md)|  | [optional] 

### Return type

[**List[AutoTestApiResult]**](AutoTestApiResult.md)

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
**403** | Read permission for autotests library is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auto_test**
> AutoTestModel create_auto_test(auto_test_post_model=auto_test_post_model)

Create autotest

 This method creates a new autotest.   To add an autotest to the test plan, link it to a work item using the `POST /api/v2/autoTests/{autoTestId}/workItems` method.   Use the `POST /api/v2/testRuns/byAutoTests` method to run autotest outside the test plan.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_model import AutoTestModel
from testit_api_client.models.auto_test_post_model import AutoTestPostModel
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    auto_test_post_model = testit_api_client.AutoTestPostModel() # AutoTestPostModel |  (optional)

    try:
        # Create autotest
        api_response = api_instance.create_auto_test(auto_test_post_model=auto_test_post_model)
        print("The response of AutoTestsApi->create_auto_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->create_auto_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_test_post_model** | [**AutoTestPostModel**](AutoTestPostModel.md)|  | [optional] 

### Return type

[**AutoTestModel**](AutoTestModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  - Name cannot be empty or contain only white space characters   - External ID cannot be empty or contain only white space characters   - Namespace cannot be empty or contain only white space characters   - Classname cannot be empty or contain only white space characters   - Steps cannot be &#x60;null&#x60;   - Steps nesting level is more than 15   - Invalid URI |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for autotests is required |  -  |
**404** | Project with provided ID cannot be found |  -  |
**409** | Autotest with the same external ID already exists is the project |  -  |
**422** |  - Labels have duplicates   - Labels begin with &#x60;::&#x60;   - Labels with the same base have different values |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple**
> List[AutoTestModel] create_multiple(auto_test_post_model=auto_test_post_model)

Create multiple autotests

 Use case   User sets autotest parameters (listed in the example) and runs method execution   System creates autotest   [Optional] If steps enumeration is set, system creates step items and relates them to autotest   [Optional] If setup enumeration is set, system creates setup items and relates them to autotest   [Optional] If teardown enumeration is set, system creates teardown items and relates them to autotest   [Optional] If label enumeration is set, system creates labels and relates them to autotest   [Optional] If link enumeration is set, system creates links and relates them to autotest   System returns autotest model (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_model import AutoTestModel
from testit_api_client.models.auto_test_post_model import AutoTestPostModel
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    auto_test_post_model = [testit_api_client.AutoTestPostModel()] # List[AutoTestPostModel] |  (optional)

    try:
        # Create multiple autotests
        api_response = api_instance.create_multiple(auto_test_post_model=auto_test_post_model)
        print("The response of AutoTestsApi->create_multiple:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->create_multiple: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_test_post_model** | [**List[AutoTestPostModel]**](AutoTestPostModel.md)|  | [optional] 

### Return type

[**List[AutoTestModel]**](AutoTestModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  - Name cannot be empty or contain only white space characters   - External ID cannot be empty or contain only white space characters   - Namespace cannot be empty or contain only white space characters   - Classname cannot be empty or contain only white space characters   - Steps cannot be &#x60;null&#x60;   - Steps nesting level is more than 15   - Invalid URI |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for autotests is required |  -  |
**404** | Project with provided ID cannot be found |  -  |
**409** | Autotest with the same external ID already exists is the project |  -  |
**422** |  - Labels have duplicates   - Labels begin with &#x60;::&#x60;   - Labels with the same base have different values |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_test**
> delete_auto_test(id)

Delete autotest

 Use case   User sets autotest internal (guid format) or global (integer format) identifier and runs method execution   System finds the autotest by the identifier   System deletes autotest and returns no content response

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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | Autotest internal (UUID) or global (integer) identifier

    try:
        # Delete autotest
        api_instance.delete_auto_test(id)
    except Exception as e:
        print("Exception when calling AutoTestsApi->delete_auto_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Autotest internal (UUID) or global (integer) identifier | 

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
**403** | Delete permission for autotests is required |  -  |
**404** | Autotest with provided ID cannot be found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auto_test_link_from_work_item**
> delete_auto_test_link_from_work_item(id, work_item_id=work_item_id)

Unlink autotest from work item

 Use case   User sets autotest internal (guid format) or global (integer format) identifier   [Optional] User sets workitem internal (guid format) or global (integer format) identifier   User runs method execution   System finds the autotest by the autotest identifier                 [Optional] if workitem id is set by User, System finds the workitem by the workitem identifier and unlinks it              from autotest.                 [Optional] Otherwise, if workitem id is not specified, System unlinks all workitems linked to autotest.   System returns no content response

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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | Autotest internal (UUID) or global (integer) identifier
    work_item_id = 'work_item_id_example' # str | Work item internal (UUID) or global (integer) identifier (optional)

    try:
        # Unlink autotest from work item
        api_instance.delete_auto_test_link_from_work_item(id, work_item_id=work_item_id)
    except Exception as e:
        print("Exception when calling AutoTestsApi->delete_auto_test_link_from_work_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Autotest internal (UUID) or global (integer) identifier | 
 **work_item_id** | **str**| Work item internal (UUID) or global (integer) identifier | [optional] 

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
**400** | Work item ID is invalid |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for autotests is required |  -  |
**404** |  - Autotest with provided ID cannot be found   - Work item with provided ID cannot be found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_auto_tests**
> List[AutoTestModel] get_all_auto_tests(project_id=project_id, external_id=external_id, global_id=global_id, namespace=namespace, is_namespace_null=is_namespace_null, include_empty_namespaces=include_empty_namespaces, class_name=class_name, is_classname_null=is_classname_null, include_empty_class_names=include_empty_class_names, is_deleted=is_deleted, deleted=deleted, labels=labels, stability_minimal=stability_minimal, min_stability=min_stability, stability_maximal=stability_maximal, max_stability=max_stability, is_flaky=is_flaky, flaky=flaky, include_steps=include_steps, include_labels=include_labels, external_key=external_key, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)



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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    project_id = 'project_id_example' # str | Project internal ID (optional)
    external_id = 'external_id_example' # str | Autotest external ID (optional)
    global_id = 56 # int | Autotest global ID (optional)
    namespace = 'namespace_example' # str | Namespace in which autotest is located (optional)
    is_namespace_null = True # bool | OBSOLETE: Use `includeEmptyNamespaces` instead (optional)
    include_empty_namespaces = True # bool | If result must contain autotests without namespace (optional)
    class_name = 'class_name_example' # str | Name of class in which autotest is located (optional)
    is_classname_null = True # bool | OBSOLETE: Use `includeEmptyClassNames` instead (optional)
    include_empty_class_names = True # bool | If result must contain autotests without class (optional)
    is_deleted = True # bool | OBSOLETE: Use `deleted` instead (optional)
    deleted = True # bool | Is autotest deleted (optional)
    labels = ['labels_example'] # List[str] | Include only autotests with provided labels (optional)
    stability_minimal = 56 # int | OBSOLETE: Use `minStability` instead (optional)
    min_stability = 56 # int | Minimum stability value of autotest (optional)
    stability_maximal = 56 # int | OBSOLETE: Use `maxStability` instead (optional)
    max_stability = 56 # int | Maximum stability value of autotest (optional)
    is_flaky = True # bool | OBSOLETE: Use `flaky` instead (optional)
    flaky = True # bool | Is autotest marked as \"Flaky\" (optional)
    include_steps = True # bool | If result must also include autotest steps (optional)
    include_labels = True # bool | If result must also include autotest labels (optional)
    external_key = 'external_key_example' # str | External key of autotest (optional)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        api_response = api_instance.get_all_auto_tests(project_id=project_id, external_id=external_id, global_id=global_id, namespace=namespace, is_namespace_null=is_namespace_null, include_empty_namespaces=include_empty_namespaces, class_name=class_name, is_classname_null=is_classname_null, include_empty_class_names=include_empty_class_names, is_deleted=is_deleted, deleted=deleted, labels=labels, stability_minimal=stability_minimal, min_stability=min_stability, stability_maximal=stability_maximal, max_stability=max_stability, is_flaky=is_flaky, flaky=flaky, include_steps=include_steps, include_labels=include_labels, external_key=external_key, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of AutoTestsApi->get_all_auto_tests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->get_all_auto_tests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal ID | [optional] 
 **external_id** | **str**| Autotest external ID | [optional] 
 **global_id** | **int**| Autotest global ID | [optional] 
 **namespace** | **str**| Namespace in which autotest is located | [optional] 
 **is_namespace_null** | **bool**| OBSOLETE: Use &#x60;includeEmptyNamespaces&#x60; instead | [optional] 
 **include_empty_namespaces** | **bool**| If result must contain autotests without namespace | [optional] 
 **class_name** | **str**| Name of class in which autotest is located | [optional] 
 **is_classname_null** | **bool**| OBSOLETE: Use &#x60;includeEmptyClassNames&#x60; instead | [optional] 
 **include_empty_class_names** | **bool**| If result must contain autotests without class | [optional] 
 **is_deleted** | **bool**| OBSOLETE: Use &#x60;deleted&#x60; instead | [optional] 
 **deleted** | **bool**| Is autotest deleted | [optional] 
 **labels** | [**List[str]**](str.md)| Include only autotests with provided labels | [optional] 
 **stability_minimal** | **int**| OBSOLETE: Use &#x60;minStability&#x60; instead | [optional] 
 **min_stability** | **int**| Minimum stability value of autotest | [optional] 
 **stability_maximal** | **int**| OBSOLETE: Use &#x60;maxStability&#x60; instead | [optional] 
 **max_stability** | **int**| Maximum stability value of autotest | [optional] 
 **is_flaky** | **bool**| OBSOLETE: Use &#x60;flaky&#x60; instead | [optional] 
 **flaky** | **bool**| Is autotest marked as \&quot;Flaky\&quot; | [optional] 
 **include_steps** | **bool**| If result must also include autotest steps | [optional] 
 **include_labels** | **bool**| If result must also include autotest labels | [optional] 
 **external_key** | **str**| External key of autotest | [optional] 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 

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
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_test_average_duration**
> AutoTestAverageDurationModel get_auto_test_average_duration(id)

Get average autotest duration

 Use case   User sets autotest internal (guid format) or global (integer format) identifier   User runs method execution   System calculates pass average duration and fail average duration of autotest from all related test results   System returns pass average duration and fail average duration for autotest

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_average_duration_model import AutoTestAverageDurationModel
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | Autotest internal (UUID) or global (integer) identifier

    try:
        # Get average autotest duration
        api_response = api_instance.get_auto_test_average_duration(id)
        print("The response of AutoTestsApi->get_auto_test_average_duration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->get_auto_test_average_duration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Autotest internal (UUID) or global (integer) identifier | 

### Return type

[**AutoTestAverageDurationModel**](AutoTestAverageDurationModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Autotest with provided ID was not found |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for autotests is required |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_test_by_id**
> AutoTestModel get_auto_test_by_id(id)

Get autotest by internal or global ID

 Use case   User sets autotest internal or global identifier and runs method execution   System returns autotest, which internal or global identifier equals the identifier value set in the previous action

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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | Autotest internal (UUID) or global (integer) identifier

    try:
        # Get autotest by internal or global ID
        api_response = api_instance.get_auto_test_by_id(id)
        print("The response of AutoTestsApi->get_auto_test_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->get_auto_test_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Autotest internal (UUID) or global (integer) identifier | 

### Return type

[**AutoTestModel**](AutoTestModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Autotest with provided ID cannot be found |  -  |
**400** | Autotest ID is invalid |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for autotests is required |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_test_chronology**
> List[TestResultChronologyModel] get_auto_test_chronology(id)

Get autotest chronology

 Use case   User sets autotest internal (guid format) or global (integer format) identifier   User runs method execution   System search all test results related to autotest (with default limit equal 100)   System orders the test results by CompletedOn property descending and then orders by CreatedDate property descending   System returns test result chronology for autotest

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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | Autotest internal (UUID) or global (integer) identifier

    try:
        # Get autotest chronology
        api_response = api_instance.get_auto_test_chronology(id)
        print("The response of AutoTestsApi->get_auto_test_chronology:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->get_auto_test_chronology: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Autotest internal (UUID) or global (integer) identifier | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for autotests is required |  -  |
**404** | Autotest with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_runs**
> List[TestRunByAutoTestApiResult] get_test_runs(id)

Get completed tests runs for autotests

 Use case   User sets autotest internal (guid format) or global (integer format) identifier   User runs method execution   System search for all test runs related to the autotest   System returns the enumeration of test runs

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_run_by_auto_test_api_result import TestRunByAutoTestApiResult
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | Autotest internal (UUID) or global (integer) identifier

    try:
        # Get completed tests runs for autotests
        api_response = api_instance.get_test_runs(id)
        print("The response of AutoTestsApi->get_test_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->get_test_runs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Autotest internal (UUID) or global (integer) identifier | 

### Return type

[**List[TestRunByAutoTestApiResult]**](TestRunByAutoTestApiResult.md)

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
**403** | Read permission for autotests is required |  -  |
**404** | Autotest with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_items_linked_to_auto_test**
> List[WorkItemIdentifierModel] get_work_items_linked_to_auto_test(id, is_deleted=is_deleted, is_work_item_deleted=is_work_item_deleted)

Get work items linked to autotest

               This method links an autotest to a test case or a checklist.              A manual test case with a linked automated work item is marked in the test management system as an autotest.              You can run it from graphical user interface (GUI). To do that:                               1. Open the project in GUI.               2. Go to <b>Test plans</b> section and switch to the <b>Execution</b> tab.               3. Select the autotest(s) you want to run using checkboxes.               4. In the toolbar above the test list, click <b>Run autotests</b>.              

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_identifier_model import WorkItemIdentifierModel
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | Specifies the autotest entity ID.   You can copy it from the address bar in your web browser or use autotest GUID.
    is_deleted = True # bool | Specifies that a test is deleted or still relevant. (optional)
    is_work_item_deleted = False # bool | OBSOLETE: Use `isDeleted` instead (optional) (default to False)

    try:
        # Get work items linked to autotest
        api_response = api_instance.get_work_items_linked_to_auto_test(id, is_deleted=is_deleted, is_work_item_deleted=is_work_item_deleted)
        print("The response of AutoTestsApi->get_work_items_linked_to_auto_test:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoTestsApi->get_work_items_linked_to_auto_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the autotest entity ID.   You can copy it from the address bar in your web browser or use autotest GUID. | 
 **is_deleted** | **bool**| Specifies that a test is deleted or still relevant. | [optional] 
 **is_work_item_deleted** | **bool**| OBSOLETE: Use &#x60;isDeleted&#x60; instead | [optional] [default to False]

### Return type

[**List[WorkItemIdentifierModel]**](WorkItemIdentifierModel.md)

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
**403** | Read permission for autotests is required |  -  |
**404** | Autotest with provided ID cannot be found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_auto_test_to_work_item**
> link_auto_test_to_work_item(id, work_item_id_model=work_item_id_model)

Link autotest with work items

 Use case   User sets autotest internal (guid format) or global (integer format) identifier   User sets work item internal (guid format) or global (integer format) identifier   User runs method execution   System finds the autotest by the autotest identifier   System finds the work item by the work item identifier   System relates the work item with the autotest and returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_id_model import WorkItemIdModel
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    id = 'id_example' # str | Autotest internal (UUID) or global (integer) identifier
    work_item_id_model = testit_api_client.WorkItemIdModel() # WorkItemIdModel |  (optional)

    try:
        # Link autotest with work items
        api_instance.link_auto_test_to_work_item(id, work_item_id_model=work_item_id_model)
    except Exception as e:
        print("Exception when calling AutoTestsApi->link_auto_test_to_work_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Autotest internal (UUID) or global (integer) identifier | 
 **work_item_id_model** | [**WorkItemIdModel**](WorkItemIdModel.md)|  | [optional] 

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
**400** |  - Autotest cannot be linked to shared steps   - Autotest cannot be linked to work item from other project   - Work item ID is invalid |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for autotests is required |  -  |
**404** |  - Autotest with provided ID cannot be found   - Work item with provided ID cannot be found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auto_test**
> update_auto_test(auto_test_put_model=auto_test_put_model)

Update autotest

 Use case   User sets autotest updated parameters values (listed in the example) and runs method execution   System finds the autotest by the identifier   System updates autotest parameters                  [Optional] If steps enumeration is set, system creates step items, relates them to autotest              and deletes relations with current steps( if exist)                               [Optional] If Setup enumeration is set, system creates setup items and relates them to autotest              and deletes relations with current Setup items (if exist)                               [Optional] If teardown enumeration is set, system creates teardown items and relates them to autotest              and deletes relations with current teardown items (if exist)                               [Optional] If label enumeration is set, system creates labels and relates them to autotest              and deletes relations with current Labels (if exist)                               [Optional] If link enumeration is set, system creates links and relates them to autotest              and deletes relations with current Links (if exist)                 System updates autotest and returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_put_model import AutoTestPutModel
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    auto_test_put_model = testit_api_client.AutoTestPutModel() # AutoTestPutModel |  (optional)

    try:
        # Update autotest
        api_instance.update_auto_test(auto_test_put_model=auto_test_put_model)
    except Exception as e:
        print("Exception when calling AutoTestsApi->update_auto_test: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_test_put_model** | [**AutoTestPutModel**](AutoTestPutModel.md)|  | [optional] 

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
**200** | OK |  -  |
**400** |  - Name cannot be empty or contain only white space characters   - External ID cannot be empty or contain only white space characters   - Namespace cannot be empty or contain only white space characters   - Classname cannot be empty or contain only white space characters   - Steps cannot be &#x60;null&#x60;   - Steps nesting level is more than 15   - Invalid URI |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for autotests is required |  -  |
**404** |  - Autotests with provided ID cannot be found   - Project with provided ID cannot be found   - Link with provided ID cannot be found   - Label with provided ID cannot be found |  -  |
**409** | Autotest with the same external ID already exists is the project |  -  |
**422** |  - Project ID cannot be changed   - Labels have duplicates   - Labels begin with &#x60;::&#x60;   - Labels with the same base have different values |  -  |
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_multiple**
> update_multiple(auto_test_put_model=auto_test_put_model)

Update multiple autotests

 Use case   User sets autotest updated parameters values (listed in the example) and runs method execution   System finds the autotest by the identifier   System updates autotest parameters                  [Optional] If steps enumeration is set, system creates step items, relates them to autotest              and deletes relations with current steps( if exist)                               [Optional] If Setup enumeration is set, system creates setup items and relates them to autotest              and deletes relations with current Setup items (if exist)                               [Optional] If teardown enumeration is set, system creates teardown items and relates them to autotest              and deletes relations with current teardown items (if exist)                               [Optional] If label enumeration is set, system creates labels and relates them to autotest              and deletes relations with current Labels (if exist)                               [Optional] If link enumeration is set, system creates links and relates them to autotest              and deletes relations with current Links (if exist)                 System updates autotest and returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_put_model import AutoTestPutModel
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
    api_instance = testit_api_client.AutoTestsApi(api_client)
    auto_test_put_model = [testit_api_client.AutoTestPutModel()] # List[AutoTestPutModel] |  (optional)

    try:
        # Update multiple autotests
        api_instance.update_multiple(auto_test_put_model=auto_test_put_model)
    except Exception as e:
        print("Exception when calling AutoTestsApi->update_multiple: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_test_put_model** | [**List[AutoTestPutModel]**](AutoTestPutModel.md)|  | [optional] 

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
**400** |  - Name cannot be empty or contain only white space characters   - External ID cannot be empty or contain only white space characters   - Namespace cannot be empty or contain only white space characters   - Classname cannot be empty or contain only white space characters   - Steps cannot be &#x60;null&#x60;   - Steps nesting level is more than 15   - Invalid URI |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for autotests is required |  -  |
**404** |  - Autotests with provided ID cannot be found   - Project with provided ID cannot be found   - Link with provided ID cannot be found   - Label with provided ID cannot be found |  -  |
**409** | Autotest with the same external ID already exists is the project |  -  |
**422** |  - Project ID cannot be changed   - Labels have duplicates   - Labels begin with &#x60;::&#x60;   - Labels with the same base have different values |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

