# testit_api_client.WorkItemsCommentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_work_items_comments_comment_id_delete**](WorkItemsCommentsApi.md#api_v2_work_items_comments_comment_id_delete) | **DELETE** /api/v2/workItems/comments/{commentId} | Delete WorkItem comment
[**api_v2_work_items_comments_post**](WorkItemsCommentsApi.md#api_v2_work_items_comments_post) | **POST** /api/v2/workItems/comments | Create WorkItem comment
[**api_v2_work_items_comments_put**](WorkItemsCommentsApi.md#api_v2_work_items_comments_put) | **PUT** /api/v2/workItems/comments | Update work item comment
[**api_v2_work_items_id_comments_get**](WorkItemsCommentsApi.md#api_v2_work_items_id_comments_get) | **GET** /api/v2/workItems/{id}/comments | Get work item comments


# **api_v2_work_items_comments_comment_id_delete**
> api_v2_work_items_comments_comment_id_delete(comment_id)

Delete WorkItem comment

<br>Use case  <br>User sets comment identifier  <br>User runs method execution  <br>System delete comment   <br>System returns success status code

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
    comment_id = "commentId_example" # str | 

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
 **comment_id** | **str**|  |

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
**400** | Bad Request |  -  |
**204** | Successful operation |  -  |
**403** | System admin permission required |  -  |
**401** | Unauthorized |  -  |
**404** | WorkItem is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_work_items_comments_post**
> WorkItemCommentModel api_v2_work_items_comments_post()

Create WorkItem comment

<br>Use case  <br>User sets comment properties (listed in request parameters)  <br>User runs method execution  <br>System creates comment   <br>System returns comment model (listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import work_items_comments_api
from testit_api_client.model.work_item_comment_post_model import WorkItemCommentPostModel
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
    work_item_comment_post_model = WorkItemCommentPostModel(
        text="text_example",
        work_item_id="work_item_id_example",
    ) # WorkItemCommentPostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create WorkItem comment
        api_response = api_instance.api_v2_work_items_comments_post(work_item_comment_post_model=work_item_comment_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsCommentsApi->api_v2_work_items_comments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_comment_post_model** | [**WorkItemCommentPostModel**](WorkItemCommentPostModel.md)|  | [optional]

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
from testit_api_client.model.work_item_comment_put_model import WorkItemCommentPutModel
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
    work_item_comment_put_model = WorkItemCommentPutModel(
        text="text_example",
        id="id_example",
    ) # WorkItemCommentPutModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update work item comment
        api_instance.api_v2_work_items_comments_put(work_item_comment_put_model=work_item_comment_put_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling WorkItemsCommentsApi->api_v2_work_items_comments_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_comment_put_model** | [**WorkItemCommentPutModel**](WorkItemCommentPutModel.md)|  | [optional]

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
**403** | System administrator role is required |  -  |

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
**200** | Success |  -  |
**403** | Read permission for test library is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

