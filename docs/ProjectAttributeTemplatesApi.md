# testit_api_client.ProjectAttributeTemplatesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v2_projects_project_id_attributes_templates_search_post**](ProjectAttributeTemplatesApi.md#api_v2_projects_project_id_attributes_templates_search_post) | **POST** /api/v2/projects/{projectId}/attributes/templates/search | Search for custom attributes templates
[**api_v2_projects_project_id_attributes_templates_template_id_delete**](ProjectAttributeTemplatesApi.md#api_v2_projects_project_id_attributes_templates_template_id_delete) | **DELETE** /api/v2/projects/{projectId}/attributes/templates/{templateId} | Delete CustomAttributeTemplate from Project
[**api_v2_projects_project_id_attributes_templates_template_id_post**](ProjectAttributeTemplatesApi.md#api_v2_projects_project_id_attributes_templates_template_id_post) | **POST** /api/v2/projects/{projectId}/attributes/templates/{templateId} | Add CustomAttributeTemplate to Project


# **api_v2_projects_project_id_attributes_templates_search_post**
> [ProjectCustomAttributeTemplateGetModel] api_v2_projects_project_id_attributes_templates_search_post(project_id)

Search for custom attributes templates

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_attribute_templates_api
from testit_api_client.model.api_v2_projects_project_id_attributes_templates_search_post_request import ApiV2ProjectsProjectIdAttributesTemplatesSearchPostRequest
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_custom_attribute_template_get_model import ProjectCustomAttributeTemplateGetModel
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
    api_instance = project_attribute_templates_api.ProjectAttributeTemplatesApi(api_client)
    project_id = "projectId_example" # str | Internal (UUID) or global (integer) identifier
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    api_v2_projects_project_id_attributes_templates_search_post_request = ApiV2ProjectsProjectIdAttributesTemplatesSearchPostRequest(None) # ApiV2ProjectsProjectIdAttributesTemplatesSearchPostRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for custom attributes templates
        api_response = api_instance.api_v2_projects_project_id_attributes_templates_search_post(project_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectAttributeTemplatesApi->api_v2_projects_project_id_attributes_templates_search_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for custom attributes templates
        api_response = api_instance.api_v2_projects_project_id_attributes_templates_search_post(project_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, api_v2_projects_project_id_attributes_templates_search_post_request=api_v2_projects_project_id_attributes_templates_search_post_request)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectAttributeTemplatesApi->api_v2_projects_project_id_attributes_templates_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Internal (UUID) or global (integer) identifier |
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **api_v2_projects_project_id_attributes_templates_search_post_request** | [**ApiV2ProjectsProjectIdAttributesTemplatesSearchPostRequest**](ApiV2ProjectsProjectIdAttributesTemplatesSearchPostRequest.md)|  | [optional]

### Return type

[**[ProjectCustomAttributeTemplateGetModel]**](ProjectCustomAttributeTemplateGetModel.md)

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
**403** | Project admin permission for project settings is required |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_attributes_templates_template_id_delete**
> api_v2_projects_project_id_attributes_templates_template_id_delete(project_id, template_id)

Delete CustomAttributeTemplate from Project

  Use case    User sets project internal or global identifier    User sets attribute template internal identifier    User runs method execution    System delete attribute template from project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_attribute_templates_api
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
    api_instance = project_attribute_templates_api.ProjectAttributeTemplatesApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    template_id = "templateId_example" # str | CustomAttributeTemplate internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete CustomAttributeTemplate from Project
        api_instance.api_v2_projects_project_id_attributes_templates_template_id_delete(project_id, template_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectAttributeTemplatesApi->api_v2_projects_project_id_attributes_templates_template_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **template_id** | **str**| CustomAttributeTemplate internal (UUID) identifier |

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
**403** | Update project settings permission for project required |  -  |
**404** | Can&#39;t find a Project with identifier |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_project_id_attributes_templates_template_id_post**
> api_v2_projects_project_id_attributes_templates_template_id_post(project_id, template_id)

Add CustomAttributeTemplate to Project

  Use case    User sets project internal or global identifier    User sets attribute template internal identifier    User runs method execution    System add attribute template to project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import project_attribute_templates_api
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
    api_instance = project_attribute_templates_api.ProjectAttributeTemplatesApi(api_client)
    project_id = "projectId_example" # str | Project internal (UUID) or global (integer) identifier
    template_id = "templateId_example" # str | CustomAttributeTemplate internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Add CustomAttributeTemplate to Project
        api_instance.api_v2_projects_project_id_attributes_templates_template_id_post(project_id, template_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectAttributeTemplatesApi->api_v2_projects_project_id_attributes_templates_template_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project internal (UUID) or global (integer) identifier |
 **template_id** | **str**| CustomAttributeTemplate internal (UUID) identifier |

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Update project settings permission for project required |  -  |
**404** | Can&#39;t find a Project with identifier |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

