# testit_api_client.SectionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_sections_id_patch**](SectionsApi.md#api_v2_sections_id_patch) | **PATCH** /api/v2/sections/{id} | Patch section
[**create_section**](SectionsApi.md#create_section) | **POST** /api/v2/sections | Create section
[**delete_section**](SectionsApi.md#delete_section) | **DELETE** /api/v2/sections/{id} | Delete section
[**get_section_by_id**](SectionsApi.md#get_section_by_id) | **GET** /api/v2/sections/{id} | Get section
[**get_work_items_by_section_id**](SectionsApi.md#get_work_items_by_section_id) | **GET** /api/v2/sections/{id}/workItems | Get section work items
[**move**](SectionsApi.md#move) | **POST** /api/v2/sections/move | Move section with all work items into another section
[**rename**](SectionsApi.md#rename) | **POST** /api/v2/sections/rename | Rename section
[**update_section**](SectionsApi.md#update_section) | **PUT** /api/v2/sections | Update section


# **api_v2_sections_id_patch**
> api_v2_sections_id_patch(id, operation=operation)

Patch section

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
    api_instance = testit_api_client.SectionsApi(api_client)
    id = 'id_example' # str | Section internal (UUID) identifier
    operation = [testit_api_client.Operation()] # List[Operation] |  (optional)

    try:
        # Patch section
        api_instance.api_v2_sections_id_patch(id, operation=operation)
    except Exception as e:
        print("Exception when calling SectionsApi->api_v2_sections_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section internal (UUID) identifier | 
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
**403** | Update permission for section is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_section**
> SectionWithStepsModel create_section(section_post_model=section_post_model)

Create section

 Use case  User sets section properties (listed in request example)  User runs method execution  System creates section property values  System returns section (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.section_post_model import SectionPostModel
from testit_api_client.models.section_with_steps_model import SectionWithStepsModel
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
    api_instance = testit_api_client.SectionsApi(api_client)
    section_post_model = testit_api_client.SectionPostModel() # SectionPostModel |  (optional)

    try:
        # Create section
        api_response = api_instance.create_section(section_post_model=section_post_model)
        print("The response of SectionsApi->create_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->create_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_post_model** | [**SectionPostModel**](SectionPostModel.md)|  | [optional] 

### Return type

[**SectionWithStepsModel**](SectionWithStepsModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Cannot create section without parent ID |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library is required |  -  |
**404** | Parent section with provided ID was not found |  -  |
**409** | Section with the same name already exists in the parent section |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_section**
> delete_section(id)

Delete section

 Use case  User sets section identifier  User runs method execution  System search section by the identifier  System search and delete nested sections of the found section  System search and delete workitems related to the found nested sections  System deletes initial section and related workitem  System returns no content response

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
    api_instance = testit_api_client.SectionsApi(api_client)
    id = 'id_example' # str | Section internal (UUID) identifier

    try:
        # Delete section
        api_instance.delete_section(id)
    except Exception as e:
        print("Exception when calling SectionsApi->delete_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section internal (UUID) identifier | 

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
**403** | Delete permission for test library is required |  -  |
**404** | Section with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Cannot delete root section |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_by_id**
> SectionWithStepsModel get_section_by_id(id, is_deleted=is_deleted)

Get section

 Use case  User sets section internal (guid format) identifier  User runs method execution  System search section by the section identifier  [Optional] If isDeleted flag equals false, deleted work items are not being searched.             If true, deleted work items are also being searched, null for all work items.  System returns section

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.section_with_steps_model import SectionWithStepsModel
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
    api_instance = testit_api_client.SectionsApi(api_client)
    id = 'id_example' # str | Section internal (UUID) identifier
    is_deleted = testit_api_client.DeletionState() # DeletionState |  (optional)

    try:
        # Get section
        api_response = api_instance.get_section_by_id(id, is_deleted=is_deleted)
        print("The response of SectionsApi->get_section_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->get_section_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section internal (UUID) identifier | 
 **is_deleted** | [**DeletionState**](.md)|  | [optional] 

### Return type

[**SectionWithStepsModel**](SectionWithStepsModel.md)

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
**404** | Section with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_items_by_section_id**
> List[WorkItemShortModel] get_work_items_by_section_id(id, is_deleted=is_deleted, tag_names=tag_names, include_iterations=include_iterations, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get section work items

 Use case  User sets section identifier  User runs method execution  System search section by the identifier  System search work items related to the section  [Optional] If isDeleted flag equals false, deleted work items are not being searched.             If true, deleted work items are also being searched, null for all work items.  System returns work item collection

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
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
    api_instance = testit_api_client.SectionsApi(api_client)
    id = 'id_example' # str | Section internal (UUID) identifier
    is_deleted = False # bool | Requested section is deleted (optional) (default to False)
    tag_names = ['tag_names_example'] # List[str] | List of work item tags (optional)
    include_iterations = True # bool |  (optional) (default to True)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get section work items
        api_response = api_instance.get_work_items_by_section_id(id, is_deleted=is_deleted, tag_names=tag_names, include_iterations=include_iterations, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of SectionsApi->get_work_items_by_section_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SectionsApi->get_work_items_by_section_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section internal (UUID) identifier | 
 **is_deleted** | **bool**| Requested section is deleted | [optional] [default to False]
 **tag_names** | [**List[str]**](str.md)| List of work item tags | [optional] 
 **include_iterations** | **bool**|  | [optional] [default to True]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 

### Return type

[**List[WorkItemShortModel]**](WorkItemShortModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** |  - &#x60;orderBy&#x60; statement must have one &#x60;.&#x60; and no &#x60;,&#x60; symbols  - &#x60;orderBy&#x60; statement has invalid length  - &#x60;orderBy&#x60; statement must have UUID as attribute key  - Search field was not found |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Section with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move**
> move(section_move_model=section_move_model)

Move section with all work items into another section

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.section_move_model import SectionMoveModel
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
    api_instance = testit_api_client.SectionsApi(api_client)
    section_move_model = testit_api_client.SectionMoveModel() # SectionMoveModel |  (optional)

    try:
        # Move section with all work items into another section
        api_instance.move(section_move_model=section_move_model)
    except Exception as e:
        print("Exception when calling SectionsApi->move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_move_model** | [**SectionMoveModel**](SectionMoveModel.md)|  | [optional] 

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
**403** | Update permission for test library is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename**
> rename(section_rename_model=section_rename_model)

Rename section

 Use case  User sets section identifier and new name (listed in request example)  User runs method execution  System search section by the identifier  System updates section name using the new name  System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.section_rename_model import SectionRenameModel
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
    api_instance = testit_api_client.SectionsApi(api_client)
    section_rename_model = testit_api_client.SectionRenameModel() # SectionRenameModel |  (optional)

    try:
        # Rename section
        api_instance.rename(section_rename_model=section_rename_model)
    except Exception as e:
        print("Exception when calling SectionsApi->rename: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_rename_model** | [**SectionRenameModel**](SectionRenameModel.md)|  | [optional] 

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
**403** | Update permission for test library is required |  -  |
**404** | Section with provided ID was not found |  -  |
**409** | Section with the same name already exists in the parent section |  -  |
**422** | Root section cannot be renamed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section**
> update_section(section_put_model=section_put_model)

Update section

 Use case  User sets section properties (listed in request example)  User runs method execution  System search section by the identifier  System updates section using the property values  System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.section_put_model import SectionPutModel
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
    api_instance = testit_api_client.SectionsApi(api_client)
    section_put_model = testit_api_client.SectionPutModel() # SectionPutModel |  (optional)

    try:
        # Update section
        api_instance.update_section(section_put_model=section_put_model)
    except Exception as e:
        print("Exception when calling SectionsApi->update_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **section_put_model** | [**SectionPutModel**](SectionPutModel.md)|  | [optional] 

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
**400** |  - ID is invalid  - Root section cannot be create |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library is required |  -  |
**404** |  - Section cannot be found  - Parent section cannot be found  - Project cannot be found |  -  |
**409** | Section with the same name already exists in the parent section |  -  |
**422** |  - Root section cannot be edited  - Parent ID cannot be changed  - Project ID cannot be changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

