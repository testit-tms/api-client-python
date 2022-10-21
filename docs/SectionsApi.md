# testit_api_client.SectionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_section**](SectionsApi.md#create_section) | **POST** /api/v2/sections | Create section
[**delete_section**](SectionsApi.md#delete_section) | **DELETE** /api/v2/sections/{id} | Delete section
[**get_section_by_id**](SectionsApi.md#get_section_by_id) | **GET** /api/v2/sections/{id} | Get section
[**get_work_items_by_section_id**](SectionsApi.md#get_work_items_by_section_id) | **GET** /api/v2/sections/{id}/workItems | Get section work items
[**move**](SectionsApi.md#move) | **POST** /api/v2/sections/move | Move section
[**rename**](SectionsApi.md#rename) | **POST** /api/v2/sections/rename | Rename section
[**update_section**](SectionsApi.md#update_section) | **PUT** /api/v2/sections | Update section


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
from testit_api_client.model.section_post_model import SectionPostModel
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
    section_post_model = SectionPostModel(
        name="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        project_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        parent_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        precondition_steps=[
            StepPutModel(
                id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
                action="User press the button",
                expected="System makes a beeeep sound",
                test_data="Some variables values",
                comments="Comment on what to look for",
                work_item_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
            ),
        ],
        postcondition_steps=[
            StepPutModel(
                id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
                action="User press the button",
                expected="System makes a beeeep sound",
                test_data="Some variables values",
                comments="Comment on what to look for",
                work_item_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
            ),
        ],
    ) # SectionPostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create section
        api_response = api_instance.create_section(section_post_model=section_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**201** | Success |  -  |
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
**401** | Unauthorized |  -  |
**403** | Delete permission for test library is required |  -  |
**204** | Success |  -  |
**409** | Conflict |  -  |
**400** | Bad Request |  -  |
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
 **is_deleted** | **bool**| Requested section is deleted | [optional] if omitted the server will use the default value of False

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
**403** | Read permission for test library is required |  -  |
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
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

Move section

<br>Can be moved inside another section. It is possible to indicate a project  <br>Use case  <br>User sets section identifier, old parent identifier, parent identifier and  next section identifier (listed in request example)  <br>User runs method execution  <br>System search section by the identifier  <br>System unlink section from the old parent and links to the new one  <br>System updates section rank using the next section identifier  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import sections_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.section_move_model import SectionMoveModel
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
    section_move_model = SectionMoveModel(
        id="id_example",
        old_parent_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        parent_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        next_section_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
    ) # SectionMoveModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Move section
        api_instance.move(section_move_model=section_move_model)
    except testit_api_client.ApiException as e:
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
**404** | &lt;br&gt;- Section with provided ID was not found  &lt;br&gt;- Parent section with provided ID was not found |  -  |
**409** | Section was modified |  -  |
**204** | Success |  -  |
**400** | Action leads to section loop |  -  |
**401** | Unauthorized |  -  |
**403** | Update permission for test library is required |  -  |
**422** | Cannot move root section |  -  |

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
from testit_api_client.model.section_rename_model import SectionRenameModel
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
    section_rename_model = SectionRenameModel(
        id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        name="New root section",
    ) # SectionRenameModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Rename section
        api_instance.rename(section_rename_model=section_rename_model)
    except testit_api_client.ApiException as e:
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
**401** | Unauthorized |  -  |
**404** | Section with provided ID was not found |  -  |
**409** | Section with the same name already exists in the parent section |  -  |
**403** | Update permission for test library is required |  -  |
**204** | Success |  -  |
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
from testit_api_client.model.validation_problem_details import ValidationProblemDetails
from testit_api_client.model.section_put_model import SectionPutModel
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
    section_put_model = SectionPutModel(
        id="id_example",
        name="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        project_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        parent_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        precondition_steps=[
            StepPutModel(
                id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
                action="User press the button",
                expected="System makes a beeeep sound",
                test_data="Some variables values",
                comments="Comment on what to look for",
                work_item_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
            ),
        ],
        postcondition_steps=[
            StepPutModel(
                id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
                action="User press the button",
                expected="System makes a beeeep sound",
                test_data="Some variables values",
                comments="Comment on what to look for",
                work_item_id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
            ),
        ],
    ) # SectionPutModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update section
        api_instance.update_section(section_put_model=section_put_model)
    except testit_api_client.ApiException as e:
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
**401** | Unauthorized |  -  |
**204** | Success |  -  |
**409** | Section with the same name already exists in the parent section |  -  |
**400** | &lt;br&gt;- ID is invalid  &lt;br&gt;- Root section cannot be create |  -  |
**422** | &lt;br&gt;- Root section cannot be edited  &lt;br&gt;- Parent ID cannot be changed  &lt;br&gt;- Project ID cannot be changed |  -  |
**403** | Update permission for test library is required |  -  |
**404** | &lt;br&gt;- Section cannot be found  &lt;br&gt;- Parent section cannot be found  &lt;br&gt;- Project cannot be found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

