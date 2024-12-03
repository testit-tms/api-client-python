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
> create_custom_attribute_test_plan_project_relations(project_id, request_body=request_body)

Add attributes to project's test plans

 Use case   User sets project internal or global identifier and attributes identifiers   User runs method execution   System updates project and add attributes to project for test plans   System returns no content response

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
    api_instance = testit_api_client.ProjectTestPlanAttributesApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Add attributes to project's test plans
        api_instance.create_custom_attribute_test_plan_project_relations(project_id, request_body=request_body)
    except Exception as e:
        print("Exception when calling ProjectTestPlanAttributesApi->create_custom_attribute_test_plan_project_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier | 
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
**400** |   Attributes must be global  |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for project settings is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_attribute_test_plan_project_relations**
> delete_custom_attribute_test_plan_project_relations(project_id, attribute_id)

Delete attribute from project's test plans

 Use case   User sets project internal or global identifier and attribute identifier   User runs method execution   System updates project and delete attribute from project for test plans   System returns no content response

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
    api_instance = testit_api_client.ProjectTestPlanAttributesApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier
    attribute_id = 'attribute_id_example' # str | 

    try:
        # Delete attribute from project's test plans
        api_instance.delete_custom_attribute_test_plan_project_relations(project_id, attribute_id)
    except Exception as e:
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
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for project settings is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_attribute_test_plan_project_relations**
> List[CustomAttributeModel] get_custom_attribute_test_plan_project_relations(project_id)

Get project's test plan attributes

 Use case   User runs method execution   System returns project for test plans attributes by project identifier

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.custom_attribute_model import CustomAttributeModel
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
    api_instance = testit_api_client.ProjectTestPlanAttributesApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier

    try:
        # Get project's test plan attributes
        api_response = api_instance.get_custom_attribute_test_plan_project_relations(project_id)
        print("The response of ProjectTestPlanAttributesApi->get_custom_attribute_test_plan_project_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectTestPlanAttributesApi->get_custom_attribute_test_plan_project_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier | 

### Return type

[**List[CustomAttributeModel]**](CustomAttributeModel.md)

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
**403** | Read permission for project settings is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_test_plan_attributes_in_project**
> List[CustomAttributeGetModel] search_test_plan_attributes_in_project(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, project_attributes_filter_model=project_attributes_filter_model)

Search for attributes used in the project test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.custom_attribute_get_model import CustomAttributeGetModel
from testit_api_client.models.project_attributes_filter_model import ProjectAttributesFilterModel
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
    api_instance = testit_api_client.ProjectTestPlanAttributesApi(api_client)
    project_id = 'project_id_example' # str | Unique or global project ID
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    project_attributes_filter_model = testit_api_client.ProjectAttributesFilterModel() # ProjectAttributesFilterModel |  (optional)

    try:
        # Search for attributes used in the project test plans
        api_response = api_instance.search_test_plan_attributes_in_project(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, project_attributes_filter_model=project_attributes_filter_model)
        print("The response of ProjectTestPlanAttributesApi->search_test_plan_attributes_in_project:\n")
        pprint(api_response)
    except Exception as e:
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
 **project_attributes_filter_model** | [**ProjectAttributesFilterModel**](ProjectAttributesFilterModel.md)|  | [optional] 

### Return type

[**List[CustomAttributeGetModel]**](CustomAttributeGetModel.md)

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
**403** | Read permission for project is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_attribute_test_plan_project_relations**
> update_custom_attribute_test_plan_project_relations(project_id, custom_attribute_test_plan_project_relation_put_model=custom_attribute_test_plan_project_relation_put_model)

Update attribute of project's test plans

 Use case   User sets project internal or global identifier and attribute model   User runs method execution   System updates project and project attribute for test plan   System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.custom_attribute_test_plan_project_relation_put_model import CustomAttributeTestPlanProjectRelationPutModel
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
    api_instance = testit_api_client.ProjectTestPlanAttributesApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier
    custom_attribute_test_plan_project_relation_put_model = testit_api_client.CustomAttributeTestPlanProjectRelationPutModel() # CustomAttributeTestPlanProjectRelationPutModel |  (optional)

    try:
        # Update attribute of project's test plans
        api_instance.update_custom_attribute_test_plan_project_relations(project_id, custom_attribute_test_plan_project_relation_put_model=custom_attribute_test_plan_project_relation_put_model)
    except Exception as e:
        print("Exception when calling ProjectTestPlanAttributesApi->update_custom_attribute_test_plan_project_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **custom_attribute_test_plan_project_relation_put_model** | [**CustomAttributeTestPlanProjectRelationPutModel**](CustomAttributeTestPlanProjectRelationPutModel.md)|  | [optional] 

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
**403** | Update permission for project settings is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

