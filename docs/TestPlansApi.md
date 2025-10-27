# testit_api_client.TestPlansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_test_points_with_sections**](TestPlansApi.md#add_test_points_with_sections) | **POST** /api/v2/testPlans/{id}/test-points/withSections | Add test-points to TestPlan with sections
[**add_work_items_with_sections**](TestPlansApi.md#add_work_items_with_sections) | **POST** /api/v2/testPlans/{id}/workItems/withSections | Add WorkItems to TestPlan with Sections as TestSuites
[**api_v2_test_plans_id_analytics_get**](TestPlansApi.md#api_v2_test_plans_id_analytics_get) | **GET** /api/v2/testPlans/{id}/analytics | Get analytics by TestPlan
[**api_v2_test_plans_id_autobalance_post**](TestPlansApi.md#api_v2_test_plans_id_autobalance_post) | **POST** /api/v2/testPlans/{id}/autobalance | Distribute test points between the users
[**api_v2_test_plans_id_configurations_get**](TestPlansApi.md#api_v2_test_plans_id_configurations_get) | **GET** /api/v2/testPlans/{id}/configurations | Get TestPlan configurations
[**api_v2_test_plans_id_export_test_points_xlsx_post**](TestPlansApi.md#api_v2_test_plans_id_export_test_points_xlsx_post) | **POST** /api/v2/testPlans/{id}/export/testPoints/xlsx | Export TestPoints from TestPlan in xls format
[**api_v2_test_plans_id_export_test_result_history_xlsx_post**](TestPlansApi.md#api_v2_test_plans_id_export_test_result_history_xlsx_post) | **POST** /api/v2/testPlans/{id}/export/testResultHistory/xlsx | Export TestResults history from TestPlan in xls format
[**api_v2_test_plans_id_history_get**](TestPlansApi.md#api_v2_test_plans_id_history_get) | **GET** /api/v2/testPlans/{id}/history | Get TestPlan history
[**api_v2_test_plans_id_links_get**](TestPlansApi.md#api_v2_test_plans_id_links_get) | **GET** /api/v2/testPlans/{id}/links | Get Links of TestPlan
[**api_v2_test_plans_id_patch**](TestPlansApi.md#api_v2_test_plans_id_patch) | **PATCH** /api/v2/testPlans/{id} | Patch test plan
[**api_v2_test_plans_id_summaries_get**](TestPlansApi.md#api_v2_test_plans_id_summaries_get) | **GET** /api/v2/testPlans/{id}/summaries | Get summary by TestPlan
[**api_v2_test_plans_id_test_points_last_results_get**](TestPlansApi.md#api_v2_test_plans_id_test_points_last_results_get) | **GET** /api/v2/testPlans/{id}/testPoints/lastResults | Get TestPoints with last result from TestPlan
[**api_v2_test_plans_id_test_points_reset_post**](TestPlansApi.md#api_v2_test_plans_id_test_points_reset_post) | **POST** /api/v2/testPlans/{id}/testPoints/reset | Reset TestPoints status of TestPlan
[**api_v2_test_plans_id_test_points_tester_delete**](TestPlansApi.md#api_v2_test_plans_id_test_points_tester_delete) | **DELETE** /api/v2/testPlans/{id}/testPoints/tester | Unassign users from multiple test points
[**api_v2_test_plans_id_test_points_tester_user_id_post**](TestPlansApi.md#api_v2_test_plans_id_test_points_tester_user_id_post) | **POST** /api/v2/testPlans/{id}/testPoints/tester/{userId} | Assign user as a tester to multiple test points
[**api_v2_test_plans_id_test_runs_get**](TestPlansApi.md#api_v2_test_plans_id_test_runs_get) | **GET** /api/v2/testPlans/{id}/testRuns | Get TestRuns of TestPlan
[**api_v2_test_plans_id_test_runs_search_post**](TestPlansApi.md#api_v2_test_plans_id_test_runs_search_post) | **POST** /api/v2/testPlans/{id}/testRuns/search | Search TestRuns of TestPlan
[**api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get**](TestPlansApi.md#api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get) | **GET** /api/v2/testPlans/{id}/testRuns/testResults/lastModified/modifiedDate | Get last modification date of test plan&#39;s test results
[**api_v2_test_plans_id_unlock_request_post**](TestPlansApi.md#api_v2_test_plans_id_unlock_request_post) | **POST** /api/v2/testPlans/{id}/unlock/request | Send unlock TestPlan notification
[**api_v2_test_plans_shorts_post**](TestPlansApi.md#api_v2_test_plans_shorts_post) | **POST** /api/v2/testPlans/shorts | Get TestPlans short models by Project identifiers
[**clone**](TestPlansApi.md#clone) | **POST** /api/v2/testPlans/{id}/clone | Clone TestPlan
[**complete**](TestPlansApi.md#complete) | **POST** /api/v2/testPlans/{id}/complete | Complete TestPlan
[**create_test_plan**](TestPlansApi.md#create_test_plan) | **POST** /api/v2/testPlans | Create TestPlan
[**delete_test_plan**](TestPlansApi.md#delete_test_plan) | **DELETE** /api/v2/testPlans/{id} | Delete TestPlan
[**get_test_plan_by_id**](TestPlansApi.md#get_test_plan_by_id) | **GET** /api/v2/testPlans/{id} | Get TestPlan by Id
[**get_test_suites_by_id**](TestPlansApi.md#get_test_suites_by_id) | **GET** /api/v2/testPlans/{id}/testSuites | Get TestSuites Tree By Id
[**pause**](TestPlansApi.md#pause) | **POST** /api/v2/testPlans/{id}/pause | Pause TestPlan
[**purge_test_plan**](TestPlansApi.md#purge_test_plan) | **POST** /api/v2/testPlans/{id}/purge | Permanently delete test plan from archive
[**restore_test_plan**](TestPlansApi.md#restore_test_plan) | **POST** /api/v2/testPlans/{id}/restore | Restore TestPlan
[**start**](TestPlansApi.md#start) | **POST** /api/v2/testPlans/{id}/start | Start TestPlan
[**update_test_plan**](TestPlansApi.md#update_test_plan) | **PUT** /api/v2/testPlans | Update TestPlan


# **add_test_points_with_sections**
> add_test_points_with_sections(id)

Add test-points to TestPlan with sections

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.api_v2_projects_project_id_work_items_search_id_post_request import ApiV2ProjectsProjectIdWorkItemsSearchIdPostRequest
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    api_v2_projects_project_id_work_items_search_id_post_request = ApiV2ProjectsProjectIdWorkItemsSearchIdPostRequest(None) # ApiV2ProjectsProjectIdWorkItemsSearchIdPostRequest | Filter object to retrieve work items for test-suite's project (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add test-points to TestPlan with sections
        api_instance.add_test_points_with_sections(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->add_test_points_with_sections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add test-points to TestPlan with sections
        api_instance.add_test_points_with_sections(id, api_v2_projects_project_id_work_items_search_id_post_request=api_v2_projects_project_id_work_items_search_id_post_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->add_test_points_with_sections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **api_v2_projects_project_id_work_items_search_id_post_request** | [**ApiV2ProjectsProjectIdWorkItemsSearchIdPostRequest**](ApiV2ProjectsProjectIdWorkItemsSearchIdPostRequest.md)| Filter object to retrieve work items for test-suite&#39;s project | [optional]

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan is required |  -  |
**404** | Test suite with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Shared steps cannot be added to test suite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_work_items_with_sections**
> add_work_items_with_sections(id)

Add WorkItems to TestPlan with Sections as TestSuites

  Use case    User sets TestPlan identifier    User sets WorkItem identifiers (listed in request example)    User runs method execution    System added WorkItems and Sections to TestPlan    System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add WorkItems to TestPlan with Sections as TestSuites
        api_instance.add_work_items_with_sections(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->add_work_items_with_sections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add WorkItems to TestPlan with Sections as TestSuites
        api_instance.add_work_items_with_sections(id, request_body=request_body)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->add_work_items_with_sections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
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
**204** | Successful operation |  -  |
**400** |   TestPlan is locked    Some of configurations do not exist in the project, or they are not active |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for TestPlan required |  -  |
**404** |   Can&#39;t find a TestPlan with id    Some of workItems do not exist |  -  |
**409** | Conflict |  -  |
**422** | Can&#39;t put a SharedStep in the TestSuite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_analytics_get**
> TestPointAnalyticResult api_v2_test_plans_id_analytics_get(id)

Get analytics by TestPlan

  Use case    User sets test plan identifier    User runs method execution    System returns analytics by test plan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.test_point_analytic_result import TestPointAnalyticResult
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get analytics by TestPlan
        api_response = api_instance.api_v2_test_plans_id_analytics_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_analytics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

### Return type

[**TestPointAnalyticResult**](TestPointAnalyticResult.md)

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
**404** | Can&#39;t find a Project with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_autobalance_post**
> TestPlanWithTestSuiteTreeModel api_v2_test_plans_id_autobalance_post(id)

Distribute test points between the users

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_plan_with_test_suite_tree_model import TestPlanWithTestSuiteTreeModel
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "id_example" # str | Test plan unique or global ID
    testers = [
        "testers_example",
    ] # [str] | Specifies a project user IDs to distribute (optional)

    # example passing only required values which don't have defaults set
    try:
        # Distribute test points between the users
        api_response = api_instance.api_v2_test_plans_id_autobalance_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_autobalance_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Distribute test points between the users
        api_response = api_instance.api_v2_test_plans_id_autobalance_post(id, testers=testers)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_autobalance_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan unique or global ID |
 **testers** | **[str]**| Specifies a project user IDs to distribute | [optional]

### Return type

[**TestPlanWithTestSuiteTreeModel**](TestPlanWithTestSuiteTreeModel.md)

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
**403** | Update permission for test plan is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_configurations_get**
> [ConfigurationModel] api_v2_test_plans_id_configurations_get(id)

Get TestPlan configurations

  Use case    User sets test plan identifier    User runs method execution    System return test plan configurations

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.configuration_model import ConfigurationModel
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get TestPlan configurations
        api_response = api_instance.api_v2_test_plans_id_configurations_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_configurations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

### Return type

[**[ConfigurationModel]**](ConfigurationModel.md)

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
**403** | Read permission for test plan required |  -  |
**404** | TestPlan not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_export_test_points_xlsx_post**
> api_v2_test_plans_id_export_test_points_xlsx_post(id)

Export TestPoints from TestPlan in xls format

  Use case    User sets test plan identifier    User sets filter model (listed in request example)    User runs method execution    System return export xlsx file

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_test_plans_id_export_test_points_xlsx_post_request import ApiV2TestPlansIdExportTestPointsXlsxPostRequest
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    time_zone_offset_in_minutes = 1 # int |  (optional)
    api_v2_test_plans_id_export_test_points_xlsx_post_request = ApiV2TestPlansIdExportTestPointsXlsxPostRequest(None) # ApiV2TestPlansIdExportTestPointsXlsxPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export TestPoints from TestPlan in xls format
        api_instance.api_v2_test_plans_id_export_test_points_xlsx_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_export_test_points_xlsx_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export TestPoints from TestPlan in xls format
        api_instance.api_v2_test_plans_id_export_test_points_xlsx_post(id, time_zone_offset_in_minutes=time_zone_offset_in_minutes, api_v2_test_plans_id_export_test_points_xlsx_post_request=api_v2_test_plans_id_export_test_points_xlsx_post_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_export_test_points_xlsx_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **time_zone_offset_in_minutes** | **int**|  | [optional]
 **api_v2_test_plans_id_export_test_points_xlsx_post_request** | [**ApiV2TestPlansIdExportTestPointsXlsxPostRequest**](ApiV2TestPlansIdExportTestPointsXlsxPostRequest.md)|  | [optional]

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
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test plan required |  -  |
**404** | TestPlan not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_export_test_result_history_xlsx_post**
> api_v2_test_plans_id_export_test_result_history_xlsx_post(id)

Export TestResults history from TestPlan in xls format

  Use case    User sets test plan identifier    User sets filter model (listed in request example)    User runs method execution    System return export xlsx file

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    must_return_only_last_test_result = True # bool |  (optional)
    include_steps = True # bool |  (optional)
    include_deleted_test_suites = True # bool |  (optional)
    time_zone_offset_in_minutes = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export TestResults history from TestPlan in xls format
        api_instance.api_v2_test_plans_id_export_test_result_history_xlsx_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_export_test_result_history_xlsx_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export TestResults history from TestPlan in xls format
        api_instance.api_v2_test_plans_id_export_test_result_history_xlsx_post(id, must_return_only_last_test_result=must_return_only_last_test_result, include_steps=include_steps, include_deleted_test_suites=include_deleted_test_suites, time_zone_offset_in_minutes=time_zone_offset_in_minutes)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_export_test_result_history_xlsx_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **must_return_only_last_test_result** | **bool**|  | [optional]
 **include_steps** | **bool**|  | [optional]
 **include_deleted_test_suites** | **bool**|  | [optional]
 **time_zone_offset_in_minutes** | **int**|  | [optional]

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
**403** | Read permission for test plan required |  -  |
**404** | TestPlan not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_history_get**
> [TestPlanChangeModel] api_v2_test_plans_id_history_get(id)

Get TestPlan history

  Use case    User sets test plan identifier    User runs method execution    System return test plan history

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.test_plan_change_model import TestPlanChangeModel
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TestPlan history
        api_response = api_instance.api_v2_test_plans_id_history_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TestPlan history
        api_response = api_instance.api_v2_test_plans_id_history_get(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_history_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestPlanChangeModel]**](TestPlanChangeModel.md)

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
**403** | Read permission for test plan required |  -  |
**404** | TestPlan not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_links_get**
> [TestPlanLink] api_v2_test_plans_id_links_get(id)

Get Links of TestPlan

  Use case    User sets test plan identifier    User sets pagination filter (listed in request example)    User runs method execution    System returns links of TestPlan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.test_plan_link import TestPlanLink
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    skip = 1 # int |  (optional)
    take = 1 # int |  (optional)
    order_by = "orderBy_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Links of TestPlan
        api_response = api_instance.api_v2_test_plans_id_links_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_links_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Links of TestPlan
        api_response = api_instance.api_v2_test_plans_id_links_get(id, skip=skip, take=take, order_by=order_by)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_links_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **skip** | **int**|  | [optional]
 **take** | **int**|  | [optional]
 **order_by** | **str**|  | [optional]

### Return type

[**[TestPlanLink]**](TestPlanLink.md)

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
**403** | Read permission for test plan is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_patch**
> api_v2_test_plans_id_patch(id)

Patch test plan

See <a href=\"https://www.rfc-editor.org/rfc/rfc6902\" target=\"_blank\">RFC 6902: JavaScript Object Notation (JSON) Patch</a> for details

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "id_example" # str | Unique ID of the test plan
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
        # Patch test plan
        api_instance.api_v2_test_plans_id_patch(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch test plan
        api_instance.api_v2_test_plans_id_patch(id, operation=operation)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the test plan |
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_summaries_get**
> TestPlanSummaryModel api_v2_test_plans_id_summaries_get(id)

Get summary by TestPlan

  Use case    User sets test plan identifier    User runs method execution    System returns summary by test plan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.test_plan_summary_model import TestPlanSummaryModel
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get summary by TestPlan
        api_response = api_instance.api_v2_test_plans_id_summaries_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_summaries_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

### Return type

[**TestPlanSummaryModel**](TestPlanSummaryModel.md)

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
**404** | Can&#39;t find a Test Plan with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_points_last_results_get**
> [TestPointWithLastResultResponseModel] api_v2_test_plans_id_test_points_last_results_get(id)

Get TestPoints with last result from TestPlan

  Use case    User sets test plan identifier    User sets filter (listed in request example)    User runs method execution    System return test points with last result from test plan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_point_with_last_result_response_model import TestPointWithLastResultResponseModel
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    tester_id = "testerId_example" # str |  (optional)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TestPoints with last result from TestPlan
        api_response = api_instance.api_v2_test_plans_id_test_points_last_results_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_points_last_results_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TestPoints with last result from TestPlan
        api_response = api_instance.api_v2_test_plans_id_test_points_last_results_get(id, tester_id=tester_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_points_last_results_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **tester_id** | **str**|  | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestPointWithLastResultResponseModel]**](TestPointWithLastResultResponseModel.md)

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
**403** | Read permission for test plan required |  -  |
**404** | TestPlan not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_points_reset_post**
> api_v2_test_plans_id_test_points_reset_post(id)

Reset TestPoints status of TestPlan

  Use case    User sets test plan identifier    User sets test points identifiers    User runs method execution    System reset test points statuses of test plan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Reset TestPoints status of TestPlan
        api_instance.api_v2_test_plans_id_test_points_reset_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_points_reset_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Reset TestPoints status of TestPlan
        api_instance.api_v2_test_plans_id_test_points_reset_post(id, request_body=request_body)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_points_reset_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
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
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_points_tester_delete**
> [str] api_v2_test_plans_id_test_points_tester_delete(id)

Unassign users from multiple test points

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.api_v2_test_plans_id_test_points_tester_user_id_post_request import ApiV2TestPlansIdTestPointsTesterUserIdPostRequest
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "id_example" # str | Unique or global ID of the test plan
    api_v2_test_plans_id_test_points_tester_user_id_post_request = ApiV2TestPlansIdTestPointsTesterUserIdPostRequest(None) # ApiV2TestPlansIdTestPointsTesterUserIdPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unassign users from multiple test points
        api_response = api_instance.api_v2_test_plans_id_test_points_tester_delete(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_points_tester_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unassign users from multiple test points
        api_response = api_instance.api_v2_test_plans_id_test_points_tester_delete(id, api_v2_test_plans_id_test_points_tester_user_id_post_request=api_v2_test_plans_id_test_points_tester_user_id_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_points_tester_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the test plan |
 **api_v2_test_plans_id_test_points_tester_user_id_post_request** | [**ApiV2TestPlansIdTestPointsTesterUserIdPostRequest**](ApiV2TestPlansIdTestPointsTesterUserIdPostRequest.md)|  | [optional]

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plans is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_points_tester_user_id_post**
> [str] api_v2_test_plans_id_test_points_tester_user_id_post(id, user_id)

Assign user as a tester to multiple test points

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.api_v2_test_plans_id_test_points_tester_user_id_post_request import ApiV2TestPlansIdTestPointsTesterUserIdPostRequest
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "id_example" # str | Unique or global ID of the test plan
    user_id = "userId_example" # str | Unique ID of the user
    api_v2_test_plans_id_test_points_tester_user_id_post_request = ApiV2TestPlansIdTestPointsTesterUserIdPostRequest(None) # ApiV2TestPlansIdTestPointsTesterUserIdPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Assign user as a tester to multiple test points
        api_response = api_instance.api_v2_test_plans_id_test_points_tester_user_id_post(id, user_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_points_tester_user_id_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Assign user as a tester to multiple test points
        api_response = api_instance.api_v2_test_plans_id_test_points_tester_user_id_post(id, user_id, api_v2_test_plans_id_test_points_tester_user_id_post_request=api_v2_test_plans_id_test_points_tester_user_id_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_points_tester_user_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the test plan |
 **user_id** | **str**| Unique ID of the user |
 **api_v2_test_plans_id_test_points_tester_user_id_post_request** | [**ApiV2TestPlansIdTestPointsTesterUserIdPostRequest**](ApiV2TestPlansIdTestPointsTesterUserIdPostRequest.md)|  | [optional]

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plans is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_runs_get**
> [TestRunApiResult] api_v2_test_plans_id_test_runs_get(id)

Get TestRuns of TestPlan

  Use case    User sets test plan identifier    User sets TestRun status filter (listed in request example)    User runs method execution    System returns TestRuns for TestPlan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_run_api_result import TestRunApiResult
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    not_started = True # bool |  (optional)
    in_progress = True # bool |  (optional)
    stopped = True # bool |  (optional)
    completed = True # bool |  (optional)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TestRuns of TestPlan
        api_response = api_instance.api_v2_test_plans_id_test_runs_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_runs_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TestRuns of TestPlan
        api_response = api_instance.api_v2_test_plans_id_test_runs_get(id, not_started=not_started, in_progress=in_progress, stopped=stopped, completed=completed, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_runs_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **not_started** | **bool**|  | [optional]
 **in_progress** | **bool**|  | [optional]
 **stopped** | **bool**|  | [optional]
 **completed** | **bool**|  | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestRunApiResult]**](TestRunApiResult.md)

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
**403** | Read permission for test plan is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_runs_search_post**
> [TestRunApiResult] api_v2_test_plans_id_test_runs_search_post(id)

Search TestRuns of TestPlan

  Use case    User sets test plan identifier    User sets TestRuns filter (listed in request example)    User runs method execution    System returns TestRuns for TestPlan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_test_plans_id_test_runs_search_post_request import ApiV2TestPlansIdTestRunsSearchPostRequest
from testit_api_client.model.test_run_api_result import TestRunApiResult
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    api_v2_test_plans_id_test_runs_search_post_request = ApiV2TestPlansIdTestRunsSearchPostRequest(None) # ApiV2TestPlansIdTestRunsSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search TestRuns of TestPlan
        api_response = api_instance.api_v2_test_plans_id_test_runs_search_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_runs_search_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search TestRuns of TestPlan
        api_response = api_instance.api_v2_test_plans_id_test_runs_search_post(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, api_v2_test_plans_id_test_runs_search_post_request=api_v2_test_plans_id_test_runs_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_runs_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **api_v2_test_plans_id_test_runs_search_post_request** | [**ApiV2TestPlansIdTestRunsSearchPostRequest**](ApiV2TestPlansIdTestRunsSearchPostRequest.md)|  | [optional]

### Return type

[**[TestRunApiResult]**](TestRunApiResult.md)

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
**403** | Read permission for test plan is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get**
> api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get(id)

Get last modification date of test plan's test results

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "id_example" # str | Internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get last modification date of test plan's test results
        api_instance.api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Internal (UUID) or global (integer) identifier |

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_unlock_request_post**
> api_v2_test_plans_id_unlock_request_post(id)

Send unlock TestPlan notification

  Use case    User sets test plan identifier    User runs method execution    System send unlock test plan notification

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Send unlock TestPlan notification
        api_instance.api_v2_test_plans_id_unlock_request_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_unlock_request_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

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
**403** | Read permission for test plan required |  -  |
**404** | TestPlan not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_shorts_post**
> [TestPlanShortModel] api_v2_test_plans_shorts_post()

Get TestPlans short models by Project identifiers

  Use case    User sets projects identifiers    User runs method execution    System return test plans short models (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.test_plan_short_model import TestPlanShortModel
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    is_deleted = True # bool |  (optional)
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TestPlans short models by Project identifiers
        api_response = api_instance.api_v2_test_plans_shorts_post(is_deleted=is_deleted, request_body=request_body)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_shorts_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_deleted** | **bool**|  | [optional]
 **request_body** | **[str]**|  | [optional]

### Return type

[**[TestPlanShortModel]**](TestPlanShortModel.md)

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
**403** | Read permission for project required |  -  |
**404** | Project not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone**
> TestPlanModel clone(id)

Clone TestPlan

  Use case    User sets test plan identifier    User runs method execution    System clones test plan    System returns test plan (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_plan_model import TestPlanModel
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Clone TestPlan
        api_response = api_instance.clone(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->clone: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

### Return type

[**TestPlanModel**](TestPlanModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete**
> complete(id)

Complete TestPlan

  Use case    User sets test plan identifier    User runs method execution    System completes the test plan and updates test plan status    System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Complete TestPlan
        api_instance.complete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->complete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

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
**400** |   Execute status from New to Completed forbidden    Execute status from Completed to Completed forbidden |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_plan**
> TestPlanModel create_test_plan()

Create TestPlan

  Use case    User sets test plan properties (listed in request example)    User runs method execution    System creates test plan    System returns test plan (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_plan_model import TestPlanModel
from testit_api_client.model.create_test_plan_request import CreateTestPlanRequest
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    create_test_plan_request = CreateTestPlanRequest(None) # CreateTestPlanRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create TestPlan
        api_response = api_instance.create_test_plan(create_test_plan_request=create_test_plan_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->create_test_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_test_plan_request** | [**CreateTestPlanRequest**](CreateTestPlanRequest.md)|  | [optional]

### Return type

[**TestPlanModel**](TestPlanModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** |   Field is required    Tags must be no more than 10! |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**404** | Not Found |  -  |
**409** | TestPlan with the same name already exists! |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_plan**
> delete_test_plan(id)

Delete TestPlan

  Use case    User sets test plan identifier    User runs method execution    System delete test plan    System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete TestPlan
        api_instance.delete_test_plan(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->delete_test_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

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
**403** | Delete permission for test plan required |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_plan_by_id**
> TestPlanModel get_test_plan_by_id(id)

Get TestPlan by Id

  Use case    User sets test plan identifier    User runs method execution    System search  test plan by the identifier    System returns test plan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_plan_model import TestPlanModel
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get TestPlan by Id
        api_response = api_instance.get_test_plan_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->get_test_plan_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

### Return type

[**TestPlanModel**](TestPlanModel.md)

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
**403** | Read permission for test plan required |  -  |
**404** | Can&#39;t find a Project with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_suites_by_id**
> [TestSuiteHierarchyApiResult] get_test_suites_by_id(id)

Get TestSuites Tree By Id

  Use case    User sets test plan identifier    User runs method execution    System finds test suites related to the test plan    System returns test suites as a tree model (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_suite_hierarchy_api_result import TestSuiteHierarchyApiResult
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get TestSuites Tree By Id
        api_response = api_instance.get_test_suites_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->get_test_suites_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

### Return type

[**[TestSuiteHierarchyApiResult]**](TestSuiteHierarchyApiResult.md)

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
**403** | Read permission for test plan required |  -  |
**404** | Can&#39;t find a TestRun with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause**
> pause(id)

Pause TestPlan

  Use case    User sets test plan identifier    User runs method execution    System pauses the test plan and updates test plan status    System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Pause TestPlan
        api_instance.pause(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->pause: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

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
**400** |   Execute status from New to Paused forbidden    Execute status from Paused to Paused forbidden    Execute status from Completed to Paused forbidden |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purge_test_plan**
> purge_test_plan(id)

Permanently delete test plan from archive

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "id_example" # str | Unique or global ID of the test plan

    # example passing only required values which don't have defaults set
    try:
        # Permanently delete test plan from archive
        api_instance.purge_test_plan(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->purge_test_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the test plan |

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
**403** | Full access permission for the archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_test_plan**
> restore_test_plan(id)

Restore TestPlan

  Use case    User sets test plan identifier    User runs method execution    System restores test plan    System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Restore TestPlan
        api_instance.restore_test_plan(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->restore_test_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

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
**403** | Update permission for the archive is required |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(id)

Start TestPlan

  Use case    User sets test plan identifier    User runs method execution    System starts the test plan and updates test plan status    System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Start TestPlan
        api_instance.start(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

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
**403** | Update permission for test plan required |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_plan**
> update_test_plan()

Update TestPlan

  Use case    User sets test plan properties(listed in request example)    User runs method execution    System updates test plan    System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.update_test_plan_request import UpdateTestPlanRequest
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    update_test_plan_request = UpdateTestPlanRequest(None) # UpdateTestPlanRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update TestPlan
        api_instance.update_test_plan(update_test_plan_request=update_test_plan_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->update_test_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_test_plan_request** | [**UpdateTestPlanRequest**](UpdateTestPlanRequest.md)|  | [optional]

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
**400** |   Field is required    Tags must be no more than 10!    StartDate can&#39;t be more than EndDate! |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |
**409** | TestPlan with the same name already exists! |  -  |
**422** | Can&#39;t change ProjectId |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

