# testit_api_client.FailureCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_autotests_failure_categories_count_per_failure_category_post**](FailureCategoriesApi.md#api_v2_autotests_failure_categories_count_per_failure_category_post) | **POST** /api/v2/autotests/failure-categories/count-per-failure-category | 
[**api_v2_autotests_failure_categories_grouping_search_post**](FailureCategoriesApi.md#api_v2_autotests_failure_categories_grouping_search_post) | **POST** /api/v2/autotests/failure-categories/grouping-search | Get failure categories with support for filtering, sorting and grouping
[**api_v2_autotests_failure_categories_id_delete**](FailureCategoriesApi.md#api_v2_autotests_failure_categories_id_delete) | **DELETE** /api/v2/autotests/failure-categories/{id} | Delete failure category
[**api_v2_autotests_failure_categories_id_get**](FailureCategoriesApi.md#api_v2_autotests_failure_categories_id_get) | **GET** /api/v2/autotests/failure-categories/{id} | Get failure category by ID
[**api_v2_autotests_failure_categories_name_name_exists_get**](FailureCategoriesApi.md#api_v2_autotests_failure_categories_name_name_exists_get) | **GET** /api/v2/autotests/failure-categories/name/{name}/exists | Check failure category with the specified name already exists
[**api_v2_autotests_failure_categories_post**](FailureCategoriesApi.md#api_v2_autotests_failure_categories_post) | **POST** /api/v2/autotests/failure-categories | Create failure category
[**api_v2_autotests_failure_categories_put**](FailureCategoriesApi.md#api_v2_autotests_failure_categories_put) | **PUT** /api/v2/autotests/failure-categories | Update failure category
[**api_v2_autotests_failure_categories_search_post**](FailureCategoriesApi.md#api_v2_autotests_failure_categories_search_post) | **POST** /api/v2/autotests/failure-categories/search | 
[**api_v2_autotests_result_reasons_count_per_failure_category_post**](FailureCategoriesApi.md#api_v2_autotests_result_reasons_count_per_failure_category_post) | **POST** /api/v2/autotests/resultReasons/count-per-failure-category | 
[**api_v2_autotests_result_reasons_grouping_search_post**](FailureCategoriesApi.md#api_v2_autotests_result_reasons_grouping_search_post) | **POST** /api/v2/autotests/resultReasons/grouping-search | Get failure categories with support for filtering, sorting and grouping
[**api_v2_autotests_result_reasons_id_delete**](FailureCategoriesApi.md#api_v2_autotests_result_reasons_id_delete) | **DELETE** /api/v2/autotests/resultReasons/{id} | Delete failure category
[**api_v2_autotests_result_reasons_id_get**](FailureCategoriesApi.md#api_v2_autotests_result_reasons_id_get) | **GET** /api/v2/autotests/resultReasons/{id} | Get failure category by ID
[**api_v2_autotests_result_reasons_name_name_exists_get**](FailureCategoriesApi.md#api_v2_autotests_result_reasons_name_name_exists_get) | **GET** /api/v2/autotests/resultReasons/name/{name}/exists | Check failure category with the specified name already exists
[**api_v2_autotests_result_reasons_post**](FailureCategoriesApi.md#api_v2_autotests_result_reasons_post) | **POST** /api/v2/autotests/resultReasons | Create failure category
[**api_v2_autotests_result_reasons_put**](FailureCategoriesApi.md#api_v2_autotests_result_reasons_put) | **PUT** /api/v2/autotests/resultReasons | Update failure category
[**api_v2_autotests_result_reasons_search_post**](FailureCategoriesApi.md#api_v2_autotests_result_reasons_search_post) | **POST** /api/v2/autotests/resultReasons/search | 


# **api_v2_autotests_failure_categories_count_per_failure_category_post**
> AutoTestResultReasonsCountModel api_v2_autotests_failure_categories_count_per_failure_category_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.api_v2_autotests_result_reasons_search_post_request import ApiV2AutotestsResultReasonsSearchPostRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.auto_test_result_reasons_count_model import AutoTestResultReasonsCountModel
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    api_v2_autotests_result_reasons_search_post_request = ApiV2AutotestsResultReasonsSearchPostRequest(None) # ApiV2AutotestsResultReasonsSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_autotests_failure_categories_count_per_failure_category_post(api_v2_autotests_result_reasons_search_post_request=api_v2_autotests_result_reasons_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_failure_categories_count_per_failure_category_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_autotests_result_reasons_search_post_request** | [**ApiV2AutotestsResultReasonsSearchPostRequest**](ApiV2AutotestsResultReasonsSearchPostRequest.md)|  | [optional]

### Return type

[**AutoTestResultReasonsCountModel**](AutoTestResultReasonsCountModel.md)

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

# **api_v2_autotests_failure_categories_grouping_search_post**
> FailureCategoryGroupItemApiResultReply api_v2_autotests_failure_categories_grouping_search_post()

Get failure categories with support for filtering, sorting and grouping

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.failure_category_group_item_api_result_reply import FailureCategoryGroupItemApiResultReply
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_autotests_result_reasons_grouping_search_post_request import ApiV2AutotestsResultReasonsGroupingSearchPostRequest
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    api_v2_autotests_result_reasons_grouping_search_post_request = ApiV2AutotestsResultReasonsGroupingSearchPostRequest(None) # ApiV2AutotestsResultReasonsGroupingSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get failure categories with support for filtering, sorting and grouping
        api_response = api_instance.api_v2_autotests_failure_categories_grouping_search_post(api_v2_autotests_result_reasons_grouping_search_post_request=api_v2_autotests_result_reasons_grouping_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_failure_categories_grouping_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_autotests_result_reasons_grouping_search_post_request** | [**ApiV2AutotestsResultReasonsGroupingSearchPostRequest**](ApiV2AutotestsResultReasonsGroupingSearchPostRequest.md)|  | [optional]

### Return type

[**FailureCategoryGroupItemApiResultReply**](FailureCategoryGroupItemApiResultReply.md)

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

# **api_v2_autotests_failure_categories_id_delete**
> api_v2_autotests_failure_categories_id_delete(id)

Delete failure category

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete failure category
        api_instance.api_v2_autotests_failure_categories_id_delete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_failure_categories_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **api_v2_autotests_failure_categories_id_get**
> FailureCategoryApiResult api_v2_autotests_failure_categories_id_get(id)

Get failure category by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.failure_category_api_result import FailureCategoryApiResult
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    id = "id_example" # str | 
    is_deleted = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get failure category by ID
        api_response = api_instance.api_v2_autotests_failure_categories_id_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_failure_categories_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get failure category by ID
        api_response = api_instance.api_v2_autotests_failure_categories_id_get(id, is_deleted=is_deleted)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_failure_categories_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **is_deleted** | **bool**|  | [optional]

### Return type

[**FailureCategoryApiResult**](FailureCategoryApiResult.md)

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

# **api_v2_autotests_failure_categories_name_name_exists_get**
> bool api_v2_autotests_failure_categories_name_name_exists_get(name)

Check failure category with the specified name already exists

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Check failure category with the specified name already exists
        api_response = api_instance.api_v2_autotests_failure_categories_name_name_exists_get(name)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_failure_categories_name_name_exists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

**bool**

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

# **api_v2_autotests_failure_categories_post**
> FailureCategoryApiResult api_v2_autotests_failure_categories_post()

Create failure category

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.failure_category_api_result import FailureCategoryApiResult
from testit_api_client.model.api_v2_autotests_result_reasons_post_request import ApiV2AutotestsResultReasonsPostRequest
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    api_v2_autotests_result_reasons_post_request = ApiV2AutotestsResultReasonsPostRequest(None) # ApiV2AutotestsResultReasonsPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create failure category
        api_response = api_instance.api_v2_autotests_failure_categories_post(api_v2_autotests_result_reasons_post_request=api_v2_autotests_result_reasons_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_failure_categories_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_autotests_result_reasons_post_request** | [**ApiV2AutotestsResultReasonsPostRequest**](ApiV2AutotestsResultReasonsPostRequest.md)|  | [optional]

### Return type

[**FailureCategoryApiResult**](FailureCategoryApiResult.md)

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

# **api_v2_autotests_failure_categories_put**
> api_v2_autotests_failure_categories_put()

Update failure category

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_autotests_result_reasons_put_request import ApiV2AutotestsResultReasonsPutRequest
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    api_v2_autotests_result_reasons_put_request = ApiV2AutotestsResultReasonsPutRequest(None) # ApiV2AutotestsResultReasonsPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update failure category
        api_instance.api_v2_autotests_failure_categories_put(api_v2_autotests_result_reasons_put_request=api_v2_autotests_result_reasons_put_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_failure_categories_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_autotests_result_reasons_put_request** | [**ApiV2AutotestsResultReasonsPutRequest**](ApiV2AutotestsResultReasonsPutRequest.md)|  | [optional]

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

# **api_v2_autotests_failure_categories_search_post**
> [AutotestResultReasonShortGetModel] api_v2_autotests_failure_categories_search_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.autotest_result_reason_short_get_model import AutotestResultReasonShortGetModel
from testit_api_client.model.api_v2_autotests_result_reasons_search_post_request import ApiV2AutotestsResultReasonsSearchPostRequest
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    api_v2_autotests_result_reasons_search_post_request = ApiV2AutotestsResultReasonsSearchPostRequest(None) # ApiV2AutotestsResultReasonsSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_autotests_failure_categories_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, api_v2_autotests_result_reasons_search_post_request=api_v2_autotests_result_reasons_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_failure_categories_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **api_v2_autotests_result_reasons_search_post_request** | [**ApiV2AutotestsResultReasonsSearchPostRequest**](ApiV2AutotestsResultReasonsSearchPostRequest.md)|  | [optional]

### Return type

[**[AutotestResultReasonShortGetModel]**](AutotestResultReasonShortGetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_autotests_result_reasons_count_per_failure_category_post**
> AutoTestResultReasonsCountModel api_v2_autotests_result_reasons_count_per_failure_category_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.api_v2_autotests_result_reasons_search_post_request import ApiV2AutotestsResultReasonsSearchPostRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.auto_test_result_reasons_count_model import AutoTestResultReasonsCountModel
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    api_v2_autotests_result_reasons_search_post_request = ApiV2AutotestsResultReasonsSearchPostRequest(None) # ApiV2AutotestsResultReasonsSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_autotests_result_reasons_count_per_failure_category_post(api_v2_autotests_result_reasons_search_post_request=api_v2_autotests_result_reasons_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_result_reasons_count_per_failure_category_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_autotests_result_reasons_search_post_request** | [**ApiV2AutotestsResultReasonsSearchPostRequest**](ApiV2AutotestsResultReasonsSearchPostRequest.md)|  | [optional]

### Return type

[**AutoTestResultReasonsCountModel**](AutoTestResultReasonsCountModel.md)

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

# **api_v2_autotests_result_reasons_grouping_search_post**
> FailureCategoryGroupItemApiResultReply api_v2_autotests_result_reasons_grouping_search_post()

Get failure categories with support for filtering, sorting and grouping

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.failure_category_group_item_api_result_reply import FailureCategoryGroupItemApiResultReply
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_autotests_result_reasons_grouping_search_post_request import ApiV2AutotestsResultReasonsGroupingSearchPostRequest
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    api_v2_autotests_result_reasons_grouping_search_post_request = ApiV2AutotestsResultReasonsGroupingSearchPostRequest(None) # ApiV2AutotestsResultReasonsGroupingSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get failure categories with support for filtering, sorting and grouping
        api_response = api_instance.api_v2_autotests_result_reasons_grouping_search_post(api_v2_autotests_result_reasons_grouping_search_post_request=api_v2_autotests_result_reasons_grouping_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_result_reasons_grouping_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_autotests_result_reasons_grouping_search_post_request** | [**ApiV2AutotestsResultReasonsGroupingSearchPostRequest**](ApiV2AutotestsResultReasonsGroupingSearchPostRequest.md)|  | [optional]

### Return type

[**FailureCategoryGroupItemApiResultReply**](FailureCategoryGroupItemApiResultReply.md)

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

# **api_v2_autotests_result_reasons_id_delete**
> api_v2_autotests_result_reasons_id_delete(id)

Delete failure category

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete failure category
        api_instance.api_v2_autotests_result_reasons_id_delete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_result_reasons_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **api_v2_autotests_result_reasons_id_get**
> FailureCategoryApiResult api_v2_autotests_result_reasons_id_get(id)

Get failure category by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.failure_category_api_result import FailureCategoryApiResult
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    id = "id_example" # str | 
    is_deleted = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get failure category by ID
        api_response = api_instance.api_v2_autotests_result_reasons_id_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_result_reasons_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get failure category by ID
        api_response = api_instance.api_v2_autotests_result_reasons_id_get(id, is_deleted=is_deleted)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_result_reasons_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **is_deleted** | **bool**|  | [optional]

### Return type

[**FailureCategoryApiResult**](FailureCategoryApiResult.md)

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

# **api_v2_autotests_result_reasons_name_name_exists_get**
> bool api_v2_autotests_result_reasons_name_name_exists_get(name)

Check failure category with the specified name already exists

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Check failure category with the specified name already exists
        api_response = api_instance.api_v2_autotests_result_reasons_name_name_exists_get(name)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_result_reasons_name_name_exists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

**bool**

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

# **api_v2_autotests_result_reasons_post**
> FailureCategoryApiResult api_v2_autotests_result_reasons_post()

Create failure category

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.failure_category_api_result import FailureCategoryApiResult
from testit_api_client.model.api_v2_autotests_result_reasons_post_request import ApiV2AutotestsResultReasonsPostRequest
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    api_v2_autotests_result_reasons_post_request = ApiV2AutotestsResultReasonsPostRequest(None) # ApiV2AutotestsResultReasonsPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create failure category
        api_response = api_instance.api_v2_autotests_result_reasons_post(api_v2_autotests_result_reasons_post_request=api_v2_autotests_result_reasons_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_result_reasons_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_autotests_result_reasons_post_request** | [**ApiV2AutotestsResultReasonsPostRequest**](ApiV2AutotestsResultReasonsPostRequest.md)|  | [optional]

### Return type

[**FailureCategoryApiResult**](FailureCategoryApiResult.md)

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

# **api_v2_autotests_result_reasons_put**
> api_v2_autotests_result_reasons_put()

Update failure category

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_autotests_result_reasons_put_request import ApiV2AutotestsResultReasonsPutRequest
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    api_v2_autotests_result_reasons_put_request = ApiV2AutotestsResultReasonsPutRequest(None) # ApiV2AutotestsResultReasonsPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update failure category
        api_instance.api_v2_autotests_result_reasons_put(api_v2_autotests_result_reasons_put_request=api_v2_autotests_result_reasons_put_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_result_reasons_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_autotests_result_reasons_put_request** | [**ApiV2AutotestsResultReasonsPutRequest**](ApiV2AutotestsResultReasonsPutRequest.md)|  | [optional]

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

# **api_v2_autotests_result_reasons_search_post**
> [AutotestResultReasonShortGetModel] api_v2_autotests_result_reasons_search_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import failure_categories_api
from testit_api_client.model.autotest_result_reason_short_get_model import AutotestResultReasonShortGetModel
from testit_api_client.model.api_v2_autotests_result_reasons_search_post_request import ApiV2AutotestsResultReasonsSearchPostRequest
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
    api_instance = failure_categories_api.FailureCategoriesApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    api_v2_autotests_result_reasons_search_post_request = ApiV2AutotestsResultReasonsSearchPostRequest(None) # ApiV2AutotestsResultReasonsSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_autotests_result_reasons_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, api_v2_autotests_result_reasons_search_post_request=api_v2_autotests_result_reasons_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling FailureCategoriesApi->api_v2_autotests_result_reasons_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **api_v2_autotests_result_reasons_search_post_request** | [**ApiV2AutotestsResultReasonsSearchPostRequest**](ApiV2AutotestsResultReasonsSearchPostRequest.md)|  | [optional]

### Return type

[**[AutotestResultReasonShortGetModel]**](AutotestResultReasonShortGetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

