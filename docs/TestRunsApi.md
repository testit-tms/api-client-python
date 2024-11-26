# testit_api_client.TestRunsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_test_runs_delete**](TestRunsApi.md#api_v2_test_runs_delete) | **DELETE** /api/v2/testRuns | Delete multiple test runs
[**api_v2_test_runs_id_auto_tests_namespaces_get**](TestRunsApi.md#api_v2_test_runs_id_auto_tests_namespaces_get) | **GET** /api/v2/testRuns/{id}/autoTestsNamespaces | Get autotest classes and namespaces in test run
[**api_v2_test_runs_id_delete**](TestRunsApi.md#api_v2_test_runs_id_delete) | **DELETE** /api/v2/testRuns/{id} | Delete test run
[**api_v2_test_runs_id_purge_post**](TestRunsApi.md#api_v2_test_runs_id_purge_post) | **POST** /api/v2/testRuns/{id}/purge | Permanently delete test run from archive
[**api_v2_test_runs_id_reruns_post**](TestRunsApi.md#api_v2_test_runs_id_reruns_post) | **POST** /api/v2/testRuns/{id}/reruns | Manual autotests rerun in test run
[**api_v2_test_runs_id_restore_post**](TestRunsApi.md#api_v2_test_runs_id_restore_post) | **POST** /api/v2/testRuns/{id}/restore | Restore test run from the archive
[**api_v2_test_runs_id_statistics_filter_post**](TestRunsApi.md#api_v2_test_runs_id_statistics_filter_post) | **POST** /api/v2/testRuns/{id}/statistics/filter | Search for the test run test results and build statistics
[**api_v2_test_runs_id_test_points_results_get**](TestRunsApi.md#api_v2_test_runs_id_test_points_results_get) | **GET** /api/v2/testRuns/{id}/testPoints/results | Get test results from the test run grouped by test points
[**api_v2_test_runs_id_test_results_bulk_put**](TestRunsApi.md#api_v2_test_runs_id_test_results_bulk_put) | **PUT** /api/v2/testRuns/{id}/testResults/bulk | Partial edit of multiple test results in the test run
[**api_v2_test_runs_id_test_results_last_modified_modification_date_get**](TestRunsApi.md#api_v2_test_runs_id_test_results_last_modified_modification_date_get) | **GET** /api/v2/testRuns/{id}/testResults/lastModified/modificationDate | Get modification date of last test result of the test run
[**api_v2_test_runs_purge_bulk_post**](TestRunsApi.md#api_v2_test_runs_purge_bulk_post) | **POST** /api/v2/testRuns/purge/bulk | Permanently delete multiple test runs from archive
[**api_v2_test_runs_restore_bulk_post**](TestRunsApi.md#api_v2_test_runs_restore_bulk_post) | **POST** /api/v2/testRuns/restore/bulk | Restore multiple test runs from the archive
[**api_v2_test_runs_search_post**](TestRunsApi.md#api_v2_test_runs_search_post) | **POST** /api/v2/testRuns/search | Search for test runs
[**api_v2_test_runs_update_multiple_post**](TestRunsApi.md#api_v2_test_runs_update_multiple_post) | **POST** /api/v2/testRuns/updateMultiple | Update multiple test runs
[**complete_test_run**](TestRunsApi.md#complete_test_run) | **POST** /api/v2/testRuns/{id}/complete | Complete TestRun
[**create_and_fill_by_auto_tests**](TestRunsApi.md#create_and_fill_by_auto_tests) | **POST** /api/v2/testRuns/byAutoTests | Create test runs based on autotests and configurations
[**create_and_fill_by_configurations**](TestRunsApi.md#create_and_fill_by_configurations) | **POST** /api/v2/testRuns/byConfigurations | Create test runs picking the needed test points
[**create_and_fill_by_work_items**](TestRunsApi.md#create_and_fill_by_work_items) | **POST** /api/v2/testRuns/byWorkItems | Create test run based on configurations and work items
[**create_empty**](TestRunsApi.md#create_empty) | **POST** /api/v2/testRuns | Create empty TestRun
[**get_test_run_by_id**](TestRunsApi.md#get_test_run_by_id) | **GET** /api/v2/testRuns/{id} | Get TestRun by Id
[**set_auto_test_results_for_test_run**](TestRunsApi.md#set_auto_test_results_for_test_run) | **POST** /api/v2/testRuns/{id}/testResults | Send test results to the test runs in the system
[**start_test_run**](TestRunsApi.md#start_test_run) | **POST** /api/v2/testRuns/{id}/start | Start TestRun
[**stop_test_run**](TestRunsApi.md#stop_test_run) | **POST** /api/v2/testRuns/{id}/stop | Stop TestRun
[**update_empty**](TestRunsApi.md#update_empty) | **PUT** /api/v2/testRuns | Update empty TestRun


# **api_v2_test_runs_delete**
> int api_v2_test_runs_delete()

Delete multiple test runs

 Use case   User sets selection parameters of test runs   System search and delete collection of test runs   System returns the number of deleted test runs

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.test_run_select_model import TestRunSelectModel
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    test_run_select_model = TestRunSelectModel(
        filter=ApiV2TestRunsSearchPostRequest(None),
        extraction_model=TestRunSelectModelExtractionModel(None),
    ) # TestRunSelectModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete multiple test runs
        api_response = api_instance.api_v2_test_runs_delete(test_run_select_model=test_run_select_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_select_model** | [**TestRunSelectModel**](TestRunSelectModel.md)|  | [optional]

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
**400** |  - ID is not valid   - Project was archived and cannot be edited anymore |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_id_auto_tests_namespaces_get**
> AutoTestNamespacesCountResponse api_v2_test_runs_id_auto_tests_namespaces_get(id)

Get autotest classes and namespaces in test run

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.auto_test_namespaces_count_response import AutoTestNamespacesCountResponse
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get autotest classes and namespaces in test run
        api_response = api_instance.api_v2_test_runs_id_auto_tests_namespaces_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_auto_tests_namespaces_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**AutoTestNamespacesCountResponse**](AutoTestNamespacesCountResponse.md)

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

# **api_v2_test_runs_id_delete**
> api_v2_test_runs_id_delete(id)

Delete test run

 Use case   User sets test run internal (guid format) identifier   System search and delete test run

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "id_example" # str | Test run internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete test run
        api_instance.api_v2_test_runs_id_delete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test run internal (UUID) identifier |

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
**400** |  - ID is not valid   - Project was archived and cannot be edited anymore |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Test run with provided ID cannot be found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_id_purge_post**
> api_v2_test_runs_id_purge_post(id)

Permanently delete test run from archive

 Use case   User sets archived test run internal (guid format) identifier   System search and purge archived test run

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "id_example" # str | Test run internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Permanently delete test run from archive
        api_instance.api_v2_test_runs_id_purge_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_purge_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test run internal (UUID) identifier |

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
**400** |  - ID is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | Delete permission for archived test runs is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_id_reruns_post**
> ManualRerunResultModel api_v2_test_runs_id_reruns_post(id)

Manual autotests rerun in test run

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.api_v2_test_runs_id_reruns_post_request import ApiV2TestRunsIdRerunsPostRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.manual_rerun_result_model import ManualRerunResultModel
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "id_example" # str | 
    api_v2_test_runs_id_reruns_post_request = ApiV2TestRunsIdRerunsPostRequest(None) # ApiV2TestRunsIdRerunsPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Manual autotests rerun in test run
        api_response = api_instance.api_v2_test_runs_id_reruns_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_reruns_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Manual autotests rerun in test run
        api_response = api_instance.api_v2_test_runs_id_reruns_post(id, api_v2_test_runs_id_reruns_post_request=api_v2_test_runs_id_reruns_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_reruns_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **api_v2_test_runs_id_reruns_post_request** | [**ApiV2TestRunsIdRerunsPostRequest**](ApiV2TestRunsIdRerunsPostRequest.md)|  | [optional]

### Return type

[**ManualRerunResultModel**](ManualRerunResultModel.md)

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

# **api_v2_test_runs_id_restore_post**
> api_v2_test_runs_id_restore_post(id)

Restore test run from the archive

 Use case   User sets archived test run internal (guid format) identifier   System search and restore test run

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "id_example" # str | Unique ID of the test run

    # example passing only required values which don't have defaults set
    try:
        # Restore test run from the archive
        api_instance.api_v2_test_runs_id_restore_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_restore_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the test run |

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
**400** |  - ID is not valid   - Project was archived and cannot be edited anymore |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_id_statistics_filter_post**
> TestResultsStatisticsGetModel api_v2_test_runs_id_statistics_filter_post(id)

Search for the test run test results and build statistics

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_test_runs_id_statistics_filter_post_request import ApiV2TestRunsIdStatisticsFilterPostRequest
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.test_results_statistics_get_model import TestResultsStatisticsGetModel
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "id_example" # str | Test run unique ID
    api_v2_test_runs_id_statistics_filter_post_request = ApiV2TestRunsIdStatisticsFilterPostRequest(None) # ApiV2TestRunsIdStatisticsFilterPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for the test run test results and build statistics
        api_response = api_instance.api_v2_test_runs_id_statistics_filter_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_statistics_filter_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for the test run test results and build statistics
        api_response = api_instance.api_v2_test_runs_id_statistics_filter_post(id, api_v2_test_runs_id_statistics_filter_post_request=api_v2_test_runs_id_statistics_filter_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_statistics_filter_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test run unique ID |
 **api_v2_test_runs_id_statistics_filter_post_request** | [**ApiV2TestRunsIdStatisticsFilterPostRequest**](ApiV2TestRunsIdStatisticsFilterPostRequest.md)|  | [optional]

### Return type

[**TestResultsStatisticsGetModel**](TestResultsStatisticsGetModel.md)

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
**403** | Read permission for test runs is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_id_test_points_results_get**
> [TestPointResultModel] api_v2_test_runs_id_test_points_results_get(id)

Get test results from the test run grouped by test points

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.test_point_result_model import TestPointResultModel
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "id_example" # str | Test run unique ID

    # example passing only required values which don't have defaults set
    try:
        # Get test results from the test run grouped by test points
        api_response = api_instance.api_v2_test_runs_id_test_points_results_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_test_points_results_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test run unique ID |

### Return type

[**[TestPointResultModel]**](TestPointResultModel.md)

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
**403** | Read permission for test runs is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_id_test_results_bulk_put**
> api_v2_test_runs_id_test_results_bulk_put(id)

Partial edit of multiple test results in the test run

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.api_v2_test_runs_id_test_results_bulk_put_request import ApiV2TestRunsIdTestResultsBulkPutRequest
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "id_example" # str | Test run unique ID
    api_v2_test_runs_id_test_results_bulk_put_request = ApiV2TestRunsIdTestResultsBulkPutRequest(None) # ApiV2TestRunsIdTestResultsBulkPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Partial edit of multiple test results in the test run
        api_instance.api_v2_test_runs_id_test_results_bulk_put(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_test_results_bulk_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Partial edit of multiple test results in the test run
        api_instance.api_v2_test_runs_id_test_results_bulk_put(id, api_v2_test_runs_id_test_results_bulk_put_request=api_v2_test_runs_id_test_results_bulk_put_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_test_results_bulk_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test run unique ID |
 **api_v2_test_runs_id_test_results_bulk_put_request** | [**ApiV2TestRunsIdTestResultsBulkPutRequest**](ApiV2TestRunsIdTestResultsBulkPutRequest.md)|  | [optional]

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
**403** | Update permission for test runs is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_id_test_results_last_modified_modification_date_get**
> datetime api_v2_test_runs_id_test_results_last_modified_modification_date_get(id)

Get modification date of last test result of the test run

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "id_example" # str | Test run unique ID

    # example passing only required values which don't have defaults set
    try:
        # Get modification date of last test result of the test run
        api_response = api_instance.api_v2_test_runs_id_test_results_last_modified_modification_date_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_test_results_last_modified_modification_date_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test run unique ID |

### Return type

**datetime**

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
**403** | Read permission for test runs is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_purge_bulk_post**
> int api_v2_test_runs_purge_bulk_post()

Permanently delete multiple test runs from archive

 Use case   User sets selection parameters of archived test runs   System search and delete collection of archived test runs   System returns the number of deleted archived test runs

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.api_v2_test_runs_purge_bulk_post_request import ApiV2TestRunsPurgeBulkPostRequest
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    api_v2_test_runs_purge_bulk_post_request = ApiV2TestRunsPurgeBulkPostRequest(None) # ApiV2TestRunsPurgeBulkPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Permanently delete multiple test runs from archive
        api_response = api_instance.api_v2_test_runs_purge_bulk_post(api_v2_test_runs_purge_bulk_post_request=api_v2_test_runs_purge_bulk_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_purge_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_test_runs_purge_bulk_post_request** | [**ApiV2TestRunsPurgeBulkPostRequest**](ApiV2TestRunsPurgeBulkPostRequest.md)|  | [optional]

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
**403** | Delete permission for archived test runs is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_restore_bulk_post**
> int api_v2_test_runs_restore_bulk_post()

Restore multiple test runs from the archive

 Use case   User sets selection parameters of archived test runs   System search and restore collection of archived test runs   System returns the number of restored test runs

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.api_v2_test_runs_purge_bulk_post_request import ApiV2TestRunsPurgeBulkPostRequest
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    api_v2_test_runs_purge_bulk_post_request = ApiV2TestRunsPurgeBulkPostRequest(None) # ApiV2TestRunsPurgeBulkPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restore multiple test runs from the archive
        api_response = api_instance.api_v2_test_runs_restore_bulk_post(api_v2_test_runs_purge_bulk_post_request=api_v2_test_runs_purge_bulk_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_restore_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_test_runs_purge_bulk_post_request** | [**ApiV2TestRunsPurgeBulkPostRequest**](ApiV2TestRunsPurgeBulkPostRequest.md)|  | [optional]

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
**403** | Read permission for archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_search_post**
> [TestRunShortGetModel] api_v2_test_runs_search_post()

Search for test runs

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.test_run_short_get_model import TestRunShortGetModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.api_v2_test_runs_search_post_request import ApiV2TestRunsSearchPostRequest
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    api_v2_test_runs_search_post_request = ApiV2TestRunsSearchPostRequest(None) # ApiV2TestRunsSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for test runs
        api_response = api_instance.api_v2_test_runs_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, api_v2_test_runs_search_post_request=api_v2_test_runs_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **api_v2_test_runs_search_post_request** | [**ApiV2TestRunsSearchPostRequest**](ApiV2TestRunsSearchPostRequest.md)|  | [optional]

### Return type

[**[TestRunShortGetModel]**](TestRunShortGetModel.md)

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

# **api_v2_test_runs_update_multiple_post**
> api_v2_test_runs_update_multiple_post()

Update multiple test runs

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_test_runs_update_multiple_post_request import ApiV2TestRunsUpdateMultiplePostRequest
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    api_v2_test_runs_update_multiple_post_request = ApiV2TestRunsUpdateMultiplePostRequest(None) # ApiV2TestRunsUpdateMultiplePostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update multiple test runs
        api_instance.api_v2_test_runs_update_multiple_post(api_v2_test_runs_update_multiple_post_request=api_v2_test_runs_update_multiple_post_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_update_multiple_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_test_runs_update_multiple_post_request** | [**ApiV2TestRunsUpdateMultiplePostRequest**](ApiV2TestRunsUpdateMultiplePostRequest.md)|  | [optional]

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_test_run**
> complete_test_run(id)

Complete TestRun

 Use case   User sets test run identifier   User runs method execution   System completes test run   System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test Run internal identifier (GUID format)

    # example passing only required values which don't have defaults set
    try:
        # Complete TestRun
        api_instance.complete_test_run(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->complete_test_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test Run internal identifier (GUID format) |

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
**400** |  Field is required   the StateName is already Stopped   the StateName is already Completed |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** |  Can&#39;t find a TestRun with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_and_fill_by_auto_tests**
> TestRunV2GetModel create_and_fill_by_auto_tests()

Create test runs based on autotests and configurations

This method creates a test run based on an autotest and a configuration.  The difference between the `POST /api/v2/testRuns/byWorkItems` and `POST /api/v2/testRuns/byConfigurations` methods is  that in this method there is no need to create a test plan and work items (test cases and checklists).

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.test_run_v2_get_model import TestRunV2GetModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.create_and_fill_by_auto_tests_request import CreateAndFillByAutoTestsRequest
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    create_and_fill_by_auto_tests_request = CreateAndFillByAutoTestsRequest(None) # CreateAndFillByAutoTestsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create test runs based on autotests and configurations
        api_response = api_instance.create_and_fill_by_auto_tests(create_and_fill_by_auto_tests_request=create_and_fill_by_auto_tests_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->create_and_fill_by_auto_tests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_and_fill_by_auto_tests_request** | [**CreateAndFillByAutoTestsRequest**](CreateAndFillByAutoTestsRequest.md)|  | [optional]

### Return type

[**TestRunV2GetModel**](TestRunV2GetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  - Field is required   - Configuration does not exist in the project   - Autotest does not exist in the project   - Test run must be automated   - Project ID is invalid   - Autotest external IDs are required   - Configuration IDs are required |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test results is required |  -  |
**404** | Some autotests do not exist |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_and_fill_by_configurations**
> TestRunV2GetModel create_and_fill_by_configurations()

Create test runs picking the needed test points

This method creates a test run based on a combination of a configuration and a work item(test case or checklist).  Before you create a test run using this method, make sure to create a test plan. Work items must be automated.  This method is different from the `POST /api/v2/testRuns/byWorkItems` method because of the ability to send a  jagged array within the \"<b>testPointSelectors</b>\" parameter.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.test_run_v2_get_model import TestRunV2GetModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.create_and_fill_by_configurations_request import CreateAndFillByConfigurationsRequest
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    create_and_fill_by_configurations_request = CreateAndFillByConfigurationsRequest(None) # CreateAndFillByConfigurationsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create test runs picking the needed test points
        api_response = api_instance.create_and_fill_by_configurations(create_and_fill_by_configurations_request=create_and_fill_by_configurations_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->create_and_fill_by_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_and_fill_by_configurations_request** | [**CreateAndFillByConfigurationsRequest**](CreateAndFillByConfigurationsRequest.md)|  | [optional]

### Return type

[**TestRunV2GetModel**](TestRunV2GetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  - Field is required   - Test run cannot be created with deleted test points   - Test suites with IDs [ids] is archived   - Configurations with IDs [ids] is archived   - Test run cannot be created with non-automated test point   - Test run must be automated   - Some work items do not exist   - Project ID is invalid   - Test point selectors are required   - Some work item IDs are invalid   - Some configuration IDs are invalid |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test results is required |  -  |
**404** | Some test points do not exists |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_and_fill_by_work_items**
> TestRunV2GetModel create_and_fill_by_work_items()

Create test run based on configurations and work items

This method creates a test run based on a combination of configuration and work item (test case or checklist).  Before you create a test run using this method, make sure to create a test plan.  Work items must be automated.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.test_run_v2_get_model import TestRunV2GetModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.create_and_fill_by_work_items_request import CreateAndFillByWorkItemsRequest
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    create_and_fill_by_work_items_request = CreateAndFillByWorkItemsRequest(None) # CreateAndFillByWorkItemsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create test run based on configurations and work items
        api_response = api_instance.create_and_fill_by_work_items(create_and_fill_by_work_items_request=create_and_fill_by_work_items_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->create_and_fill_by_work_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_and_fill_by_work_items_request** | [**CreateAndFillByWorkItemsRequest**](CreateAndFillByWorkItemsRequest.md)|  | [optional]

### Return type

[**TestRunV2GetModel**](TestRunV2GetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  - Field is required   - Test run cannot be created with deleted test points   - Test suites with IDs [ids] is archived   - Configurations with IDs [ids] is archived   - Test run cannot be created with non-automated test point   - Some work items do not exist   - Project ID is invalid |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test results is required |  -  |
**404** | Some test points, work items or configurations do not exist |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_empty**
> TestRunV2GetModel create_empty()

Create empty TestRun

 Use case   User sets test run model (listed in the request example)   User runs method execution   System creates test run   System returns test run model

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.test_run_v2_get_model import TestRunV2GetModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.test_run_v2_post_short_model import TestRunV2PostShortModel
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    test_run_v2_post_short_model = TestRunV2PostShortModel(
        project_id="3e5a61f5-bb50-44f4-8898-6dda6d40fe23",
        name="First run",
        description="description_example",
        launch_source="By user via API",
        attachments=[
            AttachmentPutModel(
                id="id_example",
            ),
        ],
        links=[
            LinkPostModel(
                title="title_example",
                url="url_example",
                description="description_example",
                type=None,
                has_info=True,
            ),
        ],
    ) # TestRunV2PostShortModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create empty TestRun
        api_response = api_instance.create_empty(test_run_v2_post_short_model=test_run_v2_post_short_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->create_empty: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_v2_post_short_model** | [**TestRunV2PostShortModel**](TestRunV2PostShortModel.md)|  | [optional]

### Return type

[**TestRunV2GetModel**](TestRunV2GetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** |  Field is required   TestRun must be automated   ProjectId is not a valid! |  -  |
**401** | TestRunTesterRequirement permission required |  -  |
**403** | Update permission for test result required |  -  |
**404** | Can&#39;t find a TestRun with id &#x3D; testRunId |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_run_by_id**
> TestRunV2GetModel get_test_run_by_id(id)

Get TestRun by Id

 Use case   User sets test run identifier   User runs method execution   System finds test run   System returns test run

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.test_run_v2_get_model import TestRunV2GetModel
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test Run internal identifier (GUID format)

    # example passing only required values which don't have defaults set
    try:
        # Get TestRun by Id
        api_response = api_instance.get_test_run_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->get_test_run_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test Run internal identifier (GUID format) |

### Return type

[**TestRunV2GetModel**](TestRunV2GetModel.md)

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
**403** | Read permission for test result required |  -  |
**404** |  TestRun with ID &#39;{id}&#39; does not exist. |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_auto_test_results_for_test_run**
> [str] set_auto_test_results_for_test_run(id)

Send test results to the test runs in the system

This method sends test results to the test management system.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.auto_test_results_for_test_run_model import AutoTestResultsForTestRunModel
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "id_example" # str | Test Run internal identifier (GUID format)
    auto_test_results_for_test_run_model = [
        AutoTestResultsForTestRunModel(
            configuration_id="configuration_id_example",
            links=[
                LinkPostModel(
                    title="title_example",
                    url="url_example",
                    description="description_example",
                    type=None,
                    has_info=True,
                ),
            ],
            failure_reason_names=[
                FailureCategoryModel("InfrastructureDefect"),
            ],
            auto_test_external_id="auto_test_external_id_example",
            outcome=None,
            message="message_example",
            traces="traces_example",
            started_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
            completed_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
            duration=0,
            attachments=[
                AttachmentPutModel(
                    id="id_example",
                ),
            ],
            parameters={
                "key": "key_example",
            },
            properties={
                "key": "key_example",
            },
            step_results=[
                AttachmentPutModelAutoTestStepResultsModel(
                    title="title_example",
                    description="description_example",
                    info="info_example",
                    started_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    completed_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    duration=0,
                    outcome=None,
                    step_results=[
                        AttachmentPutModelAutoTestStepResultsModel(),
                    ],
                    attachments=[
                        AttachmentPutModel(
                            id="id_example",
                        ),
                    ],
                    parameters={
                        "key": "key_example",
                    },
                ),
            ],
            setup_results=[
                AttachmentPutModelAutoTestStepResultsModel(
                    title="title_example",
                    description="description_example",
                    info="info_example",
                    started_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    completed_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    duration=0,
                    outcome=None,
                    step_results=[
                        AttachmentPutModelAutoTestStepResultsModel(),
                    ],
                    attachments=[
                        AttachmentPutModel(
                            id="id_example",
                        ),
                    ],
                    parameters={
                        "key": "key_example",
                    },
                ),
            ],
            teardown_results=[
                AttachmentPutModelAutoTestStepResultsModel(
                    title="title_example",
                    description="description_example",
                    info="info_example",
                    started_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    completed_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    duration=0,
                    outcome=None,
                    step_results=[
                        AttachmentPutModelAutoTestStepResultsModel(),
                    ],
                    attachments=[
                        AttachmentPutModel(
                            id="id_example",
                        ),
                    ],
                    parameters={
                        "key": "key_example",
                    },
                ),
            ],
        ),
    ] # [AutoTestResultsForTestRunModel] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Send test results to the test runs in the system
        api_response = api_instance.set_auto_test_results_for_test_run(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->set_auto_test_results_for_test_run: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send test results to the test runs in the system
        api_response = api_instance.set_auto_test_results_for_test_run(id, auto_test_results_for_test_run_model=auto_test_results_for_test_run_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->set_auto_test_results_for_test_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test Run internal identifier (GUID format) |
 **auto_test_results_for_test_run_model** | [**[AutoTestResultsForTestRunModel]**](AutoTestResultsForTestRunModel.md)|  | [optional]

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
**200** | Successful operation |  -  |
**400** |  - Field is required   - Body is invalid   - Test points are required   - Duration must be a positive number   - Outcome is not defined   - Test run is stopped |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test results is required |  -  |
**404** |  - Test run with provided ID was not found   - Test point was not found   - Autotest with provided external ID was not found |  -  |
**409** | Conflict |  -  |
**422** |  - Configuration with provided ID was not found   - Test points relevant to provided filters were not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_test_run**
> start_test_run(id)

Start TestRun

 Use case   User sets test run identifier   User runs method execution   System starts test run   System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test Run internal identifier (GUID format)

    # example passing only required values which don't have defaults set
    try:
        # Start TestRun
        api_instance.start_test_run(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->start_test_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test Run internal identifier (GUID format) |

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
**400** |  Field is required   the StateName is already InProgress   the StateName is already Stopped   the StateName is already Completed |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** |  Can&#39;t find a TestRun with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_test_run**
> stop_test_run(id)

Stop TestRun

 Use case   User sets test run identifier   User runs method execution   System stops test run   System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test Run internal identifier (GUID format)

    # example passing only required values which don't have defaults set
    try:
        # Stop TestRun
        api_instance.stop_test_run(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->stop_test_run: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test Run internal identifier (GUID format) |

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
**400** |  Field is required   the StateName is already Stopped   the StateName is already Completed |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** |  Can&#39;t find a TestRun with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_empty**
> update_empty()

Update empty TestRun

 Use case   User sets test run properties (listed in the request example)   User runs method execution   System updates test run   System returns returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.test_run_v2_put_model import TestRunV2PutModel
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
    api_instance = test_runs_api.TestRunsApi(api_client)
    test_run_v2_put_model = TestRunV2PutModel(
        id="3e5a61f5-bb50-44f4-8898-6dda6d40fe23",
        name="First run",
        description="description_example",
        launch_source="By user via API",
        attachments=[
            AttachmentPutModel(
                id="id_example",
            ),
        ],
        links=[
            LinkPutModel(
                id="3e5a61f5-bb50-44f4-8898-6dda6d40fe23",
                title="title_example",
                url="url_example",
                description="description_example",
                type=None,
                has_info=True,
            ),
        ],
    ) # TestRunV2PutModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update empty TestRun
        api_instance.update_empty(test_run_v2_put_model=test_run_v2_put_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->update_empty: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_v2_put_model** | [**TestRunV2PutModel**](TestRunV2PutModel.md)|  | [optional]

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
**400** |  Field is required   Name is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** |  Can&#39;t find a TestRun with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

