# testit_api_client.TestResultsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_test_results_external_projects_external_project_id_defects_external_forms_post**](TestResultsApi.md#api_v2_test_results_external_projects_external_project_id_defects_external_forms_post) | **POST** /api/v2/testResults/external-projects/{externalProjectId}/defects/external-forms | 
[**api_v2_test_results_external_projects_external_project_id_defects_post**](TestResultsApi.md#api_v2_test_results_external_projects_external_project_id_defects_post) | **POST** /api/v2/testResults/external-projects/{externalProjectId}/defects | 
[**api_v2_test_results_id_aggregated_get**](TestResultsApi.md#api_v2_test_results_id_aggregated_get) | **GET** /api/v2/testResults/{id}/aggregated | Get test result by ID aggregated with previous results
[**api_v2_test_results_id_attachments_attachment_id_put**](TestResultsApi.md#api_v2_test_results_id_attachments_attachment_id_put) | **PUT** /api/v2/testResults/{id}/attachments/{attachmentId} | Attach file to the test result
[**api_v2_test_results_id_attachments_info_get**](TestResultsApi.md#api_v2_test_results_id_attachments_info_get) | **GET** /api/v2/testResults/{id}/attachments/info | Get test result attachments meta-information
[**api_v2_test_results_id_get**](TestResultsApi.md#api_v2_test_results_id_get) | **GET** /api/v2/testResults/{id} | Get test result by ID
[**api_v2_test_results_id_put**](TestResultsApi.md#api_v2_test_results_id_put) | **PUT** /api/v2/testResults/{id} | Edit test result by ID
[**api_v2_test_results_id_reruns_get**](TestResultsApi.md#api_v2_test_results_id_reruns_get) | **GET** /api/v2/testResults/{id}/reruns | Get reruns
[**api_v2_test_results_search_post**](TestResultsApi.md#api_v2_test_results_search_post) | **POST** /api/v2/testResults/search | Search for test results
[**api_v2_test_results_statistics_filter_post**](TestResultsApi.md#api_v2_test_results_statistics_filter_post) | **POST** /api/v2/testResults/statistics/filter | Search for test results and extract statistics
[**create_attachment**](TestResultsApi.md#create_attachment) | **POST** /api/v2/testResults/{id}/attachments | Upload and link attachment to TestResult
[**delete_attachment**](TestResultsApi.md#delete_attachment) | **DELETE** /api/v2/testResults/{id}/attachments/{attachmentId} | Remove attachment and unlink from TestResult
[**download_attachment**](TestResultsApi.md#download_attachment) | **GET** /api/v2/testResults/{id}/attachments/{attachmentId} | Get attachment of TestResult
[**get_attachment**](TestResultsApi.md#get_attachment) | **GET** /api/v2/testResults/{id}/attachments/{attachmentId}/info | Get Metadata of TestResult&#39;s attachment
[**get_attachments**](TestResultsApi.md#get_attachments) | **GET** /api/v2/testResults/{id}/attachments | Get all attachments of TestResult


# **api_v2_test_results_external_projects_external_project_id_defects_external_forms_post**
> GetExternalFormApiResult api_v2_test_results_external_projects_external_project_id_defects_external_forms_post(external_project_id, test_results_select_api_model=test_results_select_api_model)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.get_external_form_api_result import GetExternalFormApiResult
from testit_api_client.models.test_results_select_api_model import TestResultsSelectApiModel
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    external_project_id = 'external_project_id_example' # str | 
    test_results_select_api_model = testit_api_client.TestResultsSelectApiModel() # TestResultsSelectApiModel |  (optional)

    try:
        api_response = api_instance.api_v2_test_results_external_projects_external_project_id_defects_external_forms_post(external_project_id, test_results_select_api_model=test_results_select_api_model)
        print("The response of TestResultsApi->api_v2_test_results_external_projects_external_project_id_defects_external_forms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_external_projects_external_project_id_defects_external_forms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_project_id** | **str**|  | 
 **test_results_select_api_model** | [**TestResultsSelectApiModel**](TestResultsSelectApiModel.md)|  | [optional] 

### Return type

[**GetExternalFormApiResult**](GetExternalFormApiResult.md)

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

# **api_v2_test_results_external_projects_external_project_id_defects_post**
> DefectApiModel api_v2_test_results_external_projects_external_project_id_defects_post(external_project_id, create_defect_api_model=create_defect_api_model)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.create_defect_api_model import CreateDefectApiModel
from testit_api_client.models.defect_api_model import DefectApiModel
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    external_project_id = 'external_project_id_example' # str | 
    create_defect_api_model = testit_api_client.CreateDefectApiModel() # CreateDefectApiModel |  (optional)

    try:
        api_response = api_instance.api_v2_test_results_external_projects_external_project_id_defects_post(external_project_id, create_defect_api_model=create_defect_api_model)
        print("The response of TestResultsApi->api_v2_test_results_external_projects_external_project_id_defects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_external_projects_external_project_id_defects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_project_id** | **str**|  | 
 **create_defect_api_model** | [**CreateDefectApiModel**](CreateDefectApiModel.md)|  | [optional] 

### Return type

[**DefectApiModel**](DefectApiModel.md)

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

# **api_v2_test_results_id_aggregated_get**
> TestResultResponse api_v2_test_results_id_aggregated_get(id)

Get test result by ID aggregated with previous results

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_result_response import TestResultResponse
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    id = 'id_example' # str | Test result unique ID

    try:
        # Get test result by ID aggregated with previous results
        api_response = api_instance.api_v2_test_results_id_aggregated_get(id)
        print("The response of TestResultsApi->api_v2_test_results_id_aggregated_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_aggregated_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result unique ID | 

### Return type

[**TestResultResponse**](TestResultResponse.md)

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
**403** | Read permission for the test result is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_attachments_attachment_id_put**
> api_v2_test_results_id_attachments_attachment_id_put(id, attachment_id)

Attach file to the test result

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
    api_instance = testit_api_client.TestResultsApi(api_client)
    id = 'id_example' # str | Test result unique ID
    attachment_id = 'attachment_id_example' # str | Attachment unique ID

    try:
        # Attach file to the test result
        api_instance.api_v2_test_results_id_attachments_attachment_id_put(id, attachment_id)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_attachments_attachment_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result unique ID | 
 **attachment_id** | **str**| Attachment unique ID | 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Only edits from assigned user are allowed |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_attachments_info_get**
> List[AttachmentModel] api_v2_test_results_id_attachments_info_get(id)

Get test result attachments meta-information

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.attachment_model import AttachmentModel
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    id = 'id_example' # str | Test result unique ID

    try:
        # Get test result attachments meta-information
        api_response = api_instance.api_v2_test_results_id_attachments_info_get(id)
        print("The response of TestResultsApi->api_v2_test_results_id_attachments_info_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_attachments_info_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result unique ID | 

### Return type

[**List[AttachmentModel]**](AttachmentModel.md)

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
**403** | Read permission for the test result is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_get**
> TestResultResponse api_v2_test_results_id_get(id)

Get test result by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_result_response import TestResultResponse
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    id = 'id_example' # str | Test result unique ID

    try:
        # Get test result by ID
        api_response = api_instance.api_v2_test_results_id_get(id)
        print("The response of TestResultsApi->api_v2_test_results_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result unique ID | 

### Return type

[**TestResultResponse**](TestResultResponse.md)

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
**403** | Read permission for the test result is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_put**
> api_v2_test_results_id_put(id, test_result_update_v2_request=test_result_update_v2_request)

Edit test result by ID

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_result_update_v2_request import TestResultUpdateV2Request
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    id = 'id_example' # str | Test result unique ID
    test_result_update_v2_request = testit_api_client.TestResultUpdateV2Request() # TestResultUpdateV2Request |  (optional)

    try:
        # Edit test result by ID
        api_instance.api_v2_test_results_id_put(id, test_result_update_v2_request=test_result_update_v2_request)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result unique ID | 
 **test_result_update_v2_request** | [**TestResultUpdateV2Request**](TestResultUpdateV2Request.md)|  | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Only edits from assigned user are allowed |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_reruns_get**
> RerunsModel api_v2_test_results_id_reruns_get(id)

Get reruns

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.reruns_model import RerunsModel
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    id = 'id_example' # str | Test result unique ID

    try:
        # Get reruns
        api_response = api_instance.api_v2_test_results_id_reruns_get(id)
        print("The response of TestResultsApi->api_v2_test_results_id_reruns_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_reruns_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result unique ID | 

### Return type

[**RerunsModel**](RerunsModel.md)

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

# **api_v2_test_results_search_post**
> List[TestResultShortResponse] api_v2_test_results_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, test_results_filter_api_model=test_results_filter_api_model)

Search for test results

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_result_short_response import TestResultShortResponse
from testit_api_client.models.test_results_filter_api_model import TestResultsFilterApiModel
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    test_results_filter_api_model = testit_api_client.TestResultsFilterApiModel() # TestResultsFilterApiModel |  (optional)

    try:
        # Search for test results
        api_response = api_instance.api_v2_test_results_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, test_results_filter_api_model=test_results_filter_api_model)
        print("The response of TestResultsApi->api_v2_test_results_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **test_results_filter_api_model** | [**TestResultsFilterApiModel**](TestResultsFilterApiModel.md)|  | [optional] 

### Return type

[**List[TestResultShortResponse]**](TestResultShortResponse.md)

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
**403** | Read permission for all requested test runs is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_statistics_filter_post**
> TestResultsStatisticsApiResult api_v2_test_results_statistics_filter_post(test_results_filter_api_model=test_results_filter_api_model)

Search for test results and extract statistics

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.test_results_filter_api_model import TestResultsFilterApiModel
from testit_api_client.models.test_results_statistics_api_result import TestResultsStatisticsApiResult
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    test_results_filter_api_model = testit_api_client.TestResultsFilterApiModel() # TestResultsFilterApiModel |  (optional)

    try:
        # Search for test results and extract statistics
        api_response = api_instance.api_v2_test_results_statistics_filter_post(test_results_filter_api_model=test_results_filter_api_model)
        print("The response of TestResultsApi->api_v2_test_results_statistics_filter_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_statistics_filter_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_results_filter_api_model** | [**TestResultsFilterApiModel**](TestResultsFilterApiModel.md)|  | [optional] 

### Return type

[**TestResultsStatisticsApiResult**](TestResultsStatisticsApiResult.md)

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
**403** | Read permission for all requested test runs is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_attachment**
> create_attachment(id, file=file)

Upload and link attachment to TestResult

 Use case   User sets testResultId   User attaches a file   System creates attachment and links it to the test result   System returns attachment identifier

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
    api_instance = testit_api_client.TestResultsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test result internal identifier (guid format)
    file = None # bytearray | Select file (optional)

    try:
        # Upload and link attachment to TestResult
        api_instance.create_attachment(id, file=file)
    except Exception as e:
        print("Exception when calling TestResultsApi->create_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result internal identifier (guid format) | 
 **file** | **bytearray**| Select file | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**413** | Multipart body length limit exceeded (default constraint is one gigabyte) |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**404** |  |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |
**200** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attachment**
> delete_attachment(id, attachment_id)

Remove attachment and unlink from TestResult

 Use case   User sets testResultId and attachmentId   User attaches a file   User runs method execution   System deletes attachment and unlinks it from the test result   System returns attachment identifier

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
    api_instance = testit_api_client.TestResultsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test result internal identifier (guid format)
    attachment_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Attachment internal identifier (guid format)

    try:
        # Remove attachment and unlink from TestResult
        api_instance.delete_attachment(id, attachment_id)
    except Exception as e:
        print("Exception when calling TestResultsApi->delete_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result internal identifier (guid format) | 
 **attachment_id** | **str**| Attachment internal identifier (guid format) | 

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
**403** | Update permission for test result required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_attachment**
> download_attachment(attachment_id, id, width=width, height=height, resize_type=resize_type, background_color=background_color, preview=preview)

Get attachment of TestResult

 Use case   User sets attachmentId and testResultId   [Optional] User sets resize configuration   User runs method execution   System search attachments by the attachmentId and the testResultId                         [Optional] If resize configuration is set, System resizes the attachment according to the resize                      configuration                     [Optional] Otherwise, System does not resize the attachment   System returns attachment as a file

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
    api_instance = testit_api_client.TestResultsApi(api_client)
    attachment_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Attachment internal identifier (guid format)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test result internal identifier (guid format)
    width = 56 # int | Width of the result image (optional)
    height = 56 # int | Height of the result image (optional)
    resize_type = testit_api_client.ImageResizeType() # ImageResizeType | Type of resizing to apply to the result image (optional)
    background_color = 'background_color_example' # str | Color of the background if the `resizeType` is `AddBackgroundStripes` (optional)
    preview = True # bool | If image must be converted to a preview (lower quality, no animation) (optional)

    try:
        # Get attachment of TestResult
        api_instance.download_attachment(attachment_id, id, width=width, height=height, resize_type=resize_type, background_color=background_color, preview=preview)
    except Exception as e:
        print("Exception when calling TestResultsApi->download_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Attachment internal identifier (guid format) | 
 **id** | **str**| Test result internal identifier (guid format) | 
 **width** | **int**| Width of the result image | [optional] 
 **height** | **int**| Height of the result image | [optional] 
 **resize_type** | [**ImageResizeType**](.md)| Type of resizing to apply to the result image | [optional] 
 **background_color** | **str**| Color of the background if the &#x60;resizeType&#x60; is &#x60;AddBackgroundStripes&#x60; | [optional] 
 **preview** | **bool**| If image must be converted to a preview (lower quality, no animation) | [optional] 

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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test result required |  -  |
**404** |  File not found   Attachment not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> AttachmentModel get_attachment(id, attachment_id)

Get Metadata of TestResult's attachment

 Use case   User sets attachmentId and testResultId   User runs method execution   System search attachment by the attachmentId and the testResultId   System returns attachment data

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.attachment_model import AttachmentModel
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test result internal identifier (guid format)
    attachment_id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Attachment internal identifier (guid format)

    try:
        # Get Metadata of TestResult's attachment
        api_response = api_instance.get_attachment(id, attachment_id)
        print("The response of TestResultsApi->get_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->get_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result internal identifier (guid format) | 
 **attachment_id** | **str**| Attachment internal identifier (guid format) | 

### Return type

[**AttachmentModel**](AttachmentModel.md)

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
**403** | Read permission for test result required |  -  |
**404** | File not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments**
> List[AttachmentModel] get_attachments(id)

Get all attachments of TestResult

 Use case   User sets testResultId   User runs method execution   System search all attachments of the test result   System returns attachments enumeration

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.attachment_model import AttachmentModel
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
    api_instance = testit_api_client.TestResultsApi(api_client)
    id = '3fa85f64-5717-4562-b3fc-2c963f66afa6' # str | Test result internal identifier (guid format)

    try:
        # Get all attachments of TestResult
        api_response = api_instance.get_attachments(id)
        print("The response of TestResultsApi->get_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TestResultsApi->get_attachments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result internal identifier (guid format) | 

### Return type

[**List[AttachmentModel]**](AttachmentModel.md)

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
**403** | Read permission for test result required |  -  |
**404** | TestResult not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

