# testit_api_client.WebhooksApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_webhooks_get**](WebhooksApi.md#api_v2_webhooks_get) | **GET** /api/v2/webhooks | Get all webhooks
[**api_v2_webhooks_id_delete**](WebhooksApi.md#api_v2_webhooks_id_delete) | **DELETE** /api/v2/webhooks/{id} | Delete webhook by ID
[**api_v2_webhooks_id_get**](WebhooksApi.md#api_v2_webhooks_id_get) | **GET** /api/v2/webhooks/{id} | Get webhook by ID
[**api_v2_webhooks_id_put**](WebhooksApi.md#api_v2_webhooks_id_put) | **PUT** /api/v2/webhooks/{id} | Edit webhook by ID
[**api_v2_webhooks_post**](WebhooksApi.md#api_v2_webhooks_post) | **POST** /api/v2/webhooks | Create webhook
[**api_v2_webhooks_search_post**](WebhooksApi.md#api_v2_webhooks_search_post) | **POST** /api/v2/webhooks/search | Search for webhooks
[**api_v2_webhooks_special_variables_get**](WebhooksApi.md#api_v2_webhooks_special_variables_get) | **GET** /api/v2/webhooks/specialVariables | Get special variables for webhook event type


# **api_v2_webhooks_get**
> [WebHookModel] api_v2_webhooks_get()

Get all webhooks

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import webhooks_api
from testit_api_client.model.web_hook_model import WebHookModel
from testit_api_client.model.problem_details import ProblemDetails
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    project_id = "projectId_example" # str | Project unique ID (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all webhooks
        api_response = api_instance.api_v2_webhooks_get(project_id=project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project unique ID | [optional]

### Return type

[**[WebHookModel]**](WebHookModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Read permission for requested project is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_id_delete**
> api_v2_webhooks_id_delete(id)

Delete webhook by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import webhooks_api
from testit_api_client.model.problem_details import ProblemDetails
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = "id_example" # str | Webhook unique ID

    # example passing only required values which don't have defaults set
    try:
        # Delete webhook by ID
        api_instance.api_v2_webhooks_id_delete(id)
    except testit_api_client.ApiException as e:
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
**403** | Delete permission for webhooks is required |  -  |
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_id_get**
> WebHookModel api_v2_webhooks_id_get(id)

Get webhook by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import webhooks_api
from testit_api_client.model.web_hook_model import WebHookModel
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = "id_example" # str | Webhook unique ID

    # example passing only required values which don't have defaults set
    try:
        # Get webhook by ID
        api_response = api_instance.api_v2_webhooks_id_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**200** | Success |  -  |
**403** | Update permission for webhooks is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_id_put**
> WebHookModel api_v2_webhooks_id_put(id)

Edit webhook by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import webhooks_api
from testit_api_client.model.web_hook_model import WebHookModel
from testit_api_client.model.web_hook_post_model import WebHookPostModel
from testit_api_client.model.problem_details import ProblemDetails
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    id = "id_example" # str | Webhook unique ID
    web_hook_post_model = WebHookPostModel(
        project_id="project_id_example",
        event_type=WebHookEventTypeModel("AutomatedTestRunCreated"),
        description="description_example",
        url="url_example",
        request_type=RequestTypeModel("Post"),
        should_send_body=True,
        headers={
            "key": "key_example",
        },
        query_parameters={
            "key": "key_example",
        },
        is_enabled=True,
        should_send_custom_body=True,
        custom_body="custom_body_example",
        should_replace_parameters=True,
        should_escape_parameters=True,
        name="name_example",
    ) # WebHookPostModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit webhook by ID
        api_response = api_instance.api_v2_webhooks_id_put(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit webhook by ID
        api_response = api_instance.api_v2_webhooks_id_put(id, web_hook_post_model=web_hook_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**200** | Success |  -  |
**403** | Update permission for webhooks is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_post**
> WebHookModel api_v2_webhooks_post()

Create webhook

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import webhooks_api
from testit_api_client.model.web_hook_model import WebHookModel
from testit_api_client.model.web_hook_post_model import WebHookPostModel
from testit_api_client.model.problem_details import ProblemDetails
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    web_hook_post_model = WebHookPostModel(
        project_id="project_id_example",
        event_type=WebHookEventTypeModel("AutomatedTestRunCreated"),
        description="description_example",
        url="url_example",
        request_type=RequestTypeModel("Post"),
        should_send_body=True,
        headers={
            "key": "key_example",
        },
        query_parameters={
            "key": "key_example",
        },
        is_enabled=True,
        should_send_custom_body=True,
        custom_body="custom_body_example",
        should_replace_parameters=True,
        should_escape_parameters=True,
        name="name_example",
    ) # WebHookPostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create webhook
        api_response = api_instance.api_v2_webhooks_post(web_hook_post_model=web_hook_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**403** | Update permission for webhooks is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_search_post**
> [WebHookModel] api_v2_webhooks_search_post()

Search for webhooks

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import webhooks_api
from testit_api_client.model.web_hook_model import WebHookModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.search_webhooks_query_model import SearchWebhooksQueryModel
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    search_webhooks_query_model = SearchWebhooksQueryModel(
        name="name_example",
        event_types=[
            WebHookEventTypeModel("AutomatedTestRunCreated"),
        ],
        methods=[
            RequestTypeModel("Post"),
        ],
        project_ids=[
            "project_ids_example",
        ],
        is_enabled=True,
    ) # SearchWebhooksQueryModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for webhooks
        api_response = api_instance.api_v2_webhooks_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, search_webhooks_query_model=search_webhooks_query_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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

[**[WebHookModel]**](WebHookModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**403** | Read permission for all requested projects is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_webhooks_special_variables_get**
> [str] api_v2_webhooks_special_variables_get()

Get special variables for webhook event type

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import webhooks_api
from testit_api_client.model.web_hook_event_type import WebHookEventType
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    event_type = WebHookEventType("AutomatedTestRunCreated") # WebHookEventType | Webhook event type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get special variables for webhook event type
        api_response = api_instance.api_v2_webhooks_special_variables_get(event_type=event_type)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WebhooksApi->api_v2_webhooks_special_variables_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type** | **WebHookEventType**| Webhook event type | [optional]

### Return type

**[str]**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

