# testit_api_client.TestRunsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_test_runs_id_statistics_filter_post**](TestRunsApi.md#api_v2_test_runs_id_statistics_filter_post) | **POST** /api/v2/testRuns/{id}/statistics/filter | Search for the test run test results and build statistics
[**api_v2_test_runs_id_test_points_results_get**](TestRunsApi.md#api_v2_test_runs_id_test_points_results_get) | **GET** /api/v2/testRuns/{id}/testPoints/results | Get test results from the test run grouped by test points
[**api_v2_test_runs_id_test_results_bulk_put**](TestRunsApi.md#api_v2_test_runs_id_test_results_bulk_put) | **PUT** /api/v2/testRuns/{id}/testResults/bulk | Partial edit of multiple test results in the test run
[**api_v2_test_runs_id_test_results_last_modified_modification_date_get**](TestRunsApi.md#api_v2_test_runs_id_test_results_last_modified_modification_date_get) | **GET** /api/v2/testRuns/{id}/testResults/lastModified/modificationDate | Get modification date of last test result of the test run
[**api_v2_test_runs_search_post**](TestRunsApi.md#api_v2_test_runs_search_post) | **POST** /api/v2/testRuns/search | Search for test runs
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
**200** | Success |  -  |
**403** | Read permission for test runs is required |  -  |

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
**200** | Success |  -  |
**403** | Read permission for test runs is required |  -  |

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
**403** | Update permission for test runs is required |  -  |

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
**200** | Success |  -  |
**403** | Read permission for test runs is required |  -  |

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
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**403** | Read permission for autotests library is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_test_run**
> complete_test_run(id)

Complete TestRun

<br>Use case  <br>User sets test run identifier  <br>User runs method execution  <br>System completes test run  <br>System returns no content response

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
**400** | &lt;br&gt;Field is required  &lt;br&gt;the StateName is already Stopped  &lt;br&gt;the StateName is already Completed |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestRun with id! |  -  |

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
**400** | &lt;br&gt;- Field is required  &lt;br&gt;- Configuration does not exist in the project  &lt;br&gt;- Autotest does not exist in the project  &lt;br&gt;- Test run must be automated  &lt;br&gt;- Project ID is invalid  &lt;br&gt;- Autotest external IDs are required  &lt;br&gt;- Configuration IDs are required |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test results is required |  -  |
**404** | Some autotests do not exist |  -  |

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
**400** | &lt;br&gt;- Field is required  &lt;br&gt;- Test run cannot be created with deleted test points  &lt;br&gt;- Test run cannot be created in deleted test suite  &lt;br&gt;- Test run cannot be created with non-automated test point  &lt;br&gt;- Test run must be automated  &lt;br&gt;- Some work items do not exist  &lt;br&gt;- Project ID is invalid  &lt;br&gt;- Test point selectors are required  &lt;br&gt;- Some work item IDs are invalid  &lt;br&gt;- Some configuration IDs are invalid |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test results is required |  -  |
**404** | Some test points do not exists |  -  |

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
**400** | &lt;br&gt;- Field is required  &lt;br&gt;- Test run cannot be created with deleted test points  &lt;br&gt;- Test run cannot be created in deleted test suite  &lt;br&gt;- Test run cannot be created with non-automated test point  &lt;br&gt;- Some work items do not exist  &lt;br&gt;- Project ID is invalid |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test results is required |  -  |
**404** | Some test points, work items or configurations do not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_empty**
> TestRunV2GetModel create_empty()

Create empty TestRun

<br>Use case  <br>User sets test run model (listed in the request example)  <br>User runs method execution  <br>System creates test run  <br>System returns test run model

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.test_run_v2_get_model import TestRunV2GetModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.create_empty_request import CreateEmptyRequest
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
    create_empty_request = CreateEmptyRequest(None) # CreateEmptyRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create empty TestRun
        api_response = api_instance.create_empty(create_empty_request=create_empty_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->create_empty: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_empty_request** | [**CreateEmptyRequest**](CreateEmptyRequest.md)|  | [optional]

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
**400** | &lt;br&gt;Field is required  &lt;br&gt;TestRun must be automated  &lt;br&gt;ProjectId is not a valid! |  -  |
**401** | TestRunTesterRequirement permission required |  -  |
**403** | Update permission for test result required |  -  |
**404** | Can&#39;t find a TestRun with id &#x3D; testRunId |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_run_by_id**
> TestRunV2GetModel get_test_run_by_id(id)

Get TestRun by Id

<br>Use case  <br>User sets test run identifier  <br>User runs method execution  <br>System finds test run  <br>System returns test run

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
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
**401** | Unauthorized |  -  |
**403** | Read permission for test result required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestRun with id! |  -  |

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
**400** | &lt;br&gt;- Field is required  &lt;br&gt;- Body is invalid  &lt;br&gt;- Test points are required  &lt;br&gt;- Duration must be a positive number  &lt;br&gt;- Outcome is not defined  &lt;br&gt;- Test run is stopped |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test results is required |  -  |
**404** | &lt;br&gt;- Test run with provided ID was not found  &lt;br&gt;- Test point was not found  &lt;br&gt;- Autotest with provided external ID was not found |  -  |
**422** | &lt;br&gt;- Configuration with provided ID was not found  &lt;br&gt;- Test points relevant to provided filters were not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_test_run**
> start_test_run(id)

Start TestRun

<br>Use case  <br>User sets test run identifier  <br>User runs method execution  <br>System starts test run  <br>System returns no content response

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
**400** | &lt;br&gt;Field is required  &lt;br&gt;the StateName is already InProgress  &lt;br&gt;the StateName is already Stopped  &lt;br&gt;the StateName is already Completed |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestRun with id! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_test_run**
> stop_test_run(id)

Stop TestRun

<br>Use case  <br>User sets test run identifier  <br>User runs method execution  <br>System stops test run  <br>System returns no content response

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
**400** | &lt;br&gt;Field is required  &lt;br&gt;the StateName is already Stopped  &lt;br&gt;the StateName is already Completed |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestRun with id! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_empty**
> update_empty()

Update empty TestRun

<br>Use case  <br>User sets test run properties (listed in the request example)  <br>User runs method execution  <br>System updates test run  <br>System returns returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.update_empty_request import UpdateEmptyRequest
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
    update_empty_request = UpdateEmptyRequest(None) # UpdateEmptyRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update empty TestRun
        api_instance.update_empty(update_empty_request=update_empty_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->update_empty: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_empty_request** | [**UpdateEmptyRequest**](UpdateEmptyRequest.md)|  | [optional]

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
**400** | &lt;br&gt;Field is required  &lt;br&gt;Name is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestRun with id! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

