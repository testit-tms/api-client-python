# testit_api_client.TestSuitesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_test_points_to_test_suite**](TestSuitesApi.md#add_test_points_to_test_suite) | **POST** /api/v2/testSuites/{id}/test-points | Add test-points to test suite
[**api_v2_test_suites_id_patch**](TestSuitesApi.md#api_v2_test_suites_id_patch) | **PATCH** /api/v2/testSuites/{id} | Patch test suite
[**api_v2_test_suites_id_refresh_post**](TestSuitesApi.md#api_v2_test_suites_id_refresh_post) | **POST** /api/v2/testSuites/{id}/refresh | Refresh test suite. Only dynamic test suites are supported by this method
[**api_v2_test_suites_id_work_items_post**](TestSuitesApi.md#api_v2_test_suites_id_work_items_post) | **POST** /api/v2/testSuites/{id}/workItems | Set work items for test suite
[**api_v2_test_suites_post**](TestSuitesApi.md#api_v2_test_suites_post) | **POST** /api/v2/testSuites | Create test suite
[**api_v2_test_suites_put**](TestSuitesApi.md#api_v2_test_suites_put) | **PUT** /api/v2/testSuites | Edit test suite
[**delete_test_suite**](TestSuitesApi.md#delete_test_suite) | **DELETE** /api/v2/testSuites/{id} | Delete TestSuite
[**get_configurations_by_test_suite_id**](TestSuitesApi.md#get_configurations_by_test_suite_id) | **GET** /api/v2/testSuites/{id}/configurations | Get Configurations By Id
[**get_test_points_by_id**](TestSuitesApi.md#get_test_points_by_id) | **GET** /api/v2/testSuites/{id}/testPoints | Get TestPoints By Id
[**get_test_results_by_id**](TestSuitesApi.md#get_test_results_by_id) | **GET** /api/v2/testSuites/{id}/testResults | Get TestResults By Id
[**get_test_suite_by_id**](TestSuitesApi.md#get_test_suite_by_id) | **GET** /api/v2/testSuites/{id} | Get TestSuite by Id
[**search_work_items**](TestSuitesApi.md#search_work_items) | **POST** /api/v2/testSuites/{id}/workItems/search | Search WorkItems
[**set_configurations_by_test_suite_id**](TestSuitesApi.md#set_configurations_by_test_suite_id) | **POST** /api/v2/testSuites/{id}/configurations | Set Configurations By TestSuite Id


# **add_test_points_to_test_suite**
> add_test_points_to_test_suite(id, work_item_select_model=work_item_select_model)

Add test-points to test suite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_select_model import WorkItemSelectModel
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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = '1ed608bf-8ac9-4ffd-b91e-ebdbbdce6132' # str | Test suite internal identifier
    work_item_select_model = testit_api_client.WorkItemSelectModel() # WorkItemSelectModel | Filter object to retrieve work items for test-suite's project (optional)

    try:
        # Add test-points to test suite
        api_instance.add_test_points_to_test_suite(id, work_item_select_model=work_item_select_model)
    except Exception as e:
        print("Exception when calling TestSuitesApi->add_test_points_to_test_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal identifier | 
 **work_item_select_model** | [**WorkItemSelectModel**](WorkItemSelectModel.md)| Filter object to retrieve work items for test-suite&#39;s project | [optional] 

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
**204** | Successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan is required |  -  |
**404** | Test suite with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Shared steps cannot be added to test suite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_suites_id_patch**
> api_v2_test_suites_id_patch(id, operation=operation)

Patch test suite

See <a href=\"https://www.rfc-editor.org/rfc/rfc6902\" target=\"_blank\">RFC 6902: JavaScript Object Notation (JSON) Patch</a> for details

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.operation import Operation
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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = 'id_example' # str | Test Suite internal (UUID) identifier
    operation = [testit_api_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch test suite
        api_instance.api_v2_test_suites_id_patch(id, operation=operation)
    except Exception as e:
        print("Exception when calling TestSuitesApi->api_v2_test_suites_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test Suite internal (UUID) identifier | 
 **operation** | [**List[Operation]**](Operation.md)|  | [optional] 

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
**403** | Update permission for test suite is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_suites_id_refresh_post**
> api_v2_test_suites_id_refresh_post(id)

Refresh test suite. Only dynamic test suites are supported by this method

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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = 'id_example' # str | Test Suite internal (UUID) identifier

    try:
        # Refresh test suite. Only dynamic test suites are supported by this method
        api_instance.api_v2_test_suites_id_refresh_post(id)
    except Exception as e:
        print("Exception when calling TestSuitesApi->api_v2_test_suites_id_refresh_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test Suite internal (UUID) identifier | 

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
**403** | Update permission for test suite is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_suites_id_work_items_post**
> api_v2_test_suites_id_work_items_post(id, request_body=request_body)

Set work items for test suite

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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = 'id_example' # str | Unique ID of the test suite
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Set work items for test suite
        api_instance.api_v2_test_suites_id_work_items_post(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling TestSuitesApi->api_v2_test_suites_id_work_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique ID of the test suite | 
 **request_body** | [**List[str]**](str.md)|  | [optional] 

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
**403** | Update permission for test plan is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_suites_post**
> TestSuiteV2GetModel api_v2_test_suites_post(test_suite_v2_post_model=test_suite_v2_post_model)

Create test suite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_suite_v2_get_model import TestSuiteV2GetModel
from testit_api_client.models.test_suite_v2_post_model import TestSuiteV2PostModel
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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    test_suite_v2_post_model = testit_api_client.TestSuiteV2PostModel() # TestSuiteV2PostModel |  (optional)

    try:
        # Create test suite
        api_response = api_instance.api_v2_test_suites_post(test_suite_v2_post_model=test_suite_v2_post_model)
        print("The response of TestSuitesApi->api_v2_test_suites_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->api_v2_test_suites_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_suite_v2_post_model** | [**TestSuiteV2PostModel**](TestSuiteV2PostModel.md)|  | [optional] 

### Return type

[**TestSuiteV2GetModel**](TestSuiteV2GetModel.md)

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
**403** | Update permission for test plan is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_suites_put**
> api_v2_test_suites_put(test_suite_v2_put_model=test_suite_v2_put_model)

Edit test suite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_suite_v2_put_model import TestSuiteV2PutModel
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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    test_suite_v2_put_model = testit_api_client.TestSuiteV2PutModel() # TestSuiteV2PutModel |  (optional)

    try:
        # Edit test suite
        api_instance.api_v2_test_suites_put(test_suite_v2_put_model=test_suite_v2_put_model)
    except Exception as e:
        print("Exception when calling TestSuitesApi->api_v2_test_suites_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_suite_v2_put_model** | [**TestSuiteV2PutModel**](TestSuiteV2PutModel.md)|  | [optional] 

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
**403** | Update permission for test plan is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_suite**
> delete_test_suite(id)

Delete TestSuite

 Use case   User sets test suite identifier   User runs method execution   System search test suite by identifier   System deletes test suite   System returns no content response

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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test suite internal (guid format) identifier\"

    try:
        # Delete TestSuite
        api_instance.delete_test_suite(id)
    except Exception as e:
        print("Exception when calling TestSuitesApi->delete_test_suite: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; | 

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
**403** | Delete permission for test plan required |  -  |
**404** |  Can&#39;t find a TestSuite with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configurations_by_test_suite_id**
> List[ConfigurationModel] get_configurations_by_test_suite_id(id)

Get Configurations By Id

 Use case   User sets test suite identifier   User runs method execution   System search test suite by identifier   System search test points related to the test suite   System search configurations related to the test points   System returns configurations array

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.configuration_model import ConfigurationModel
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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test suite internal (guid format) identifier\"

    try:
        # Get Configurations By Id
        api_response = api_instance.get_configurations_by_test_suite_id(id)
        print("The response of TestSuitesApi->get_configurations_by_test_suite_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->get_configurations_by_test_suite_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; | 

### Return type

[**List[ConfigurationModel]**](ConfigurationModel.md)

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
**403** | Read permission for test plan required |  -  |
**404** |  Can&#39;t find a TestSuite with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_points_by_id**
> List[TestPointByTestSuiteModel] get_test_points_by_id(id)

Get TestPoints By Id

 Use case   User sets test suite identifier   User runs method execution   System search test suite by identifier   System search test points related to the test suite   System returns test points array

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_point_by_test_suite_model import TestPointByTestSuiteModel
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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test suite internal (guid format) identifier\"

    try:
        # Get TestPoints By Id
        api_response = api_instance.get_test_points_by_id(id)
        print("The response of TestSuitesApi->get_test_points_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->get_test_points_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; | 

### Return type

[**List[TestPointByTestSuiteModel]**](TestPointByTestSuiteModel.md)

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
**403** | Read permission for test plan required |  -  |
**404** |  Can&#39;t find a TestSuite with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_results_by_id**
> List[TestResultV2ShortModel] get_test_results_by_id(id)

Get TestResults By Id

 Use case   User sets test suite identifier   User runs method execution   System search test suite by identifier   System search test points related to the test suite   System search test results related to the test points   System returns test results array

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_result_v2_short_model import TestResultV2ShortModel
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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test suite internal (guid format) identifier\"

    try:
        # Get TestResults By Id
        api_response = api_instance.get_test_results_by_id(id)
        print("The response of TestSuitesApi->get_test_results_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->get_test_results_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; | 

### Return type

[**List[TestResultV2ShortModel]**](TestResultV2ShortModel.md)

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
**403** | Read permission for test plan required |  -  |
**404** |  Can&#39;t find a TestSuite with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_suite_by_id**
> TestSuiteV2GetModel get_test_suite_by_id(id)

Get TestSuite by Id

 Use case   User sets test suite identifier   User runs method execution   System search test suite by identifier   System returns test suite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_suite_v2_get_model import TestSuiteV2GetModel
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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test suite internal (guid format) identifier\"

    try:
        # Get TestSuite by Id
        api_response = api_instance.get_test_suite_by_id(id)
        print("The response of TestSuitesApi->get_test_suite_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->get_test_suite_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; | 

### Return type

[**TestSuiteV2GetModel**](TestSuiteV2GetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** |  Can&#39;t find a TestSuite with id! |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test plan required |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_work_items**
> List[WorkItemShortModel] search_work_items(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, test_suite_work_items_search_model=test_suite_work_items_search_model)

Search WorkItems

 Use case   User sets test suite identifier   [Optional] User sets filter   User runs method execution   System search test suite by identifier   System search test points related to the test suite   System search work items related to the test points                         [Optional] User sets filter, system applies filter                     System returns work items array

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_suite_work_items_search_model import TestSuiteWorkItemsSearchModel
from testit_api_client.models.work_item_short_model import WorkItemShortModel
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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test suite internal (guid format) identifier\"
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    test_suite_work_items_search_model = testit_api_client.TestSuiteWorkItemsSearchModel() # TestSuiteWorkItemsSearchModel |  (optional)

    try:
        # Search WorkItems
        api_response = api_instance.search_work_items(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, test_suite_work_items_search_model=test_suite_work_items_search_model)
        print("The response of TestSuitesApi->search_work_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestSuitesApi->search_work_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; | 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **test_suite_work_items_search_model** | [**TestSuiteWorkItemsSearchModel**](TestSuiteWorkItemsSearchModel.md)|  | [optional] 

### Return type

[**List[WorkItemShortModel]**](WorkItemShortModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test plan required |  -  |
**404** | Can&#39;t find a TestSuite with id! |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configurations_by_test_suite_id**
> set_configurations_by_test_suite_id(id, request_body=request_body)

Set Configurations By TestSuite Id

 Use case   User sets test suite identifier   User sets collection of configuration identifiers   User runs method execution   System search test suite by identifier   System search test points related to the test suite   System search configuration   System restores(if exist) or creates test points with listed configuration   System returns no content response

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
    api_instance = testit_api_client.TestSuitesApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test suite internal (guid format) identifier\"
    request_body = ['request_body_example'] # List[str] | Collection of configuration identifiers\" (optional)

    try:
        # Set Configurations By TestSuite Id
        api_instance.set_configurations_by_test_suite_id(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling TestSuitesApi->set_configurations_by_test_suite_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; | 
 **request_body** | [**List[str]**](str.md)| Collection of configuration identifiers\&quot; | [optional] 

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
**204** | Successful operation |  -  |
**400** |  Some of Configurations do not exist in the project, or they are not active |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**404** |  Can&#39;t find a TestSuite with id |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

