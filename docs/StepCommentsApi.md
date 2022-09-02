# testit_api_client.StepCommentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_step_comments_id_get**](StepCommentsApi.md#api_v2_step_comments_id_get) | **GET** /api/v2/stepComments/{id} | Get StepComment by internal ID


# **api_v2_step_comments_id_get**
> StepCommentModel api_v2_step_comments_id_get(id)

Get StepComment by internal ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import step_comments_api
from testit_api_client.model.step_comment_model import StepCommentModel
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
    api_instance = step_comments_api.StepCommentsApi(api_client)
    id = "id_example" # str | StepComment internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get StepComment by internal ID
        api_response = api_instance.api_v2_step_comments_id_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling StepCommentsApi->api_v2_step_comments_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| StepComment internal (UUID) identifier |

### Return type

[**StepCommentModel**](StepCommentModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | Can&#39;t find a StepComment with id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

