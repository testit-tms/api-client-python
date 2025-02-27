# testit_api_client.WebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_webhooks_delete**](WebhooksApi.md#api_v2_webhooks_delete) | **DELETE** /api/v2/webhooks | 
[**api_v2_webhooks_get**](WebhooksApi.md#api_v2_webhooks_get) | **GET** /api/v2/webhooks | Get all webhooks
[**api_v2_webhooks_id_delete**](WebhooksApi.md#api_v2_webhooks_id_delete) | **DELETE** /api/v2/webhooks/{id} | Delete webhook by ID
[**api_v2_webhooks_id_get**](WebhooksApi.md#api_v2_webhooks_id_get) | **GET** /api/v2/webhooks/{id} | Get webhook by ID
[**api_v2_webhooks_id_put**](WebhooksApi.md#api_v2_webhooks_id_put) | **PUT** /api/v2/webhooks/{id} | Edit webhook by ID
[**api_v2_webhooks_post**](WebhooksApi.md#api_v2_webhooks_post) | **POST** /api/v2/webhooks | Create webhook
[**api_v2_webhooks_put**](WebhooksApi.md#api_v2_webhooks_put) | **PUT** /api/v2/webhooks | 
[**api_v2_webhooks_search_post**](WebhooksApi.md#api_v2_webhooks_search_post) | **POST** /api/v2/webhooks/search | Search for webhooks
[**api_v2_webhooks_special_variables_get**](WebhooksApi.md#api_v2_webhooks_special_variables_get) | **GET** /api/v2/webhooks/specialVariables | Get special variables for webhook event type
[**api_v2_webhooks_test_post**](WebhooksApi.md#api_v2_webhooks_test_post) | **POST** /api/v2/webhooks/test | Test webhook&#39;s url


# **api_v2_webhooks_delete**
> api_v2_webhooks_delete(webhooks_delete_api_model=webhooks_delete_api_model)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.webhooks_delete_api_model import WebhooksDeleteApiModel
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
    api_instance = testit_api_client.WebhooksApi(api_client)
    webhooks_delete_api_model = testit_api_client.WebhooksDeleteApiModel() # WebhooksDeleteApiModel |  (optional)

    try:
        api_instance.api_v2_webhooks_delete(webhooks_delete_api_model=webhooks_delete_api_model)
    except Exception as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhooks_delete_api_model** | [**WebhooksDeleteApiModel**](WebhooksDeleteApiModel.md)|  | [optional] 

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

# **api_v2_webhooks_get**
> List[WebHookModel] api_v2_webhooks_get(project_id=project_id)

Get all webhooks

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.web_hook_model import WebHookModel
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
    api_instance = testit_api_client.WebhooksApi(api_client)
    project_id = 'project_id_example' # str | Project unique ID (optional)

    try:
        # Get all webhooks
        api_response = api_instance.api_v2_webhooks_get(project_id=project_id)
        print("The response of WebhooksApi->api_v2_webhooks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project unique ID | [optional] 

### Return type

[**List[WebHookModel]**](WebHookModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for requested project is required |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_id_delete**
> api_v2_webhooks_id_delete(id)

Delete webhook by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
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
    api_instance = testit_api_client.WebhooksApi(api_client)
    id = 'id_example' # str | Webhook unique ID

    try:
        # Delete webhook by ID
        api_instance.api_v2_webhooks_id_delete(id)
    except Exception as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook unique ID | 

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
**403** | Delete permission for webhooks is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_id_get**
> WebHookModel api_v2_webhooks_id_get(id)

Get webhook by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.web_hook_model import WebHookModel
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
    api_instance = testit_api_client.WebhooksApi(api_client)
    id = 'id_example' # str | Webhook unique ID

    try:
        # Get webhook by ID
        api_response = api_instance.api_v2_webhooks_id_get(id)
        print("The response of WebhooksApi->api_v2_webhooks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook unique ID | 

### Return type

[**WebHookModel**](WebHookModel.md)

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
**403** | Update permission for webhooks is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_id_put**
> WebHookModel api_v2_webhooks_id_put(id, web_hook_post_model=web_hook_post_model)

Edit webhook by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.web_hook_model import WebHookModel
from testit_api_client.models.web_hook_post_model import WebHookPostModel
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
    api_instance = testit_api_client.WebhooksApi(api_client)
    id = 'id_example' # str | Webhook unique ID
    web_hook_post_model = testit_api_client.WebHookPostModel() # WebHookPostModel |  (optional)

    try:
        # Edit webhook by ID
        api_response = api_instance.api_v2_webhooks_id_put(id, web_hook_post_model=web_hook_post_model)
        print("The response of WebhooksApi->api_v2_webhooks_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Webhook unique ID | 
 **web_hook_post_model** | [**WebHookPostModel**](WebHookPostModel.md)|  | [optional] 

### Return type

[**WebHookModel**](WebHookModel.md)

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
**403** | Update permission for webhooks is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_post**
> WebHookModel api_v2_webhooks_post(web_hook_post_model=web_hook_post_model)

Create webhook

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.web_hook_model import WebHookModel
from testit_api_client.models.web_hook_post_model import WebHookPostModel
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
    api_instance = testit_api_client.WebhooksApi(api_client)
    web_hook_post_model = testit_api_client.WebHookPostModel() # WebHookPostModel |  (optional)

    try:
        # Create webhook
        api_response = api_instance.api_v2_webhooks_post(web_hook_post_model=web_hook_post_model)
        print("The response of WebhooksApi->api_v2_webhooks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_post_model** | [**WebHookPostModel**](WebHookPostModel.md)|  | [optional] 

### Return type

[**WebHookModel**](WebHookModel.md)

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
**403** | Update permission for webhooks is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_put**
> WebhooksUpdateApiResult api_v2_webhooks_put(webhooks_update_api_model=webhooks_update_api_model)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.webhooks_update_api_model import WebhooksUpdateApiModel
from testit_api_client.models.webhooks_update_api_result import WebhooksUpdateApiResult
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
    api_instance = testit_api_client.WebhooksApi(api_client)
    webhooks_update_api_model = testit_api_client.WebhooksUpdateApiModel() # WebhooksUpdateApiModel |  (optional)

    try:
        api_response = api_instance.api_v2_webhooks_put(webhooks_update_api_model=webhooks_update_api_model)
        print("The response of WebhooksApi->api_v2_webhooks_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhooks_update_api_model** | [**WebhooksUpdateApiModel**](WebhooksUpdateApiModel.md)|  | [optional] 

### Return type

[**WebhooksUpdateApiResult**](WebhooksUpdateApiResult.md)

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

# **api_v2_webhooks_search_post**
> List[WebHookModel] api_v2_webhooks_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, search_webhooks_query_model=search_webhooks_query_model)

Search for webhooks

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.search_webhooks_query_model import SearchWebhooksQueryModel
from testit_api_client.models.web_hook_model import WebHookModel
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
    api_instance = testit_api_client.WebhooksApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    search_webhooks_query_model = testit_api_client.SearchWebhooksQueryModel() # SearchWebhooksQueryModel |  (optional)

    try:
        # Search for webhooks
        api_response = api_instance.api_v2_webhooks_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, search_webhooks_query_model=search_webhooks_query_model)
        print("The response of WebhooksApi->api_v2_webhooks_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **search_webhooks_query_model** | [**SearchWebhooksQueryModel**](SearchWebhooksQueryModel.md)|  | [optional] 

### Return type

[**List[WebHookModel]**](WebHookModel.md)

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
**403** | Read permission for all requested projects is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_special_variables_get**
> List[str] api_v2_webhooks_special_variables_get(event_type=event_type, variables_type=variables_type)

Get special variables for webhook event type

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
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
    api_instance = testit_api_client.WebhooksApi(api_client)
    event_type = testit_api_client.WebHookEventType() # WebHookEventType | Webhook event type (optional)
    variables_type = testit_api_client.WebhookVariablesType() # WebhookVariablesType |  (optional)

    try:
        # Get special variables for webhook event type
        api_response = api_instance.api_v2_webhooks_special_variables_get(event_type=event_type, variables_type=variables_type)
        print("The response of WebhooksApi->api_v2_webhooks_special_variables_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_special_variables_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | [**WebHookEventType**](.md)| Webhook event type | [optional] 
 **variables_type** | [**WebhookVariablesType**](.md)|  | [optional] 

### Return type

**List[str]**

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

# **api_v2_webhooks_test_post**
> WebhookResponse api_v2_webhooks_test_post(web_hook_test_model=web_hook_test_model)

Test webhook's url

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.web_hook_test_model import WebHookTestModel
from testit_api_client.models.webhook_response import WebhookResponse
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
    api_instance = testit_api_client.WebhooksApi(api_client)
    web_hook_test_model = testit_api_client.WebHookTestModel() # WebHookTestModel |  (optional)

    try:
        # Test webhook's url
        api_response = api_instance.api_v2_webhooks_test_post(web_hook_test_model=web_hook_test_model)
        print("The response of WebhooksApi->api_v2_webhooks_test_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_test_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_test_model** | [**WebHookTestModel**](WebHookTestModel.md)|  | [optional] 

### Return type

[**WebhookResponse**](WebhookResponse.md)

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
**403** | Update permission for webhooks is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

