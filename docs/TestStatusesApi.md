# testit_api_client.TestStatusesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_test_statuses_code_code_exists_get**](TestStatusesApi.md#api_v2_test_statuses_code_code_exists_get) | **GET** /api/v2/testStatuses/code/{code}/exists | 
[**api_v2_test_statuses_id_delete**](TestStatusesApi.md#api_v2_test_statuses_id_delete) | **DELETE** /api/v2/testStatuses/{id} | 
[**api_v2_test_statuses_id_get**](TestStatusesApi.md#api_v2_test_statuses_id_get) | **GET** /api/v2/testStatuses/{id} | 
[**api_v2_test_statuses_id_put**](TestStatusesApi.md#api_v2_test_statuses_id_put) | **PUT** /api/v2/testStatuses/{id} | 
[**api_v2_test_statuses_name_name_exists_get**](TestStatusesApi.md#api_v2_test_statuses_name_name_exists_get) | **GET** /api/v2/testStatuses/name/{name}/exists | 
[**api_v2_test_statuses_post**](TestStatusesApi.md#api_v2_test_statuses_post) | **POST** /api/v2/testStatuses | 
[**api_v2_test_statuses_search_post**](TestStatusesApi.md#api_v2_test_statuses_search_post) | **POST** /api/v2/testStatuses/search | 


# **api_v2_test_statuses_code_code_exists_get**
> bool api_v2_test_statuses_code_code_exists_get(code)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_statuses_api
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
    api_instance = test_statuses_api.TestStatusesApi(api_client)
    code = "code_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_test_statuses_code_code_exists_get(code)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestStatusesApi->api_v2_test_statuses_code_code_exists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  |

### Return type

**bool**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


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

# **api_v2_test_statuses_id_delete**
> api_v2_test_statuses_id_delete(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_statuses_api
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
    api_instance = test_statuses_api.TestStatusesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_v2_test_statuses_id_delete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestStatusesApi->api_v2_test_statuses_id_delete: %s\n" % e)
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

# **api_v2_test_statuses_id_get**
> TestStatusApiResult api_v2_test_statuses_id_get(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_statuses_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_status_api_result import TestStatusApiResult
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
    api_instance = test_statuses_api.TestStatusesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_test_statuses_id_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestStatusesApi->api_v2_test_statuses_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**TestStatusApiResult**](TestStatusApiResult.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


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

# **api_v2_test_statuses_id_put**
> api_v2_test_statuses_id_put(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_statuses_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_test_statuses_id_put_request import ApiV2TestStatusesIdPutRequest
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
    api_instance = test_statuses_api.TestStatusesApi(api_client)
    id = "id_example" # str | 
    api_v2_test_statuses_id_put_request = ApiV2TestStatusesIdPutRequest(None) # ApiV2TestStatusesIdPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_v2_test_statuses_id_put(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestStatusesApi->api_v2_test_statuses_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.api_v2_test_statuses_id_put(id, api_v2_test_statuses_id_put_request=api_v2_test_statuses_id_put_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestStatusesApi->api_v2_test_statuses_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **api_v2_test_statuses_id_put_request** | [**ApiV2TestStatusesIdPutRequest**](ApiV2TestStatusesIdPutRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
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

# **api_v2_test_statuses_name_name_exists_get**
> bool api_v2_test_statuses_name_name_exists_get(name)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_statuses_api
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
    api_instance = test_statuses_api.TestStatusesApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_test_statuses_name_name_exists_get(name)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestStatusesApi->api_v2_test_statuses_name_name_exists_get: %s\n" % e)
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
 - **Accept**: text/plain, application/json, text/json


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

# **api_v2_test_statuses_post**
> TestStatusApiResult api_v2_test_statuses_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_statuses_api
from testit_api_client.model.api_v2_test_statuses_post_request import ApiV2TestStatusesPostRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_status_api_result import TestStatusApiResult
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
    api_instance = test_statuses_api.TestStatusesApi(api_client)
    api_v2_test_statuses_post_request = ApiV2TestStatusesPostRequest(None) # ApiV2TestStatusesPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_test_statuses_post(api_v2_test_statuses_post_request=api_v2_test_statuses_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestStatusesApi->api_v2_test_statuses_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_test_statuses_post_request** | [**ApiV2TestStatusesPostRequest**](ApiV2TestStatusesPostRequest.md)|  | [optional]

### Return type

[**TestStatusApiResult**](TestStatusApiResult.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


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

# **api_v2_test_statuses_search_post**
> TestStatusApiResultReply api_v2_test_statuses_search_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_statuses_api
from testit_api_client.model.api_v2_test_statuses_search_post_request import ApiV2TestStatusesSearchPostRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_status_api_result_reply import TestStatusApiResultReply
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
    api_instance = test_statuses_api.TestStatusesApi(api_client)
    api_v2_test_statuses_search_post_request = ApiV2TestStatusesSearchPostRequest(None) # ApiV2TestStatusesSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_test_statuses_search_post(api_v2_test_statuses_search_post_request=api_v2_test_statuses_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestStatusesApi->api_v2_test_statuses_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_test_statuses_search_post_request** | [**ApiV2TestStatusesSearchPostRequest**](ApiV2TestStatusesSearchPostRequest.md)|  | [optional]

### Return type

[**TestStatusApiResultReply**](TestStatusApiResultReply.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


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

