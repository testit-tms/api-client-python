# testit_api_client.ProjectFailureCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_project_id_autotests_failure_categories_grouping_search_post**](ProjectFailureCategoriesApi.md#api_v2_projects_project_id_autotests_failure_categories_grouping_search_post) | **POST** /api/v2/projects/{projectId}/autotests/failure-categories/grouping-search | Get failure categories with support for filtering, sorting and grouping
[**api_v2_projects_project_id_autotests_failure_categories_id_delete**](ProjectFailureCategoriesApi.md#api_v2_projects_project_id_autotests_failure_categories_id_delete) | **DELETE** /api/v2/projects/{projectId}/autotests/failure-categories/{id} | Delete failure category
[**api_v2_projects_project_id_autotests_failure_categories_id_get**](ProjectFailureCategoriesApi.md#api_v2_projects_project_id_autotests_failure_categories_id_get) | **GET** /api/v2/projects/{projectId}/autotests/failure-categories/{id} | Get failure category by ID
[**api_v2_projects_project_id_autotests_failure_categories_post**](ProjectFailureCategoriesApi.md#api_v2_projects_project_id_autotests_failure_categories_post) | **POST** /api/v2/projects/{projectId}/autotests/failure-categories | Create failure category
[**api_v2_projects_project_id_autotests_failure_categories_put**](ProjectFailureCategoriesApi.md#api_v2_projects_project_id_autotests_failure_categories_put) | **PUT** /api/v2/projects/{projectId}/autotests/failure-categories | Update failure category


# **api_v2_projects_project_id_autotests_failure_categories_grouping_search_post**
> ProjectFailureCategoryGroupItemApiResultReply api_v2_projects_project_id_autotests_failure_categories_grouping_search_post(project_id)

Get failure categories with support for filtering, sorting and grouping

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_failure_categories_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_autotests_result_reasons_grouping_search_post_request import ApiV2AutotestsResultReasonsGroupingSearchPostRequest
from testit_api_client.model.project_failure_category_group_item_api_result_reply import ProjectFailureCategoryGroupItemApiResultReply
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
    api_instance = project_failure_categories_api.ProjectFailureCategoriesApi(api_client)
    project_id = "projectId_example" # str | Internal (UUID) or global (integer) identifier
    api_v2_autotests_result_reasons_grouping_search_post_request = ApiV2AutotestsResultReasonsGroupingSearchPostRequest(None) # ApiV2AutotestsResultReasonsGroupingSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get failure categories with support for filtering, sorting and grouping
        api_response = api_instance.api_v2_projects_project_id_autotests_failure_categories_grouping_search_post(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectFailureCategoriesApi->api_v2_projects_project_id_autotests_failure_categories_grouping_search_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get failure categories with support for filtering, sorting and grouping
        api_response = api_instance.api_v2_projects_project_id_autotests_failure_categories_grouping_search_post(project_id, api_v2_autotests_result_reasons_grouping_search_post_request=api_v2_autotests_result_reasons_grouping_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectFailureCategoriesApi->api_v2_projects_project_id_autotests_failure_categories_grouping_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Internal (UUID) or global (integer) identifier |
 **api_v2_autotests_result_reasons_grouping_search_post_request** | [**ApiV2AutotestsResultReasonsGroupingSearchPostRequest**](ApiV2AutotestsResultReasonsGroupingSearchPostRequest.md)|  | [optional]

### Return type

[**ProjectFailureCategoryGroupItemApiResultReply**](ProjectFailureCategoryGroupItemApiResultReply.md)

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

# **api_v2_projects_project_id_autotests_failure_categories_id_delete**
> api_v2_projects_project_id_autotests_failure_categories_id_delete(project_id, id)

Delete failure category

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_failure_categories_api
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
    api_instance = project_failure_categories_api.ProjectFailureCategoriesApi(api_client)
    project_id = "projectId_example" # str | Internal (UUID) or global (integer) identifier
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete failure category
        api_instance.api_v2_projects_project_id_autotests_failure_categories_id_delete(project_id, id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectFailureCategoriesApi->api_v2_projects_project_id_autotests_failure_categories_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Internal (UUID) or global (integer) identifier |
 **id** | **str**|  |

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

# **api_v2_projects_project_id_autotests_failure_categories_id_get**
> ProjectDetailedFailureCategoryApiResult api_v2_projects_project_id_autotests_failure_categories_id_get(project_id, id)

Get failure category by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_failure_categories_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_detailed_failure_category_api_result import ProjectDetailedFailureCategoryApiResult
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
    api_instance = project_failure_categories_api.ProjectFailureCategoriesApi(api_client)
    project_id = "projectId_example" # str | Internal (UUID) or global (integer) identifier
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get failure category by ID
        api_response = api_instance.api_v2_projects_project_id_autotests_failure_categories_id_get(project_id, id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectFailureCategoriesApi->api_v2_projects_project_id_autotests_failure_categories_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Internal (UUID) or global (integer) identifier |
 **id** | **str**|  |

### Return type

[**ProjectDetailedFailureCategoryApiResult**](ProjectDetailedFailureCategoryApiResult.md)

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

# **api_v2_projects_project_id_autotests_failure_categories_post**
> ProjectDetailedFailureCategoryApiResult api_v2_projects_project_id_autotests_failure_categories_post(project_id)

Create failure category

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_failure_categories_api
from testit_api_client.model.api_v2_projects_project_id_autotests_failure_categories_post_request import ApiV2ProjectsProjectIdAutotestsFailureCategoriesPostRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_detailed_failure_category_api_result import ProjectDetailedFailureCategoryApiResult
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
    api_instance = project_failure_categories_api.ProjectFailureCategoriesApi(api_client)
    project_id = "projectId_example" # str | Internal (UUID) or global (integer) identifier
    api_v2_projects_project_id_autotests_failure_categories_post_request = ApiV2ProjectsProjectIdAutotestsFailureCategoriesPostRequest(None) # ApiV2ProjectsProjectIdAutotestsFailureCategoriesPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create failure category
        api_response = api_instance.api_v2_projects_project_id_autotests_failure_categories_post(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectFailureCategoriesApi->api_v2_projects_project_id_autotests_failure_categories_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create failure category
        api_response = api_instance.api_v2_projects_project_id_autotests_failure_categories_post(project_id, api_v2_projects_project_id_autotests_failure_categories_post_request=api_v2_projects_project_id_autotests_failure_categories_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectFailureCategoriesApi->api_v2_projects_project_id_autotests_failure_categories_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Internal (UUID) or global (integer) identifier |
 **api_v2_projects_project_id_autotests_failure_categories_post_request** | [**ApiV2ProjectsProjectIdAutotestsFailureCategoriesPostRequest**](ApiV2ProjectsProjectIdAutotestsFailureCategoriesPostRequest.md)|  | [optional]

### Return type

[**ProjectDetailedFailureCategoryApiResult**](ProjectDetailedFailureCategoryApiResult.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_autotests_failure_categories_put**
> api_v2_projects_project_id_autotests_failure_categories_put(project_id)

Update failure category

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_failure_categories_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.api_v2_projects_project_id_autotests_failure_categories_put_request import ApiV2ProjectsProjectIdAutotestsFailureCategoriesPutRequest
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
    api_instance = project_failure_categories_api.ProjectFailureCategoriesApi(api_client)
    project_id = "projectId_example" # str | Internal (UUID) or global (integer) identifier
    api_v2_projects_project_id_autotests_failure_categories_put_request = ApiV2ProjectsProjectIdAutotestsFailureCategoriesPutRequest(None) # ApiV2ProjectsProjectIdAutotestsFailureCategoriesPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update failure category
        api_instance.api_v2_projects_project_id_autotests_failure_categories_put(project_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectFailureCategoriesApi->api_v2_projects_project_id_autotests_failure_categories_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update failure category
        api_instance.api_v2_projects_project_id_autotests_failure_categories_put(project_id, api_v2_projects_project_id_autotests_failure_categories_put_request=api_v2_projects_project_id_autotests_failure_categories_put_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectFailureCategoriesApi->api_v2_projects_project_id_autotests_failure_categories_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Internal (UUID) or global (integer) identifier |
 **api_v2_projects_project_id_autotests_failure_categories_put_request** | [**ApiV2ProjectsProjectIdAutotestsFailureCategoriesPutRequest**](ApiV2ProjectsProjectIdAutotestsFailureCategoriesPutRequest.md)|  | [optional]

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

