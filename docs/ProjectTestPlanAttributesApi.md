# testit_api_client.ProjectTestPlanAttributesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_attribute_test_plan_project_relations**](ProjectTestPlanAttributesApi.md#create_custom_attribute_test_plan_project_relations) | **POST** /api/v2/projects/{projectId}/testPlans/attributes | Add attributes to project&#39;s test plans
[**delete_custom_attribute_test_plan_project_relations**](ProjectTestPlanAttributesApi.md#delete_custom_attribute_test_plan_project_relations) | **DELETE** /api/v2/projects/{projectId}/testPlans/attributes/{attributeId} | Delete attribute from project&#39;s test plans
[**get_custom_attribute_test_plan_project_relations**](ProjectTestPlanAttributesApi.md#get_custom_attribute_test_plan_project_relations) | **GET** /api/v2/projects/{projectId}/testPlans/attributes | Get project&#39;s test plan attributes
[**search_test_plan_attributes_in_project**](ProjectTestPlanAttributesApi.md#search_test_plan_attributes_in_project) | **POST** /api/v2/projects/{projectId}/testPlans/attributes/search | Search for attributes used in the project test plans
[**update_custom_attribute_test_plan_project_relations**](ProjectTestPlanAttributesApi.md#update_custom_attribute_test_plan_project_relations) | **PUT** /api/v2/projects/{projectId}/testPlans/attributes | Update attribute of project&#39;s test plans


# **create_custom_attribute_test_plan_project_relations**
> create_custom_attribute_test_plan_project_relations(project_id)

Add attributes to project's test plans

<br>Use case  <br>User sets project internal or global identifier and attributes identifiers  <br>User runs method execution  <br>System updates project and add attributes to project for test plans  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plan_attributes_api
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
    api_instance = project_test_plan_attributes_api.ProjectTestPlanAttributesApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add attributes to project's test plans
        api_instance.create_custom_attribute_test_plan_project_relations(project_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanAttributesApi->create_custom_attribute_test_plan_project_relations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add attributes to project's test plans
        api_instance.create_custom_attribute_test_plan_project_relations(project_id, request_body=request_body)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanAttributesApi->create_custom_attribute_test_plan_project_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **request_body** | **[str]**|  | [optional]

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
**403** | Update permission for project settings is required |  -  |
**400** | &lt;br&gt; Attributes must be global  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_attribute_test_plan_project_relations**
> delete_custom_attribute_test_plan_project_relations(project_id, attribute_id)

Delete attribute from project's test plans

<br>Use case  <br>User sets project internal or global identifier and attribute identifier  <br>User runs method execution  <br>System updates project and delete attribute from project for test plans  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plan_attributes_api
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
    api_instance = project_test_plan_attributes_api.ProjectTestPlanAttributesApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    attribute_id = "attributeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete attribute from project's test plans
        api_instance.delete_custom_attribute_test_plan_project_relations(project_id, attribute_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanAttributesApi->delete_custom_attribute_test_plan_project_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **attribute_id** | **str**|  |

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
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_attribute_test_plan_project_relations**
> [CustomAttributeModel] get_custom_attribute_test_plan_project_relations(project_id)

Get project's test plan attributes

<br>Use case  <br>User runs method execution  <br>System returns project for test plans attributes by project identifier

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plan_attributes_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_model import CustomAttributeModel
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
    api_instance = project_test_plan_attributes_api.ProjectTestPlanAttributesApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get project's test plan attributes
        api_response = api_instance.get_custom_attribute_test_plan_project_relations(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanAttributesApi->get_custom_attribute_test_plan_project_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**[CustomAttributeModel]**](CustomAttributeModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Read permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_test_plan_attributes_in_project**
> [CustomAttributeGetModel] search_test_plan_attributes_in_project(project_id)

Search for attributes used in the project test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plan_attributes_api
from testit_api_client.model.custom_attribute_get_model import CustomAttributeGetModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.search_attributes_in_project_request import SearchAttributesInProjectRequest
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
    api_instance = project_test_plan_attributes_api.ProjectTestPlanAttributesApi(api_client)
    project_id = "projectId_example" # str | Unique or global project ID
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    search_attributes_in_project_request = SearchAttributesInProjectRequest(None) # SearchAttributesInProjectRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for attributes used in the project test plans
        api_response = api_instance.search_test_plan_attributes_in_project(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanAttributesApi->search_test_plan_attributes_in_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for attributes used in the project test plans
        api_response = api_instance.search_test_plan_attributes_in_project(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, search_attributes_in_project_request=search_attributes_in_project_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanAttributesApi->search_test_plan_attributes_in_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global project ID |
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **search_attributes_in_project_request** | [**SearchAttributesInProjectRequest**](SearchAttributesInProjectRequest.md)|  | [optional]

### Return type

[**[CustomAttributeGetModel]**](CustomAttributeGetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**403** | Read permission for project is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_attribute_test_plan_project_relations**
> update_custom_attribute_test_plan_project_relations(project_id)

Update attribute of project's test plans

<br>Use case  <br>User sets project internal or global identifier and attribute model  <br>User runs method execution  <br>System updates project and project attribute for test plan  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_test_plan_attributes_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.update_custom_attribute_test_plan_project_relations_request import UpdateCustomAttributeTestPlanProjectRelationsRequest
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
    api_instance = project_test_plan_attributes_api.ProjectTestPlanAttributesApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    update_custom_attribute_test_plan_project_relations_request = UpdateCustomAttributeTestPlanProjectRelationsRequest(None) # UpdateCustomAttributeTestPlanProjectRelationsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update attribute of project's test plans
        api_instance.update_custom_attribute_test_plan_project_relations(project_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanAttributesApi->update_custom_attribute_test_plan_project_relations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update attribute of project's test plans
        api_instance.update_custom_attribute_test_plan_project_relations(project_id, update_custom_attribute_test_plan_project_relations_request=update_custom_attribute_test_plan_project_relations_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectTestPlanAttributesApi->update_custom_attribute_test_plan_project_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **update_custom_attribute_test_plan_project_relations_request** | [**UpdateCustomAttributeTestPlanProjectRelationsRequest**](UpdateCustomAttributeTestPlanProjectRelationsRequest.md)|  | [optional]

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
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

