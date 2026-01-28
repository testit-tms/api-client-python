# testit_api_client.ExternalServicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_external_services_metadata_get**](ExternalServicesApi.md#api_v2_external_services_metadata_get) | **GET** /api/v2/external-services/metadata | Retrieves the metadata for all available external services


# **api_v2_external_services_metadata_get**
> ExternalServicesMetadataApiResult api_v2_external_services_metadata_get()

Retrieves the metadata for all available external services

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import external_services_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.external_services_metadata_api_result import ExternalServicesMetadataApiResult
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
    api_instance = external_services_api.ExternalServicesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieves the metadata for all available external services
        api_response = api_instance.api_v2_external_services_metadata_get()
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ExternalServicesApi->api_v2_external_services_metadata_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ExternalServicesMetadataApiResult**](ExternalServicesMetadataApiResult.md)

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

