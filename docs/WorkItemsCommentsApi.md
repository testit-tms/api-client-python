# testit_api_client.WorkItemsCommentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_work_items_comments_comment_id_delete**](WorkItemsCommentsApi.md#api_v2_work_items_comments_comment_id_delete) | **DELETE** /api/v2/workItems/comments/{commentId} | Delete WorkItem comment
[**api_v2_work_items_comments_post**](WorkItemsCommentsApi.md#api_v2_work_items_comments_post) | **POST** /api/v2/workItems/comments | Create WorkItem comment
[**api_v2_work_items_comments_put**](WorkItemsCommentsApi.md#api_v2_work_items_comments_put) | **PUT** /api/v2/workItems/comments | Update work item comment
[**api_v2_work_items_id_comments_count_get**](WorkItemsCommentsApi.md#api_v2_work_items_id_comments_count_get) | **GET** /api/v2/workItems/{id}/comments/count | Get work item comments count
[**api_v2_work_items_id_comments_get**](WorkItemsCommentsApi.md#api_v2_work_items_id_comments_get) | **GET** /api/v2/workItems/{id}/comments | Get work item comments


# **api_v2_work_items_comments_comment_id_delete**
> api_v2_work_items_comments_comment_id_delete(comment_id)

Delete WorkItem comment

 Use case   User sets comment identifier   User runs method execution   System delete comment    System returns success status code

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_comments_api
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
    api_instance = work_items_comments_api.WorkItemsCommentsApi(api_client)
    comment_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Comment internal (guid format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete WorkItem comment
        api_instance.api_v2_work_items_comments_comment_id_delete(comment_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsCommentsApi->api_v2_work_items_comments_comment_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**| Comment internal (guid format) identifier |

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
**204** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | System admin permission required |  -  |
**404** | WorkItem is not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_comments_post**
> WorkItemCommentModel api_v2_work_items_comments_post()

Create WorkItem comment

 Use case   User sets comment properties (listed in request parameters)   User runs method execution   System creates comment    System returns comment model (listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_comments_api
from testit_api_client.model.api_v2_work_items_comments_post_request import ApiV2WorkItemsCommentsPostRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.work_item_comment_model import WorkItemCommentModel
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
    api_instance = work_items_comments_api.WorkItemsCommentsApi(api_client)
    api_v2_work_items_comments_post_request = ApiV2WorkItemsCommentsPostRequest(None) # ApiV2WorkItemsCommentsPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create WorkItem comment
        api_response = api_instance.api_v2_work_items_comments_post(api_v2_work_items_comments_post_request=api_v2_work_items_comments_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsCommentsApi->api_v2_work_items_comments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_work_items_comments_post_request** | [**ApiV2WorkItemsCommentsPostRequest**](ApiV2WorkItemsCommentsPostRequest.md)|  | [optional]

### Return type

[**WorkItemCommentModel**](WorkItemCommentModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library required |  -  |
**404** | WorkItem is not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_comments_put**
> api_v2_work_items_comments_put()

Update work item comment

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_comments_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.api_v2_work_items_comments_put_request import ApiV2WorkItemsCommentsPutRequest
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
    api_instance = work_items_comments_api.WorkItemsCommentsApi(api_client)
    api_v2_work_items_comments_put_request = ApiV2WorkItemsCommentsPutRequest(None) # ApiV2WorkItemsCommentsPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update work item comment
        api_instance.api_v2_work_items_comments_put(api_v2_work_items_comments_put_request=api_v2_work_items_comments_put_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsCommentsApi->api_v2_work_items_comments_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_work_items_comments_put_request** | [**ApiV2WorkItemsCommentsPutRequest**](ApiV2WorkItemsCommentsPutRequest.md)|  | [optional]

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
**403** | System administrator role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_comments_count_get**
> int api_v2_work_items_id_comments_count_get(id)

Get work item comments count

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_comments_api
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
    api_instance = work_items_comments_api.WorkItemsCommentsApi(api_client)
    id = "id_example" # str | Unique or global ID of the work item

    # example passing only required values which don't have defaults set
    try:
        # Get work item comments count
        api_response = api_instance.api_v2_work_items_id_comments_count_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsCommentsApi->api_v2_work_items_id_comments_count_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the work item |

### Return type

**int**

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
**403** | Read permission for test library is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_id_comments_get**
> [WorkItemCommentModel] api_v2_work_items_id_comments_get(id)

Get work item comments

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_comments_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.work_item_comment_model import WorkItemCommentModel
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
    api_instance = work_items_comments_api.WorkItemsCommentsApi(api_client)
    id = "id_example" # str | Unique or global ID of the work item

    # example passing only required values which don't have defaults set
    try:
        # Get work item comments
        api_response = api_instance.api_v2_work_items_id_comments_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsCommentsApi->api_v2_work_items_id_comments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the work item |

### Return type

[**[WorkItemCommentModel]**](WorkItemCommentModel.md)

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
**403** | Read permission for test library is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

