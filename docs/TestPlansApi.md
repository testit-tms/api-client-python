# testit_api_client.TestPlansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_test_points_with_sections**](TestPlansApi.md#add_test_points_with_sections) | **POST** /api/v2/testPlans/{id}/test-points/withSections | Add test-points to test suite with sections
[**add_work_items_with_sections**](TestPlansApi.md#add_work_items_with_sections) | **POST** /api/v2/testPlans/{id}/workItems/withSections | Add WorkItems to TestPlan with Sections as TestSuites
[**api_v2_test_plans_id_analytics_get**](TestPlansApi.md#api_v2_test_plans_id_analytics_get) | **GET** /api/v2/testPlans/{id}/analytics | Get analytics by TestPlan
[**api_v2_test_plans_id_autobalance_post**](TestPlansApi.md#api_v2_test_plans_id_autobalance_post) | **POST** /api/v2/testPlans/{id}/autobalance | Auto-balance for TestPlan with testers
[**api_v2_test_plans_id_configurations_get**](TestPlansApi.md#api_v2_test_plans_id_configurations_get) | **GET** /api/v2/testPlans/{id}/configurations | Get TestPlan configurations
[**api_v2_test_plans_id_export_test_points_xlsx_post**](TestPlansApi.md#api_v2_test_plans_id_export_test_points_xlsx_post) | **POST** /api/v2/testPlans/{id}/export/testPoints/xlsx | Export TestPoints from TestPlan in xls format
[**api_v2_test_plans_id_export_test_result_history_xlsx_post**](TestPlansApi.md#api_v2_test_plans_id_export_test_result_history_xlsx_post) | **POST** /api/v2/testPlans/{id}/export/testResultHistory/xlsx | Export TestResults history from TestPlan in xls format
[**api_v2_test_plans_id_history_get**](TestPlansApi.md#api_v2_test_plans_id_history_get) | **GET** /api/v2/testPlans/{id}/history | Get TestPlan history
[**api_v2_test_plans_id_links_get**](TestPlansApi.md#api_v2_test_plans_id_links_get) | **GET** /api/v2/testPlans/{id}/links | Get Links of TestPlan
[**api_v2_test_plans_id_test_points_last_results_get**](TestPlansApi.md#api_v2_test_plans_id_test_points_last_results_get) | **GET** /api/v2/testPlans/{id}/testPoints/lastResults | Get TestPoints with last result from TestPlan
[**api_v2_test_plans_id_test_points_reset_post**](TestPlansApi.md#api_v2_test_plans_id_test_points_reset_post) | **POST** /api/v2/testPlans/{id}/testPoints/reset | Reset TestPoints status of TestPlan
[**api_v2_test_plans_id_test_runs_get**](TestPlansApi.md#api_v2_test_plans_id_test_runs_get) | **GET** /api/v2/testPlans/{id}/testRuns | Get TestRuns of TestPlan
[**api_v2_test_plans_id_test_runs_search_post**](TestPlansApi.md#api_v2_test_plans_id_test_runs_search_post) | **POST** /api/v2/testPlans/{id}/testRuns/search | Search TestRuns of TestPlan
[**api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get**](TestPlansApi.md#api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get) | **GET** /api/v2/testPlans/{id}/testRuns/testResults/lastModified/modifiedDate | Get max modified date in TestRun for TestPlan
[**api_v2_test_plans_id_unlock_request_post**](TestPlansApi.md#api_v2_test_plans_id_unlock_request_post) | **POST** /api/v2/testPlans/{id}/unlock/request | Send unlock TestPlan notification
[**api_v2_test_plans_shorts_post**](TestPlansApi.md#api_v2_test_plans_shorts_post) | **POST** /api/v2/testPlans/shorts | Get TestPlans short models by Project identifiers
[**clone**](TestPlansApi.md#clone) | **POST** /api/v2/testPlans/{id}/clone | Clone TestPlan
[**complete**](TestPlansApi.md#complete) | **POST** /api/v2/testPlans/{id}/complete | Complete TestPlan
[**create_test_plan**](TestPlansApi.md#create_test_plan) | **POST** /api/v2/testPlans | Create TestPlan
[**delete_test_plan**](TestPlansApi.md#delete_test_plan) | **DELETE** /api/v2/testPlans/{id} | Delete TestPlan
[**get_test_plan_by_id**](TestPlansApi.md#get_test_plan_by_id) | **GET** /api/v2/testPlans/{id} | Get TestPlan by Id
[**get_test_suites_by_id**](TestPlansApi.md#get_test_suites_by_id) | **GET** /api/v2/testPlans/{id}/testSuites | Get TestSuites Tree By Id
[**pause**](TestPlansApi.md#pause) | **POST** /api/v2/testPlans/{id}/pause | Pause TestPlan
[**restore_test_plan**](TestPlansApi.md#restore_test_plan) | **POST** /api/v2/testPlans/{id}/restore | Restore TestPlan
[**start**](TestPlansApi.md#start) | **POST** /api/v2/testPlans/{id}/start | Start TestPlan
[**update_test_plan**](TestPlansApi.md#update_test_plan) | **PUT** /api/v2/testPlans | Update TestPlan


# **add_test_points_with_sections**
> add_test_points_with_sections(id)

Add test-points to test suite with sections

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.work_item_select_model import WorkItemSelectModel
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
    id = "1ed608bf-8ac9-4ffd-b91e-ebdbbdce6132" # str | Test suite internal identifier
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
            entity_types=[
                "entity_types_example",
            ],
            created_date_minimal=dateutil_parser('1970-01-01T00:00:00.00Z'),
            created_date_maximal=dateutil_parser('1970-01-01T00:00:00.00Z'),
            modified_date_minimal=dateutil_parser('1970-01-01T00:00:00.00Z'),
            modified_date_maximal=dateutil_parser('1970-01-01T00:00:00.00Z'),
            duration_minimal=1,
            duration_maximal=1,
            is_automated=True,
            tag_names=[
                "tag_names_example",
            ],
            auto_test_ids=[
                "auto_test_ids_example",
            ],
            except_work_item_ids=[
                "except_work_item_ids_example",
            ],
        ),
        extraction_model=WorkItemExtractionModel(
            include_work_items=[
                "include_work_items_example",
            ],
            include_sections=[
                "include_sections_example",
            ],
            include_projects=[
                "include_projects_example",
            ],
            exclude_work_items=[
                "exclude_work_items_example",
            ],
            exclude_sections=[
                "exclude_sections_example",
            ],
            exclude_projects=[
                "exclude_projects_example",
            ],
        ),
    ) # WorkItemSelectModel | Filter object to retrieve work items for test-suite's project (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add test-points to test suite with sections
        api_instance.add_test_points_with_sections(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->add_test_points_with_sections: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add test-points to test suite with sections
        api_instance.add_test_points_with_sections(id, work_item_select_model=work_item_select_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->add_test_points_with_sections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal identifier |
 **work_item_select_model** | [**WorkItemSelectModel**](WorkItemSelectModel.md)| Filter object to retrieve work items for test-suite&#39;s project | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan is required |  -  |
**404** | Test suite with provided ID was not found |  -  |
**422** | Shared steps cannot be added to test suite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_work_items_with_sections**
> add_work_items_with_sections(id)

Add WorkItems to TestPlan with Sections as TestSuites

<br>Use case  <br>User sets TestPlan identifier  <br>User sets WorkItem identifiers (listed in request example)  <br>User runs method execution  <br>System added WorkItems and Sections to TestPlan  <br>System returns no content response

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
**403** | Update permission for TestPlan required |  -  |
**422** | Can&#39;t put a SharedStep in the TestSuite |  -  |
**204** | Successful operation |  -  |
**400** | &lt;br&gt;TestPlan is locked  &lt;br&gt;Some of configurations do not exist in the project, or they are not active |  -  |
**401** | Unauthorized |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestPlan with id  &lt;br&gt;Some of workItems do not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_analytics_get**
> TestPointAnalyticResult api_v2_test_plans_id_analytics_get(id)

Get analytics by TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System returns analytics by test plan

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
**404** | Can&#39;t find a Project with id |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_autobalance_post**
> TestPlanWithTestSuiteTreeModel api_v2_test_plans_id_autobalance_post(id)

Auto-balance for TestPlan with testers

<br>Use case  <br>User sets TestPlan identifier  <br>User sets testers identifiers (listed in request example)  <br>User runs method execution  <br>System auto-balances TestPlan  <br>System returns test plan model (listed in response example)

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
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier
    testers = [
        "testers_example",
    ] # [str] | List of testers internal identifiers (optional)

    # example passing only required values which don't have defaults set
    try:
        # Auto-balance for TestPlan with testers
        api_response = api_instance.api_v2_test_plans_id_autobalance_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_autobalance_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Auto-balance for TestPlan with testers
        api_response = api_instance.api_v2_test_plans_id_autobalance_post(id, testers=testers)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_autobalance_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **testers** | **[str]**| List of testers internal identifiers | [optional]

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
**400** | Bad Request |  -  |
**200** | Successful operation |  -  |
**404** | Test suite with provided ID was not found |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_configurations_get**
> [ConfigurationModel] api_v2_test_plans_id_configurations_get(id)

Get TestPlan configurations

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System return test plan configurations

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
**400** | Bad Request |  -  |
**403** | Read permission for test plan required |  -  |
**401** | Unauthorized |  -  |
**200** | Successful operation |  -  |
**404** | TestPlan not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_export_test_points_xlsx_post**
> file_type api_v2_test_plans_id_export_test_points_xlsx_post(id)

Export TestPoints from TestPlan in xls format

<br>Use case  <br>User sets test plan identifier  <br>User sets filter model (listed in request example)  <br>User runs method execution  <br>System return export xlsx file

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.get_xlsx_test_points_by_test_plan_model import GetXlsxTestPointsByTestPlanModel
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
    time_zone_offset_in_minutes = 1 # int |  (optional)
    get_xlsx_test_points_by_test_plan_model = GetXlsxTestPointsByTestPlanModel(
        include_name=True,
        include_section=True,
        include_priority=True,
        include_automated=True,
        include_status=True,
        include_duration=True,
        include_creation_date=True,
        include_author=True,
        include_modification_date=True,
        include_modified_by=True,
        include_tags=True,
        include_iterations=True,
        custom_attributes_ids=[
            "custom_attributes_ids_example",
        ],
        configuration_ids=[
            "configuration_ids_example",
        ],
    ) # GetXlsxTestPointsByTestPlanModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export TestPoints from TestPlan in xls format
        api_response = api_instance.api_v2_test_plans_id_export_test_points_xlsx_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_export_test_points_xlsx_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export TestPoints from TestPlan in xls format
        api_response = api_instance.api_v2_test_plans_id_export_test_points_xlsx_post(id, time_zone_offset_in_minutes=time_zone_offset_in_minutes, get_xlsx_test_points_by_test_plan_model=get_xlsx_test_points_by_test_plan_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_export_test_points_xlsx_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **time_zone_offset_in_minutes** | **int**|  | [optional]
 **get_xlsx_test_points_by_test_plan_model** | [**GetXlsxTestPointsByTestPlanModel**](GetXlsxTestPointsByTestPlanModel.md)|  | [optional]

### Return type

**file_type**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Read permission for test plan required |  -  |
**401** | Unauthorized |  -  |
**404** | TestPlan not found |  -  |
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_export_test_result_history_xlsx_post**
> file_type api_v2_test_plans_id_export_test_result_history_xlsx_post(id)

Export TestResults history from TestPlan in xls format

<br>Use case  <br>User sets test plan identifier  <br>User sets filter model (listed in request example)  <br>User runs method execution  <br>System return export xlsx file

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
        api_response = api_instance.api_v2_test_plans_id_export_test_result_history_xlsx_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_export_test_result_history_xlsx_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export TestResults history from TestPlan in xls format
        api_response = api_instance.api_v2_test_plans_id_export_test_result_history_xlsx_post(id, must_return_only_last_test_result=must_return_only_last_test_result, include_steps=include_steps, include_deleted_test_suites=include_deleted_test_suites, time_zone_offset_in_minutes=time_zone_offset_in_minutes)
        pprint(api_response)
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

**file_type**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test plan required |  -  |
**404** | TestPlan not found |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_history_get**
> [TestPlanChangeModel] api_v2_test_plans_id_history_get(id)

Get TestPlan history

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System return test plan history

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
**404** | TestPlan not found |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test plan required |  -  |
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_links_get**
> [TestPlanLink] api_v2_test_plans_id_links_get(id)

Get Links of TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User sets pagination filter (listed in request example)  <br>User runs method execution  <br>System returns links of TestPlan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.test_plan_link import TestPlanLink
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
**401** | Unauthorized |  -  |
**200** | Successful operation |  -  |
**403** | Read permission for test plan is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_points_last_results_get**
> [TestPointWithLastResultModel] api_v2_test_plans_id_test_points_last_results_get(id)

Get TestPoints with last result from TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User sets filter (listed in request example)  <br>User runs method execution  <br>System return test points with last result from test plan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.test_point_with_last_result_model import TestPointWithLastResultModel
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
    must_add_grouping_elements = True # bool |  (optional)
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
        api_response = api_instance.api_v2_test_plans_id_test_points_last_results_get(id, must_add_grouping_elements=must_add_grouping_elements, tester_id=tester_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_points_last_results_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |
 **must_add_grouping_elements** | **bool**|  | [optional]
 **tester_id** | **str**|  | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestPointWithLastResultModel]**](TestPointWithLastResultModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | TestPlan not found |  -  |
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test plan required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_points_reset_post**
> api_v2_test_plans_id_test_points_reset_post(id)

Reset TestPoints status of TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User sets test points identifiers  <br>User runs method execution  <br>System reset test points statuses of test plan

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
**400** | Bad Request |  -  |
**200** | Successful operation |  -  |
**422** | Client Error |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_runs_get**
> [TestRunModel] api_v2_test_plans_id_test_runs_get(id)

Get TestRuns of TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User sets TestRun status filter (listed in request example)  <br>User runs method execution  <br>System returns TestRuns for TestPlan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_run_model import TestRunModel
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

[**[TestRunModel]**](TestRunModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**403** | Read permission for test plan is required |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_runs_search_post**
> [TestRunModel] api_v2_test_plans_id_test_runs_search_post(id)

Search TestRuns of TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User sets TestRuns filter (listed in request example)  <br>User runs method execution  <br>System returns TestRuns for TestPlan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_run_model import TestRunModel
from testit_api_client.model.test_run_search_query_model import TestRunSearchQueryModel
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
    test_run_search_query_model = TestRunSearchQueryModel(
        name="name_example",
        state=[
            TestRunStateTypeModel("NotStarted"),
        ],
        start_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        end_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        created_by_ids=[
            "created_by_ids_example",
        ],
    ) # TestRunSearchQueryModel |  (optional)

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
        api_response = api_instance.api_v2_test_plans_id_test_runs_search_post(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, test_run_search_query_model=test_run_search_query_model)
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
 **test_run_search_query_model** | [**TestRunSearchQueryModel**](TestRunSearchQueryModel.md)|  | [optional]

### Return type

[**[TestRunModel]**](TestRunModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Read permission for test plan is required |  -  |
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get**
> datetime api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get(id)

Get max modified date in TestRun for TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System returns max modified date in TestRun for TestPlan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
    api_instance = test_plans_api.TestPlansApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test plan internal (guid format) or global (int  format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get max modified date in TestRun for TestPlan
        api_response = api_instance.api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test plan internal (guid format) or global (int  format) identifier |

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
**403** | Update permission for test plan is required |  -  |
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_id_unlock_request_post**
> api_v2_test_plans_id_unlock_request_post(id)

Send unlock TestPlan notification

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System send unlock test plan notification

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
**401** | Unauthorized |  -  |
**200** | Successful operation |  -  |
**404** | TestPlan not found |  -  |
**403** | Read permission for test plan required |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_plans_shorts_post**
> [TestPlanShortModel] api_v2_test_plans_shorts_post()

Get TestPlans short models by Project identifiers

<br>Use case  <br>User sets projects identifiers  <br>User runs method execution  <br>System return test plans short models (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.test_plan_short_model import TestPlanShortModel
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
**404** | Project not found |  -  |
**403** | Read permission for project required |  -  |
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone**
> TestPlanModel clone(id)

Clone TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System clones test plan  <br>System returns test plan (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete**
> complete(id)

Complete TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System completes the test plan and updates test plan status  <br>System returns no content response

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
**400** | &lt;br&gt;Change status from New to Completed forbidden  &lt;br&gt;Change status from Completed to Completed forbidden |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_plan**
> TestPlanModel create_test_plan()

Create TestPlan

<br>Use case  <br>User sets test plan properties (listed in request example)  <br>User runs method execution  <br>System creates test plan  <br>System returns test plan (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.test_plan_post_model import TestPlanPostModel
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
    test_plan_post_model = TestPlanPostModel(
        tags=[
            TagShortModel(
                name="name_example",
            ),
        ],
        name="Base test plan",
        start_date=dateutil_parser('2022-07-21T14:38:15.619775Z'),
        end_date=dateutil_parser('2022-07-21T14:38:15.619775Z'),
        description="This is a base test plan",
        build="v.3.0.0-b94f3055",
        project_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        product_name="Billing service",
        has_automatic_duration_timer=True,
        attributes={
            "key": None,
        },
    ) # TestPlanPostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create TestPlan
        api_response = api_instance.create_test_plan(test_plan_post_model=test_plan_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->create_test_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_plan_post_model** | [**TestPlanPostModel**](TestPlanPostModel.md)|  | [optional]

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
**400** | &lt;br&gt;Field is required  &lt;br&gt;Tags must be no more than 10! |  -  |
**409** | TestPlan with the same name already exists! |  -  |
**401** | Unauthorized |  -  |
**201** | Successful operation |  -  |
**403** | Update permission for test plan required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_plan**
> delete_test_plan(id)

Delete TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System delete test plan  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
**404** | Can&#39;t find a TestPlan with id! |  -  |
**401** | Unauthorized |  -  |
**403** | Delete permission for test plan required |  -  |
**204** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_plan_by_id**
> TestPlanModel get_test_plan_by_id(id)

Get TestPlan by Id

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System search  test plan by the identifier  <br>System returns test plan

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_plan_model import TestPlanModel
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
**401** | Unauthorized |  -  |
**403** | Read permission for test plan required |  -  |
**404** | Can&#39;t find a Project with id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_suites_by_id**
> [TestSuiteV2TreeModel] get_test_suites_by_id(id)

Get TestSuites Tree By Id

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System finds test suites related to the test plan  <br>System returns test suites as a tree model (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_suite_v2_tree_model import TestSuiteV2TreeModel
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

[**[TestSuiteV2TreeModel]**](TestSuiteV2TreeModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**404** | Can&#39;t find a TestRun with id! |  -  |
**403** | Read permission for test plan required |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pause**
> pause(id)

Pause TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System pauses the test plan and updates test plan status  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
**404** | Can&#39;t find a TestPlan with id! |  -  |
**204** | Successful operation |  -  |
**400** | &lt;br&gt;Change status from New to Paused forbidden  &lt;br&gt;Change status from Paused to Paused forbidden  &lt;br&gt;Change status from Completed to Paused forbidden |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_test_plan**
> restore_test_plan(id)

Restore TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System restores test plan  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
**401** | Unauthorized |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |
**204** | Successful operation |  -  |
**403** | Update permission for test plan required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start**
> start(id)

Start TestPlan

<br>Use case  <br>User sets test plan identifier  <br>User runs method execution  <br>System starts the test plan and updates test plan status  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
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
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |
**204** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_plan**
> update_test_plan()

Update TestPlan

<br>Use case  <br>User sets test plan properties(listed in request example)  <br>User runs method execution  <br>System updates test plan  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_plans_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_plan_put_model import TestPlanPutModel
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
    test_plan_put_model = TestPlanPutModel(
        id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        locked_by_id="locked_by_id_example",
        tags=[
            TagShortModel(
                name="name_example",
            ),
        ],
        name="Base test plan",
        start_date=dateutil_parser('2022-07-21T14:38:15.619775Z'),
        end_date=dateutil_parser('2022-07-21T14:38:15.619775Z'),
        description="This is a base test plan",
        build="v.3.0.0-b94f3055",
        project_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        product_name="Billing service",
        has_automatic_duration_timer=True,
        attributes={
            "key": None,
        },
    ) # TestPlanPutModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update TestPlan
        api_instance.update_test_plan(test_plan_put_model=test_plan_put_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestPlansApi->update_test_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_plan_put_model** | [**TestPlanPutModel**](TestPlanPutModel.md)|  | [optional]

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
**400** | &lt;br&gt;Field is required  &lt;br&gt;Tags must be no more than 10!  &lt;br&gt;StartDate can&#39;t be more than EndDate! |  -  |
**204** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**409** | TestPlan with the same name already exists! |  -  |
**404** | Can&#39;t find a TestPlan with id! |  -  |
**422** | Can&#39;t change ProjectId |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

