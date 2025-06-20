# testit_api_client.CustomAttributeTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_custom_attributes_templates_exists_get**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_exists_get) | **GET** /api/v2/customAttributes/templates/exists | 
[**api_v2_custom_attributes_templates_id_custom_attributes_exclude_post**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_custom_attributes_exclude_post) | **POST** /api/v2/customAttributes/templates/{id}/customAttributes/exclude | Exclude CustomAttributes from CustomAttributeTemplate
[**api_v2_custom_attributes_templates_id_custom_attributes_include_post**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_custom_attributes_include_post) | **POST** /api/v2/customAttributes/templates/{id}/customAttributes/include | Include CustomAttributes to CustomAttributeTemplate
[**api_v2_custom_attributes_templates_id_delete**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_delete) | **DELETE** /api/v2/customAttributes/templates/{id} | Delete CustomAttributeTemplate
[**api_v2_custom_attributes_templates_id_get**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_get) | **GET** /api/v2/customAttributes/templates/{id} | Get CustomAttributeTemplate by ID
[**api_v2_custom_attributes_templates_name_get**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_name_get) | **GET** /api/v2/customAttributes/templates/{name} | Get CustomAttributeTemplate by name
[**api_v2_custom_attributes_templates_post**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_post) | **POST** /api/v2/customAttributes/templates | Create CustomAttributeTemplate
[**api_v2_custom_attributes_templates_put**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_put) | **PUT** /api/v2/customAttributes/templates | Update custom attributes template
[**api_v2_custom_attributes_templates_search_post**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_search_post) | **POST** /api/v2/customAttributes/templates/search | Search CustomAttributeTemplates


# **api_v2_custom_attributes_templates_exists_get**
> CustomAttributeTemplateValidationResult api_v2_custom_attributes_templates_exists_get(name=name)





### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
from testit_api_client.models.custom_attribute_template_validation_result import CustomAttributeTemplateValidationResult
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
    api_instance = testit_api_client.CustomAttributeTemplatesApi(api_client)
    name = 'name_example' # str |  (optional)

    try:
        api_response = api_instance.api_v2_custom_attributes_templates_exists_get(name=name)
        print("The response of CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_exists_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_exists_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**CustomAttributeTemplateValidationResult**](CustomAttributeTemplateValidationResult.md)

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

# **api_v2_custom_attributes_templates_id_custom_attributes_exclude_post**
> api_v2_custom_attributes_templates_id_custom_attributes_exclude_post(id, request_body=request_body)

Exclude CustomAttributes from CustomAttributeTemplate


Use case

User sets attribute template internal identifier

User sets attribute internal identifiers

User runs method execution

System delete attributes from attributes tempalte

### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
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
    api_instance = testit_api_client.CustomAttributeTemplatesApi(api_client)
    id = 'id_example' # str | Attribute template internal (UUID) identifier
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Exclude CustomAttributes from CustomAttributeTemplate
        api_instance.api_v2_custom_attributes_templates_id_custom_attributes_exclude_post(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_id_custom_attributes_exclude_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Attribute template internal (UUID) identifier | 
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Admin system role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_id_custom_attributes_include_post**
> api_v2_custom_attributes_templates_id_custom_attributes_include_post(id, request_body=request_body)

Include CustomAttributes to CustomAttributeTemplate


Use case

User sets attribute template internal identifier

User sets attribute internal identifiers

User runs method execution

System add attributes to attributes tempalte

### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
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
    api_instance = testit_api_client.CustomAttributeTemplatesApi(api_client)
    id = 'id_example' # str | Attribute template internal (UUID) identifier
    request_body = ['request_body_example'] # List[str] |  (optional)

    try:
        # Include CustomAttributes to CustomAttributeTemplate
        api_instance.api_v2_custom_attributes_templates_id_custom_attributes_include_post(id, request_body=request_body)
    except Exception as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_id_custom_attributes_include_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Attribute template internal (UUID) identifier | 
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Admin system role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_id_delete**
> api_v2_custom_attributes_templates_id_delete(id)

Delete CustomAttributeTemplate


Use case

User sets attribute template internal identifier

User runs method execution

System search and delete attribute template

System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
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
    api_instance = testit_api_client.CustomAttributeTemplatesApi(api_client)
    id = 'id_example' # str | Attribute template internal (UUID) identifier

    try:
        # Delete CustomAttributeTemplate
        api_instance.api_v2_custom_attributes_templates_id_delete(id)
    except Exception as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Attribute template internal (UUID) identifier | 

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
**403** | Admin system role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_id_get**
> CustomAttributeTemplateModel api_v2_custom_attributes_templates_id_get(id)

Get CustomAttributeTemplate by ID


Use case

User sets attribute template internal identifier

User runs method execution

System return attribute template (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
from testit_api_client.models.custom_attribute_template_model import CustomAttributeTemplateModel
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
    api_instance = testit_api_client.CustomAttributeTemplatesApi(api_client)
    id = 'id_example' # str | CustomAttributeTemplate internal (UUID) identifier

    try:
        # Get CustomAttributeTemplate by ID
        api_response = api_instance.api_v2_custom_attributes_templates_id_get(id)
        print("The response of CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CustomAttributeTemplate internal (UUID) identifier | 

### Return type

[**CustomAttributeTemplateModel**](CustomAttributeTemplateModel.md)

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
**404** | Can&#39;t find a CustomAttributeTemplate with identifier |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_name_get**
> CustomAttributeTemplateModel api_v2_custom_attributes_templates_name_get(name)

Get CustomAttributeTemplate by name


Use case

User sets attribute template name

User runs method execution

System search and return list of attribute templates (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
from testit_api_client.models.custom_attribute_template_model import CustomAttributeTemplateModel
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
    api_instance = testit_api_client.CustomAttributeTemplatesApi(api_client)
    name = 'name_example' # str | CustomAttributeTemplate name for search

    try:
        # Get CustomAttributeTemplate by name
        api_response = api_instance.api_v2_custom_attributes_templates_name_get(name)
        print("The response of CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_name_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| CustomAttributeTemplate name for search | 

### Return type

[**CustomAttributeTemplateModel**](CustomAttributeTemplateModel.md)

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

# **api_v2_custom_attributes_templates_post**
> CustomAttributeTemplateModel api_v2_custom_attributes_templates_post(custom_attribute_template_post_model=custom_attribute_template_post_model)

Create CustomAttributeTemplate


Use case

User sets attribute template parameters (listed in request example)

User runs method execution

System creates attribute template

System returns attribute template model (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
from testit_api_client.models.custom_attribute_template_model import CustomAttributeTemplateModel
from testit_api_client.models.custom_attribute_template_post_model import CustomAttributeTemplatePostModel
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
    api_instance = testit_api_client.CustomAttributeTemplatesApi(api_client)
    custom_attribute_template_post_model = testit_api_client.CustomAttributeTemplatePostModel() # CustomAttributeTemplatePostModel |  (optional)

    try:
        # Create CustomAttributeTemplate
        api_response = api_instance.api_v2_custom_attributes_templates_post(custom_attribute_template_post_model=custom_attribute_template_post_model)
        print("The response of CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute_template_post_model** | [**CustomAttributeTemplatePostModel**](CustomAttributeTemplatePostModel.md)|  | [optional] 

### Return type

[**CustomAttributeTemplateModel**](CustomAttributeTemplateModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Admin system role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_put**
> api_v2_custom_attributes_templates_put(custom_attribute_template_put_model=custom_attribute_template_put_model)

Update custom attributes template



### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
from testit_api_client.models.custom_attribute_template_put_model import CustomAttributeTemplatePutModel
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
    api_instance = testit_api_client.CustomAttributeTemplatesApi(api_client)
    custom_attribute_template_put_model = testit_api_client.CustomAttributeTemplatePutModel() # CustomAttributeTemplatePutModel |  (optional)

    try:
        # Update custom attributes template
        api_instance.api_v2_custom_attributes_templates_put(custom_attribute_template_put_model=custom_attribute_template_put_model)
    except Exception as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute_template_put_model** | [**CustomAttributeTemplatePutModel**](CustomAttributeTemplatePutModel.md)|  | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | System administrator role is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_search_post**
> List[SearchCustomAttributeTemplateGetModel] api_v2_custom_attributes_templates_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, custom_attribute_template_search_query_model=custom_attribute_template_search_query_model)

Search CustomAttributeTemplates


Use case

User sets search params model (listed in request example)

User runs method execution

System return attribute templates (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):
```python
import time
import os
import testit_api_client
from testit_api_client.models.custom_attribute_template_search_query_model import CustomAttributeTemplateSearchQueryModel
from testit_api_client.models.search_custom_attribute_template_get_model import SearchCustomAttributeTemplateGetModel
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
    api_instance = testit_api_client.CustomAttributeTemplatesApi(api_client)
    skip = 56 # int | Amount of items to be skipped (offset) (optional)
    take = 56 # int | Amount of items to be taken (limit) (optional)
    order_by = 'order_by_example' # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = 'search_field_example' # str | Property name for searching (optional)
    search_value = 'search_value_example' # str | Value for searching (optional)
    custom_attribute_template_search_query_model = testit_api_client.CustomAttributeTemplateSearchQueryModel() # CustomAttributeTemplateSearchQueryModel |  (optional)

    try:
        # Search CustomAttributeTemplates
        api_response = api_instance.api_v2_custom_attributes_templates_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, custom_attribute_template_search_query_model=custom_attribute_template_search_query_model)
        print("The response of CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_search_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional] 
 **take** | **int**| Amount of items to be taken (limit) | [optional] 
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional] 
 **search_field** | **str**| Property name for searching | [optional] 
 **search_value** | **str**| Value for searching | [optional] 
 **custom_attribute_template_search_query_model** | [**CustomAttributeTemplateSearchQueryModel**](CustomAttributeTemplateSearchQueryModel.md)|  | [optional] 

### Return type

[**List[SearchCustomAttributeTemplateGetModel]**](SearchCustomAttributeTemplateGetModel.md)

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

