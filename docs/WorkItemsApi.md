# testit_api_client.WorkItemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
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
[**api_v2_work_items_shared_step_id_references_work_items_post**](WorkItemsApi.md#api_v2_work_items_shared_step_id_references_work_items_post) | **POST** /api/v2/workItems/{sharedStepId}/references/workItems | Get SharedStep references in workitems
[**api_v2_work_items_shared_steps_shared_step_id_references_get**](WorkItemsApi.md#api_v2_work_items_shared_steps_shared_step_id_references_get) | **GET** /api/v2/workItems/sharedSteps/{sharedStepId}/references | Get SharedStep references
[**create_work_item**](WorkItemsApi.md#create_work_item) | **POST** /api/v2/workItems | Create Test Case, Checklist or Shared Step
[**delete_all_work_items_from_auto_test**](WorkItemsApi.md#delete_all_work_items_from_auto_test) | **DELETE** /api/v2/workItems/{id}/autoTests | Delete all links AutoTests from WorkItem by Id or GlobalId
[**delete_work_item**](WorkItemsApi.md#delete_work_item) | **DELETE** /api/v2/workItems/{id} | Delete Test Case, Checklist or Shared Step by Id or GlobalId
[**get_auto_tests_for_work_item**](WorkItemsApi.md#get_auto_tests_for_work_item) | **GET** /api/v2/workItems/{id}/autoTests | Get all AutoTests linked to WorkItem by Id or GlobalId
[**get_iterations**](WorkItemsApi.md#get_iterations) | **GET** /api/v2/workItems/{id}/iterations | Get iterations by workitem Id or GlobalId
[**get_work_item_by_id**](WorkItemsApi.md#get_work_item_by_id) | **GET** /api/v2/workItems/{id} | Get Test Case, Checklist or Shared Step by Id or GlobalId
[**get_work_item_chronology**](WorkItemsApi.md#get_work_item_chronology) | **GET** /api/v2/workItems/{id}/chronology | Get WorkItem chronology by Id or GlobalId
[**get_work_item_versions**](WorkItemsApi.md#get_work_item_versions) | **GET** /api/v2/workItems/{id}/versions | Get WorkItem versions
[**update_work_item**](WorkItemsApi.md#update_work_item) | **PUT** /api/v2/workItems | Update Test Case, Checklist or Shared Step


# **api_v2_work_items_id_check_list_transform_to_test_case_post**
> WorkItemModel api_v2_work_items_id_check_list_transform_to_test_case_post(id)

Transform CheckList to TestCase

<br>Use case  <br>User sets checklist identifier  <br>User runs method execution  <br>System transform CheckList to TestCase

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.work_item_model import WorkItemModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Transform CheckList to TestCase
        api_response = api_instance.api_v2_work_items_id_check_list_transform_to_test_case_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**422** | Client Error |  -  |
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library required |  -  |
**404** | Can&#39;t find CheckList with id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_history_get**
> [WorkItemChangeModel] api_v2_work_items_id_history_get(id)

Get change history of WorkItem

<br>Use case  <br>User sets workitem identifier  <br>User runs method execution  <br>System return change history of WorkItem

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.work_item_change_model import WorkItemChangeModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "id_example" # str | 
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get change history of WorkItem
        api_response = api_instance.api_v2_work_items_id_history_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get change history of WorkItem
        api_response = api_instance.api_v2_work_items_id_history_get(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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

[**[WorkItemChangeModel]**](WorkItemChangeModel.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_like_delete**
> api_v2_work_items_id_like_delete(id)

Delete like from WorkItem

<br>Use case  <br>User sets WorkItem identifier  <br>User runs method execution  <br>System delete like from WorkItem

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete like from WorkItem
        api_instance.api_v2_work_items_id_like_delete(id)
    except testit_api_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_like_post**
> api_v2_work_items_id_like_post(id)

Set like to WorkItem

<br>Use case  <br>User sets WorkItem identifier  <br>User runs method execution  <br>System set like to WorkItem

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set like to WorkItem
        api_instance.api_v2_work_items_id_like_post(id)
    except testit_api_client.ApiException as e:
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
**400** | Bad Request |  -  |
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_likes_count_get**
> int api_v2_work_items_id_likes_count_get(id)

Get likes count of WorkItem

<br>Use case  <br>User sets WorkItem identifier  <br>User runs method execution  <br>System return likes count of WorkItem

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get likes count of WorkItem
        api_response = api_instance.api_v2_work_items_id_likes_count_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_likes_get**
> [WorkItemLikeModel] api_v2_work_items_id_likes_get(id)

Get likes of WorkItem

<br>Use case  <br>User sets WorkItem identifier  <br>User runs method execution  <br>System return likes of WorkItem

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.work_item_like_model import WorkItemLikeModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get likes of WorkItem
        api_response = api_instance.api_v2_work_items_id_likes_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_likes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[WorkItemLikeModel]**](WorkItemLikeModel.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_test_results_history_get**
> [TestResultHistoryReportModel] api_v2_work_items_id_test_results_history_get(id)

Get test results history of WorkItem

<br>Use case  <br>User sets WorkItem identifier  <br>User runs method execution  <br>System return test results history of WorkItem

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.test_result_history_report_model import TestResultHistoryReportModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "id_example" # str | 
    _from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Take results from this date (optional)
    to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Take results until this date (optional)
    configuration_ids = [
        "configurationIds_example",
    ] # [str] | Identifiers of test result configurations (optional)
    test_plan_ids = [
        "testPlanIds_example",
    ] # [str] | Identifiers of test plans which contain test results (optional)
    user_ids = [
        "userIds_example",
    ] # [str] | Identifiers of users who set test results (optional)
    outcomes = [
        "outcomes_example",
    ] # [str] | List of outcomes of test results (optional)
    is_automated = True # bool | OBSOLETE: Use `Automated` instead (optional)
    automated = True # bool | If result must consist of only manual/automated test results (optional)
    test_run_ids = [
        "testRunIds_example",
    ] # [str] | Identifiers of test runs which contain test results (optional)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get test results history of WorkItem
        api_response = api_instance.api_v2_work_items_id_test_results_history_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_test_results_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get test results history of WorkItem
        api_response = api_instance.api_v2_work_items_id_test_results_history_get(id, _from=_from, to=to, configuration_ids=configuration_ids, test_plan_ids=test_plan_ids, user_ids=user_ids, outcomes=outcomes, is_automated=is_automated, automated=automated, test_run_ids=test_run_ids, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_id_test_results_history_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **_from** | **datetime**| Take results from this date | [optional]
 **to** | **datetime**| Take results until this date | [optional]
 **configuration_ids** | **[str]**| Identifiers of test result configurations | [optional]
 **test_plan_ids** | **[str]**| Identifiers of test plans which contain test results | [optional]
 **user_ids** | **[str]**| Identifiers of users who set test results | [optional]
 **outcomes** | **[str]**| List of outcomes of test results | [optional]
 **is_automated** | **bool**| OBSOLETE: Use &#x60;Automated&#x60; instead | [optional]
 **automated** | **bool**| If result must consist of only manual/automated test results | [optional]
 **test_run_ids** | **[str]**| Identifiers of test runs which contain test results | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestResultHistoryReportModel]**](TestResultHistoryReportModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_version_version_id_actual_post**
> WorkItemModel api_v2_work_items_id_version_version_id_actual_post(id, version_id)

Set WorkItem as actual

<br>Use case  <br>User sets workitem identifier  <br>User runs method execution  <br>System set WorkItem as actual

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.work_item_model import WorkItemModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "id_example" # str | 
    version_id = "versionId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Set WorkItem as actual
        api_response = api_instance.api_v2_work_items_id_version_version_id_actual_post(id, version_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_move_post**
> WorkItemShortModel api_v2_work_items_move_post()

Move WorkItem to another section

<br>Use case  <br>User sets WorkItem identifier  <br>User runs method execution  <br>System move WorkItem to another section

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.work_item_short_model import WorkItemShortModel
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.work_item_move_post_model import WorkItemMovePostModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    work_item_move_post_model = WorkItemMovePostModel(
        id="id_example",
        new_section_id="new_section_id_example",
        old_section_id="old_section_id_example",
        next_work_item_id="next_work_item_id_example",
    ) # WorkItemMovePostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Move WorkItem to another section
        api_response = api_instance.api_v2_work_items_move_post(work_item_move_post_model=work_item_move_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**400** | Bad Request |  -  |
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_search_post**
> [WorkItemShortModel] api_v2_work_items_search_post()

Search for work items

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.work_item_select_model import WorkItemSelectModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.work_item_short_model import WorkItemShortModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    work_item_select_model = WorkItemSelectModel(
        filter=WorkItemFilterModel(
            name_or_id="name_or_id_example",
            include_ids=[
                "include_ids_example",
            ],
            exclude_ids=[
                "exclude_ids_example",
            ],
            name="name_example",
            ids=[
                "ids_example",
            ],
            global_ids=[
                1,
            ],
            attributes={
                "key": [
                    "key_example",
                ],
            },
            is_deleted=True,
            project_ids=[
                "project_ids_example",
            ],
            section_ids=[
                "section_ids_example",
            ],
            created_by_ids=[
                "created_by_ids_example",
            ],
            modified_by_ids=[
                "modified_by_ids_example",
            ],
            states=[
                WorkItemStates("NeedsWork"),
            ],
            priorities=[
                WorkItemPriorityModel("Lowest"),
            ],
            types=[
                WorkItemEntityTypes("TestCases"),
            ],
            created_date=DateTimeRangeSelectorModel(
                _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            modified_date=DateTimeRangeSelectorModel(
                _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            duration=Int32RangeSelectorModel(
                _from=1,
                to=1,
            ),
            is_automated=True,
            tags=[
                "tags_example",
            ],
            auto_test_ids=[
                "auto_test_ids_example",
            ],
        ),
        extraction_model=WorkItemsExtractionModel(
            ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
            section_ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
            project_ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
        ),
    ) # WorkItemSelectModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for work items
        api_response = api_instance.api_v2_work_items_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_select_model=work_item_select_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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

[**[WorkItemShortModel]**](WorkItemShortModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**403** | Test library read permission for all requested projects is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_shared_step_id_references_sections_post**
> [SharedStepReferenceSectionModel] api_v2_work_items_shared_step_id_references_sections_post(shared_step_id)

Get SharedStep references in sections

<br>Use case  <br>User sets SharedStep identifier  <br>User runs method execution  <br>System return SharedStep references

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.shared_step_reference_section_model import SharedStepReferenceSectionModel
from testit_api_client.model.shared_step_reference_sections_query_filter_model import SharedStepReferenceSectionsQueryFilterModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    shared_step_id = "sharedStepId_example" # str | 
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    shared_step_reference_sections_query_filter_model = SharedStepReferenceSectionsQueryFilterModel(
        name="name_example",
        created_by_ids=[
            "created_by_ids_example",
        ],
        modified_by_ids=[
            "modified_by_ids_example",
        ],
        created_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        modified_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
    ) # SharedStepReferenceSectionsQueryFilterModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get SharedStep references in sections
        api_response = api_instance.api_v2_work_items_shared_step_id_references_sections_post(shared_step_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_shared_step_id_references_sections_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SharedStep references in sections
        api_response = api_instance.api_v2_work_items_shared_step_id_references_sections_post(shared_step_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, shared_step_reference_sections_query_filter_model=shared_step_reference_sections_query_filter_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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

[**[SharedStepReferenceSectionModel]**](SharedStepReferenceSectionModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**401** | Unauthorized |  -  |
**404** | Can&#39;t find SharedStep with id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_shared_step_id_references_work_items_post**
> [SharedStepReferenceModel] api_v2_work_items_shared_step_id_references_work_items_post(shared_step_id)

Get SharedStep references in workitems

<br>Use case  <br>User sets SharedStep identifier  <br>User runs method execution  <br>System return SharedStep references

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.shared_step_reference_model import SharedStepReferenceModel
from testit_api_client.model.shared_step_references_query_filter_model import SharedStepReferencesQueryFilterModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    shared_step_id = "sharedStepId_example" # str | 
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    shared_step_references_query_filter_model = SharedStepReferencesQueryFilterModel(
        name="name_example",
        global_ids=[
            1,
        ],
        section_ids=[
            "section_ids_example",
        ],
        created_by_ids=[
            "created_by_ids_example",
        ],
        modified_by_ids=[
            "modified_by_ids_example",
        ],
        states=[
            WorkItemStates("NeedsWork"),
        ],
        priorities=[
            WorkItemPriorityModel("Lowest"),
        ],
        entity_types=[
            "entity_types_example",
        ],
        created_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        modified_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        is_automated=True,
        tags=[
            "tags_example",
        ],
    ) # SharedStepReferencesQueryFilterModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get SharedStep references in workitems
        api_response = api_instance.api_v2_work_items_shared_step_id_references_work_items_post(shared_step_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_shared_step_id_references_work_items_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get SharedStep references in workitems
        api_response = api_instance.api_v2_work_items_shared_step_id_references_work_items_post(shared_step_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, shared_step_references_query_filter_model=shared_step_references_query_filter_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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

[**[SharedStepReferenceModel]**](SharedStepReferenceModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**401** | Unauthorized |  -  |
**404** | Can&#39;t find SharedStep with id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_shared_steps_shared_step_id_references_get**
> [SharedStepReferenceModel] api_v2_work_items_shared_steps_shared_step_id_references_get(shared_step_id)

Get SharedStep references

<br>Use case  <br>User sets SharedStep identifier  <br>User runs method execution  <br>System return SharedStep references

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.shared_step_reference_model import SharedStepReferenceModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    shared_step_id = "sharedStepId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get SharedStep references
        api_response = api_instance.api_v2_work_items_shared_steps_shared_step_id_references_get(shared_step_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->api_v2_work_items_shared_steps_shared_step_id_references_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_step_id** | **str**|  |

### Return type

[**[SharedStepReferenceModel]**](SharedStepReferenceModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**404** | Can&#39;t find SharedStep with id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_work_item**
> WorkItemModel create_work_item()

Create Test Case, Checklist or Shared Step

<br>Use case  <br>User sets workitem properties (listed in request parameters)  <br>User runs method execution  <br>System creates workitem by identifier  <br>System returns workitem model (listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.work_item_post_model import WorkItemPostModel
from testit_api_client.model.work_item_model import WorkItemModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    work_item_post_model = WorkItemPostModel(
        entity_type_name=WorkItemEntityTypes("TestCases"),
        description="This is a basic test template",
        state=WorkItemStates("NeedsWork"),
        priority=WorkItemPriorityModel("Lowest"),
        steps=[
            StepPutModel(
                id="573f916c-d8ad-4f87-846f-4dba1839ae56",
                action="User press the button",
                expected="System makes a beeeep sound",
                test_data="Some variables values",
                comments="Comment on what to look for",
                work_item_id="573f916c-d8ad-4f87-846f-4dba1839ae56",
            ),
        ],
        precondition_steps=[
            StepPutModel(
                id="573f916c-d8ad-4f87-846f-4dba1839ae56",
                action="User press the button",
                expected="System makes a beeeep sound",
                test_data="Some variables values",
                comments="Comment on what to look for",
                work_item_id="573f916c-d8ad-4f87-846f-4dba1839ae56",
            ),
        ],
        postcondition_steps=[
            StepPutModel(
                id="573f916c-d8ad-4f87-846f-4dba1839ae56",
                action="User press the button",
                expected="System makes a beeeep sound",
                test_data="Some variables values",
                comments="Comment on what to look for",
                work_item_id="573f916c-d8ad-4f87-846f-4dba1839ae56",
            ),
        ],
        duration=10000,
        attributes={
            "key": None,
        },
        tags=[
            TagShortModel(
                name="name_example",
            ),
        ],
        attachments=[
            AttachmentPutModel(
                id="id_example",
            ),
        ],
        iterations=[
            IterationPutModel(
                parameters=[
                    ParameterIterationModel(
                        id="573f916c-d8ad-4f87-846f-4dba1839ae56",
                    ),
                ],
                id="00000000-0000-0000-0000-000000000000",
            ),
        ],
        links=[
            LinkPostModel(
                title="title_example",
                url="url_example",
                description="description_example",
                type=LinkType("Related"),
                has_info=True,
            ),
        ],
        name="Basic template",
        project_id="573f916c-d8ad-4f87-846f-4dba1839ae56",
        section_id="573f916c-d8ad-4f87-846f-4dba1839ae56",
        auto_tests=[
            AutoTestIdModel(
                id="id_example",
            ),
        ],
    ) # WorkItemPostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Test Case, Checklist or Shared Step
        api_response = api_instance.create_work_item(work_item_post_model=work_item_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**404** | &lt;br&gt;Can&#39;t find section  &lt;br&gt;Can&#39;t find project  &lt;br&gt;Can&#39;t find attachmentIds  &lt;br&gt;Project not found  &lt;br&gt;Can&#39;t attributesScheme  &lt;br&gt;Can&#39;t attribute  &lt;br&gt;AutoTestIds not exist in project |  -  |
**201** | Successful operation |  -  |
**400** | &lt;br&gt;Field is required  &lt;br&gt;Priority is not a valid  &lt;br&gt;Tags must be set  &lt;br&gt;Duration should be a positive number  &lt;br&gt;Should be empty for CheckList  &lt;br&gt;Attribute value must be a valid guid for user scheme  &lt;br&gt;There is no option in ProjectAttributesScheme with such Id  &lt;br&gt;Attribute value must be a valid guid for options scheme |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_work_items_from_auto_test**
> delete_all_work_items_from_auto_test(id)

Delete all links AutoTests from WorkItem by Id or GlobalId

<br>Use case  <br>User sets workitem identifier  <br>User runs method execution  <br>System search workitem by identifier  <br>System search and delete all autotests, related to found workitem  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | WorkItem internal (guid format) or  global(integer format) identifier\"

    # example passing only required values which don't have defaults set
    try:
        # Delete all links AutoTests from WorkItem by Id or GlobalId
        api_instance.delete_all_work_items_from_auto_test(id)
    except testit_api_client.ApiException as e:
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
**400** | Bad Request |  -  |
**404** | Can&#39;t find a WorkItem with workItemId |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library required |  -  |
**204** | No Content |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_item**
> delete_work_item(id)

Delete Test Case, Checklist or Shared Step by Id or GlobalId

<br>Use case  <br>User sets workitem identifier  <br>User runs method execution  <br>System deletes workitem  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | WorkItem internal (guid format) or  global(integer format) identifier\"

    # example passing only required values which don't have defaults set
    try:
        # Delete Test Case, Checklist or Shared Step by Id or GlobalId
        api_instance.delete_work_item(id)
    except testit_api_client.ApiException as e:
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
**401** | Unauthorized |  -  |
**422** | Could not delete Shared Step that has references |  -  |
**400** | Bad Request |  -  |
**404** | Can&#39;t find a WorkItem with id |  -  |
**403** | Delete permission for test library required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_tests_for_work_item**
> [AutoTestModel] get_auto_tests_for_work_item(id)

Get all AutoTests linked to WorkItem by Id or GlobalId

<br>Use case  <br>User sets workitem identifier  <br>User runs method execution  <br>System search workitem by identifier  <br>System search all autotests, related to found workitem  <br>System returns list of found autotests

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.auto_test_model import AutoTestModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | WorkItem internal (guid format) or  global(integer format) identifier\"

    # example passing only required values which don't have defaults set
    try:
        # Get all AutoTests linked to WorkItem by Id or GlobalId
        api_response = api_instance.get_auto_tests_for_work_item(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->get_auto_tests_for_work_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WorkItem internal (guid format) or  global(integer format) identifier\&quot; |

### Return type

[**[AutoTestModel]**](AutoTestModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**200** | Successful operation |  -  |
**403** | Read permission for test library required |  -  |
**404** | Can&#39;t find WorkItem with workItemId |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_iterations**
> [IterationModel] get_iterations(id)

Get iterations by workitem Id or GlobalId

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.iteration_model import IterationModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | WorkItem internal (guid format) or  global(integer format) identifier\"
    version_id = "00000000-0000-0000-0000-000000000000" # str | WorkItem version (guid format) identifier (optional)
    version_number = 0 # int | WorkItem version number (0 is the last version)\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get iterations by workitem Id or GlobalId
        api_response = api_instance.get_iterations(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->get_iterations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get iterations by workitem Id or GlobalId
        api_response = api_instance.get_iterations(id, version_id=version_id, version_number=version_number)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->get_iterations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WorkItem internal (guid format) or  global(integer format) identifier\&quot; |
 **version_id** | **str**| WorkItem version (guid format) identifier | [optional]
 **version_number** | **int**| WorkItem version number (0 is the last version)\&quot; | [optional]

### Return type

[**[IterationModel]**](IterationModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**404** | Can&#39;t find workItem with id |  -  |
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_item_by_id**
> WorkItemModel get_work_item_by_id(id)

Get Test Case, Checklist or Shared Step by Id or GlobalId

<br>Use case  <br>User sets workitem identifier  <br>[Optional] User sets workitem version identifier  <br>[Optional] User sets workitem version number  <br>User runs method execution  <br>System search workitem by identifier  <br>[Optional] if User sets workitem version identifier, system search workitem version by identifier.  <br>[Optional] if user sets workitem version number, system search workitem version by number  <br>Otherwise, system search last workitem version  <br>System returns workitem 

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.work_item_model import WorkItemModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | WorkItem internal (guid format) or  global(integer format) identifier\"
    version_id = "00000000-0000-0000-0000-000000000000" # str | WorkItem version (guid format) identifier\" (optional)
    version_number = 0 # int | WorkItem version number (0 is the last version)\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Test Case, Checklist or Shared Step by Id or GlobalId
        api_response = api_instance.get_work_item_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->get_work_item_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Test Case, Checklist or Shared Step by Id or GlobalId
        api_response = api_instance.get_work_item_by_id(id, version_id=version_id, version_number=version_number)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**403** | Read permission for test library required |  -  |
**404** | Can&#39;t find workItem with id |  -  |
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_item_chronology**
> [TestResultChronologyModel] get_work_item_chronology(id)

Get WorkItem chronology by Id or GlobalId

<br>Use case  <br>User sets workitem identifier  <br>User runs method execution  <br>System search workitem by identifier  <br>System search test results of all autotests, related to found workitem  <br>System sort results by CompletedOn ascending, then by CreatedDate ascending  <br>System returns sorted collection of test results

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.test_result_chronology_model import TestResultChronologyModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get WorkItem chronology by Id or GlobalId
        api_response = api_instance.get_work_item_chronology(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->get_work_item_chronology: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[TestResultChronologyModel]**](TestResultChronologyModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**404** | Can&#39;t find WorkItem with workItemId |  -  |
**200** | Successful operation |  -  |
**400** | Not valid workItemId |  -  |
**403** | Read permission for test library required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_item_versions**
> [WorkItemVersionModel] get_work_item_versions(id)

Get WorkItem versions

<br>Use case  <br>User sets workitem identifier  <br>[Optional] User sets workitem version identifier  <br>User runs method execution  <br>System search workitem by identifier  <br>                      [Optional] If User set workitem version identifier, System search workitem version by version identifier                      Otherwise, system search all version of workitem                    <br>System returns array of workitem version models (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.work_item_version_model import WorkItemVersionModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | WorkItem internal (guid format) or  global(integer format) identifier\"
    work_item_version_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | WorkItem version (guid format)  identifier\" (optional)
    version_number = 1 # int | WorkItem version (integer format)  number\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get WorkItem versions
        api_response = api_instance.get_work_item_versions(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->get_work_item_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get WorkItem versions
        api_response = api_instance.get_work_item_versions(id, work_item_version_id=work_item_version_id, version_number=version_number)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsApi->get_work_item_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| WorkItem internal (guid format) or  global(integer format) identifier\&quot; |
 **work_item_version_id** | **str**| WorkItem version (guid format)  identifier\&quot; | [optional]
 **version_number** | **int**| WorkItem version (integer format)  number\&quot; | [optional]

### Return type

[**[WorkItemVersionModel]**](WorkItemVersionModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | Can&#39;t find WorkItem with workItemId |  -  |
**400** | Bad Request |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_work_item**
> update_work_item()

Update Test Case, Checklist or Shared Step

<br>Use case  <br>User sets workitem properties (listed in request parameters)  <br>User runs method execution  <br>System updates workitem by identifier  <br>System returns updated workitem model (listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_api
from testit_api_client.model.work_item_put_model import WorkItemPutModel
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
    api_instance = work_items_api.WorkItemsApi(api_client)
    work_item_put_model = WorkItemPutModel(
        attachments=[
            AttachmentPutModel(
                id="id_example",
            ),
        ],
        iterations=[
            IterationPutModel(
                parameters=[
                    ParameterIterationModel(
                        id="573f916c-d8ad-4f87-846f-4dba1839ae56",
                    ),
                ],
                id="00000000-0000-0000-0000-000000000000",
            ),
        ],
        auto_tests=[
            AutoTestIdModel(
                id="id_example",
            ),
        ],
        id="573f916c-d8ad-4f87-846f-4dba1839ae56",
        section_id="573f916c-d8ad-4f87-846f-4dba1839ae56",
        description="This is a basic test template",
        state=WorkItemStates("NeedsWork"),
        priority=WorkItemPriorityModel("Lowest"),
        steps=[
            StepPutModel(
                id="573f916c-d8ad-4f87-846f-4dba1839ae56",
                action="User press the button",
                expected="System makes a beeeep sound",
                test_data="Some variables values",
                comments="Comment on what to look for",
                work_item_id="573f916c-d8ad-4f87-846f-4dba1839ae56",
            ),
        ],
        precondition_steps=[
            StepPutModel(
                id="573f916c-d8ad-4f87-846f-4dba1839ae56",
                action="User press the button",
                expected="System makes a beeeep sound",
                test_data="Some variables values",
                comments="Comment on what to look for",
                work_item_id="573f916c-d8ad-4f87-846f-4dba1839ae56",
            ),
        ],
        postcondition_steps=[
            StepPutModel(
                id="573f916c-d8ad-4f87-846f-4dba1839ae56",
                action="User press the button",
                expected="System makes a beeeep sound",
                test_data="Some variables values",
                comments="Comment on what to look for",
                work_item_id="573f916c-d8ad-4f87-846f-4dba1839ae56",
            ),
        ],
        duration=10000,
        attributes={
            "key": None,
        },
        tags=[
            TagShortModel(
                name="name_example",
            ),
        ],
        links=[
            LinkPutModel(
                id="573f916c-d8ad-4f87-846f-4dba1839ae56",
                title="title_example",
                url="url_example",
                description="description_example",
                type=LinkType("Related"),
                has_info=True,
            ),
        ],
        name="Basic template",
    ) # WorkItemPutModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Test Case, Checklist or Shared Step
        api_instance.update_work_item(work_item_put_model=work_item_put_model)
    except testit_api_client.ApiException as e:
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
**401** | Unauthorized |  -  |
**403** | Update permission for test library required |  -  |
**404** | &lt;br&gt;WorkItem not found  &lt;br&gt;Can&#39;t find section  &lt;br&gt;Can&#39;t attributesScheme  &lt;br&gt;Can&#39;t attribute  &lt;br&gt;AutoTestIds not exist in project |  -  |
**400** | &lt;br&gt;Field is required  &lt;br&gt;Priority is not a valid  &lt;br&gt;duration should be a positive number  &lt;br&gt;should be empty for CheckList  &lt;br&gt;There is no option in ProjectAttributesScheme with such Id  &lt;br&gt;Attribute value must be a valid guid for options scheme |  -  |
**204** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

