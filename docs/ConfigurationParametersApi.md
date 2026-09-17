# testit_api_client.ConfigurationParametersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_configuration_parameters_configuration_parameter_id_delete**](ConfigurationParametersApi.md#api_v2_configuration_parameters_configuration_parameter_id_delete) | **DELETE** /api/v2/configuration-parameters/{configurationParameterId} | Deletes configuration parameter
[**api_v2_configuration_parameters_configuration_parameter_id_get**](ConfigurationParametersApi.md#api_v2_configuration_parameters_configuration_parameter_id_get) | **GET** /api/v2/configuration-parameters/{configurationParameterId} | Gets configuration parameter by its identifier
[**api_v2_configuration_parameters_configuration_parameter_id_put**](ConfigurationParametersApi.md#api_v2_configuration_parameters_configuration_parameter_id_put) | **PUT** /api/v2/configuration-parameters/{configurationParameterId} | Updates configuration parameter
[**api_v2_configuration_parameters_post**](ConfigurationParametersApi.md#api_v2_configuration_parameters_post) | **POST** /api/v2/configuration-parameters | Creates new configuration parameter
[**api_v2_configuration_parameters_search_post**](ConfigurationParametersApi.md#api_v2_configuration_parameters_search_post) | **POST** /api/v2/configuration-parameters/search | Searches for configuration parameters


# **api_v2_configuration_parameters_configuration_parameter_id_delete**
> api_v2_configuration_parameters_configuration_parameter_id_delete(configuration_parameter_id)

Deletes configuration parameter

### Example

* Api Key Authentication (PrivateToken):
* Api Key Authentication (Identity.Application):

```python
import time
import testit_api_client
from testit_api_client.api import configuration_parameters_api
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

# Configure API key authorization: PrivateToken
configuration.api_key['PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PrivateToken'] = 'Bearer'

# Configure API key authorization: Identity.Application
configuration.api_key['Identity.Application'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Identity.Application'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_parameters_api.ConfigurationParametersApi(api_client)
    configuration_parameter_id = "configurationParameterId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deletes configuration parameter
        api_instance.api_v2_configuration_parameters_configuration_parameter_id_delete(configuration_parameter_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationParametersApi->api_v2_configuration_parameters_configuration_parameter_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_parameter_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[PrivateToken](../README.md#PrivateToken), [Identity.Application](../README.md#Identity.Application)

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

# **api_v2_configuration_parameters_configuration_parameter_id_get**
> ConfigurationParameterApiResult api_v2_configuration_parameters_configuration_parameter_id_get(configuration_parameter_id)

Gets configuration parameter by its identifier

### Example

* Api Key Authentication (PrivateToken):
* Api Key Authentication (Identity.Application):

```python
import time
import testit_api_client
from testit_api_client.api import configuration_parameters_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.configuration_parameter_api_result import ConfigurationParameterApiResult
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

# Configure API key authorization: PrivateToken
configuration.api_key['PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PrivateToken'] = 'Bearer'

# Configure API key authorization: Identity.Application
configuration.api_key['Identity.Application'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Identity.Application'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_parameters_api.ConfigurationParametersApi(api_client)
    configuration_parameter_id = "configurationParameterId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Gets configuration parameter by its identifier
        api_response = api_instance.api_v2_configuration_parameters_configuration_parameter_id_get(configuration_parameter_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationParametersApi->api_v2_configuration_parameters_configuration_parameter_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_parameter_id** | **str**|  |

### Return type

[**ConfigurationParameterApiResult**](ConfigurationParameterApiResult.md)

### Authorization

[PrivateToken](../README.md#PrivateToken), [Identity.Application](../README.md#Identity.Application)

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

# **api_v2_configuration_parameters_configuration_parameter_id_put**
> api_v2_configuration_parameters_configuration_parameter_id_put(configuration_parameter_id)

Updates configuration parameter

### Example

* Api Key Authentication (PrivateToken):
* Api Key Authentication (Identity.Application):

```python
import time
import testit_api_client
from testit_api_client.api import configuration_parameters_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_configuration_parameters_post_request import ApiV2ConfigurationParametersPostRequest
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

# Configure API key authorization: PrivateToken
configuration.api_key['PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PrivateToken'] = 'Bearer'

# Configure API key authorization: Identity.Application
configuration.api_key['Identity.Application'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Identity.Application'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_parameters_api.ConfigurationParametersApi(api_client)
    configuration_parameter_id = "configurationParameterId_example" # str | 
    api_v2_configuration_parameters_post_request = ApiV2ConfigurationParametersPostRequest(None) # ApiV2ConfigurationParametersPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates configuration parameter
        api_instance.api_v2_configuration_parameters_configuration_parameter_id_put(configuration_parameter_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationParametersApi->api_v2_configuration_parameters_configuration_parameter_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates configuration parameter
        api_instance.api_v2_configuration_parameters_configuration_parameter_id_put(configuration_parameter_id, api_v2_configuration_parameters_post_request=api_v2_configuration_parameters_post_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationParametersApi->api_v2_configuration_parameters_configuration_parameter_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_parameter_id** | **str**|  |
 **api_v2_configuration_parameters_post_request** | [**ApiV2ConfigurationParametersPostRequest**](ApiV2ConfigurationParametersPostRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[PrivateToken](../README.md#PrivateToken), [Identity.Application](../README.md#Identity.Application)

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

# **api_v2_configuration_parameters_post**
> ConfigurationParameterApiResult api_v2_configuration_parameters_post()

Creates new configuration parameter

### Example

* Api Key Authentication (PrivateToken):
* Api Key Authentication (Identity.Application):

```python
import time
import testit_api_client
from testit_api_client.api import configuration_parameters_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_configuration_parameters_post_request import ApiV2ConfigurationParametersPostRequest
from testit_api_client.model.configuration_parameter_api_result import ConfigurationParameterApiResult
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

# Configure API key authorization: PrivateToken
configuration.api_key['PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PrivateToken'] = 'Bearer'

# Configure API key authorization: Identity.Application
configuration.api_key['Identity.Application'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Identity.Application'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_parameters_api.ConfigurationParametersApi(api_client)
    api_v2_configuration_parameters_post_request = ApiV2ConfigurationParametersPostRequest(None) # ApiV2ConfigurationParametersPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates new configuration parameter
        api_response = api_instance.api_v2_configuration_parameters_post(api_v2_configuration_parameters_post_request=api_v2_configuration_parameters_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationParametersApi->api_v2_configuration_parameters_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_configuration_parameters_post_request** | [**ApiV2ConfigurationParametersPostRequest**](ApiV2ConfigurationParametersPostRequest.md)|  | [optional]

### Return type

[**ConfigurationParameterApiResult**](ConfigurationParameterApiResult.md)

### Authorization

[PrivateToken](../README.md#PrivateToken), [Identity.Application](../README.md#Identity.Application)

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

# **api_v2_configuration_parameters_search_post**
> ConfigurationParameterPreviewApiResultIReply api_v2_configuration_parameters_search_post()

Searches for configuration parameters

### Example

* Api Key Authentication (PrivateToken):
* Api Key Authentication (Identity.Application):

```python
import time
import testit_api_client
from testit_api_client.api import configuration_parameters_api
from testit_api_client.model.configuration_parameter_preview_api_result_i_reply import ConfigurationParameterPreviewApiResultIReply
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.api_v2_configuration_parameters_search_post_request import ApiV2ConfigurationParametersSearchPostRequest
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

# Configure API key authorization: PrivateToken
configuration.api_key['PrivateToken'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['PrivateToken'] = 'Bearer'

# Configure API key authorization: Identity.Application
configuration.api_key['Identity.Application'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Identity.Application'] = 'Bearer'

# Enter a context with an instance of the API client
with testit_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = configuration_parameters_api.ConfigurationParametersApi(api_client)
    api_v2_configuration_parameters_search_post_request = ApiV2ConfigurationParametersSearchPostRequest(None) # ApiV2ConfigurationParametersSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Searches for configuration parameters
        api_response = api_instance.api_v2_configuration_parameters_search_post(api_v2_configuration_parameters_search_post_request=api_v2_configuration_parameters_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationParametersApi->api_v2_configuration_parameters_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_configuration_parameters_search_post_request** | [**ApiV2ConfigurationParametersSearchPostRequest**](ApiV2ConfigurationParametersSearchPostRequest.md)|  | [optional]

### Return type

[**ConfigurationParameterPreviewApiResultIReply**](ConfigurationParameterPreviewApiResultIReply.md)

### Authorization

[PrivateToken](../README.md#PrivateToken), [Identity.Application](../README.md#Identity.Application)

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

