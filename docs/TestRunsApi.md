# testit_api_client.TestRunsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_test_runs_id_test_points_results_get**](TestRunsApi.md#api_v2_test_runs_id_test_points_results_get) | **GET** /api/v2/testRuns/{id}/testPoints/results | 
[**api_v2_test_runs_id_test_results_last_modified_modification_date_get**](TestRunsApi.md#api_v2_test_runs_id_test_results_last_modified_modification_date_get) | **GET** /api/v2/testRuns/{id}/testResults/lastModified/modificationDate | 
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


# **api_v2_test_runs_id_test_points_results_get**
> [TestPointResultModel] api_v2_test_runs_id_test_points_results_get(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
from testit_api_client.model.test_point_result_model import TestPointResultModel
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
        api_response = api_instance.api_v2_test_runs_id_test_points_results_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_test_points_results_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_runs_id_test_results_last_modified_modification_date_get**
> datetime api_v2_test_runs_id_test_results_last_modified_modification_date_get(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_runs_api
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
        api_response = api_instance.api_v2_test_runs_id_test_results_last_modified_modification_date_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->api_v2_test_runs_id_test_results_last_modified_modification_date_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestRun with id! |  -  |
**204** | Successful operation |  -  |
**400** | &lt;br&gt;Field is required  &lt;br&gt;the StateName is already Stopped  &lt;br&gt;the StateName is already Completed |  -  |

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
from testit_api_client.model.test_run_fill_by_auto_tests_post_model import TestRunFillByAutoTestsPostModel
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
    test_run_fill_by_auto_tests_post_model = TestRunFillByAutoTestsPostModel(
        project_id="project_id_example",
        name="name_example",
        configuration_ids=[
            "configuration_ids_example",
        ],
        auto_test_external_ids=[
            "auto_test_external_ids_example",
        ],
        description="description_example",
        launch_source="launch_source_example",
    ) # TestRunFillByAutoTestsPostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create test runs based on autotests and configurations
        api_response = api_instance.create_and_fill_by_auto_tests(test_run_fill_by_auto_tests_post_model=test_run_fill_by_auto_tests_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->create_and_fill_by_auto_tests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_fill_by_auto_tests_post_model** | [**TestRunFillByAutoTestsPostModel**](TestRunFillByAutoTestsPostModel.md)|  | [optional]

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
**201** | Success |  -  |
**404** | Some autotests do not exist |  -  |
**400** | &lt;br&gt;- Field is required  &lt;br&gt;- Configuration does not exist in the project  &lt;br&gt;- Autotest does not exist in the project  &lt;br&gt;- Test run must be automated  &lt;br&gt;- Project ID is invalid  &lt;br&gt;- Autotest external IDs are required  &lt;br&gt;- Configuration IDs are required |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test results is required |  -  |

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
from testit_api_client.model.test_run_fill_by_configurations_post_model import TestRunFillByConfigurationsPostModel
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
    test_run_fill_by_configurations_post_model = TestRunFillByConfigurationsPostModel(
        test_point_selectors=[
            TestPointSelector(
                configuration_id="configuration_id_example",
                workitem_ids=[
                    "workitem_ids_example",
                ],
            ),
        ],
        project_id="project_id_example",
        test_plan_id="test_plan_id_example",
        name="name_example",
        description="description_example",
        launch_source="launch_source_example",
    ) # TestRunFillByConfigurationsPostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create test runs picking the needed test points
        api_response = api_instance.create_and_fill_by_configurations(test_run_fill_by_configurations_post_model=test_run_fill_by_configurations_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->create_and_fill_by_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_fill_by_configurations_post_model** | [**TestRunFillByConfigurationsPostModel**](TestRunFillByConfigurationsPostModel.md)|  | [optional]

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
**201** | Success |  -  |
**403** | Update permission for test results is required |  -  |
**400** | &lt;br&gt;- Field is required  &lt;br&gt;- Test run cannot be created with deleted test points  &lt;br&gt;- Test run cannot be created in deleted test suite  &lt;br&gt;- Test run cannot be created with non-automated test point  &lt;br&gt;- Test run must be automated  &lt;br&gt;- Some work items do not exist  &lt;br&gt;- Project ID is invalid  &lt;br&gt;- Test point selectors are required  &lt;br&gt;- Some work item IDs are invalid  &lt;br&gt;- Some configuration IDs are invalid |  -  |
**401** | Unauthorized |  -  |
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
from testit_api_client.model.test_run_fill_by_work_items_post_model import TestRunFillByWorkItemsPostModel
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
    test_run_fill_by_work_items_post_model = TestRunFillByWorkItemsPostModel(
        configuration_ids=[
            "configuration_ids_example",
        ],
        workitem_ids=[
            "workitem_ids_example",
        ],
        project_id="project_id_example",
        test_plan_id="test_plan_id_example",
        name="name_example",
        description="description_example",
        launch_source="launch_source_example",
    ) # TestRunFillByWorkItemsPostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create test run based on configurations and work items
        api_response = api_instance.create_and_fill_by_work_items(test_run_fill_by_work_items_post_model=test_run_fill_by_work_items_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestRunsApi->create_and_fill_by_work_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_run_fill_by_work_items_post_model** | [**TestRunFillByWorkItemsPostModel**](TestRunFillByWorkItemsPostModel.md)|  | [optional]

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
**403** | Update permission for test results is required |  -  |
**401** | Unauthorized |  -  |
**404** | Some test points, work items or configurations do not exist |  -  |
**201** | Success |  -  |
**400** | &lt;br&gt;- Field is required  &lt;br&gt;- Test run cannot be created with deleted test points  &lt;br&gt;- Test run cannot be created in deleted test suite  &lt;br&gt;- Test run cannot be created with non-automated test point  &lt;br&gt;- Some work items do not exist  &lt;br&gt;- Project ID is invalid |  -  |

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
        project_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        name="First run",
        description="description_example",
        launch_source="By user via API",
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
**401** | TestRunTesterRequirement permission required |  -  |
**201** | Successful operation |  -  |
**400** | &lt;br&gt;Field is required  &lt;br&gt;TestRun must be automated  &lt;br&gt;ProjectId is not a valid! |  -  |
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
**403** | Read permission for test result required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestRun with id! |  -  |
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |

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
                    type=LinkType("Related"),
                    has_info=True,
                ),
            ],
            failure_reason_names=[
                "failure_reason_names_example",
            ],
            auto_test_external_id="auto_test_external_id_example",
            outcome="outcome_example",
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
                    outcome="outcome_example",
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
                    outcome="outcome_example",
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
                    outcome="outcome_example",
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
**401** | Unauthorized |  -  |
**403** | Update permission for test results is required |  -  |
**404** | &lt;br&gt;- Test run with provided ID was not found  &lt;br&gt;- Test point was not found  &lt;br&gt;- Autotest with provided external ID was not found |  -  |
**422** | &lt;br&gt;- Configuration with provided ID was not found  &lt;br&gt;- Test points relevant to provided filters were not found |  -  |
**400** | &lt;br&gt;- Field is required  &lt;br&gt;- Body is invalid  &lt;br&gt;- Test points are required  &lt;br&gt;- Duration must be a positive number  &lt;br&gt;- Outcome is not defined  &lt;br&gt;- Test run is stopped |  -  |

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
**403** | Update permission for test result required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestRun with id! |  -  |
**400** | &lt;br&gt;Field is required  &lt;br&gt;the StateName is already InProgress  &lt;br&gt;the StateName is already Stopped  &lt;br&gt;the StateName is already Completed |  -  |
**401** | Unauthorized |  -  |

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
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestRun with id! |  -  |
**400** | &lt;br&gt;Field is required  &lt;br&gt;the StateName is already Stopped  &lt;br&gt;the StateName is already Completed |  -  |

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
        id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        name="First run",
        description="description_example",
        launch_source="By user via API",
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
**401** | Unauthorized |  -  |
**400** | &lt;br&gt;Field is required  &lt;br&gt;Name is not valid |  -  |
**403** | Update permission for test result required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestRun with id! |  -  |
**204** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

