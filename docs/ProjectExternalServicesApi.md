# testit_api_client.ProjectExternalServicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_id_external_services_external_service_id_delete**](ProjectExternalServicesApi.md#api_v2_projects_id_external_services_external_service_id_delete) | **DELETE** /api/v2/projects/{id}/external-services/{externalServiceId} | Disable an external service
[**api_v2_projects_id_external_services_external_service_id_get**](ProjectExternalServicesApi.md#api_v2_projects_id_external_services_external_service_id_get) | **GET** /api/v2/projects/{id}/external-services/{externalServiceId} | Retrieves settings of an external service
[**api_v2_projects_id_external_services_external_service_id_patch**](ProjectExternalServicesApi.md#api_v2_projects_id_external_services_external_service_id_patch) | **PATCH** /api/v2/projects/{id}/external-services/{externalServiceId} | Replaces one active external service with another
[**api_v2_projects_id_external_services_external_service_id_put**](ProjectExternalServicesApi.md#api_v2_projects_id_external_services_external_service_id_put) | **PUT** /api/v2/projects/{id}/external-services/{externalServiceId} | Enable an external service
[**api_v2_projects_id_external_services_get**](ProjectExternalServicesApi.md#api_v2_projects_id_external_services_get) | **GET** /api/v2/projects/{id}/external-services | Retrieves information about external services, including their integration status (enabled or not)
[**api_v2_projects_id_external_services_issues_search_post**](ProjectExternalServicesApi.md#api_v2_projects_id_external_services_issues_search_post) | **POST** /api/v2/projects/{id}/external-services/issues/search | Searches for external issues using enabled external services in project


# **api_v2_projects_id_external_services_external_service_id_delete**
> api_v2_projects_id_external_services_external_service_id_delete(id, external_service_id)

Disable an external service

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_external_services_api
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
    api_instance = project_external_services_api.ProjectExternalServicesApi(api_client)
    id = "id_example" # str | Project ID
    external_service_id = "externalServiceId_example" # str | External service ID

    # example passing only required values which don't have defaults set
    try:
        # Disable an external service
        api_instance.api_v2_projects_id_external_services_external_service_id_delete(id, external_service_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExternalServicesApi->api_v2_projects_id_external_services_external_service_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project ID |
 **external_service_id** | **str**| External service ID |

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_external_services_external_service_id_get**
> ProjectExternalServiceSettingsApiResult api_v2_projects_id_external_services_external_service_id_get(id, external_service_id)

Retrieves settings of an external service

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_external_services_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_external_service_settings_api_result import ProjectExternalServiceSettingsApiResult
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
    api_instance = project_external_services_api.ProjectExternalServicesApi(api_client)
    id = "id_example" # str | Project ID
    external_service_id = "externalServiceId_example" # str | External service ID

    # example passing only required values which don't have defaults set
    try:
        # Retrieves settings of an external service
        api_response = api_instance.api_v2_projects_id_external_services_external_service_id_get(id, external_service_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExternalServicesApi->api_v2_projects_id_external_services_external_service_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project ID |
 **external_service_id** | **str**| External service ID |

### Return type

[**ProjectExternalServiceSettingsApiResult**](ProjectExternalServiceSettingsApiResult.md)

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

# **api_v2_projects_id_external_services_external_service_id_patch**
> api_v2_projects_id_external_services_external_service_id_patch(id, external_service_id)

Replaces one active external service with another

See <a href=\"https://www.rfc-editor.org/rfc/rfc6902\" target=\"_blank\">RFC 6902: JavaScript Object Notation (JSON) Patch</a> for details

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_external_services_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_projects_id_external_services_external_service_id_patch_request import ApiV2ProjectsIdExternalServicesExternalServiceIdPatchRequest
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
    api_instance = project_external_services_api.ProjectExternalServicesApi(api_client)
    id = "id_example" # str | Project ID
    external_service_id = "externalServiceId_example" # str | External service ID
    api_v2_projects_id_external_services_external_service_id_patch_request = ApiV2ProjectsIdExternalServicesExternalServiceIdPatchRequest(None) # ApiV2ProjectsIdExternalServicesExternalServiceIdPatchRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Replaces one active external service with another
        api_instance.api_v2_projects_id_external_services_external_service_id_patch(id, external_service_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExternalServicesApi->api_v2_projects_id_external_services_external_service_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Replaces one active external service with another
        api_instance.api_v2_projects_id_external_services_external_service_id_patch(id, external_service_id, api_v2_projects_id_external_services_external_service_id_patch_request=api_v2_projects_id_external_services_external_service_id_patch_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExternalServicesApi->api_v2_projects_id_external_services_external_service_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project ID |
 **external_service_id** | **str**| External service ID |
 **api_v2_projects_id_external_services_external_service_id_patch_request** | [**ApiV2ProjectsIdExternalServicesExternalServiceIdPatchRequest**](ApiV2ProjectsIdExternalServicesExternalServiceIdPatchRequest.md)|  | [optional]

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

# **api_v2_projects_id_external_services_external_service_id_put**
> api_v2_projects_id_external_services_external_service_id_put(id, external_service_id)

Enable an external service

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_external_services_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.api_v2_projects_id_external_services_external_service_id_put_request import ApiV2ProjectsIdExternalServicesExternalServiceIdPutRequest
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
    api_instance = project_external_services_api.ProjectExternalServicesApi(api_client)
    id = "id_example" # str | Project ID
    external_service_id = "externalServiceId_example" # str | External service ID
    api_v2_projects_id_external_services_external_service_id_put_request = ApiV2ProjectsIdExternalServicesExternalServiceIdPutRequest(None) # ApiV2ProjectsIdExternalServicesExternalServiceIdPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Enable an external service
        api_instance.api_v2_projects_id_external_services_external_service_id_put(id, external_service_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExternalServicesApi->api_v2_projects_id_external_services_external_service_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable an external service
        api_instance.api_v2_projects_id_external_services_external_service_id_put(id, external_service_id, api_v2_projects_id_external_services_external_service_id_put_request=api_v2_projects_id_external_services_external_service_id_put_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExternalServicesApi->api_v2_projects_id_external_services_external_service_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project ID |
 **external_service_id** | **str**| External service ID |
 **api_v2_projects_id_external_services_external_service_id_put_request** | [**ApiV2ProjectsIdExternalServicesExternalServiceIdPutRequest**](ApiV2ProjectsIdExternalServicesExternalServiceIdPutRequest.md)|  | [optional]

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

# **api_v2_projects_id_external_services_get**
> ProjectExternalServicesApiResult api_v2_projects_id_external_services_get(id)

Retrieves information about external services, including their integration status (enabled or not)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_external_services_api
from testit_api_client.model.api_external_service_category import ApiExternalServiceCategory
from testit_api_client.model.project_external_services_api_result import ProjectExternalServicesApiResult
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
    api_instance = project_external_services_api.ProjectExternalServicesApi(api_client)
    id = "id_example" # str | Project ID
    category = None # ApiExternalServiceCategory |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieves information about external services, including their integration status (enabled or not)
        api_response = api_instance.api_v2_projects_id_external_services_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExternalServicesApi->api_v2_projects_id_external_services_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieves information about external services, including their integration status (enabled or not)
        api_response = api_instance.api_v2_projects_id_external_services_get(id, category=category)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExternalServicesApi->api_v2_projects_id_external_services_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project ID |
 **category** | **ApiExternalServiceCategory**|  | [optional]

### Return type

[**ProjectExternalServicesApiResult**](ProjectExternalServicesApiResult.md)

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

# **api_v2_projects_id_external_services_issues_search_post**
> [ExternalIssueApiResult] api_v2_projects_id_external_services_issues_search_post(id)

Searches for external issues using enabled external services in project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_external_services_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.external_issue_api_result import ExternalIssueApiResult
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.api_v2_projects_id_external_services_issues_search_post_request import ApiV2ProjectsIdExternalServicesIssuesSearchPostRequest
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
    api_instance = project_external_services_api.ProjectExternalServicesApi(api_client)
    id = "id_example" # str | Internal (UUID) or global (integer) identifier
    api_v2_projects_id_external_services_issues_search_post_request = ApiV2ProjectsIdExternalServicesIssuesSearchPostRequest(None) # ApiV2ProjectsIdExternalServicesIssuesSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Searches for external issues using enabled external services in project
        api_response = api_instance.api_v2_projects_id_external_services_issues_search_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExternalServicesApi->api_v2_projects_id_external_services_issues_search_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Searches for external issues using enabled external services in project
        api_response = api_instance.api_v2_projects_id_external_services_issues_search_post(id, api_v2_projects_id_external_services_issues_search_post_request=api_v2_projects_id_external_services_issues_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectExternalServicesApi->api_v2_projects_id_external_services_issues_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Internal (UUID) or global (integer) identifier |
 **api_v2_projects_id_external_services_issues_search_post_request** | [**ApiV2ProjectsIdExternalServicesIssuesSearchPostRequest**](ApiV2ProjectsIdExternalServicesIssuesSearchPostRequest.md)|  | [optional]

### Return type

[**[ExternalIssueApiResult]**](ExternalIssueApiResult.md)

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

