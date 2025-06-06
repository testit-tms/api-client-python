# testit_api_client.TagsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_tags_delete**](TagsApi.md#api_v2_tags_delete) | **DELETE** /api/v2/tags | Delete tags
[**api_v2_tags_id_delete**](TagsApi.md#api_v2_tags_id_delete) | **DELETE** /api/v2/tags/{id} | Delete tag
[**api_v2_tags_post**](TagsApi.md#api_v2_tags_post) | **POST** /api/v2/tags | Create tag
[**api_v2_tags_put**](TagsApi.md#api_v2_tags_put) | **PUT** /api/v2/tags | Update tag
[**api_v2_tags_search_get**](TagsApi.md#api_v2_tags_search_get) | **GET** /api/v2/tags/search | Search tags
[**api_v2_tags_test_plans_tags_get**](TagsApi.md#api_v2_tags_test_plans_tags_get) | **GET** /api/v2/tags/testPlansTags | Get all Tags that are used in TestPlans


# **api_v2_tags_delete**
> api_v2_tags_delete(select_tags_api_model=select_tags_api_model)

Delete tags

 Use case  User sets collection of tags internal (guid format) identifiers  System searches and deletes a collection of tags

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.select_tags_api_model import SelectTagsApiModel
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
    api_instance = testit_api_client.TagsApi(api_client)
    select_tags_api_model = testit_api_client.SelectTagsApiModel() # SelectTagsApiModel |  (optional)

    try:
        # Delete tags
        api_instance.api_v2_tags_delete(select_tags_api_model=select_tags_api_model)
    except Exception as e:
        print("Exception when calling TagsApi->api_v2_tags_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select_tags_api_model** | [**SelectTagsApiModel**](SelectTagsApiModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** |  - ID is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | System administrator role is required |  -  |
**404** | No tags with provided IDs were found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_id_delete**
> api_v2_tags_id_delete(id)

Delete tag

 Use case  User sets tag internal (guid format) identifier  System search and delete tag

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
    api_instance = testit_api_client.TagsApi(api_client)
    id = 'id_example' # str | Tag internal (UUID) identifier

    try:
        # Delete tag
        api_instance.api_v2_tags_id_delete(id)
    except Exception as e:
        print("Exception when calling TagsApi->api_v2_tags_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Tag internal (UUID) identifier | 

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
**400** |  - ID is not valid |  -  |
**401** | Unauthorized |  -  |
**403** | System administrator role is required |  -  |
**404** | Tag with provided ID cannot be found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_post**
> TagApiResult api_v2_tags_post(create_tag_api_model=create_tag_api_model)

Create tag

 Use case  User sets tag model (listed in the request example)  User runs method execution  System creates tag  System returns tag model (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.create_tag_api_model import CreateTagApiModel
from testit_api_client.models.tag_api_result import TagApiResult
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
    api_instance = testit_api_client.TagsApi(api_client)
    create_tag_api_model = testit_api_client.CreateTagApiModel() # CreateTagApiModel |  (optional)

    try:
        # Create tag
        api_response = api_instance.api_v2_tags_post(create_tag_api_model=create_tag_api_model)
        print("The response of TagsApi->api_v2_tags_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->api_v2_tags_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tag_api_model** | [**CreateTagApiModel**](CreateTagApiModel.md)|  | [optional] 

### Return type

[**TagApiResult**](TagApiResult.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful operation |  -  |
**400** |  - Name cannot be empty or contain only white space characters  - Name already in use  - Name must be no more than 30 characters long |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_put**
> TagApiResult api_v2_tags_put(id=id, update_tag_api_model=update_tag_api_model)

Update tag

 Use case  User sets tag ID and model (listed in the request example)  User runs method execution  System updates tag  System returns tag model (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.tag_api_result import TagApiResult
from testit_api_client.models.update_tag_api_model import UpdateTagApiModel
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
    api_instance = testit_api_client.TagsApi(api_client)
    id = 'id_example' # str |  (optional)
    update_tag_api_model = testit_api_client.UpdateTagApiModel() # UpdateTagApiModel |  (optional)

    try:
        # Update tag
        api_response = api_instance.api_v2_tags_put(id=id, update_tag_api_model=update_tag_api_model)
        print("The response of TagsApi->api_v2_tags_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->api_v2_tags_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **update_tag_api_model** | [**UpdateTagApiModel**](UpdateTagApiModel.md)|  | [optional] 

### Return type

[**TagApiResult**](TagApiResult.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** |  - ID is not valid  - Name cannot be empty or contain only white space characters  - Name already in use  - Name must be no more than 30 characters long |  -  |
**401** | Unauthorized |  -  |
**403** | Project creator role is required |  -  |
**404** | Tag with provided ID cannot be found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_search_get**
> List[TagApiResult] api_v2_tags_search_get(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Search tags

 Use case  User runs method execution  System returns collection of tags (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.tag_api_result import TagApiResult
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
    api_instance = testit_api_client.TagsApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Search tags
        api_response = api_instance.api_v2_tags_search_get(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of TagsApi->api_v2_tags_search_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->api_v2_tags_search_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 

### Return type

[**List[TagApiResult]**](TagApiResult.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** |  orderByStatement must have one &#39;.&#39; and no &#39;,&#39; symbols  orderByStatement has invalid length  orderByStatement must have uuid as attribute key  Search field not found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_tags_test_plans_tags_get**
> List[TagApiResult] api_v2_tags_test_plans_tags_get(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)

Get all Tags that are used in TestPlans

 Use case  User runs method execution  System returns tags (listed in the response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import testit_api_client
from testit_api_client.models.tag_api_result import TagApiResult
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
    api_instance = testit_api_client.TagsApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)

    try:
        # Get all Tags that are used in TestPlans
        api_response = api_instance.api_v2_tags_test_plans_tags_get(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        print("The response of TagsApi->api_v2_tags_test_plans_tags_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TagsApi->api_v2_tags_test_plans_tags_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 

### Return type

[**List[TagApiResult]**](TagApiResult.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** |  orderByStatement must have one &#39;.&#39; and no &#39;,&#39; symbols  orderByStatement has invalid length  orderByStatement must have uuid as attribute key  Search field not found |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

