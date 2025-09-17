# testit_api_client.ProjectTestPlanTestPointsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post**](ProjectTestPlanTestPointsApi.md#api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post) | **POST** /api/v2/projects/{projectId}/test-plans/{testPlanId}/test-points/autotests/rerun | Rerun autotests.
[**api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post**](ProjectTestPlanTestPointsApi.md#api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post) | **POST** /api/v2/projects/{projectId}/test-plans/{testPlanId}/test-points/autotests/run | Run autotests.


# **api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post**
> api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post(project_id, test_plan_id)

Rerun autotests.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plan_test_points_api
from testit_api_client.model.api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post_request import ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRerunPostRequest
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
    api_instance = project_test_plan_test_points_api.ProjectTestPlanTestPointsApi(api_client)
    project_id = "projectId_example" # str | 
    test_plan_id = "testPlanId_example" # str | 
    api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post_request = ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRerunPostRequest(None) # ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRerunPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Rerun autotests.
        api_instance.api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post(project_id, test_plan_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanTestPointsApi->api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Rerun autotests.
        api_instance.api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post(project_id, test_plan_id, api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post_request=api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanTestPointsApi->api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **test_plan_id** | **str**|  |
 **api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post_request** | [**ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRerunPostRequest**](ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRerunPostRequest.md)|  | [optional]

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post**
> TestRunNameApiResult api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post(project_id, test_plan_id)

Run autotests.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plan_test_points_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post_request import ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRunPostRequest
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.test_run_name_api_result import TestRunNameApiResult
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
    api_instance = project_test_plan_test_points_api.ProjectTestPlanTestPointsApi(api_client)
    project_id = "projectId_example" # str | 
    test_plan_id = "testPlanId_example" # str | 
    api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post_request = ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRunPostRequest(None) # ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRunPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Run autotests.
        api_response = api_instance.api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post(project_id, test_plan_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanTestPointsApi->api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Run autotests.
        api_response = api_instance.api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post(project_id, test_plan_id, api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post_request=api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanTestPointsApi->api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **test_plan_id** | **str**|  |
 **api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post_request** | [**ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRunPostRequest**](ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRunPostRequest.md)|  | [optional]

### Return type

[**TestRunNameApiResult**](TestRunNameApiResult.md)

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

