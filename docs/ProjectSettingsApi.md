# testit_api_client.ProjectSettingsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_project_id_settings_autotests_post**](ProjectSettingsApi.md#api_v2_projects_project_id_settings_autotests_post) | **POST** /api/v2/projects/{projectId}/settings/autotests | Set autotest project settings.
[**get_autotest_project_settings**](ProjectSettingsApi.md#get_autotest_project_settings) | **GET** /api/v2/projects/{projectId}/settings/autotests | Get autotest project settings.


# **api_v2_projects_project_id_settings_autotests_post**
> api_v2_projects_project_id_settings_autotests_post(project_id, auto_test_project_settings_post_model=auto_test_project_settings_post_model)

Set autotest project settings.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.auto_test_project_settings_post_model import AutoTestProjectSettingsPostModel
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
    api_instance = testit_api_client.ProjectSettingsApi(api_client)
    project_id = 'project_id_example' # str | 
    auto_test_project_settings_post_model = testit_api_client.AutoTestProjectSettingsPostModel() # AutoTestProjectSettingsPostModel |  (optional)

    try:
        # Set autotest project settings.
        api_instance.api_v2_projects_project_id_settings_autotests_post(project_id, auto_test_project_settings_post_model=auto_test_project_settings_post_model)
    except Exception as e:
        print("Exception when calling ProjectSettingsApi->api_v2_projects_project_id_settings_autotests_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **auto_test_project_settings_post_model** | [**AutoTestProjectSettingsPostModel**](AutoTestProjectSettingsPostModel.md)|  | [optional] 

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
import testit_api_client
from testit_api_client.models.auto_test_project_settings_get_model import AutoTestProjectSettingsGetModel
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
    api_instance = testit_api_client.ProjectSettingsApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Get autotest project settings.
        api_response = api_instance.get_autotest_project_settings(project_id)
        print("The response of ProjectSettingsApi->get_autotest_project_settings:\n")
        pprint(api_response)
    except Exception as e:
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

