# testit_api_client.ParametersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_parameters_bulk_post**](ParametersApi.md#api_v2_parameters_bulk_post) | **POST** /api/v2/parameters/bulk | Create multiple parameters
[**api_v2_parameters_bulk_put**](ParametersApi.md#api_v2_parameters_bulk_put) | **PUT** /api/v2/parameters/bulk | Update multiple parameters
[**api_v2_parameters_groups_get**](ParametersApi.md#api_v2_parameters_groups_get) | **GET** /api/v2/parameters/groups | Get parameters as group
[**api_v2_parameters_key_name_name_exists_get**](ParametersApi.md#api_v2_parameters_key_name_name_exists_get) | **GET** /api/v2/parameters/key/name/{name}/exists | Check existence parameter key in system
[**api_v2_parameters_key_values_get**](ParametersApi.md#api_v2_parameters_key_values_get) | **GET** /api/v2/parameters/{key}/values | Get all parameter key values
[**api_v2_parameters_keys_get**](ParametersApi.md#api_v2_parameters_keys_get) | **GET** /api/v2/parameters/keys | Get all parameter keys
[**api_v2_parameters_search_groups_post**](ParametersApi.md#api_v2_parameters_search_groups_post) | **POST** /api/v2/parameters/search/groups | Search for parameters as group
[**api_v2_parameters_search_post**](ParametersApi.md#api_v2_parameters_search_post) | **POST** /api/v2/parameters/search | Search for parameters
[**create_parameter**](ParametersApi.md#create_parameter) | **POST** /api/v2/parameters | Create parameter
[**delete_by_name**](ParametersApi.md#delete_by_name) | **DELETE** /api/v2/parameters/name/{name} | Delete parameter by name
[**delete_by_parameter_key_id**](ParametersApi.md#delete_by_parameter_key_id) | **DELETE** /api/v2/parameters/keyId/{keyId} | Delete parameters by parameter key identifier
[**delete_parameter**](ParametersApi.md#delete_parameter) | **DELETE** /api/v2/parameters/{id} | Delete parameter
[**get_all_parameters**](ParametersApi.md#get_all_parameters) | **GET** /api/v2/parameters | Get all parameters
[**get_parameter_by_id**](ParametersApi.md#get_parameter_by_id) | **GET** /api/v2/parameters/{id} | Get parameter by ID
[**update_parameter**](ParametersApi.md#update_parameter) | **PUT** /api/v2/parameters | Update parameter


# **api_v2_parameters_bulk_post**
> List[ParameterModel] api_v2_parameters_bulk_post(parameter_post_model=parameter_post_model)

Create multiple parameters

 Use case   User sets list of parameter model (listed in the request example)   User runs method execution   System creates parameters   System returns list of parameter model (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.parameter_model import ParameterModel
from testit_api_client.models.parameter_post_model import ParameterPostModel
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
    api_instance = testit_api_client.ParametersApi(api_client)
    parameter_post_model = [testit_api_client.ParameterPostModel()] # List[ParameterPostModel] |  (optional)

    try:
        # Create multiple parameters
        api_response = api_instance.api_v2_parameters_bulk_post(parameter_post_model=parameter_post_model)
        print("The response of ParametersApi->api_v2_parameters_bulk_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParametersApi->api_v2_parameters_bulk_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_post_model** | [**List[ParameterPostModel]**](ParameterPostModel.md)|  | [optional] 

### Return type

[**List[ParameterModel]**](ParameterModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  - Parameter model is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_parameters_bulk_put**
> api_v2_parameters_bulk_put(parameter_put_model=parameter_put_model)

Update multiple parameters

 Use case   User sets list of parameter model (listed in the request example)   User runs method execution   System updates parameters

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.parameter_put_model import ParameterPutModel
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
    api_instance = testit_api_client.ParametersApi(api_client)
    parameter_put_model = [testit_api_client.ParameterPutModel()] # List[ParameterPutModel] |  (optional)

    try:
        # Update multiple parameters
        api_instance.api_v2_parameters_bulk_put(parameter_put_model=parameter_put_model)
    except Exception as e:
        print("Exception when calling ParametersApi->api_v2_parameters_bulk_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_put_model** | [**List[ParameterPutModel]**](ParameterPutModel.md)|  | [optional] 

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
**400** |  - Parameter model is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | Invalid user permissions |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_parameters_groups_get**
> List[ParameterGroupModel] api_v2_parameters_groups_get(is_deleted=is_deleted, parameter_key_ids=parameter_key_ids, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get parameters as group

 Use case   User runs method execution   System search parameters   System returns parameters models as groups (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.parameter_group_model import ParameterGroupModel
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
    api_instance = testit_api_client.ParametersApi(api_client)
    is_deleted = True # bool |  (optional)
    parameter_key_ids = ['parameter_key_ids_example'] # List[str] |  (optional)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get parameters as group
        api_response = api_instance.api_v2_parameters_groups_get(is_deleted=is_deleted, parameter_key_ids=parameter_key_ids, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of ParametersApi->api_v2_parameters_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParametersApi->api_v2_parameters_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_deleted** | **bool**|  | [optional] 
 **parameter_key_ids** | [**List[str]**](str.md)|  | [optional] 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 

### Return type

[**List[ParameterGroupModel]**](ParameterGroupModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **api_v2_parameters_key_name_name_exists_get**
> bool api_v2_parameters_key_name_name_exists_get(name)

Check existence parameter key in system

 Use case   User sets name of parameter key   User runs method execution   System search parameter key   System returns the flag for the existence of the parameter key in the system

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
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
    api_instance = testit_api_client.ParametersApi(api_client)
    name = 'name_example' # str | 

    try:
        # Check existence parameter key in system
        api_response = api_instance.api_v2_parameters_key_name_name_exists_get(name)
        print("The response of ParametersApi->api_v2_parameters_key_name_name_exists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParametersApi->api_v2_parameters_key_name_name_exists_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

**bool**

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

# **api_v2_parameters_key_values_get**
> List[str] api_v2_parameters_key_values_get(key)

Get all parameter key values

 Use case   User sets parameter key (string format)   User runs method execution   System search parameter values using the key   System returns parameter

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
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
    api_instance = testit_api_client.ParametersApi(api_client)
    key = 'SomeKey' # str | Parameter key (string format)

    try:
        # Get all parameter key values
        api_response = api_instance.api_v2_parameters_key_values_get(key)
        print("The response of ParametersApi->api_v2_parameters_key_values_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParametersApi->api_v2_parameters_key_values_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Parameter key (string format) | 

### Return type

**List[str]**

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_parameters_keys_get**
> List[str] api_v2_parameters_keys_get()

Get all parameter keys

 Use case   User runs method execution   System search all parameter keys   System returns parameter keys

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
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
    api_instance = testit_api_client.ParametersApi(api_client)

    try:
        # Get all parameter keys
        api_response = api_instance.api_v2_parameters_keys_get()
        print("The response of ParametersApi->api_v2_parameters_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParametersApi->api_v2_parameters_keys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_parameters_search_groups_post**
> List[ParameterGroupModel] api_v2_parameters_search_groups_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, parameter_filter_model=parameter_filter_model)

Search for parameters as group

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.parameter_filter_model import ParameterFilterModel
from testit_api_client.models.parameter_group_model import ParameterGroupModel
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
    api_instance = testit_api_client.ParametersApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    parameter_filter_model = testit_api_client.ParameterFilterModel() # ParameterFilterModel |  (optional)

    try:
        # Search for parameters as group
        api_response = api_instance.api_v2_parameters_search_groups_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, parameter_filter_model=parameter_filter_model)
        print("The response of ParametersApi->api_v2_parameters_search_groups_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParametersApi->api_v2_parameters_search_groups_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **parameter_filter_model** | [**ParameterFilterModel**](ParameterFilterModel.md)|  | [optional] 

### Return type

[**List[ParameterGroupModel]**](ParameterGroupModel.md)

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

# **api_v2_parameters_search_post**
> List[ParameterModel] api_v2_parameters_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, parameter_filter_model=parameter_filter_model)

Search for parameters

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.parameter_filter_model import ParameterFilterModel
from testit_api_client.models.parameter_model import ParameterModel
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
    api_instance = testit_api_client.ParametersApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    parameter_filter_model = testit_api_client.ParameterFilterModel() # ParameterFilterModel |  (optional)

    try:
        # Search for parameters
        api_response = api_instance.api_v2_parameters_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, parameter_filter_model=parameter_filter_model)
        print("The response of ParametersApi->api_v2_parameters_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParametersApi->api_v2_parameters_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **parameter_filter_model** | [**ParameterFilterModel**](ParameterFilterModel.md)|  | [optional] 

### Return type

[**List[ParameterModel]**](ParameterModel.md)

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

# **create_parameter**
> ParameterModel create_parameter(parameter_post_model=parameter_post_model)

Create parameter

 Use case   User sets parameter model (listed in the request example)   User runs method execution   System creates parameter   System returns parameter model

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.parameter_model import ParameterModel
from testit_api_client.models.parameter_post_model import ParameterPostModel
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
    api_instance = testit_api_client.ParametersApi(api_client)
    parameter_post_model = testit_api_client.ParameterPostModel() # ParameterPostModel |  (optional)

    try:
        # Create parameter
        api_response = api_instance.create_parameter(parameter_post_model=parameter_post_model)
        print("The response of ParametersApi->create_parameter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParametersApi->create_parameter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_post_model** | [**ParameterPostModel**](ParameterPostModel.md)|  | [optional] 

### Return type

[**ParameterModel**](ParameterModel.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_by_name**
> delete_by_name(name)

Delete parameter by name

Deletes parameter and all it's values

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
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
    api_instance = testit_api_client.ParametersApi(api_client)
    name = 'name_example' # str | Name of the parameter

    try:
        # Delete parameter by name
        api_instance.delete_by_name(name)
    except Exception as e:
        print("Exception when calling ParametersApi->delete_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the parameter | 

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
**400** | Provided name either is empty or contains only white spaces |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Parameter is in use in iterations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_by_parameter_key_id**
> delete_by_parameter_key_id(key_id)

Delete parameters by parameter key identifier

Deletes parameter and all it's values by parameter key identifier

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
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
    api_instance = testit_api_client.ParametersApi(api_client)
    key_id = 'key_id_example' # str | Identifier of the parameter key

    try:
        # Delete parameters by parameter key identifier
        api_instance.delete_by_parameter_key_id(key_id)
    except Exception as e:
        print("Exception when calling ParametersApi->delete_by_parameter_key_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| Identifier of the parameter key | 

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
**403** | Invalid user permissions |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Parameter is in use in iterations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parameter**
> delete_parameter(id)

Delete parameter

 Use case   User sets parameter internal (guid format) identifier   System search and delete parameter   System returns deleted parameter

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
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
    api_instance = testit_api_client.ParametersApi(api_client)
    id = 'id_example' # str | Parameter internal (UUID) identifier

    try:
        # Delete parameter
        api_instance.delete_parameter(id)
    except Exception as e:
        print("Exception when calling ParametersApi->delete_parameter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Parameter internal (UUID) identifier | 

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
**200** | OK |  -  |
**404** | Not Found |  -  |
**400** |  - ID is not valid   - DTO is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**422** | Parameter is in use in iterations |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_parameters**
> List[ParameterModel] get_all_parameters(is_deleted=is_deleted, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get all parameters

 Use case   [Optional] User sets isDeleted field value   [Optional] If User sets isDeleted field value as true, System search all deleted parameters   [Optional] If User sets isDeleted field value as false, System search all parameters which are not deleted   If User did not set isDeleted field value, System search all parameters   System returns array of all found parameters(listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.parameter_model import ParameterModel
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
    api_instance = testit_api_client.ParametersApi(api_client)
    is_deleted = True # bool | If result must consist of only actual/deleted parameters (optional)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get all parameters
        api_response = api_instance.get_all_parameters(is_deleted=is_deleted, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of ParametersApi->get_all_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParametersApi->get_all_parameters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_deleted** | **bool**| If result must consist of only actual/deleted parameters | [optional] 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 

### Return type

[**List[ParameterModel]**](ParameterModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Invalid user permissions |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_by_id**
> ParameterModel get_parameter_by_id(id)

Get parameter by ID

 Use case   User sets parameter internal (guid format) identifier   User runs method execution   System search parameter using the identifier   System returns parameter

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.parameter_model import ParameterModel
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
    api_instance = testit_api_client.ParametersApi(api_client)
    id = 'id_example' # str | Parameter internal (UUID) identifier

    try:
        # Get parameter by ID
        api_response = api_instance.get_parameter_by_id(id)
        print("The response of ParametersApi->get_parameter_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParametersApi->get_parameter_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Parameter internal (UUID) identifier | 

### Return type

[**ParameterModel**](ParameterModel.md)

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
**404** | Parameter with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_parameter**
> update_parameter(parameter_put_model=parameter_put_model)

Update parameter

 Use case   User sets parameter updated properties(listed in the request example)   User runs method execution   System updated parameter using updated properties   System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.parameter_put_model import ParameterPutModel
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
    api_instance = testit_api_client.ParametersApi(api_client)
    parameter_put_model = testit_api_client.ParameterPutModel() # ParameterPutModel |  (optional)

    try:
        # Update parameter
        api_instance.update_parameter(parameter_put_model=parameter_put_model)
    except Exception as e:
        print("Exception when calling ParametersApi->update_parameter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_put_model** | [**ParameterPutModel**](ParameterPutModel.md)|  | [optional] 

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
**400** |  - ID is not valid   - DTO is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Parameter with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

