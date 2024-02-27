# testit_api_client.TagsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_tags_delete**](TagsApi.md#api_v2_tags_delete) | **DELETE** /api/v2/tags | Delete tags
[**api_v2_tags_get**](TagsApi.md#api_v2_tags_get) | **GET** /api/v2/tags | Get all Tags
[**api_v2_tags_id_delete**](TagsApi.md#api_v2_tags_id_delete) | **DELETE** /api/v2/tags/{id} | Delete tag
[**api_v2_tags_post**](TagsApi.md#api_v2_tags_post) | **POST** /api/v2/tags | Create tag
[**api_v2_tags_put**](TagsApi.md#api_v2_tags_put) | **PUT** /api/v2/tags | Update tag
[**api_v2_tags_search_get**](TagsApi.md#api_v2_tags_search_get) | **GET** /api/v2/tags/search | Search tags
[**api_v2_tags_test_plans_tags_get**](TagsApi.md#api_v2_tags_test_plans_tags_get) | **GET** /api/v2/tags/testPlansTags | Get all Tags that are used in TestPlans


# **api_v2_tags_delete**
> api_v2_tags_delete()

Delete tags

<br>Use case  <br>User sets collection of tags internal (guid format) identifiers  <br>System searches and deletes a collection of tags

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import tags_api
from testit_api_client.model.api_v2_tags_delete_request import ApiV2TagsDeleteRequest
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
    api_instance = tags_api.TagsApi(api_client)
    api_v2_tags_delete_request = ApiV2TagsDeleteRequest(None) # ApiV2TagsDeleteRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete tags
        api_instance.api_v2_tags_delete(api_v2_tags_delete_request=api_v2_tags_delete_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling TagsApi->api_v2_tags_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_tags_delete_request** | [**ApiV2TagsDeleteRequest**](ApiV2TagsDeleteRequest.md)|  | [optional]

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
**400** | &lt;br&gt;- ID is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | System administrator role is required |  -  |
**404** | No tags with provided IDs were found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_get**
> [TagModel] api_v2_tags_get()

Get all Tags

<br>Use case  <br>User runs method execution  <br>System returns tags (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import tags_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.tag_model import TagModel
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
    api_instance = tags_api.TagsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all Tags
        api_response = api_instance.api_v2_tags_get()
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TagsApi->api_v2_tags_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[TagModel]**](TagModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_id_delete**
> api_v2_tags_id_delete(id)

Delete tag

<br>Use case  <br>User sets tag internal (guid format) identifier  <br>System search and delete tag

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import tags_api
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
    api_instance = tags_api.TagsApi(api_client)
    id = "id_example" # str | Tag internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete tag
        api_instance.api_v2_tags_id_delete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TagsApi->api_v2_tags_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag internal (UUID) identifier |

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
**400** | &lt;br&gt;- ID is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | System administrator role is required |  -  |
**404** | Tag with provided ID cannot be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_post**
> TagModel api_v2_tags_post()

Create tag

<br>Use case  <br>User sets tag model (listed in the request example)  <br>User runs method execution  <br>System creates tag  <br>System returns tag model (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import tags_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.tag_model import TagModel
from testit_api_client.model.api_v2_tags_post_request import ApiV2TagsPostRequest
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
    api_instance = tags_api.TagsApi(api_client)
    api_v2_tags_post_request = ApiV2TagsPostRequest(None) # ApiV2TagsPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create tag
        api_response = api_instance.api_v2_tags_post(api_v2_tags_post_request=api_v2_tags_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TagsApi->api_v2_tags_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_tags_post_request** | [**ApiV2TagsPostRequest**](ApiV2TagsPostRequest.md)|  | [optional]

### Return type

[**TagModel**](TagModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | &lt;br&gt;- Name cannot be empty or contain only white space characters  &lt;br&gt;- Name already in use  &lt;br&gt;- Name must be no more than 30 characters long |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_put**
> TagModel api_v2_tags_put()

Update tag

<br>Use case  <br>User sets tag ID and model (listed in the request example)  <br>User runs method execution  <br>System updates tag  <br>System returns tag model (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import tags_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.tag_model import TagModel
from testit_api_client.model.api_v2_tags_put_request import ApiV2TagsPutRequest
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
    api_instance = tags_api.TagsApi(api_client)
    id = "id_example" # str |  (optional)
    api_v2_tags_put_request = ApiV2TagsPutRequest(None) # ApiV2TagsPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update tag
        api_response = api_instance.api_v2_tags_put(id=id, api_v2_tags_put_request=api_v2_tags_put_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TagsApi->api_v2_tags_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional]
 **api_v2_tags_put_request** | [**ApiV2TagsPutRequest**](ApiV2TagsPutRequest.md)|  | [optional]

### Return type

[**TagModel**](TagModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | &lt;br&gt;- ID is not valid  &lt;br&gt;- Name cannot be empty or contain only white space characters  &lt;br&gt;- Name already in use  &lt;br&gt;- Name must be no more than 30 characters long |  -  |
**401** | Unauthorized |  -  |
**403** | Project creator role is required |  -  |
**404** | Tag with provided ID cannot be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_search_get**
> [TagModel] api_v2_tags_search_get()

Search tags

<br>Use case  <br>User runs method execution  <br>System returns collection of tags (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import tags_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.tag_model import TagModel
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
    api_instance = tags_api.TagsApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search tags
        api_response = api_instance.api_v2_tags_search_get(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TagsApi->api_v2_tags_search_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TagModel]**](TagModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**401** | Unauthorized |  -  |
**400** | &lt;br&gt;orderByStatement must have one &#39;.&#39; and no &#39;,&#39; symbols  &lt;br&gt;orderByStatement has invalid length  &lt;br&gt;orderByStatement must have uuid as attribute key  &lt;br&gt;Search field not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_test_plans_tags_get**
> [TagModel] api_v2_tags_test_plans_tags_get()

Get all Tags that are used in TestPlans

<br>Use case  <br>User runs method execution  <br>System returns tags (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import tags_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.tag_model import TagModel
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
    api_instance = tags_api.TagsApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all Tags that are used in TestPlans
        api_response = api_instance.api_v2_tags_test_plans_tags_get(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TagsApi->api_v2_tags_test_plans_tags_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TagModel]**](TagModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | &lt;br&gt;orderByStatement must have one &#39;.&#39; and no &#39;,&#39; symbols  &lt;br&gt;orderByStatement has invalid length  &lt;br&gt;orderByStatement must have uuid as attribute key  &lt;br&gt;Search field not found |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

