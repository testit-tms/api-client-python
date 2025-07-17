# testit_api_client.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_search_global_search_post**](SearchApi.md#api_v2_search_global_search_post) | **POST** /api/v2/search/globalSearch | 


# **api_v2_search_global_search_post**
> GlobalSearchResponse api_v2_search_global_search_post(global_search_request=global_search_request)





### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
from testit_api_client.models.global_search_request import GlobalSearchRequest
from testit_api_client.models.global_search_response import GlobalSearchResponse
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
    api_instance = testit_api_client.SearchApi(api_client)
    global_search_request = testit_api_client.GlobalSearchRequest() # GlobalSearchRequest |  (optional)

    try:
        api_response = api_instance.api_v2_search_global_search_post(global_search_request=global_search_request)
        print("The response of SearchApi->api_v2_search_global_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->api_v2_search_global_search_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **global_search_request** | [**GlobalSearchRequest**](GlobalSearchRequest.md)|  | [optional] 

### Return type

[**GlobalSearchResponse**](GlobalSearchResponse.md)

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

