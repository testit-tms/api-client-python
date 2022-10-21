# testit_api_client.CustomAttributesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_custom_attributes_id_delete**](CustomAttributesApi.md#api_v2_custom_attributes_id_delete) | **DELETE** /api/v2/customAttributes/{id} | 
[**api_v2_custom_attributes_id_get**](CustomAttributesApi.md#api_v2_custom_attributes_id_get) | **GET** /api/v2/customAttributes/{id} | 
[**api_v2_custom_attributes_id_make_global_post**](CustomAttributesApi.md#api_v2_custom_attributes_id_make_global_post) | **POST** /api/v2/customAttributes/{id}/makeGlobal | 
[**api_v2_custom_attributes_id_projects_get**](CustomAttributesApi.md#api_v2_custom_attributes_id_projects_get) | **GET** /api/v2/customAttributes/{id}/projects | 
[**api_v2_custom_attributes_id_put**](CustomAttributesApi.md#api_v2_custom_attributes_id_put) | **PUT** /api/v2/customAttributes/{id} | 
[**api_v2_custom_attributes_merge_post**](CustomAttributesApi.md#api_v2_custom_attributes_merge_post) | **POST** /api/v2/customAttributes/merge | 
[**api_v2_custom_attributes_order_post**](CustomAttributesApi.md#api_v2_custom_attributes_order_post) | **POST** /api/v2/customAttributes/order | 
[**api_v2_custom_attributes_post**](CustomAttributesApi.md#api_v2_custom_attributes_post) | **POST** /api/v2/customAttributes | 
[**api_v2_custom_attributes_replace_post**](CustomAttributesApi.md#api_v2_custom_attributes_replace_post) | **POST** /api/v2/customAttributes/replace | 
[**api_v2_custom_attributes_search_post**](CustomAttributesApi.md#api_v2_custom_attributes_search_post) | **POST** /api/v2/customAttributes/search | 


# **api_v2_custom_attributes_id_delete**
> api_v2_custom_attributes_id_delete(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_v2_custom_attributes_id_delete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_id_get**
> CustomAttributeModel api_v2_custom_attributes_id_get(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_custom_attributes_id_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_id_make_global_post**
> api_v2_custom_attributes_id_make_global_post(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_v2_custom_attributes_id_make_global_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_id_make_global_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

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

# **api_v2_custom_attributes_id_projects_get**
> [ProjectShortestModel] api_v2_custom_attributes_id_projects_get(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.project_shortest_model import ProjectShortestModel
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_custom_attributes_id_projects_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_id_projects_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**[ProjectShortestModel]**](ProjectShortestModel.md)

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

# **api_v2_custom_attributes_id_put**
> api_v2_custom_attributes_id_put(id)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.custom_attribute_update_model import CustomAttributeUpdateModel
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    id = "id_example" # str | 
    custom_attribute_update_model = CustomAttributeUpdateModel(
        name="name_example",
        type=CustomAttributeTypesEnum("string"),
        options=[
            CustomAttributeOptionModel(
                id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
                is_deleted=True,
                value="5 hours",
                is_default=True,
            ),
        ],
        enabled=True,
        required=True,
        is_global=True,
    ) # CustomAttributeUpdateModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_instance.api_v2_custom_attributes_id_put(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_id_put: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.api_v2_custom_attributes_id_put(id, custom_attribute_update_model=custom_attribute_update_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_id_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **custom_attribute_update_model** | [**CustomAttributeUpdateModel**](CustomAttributeUpdateModel.md)|  | [optional]

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

# **api_v2_custom_attributes_merge_post**
> CustomAttributeModel api_v2_custom_attributes_merge_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.custom_attribute_merge_to_global_model import CustomAttributeMergeToGlobalModel
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    custom_attribute_merge_to_global_model = CustomAttributeMergeToGlobalModel(
        merge_custom_attribute_ids=[
            "merge_custom_attribute_ids_example",
        ],
        options=[
            CustomAttributeOptionModel(
                id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
                is_deleted=True,
                value="5 hours",
                is_default=True,
            ),
        ],
        name="Original estimate",
        enabled=True,
        required=True,
        is_global=True,
    ) # CustomAttributeMergeToGlobalModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_custom_attributes_merge_post(custom_attribute_merge_to_global_model=custom_attribute_merge_to_global_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_merge_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute_merge_to_global_model** | [**CustomAttributeMergeToGlobalModel**](CustomAttributeMergeToGlobalModel.md)|  | [optional]

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_order_post**
> api_v2_custom_attributes_order_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.custom_attribute_set_positions_model import CustomAttributeSetPositionsModel
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    custom_attribute_set_positions_model = CustomAttributeSetPositionsModel(
        project_id="project_id_example",
        custom_attribute_ids=[
            "custom_attribute_ids_example",
        ],
    ) # CustomAttributeSetPositionsModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_instance.api_v2_custom_attributes_order_post(custom_attribute_set_positions_model=custom_attribute_set_positions_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_order_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute_set_positions_model** | [**CustomAttributeSetPositionsModel**](CustomAttributeSetPositionsModel.md)|  | [optional]

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

# **api_v2_custom_attributes_post**
> CustomAttributeModel api_v2_custom_attributes_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.custom_attribute_model import CustomAttributeModel
from testit_api_client.model.custom_attribute_post_model import CustomAttributePostModel
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    custom_attribute_post_model = CustomAttributePostModel(
        options=[
            CustomAttributeOptionPostModel(
                value="5 hours",
                is_default=True,
            ),
        ],
        type=CustomAttributeTypesEnum("string"),
        name="Original estimate",
        enabled=True,
        required=True,
        is_global=True,
    ) # CustomAttributePostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_custom_attributes_post(custom_attribute_post_model=custom_attribute_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_replace_post**
> CustomAttributeModel api_v2_custom_attributes_replace_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.custom_attribute_replace_model import CustomAttributeReplaceModel
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    custom_attribute_replace_model = CustomAttributeReplaceModel(
        custom_attribute_options_replace_ids={
            "key": "key_example",
        },
        target_custom_attribute_id="target_custom_attribute_id_example",
        source_custom_attribute_ids=[
            "source_custom_attribute_ids_example",
        ],
    ) # CustomAttributeReplaceModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_custom_attributes_replace_post(custom_attribute_replace_model=custom_attribute_replace_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_replace_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute_replace_model** | [**CustomAttributeReplaceModel**](CustomAttributeReplaceModel.md)|  | [optional]

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_search_post**
> [CustomAttributeModel] api_v2_custom_attributes_search_post()



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attributes_api
from testit_api_client.model.custom_attribute_search_query_model import CustomAttributeSearchQueryModel
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
    api_instance = custom_attributes_api.CustomAttributesApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    custom_attribute_search_query_model = CustomAttributeSearchQueryModel(
        name="name_example",
        project_ids=[
            "project_ids_example",
        ],
        custom_attribute_ids=[
            "custom_attribute_ids_example",
        ],
        custom_attribute_types=[
            CustomAttributeTypesEnum("string"),
        ],
        is_global=True,
        is_deleted=True,
    ) # CustomAttributeSearchQueryModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.api_v2_custom_attributes_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, custom_attribute_search_query_model=custom_attribute_search_query_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributesApi->api_v2_custom_attributes_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **custom_attribute_search_query_model** | [**CustomAttributeSearchQueryModel**](CustomAttributeSearchQueryModel.md)|  | [optional]

### Return type

[**[CustomAttributeModel]**](CustomAttributeModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

