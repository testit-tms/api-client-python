# testit_api_client.AIServicesAPIApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_external_services_id_ai_models_post**](AIServicesAPIApi.md#api_v2_external_services_id_ai_models_post) | **POST** /api/v2/external-services/{id}/ai/models | Ask for models with inquiry filter, cached


# **api_v2_external_services_id_ai_models_post**
> AIServiceModelApiResultReply api_v2_external_services_id_ai_models_post(id)

Ask for models with inquiry filter, cached

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import ai_services_api_api
from testit_api_client.model.ai_service_model_api_result_reply import AIServiceModelApiResultReply
from testit_api_client.model.api_v2_external_services_id_ai_models_post_request import ApiV2ExternalServicesIdAiModelsPostRequest
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
    api_instance = ai_services_api_api.AIServicesAPIApi(api_client)
    id = "id_example" # str | 
    api_v2_external_services_id_ai_models_post_request = ApiV2ExternalServicesIdAiModelsPostRequest(None) # ApiV2ExternalServicesIdAiModelsPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Ask for models with inquiry filter, cached
        api_response = api_instance.api_v2_external_services_id_ai_models_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling AIServicesAPIApi->api_v2_external_services_id_ai_models_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Ask for models with inquiry filter, cached
        api_response = api_instance.api_v2_external_services_id_ai_models_post(id, api_v2_external_services_id_ai_models_post_request=api_v2_external_services_id_ai_models_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling AIServicesAPIApi->api_v2_external_services_id_ai_models_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **api_v2_external_services_id_ai_models_post_request** | [**ApiV2ExternalServicesIdAiModelsPostRequest**](ApiV2ExternalServicesIdAiModelsPostRequest.md)|  | [optional]

### Return type

[**AIServiceModelApiResultReply**](AIServiceModelApiResultReply.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Not valid data or models request errors |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

