# testit_api_client.CustomAttributeTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_custom_attributes_templates_id_custom_attributes_exclude_post**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_custom_attributes_exclude_post) | **POST** /api/v2/customAttributes/templates/{id}/customAttributes/exclude | Exclude CustomAttributes from CustomAttributeTemplate
[**api_v2_custom_attributes_templates_id_custom_attributes_include_post**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_custom_attributes_include_post) | **POST** /api/v2/customAttributes/templates/{id}/customAttributes/include | Include CustomAttributes to CustomAttributeTemplate
[**api_v2_custom_attributes_templates_id_delete**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_delete) | **DELETE** /api/v2/customAttributes/templates/{id} | Delete CustomAttributeTemplate
[**api_v2_custom_attributes_templates_id_get**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_get) | **GET** /api/v2/customAttributes/templates/{id} | Get CustomAttributeTemplate by ID
[**api_v2_custom_attributes_templates_name_get**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_name_get) | **GET** /api/v2/customAttributes/templates/{name} | Get CustomAttributeTemplate by name
[**api_v2_custom_attributes_templates_post**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_post) | **POST** /api/v2/customAttributes/templates | Create CustomAttributeTemplate
[**api_v2_custom_attributes_templates_put**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_put) | **PUT** /api/v2/customAttributes/templates | Update custom attributes template
[**api_v2_custom_attributes_templates_search_post**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_search_post) | **POST** /api/v2/customAttributes/templates/search | Search CustomAttributeTemplates


# **api_v2_custom_attributes_templates_id_custom_attributes_exclude_post**
> api_v2_custom_attributes_templates_id_custom_attributes_exclude_post(id)

Exclude CustomAttributes from CustomAttributeTemplate

<br>Use case  <br>User sets attribute template internal identifier  <br>User sets attribute internal identifiers   <br>User runs method execution  <br>System delete attributes from attributes tempalte

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attribute_templates_api
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
    api_instance = custom_attribute_templates_api.CustomAttributeTemplatesApi(api_client)
    id = "id_example" # str | Attribute template internal (UUID) identifier
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Exclude CustomAttributes from CustomAttributeTemplate
        api_instance.api_v2_custom_attributes_templates_id_custom_attributes_exclude_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_id_custom_attributes_exclude_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Exclude CustomAttributes from CustomAttributeTemplate
        api_instance.api_v2_custom_attributes_templates_id_custom_attributes_exclude_post(id, request_body=request_body)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_id_custom_attributes_exclude_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Attribute template internal (UUID) identifier |
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**403** | Admin system role is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_id_custom_attributes_include_post**
> api_v2_custom_attributes_templates_id_custom_attributes_include_post(id)

Include CustomAttributes to CustomAttributeTemplate

<br>Use case  <br>User sets attribute template internal identifier  <br>User sets attribute internal identifiers   <br>User runs method execution  <br>System add attributes to attributes tempalte

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attribute_templates_api
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
    api_instance = custom_attribute_templates_api.CustomAttributeTemplatesApi(api_client)
    id = "id_example" # str | Attribute template internal (UUID) identifier
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Include CustomAttributes to CustomAttributeTemplate
        api_instance.api_v2_custom_attributes_templates_id_custom_attributes_include_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_id_custom_attributes_include_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Include CustomAttributes to CustomAttributeTemplate
        api_instance.api_v2_custom_attributes_templates_id_custom_attributes_include_post(id, request_body=request_body)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_id_custom_attributes_include_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Attribute template internal (UUID) identifier |
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**403** | Admin system role is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_id_delete**
> NoContentResult api_v2_custom_attributes_templates_id_delete(id)

Delete CustomAttributeTemplate

<br>Use case  <br>User sets attribute template internal identifier  <br>User runs method execution  <br>System search and delete attribute template  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attribute_templates_api
from testit_api_client.model.no_content_result import NoContentResult
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
    api_instance = custom_attribute_templates_api.CustomAttributeTemplatesApi(api_client)
    id = "id_example" # str | Attribute template internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete CustomAttributeTemplate
        api_response = api_instance.api_v2_custom_attributes_templates_id_delete(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Attribute template internal (UUID) identifier |

### Return type

[**NoContentResult**](NoContentResult.md)

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
**403** | Admin system role is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_id_get**
> CustomAttributeTemplateModel api_v2_custom_attributes_templates_id_get(id)

Get CustomAttributeTemplate by ID

<br>Use case  <br>User sets attribute template internal identifier   <br>User runs method execution  <br>System return attribute template (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attribute_templates_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_template_model import CustomAttributeTemplateModel
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
    api_instance = custom_attribute_templates_api.CustomAttributeTemplatesApi(api_client)
    id = "id_example" # str | CustomAttributeTemplate internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get CustomAttributeTemplate by ID
        api_response = api_instance.api_v2_custom_attributes_templates_id_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**200** | Success |  -  |
**400** | Bad Request |  -  |
**404** | Can&#39;t find a CustomAttributeTemplate with identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_name_get**
> CustomAttributeTemplateModel api_v2_custom_attributes_templates_name_get(name)

Get CustomAttributeTemplate by name

<br>Use case  <br>User sets attribute template name  <br>User runs method execution  <br>System search and return list of attribute templates (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attribute_templates_api
from testit_api_client.model.custom_attribute_template_model import CustomAttributeTemplateModel
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
    api_instance = custom_attribute_templates_api.CustomAttributeTemplatesApi(api_client)
    name = "name_example" # str | CustomAttributeTemplate name for search

    # example passing only required values which don't have defaults set
    try:
        # Get CustomAttributeTemplate by name
        api_response = api_instance.api_v2_custom_attributes_templates_name_get(name)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_post**
> CustomAttributeTemplateModel api_v2_custom_attributes_templates_post()

Create CustomAttributeTemplate

<br>Use case  <br>User sets attribute template parameters (listed in request example)  <br>User runs method execution  <br>System creates attribute template  <br>System returns attribute template model (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attribute_templates_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_template_model import CustomAttributeTemplateModel
from testit_api_client.model.validate_anti_forgery_token_attribute import ValidateAntiForgeryTokenAttribute
from testit_api_client.model.api_v2_custom_attributes_templates_post_request import ApiV2CustomAttributesTemplatesPostRequest
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
    api_instance = custom_attribute_templates_api.CustomAttributeTemplatesApi(api_client)
    api_v2_custom_attributes_templates_post_request = ApiV2CustomAttributesTemplatesPostRequest(None) # ApiV2CustomAttributesTemplatesPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create CustomAttributeTemplate
        api_response = api_instance.api_v2_custom_attributes_templates_post(api_v2_custom_attributes_templates_post_request=api_v2_custom_attributes_templates_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_custom_attributes_templates_post_request** | [**ApiV2CustomAttributesTemplatesPostRequest**](ApiV2CustomAttributesTemplatesPostRequest.md)|  | [optional]

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
**403** | Admin system role is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_put**
> api_v2_custom_attributes_templates_put()

Update custom attributes template

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attribute_templates_api
from testit_api_client.model.api_v2_custom_attributes_templates_put_request import ApiV2CustomAttributesTemplatesPutRequest
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
    api_instance = custom_attribute_templates_api.CustomAttributeTemplatesApi(api_client)
    api_v2_custom_attributes_templates_put_request = ApiV2CustomAttributesTemplatesPutRequest(None) # ApiV2CustomAttributesTemplatesPutRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update custom attributes template
        api_instance.api_v2_custom_attributes_templates_put(api_v2_custom_attributes_templates_put_request=api_v2_custom_attributes_templates_put_request)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_v2_custom_attributes_templates_put_request** | [**ApiV2CustomAttributesTemplatesPutRequest**](ApiV2CustomAttributesTemplatesPutRequest.md)|  | [optional]

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
**200** | Success |  -  |
**403** | System administrator role is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_search_post**
> [SearchCustomAttributeTemplateGetModel] api_v2_custom_attributes_templates_search_post()

Search CustomAttributeTemplates

<br>Use case  <br>User sets search params model (listed in request example)  <br>User runs method execution  <br>System return attribute templates (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attribute_templates_api
from testit_api_client.model.api_v2_custom_attributes_templates_search_post_request import ApiV2CustomAttributesTemplatesSearchPostRequest
from testit_api_client.model.search_custom_attribute_template_get_model import SearchCustomAttributeTemplateGetModel
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
    api_instance = custom_attribute_templates_api.CustomAttributeTemplatesApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    api_v2_custom_attributes_templates_search_post_request = ApiV2CustomAttributesTemplatesSearchPostRequest(None) # ApiV2CustomAttributesTemplatesSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search CustomAttributeTemplates
        api_response = api_instance.api_v2_custom_attributes_templates_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, api_v2_custom_attributes_templates_search_post_request=api_v2_custom_attributes_templates_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
 **api_v2_custom_attributes_templates_search_post_request** | [**ApiV2CustomAttributesTemplatesSearchPostRequest**](ApiV2CustomAttributesTemplatesSearchPostRequest.md)|  | [optional]

### Return type

[**[SearchCustomAttributeTemplateGetModel]**](SearchCustomAttributeTemplateGetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

