# testit_api_client.TestSuitesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_test_points_to_test_suite**](TestSuitesApi.md#add_test_points_to_test_suite) | **POST** /api/v2/testSuites/{id}/test-points | Add test-points to test suite
[**api_v2_test_suites_id_patch**](TestSuitesApi.md#api_v2_test_suites_id_patch) | **PATCH** /api/v2/testSuites/{id} | Patch test suite
[**api_v2_test_suites_id_refresh_post**](TestSuitesApi.md#api_v2_test_suites_id_refresh_post) | **POST** /api/v2/testSuites/{id}/refresh | Refresh test suite. Only dynamic test suites are supported by this method
[**create_test_suite**](TestSuitesApi.md#create_test_suite) | **POST** /api/v2/testSuites | Create TestSuite
[**delete_test_suite**](TestSuitesApi.md#delete_test_suite) | **DELETE** /api/v2/testSuites/{id} | Delete TestSuite
[**get_configurations_by_test_suite_id**](TestSuitesApi.md#get_configurations_by_test_suite_id) | **GET** /api/v2/testSuites/{id}/configurations | Get Configurations By Id
[**get_test_points_by_id**](TestSuitesApi.md#get_test_points_by_id) | **GET** /api/v2/testSuites/{id}/testPoints | Get TestPoints By Id
[**get_test_results_by_id**](TestSuitesApi.md#get_test_results_by_id) | **GET** /api/v2/testSuites/{id}/testResults | Get TestResults By Id
[**get_test_suite_by_id**](TestSuitesApi.md#get_test_suite_by_id) | **GET** /api/v2/testSuites/{id} | Get TestSuite by Id
[**get_work_items_by_id**](TestSuitesApi.md#get_work_items_by_id) | **GET** /api/v2/testSuites/{id}/workItems | 
[**search_work_items**](TestSuitesApi.md#search_work_items) | **POST** /api/v2/testSuites/{id}/workItems/search | Search WorkItems
[**set_configurations_by_test_suite_id**](TestSuitesApi.md#set_configurations_by_test_suite_id) | **POST** /api/v2/testSuites/{id}/configurations | Set Configurations By TestSuite Id
[**set_work_items_by_test_suite_id**](TestSuitesApi.md#set_work_items_by_test_suite_id) | **POST** /api/v2/testSuites/{id}/workItems | Set WorkItems By TestSuite Id
[**update_test_suite**](TestSuitesApi.md#update_test_suite) | **PUT** /api/v2/testSuites | Update TestSuite


# **add_test_points_to_test_suite**
> add_test_points_to_test_suite(id)

Add test-points to test suite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
from testit_api_client.model.work_item_select_model import WorkItemSelectModel
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "1ed608bf-8ac9-4ffd-b91e-ebdbbdce6132" # str | Test suite internal identifier
    work_item_select_model = WorkItemSelectModel(
        filter=WorkItemFilterModel(
            name_or_id="name_or_id_example",
            include_ids=[
                "include_ids_example",
            ],
            exclude_ids=[
                "exclude_ids_example",
            ],
            name="name_example",
            ids=[
                "ids_example",
            ],
            global_ids=[
                1,
            ],
            attributes={
                "key": [
                    "key_example",
                ],
            },
            is_deleted=True,
            project_ids=[
                "project_ids_example",
            ],
            section_ids=[
                "section_ids_example",
            ],
            created_by_ids=[
                "created_by_ids_example",
            ],
            modified_by_ids=[
                "modified_by_ids_example",
            ],
            states=[
                WorkItemStates("NeedsWork"),
            ],
            priorities=[
                WorkItemPriorityModel("Lowest"),
            ],
            types=[
                WorkItemEntityTypes("TestCases"),
            ],
            created_date=DateTimeRangeSelectorModel(
                _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            modified_date=DateTimeRangeSelectorModel(
                _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            duration=Int32RangeSelectorModel(
                _from=1,
                to=1,
            ),
            is_automated=True,
            tags=[
                "tags_example",
            ],
            auto_test_ids=[
                "auto_test_ids_example",
            ],
        ),
        extraction_model=WorkItemsExtractionModel(
            ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
            section_ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
            project_ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
        ),
    ) # WorkItemSelectModel | Filter object to retrieve work items for test-suite's project (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add test-points to test suite
        api_instance.add_test_points_to_test_suite(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->add_test_points_to_test_suite: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add test-points to test suite
        api_instance.add_test_points_to_test_suite(id, work_item_select_model=work_item_select_model)
    except testit_api_client.ApiException as e:
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
**422** | Shared steps cannot be added to test suite |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_suites_id_patch**
> api_v2_test_suites_id_patch(id)

Patch test suite

See <a href=\"https://www.rfc-editor.org/rfc/rfc6902\" target=\"_blank\">RFC 6902: JavaScript Object Notation (JSON) Patch</a> for details

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
from testit_api_client.model.problem_details import ProblemDetails
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "id_example" # str | Test Suite internal (UUID) identifier
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
        # Patch test suite
        api_instance.api_v2_test_suites_id_patch(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->api_v2_test_suites_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch test suite
        api_instance.api_v2_test_suites_id_patch(id, operation=operation)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->api_v2_test_suites_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test Suite internal (UUID) identifier |
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
**403** | Update permission for test suite is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_suites_id_refresh_post**
> api_v2_test_suites_id_refresh_post(id)

Refresh test suite. Only dynamic test suites are supported by this method

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "id_example" # str | Test Suite internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Refresh test suite. Only dynamic test suites are supported by this method
        api_instance.api_v2_test_suites_id_refresh_post(id)
    except testit_api_client.ApiException as e:
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
**403** | Update permission for test suite is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_test_suite**
> TestSuiteV2GetModel create_test_suite()

Create TestSuite

<br>Use case  <br>User sets test suite model (listed in request parameters)  <br>User runs method execution  <br>System creates test suite  <br>System returns test suite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_suite_v2_get_model import TestSuiteV2GetModel
from testit_api_client.model.test_suite_v2_post_model import TestSuiteV2PostModel
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    test_suite_v2_post_model = TestSuiteV2PostModel(
        parent_id="7ade0007-e3a1-4df6-9680-a5eb939c2fec",
        test_plan_id="7ade0007-e3a1-4df6-9680-a5eb939c2fec",
        name="base test suite",
        type=TestSuiteType("Custom"),
        save_structure=True,
    ) # TestSuiteV2PostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create TestSuite
        api_response = api_instance.create_test_suite(test_suite_v2_post_model=test_suite_v2_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->create_test_suite: %s\n" % e)
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
**401** | Unauthorized |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestPlan with id  &lt;br&gt;Can&#39;t find a TestSuite with id |  -  |
**403** | Update permission for test plan required |  -  |
**201** | Successful operation |  -  |
**400** | &lt;br&gt;Field is required  &lt;br&gt;Suite with Id creates loop! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_test_suite**
> delete_test_suite(id)

Delete TestSuite

<br>Use case  <br>User sets test suite identifier  <br>User runs method execution  <br>System search test suite by identifier  <br>System deletes test suite  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test suite internal (guid format) identifier\"

    # example passing only required values which don't have defaults set
    try:
        # Delete TestSuite
        api_instance.delete_test_suite(id)
    except testit_api_client.ApiException as e:
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
**401** | Unauthorized |  -  |
**403** | Delete permission for test plan required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestSuite with id |  -  |
**204** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configurations_by_test_suite_id**
> [ConfigurationModel] get_configurations_by_test_suite_id(id)

Get Configurations By Id

<br>Use case  <br>User sets test suite identifier  <br>User runs method execution  <br>System search test suite by identifier  <br>System search test points related to the test suite  <br>System search configurations related to the test points  <br>System returns configurations array

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.configuration_model import ConfigurationModel
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test suite internal (guid format) identifier\"

    # example passing only required values which don't have defaults set
    try:
        # Get Configurations By Id
        api_response = api_instance.get_configurations_by_test_suite_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->get_configurations_by_test_suite_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; |

### Return type

[**[ConfigurationModel]**](ConfigurationModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | &lt;br&gt;Can&#39;t find a TestSuite with id! |  -  |
**403** | Read permission for test plan required |  -  |
**401** | Unauthorized |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_points_by_id**
> [TestPointByTestSuiteModel] get_test_points_by_id(id)

Get TestPoints By Id

<br>Use case  <br>User sets test suite identifier  <br>User runs method execution  <br>System search test suite by identifier  <br>System search test points related to the test suite  <br>System returns test points array

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_point_by_test_suite_model import TestPointByTestSuiteModel
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test suite internal (guid format) identifier\"

    # example passing only required values which don't have defaults set
    try:
        # Get TestPoints By Id
        api_response = api_instance.get_test_points_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->get_test_points_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; |

### Return type

[**[TestPointByTestSuiteModel]**](TestPointByTestSuiteModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**401** | Unauthorized |  -  |
**403** | Read permission for test plan required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestSuite with id! |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_results_by_id**
> [TestResultV2ShortModel] get_test_results_by_id(id)

Get TestResults By Id

<br>Use case  <br>User sets test suite identifier  <br>User runs method execution  <br>System search test suite by identifier  <br>System search test points related to the test suite  <br>System search test results related to the test points  <br>System returns test results array

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_result_v2_short_model import TestResultV2ShortModel
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test suite internal (guid format) identifier\"

    # example passing only required values which don't have defaults set
    try:
        # Get TestResults By Id
        api_response = api_instance.get_test_results_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->get_test_results_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; |

### Return type

[**[TestResultV2ShortModel]**](TestResultV2ShortModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Read permission for test plan required |  -  |
**401** | Unauthorized |  -  |
**200** | Successful operation |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestSuite with id! |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_suite_by_id**
> TestSuiteV2GetModel get_test_suite_by_id(id)

Get TestSuite by Id

<br>Use case  <br>User sets test suite identifier  <br>User runs method execution  <br>System search test suite by identifier  <br>System returns test suite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_suite_v2_get_model import TestSuiteV2GetModel
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test suite internal (guid format) identifier\"

    # example passing only required values which don't have defaults set
    try:
        # Get TestSuite by Id
        api_response = api_instance.get_test_suite_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**404** | &lt;br&gt;Can&#39;t find a TestSuite with id! |  -  |
**403** | Read permission for test plan required |  -  |
**401** | Unauthorized |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_items_by_id**
> [WorkItemShortModel] get_work_items_by_id(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.work_item_short_model import WorkItemShortModel
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "id_example" # str | 
    is_deleted = False # bool |  (optional) if omitted the server will use the default value of False
    tag_names = [
        "tagNames_example",
    ] # [str] |  (optional)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_work_items_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->get_work_items_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_work_items_by_id(id, is_deleted=is_deleted, tag_names=tag_names, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->get_work_items_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **is_deleted** | **bool**|  | [optional] if omitted the server will use the default value of False
 **tag_names** | **[str]**|  | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[WorkItemShortModel]**](WorkItemShortModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_work_items**
> [WorkItemShortModel] search_work_items(id)

Search WorkItems

<br>Use case  <br>User sets test suite identifier  <br>[Optional] User sets filter  <br>User runs method execution  <br>System search test suite by identifier  <br>System search test points related to the test suite  <br>System search work items related to the test points  <br>                      [Optional] User sets filter, system applies filter                     <br>System returns work items array

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
from testit_api_client.model.test_suite_work_items_search_model import TestSuiteWorkItemsSearchModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.work_item_short_model import WorkItemShortModel
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test suite internal (guid format) identifier\"
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    test_suite_work_items_search_model = TestSuiteWorkItemsSearchModel(
        name="name_example",
        global_ids=[
            1,
        ],
        section_ids=[
            "section_ids_example",
        ],
        priorities=[
            WorkItemPriorityModel("Lowest"),
        ],
        is_automated=True,
        states=[
            WorkItemStates("NeedsWork"),
        ],
        duration=Int32RangeSelectorModel(
            _from=1,
            to=1,
        ),
        created_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        modified_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        created_by_ids=[
            "created_by_ids_example",
        ],
        modified_by_ids=[
            "modified_by_ids_example",
        ],
        attributes={
            "key": [
                "key_example",
            ],
        },
        is_deleted=True,
        tag_names=[
            "tag_names_example",
        ],
        entity_types=[
            "entity_types_example",
        ],
    ) # TestSuiteWorkItemsSearchModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search WorkItems
        api_response = api_instance.search_work_items(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->search_work_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search WorkItems
        api_response = api_instance.search_work_items(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, test_suite_work_items_search_model=test_suite_work_items_search_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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

[**[WorkItemShortModel]**](WorkItemShortModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | &lt;br&gt;Can&#39;t find a TestSuite with id! |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test plan required |  -  |
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_configurations_by_test_suite_id**
> set_configurations_by_test_suite_id(id)

Set Configurations By TestSuite Id

<br>Use case  <br>User sets test suite identifier  <br>User sets collection of configuration identifiers  <br>User runs method execution  <br>System search test suite by identifier  <br>System search test points related to the test suite  <br>System search configuration  <br>System restores(if exist) or creates test points with listed configuration  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test suite internal (guid format) identifier\"
    request_body = [
        "request_body_example",
    ] # [str] | Collection of configuration identifiers\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set Configurations By TestSuite Id
        api_instance.set_configurations_by_test_suite_id(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->set_configurations_by_test_suite_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set Configurations By TestSuite Id
        api_instance.set_configurations_by_test_suite_id(id, request_body=request_body)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->set_configurations_by_test_suite_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; |
 **request_body** | **[str]**| Collection of configuration identifiers\&quot; | [optional]

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
**404** | &lt;br&gt;Can&#39;t find a TestSuite with id |  -  |
**204** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test plan required |  -  |
**400** | &lt;br&gt;Some of Configurations do not exist in the project, or they are not active |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_work_items_by_test_suite_id**
> set_work_items_by_test_suite_id(id)

Set WorkItems By TestSuite Id

<br>Use case  <br>User sets test suite identifier  <br>User sets collection of work items identifiers  <br>User runs method execution  <br>System search test suite by identifier  <br>System search test points related to the test suite  <br>System search work items  <br>System restores(if exist) or creates test points with listed work items  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test suite internal (guid format) identifier\"
    request_body = [
        "request_body_example",
    ] # [str] | Collection of work item identifiers\" (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set WorkItems By TestSuite Id
        api_instance.set_work_items_by_test_suite_id(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->set_work_items_by_test_suite_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set WorkItems By TestSuite Id
        api_instance.set_work_items_by_test_suite_id(id, request_body=request_body)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->set_work_items_by_test_suite_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test suite internal (guid format) identifier\&quot; |
 **request_body** | **[str]**| Collection of work item identifiers\&quot; | [optional]

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
**403** | Update permission for test plan required |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestSuite with id  &lt;br&gt;Some of WorkItems does not exist or deleted |  -  |
**422** | &lt;br&gt;can&#39;t put a SharedStep in the TestSuite  &lt;br&gt;ProjectId must be the same for TestSuites |  -  |
**400** | Bad Request |  -  |
**204** | Successful operation |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_test_suite**
> update_test_suite()

Update TestSuite

<br>Use case  <br>User sets test suite model (listed in request parameters)  <br>User runs method execution  <br>System updates test suite  <br>System returns test suite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_suites_api
from testit_api_client.model.test_suite_v2_put_model import TestSuiteV2PutModel
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
    api_instance = test_suites_api.TestSuitesApi(api_client)
    test_suite_v2_put_model = TestSuiteV2PutModel(
        id="id_example",
        parent_id="parent_id_example",
        name="name_example",
        is_deleted=True,
    ) # TestSuiteV2PutModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update TestSuite
        api_instance.update_test_suite(test_suite_v2_put_model=test_suite_v2_put_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestSuitesApi->update_test_suite: %s\n" % e)
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
**403** | Update permission for test plan required |  -  |
**204** | Successful operation |  -  |
**400** | &lt;br&gt;Field is required  &lt;br&gt;Suite with Id creates loop! |  -  |
**401** | Unauthorized |  -  |
**404** | &lt;br&gt;Can&#39;t find a TestPlan with id  &lt;br&gt;Can&#39;t find a TestSuite with id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

