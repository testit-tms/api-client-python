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
> api_v2_sections_id_patch(id)

Patch section

See <a href=\"https://www.rfc-editor.org/rfc/rfc6902\" target=\"_blank\">RFC 6902: JavaScript Object Notation (JSON) Patch</a> for details

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import sections_api
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
    api_instance = sections_api.SectionsApi(api_client)
    id = "id_example" # str | Section internal (UUID) identifier
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
        # Patch section
        api_instance.api_v2_sections_id_patch(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling SectionsApi->api_v2_sections_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch section
        api_instance.api_v2_sections_id_patch(id, operation=operation)
    except testit_api_client.ApiException as e:
        print("Exception when calling SectionsApi->api_v2_sections_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section internal (UUID) identifier |
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
**403** | Update permission for section is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_section**
> SectionWithStepsModel create_section()

Create section

<br>Use case  <br>User sets section properties (listed in request example)  <br>User runs method execution  <br>System creates section property values  <br>System returns section (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import sections_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.section_with_steps_model import SectionWithStepsModel
from testit_api_client.model.create_section_request import CreateSectionRequest
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
    api_instance = sections_api.SectionsApi(api_client)
    create_section_request = CreateSectionRequest(None) # CreateSectionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create section
        api_response = api_instance.create_section(create_section_request=create_section_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling SectionsApi->create_section: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_section_request** | [**CreateSectionRequest**](CreateSectionRequest.md)|  | [optional]

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_section**
> delete_section(id)

Delete section

<br>Use case  <br>User sets section identifier  <br>User runs method execution  <br>System search section by the identifier  <br>System search and delete nested sections of the found section  <br>System search and delete workitems related to the found nested sections  <br>System deletes initial section and related workitem  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import sections_api
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
    api_instance = sections_api.SectionsApi(api_client)
    id = "id_example" # str | Section internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete section
        api_instance.delete_section(id)
    except testit_api_client.ApiException as e:
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
**409** | Conflict |  -  |
**404** | Section with provided ID was not found |  -  |
**422** | Cannot delete root section |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_section_by_id**
> SectionWithStepsModel get_section_by_id(id)

Get section

<br>Use case  <br>User sets section internal (guid format) identifier  <br>User runs method execution  <br>System search section by the section identifier  <br>              [Optional] If isDeleted flag equals false, deleted work items are not being searched.              If true, deleted work items are also being searched, null for all work items.                <br>System returns section

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import sections_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.section_with_steps_model import SectionWithStepsModel
from testit_api_client.model.deletion_state import DeletionState
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
    api_instance = sections_api.SectionsApi(api_client)
    id = "id_example" # str | Section internal (UUID) identifier
    is_deleted = None # DeletionState |  (optional) if omitted the server will use the default value of NotDeleted

    # example passing only required values which don't have defaults set
    try:
        # Get section
        api_response = api_instance.get_section_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling SectionsApi->get_section_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get section
        api_response = api_instance.get_section_by_id(id, is_deleted=is_deleted)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling SectionsApi->get_section_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section internal (UUID) identifier |
 **is_deleted** | **DeletionState**|  | [optional] if omitted the server will use the default value of NotDeleted

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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Section with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_items_by_section_id**
> [WorkItemShortModel] get_work_items_by_section_id(id)

Get section work items

<br>Use case  <br>User sets section identifier  <br>User runs method execution  <br>System search section by the identifier  <br>System search work items related to the section  <br>              [Optional] If isDeleted flag equals false, deleted work items are not being searched.              If true, deleted work items are also being searched, null for all work items.                <br>System returns work item collection

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import sections_api
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
    api_instance = sections_api.SectionsApi(api_client)
    id = "id_example" # str | Section internal (UUID) identifier
    is_deleted = False # bool | Requested section is deleted (optional) if omitted the server will use the default value of False
    tag_names = [
        "tagNames_example",
    ] # [str] | List of work item tags (optional)
    include_iterations = True # bool |  (optional) if omitted the server will use the default value of True
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get section work items
        api_response = api_instance.get_work_items_by_section_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling SectionsApi->get_work_items_by_section_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get section work items
        api_response = api_instance.get_work_items_by_section_id(id, is_deleted=is_deleted, tag_names=tag_names, include_iterations=include_iterations, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling SectionsApi->get_work_items_by_section_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Section internal (UUID) identifier |
 **is_deleted** | **bool**| Requested section is deleted | [optional] if omitted the server will use the default value of False
 **tag_names** | **[str]**| List of work item tags | [optional]
 **include_iterations** | **bool**|  | [optional] if omitted the server will use the default value of True
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
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | &lt;br&gt;- &#x60;orderBy&#x60; statement must have one &#x60;.&#x60; and no &#x60;,&#x60; symbols  &lt;br&gt;- &#x60;orderBy&#x60; statement has invalid length  &lt;br&gt;- &#x60;orderBy&#x60; statement must have UUID as attribute key  &lt;br&gt;- Search field was not found |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Section with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move**
> move()

Move section with all work items into another section

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import sections_api
from testit_api_client.model.move_request import MoveRequest
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
    api_instance = sections_api.SectionsApi(api_client)
    move_request = MoveRequest(None) # MoveRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Move section with all work items into another section
        api_instance.move(move_request=move_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling SectionsApi->move: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_request** | [**MoveRequest**](MoveRequest.md)|  | [optional]

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
**403** | Update permission for test library is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename**
> rename()

Rename section

<br>Use case  <br>User sets section identifier and new name (listed in request example)  <br>User runs method execution  <br>System search section by the identifier  <br>System updates section name using the new name  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import sections_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.rename_request import RenameRequest
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
    api_instance = sections_api.SectionsApi(api_client)
    rename_request = RenameRequest(None) # RenameRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Rename section
        api_instance.rename(rename_request=rename_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling SectionsApi->rename: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rename_request** | [**RenameRequest**](RenameRequest.md)|  | [optional]

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
**401** | Unauthorized |  -  |
**403** | Update permission for test library is required |  -  |
**404** | Section with provided ID was not found |  -  |
**409** | Section with the same name already exists in the parent section |  -  |
**422** | Root section cannot be renamed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_section**
> update_section()

Update section

<br>Use case  <br>User sets section properties (listed in request example)  <br>User runs method execution  <br>System search section by the identifier  <br>System updates section using the property values  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import sections_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.update_section_request import UpdateSectionRequest
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
    api_instance = sections_api.SectionsApi(api_client)
    update_section_request = UpdateSectionRequest(None) # UpdateSectionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update section
        api_instance.update_section(update_section_request=update_section_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling SectionsApi->update_section: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_section_request** | [**UpdateSectionRequest**](UpdateSectionRequest.md)|  | [optional]

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
**400** | &lt;br&gt;- ID is invalid  &lt;br&gt;- Root section cannot be create |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library is required |  -  |
**404** | &lt;br&gt;- Section cannot be found  &lt;br&gt;- Parent section cannot be found  &lt;br&gt;- Project cannot be found |  -  |
**409** | Section with the same name already exists in the parent section |  -  |
**422** | &lt;br&gt;- Root section cannot be edited  &lt;br&gt;- Parent ID cannot be changed  &lt;br&gt;- Project ID cannot be changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

