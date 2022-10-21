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
[**api_v2_custom_attributes_templates_put**](CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_put) | **PUT** /api/v2/customAttributes/templates | Update CustomAttributeTemplate
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
**404** | Not Found |  -  |
**200** | Success |  -  |
**400** | Bad Request |  -  |
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
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**200** | Success |  -  |
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
**204** | Success |  -  |
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
> [CustomAttributeTemplateModel] api_v2_custom_attributes_templates_name_get(name)

Get CustomAttributeTemplate by name

<br>Use case  <br>User sets attribute template name  <br>User runs method execution  <br>System search and return list of attribute templates (listed in response example)

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

[**[CustomAttributeTemplateModel]**](CustomAttributeTemplateModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Not Found |  -  |
**200** | Success |  -  |
**400** | Bad Request |  -  |

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
from testit_api_client.model.custom_attribute_template_post_model import CustomAttributeTemplatePostModel
from testit_api_client.model.custom_attribute_template_model import CustomAttributeTemplateModel
from testit_api_client.model.validate_anti_forgery_token_attribute import ValidateAntiForgeryTokenAttribute
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
    custom_attribute_template_post_model = CustomAttributeTemplatePostModel(
        custom_attribute_ids=[
            "custom_attribute_ids_example",
        ],
        name="name_example",
    ) # CustomAttributeTemplatePostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create CustomAttributeTemplate
        api_response = api_instance.api_v2_custom_attributes_templates_post(custom_attribute_template_post_model=custom_attribute_template_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
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
**403** | Admin system role is required |  -  |
**201** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_put**
> api_v2_custom_attributes_templates_put()

Update CustomAttributeTemplate

<br>Use case  <br>User sets attribute template parameters (listed in request example)  <br>User runs method execution  <br>System updates attribute template

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attribute_templates_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_template_put_model import CustomAttributeTemplatePutModel
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
    custom_attribute_template_put_model = CustomAttributeTemplatePutModel(
        id="31337224-8fed-438c-8ab2-aa59e58ce1cd",
        custom_attribute_ids=[
            "custom_attribute_ids_example",
        ],
        name="name_example",
    ) # CustomAttributeTemplatePutModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update CustomAttributeTemplate
        api_instance.api_v2_custom_attributes_templates_put(custom_attribute_template_put_model=custom_attribute_template_put_model)
    except testit_api_client.ApiException as e:
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
**404** | Not Found |  -  |
**200** | Success |  -  |
**403** | Admin system role is required |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_custom_attributes_templates_search_post**
> [CustomAttributeTemplateSearchResponseModel] api_v2_custom_attributes_templates_search_post()

Search CustomAttributeTemplates

<br>Use case  <br>User sets search params model (listed in request example)  <br>User runs method execution  <br>System return attribute templates (listed in response example)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import custom_attribute_templates_api
from testit_api_client.model.custom_attribute_template_search_query_model import CustomAttributeTemplateSearchQueryModel
from testit_api_client.model.custom_attribute_template_search_response_model import CustomAttributeTemplateSearchResponseModel
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
    custom_attribute_template_search_query_model = CustomAttributeTemplateSearchQueryModel(
        name="name_example",
        project_ids=[
            "project_ids_example",
        ],
        custom_attribute_types=[
            CustomAttributeTypesEnum("string"),
        ],
        is_deleted=True,
    ) # CustomAttributeTemplateSearchQueryModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search CustomAttributeTemplates
        api_response = api_instance.api_v2_custom_attributes_templates_search_post(custom_attribute_template_search_query_model=custom_attribute_template_search_query_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling CustomAttributeTemplatesApi->api_v2_custom_attributes_templates_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_attribute_template_search_query_model** | [**CustomAttributeTemplateSearchQueryModel**](CustomAttributeTemplateSearchQueryModel.md)|  | [optional]

### Return type

[**[CustomAttributeTemplateSearchResponseModel]**](CustomAttributeTemplateSearchResponseModel.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

