# testit_api_client.ProjectAttributesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_projects_attribute**](ProjectAttributesApi.md#create_projects_attribute) | **POST** /api/v2/projects/{projectId}/attributes | Create project attribute
[**delete_projects_attribute**](ProjectAttributesApi.md#delete_projects_attribute) | **DELETE** /api/v2/projects/{projectId}/attributes/{attributeId} | Delete project attribute
[**get_attribute_by_project_id**](ProjectAttributesApi.md#get_attribute_by_project_id) | **GET** /api/v2/projects/{projectId}/attributes/{attributeId} | Get project attribute
[**get_attributes_by_project_id**](ProjectAttributesApi.md#get_attributes_by_project_id) | **GET** /api/v2/projects/{projectId}/attributes | Get project attributes
[**search_attributes_in_project**](ProjectAttributesApi.md#search_attributes_in_project) | **POST** /api/v2/projects/{projectId}/attributes/search | Search for attributes used in the project
[**update_projects_attribute**](ProjectAttributesApi.md#update_projects_attribute) | **PUT** /api/v2/projects/{projectId}/attributes | Edit attribute of the project


# **create_projects_attribute**
> CustomAttributeModel create_projects_attribute(project_id, custom_attribute_post_model=custom_attribute_post_model)

Create project attribute

 Use case   User sets attribute parameters (listed in request example) and runs method execution   System search project   System creates attribute and relates it to the project   System returns project attribute properties (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.custom_attribute_model import CustomAttributeModel
from testit_api_client.models.custom_attribute_post_model import CustomAttributePostModel
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
    api_instance = testit_api_client.ProjectAttributesApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier
    custom_attribute_post_model = testit_api_client.CustomAttributePostModel() # CustomAttributePostModel |  (optional)

    try:
        # Create project attribute
        api_response = api_instance.create_projects_attribute(project_id, custom_attribute_post_model=custom_attribute_post_model)
        print("The response of ProjectAttributesApi->create_projects_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAttributesApi->create_projects_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **custom_attribute_post_model** | [**CustomAttributePostModel**](CustomAttributePostModel.md)|  | [optional] 

### Return type

[**CustomAttributeModel**](CustomAttributeModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  - Attribute is &#x60;null&#x60;   - Priority is invalid   - Attribute with &#x60;Options&#x60; type must have an options   - ID is not &#x60;null&#x60;   - Option ID is not &#x60;null&#x60; |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for project settings is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** |  &#x60;CustomAttribute.Name&#x60; or &#x60;CustomAttribute.Id&#x60; are not unique in attributes schemes   &#x60;CustomAttributeOptionModel.Id&#x60; or &#x60;CustomAttributeOptionModel.Value&#x60; are not unique in &#x60;attributesScheme.Options&#x60; |  -  |
**422** | Cannot add new attribute from template which is in use |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_projects_attribute**
> delete_projects_attribute(project_id, attribute_id)

Delete project attribute

 Use case   User sets project identifier and runs method execution   User sets attribute identifier   User runs method execution   System search project   System search and delete attribute   System returns no content response

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
    api_instance = testit_api_client.ProjectAttributesApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier
    attribute_id = 'attribute_id_example' # str | Project attribute internal (UUID)

    try:
        # Delete project attribute
        api_instance.delete_projects_attribute(project_id, attribute_id)
    except Exception as e:
        print("Exception when calling ProjectAttributesApi->delete_projects_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **attribute_id** | **str**| Project attribute internal (UUID) | 

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
**400** |  - Project ID is invalid   - Project attribute ID is invalid   - Attribute is empty |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for project settings is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_by_project_id**
> CustomAttributeModel get_attribute_by_project_id(project_id, attribute_id)

Get project attribute

 Use case   User sets project internal or global identifier   User sets project attribute identifier   User runs method execution   System search project   System search project attribute    System returns project attribute (listed in response model)

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
    api_instance = testit_api_client.ProjectAttributesApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier
    attribute_id = 'attribute_id_example' # str | Project attribute internal (UUID) or global (integer) identifier

    try:
        # Get project attribute
        api_response = api_instance.get_attribute_by_project_id(project_id, attribute_id)
        print("The response of ProjectAttributesApi->get_attribute_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAttributesApi->get_attribute_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **attribute_id** | **str**| Project attribute internal (UUID) or global (integer) identifier | 

### Return type

[**CustomAttributeModel**](CustomAttributeModel.md)

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
**403** | Read permission for test library is required |  -  |
**404** |  - Project with provided ID was not found   - Project attribute with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes_by_project_id**
> List[CustomAttributeModel] get_attributes_by_project_id(project_id, is_deleted=is_deleted)

Get project attributes

 Use case   User sets project internal or global identifier   [Optional] User sets isDeleted field value   User runs method execution   System search project   [Optional] If User sets isDeleted field value as true, System search all deleted attributes related to project   [Optional] If User sets isDeleted field value as false, System search all attributes related to project which are not deleted   [Optional] If User did not set isDeleted field value, System search all attributes related to project   System returns array of found attributes (listed in response model)

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
    api_instance = testit_api_client.ProjectAttributesApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier
    is_deleted = testit_api_client.DeletionState() # DeletionState |  (optional)

    try:
        # Get project attributes
        api_response = api_instance.get_attributes_by_project_id(project_id, is_deleted=is_deleted)
        print("The response of ProjectAttributesApi->get_attributes_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAttributesApi->get_attributes_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **is_deleted** | [**DeletionState**](.md)|  | [optional] 

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
**403** | Read permission for test library is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_attributes_in_project**
> List[CustomAttributeGetModel] search_attributes_in_project(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, project_attributes_filter_model=project_attributes_filter_model)

Search for attributes used in the project

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
    api_instance = testit_api_client.ProjectAttributesApi(api_client)
    project_id = 'project_id_example' # str | Unique or global project ID
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    project_attributes_filter_model = testit_api_client.ProjectAttributesFilterModel() # ProjectAttributesFilterModel |  (optional)

    try:
        # Search for attributes used in the project
        api_response = api_instance.search_attributes_in_project(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, project_attributes_filter_model=project_attributes_filter_model)
        print("The response of ProjectAttributesApi->search_attributes_in_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectAttributesApi->search_attributes_in_project: %s\n" % e)
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

# **update_projects_attribute**
> update_projects_attribute(project_id, custom_attribute_put_model=custom_attribute_put_model)

Edit attribute of the project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.custom_attribute_put_model import CustomAttributePutModel
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
    api_instance = testit_api_client.ProjectAttributesApi(api_client)
    project_id = 'project_id_example' # str | Unique or global project ID
    custom_attribute_put_model = testit_api_client.CustomAttributePutModel() # CustomAttributePutModel |  (optional)

    try:
        # Edit attribute of the project
        api_instance.update_projects_attribute(project_id, custom_attribute_put_model=custom_attribute_put_model)
    except Exception as e:
        print("Exception when calling ProjectAttributesApi->update_projects_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global project ID | 
 **custom_attribute_put_model** | [**CustomAttributePutModel**](CustomAttributePutModel.md)|  | [optional] 

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

