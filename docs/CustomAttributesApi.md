# testit_api_client.CustomAttributesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_custom_attributes_exists_get**](CustomAttributesApi.md#api_v2_custom_attributes_exists_get) | **GET** /api/v2/customAttributes/exists | 
[**api_v2_custom_attributes_global_id_delete**](CustomAttributesApi.md#api_v2_custom_attributes_global_id_delete) | **DELETE** /api/v2/customAttributes/global/{id} | Delete global attribute
[**api_v2_custom_attributes_global_id_put**](CustomAttributesApi.md#api_v2_custom_attributes_global_id_put) | **PUT** /api/v2/customAttributes/global/{id} | Edit global attribute
[**api_v2_custom_attributes_global_post**](CustomAttributesApi.md#api_v2_custom_attributes_global_post) | **POST** /api/v2/customAttributes/global | Create global attribute
[**api_v2_custom_attributes_id_get**](CustomAttributesApi.md#api_v2_custom_attributes_id_get) | **GET** /api/v2/customAttributes/{id} | Get attribute
[**api_v2_custom_attributes_search_post**](CustomAttributesApi.md#api_v2_custom_attributes_search_post) | **POST** /api/v2/customAttributes/search | Search for attributes


# **api_v2_custom_attributes_exists_get**
> CustomAttributeValidationResult api_v2_custom_attributes_exists_get()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_validation_result import CustomAttributeValidationResult
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    name = "name_example" # str |  (optional)
    is_global = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_custom_attributes_exists_get(name=name, is_global=is_global)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_exists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional]
 **is_global** | **bool**|  | [optional]

### Return type

[**CustomAttributeValidationResult**](CustomAttributeValidationResult.md)

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

# **api_v2_custom_attributes_global_id_delete**
> api_v2_custom_attributes_global_id_delete(id)

Delete global attribute

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    id = "id_example" # str | Unique ID of attribute

    # example passing only required values which don't have defaults set
    try:
        # Delete global attribute
        api_instance.api_v2_custom_attributes_global_id_delete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_global_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of attribute |

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
**403** | System administrator role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_global_id_put**
> CustomAttributeModel api_v2_custom_attributes_global_id_put(id)

Edit global attribute

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.api_v2_custom_attributes_global_id_put_request import ApiV2CustomAttributesGlobalIdPutRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_model import CustomAttributeModel
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    id = "id_example" # str | Unique ID of attribute
    api_v2_custom_attributes_global_id_put_request = ApiV2CustomAttributesGlobalIdPutRequest(None) # ApiV2CustomAttributesGlobalIdPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit global attribute
        api_response = api_instance.api_v2_custom_attributes_global_id_put(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_global_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit global attribute
        api_response = api_instance.api_v2_custom_attributes_global_id_put(id, api_v2_custom_attributes_global_id_put_request=api_v2_custom_attributes_global_id_put_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_global_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of attribute |
 **api_v2_custom_attributes_global_id_put_request** | [**ApiV2CustomAttributesGlobalIdPutRequest**](ApiV2CustomAttributesGlobalIdPutRequest.md)|  | [optional]

### Return type

[**CustomAttributeModel**](CustomAttributeModel.md)

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
**403** | System administrator role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_global_post**
> CustomAttributeModel api_v2_custom_attributes_global_post()

Create global attribute

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.api_v2_custom_attributes_global_post_request import ApiV2CustomAttributesGlobalPostRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_model import CustomAttributeModel
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    api_v2_custom_attributes_global_post_request = ApiV2CustomAttributesGlobalPostRequest(None) # ApiV2CustomAttributesGlobalPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create global attribute
        api_response = api_instance.api_v2_custom_attributes_global_post(api_v2_custom_attributes_global_post_request=api_v2_custom_attributes_global_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_global_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_custom_attributes_global_post_request** | [**ApiV2CustomAttributesGlobalPostRequest**](ApiV2CustomAttributesGlobalPostRequest.md)|  | [optional]

### Return type

[**CustomAttributeModel**](CustomAttributeModel.md)

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
**403** | System administrator role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_id_get**
> CustomAttributeModel api_v2_custom_attributes_id_get(id)

Get attribute

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_model import CustomAttributeModel
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    id = "id_example" # str | Unique ID of attribute

    # example passing only required values which don't have defaults set
    try:
        # Get attribute
        api_response = api_instance.api_v2_custom_attributes_id_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of attribute |

### Return type

[**CustomAttributeModel**](CustomAttributeModel.md)

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

# **api_v2_custom_attributes_search_post**
> [CustomAttributeSearchResponseModel] api_v2_custom_attributes_search_post()

Search for attributes

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.custom_attribute_search_response_model import CustomAttributeSearchResponseModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.api_v2_custom_attributes_search_post_request import ApiV2CustomAttributesSearchPostRequest
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    api_v2_custom_attributes_search_post_request = ApiV2CustomAttributesSearchPostRequest(None) # ApiV2CustomAttributesSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for attributes
        api_response = api_instance.api_v2_custom_attributes_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, api_v2_custom_attributes_search_post_request=api_v2_custom_attributes_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **api_v2_custom_attributes_search_post_request** | [**ApiV2CustomAttributesSearchPostRequest**](ApiV2CustomAttributesSearchPostRequest.md)|  | [optional]

### Return type

[**[CustomAttributeSearchResponseModel]**](CustomAttributeSearchResponseModel.md)

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

