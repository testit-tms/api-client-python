# testit_api_client.ProjectSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_project_id_settings_autotests_post**](ProjectSettingsApi.md#api_v2_projects_project_id_settings_autotests_post) | **POST** /api/v2/projects/{projectId}/settings/autotests | Set autotest project settings.
[**get_autotest_project_settings**](ProjectSettingsApi.md#get_autotest_project_settings) | **GET** /api/v2/projects/{projectId}/settings/autotests | Get autotest project settings.


# **api_v2_projects_project_id_settings_autotests_post**
> api_v2_projects_project_id_settings_autotests_post(project_id)

Set autotest project settings.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_settings_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_projects_project_id_settings_autotests_post_request import ApiV2ProjectsProjectIdSettingsAutotestsPostRequest
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
    api_instance = project_settings_api.ProjectSettingsApi(api_client)
    project_id = "projectId_example" # str | 
    api_v2_projects_project_id_settings_autotests_post_request = ApiV2ProjectsProjectIdSettingsAutotestsPostRequest(None) # ApiV2ProjectsProjectIdSettingsAutotestsPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set autotest project settings.
        api_instance.api_v2_projects_project_id_settings_autotests_post(project_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectSettingsApi->api_v2_projects_project_id_settings_autotests_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set autotest project settings.
        api_instance.api_v2_projects_project_id_settings_autotests_post(project_id, api_v2_projects_project_id_settings_autotests_post_request=api_v2_projects_project_id_settings_autotests_post_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectSettingsApi->api_v2_projects_project_id_settings_autotests_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |
 **api_v2_projects_project_id_settings_autotests_post_request** | [**ApiV2ProjectsProjectIdSettingsAutotestsPostRequest**](ApiV2ProjectsProjectIdSettingsAutotestsPostRequest.md)|  | [optional]

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

# **get_autotest_project_settings**
> AutoTestProjectSettingsGetModel get_autotest_project_settings(project_id)

Get autotest project settings.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_settings_api
from testit_api_client.model.auto_test_project_settings_get_model import AutoTestProjectSettingsGetModel
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
    api_instance = project_settings_api.ProjectSettingsApi(api_client)
    project_id = "projectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get autotest project settings.
        api_response = api_instance.get_autotest_project_settings(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectSettingsApi->get_autotest_project_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  |

### Return type

[**AutoTestProjectSettingsGetModel**](AutoTestProjectSettingsGetModel.md)

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

