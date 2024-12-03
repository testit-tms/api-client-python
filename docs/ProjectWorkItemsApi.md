# testit_api_client.ProjectWorkItemsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_project_id_work_items_search_grouped_post**](ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_search_grouped_post) | **POST** /api/v2/projects/{projectId}/workItems/search/grouped | Search for work items and group results by attribute
[**api_v2_projects_project_id_work_items_search_id_post**](ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_search_id_post) | **POST** /api/v2/projects/{projectId}/workItems/search/id | Search for work items and extract IDs only
[**api_v2_projects_project_id_work_items_search_post**](ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_search_post) | **POST** /api/v2/projects/{projectId}/workItems/search | Search for work items
[**api_v2_projects_project_id_work_items_tags_get**](ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_tags_get) | **GET** /api/v2/projects/{projectId}/workItems/tags | Get WorkItems Tags
[**get_work_items_by_project_id**](ProjectWorkItemsApi.md#get_work_items_by_project_id) | **GET** /api/v2/projects/{projectId}/workItems | Get project work items


# **api_v2_projects_project_id_work_items_search_grouped_post**
> List[WorkItemGroupModel] api_v2_projects_project_id_work_items_search_grouped_post(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_group_get_model=work_item_group_get_model)

Search for work items and group results by attribute

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_group_get_model import WorkItemGroupGetModel
from testit_api_client.models.work_item_group_model import WorkItemGroupModel
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
    api_instance = testit_api_client.ProjectWorkItemsApi(api_client)
    project_id = 'project_id_example' # str | Unique or global ID of the project
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    work_item_group_get_model = testit_api_client.WorkItemGroupGetModel() # WorkItemGroupGetModel |  (optional)

    try:
        # Search for work items and group results by attribute
        api_response = api_instance.api_v2_projects_project_id_work_items_search_grouped_post(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_group_get_model=work_item_group_get_model)
        print("The response of ProjectWorkItemsApi->api_v2_projects_project_id_work_items_search_grouped_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkItemsApi->api_v2_projects_project_id_work_items_search_grouped_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global ID of the project | 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **work_item_group_get_model** | [**WorkItemGroupGetModel**](WorkItemGroupGetModel.md)|  | [optional] 

### Return type

[**List[WorkItemGroupModel]**](WorkItemGroupModel.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_work_items_search_id_post**
> List[str] api_v2_projects_project_id_work_items_search_id_post(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_select_model=work_item_select_model)

Search for work items and extract IDs only

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
    api_instance = testit_api_client.ProjectWorkItemsApi(api_client)
    project_id = 'project_id_example' # str | Unique or global ID of the project
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    work_item_select_model = testit_api_client.WorkItemSelectModel() # WorkItemSelectModel |  (optional)

    try:
        # Search for work items and extract IDs only
        api_response = api_instance.api_v2_projects_project_id_work_items_search_id_post(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_select_model=work_item_select_model)
        print("The response of ProjectWorkItemsApi->api_v2_projects_project_id_work_items_search_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkItemsApi->api_v2_projects_project_id_work_items_search_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global ID of the project | 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **work_item_select_model** | [**WorkItemSelectModel**](WorkItemSelectModel.md)|  | [optional] 

### Return type

**List[str]**

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
**403** | Read permission for test library is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_work_items_search_post**
> List[WorkItemShortModel] api_v2_projects_project_id_work_items_search_post(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_select_model=work_item_select_model)

Search for work items

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.work_item_select_model import WorkItemSelectModel
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
    api_instance = testit_api_client.ProjectWorkItemsApi(api_client)
    project_id = 'project_id_example' # str | Unique or global ID of the project
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    work_item_select_model = testit_api_client.WorkItemSelectModel() # WorkItemSelectModel |  (optional)

    try:
        # Search for work items
        api_response = api_instance.api_v2_projects_project_id_work_items_search_post(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_select_model=work_item_select_model)
        print("The response of ProjectWorkItemsApi->api_v2_projects_project_id_work_items_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkItemsApi->api_v2_projects_project_id_work_items_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Unique or global ID of the project | 
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **work_item_select_model** | [**WorkItemSelectModel**](WorkItemSelectModel.md)|  | [optional] 

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
**200** | OK |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_work_items_tags_get**
> List[TagShortModel] api_v2_projects_project_id_work_items_tags_get(project_id, is_deleted=is_deleted)

Get WorkItems Tags

 Use case   User sets project internal identifier    User runs method execution   System returns work items tags

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.tag_short_model import TagShortModel
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
    api_instance = testit_api_client.ProjectWorkItemsApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) identifier
    is_deleted = True # bool |  (optional)

    try:
        # Get WorkItems Tags
        api_response = api_instance.api_v2_projects_project_id_work_items_tags_get(project_id, is_deleted=is_deleted)
        print("The response of ProjectWorkItemsApi->api_v2_projects_project_id_work_items_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkItemsApi->api_v2_projects_project_id_work_items_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) identifier | 
 **is_deleted** | **bool**|  | [optional] 

### Return type

[**List[TagShortModel]**](TagShortModel.md)

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

# **get_work_items_by_project_id**
> List[WorkItemShortModel] get_work_items_by_project_id(project_id, is_deleted=is_deleted, tag_names=tag_names, include_iterations=include_iterations, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get project work items

 Use case   User sets project internal or global identifier   [Optional] User sets isDeleted field value   User runs method execution   System search project   [Optional] If User sets isDeleted field value as true, System search all deleted workitems related to project   [Optional] If User sets isDeleted field value as false, System search all workitems related to project which are not deleted   If User did not set isDeleted field value, System search all  workitems related to project   System returns array of found workitems (listed in response model)

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
    api_instance = testit_api_client.ProjectWorkItemsApi(api_client)
    project_id = 'project_id_example' # str | Project internal (UUID) or global (integer) identifier
    is_deleted = False # bool | If result must consist of only actual/deleted work items (optional) (default to False)
    tag_names = ['tag_names_example'] # List[str] | List of tags to filter by (optional)
    include_iterations = True # bool |  (optional) (default to True)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get project work items
        api_response = api_instance.get_work_items_by_project_id(project_id, is_deleted=is_deleted, tag_names=tag_names, include_iterations=include_iterations, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of ProjectWorkItemsApi->get_work_items_by_project_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectWorkItemsApi->get_work_items_by_project_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier | 
 **is_deleted** | **bool**| If result must consist of only actual/deleted work items | [optional] [default to False]
 **tag_names** | [**List[str]**](str.md)| List of tags to filter by | [optional] 
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
**400** |  - &#x60;orderBy&#x60; statement must have one &#x60;.&#x60; and no &#x60;,&#x60; characters   - &#x60;orderBy&#x60; statement has invalid length   - &#x60;orderBy&#x60; statement must have UUID as attribute key   - Search field was not found |  -  |
**401** | Unauthorized |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

