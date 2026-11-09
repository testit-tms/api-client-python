# testit_api_client.AutoTestsProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_project_id_auto_tests_import_post**](AutoTestsProjectApi.md#api_v2_projects_project_id_auto_tests_import_post) | **POST** /api/v2/projects/{projectId}/auto-tests/import | Schedules import of auto tests JUnit XML report.


# **api_v2_projects_project_id_auto_tests_import_post**
> api_v2_projects_project_id_auto_tests_import_post(project_id)

Schedules import of auto tests JUnit XML report.

### Example

* Api Key Authentication (PrivateToken):
* Api Key Authentication (Cookies):

```python
import time
import testit_api_client
from testit_api_client.api import auto_tests_project_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_projects_project_id_auto_tests_import_post_request import ApiV2ProjectsProjectIdAutoTestsImportPostRequest
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

# Configure API key authorization: PrivateToken
configuration.api_key['PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PrivateToken'] = 'Bearer'

# Configure API key authorization: Cookies
configuration.api_key['Cookies'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Cookies'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auto_tests_project_api.AutoTestsProjectApi(api_client)
    project_id = "projectId_example" # str | Project ID
    api_v2_projects_project_id_auto_tests_import_post_request = ApiV2ProjectsProjectIdAutoTestsImportPostRequest(None) # ApiV2ProjectsProjectIdAutoTestsImportPostRequest | The request model with collection of reports to import. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Schedules import of auto tests JUnit XML report.
        api_instance.api_v2_projects_project_id_auto_tests_import_post(project_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling AutoTestsProjectApi->api_v2_projects_project_id_auto_tests_import_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Schedules import of auto tests JUnit XML report.
        api_instance.api_v2_projects_project_id_auto_tests_import_post(project_id, api_v2_projects_project_id_auto_tests_import_post_request=api_v2_projects_project_id_auto_tests_import_post_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling AutoTestsProjectApi->api_v2_projects_project_id_auto_tests_import_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
 **api_v2_projects_project_id_auto_tests_import_post_request** | [**ApiV2ProjectsProjectIdAutoTestsImportPostRequest**](ApiV2ProjectsProjectIdAutoTestsImportPostRequest.md)| The request model with collection of reports to import. | [optional]

### Return type

void (empty response body)

### Authorization

[PrivateToken](../README.md#PrivateToken), [Cookies](../README.md#Cookies)

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

