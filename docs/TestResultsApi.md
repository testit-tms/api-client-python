# testit_api_client.TestResultsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_test_results_id_aggregated_get**](TestResultsApi.md#api_v2_test_results_id_aggregated_get) | **GET** /api/v2/testResults/{id}/aggregated | 
[**api_v2_test_results_id_attachments_attachment_id_put**](TestResultsApi.md#api_v2_test_results_id_attachments_attachment_id_put) | **PUT** /api/v2/testResults/{id}/attachments/{attachmentId} | 
[**api_v2_test_results_id_attachments_info_get**](TestResultsApi.md#api_v2_test_results_id_attachments_info_get) | **GET** /api/v2/testResults/{id}/attachments/info | 
[**api_v2_test_results_id_external_projects_external_project_id_defect_post**](TestResultsApi.md#api_v2_test_results_id_external_projects_external_project_id_defect_post) | **POST** /api/v2/testResults/{id}/externalProjects/{externalProjectId}/defect | 
[**api_v2_test_results_id_external_projects_external_project_id_form_get**](TestResultsApi.md#api_v2_test_results_id_external_projects_external_project_id_form_get) | **GET** /api/v2/testResults/{id}/externalProjects/{externalProjectId}/form | 
[**api_v2_test_results_id_get**](TestResultsApi.md#api_v2_test_results_id_get) | **GET** /api/v2/testResults/{id} | 
[**api_v2_test_results_id_link_requests_post**](TestResultsApi.md#api_v2_test_results_id_link_requests_post) | **POST** /api/v2/testResults/{id}/linkRequests | 
[**api_v2_test_results_id_put**](TestResultsApi.md#api_v2_test_results_id_put) | **PUT** /api/v2/testResults/{id} | 
[**api_v2_test_results_link_requests_link_request_id_use_post**](TestResultsApi.md#api_v2_test_results_link_requests_link_request_id_use_post) | **POST** /api/v2/testResults/linkRequests/{linkRequestId}/use | 
[**create_attachment**](TestResultsApi.md#create_attachment) | **POST** /api/v2/testResults/{id}/attachments | Upload and link attachment to TestResult
[**delete_attachment**](TestResultsApi.md#delete_attachment) | **DELETE** /api/v2/testResults/{id}/attachments/{attachmentId} | Remove attachment and unlink from TestResult
[**download_attachment**](TestResultsApi.md#download_attachment) | **GET** /api/v2/testResults/{id}/attachments/{attachmentId} | Get attachment of TestResult
[**get_attachment**](TestResultsApi.md#get_attachment) | **GET** /api/v2/testResults/{id}/attachments/{attachmentId}/info | Get Metadata of TestResult&#39;s attachment
[**get_attachments**](TestResultsApi.md#get_attachments) | **GET** /api/v2/testResults/{id}/attachments | Get all attachments of TestResult


# **api_v2_test_results_id_aggregated_get**
> TestResultModel api_v2_test_results_id_aggregated_get(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
from testit_api_client.model.test_result_model import TestResultModel
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_test_results_id_aggregated_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_aggregated_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**TestResultModel**](TestResultModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_attachments_attachment_id_put**
> api_v2_test_results_id_attachments_attachment_id_put(id, attachment_id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "id_example" # str | 
    attachment_id = "attachmentId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_v2_test_results_id_attachments_attachment_id_put(id, attachment_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_attachments_attachment_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **attachment_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_attachments_info_get**
> [AttachmentModel] api_v2_test_results_id_attachments_info_get(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
from testit_api_client.model.attachment_model import AttachmentModel
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_test_results_id_attachments_info_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_attachments_info_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[AttachmentModel]**](AttachmentModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_external_projects_external_project_id_defect_post**
> str api_v2_test_results_id_external_projects_external_project_id_defect_post(id, external_project_id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "id_example" # str | 
    external_project_id = "externalProjectId_example" # str | 
    body = None # bool, date, datetime, dict, float, int, list, str, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_test_results_id_external_projects_external_project_id_defect_post(id, external_project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_external_projects_external_project_id_defect_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_test_results_id_external_projects_external_project_id_defect_post(id, external_project_id, body=body)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_external_projects_external_project_id_defect_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **external_project_id** | **str**|  |
 **body** | **bool, date, datetime, dict, float, int, list, str, none_type**|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_external_projects_external_project_id_form_get**
> bool, date, datetime, dict, float, int, list, str, none_type api_v2_test_results_id_external_projects_external_project_id_form_get(id, external_project_id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "id_example" # str | 
    external_project_id = "externalProjectId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_test_results_id_external_projects_external_project_id_form_get(id, external_project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_external_projects_external_project_id_form_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **external_project_id** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_get**
> TestResultModel api_v2_test_results_id_get(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
from testit_api_client.model.test_result_model import TestResultModel
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_test_results_id_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**TestResultModel**](TestResultModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_link_requests_post**
> str api_v2_test_results_id_link_requests_post(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
from testit_api_client.model.test_result_link_request_post_model import TestResultLinkRequestPostModel
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "id_example" # str | 
    test_result_link_request_post_model = TestResultLinkRequestPostModel(
        external_project_id="external_project_id_example",
        url="url_example",
    ) # TestResultLinkRequestPostModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_test_results_id_link_requests_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_link_requests_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_test_results_id_link_requests_post(id, test_result_link_request_post_model=test_result_link_request_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_link_requests_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **test_result_link_request_post_model** | [**TestResultLinkRequestPostModel**](TestResultLinkRequestPostModel.md)|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_id_put**
> api_v2_test_results_id_put(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
from testit_api_client.model.test_result_create_model import TestResultCreateModel
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "id_example" # str | 
    test_result_create_model = TestResultCreateModel(
        duration_in_ms=0,
        step_comments=[
            TestResultStepCommentPutModel(
                id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
                text="text_example",
                step_id="step_id_example",
                parent_step_id="parent_step_id_example",
                attachments=[
                    AttachmentPutModel(
                        id="id_example",
                    ),
                ],
            ),
        ],
        failure_class_ids=[
            "failure_class_ids_example",
        ],
        outcome="outcome_example",
        comment="comment_example",
        links=[
            LinkModel(
                id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
                title="title_example",
                url="url_example",
                description="description_example",
                type=LinkType("Related"),
                has_info=True,
            ),
        ],
        step_results=[
            StepResultModel(
                step_id="step_id_example",
                outcome="outcome_example",
                shared_step_version_id="shared_step_version_id_example",
                shared_step_results=[
                    SharedStepResultModel(
                        step_id="step_id_example",
                        outcome="outcome_example",
                    ),
                ],
            ),
        ],
        attachments=[
            AttachmentPutModel(
                id="id_example",
            ),
        ],
    ) # TestResultCreateModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_v2_test_results_id_put(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.api_v2_test_results_id_put(id, test_result_create_model=test_result_create_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **test_result_create_model** | [**TestResultCreateModel**](TestResultCreateModel.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_test_results_link_requests_link_request_id_use_post**
> LinkModel api_v2_test_results_link_requests_link_request_id_use_post(link_request_id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
from testit_api_client.model.use_test_result_link_request_post_model import UseTestResultLinkRequestPostModel
from testit_api_client.model.link_model import LinkModel
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
    api_instance = test_results_api.TestResultsApi(api_client)
    link_request_id = "linkRequestId_example" # str | 
    use_test_result_link_request_post_model = UseTestResultLinkRequestPostModel(
        title="title_example",
        url="url_example",
    ) # UseTestResultLinkRequestPostModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_test_results_link_requests_link_request_id_use_post(link_request_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_link_requests_link_request_id_use_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_test_results_link_requests_link_request_id_use_post(link_request_id, use_test_result_link_request_post_model=use_test_result_link_request_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->api_v2_test_results_link_requests_link_request_id_use_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_request_id** | **str**|  |
 **use_test_result_link_request_post_model** | [**UseTestResultLinkRequestPostModel**](UseTestResultLinkRequestPostModel.md)|  | [optional]

### Return type

[**LinkModel**](LinkModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_attachment**
> str create_attachment(id)

Upload and link attachment to TestResult

<br>Use case  <br>User sets testResultId  <br>User attaches a file  <br>System creates attachment and links it to the test result  <br>System returns attachment identifier

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test result internal identifier (guid format)
    file = open('/path/to/file', 'rb') # file_type | Select file (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload and link attachment to TestResult
        api_response = api_instance.create_attachment(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->create_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload and link attachment to TestResult
        api_response = api_instance.create_attachment(id, file=file)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->create_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result internal identifier (guid format) |
 **file** | **file_type**| Select file | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**413** | Multipart body length limit exceeded (default constraint is one gigabyte) |  -  |
**404** |  |  -  |
**403** | Update permission for test result required |  -  |
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attachment**
> delete_attachment(id, attachment_id)

Remove attachment and unlink from TestResult

<br>Use case  <br>User sets testResultId and attachmentId  <br>User attaches a file  <br>User runs method execution  <br>System deletes attachment and unlinks it from the test result  <br>System returns attachment identifier

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test result internal identifier (guid format)
    attachment_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Attachment internal identifier (guid format)

    # example passing only required values which don't have defaults set
    try:
        # Remove attachment and unlink from TestResult
        api_instance.delete_attachment(id, attachment_id)
    except testit_api_client.ApiException as e:
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
**401** | Unauthorized |  -  |
**403** | Update permission for test result required |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_attachment**
> download_attachment(attachment_id, id)

Get attachment of TestResult

<br>Use case  <br>User sets attachmentId and testResultId  <br>[Optional] User sets resize configuration  <br>User runs method execution  <br>System search attachments by the attachmentId and the testResultId  <br>                      [Optional] If resize configuration is set, System resizes the attachment according to the resize                      configuration                    <br>[Optional] Otherwise, System does not resize the attachment  <br>System returns attachment as a file

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.image_resize_type import ImageResizeType
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
    api_instance = test_results_api.TestResultsApi(api_client)
    attachment_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Attachment internal identifier (guid format)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test result internal identifier (guid format)
    width = 1 # int | Width of the result image (optional)
    height = 1 # int | Height of the result image (optional)
    resize_type = ImageResizeType("Crop") # ImageResizeType | Type of resizing to apply to the result image (optional)
    background_color = "backgroundColor_example" # str | Color of the background if the `resizeType` is `AddBackgroundStripes` (optional)
    preview = True # bool | If image must be converted to a preview (lower quality, no animation) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get attachment of TestResult
        api_instance.download_attachment(attachment_id, id)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->download_attachment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get attachment of TestResult
        api_instance.download_attachment(attachment_id, id, width=width, height=height, resize_type=resize_type, background_color=background_color, preview=preview)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->download_attachment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| Attachment internal identifier (guid format) |
 **id** | **str**| Test result internal identifier (guid format) |
 **width** | **int**| Width of the result image | [optional]
 **height** | **int**| Height of the result image | [optional]
 **resize_type** | **ImageResizeType**| Type of resizing to apply to the result image | [optional]
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
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**404** | &lt;br&gt;File not found  &lt;br&gt;Attachment not found |  -  |
**400** | Bad Request |  -  |
**403** | Read permission for test result required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment**
> AttachmentModel get_attachment(id, attachment_id)

Get Metadata of TestResult's attachment

<br>Use case  <br>User sets attachmentId and testResultId  <br>User runs method execution  <br>System search attachment by the attachmentId and the testResultId  <br>System returns attachment data

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.attachment_model import AttachmentModel
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test result internal identifier (guid format)
    attachment_id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Attachment internal identifier (guid format)

    # example passing only required values which don't have defaults set
    try:
        # Get Metadata of TestResult's attachment
        api_response = api_instance.get_attachment(id, attachment_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**403** | Read permission for test result required |  -  |
**404** | File not found |  -  |
**200** | Successful operation |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments**
> [AttachmentModel] get_attachments(id)

Get all attachments of TestResult

<br>Use case  <br>User sets testResultId  <br>User runs method execution  <br>System search all attachments of the test result  <br>System returns attachments enumeration

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import test_results_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.attachment_model import AttachmentModel
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
    api_instance = test_results_api.TestResultsApi(api_client)
    id = "3fa85f64-5717-4562-b3fc-2c963f66afa6" # str | Test result internal identifier (guid format)

    # example passing only required values which don't have defaults set
    try:
        # Get all attachments of TestResult
        api_response = api_instance.get_attachments(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling TestResultsApi->get_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Test result internal identifier (guid format) |

### Return type

[**[AttachmentModel]**](AttachmentModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**403** | Read permission for test result required |  -  |
**404** | TestResult not found |  -  |
**401** | Unauthorized |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

