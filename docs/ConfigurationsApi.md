# testit_api_client.ConfigurationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_configurations_create_by_parameters_post**](ConfigurationsApi.md#api_v2_configurations_create_by_parameters_post) | **POST** /api/v2/configurations/createByParameters | Create configurations by parameters
[**api_v2_configurations_delete_bulk_post**](ConfigurationsApi.md#api_v2_configurations_delete_bulk_post) | **POST** /api/v2/configurations/delete/bulk | Delete multiple configurations
[**api_v2_configurations_id_delete**](ConfigurationsApi.md#api_v2_configurations_id_delete) | **DELETE** /api/v2/configurations/{id} | Delete configuration
[**api_v2_configurations_id_patch**](ConfigurationsApi.md#api_v2_configurations_id_patch) | **PATCH** /api/v2/configurations/{id} | Patch configuration
[**api_v2_configurations_id_purge_post**](ConfigurationsApi.md#api_v2_configurations_id_purge_post) | **POST** /api/v2/configurations/{id}/purge | Permanently delete configuration from archive
[**api_v2_configurations_id_restore_post**](ConfigurationsApi.md#api_v2_configurations_id_restore_post) | **POST** /api/v2/configurations/{id}/restore | Restore configuration from the archive
[**api_v2_configurations_purge_bulk_post**](ConfigurationsApi.md#api_v2_configurations_purge_bulk_post) | **POST** /api/v2/configurations/purge/bulk | Permanently delete multiple archived configurations
[**api_v2_configurations_put**](ConfigurationsApi.md#api_v2_configurations_put) | **PUT** /api/v2/configurations | Edit configuration
[**api_v2_configurations_restore_bulk_post**](ConfigurationsApi.md#api_v2_configurations_restore_bulk_post) | **POST** /api/v2/configurations/restore/bulk | Restore multiple configurations from the archive
[**api_v2_configurations_search_post**](ConfigurationsApi.md#api_v2_configurations_search_post) | **POST** /api/v2/configurations/search | Search for configurations
[**create_configuration**](ConfigurationsApi.md#create_configuration) | **POST** /api/v2/configurations | Create Configuration
[**get_configuration_by_id**](ConfigurationsApi.md#get_configuration_by_id) | **GET** /api/v2/configurations/{id} | Get configuration by internal or global ID


# **api_v2_configurations_create_by_parameters_post**
> [str] api_v2_configurations_create_by_parameters_post()

Create configurations by parameters

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.api_v2_configurations_create_by_parameters_post_request import ApiV2ConfigurationsCreateByParametersPostRequest
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    api_v2_configurations_create_by_parameters_post_request = ApiV2ConfigurationsCreateByParametersPostRequest(None) # ApiV2ConfigurationsCreateByParametersPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create configurations by parameters
        api_response = api_instance.api_v2_configurations_create_by_parameters_post(api_v2_configurations_create_by_parameters_post_request=api_v2_configurations_create_by_parameters_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_create_by_parameters_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_configurations_create_by_parameters_post_request** | [**ApiV2ConfigurationsCreateByParametersPostRequest**](ApiV2ConfigurationsCreateByParametersPostRequest.md)|  | [optional]

### Return type

**[str]**

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
**403** | Update permission for configuration is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configurations_delete_bulk_post**
> int api_v2_configurations_delete_bulk_post()

Delete multiple configurations

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.api_v2_configurations_purge_bulk_post_request import ApiV2ConfigurationsPurgeBulkPostRequest
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    api_v2_configurations_purge_bulk_post_request = ApiV2ConfigurationsPurgeBulkPostRequest(None) # ApiV2ConfigurationsPurgeBulkPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete multiple configurations
        api_response = api_instance.api_v2_configurations_delete_bulk_post(api_v2_configurations_purge_bulk_post_request=api_v2_configurations_purge_bulk_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_delete_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_configurations_purge_bulk_post_request** | [**ApiV2ConfigurationsPurgeBulkPostRequest**](ApiV2ConfigurationsPurgeBulkPostRequest.md)|  | [optional]

### Return type

**int**

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

# **api_v2_configurations_id_delete**
> api_v2_configurations_id_delete(id)

Delete configuration

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    id = "id_example" # str | Unique or global ID of the configuration

    # example passing only required values which don't have defaults set
    try:
        # Delete configuration
        api_instance.api_v2_configurations_id_delete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the configuration |

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
**403** | Delete permission for configurations is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configurations_id_patch**
> api_v2_configurations_id_patch(id)

Patch configuration

See <a href=\"https://www.rfc-editor.org/rfc/rfc6902\" target=\"_blank\">RFC 6902: JavaScript Object Notation (JSON) Patch</a> for details

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.operation import Operation
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    id = "id_example" # str | Unique ID of the configuration
    operation = [
        Operation(
            value=None,
            path="path_example",
            op="op_example",
            _from="_from_example",
        ),
    ] # [Operation] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Patch configuration
        api_instance.api_v2_configurations_id_patch(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch configuration
        api_instance.api_v2_configurations_id_patch(id, operation=operation)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the configuration |
 **operation** | [**[Operation]**](Operation.md)|  | [optional]

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
**403** | Update permission for configuration is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configurations_id_purge_post**
> api_v2_configurations_id_purge_post(id)

Permanently delete configuration from archive

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    id = "id_example" # str | Unique or global ID of the configuration

    # example passing only required values which don't have defaults set
    try:
        # Permanently delete configuration from archive
        api_instance.api_v2_configurations_id_purge_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_id_purge_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the configuration |

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
**403** | Full access permission for the archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configurations_id_restore_post**
> api_v2_configurations_id_restore_post(id)

Restore configuration from the archive

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    id = "id_example" # str | Unique or global ID of the configuration

    # example passing only required values which don't have defaults set
    try:
        # Restore configuration from the archive
        api_instance.api_v2_configurations_id_restore_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_id_restore_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the configuration |

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
**403** | Update permission for archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configurations_purge_bulk_post**
> int api_v2_configurations_purge_bulk_post()

Permanently delete multiple archived configurations

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.api_v2_configurations_purge_bulk_post_request import ApiV2ConfigurationsPurgeBulkPostRequest
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    api_v2_configurations_purge_bulk_post_request = ApiV2ConfigurationsPurgeBulkPostRequest(None) # ApiV2ConfigurationsPurgeBulkPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Permanently delete multiple archived configurations
        api_response = api_instance.api_v2_configurations_purge_bulk_post(api_v2_configurations_purge_bulk_post_request=api_v2_configurations_purge_bulk_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_purge_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_configurations_purge_bulk_post_request** | [**ApiV2ConfigurationsPurgeBulkPostRequest**](ApiV2ConfigurationsPurgeBulkPostRequest.md)|  | [optional]

### Return type

**int**

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
**403** | Full access permission for the archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configurations_put**
> api_v2_configurations_put()

Edit configuration

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.api_v2_configurations_put_request import ApiV2ConfigurationsPutRequest
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    api_v2_configurations_put_request = ApiV2ConfigurationsPutRequest(None) # ApiV2ConfigurationsPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit configuration
        api_instance.api_v2_configurations_put(api_v2_configurations_put_request=api_v2_configurations_put_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_configurations_put_request** | [**ApiV2ConfigurationsPutRequest**](ApiV2ConfigurationsPutRequest.md)|  | [optional]

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
**403** | Update permission for configurations is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configurations_restore_bulk_post**
> int api_v2_configurations_restore_bulk_post()

Restore multiple configurations from the archive

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.api_v2_configurations_purge_bulk_post_request import ApiV2ConfigurationsPurgeBulkPostRequest
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    api_v2_configurations_purge_bulk_post_request = ApiV2ConfigurationsPurgeBulkPostRequest(None) # ApiV2ConfigurationsPurgeBulkPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restore multiple configurations from the archive
        api_response = api_instance.api_v2_configurations_restore_bulk_post(api_v2_configurations_purge_bulk_post_request=api_v2_configurations_purge_bulk_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_restore_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_configurations_purge_bulk_post_request** | [**ApiV2ConfigurationsPurgeBulkPostRequest**](ApiV2ConfigurationsPurgeBulkPostRequest.md)|  | [optional]

### Return type

**int**

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
**403** | Update permission for archive is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_configurations_search_post**
> [ConfigurationModel] api_v2_configurations_search_post()

Search for configurations

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.configuration_model import ConfigurationModel
from testit_api_client.model.api_v2_configurations_search_post_request import ApiV2ConfigurationsSearchPostRequest
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    api_v2_configurations_search_post_request = ApiV2ConfigurationsSearchPostRequest(None) # ApiV2ConfigurationsSearchPostRequest | Model containing all the filters (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for configurations
        api_response = api_instance.api_v2_configurations_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, api_v2_configurations_search_post_request=api_v2_configurations_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->api_v2_configurations_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **api_v2_configurations_search_post_request** | [**ApiV2ConfigurationsSearchPostRequest**](ApiV2ConfigurationsSearchPostRequest.md)| Model containing all the filters | [optional]

### Return type

[**[ConfigurationModel]**](ConfigurationModel.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_configuration**
> ConfigurationModel create_configuration()

Create Configuration

  Use case    User sets configuration model (listed in the request example)    User runs method execution    System creates configuration    System returns created configuration (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.create_configuration_request import CreateConfigurationRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.configuration_model import ConfigurationModel
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    create_configuration_request = CreateConfigurationRequest(None) # CreateConfigurationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Configuration
        api_response = api_instance.create_configuration(create_configuration_request=create_configuration_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->create_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_configuration_request** | [**CreateConfigurationRequest**](CreateConfigurationRequest.md)|  | [optional]

### Return type

[**ConfigurationModel**](ConfigurationModel.md)

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
**403** | Update permission for configuration required |  -  |
**404** | Can&#39;t find project |  -  |
**409** | Configuration with the same name already exists! |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_by_id**
> ConfigurationModel get_configuration_by_id(id)

Get configuration by internal or global ID

  Use case    User sets configuration internal (guid format) or global (integer format) identifier    User runs method execution    System search configuration using the identifier    System returns configuration

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import configurations_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.configuration_model import ConfigurationModel
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
    api_instance = configurations_api.ConfigurationsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Configuration internal (guid format) or global (integer format) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get configuration by internal or global ID
        api_response = api_instance.get_configuration_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ConfigurationsApi->get_configuration_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Configuration internal (guid format) or global (integer format) identifier |

### Return type

[**ConfigurationModel**](ConfigurationModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for configuration required |  -  |
**404** | Can&#39;t find configuration with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

