# testit_api_client.ProjectsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_globa_attributes_to_project**](ProjectsApi.md#add_globa_attributes_to_project) | **POST** /api/v2/projects/{id}/globalAttributes | Add global attributes to project
[**api_v2_projects_id_attributes_templates_search_post**](ProjectsApi.md#api_v2_projects_id_attributes_templates_search_post) | **POST** /api/v2/projects/{id}/attributes/templates/search | Search for custom attributes templates
[**api_v2_projects_id_attributes_templates_template_id_delete**](ProjectsApi.md#api_v2_projects_id_attributes_templates_template_id_delete) | **DELETE** /api/v2/projects/{id}/attributes/templates/{templateId} | Delete CustomAttributeTemplate from Project
[**api_v2_projects_id_attributes_templates_template_id_post**](ProjectsApi.md#api_v2_projects_id_attributes_templates_template_id_post) | **POST** /api/v2/projects/{id}/attributes/templates/{templateId} | Add CustomAttributeTemplate to Project
[**api_v2_projects_id_failure_classes_get**](ProjectsApi.md#api_v2_projects_id_failure_classes_get) | **GET** /api/v2/projects/{id}/failureClasses | Get Project FailureClasses
[**api_v2_projects_id_favorite_put**](ProjectsApi.md#api_v2_projects_id_favorite_put) | **PUT** /api/v2/projects/{id}/favorite | Mark Project as favorite
[**api_v2_projects_id_filters_get**](ProjectsApi.md#api_v2_projects_id_filters_get) | **GET** /api/v2/projects/{id}/filters | Get Project filters
[**api_v2_projects_id_patch**](ProjectsApi.md#api_v2_projects_id_patch) | **PATCH** /api/v2/projects/{id} | Patch project
[**api_v2_projects_id_test_plans_analytics_get**](ProjectsApi.md#api_v2_projects_id_test_plans_analytics_get) | **GET** /api/v2/projects/{id}/testPlans/analytics | Get TestPlans analytics
[**api_v2_projects_id_test_plans_delete_bulk_post**](ProjectsApi.md#api_v2_projects_id_test_plans_delete_bulk_post) | **POST** /api/v2/projects/{id}/testPlans/delete/bulk | Delete multiple test plans
[**api_v2_projects_id_test_plans_name_exists_get**](ProjectsApi.md#api_v2_projects_id_test_plans_name_exists_get) | **GET** /api/v2/projects/{id}/testPlans/{name}/exists | Checks if TestPlan exists with the specified name exists for the project
[**api_v2_projects_id_test_plans_restore_bulk_post**](ProjectsApi.md#api_v2_projects_id_test_plans_restore_bulk_post) | **POST** /api/v2/projects/{id}/testPlans/restore/bulk | Restore multiple test plans
[**api_v2_projects_id_test_plans_search_post**](ProjectsApi.md#api_v2_projects_id_test_plans_search_post) | **POST** /api/v2/projects/{id}/testPlans/search | Get Project TestPlans with analytics
[**api_v2_projects_id_test_runs_active_get**](ProjectsApi.md#api_v2_projects_id_test_runs_active_get) | **GET** /api/v2/projects/{id}/testRuns/active | Get active Project TestRuns
[**api_v2_projects_id_test_runs_full_get**](ProjectsApi.md#api_v2_projects_id_test_runs_full_get) | **GET** /api/v2/projects/{id}/testRuns/full | Get Project TestRuns full models
[**api_v2_projects_id_work_items_search_id_post**](ProjectsApi.md#api_v2_projects_id_work_items_search_id_post) | **POST** /api/v2/projects/{id}/workItems/search/id | Search for work items and extract IDs only
[**api_v2_projects_id_work_items_search_post**](ProjectsApi.md#api_v2_projects_id_work_items_search_post) | **POST** /api/v2/projects/{id}/workItems/search | Search for work items
[**api_v2_projects_id_work_items_tags_get**](ProjectsApi.md#api_v2_projects_id_work_items_tags_get) | **GET** /api/v2/projects/{id}/workItems/tags | Get WorkItems Tags
[**api_v2_projects_name_name_exists_get**](ProjectsApi.md#api_v2_projects_name_name_exists_get) | **GET** /api/v2/projects/name/{name}/exists | 
[**api_v2_projects_search_post**](ProjectsApi.md#api_v2_projects_search_post) | **POST** /api/v2/projects/search | Search for projects
[**background_import_project**](ProjectsApi.md#background_import_project) | **POST** /api/v2/projects/import/json | Import project from JSON file in background job
[**background_import_to_existing_project**](ProjectsApi.md#background_import_to_existing_project) | **POST** /api/v2/projects/{id}/import/json | Import project from JSON file into existing project in background job
[**background_import_zip_project**](ProjectsApi.md#background_import_zip_project) | **POST** /api/v2/projects/import/zip | Import project from Zip file in background job
[**background_import_zip_to_existing_project**](ProjectsApi.md#background_import_zip_to_existing_project) | **POST** /api/v2/projects/{id}/import/zip | Import project from Zip file into existing project in background job
[**call_import**](ProjectsApi.md#call_import) | **POST** /api/v2/projects/import | Import project from JSON file
[**create_custom_attribute_test_plan_project_relations**](ProjectsApi.md#create_custom_attribute_test_plan_project_relations) | **POST** /api/v2/projects/{id}/testPlans/attributes | Add attributes to project&#39;s test plans
[**create_project**](ProjectsApi.md#create_project) | **POST** /api/v2/projects | Create project
[**create_projects_attribute**](ProjectsApi.md#create_projects_attribute) | **POST** /api/v2/projects/{id}/attributes | Create project attribute
[**delete_custom_attribute_test_plan_project_relations**](ProjectsApi.md#delete_custom_attribute_test_plan_project_relations) | **DELETE** /api/v2/projects/{id}/testPlans/attribute/{attributeId} | Delete attribute from project&#39;s test plans
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /api/v2/projects/{id} | Delete project
[**delete_project_auto_tests**](ProjectsApi.md#delete_project_auto_tests) | **DELETE** /api/v2/projects/{id}/autoTests | Delete project
[**delete_projects_attribute**](ProjectsApi.md#delete_projects_attribute) | **DELETE** /api/v2/projects/{id}/attributes/{attributeId} | Delete project attribute
[**export**](ProjectsApi.md#export) | **POST** /api/v2/projects/{id}/export | Export project as JSON file
[**export_project_json**](ProjectsApi.md#export_project_json) | **POST** /api/v2/projects/{id}/export/json | Export project as JSON file in background job
[**export_project_with_test_plans_json**](ProjectsApi.md#export_project_with_test_plans_json) | **POST** /api/v2/projects/{id}/export/testPlans/json | Export project as JSON file with test plans in background job
[**export_project_with_test_plans_zip**](ProjectsApi.md#export_project_with_test_plans_zip) | **POST** /api/v2/projects/{id}/export/testPlans/zip | Export project as Zip file with test plans in background job
[**export_project_zip**](ProjectsApi.md#export_project_zip) | **POST** /api/v2/projects/{id}/export/zip | Export project as Zip file in background job
[**export_with_test_plans_and_configurations**](ProjectsApi.md#export_with_test_plans_and_configurations) | **POST** /api/v2/projects/{id}/export-by-testPlans | Export project with test plans, test suites and test points as JSON file
[**get_all_projects**](ProjectsApi.md#get_all_projects) | **GET** /api/v2/projects | Get all projects
[**get_attribute_by_project_id**](ProjectsApi.md#get_attribute_by_project_id) | **GET** /api/v2/projects/{id}/attributes/{attributeId} | Get project attribute
[**get_attributes_by_project_id**](ProjectsApi.md#get_attributes_by_project_id) | **GET** /api/v2/projects/{id}/attributes | Get project attributes
[**get_auto_tests_namespaces**](ProjectsApi.md#get_auto_tests_namespaces) | **GET** /api/v2/projects/{id}/autoTestsNamespaces | Get namespaces of autotests in project
[**get_configurations_by_project_id**](ProjectsApi.md#get_configurations_by_project_id) | **GET** /api/v2/projects/{id}/configurations | Get project configurations
[**get_custom_attribute_test_plan_project_relations**](ProjectsApi.md#get_custom_attribute_test_plan_project_relations) | **GET** /api/v2/projects/{id}/testPlans/attributes | Get project&#39;s test plan attributes
[**get_project_by_id**](ProjectsApi.md#get_project_by_id) | **GET** /api/v2/projects/{id} | Get project by ID
[**get_sections_by_project_id**](ProjectsApi.md#get_sections_by_project_id) | **GET** /api/v2/projects/{id}/sections | Get project sections
[**get_test_plans_by_project_id**](ProjectsApi.md#get_test_plans_by_project_id) | **GET** /api/v2/projects/{id}/testPlans | Get project test plans
[**get_test_runs_by_project_id**](ProjectsApi.md#get_test_runs_by_project_id) | **GET** /api/v2/projects/{id}/testRuns | Get project test runs
[**get_work_items_by_project_id**](ProjectsApi.md#get_work_items_by_project_id) | **GET** /api/v2/projects/{id}/workItems | Get project work items
[**import_to_existing_project**](ProjectsApi.md#import_to_existing_project) | **POST** /api/v2/projects/{id}/import | Import project from JSON file into existing project
[**restore_project**](ProjectsApi.md#restore_project) | **POST** /api/v2/projects/{id}/restore | Restore project
[**search_attributes_in_project**](ProjectsApi.md#search_attributes_in_project) | **POST** /api/v2/projects/{id}/attributes/search | Search for attributes used in the project
[**search_test_plan_attributes_in_project**](ProjectsApi.md#search_test_plan_attributes_in_project) | **POST** /api/v2/projects/{id}/testPlans/attributes/search | Search for attributes used in the project test plans
[**update_custom_attribute_test_plan_project_relations**](ProjectsApi.md#update_custom_attribute_test_plan_project_relations) | **PUT** /api/v2/projects/{id}/testPlans/attribute | Update attribute of project&#39;s test plans
[**update_project**](ProjectsApi.md#update_project) | **PUT** /api/v2/projects | Update project
[**update_projects_attribute**](ProjectsApi.md#update_projects_attribute) | **PUT** /api/v2/projects/{id}/attributes | Edit attribute of the project


# **add_globa_attributes_to_project**
> add_globa_attributes_to_project(id)

Add global attributes to project

<br>Use case  <br>User sets project internal or global identifier and attributes identifiers  <br>System search project  <br>System relates global attributes with project  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add global attributes to project
        api_instance.add_globa_attributes_to_project(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->add_globa_attributes_to_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add global attributes to project
        api_instance.add_globa_attributes_to_project(id, request_body=request_body)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->add_globa_attributes_to_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
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
**404** | Project with provided ID was not found |  -  |
**409** | Conflict |  -  |
**422** | Client Error |  -  |
**200** | Success |  -  |
**400** | &lt;br&gt; Attributes must be global  |  -  |
**403** | Project admin permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_attributes_templates_search_post**
> [ProjectCustomAttributeTemplateGetModel] api_v2_projects_id_attributes_templates_search_post(id)

Search for custom attributes templates

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_custom_attributes_templates_filter_model import ProjectCustomAttributesTemplatesFilterModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_custom_attribute_template_get_model import ProjectCustomAttributeTemplateGetModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | 
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    project_custom_attributes_templates_filter_model = ProjectCustomAttributesTemplatesFilterModel(
        name="name_example",
        custom_attribute_types=[
            CustomAttributeTypesEnum("string"),
        ],
    ) # ProjectCustomAttributesTemplatesFilterModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for custom attributes templates
        api_response = api_instance.api_v2_projects_id_attributes_templates_search_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_attributes_templates_search_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for custom attributes templates
        api_response = api_instance.api_v2_projects_id_attributes_templates_search_post(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, project_custom_attributes_templates_filter_model=project_custom_attributes_templates_filter_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_attributes_templates_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **project_custom_attributes_templates_filter_model** | [**ProjectCustomAttributesTemplatesFilterModel**](ProjectCustomAttributesTemplatesFilterModel.md)|  | [optional]

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
**403** | Project admin permission for project settings is required |  -  |
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_attributes_templates_template_id_delete**
> api_v2_projects_id_attributes_templates_template_id_delete(id, template_id)

Delete CustomAttributeTemplate from Project

<br>Use case  <br>User sets project internal or global identifier   <br>User sets attribute template internal identifier   <br>User runs method execution  <br>System delete attribute template from project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    template_id = "templateId_example" # str | CustomAttributeTemplate internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete CustomAttributeTemplate from Project
        api_instance.api_v2_projects_id_attributes_templates_template_id_delete(id, template_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_attributes_templates_template_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
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
**404** | Can&#39;t find a Project with identifier |  -  |
**400** | Bad Request |  -  |
**204** | No Content |  -  |
**403** | Update project settings permission for project required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_attributes_templates_template_id_post**
> api_v2_projects_id_attributes_templates_template_id_post(id, template_id)

Add CustomAttributeTemplate to Project

<br>Use case  <br>User sets project internal or global identifier   <br>User sets attribute template internal identifier   <br>User runs method execution  <br>System add attribute template to project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    template_id = "templateId_example" # str | CustomAttributeTemplate internal (UUID) identifier

    # example passing only required values which don't have defaults set
    try:
        # Add CustomAttributeTemplate to Project
        api_instance.api_v2_projects_id_attributes_templates_template_id_post(id, template_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_attributes_templates_template_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
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
**404** | Can&#39;t find a Project with identifier |  -  |
**400** | Bad Request |  -  |
**200** | Success |  -  |
**403** | Update project settings permission for project required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_failure_classes_get**
> [FailureClassModel] api_v2_projects_id_failure_classes_get(id)

Get Project FailureClasses

<br>Use case  <br>User sets project internal or global identifier   <br>User runs method execution  <br>System returns project failre classes

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.failure_class_model import FailureClassModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    is_deleted = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Project FailureClasses
        api_response = api_instance.api_v2_projects_id_failure_classes_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_failure_classes_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project FailureClasses
        api_response = api_instance.api_v2_projects_id_failure_classes_get(id, is_deleted=is_deleted)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_failure_classes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **is_deleted** | **bool**|  | [optional]

### Return type

[**[FailureClassModel]**](FailureClassModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_favorite_put**
> api_v2_projects_id_favorite_put(id)

Mark Project as favorite

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Mark Project as favorite
        api_instance.api_v2_projects_id_favorite_put(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_favorite_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

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
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**204** | Successful operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_filters_get**
> [FilterModel] api_v2_projects_id_filters_get(id)

Get Project filters

<br>Use case  <br>User sets project internal or global identifier   <br>User runs method execution  <br>System returns project filters

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.filter_model import FilterModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get Project filters
        api_response = api_instance.api_v2_projects_id_filters_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_filters_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**[FilterModel]**](FilterModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_patch**
> api_v2_projects_id_patch(id)

Patch project

See <a href=\"https://www.rfc-editor.org/rfc/rfc6902\" target=\"_blank\">RFC 6902: JavaScript Object Notation (JSON) Patch</a> for details

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global Id of project
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
        # Patch project
        api_instance.api_v2_projects_id_patch(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Patch project
        api_instance.api_v2_projects_id_patch(id, operation=operation)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global Id of project |
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
**403** | Update permission for projects is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_plans_analytics_get**
> [TestPlanWithAnalyticModel] api_v2_projects_id_test_plans_analytics_get(id)

Get TestPlans analytics

<br>Use case  <br>User sets project internal identifier  <br>User sets query params  <br>User runs method execution  <br>System return analytics

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.test_plan_with_analytic_model import TestPlanWithAnalyticModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) identifier
    is_deleted = True # bool |  (optional)
    must_update_cache = False # bool |  (optional) if omitted the server will use the default value of False
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get TestPlans analytics
        api_response = api_instance.api_v2_projects_id_test_plans_analytics_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_analytics_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get TestPlans analytics
        api_response = api_instance.api_v2_projects_id_test_plans_analytics_get(id, is_deleted=is_deleted, must_update_cache=must_update_cache, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_analytics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) identifier |
 **is_deleted** | **bool**|  | [optional]
 **must_update_cache** | **bool**|  | [optional] if omitted the server will use the default value of False
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestPlanWithAnalyticModel]**](TestPlanWithAnalyticModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_plans_delete_bulk_post**
> [str] api_v2_projects_id_test_plans_delete_bulk_post(id)

Delete multiple test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_test_plans_filter_model import ProjectTestPlansFilterModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global ID of the project
    project_test_plans_filter_model = ProjectTestPlansFilterModel(
        name="name_example",
        description="description_example",
        build="build_example",
        product_name="product_name_example",
        status=[
            TestPlanStatusModel("New"),
        ],
        global_ids=[
            1,
        ],
        is_locked=True,
        locked_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        automatic_duration_timer=[
            True,
        ],
        created_by_ids=[
            "created_by_ids_example",
        ],
        created_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        start_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        end_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        tag_names=[
            "tag_names_example",
        ],
        attributes={
            "key": [
                "key_example",
            ],
        },
        is_deleted=True,
    ) # ProjectTestPlansFilterModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete multiple test plans
        api_response = api_instance.api_v2_projects_id_test_plans_delete_bulk_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_delete_bulk_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete multiple test plans
        api_response = api_instance.api_v2_projects_id_test_plans_delete_bulk_post(id, project_test_plans_filter_model=project_test_plans_filter_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_delete_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the project |
 **project_test_plans_filter_model** | [**ProjectTestPlansFilterModel**](ProjectTestPlansFilterModel.md)|  | [optional]

### Return type

**[str]**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | - Read permission for the project is required  - Delete permission for test plans is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_plans_name_exists_get**
> bool api_v2_projects_id_test_plans_name_exists_get(id, name)

Checks if TestPlan exists with the specified name exists for the project

<br>Use case  <br>User sets project internal or global identifier   <br>User runs method execution  <br>System purge delete project workitems

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    name = "name_example" # str | TestPlan name to check

    # example passing only required values which don't have defaults set
    try:
        # Checks if TestPlan exists with the specified name exists for the project
        api_response = api_instance.api_v2_projects_id_test_plans_name_exists_get(id, name)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_name_exists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **name** | **str**| TestPlan name to check |

### Return type

**bool**

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

# **api_v2_projects_id_test_plans_restore_bulk_post**
> api_v2_projects_id_test_plans_restore_bulk_post(id)

Restore multiple test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_test_plans_filter_model import ProjectTestPlansFilterModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global ID of the project
    project_test_plans_filter_model = ProjectTestPlansFilterModel(
        name="name_example",
        description="description_example",
        build="build_example",
        product_name="product_name_example",
        status=[
            TestPlanStatusModel("New"),
        ],
        global_ids=[
            1,
        ],
        is_locked=True,
        locked_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        automatic_duration_timer=[
            True,
        ],
        created_by_ids=[
            "created_by_ids_example",
        ],
        created_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        start_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        end_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        tag_names=[
            "tag_names_example",
        ],
        attributes={
            "key": [
                "key_example",
            ],
        },
        is_deleted=True,
    ) # ProjectTestPlansFilterModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Restore multiple test plans
        api_instance.api_v2_projects_id_test_plans_restore_bulk_post(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_restore_bulk_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restore multiple test plans
        api_instance.api_v2_projects_id_test_plans_restore_bulk_post(id, project_test_plans_filter_model=project_test_plans_filter_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_restore_bulk_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the project |
 **project_test_plans_filter_model** | [**ProjectTestPlansFilterModel**](ProjectTestPlansFilterModel.md)|  | [optional]

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
**403** | - Read permission for the project is required  - Edit permission for test plans is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_plans_search_post**
> [TestPlanWithAnalyticModel] api_v2_projects_id_test_plans_search_post(id)

Get Project TestPlans with analytics

<br>Use case  <br>User sets project internal or global identifier   <br>User sets request body   <br>User runs method execution  <br>System returns project testplans with analytics

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.test_plan_with_analytic_model import TestPlanWithAnalyticModel
from testit_api_client.model.project_test_plans_filter_model import ProjectTestPlansFilterModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    must_update_cache = False # bool |  (optional) if omitted the server will use the default value of False
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    project_test_plans_filter_model = ProjectTestPlansFilterModel(
        name="name_example",
        description="description_example",
        build="build_example",
        product_name="product_name_example",
        status=[
            TestPlanStatusModel("New"),
        ],
        global_ids=[
            1,
        ],
        is_locked=True,
        locked_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        automatic_duration_timer=[
            True,
        ],
        created_by_ids=[
            "created_by_ids_example",
        ],
        created_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        start_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        end_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        tag_names=[
            "tag_names_example",
        ],
        attributes={
            "key": [
                "key_example",
            ],
        },
        is_deleted=True,
    ) # ProjectTestPlansFilterModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Project TestPlans with analytics
        api_response = api_instance.api_v2_projects_id_test_plans_search_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_search_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project TestPlans with analytics
        api_response = api_instance.api_v2_projects_id_test_plans_search_post(id, must_update_cache=must_update_cache, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, project_test_plans_filter_model=project_test_plans_filter_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_plans_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **must_update_cache** | **bool**|  | [optional] if omitted the server will use the default value of False
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **project_test_plans_filter_model** | [**ProjectTestPlansFilterModel**](ProjectTestPlansFilterModel.md)|  | [optional]

### Return type

[**[TestPlanWithAnalyticModel]**](TestPlanWithAnalyticModel.md)

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

# **api_v2_projects_id_test_runs_active_get**
> [PublicTestRunModel] api_v2_projects_id_test_runs_active_get(id)

Get active Project TestRuns

<br>Use case  <br>User sets project internal or global identifier   <br>User runs method execution  <br>System returns active testruns

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.public_test_run_model import PublicTestRunModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get active Project TestRuns
        api_response = api_instance.api_v2_projects_id_test_runs_active_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_runs_active_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**[PublicTestRunModel]**](PublicTestRunModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_test_runs_full_get**
> [TestRunModel] api_v2_projects_id_test_runs_full_get(id)

Get Project TestRuns full models

<br>Use case  <br>User sets project internal or global identifier   <br>User sets query params   <br>User runs method execution  <br>System returns project test runs full models

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.test_run_model import TestRunModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    include_test_results = False # bool |  (optional) if omitted the server will use the default value of False
    must_aggregate_test_results = True # bool |  (optional) if omitted the server will use the default value of True
    not_started = True # bool |  (optional)
    in_progress = True # bool |  (optional)
    stopped = True # bool |  (optional)
    completed = True # bool |  (optional)
    created_date_from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    created_date_to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    test_plan_id = "testPlanId_example" # str |  (optional)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Project TestRuns full models
        api_response = api_instance.api_v2_projects_id_test_runs_full_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_runs_full_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Project TestRuns full models
        api_response = api_instance.api_v2_projects_id_test_runs_full_get(id, include_test_results=include_test_results, must_aggregate_test_results=must_aggregate_test_results, not_started=not_started, in_progress=in_progress, stopped=stopped, completed=completed, created_date_from=created_date_from, created_date_to=created_date_to, test_plan_id=test_plan_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_test_runs_full_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **include_test_results** | **bool**|  | [optional] if omitted the server will use the default value of False
 **must_aggregate_test_results** | **bool**|  | [optional] if omitted the server will use the default value of True
 **not_started** | **bool**|  | [optional]
 **in_progress** | **bool**|  | [optional]
 **stopped** | **bool**|  | [optional]
 **completed** | **bool**|  | [optional]
 **created_date_from** | **datetime**|  | [optional]
 **created_date_to** | **datetime**|  | [optional]
 **test_plan_id** | **str**|  | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestRunModel]**](TestRunModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_work_items_search_id_post**
> [str] api_v2_projects_id_work_items_search_id_post(id)

Search for work items and extract IDs only

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.work_item_select_model import WorkItemSelectModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global ID of the project
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    work_item_select_model = WorkItemSelectModel(
        filter=WorkItemFilterModel(
            name_or_id="name_or_id_example",
            include_ids=[
                "include_ids_example",
            ],
            exclude_ids=[
                "exclude_ids_example",
            ],
            name="name_example",
            ids=[
                "ids_example",
            ],
            global_ids=[
                1,
            ],
            attributes={
                "key": [
                    "key_example",
                ],
            },
            is_deleted=True,
            project_ids=[
                "project_ids_example",
            ],
            section_ids=[
                "section_ids_example",
            ],
            created_by_ids=[
                "created_by_ids_example",
            ],
            modified_by_ids=[
                "modified_by_ids_example",
            ],
            states=[
                WorkItemStates("NeedsWork"),
            ],
            priorities=[
                WorkItemPriorityModel("Lowest"),
            ],
            types=[
                WorkItemEntityTypes("TestCases"),
            ],
            created_date=DateTimeRangeSelectorModel(
                _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            modified_date=DateTimeRangeSelectorModel(
                _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            duration=Int32RangeSelectorModel(
                _from=1,
                to=1,
            ),
            is_automated=True,
            tags=[
                "tags_example",
            ],
            auto_test_ids=[
                "auto_test_ids_example",
            ],
        ),
        extraction_model=WorkItemsExtractionModel(
            ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
            section_ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
            project_ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
        ),
    ) # WorkItemSelectModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for work items and extract IDs only
        api_response = api_instance.api_v2_projects_id_work_items_search_id_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_work_items_search_id_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for work items and extract IDs only
        api_response = api_instance.api_v2_projects_id_work_items_search_id_post(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_select_model=work_item_select_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_work_items_search_id_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the project |
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **work_item_select_model** | [**WorkItemSelectModel**](WorkItemSelectModel.md)|  | [optional]

### Return type

**[str]**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Read permission for test library is required |  -  |
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_work_items_search_post**
> [WorkItemShortModel] api_v2_projects_id_work_items_search_post(id)

Search for work items

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.work_item_select_model import WorkItemSelectModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.work_item_short_model import WorkItemShortModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global ID of the project
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    work_item_select_model = WorkItemSelectModel(
        filter=WorkItemFilterModel(
            name_or_id="name_or_id_example",
            include_ids=[
                "include_ids_example",
            ],
            exclude_ids=[
                "exclude_ids_example",
            ],
            name="name_example",
            ids=[
                "ids_example",
            ],
            global_ids=[
                1,
            ],
            attributes={
                "key": [
                    "key_example",
                ],
            },
            is_deleted=True,
            project_ids=[
                "project_ids_example",
            ],
            section_ids=[
                "section_ids_example",
            ],
            created_by_ids=[
                "created_by_ids_example",
            ],
            modified_by_ids=[
                "modified_by_ids_example",
            ],
            states=[
                WorkItemStates("NeedsWork"),
            ],
            priorities=[
                WorkItemPriorityModel("Lowest"),
            ],
            types=[
                WorkItemEntityTypes("TestCases"),
            ],
            created_date=DateTimeRangeSelectorModel(
                _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            modified_date=DateTimeRangeSelectorModel(
                _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
                to=dateutil_parser('1970-01-01T00:00:00.00Z'),
            ),
            duration=Int32RangeSelectorModel(
                _from=1,
                to=1,
            ),
            is_automated=True,
            tags=[
                "tags_example",
            ],
            auto_test_ids=[
                "auto_test_ids_example",
            ],
        ),
        extraction_model=WorkItemsExtractionModel(
            ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
            section_ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
            project_ids=GuidExtractionModel(
                include=[
                    "include_example",
                ],
                exclude=[
                    "exclude_example",
                ],
            ),
        ),
    ) # WorkItemSelectModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for work items
        api_response = api_instance.api_v2_projects_id_work_items_search_post(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_work_items_search_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for work items
        api_response = api_instance.api_v2_projects_id_work_items_search_post(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, work_item_select_model=work_item_select_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_work_items_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global ID of the project |
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **work_item_select_model** | [**WorkItemSelectModel**](WorkItemSelectModel.md)|  | [optional]

### Return type

[**[WorkItemShortModel]**](WorkItemShortModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Read permission for test library is required |  -  |
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_id_work_items_tags_get**
> [TagShortModel] api_v2_projects_id_work_items_tags_get(id)

Get WorkItems Tags

<br>Use case  <br>User sets project internal identifier   <br>User runs method execution  <br>System returns work items tags

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.tag_short_model import TagShortModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) identifier
    is_deleted = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get WorkItems Tags
        api_response = api_instance.api_v2_projects_id_work_items_tags_get(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_work_items_tags_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get WorkItems Tags
        api_response = api_instance.api_v2_projects_id_work_items_tags_get(id, is_deleted=is_deleted)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_id_work_items_tags_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) identifier |
 **is_deleted** | **bool**|  | [optional]

### Return type

[**[TagShortModel]**](TagShortModel.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v2_projects_name_name_exists_get**
> bool api_v2_projects_name_name_exists_get(name)



### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_v2_projects_name_name_exists_get(name)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_name_name_exists_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

**bool**

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

# **api_v2_projects_search_post**
> [ProjectModel] api_v2_projects_search_post()

Search for projects

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_model import ProjectModel
from testit_api_client.model.projects_filter_model import ProjectsFilterModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    projects_filter_model = ProjectsFilterModel(
        name="name_example",
        is_favorite=True,
        is_deleted=True,
        test_cases_count=Int32RangeSelectorModel(
            _from=1,
            to=1,
        ),
        checklists_count=Int32RangeSelectorModel(
            _from=1,
            to=1,
        ),
        shared_steps_count=Int32RangeSelectorModel(
            _from=1,
            to=1,
        ),
        autotests_count=Int32RangeSelectorModel(
            _from=1,
            to=1,
        ),
        global_ids=[
            1,
        ],
        created_date=DateTimeRangeSelectorModel(
            _from=dateutil_parser('1970-01-01T00:00:00.00Z'),
            to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        ),
        created_by_ids=[
            "created_by_ids_example",
        ],
    ) # ProjectsFilterModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for projects
        api_response = api_instance.api_v2_projects_search_post(skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, projects_filter_model=projects_filter_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->api_v2_projects_search_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **projects_filter_model** | [**ProjectsFilterModel**](ProjectsFilterModel.md)|  | [optional]

### Return type

[**[ProjectModel]**](ProjectModel.md)

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

# **background_import_project**
> str background_import_project()

Import project from JSON file in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from JSON file in background job
        api_response = api_instance.background_import_project(file=file)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->background_import_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **background_import_to_existing_project**
> str background_import_to_existing_project(id)

Import project from JSON file into existing project in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    file = open('/path/to/file', 'rb') # file_type | Select file (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import project from JSON file into existing project in background job
        api_response = api_instance.background_import_to_existing_project(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->background_import_to_existing_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from JSON file into existing project in background job
        api_response = api_instance.background_import_to_existing_project(id, file=file)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->background_import_to_existing_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **file** | **file_type**| Select file | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **background_import_zip_project**
> str background_import_zip_project()

Import project from Zip file in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    file = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from Zip file in background job
        api_response = api_instance.background_import_zip_project(file=file)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->background_import_zip_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file_type**|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **background_import_zip_to_existing_project**
> str background_import_zip_to_existing_project(id)

Import project from Zip file into existing project in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    file = open('/path/to/file', 'rb') # file_type | Select file (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import project from Zip file into existing project in background job
        api_response = api_instance.background_import_zip_to_existing_project(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->background_import_zip_to_existing_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from Zip file into existing project in background job
        api_response = api_instance.background_import_zip_to_existing_project(id, file=file)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->background_import_zip_to_existing_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **file** | **file_type**| Select file | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **call_import**
> call_import()

Import project from JSON file

<br>    <b>A project can only be exported to another TMS instance, different from the one it was imported from.</b>    <br>This method imports a `.json` file with a project to the test management system.  <br>In the body of the request, send the `.json` file received by the `POST /api/v2/projects/export` method:  <br>    ```              curl -X POST \"http://{domain.com}/api/v2/projects/import\" \\              -H \"accept: /\" -H \"Authorization: PrivateToken {token}\" -H \"Content-Type: multipart/form-data\" \\              -F \"file=@import.txt;type=text/plain\"              ```    <br>              In the second instance, a project with the name of the imported one is created.              User attributes and the test library (along with content and structure) are imported.                <br>Test plan execution history from the first instance of TMS cannot be transferred.

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    include_attachments = False # bool | Enables attachment import. (optional) if omitted the server will use the default value of False
    file = open('/path/to/file', 'rb') # file_type | Select file (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from JSON file
        api_instance.call_import(include_attachments=include_attachments, file=file)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->call_import: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_attachments** | **bool**| Enables attachment import. | [optional] if omitted the server will use the default value of False
 **file** | **file_type**| Select file | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**403** | Project creator or admin system role is required |  -  |
**413** | Multipart body length limit exceeded |  -  |
**400** | Bad Request |  -  |
**409** | Entity with the same ID was already imported in other project |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_attribute_test_plan_project_relations**
> create_custom_attribute_test_plan_project_relations(id)

Add attributes to project's test plans

<br>Use case  <br>User sets project internal or global identifier and attributes identifiers  <br>User runs method execution  <br>System updates project and add attributes to project for test plans  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    request_body = [
        "request_body_example",
    ] # [str] |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add attributes to project's test plans
        api_instance.create_custom_attribute_test_plan_project_relations(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->create_custom_attribute_test_plan_project_relations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add attributes to project's test plans
        api_instance.create_custom_attribute_test_plan_project_relations(id, request_body=request_body)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->create_custom_attribute_test_plan_project_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
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
**403** | Update permission for project settings is required |  -  |
**204** | No Content |  -  |
**400** | &lt;br&gt; Attributes must be global  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> ProjectModel create_project()

Create project

<br>Use case  <br>User sets project parameters (listed in request example) and runs method execution  <br>System creates project  <br>System returns project model (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_model import ProjectModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_post_model import ProjectPostModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_post_model = ProjectPostModel(
        description="description_example",
        name="name_example",
        is_favorite=True,
    ) # ProjectPostModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create project
        api_response = api_instance.create_project(project_post_model=project_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_post_model** | [**ProjectPostModel**](ProjectPostModel.md)|  | [optional]

### Return type

[**ProjectModel**](ProjectModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Project creator or admin system role is required |  -  |
**201** | Created |  -  |
**400** | Bad Request |  -  |
**409** | Project with the same name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_projects_attribute**
> CustomAttributeModel create_projects_attribute(id)

Create project attribute

<br>Use case  <br>User sets attribute parameters (listed in request example) and runs method execution  <br>System search project  <br>System creates attribute and relates it to the project  <br>System returns project attribute properties (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_model import CustomAttributeModel
from testit_api_client.model.custom_attribute_post_model import CustomAttributePostModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    custom_attribute_post_model = CustomAttributePostModel(
        options=[
            CustomAttributeOptionPostModel(
                value="value_example",
                is_default=True,
            ),
        ],
        type=CustomAttributeTypesEnum("string"),
        name="name_example",
        is_enabled=True,
        is_required=True,
        is_global=True,
    ) # CustomAttributePostModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create project attribute
        api_response = api_instance.create_projects_attribute(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->create_projects_attribute: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create project attribute
        api_response = api_instance.create_projects_attribute(id, custom_attribute_post_model=custom_attribute_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->create_projects_attribute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
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
**422** | Cannot add new attribute from template which is in use |  -  |
**403** | Update permission for project settings is required |  -  |
**404** | Project with provided ID was not found |  -  |
**400** | &lt;br&gt;- Attribute is &#x60;null&#x60;  &lt;br&gt;- Priority is invalid  &lt;br&gt;- Attribute with &#x60;Options&#x60; type must have an options  &lt;br&gt;- ID is not &#x60;null&#x60;  &lt;br&gt;- Option ID is not &#x60;null&#x60; |  -  |
**409** | &lt;br&gt;&#x60;CustomAttribute.Name&#x60; or &#x60;CustomAttribute.Id&#x60; are not unique in attributes schemes  &lt;br&gt;&#x60;CustomAttributeOptionModel.Id&#x60; or &#x60;CustomAttributeOptionModel.Value&#x60; are not unique in &#x60;attributesScheme.Options&#x60; |  -  |
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_attribute_test_plan_project_relations**
> delete_custom_attribute_test_plan_project_relations(id, attribute_id)

Delete attribute from project's test plans

<br>Use case  <br>User sets project internal or global identifier and attribute identifier  <br>User runs method execution  <br>System updates project and delete attribute from project for test plans  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    attribute_id = "attributeId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete attribute from project's test plans
        api_instance.delete_custom_attribute_test_plan_project_relations(id, attribute_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->delete_custom_attribute_test_plan_project_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **attribute_id** | **str**|  |

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
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(id)

Delete project

<br>Use case:  <br>1. User sets project internal or global identifier and runs method execution  <br>2. System searches and moves requested project to archive  <br>3. System responds with no content (204) result

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete project
        api_instance.delete_project(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

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
**404** | Project with provided ID does not exists |  -  |
**204** | No Content |  -  |
**403** | Delete permission for projects is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_auto_tests**
> delete_project_auto_tests(id)

Delete project

<br>Use case  <br>User sets project internal or global identifier   <br>User runs method execution  <br>System delete all autotests from project  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete project
        api_instance.delete_project_auto_tests(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->delete_project_auto_tests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

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
**403** | Delete permission for AutoTest required |  -  |
**404** | Can&#39;t find a Project with identifier |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_projects_attribute**
> delete_projects_attribute(id, attribute_id)

Delete project attribute

<br>Use case  <br>User sets project identifier and runs method execution  <br>User sets attribute identifier  <br>User runs method execution  <br>System search project  <br>System search and delete attribute  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    attribute_id = "attributeId_example" # str | Project attribute internal (UUID)

    # example passing only required values which don't have defaults set
    try:
        # Delete project attribute
        api_instance.delete_projects_attribute(id, attribute_id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->delete_projects_attribute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **attribute_id** | **str**| Project attribute internal (UUID) |

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
**204** | Successful operation |  -  |
**404** | Project with provided ID was not found |  -  |
**400** | &lt;br&gt;- Project ID is invalid  &lt;br&gt;- Project attribute ID is invalid  &lt;br&gt;- Attribute is empty |  -  |
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export**
> file_type export(id)

Export project as JSON file

<br>This method exports the selected project or its part (sections, work items) to a `.json` file.  <br>In the request body, you can specify sections and test cases to be exported.  <br>Example of a request to export two sections and two test cases:  <br>    ```              curl -X POST \"http://{domain}.com/api/v2/projects/27a32ce6-d972-4ef8-bef5-51be4bf9e468/export\" \\              -H \"accept: application/json\" -H \"Authorization: PrivateToken {token}\" -H \"Content-Type: application/json-patch+json\" \\              -d \"{\\\"sectionIds\\\":[\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"9fa85f64-5717-4562-b3fc-2c963f66a000\\\"],\\\"workItemIds\\\":[\\\"3fa85f64-5717-4562-b3fc-2c963f66afa6\\\",\\\"90085f64-5717-4562-b3fc-2c963f66a000\\\"]}\"              ```    <br>In the response, you get:  <br>              - A `.zip` file with attachments and a.json file if you enable attachments export.<br />              - A `.json` file with the project if you do not enable attachments export.              

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_export_query_model import ProjectExportQueryModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Specifies the ID of the project you want to export.
    include_attachments = False # bool | Enables attachment export. (optional) if omitted the server will use the default value of False
    project_export_query_model = ProjectExportQueryModel(
        section_ids=[
            "section_ids_example",
        ],
        work_item_ids=[
            "work_item_ids_example",
        ],
    ) # ProjectExportQueryModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project as JSON file
        api_response = api_instance.export(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project as JSON file
        api_response = api_instance.export(id, include_attachments=include_attachments, project_export_query_model=project_export_query_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the ID of the project you want to export. |
 **include_attachments** | **bool**| Enables attachment export. | [optional] if omitted the server will use the default value of False
 **project_export_query_model** | [**ProjectExportQueryModel**](ProjectExportQueryModel.md)|  | [optional]

### Return type

**file_type**

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
**403** | Update permission for project settings is required |  -  |
**400** | Root section was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_json**
> str export_project_json(id)

Export project as JSON file in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_export_query_model import ProjectExportQueryModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    time_zone_offset_in_minutes = 1 # int |  (optional)
    project_export_query_model = ProjectExportQueryModel(
        section_ids=[
            "section_ids_example",
        ],
        work_item_ids=[
            "work_item_ids_example",
        ],
    ) # ProjectExportQueryModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project as JSON file in background job
        api_response = api_instance.export_project_json(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_project_json: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project as JSON file in background job
        api_response = api_instance.export_project_json(id, time_zone_offset_in_minutes=time_zone_offset_in_minutes, project_export_query_model=project_export_query_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_project_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **time_zone_offset_in_minutes** | **int**|  | [optional]
 **project_export_query_model** | [**ProjectExportQueryModel**](ProjectExportQueryModel.md)|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Update permission for project settings is required |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_with_test_plans_json**
> str export_project_with_test_plans_json(id)

Export project as JSON file with test plans in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_export_with_test_plans_post_model import ProjectExportWithTestPlansPostModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    time_zone_offset_in_minutes = 1 # int |  (optional)
    project_export_with_test_plans_post_model = ProjectExportWithTestPlansPostModel(
        test_plans_ids=[
            "test_plans_ids_example",
        ],
    ) # ProjectExportWithTestPlansPostModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project as JSON file with test plans in background job
        api_response = api_instance.export_project_with_test_plans_json(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_project_with_test_plans_json: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project as JSON file with test plans in background job
        api_response = api_instance.export_project_with_test_plans_json(id, time_zone_offset_in_minutes=time_zone_offset_in_minutes, project_export_with_test_plans_post_model=project_export_with_test_plans_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_project_with_test_plans_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **time_zone_offset_in_minutes** | **int**|  | [optional]
 **project_export_with_test_plans_post_model** | [**ProjectExportWithTestPlansPostModel**](ProjectExportWithTestPlansPostModel.md)|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_with_test_plans_zip**
> str export_project_with_test_plans_zip(id)

Export project as Zip file with test plans in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_export_with_test_plans_post_model import ProjectExportWithTestPlansPostModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    time_zone_offset_in_minutes = 1 # int |  (optional)
    project_export_with_test_plans_post_model = ProjectExportWithTestPlansPostModel(
        test_plans_ids=[
            "test_plans_ids_example",
        ],
    ) # ProjectExportWithTestPlansPostModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project as Zip file with test plans in background job
        api_response = api_instance.export_project_with_test_plans_zip(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_project_with_test_plans_zip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project as Zip file with test plans in background job
        api_response = api_instance.export_project_with_test_plans_zip(id, time_zone_offset_in_minutes=time_zone_offset_in_minutes, project_export_with_test_plans_post_model=project_export_with_test_plans_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_project_with_test_plans_zip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **time_zone_offset_in_minutes** | **int**|  | [optional]
 **project_export_with_test_plans_post_model** | [**ProjectExportWithTestPlansPostModel**](ProjectExportWithTestPlansPostModel.md)|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Update permission for project settings is required |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project_zip**
> str export_project_zip(id)

Export project as Zip file in background job

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_export_query_model import ProjectExportQueryModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    time_zone_offset_in_minutes = 1 # int |  (optional)
    project_export_query_model = ProjectExportQueryModel(
        section_ids=[
            "section_ids_example",
        ],
        work_item_ids=[
            "work_item_ids_example",
        ],
    ) # ProjectExportQueryModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project as Zip file in background job
        api_response = api_instance.export_project_zip(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_project_zip: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project as Zip file in background job
        api_response = api_instance.export_project_zip(id, time_zone_offset_in_minutes=time_zone_offset_in_minutes, project_export_query_model=project_export_query_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_project_zip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **time_zone_offset_in_minutes** | **int**|  | [optional]
 **project_export_query_model** | [**ProjectExportQueryModel**](ProjectExportQueryModel.md)|  | [optional]

### Return type

**str**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Update permission for project settings is required |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_with_test_plans_and_configurations**
> file_type export_with_test_plans_and_configurations(id)

Export project with test plans, test suites and test points as JSON file

<br>    <b>You cannot export test cases execution history.</b>    <br>This method exports the project with the test library and specified test plans to another TMS instance.  <br>              After sending a correct request, the project is exported to a `.json` file.              If you enable attachment export, the `.json` file and the attachments are placed in a `.zip` file.              You can import such a project by using the `POST /api/v2/projects/import` method.              

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_export_with_test_plans_post_model import ProjectExportWithTestPlansPostModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Specifies the ID of the project you want to export.
    include_attachments = False # bool | Enables attachment export. (optional) if omitted the server will use the default value of False
    project_export_with_test_plans_post_model = ProjectExportWithTestPlansPostModel(
        test_plans_ids=[
            "test_plans_ids_example",
        ],
    ) # ProjectExportWithTestPlansPostModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export project with test plans, test suites and test points as JSON file
        api_response = api_instance.export_with_test_plans_and_configurations(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_with_test_plans_and_configurations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export project with test plans, test suites and test points as JSON file
        api_response = api_instance.export_with_test_plans_and_configurations(id, include_attachments=include_attachments, project_export_with_test_plans_post_model=project_export_with_test_plans_post_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->export_with_test_plans_and_configurations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Specifies the ID of the project you want to export. |
 **include_attachments** | **bool**| Enables attachment export. | [optional] if omitted the server will use the default value of False
 **project_export_with_test_plans_post_model** | [**ProjectExportWithTestPlansPostModel**](ProjectExportWithTestPlansPostModel.md)|  | [optional]

### Return type

**file_type**

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Project with provided ID was not found |  -  |
**400** | Root section was not found |  -  |
**403** | Update permission for project settings is required |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_projects**
> [ProjectModel] get_all_projects()

Get all projects

<br>Use case  <br>[Optional] User sets isDeleted field value  <br>[Optional] If User sets isDeleted field value as true, System search all deleted projects  <br>[Optional] If User sets isDeleted field value as false, System search all projects which are not deleted  <br>If User did not set isDeleted field value, System search all projects  <br>System returns array of all found projects(listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_model import ProjectModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    is_deleted = True # bool | If result must consist of only actual/deleted parameters (optional)
    project_name = "projectName_example" # str |  (optional)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all projects
        api_response = api_instance.get_all_projects(is_deleted=is_deleted, project_name=project_name, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_all_projects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_deleted** | **bool**| If result must consist of only actual/deleted parameters | [optional]
 **project_name** | **str**|  | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[ProjectModel]**](ProjectModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**403** | Invalid user permissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_by_project_id**
> CustomAttributeModel get_attribute_by_project_id(id, attribute_id)

Get project attribute

<br>Use case  <br>User sets project internal or global identifier  <br>User sets project attribute identifier  <br>User runs method execution  <br>System search project  <br>System search project attribute   <br>System returns project attribute (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_model import CustomAttributeModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    attribute_id = "attributeId_example" # str | Project attribute internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get project attribute
        api_response = api_instance.get_attribute_by_project_id(id, attribute_id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_attribute_by_project_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **attribute_id** | **str**| Project attribute internal (UUID) or global (integer) identifier |

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
**404** | &lt;br&gt;- Project with provided ID was not found  &lt;br&gt;- Project attribute with provided ID was not found |  -  |
**403** | Read permission for test library is required |  -  |
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attributes_by_project_id**
> [CustomAttributeModel] get_attributes_by_project_id(id)

Get project attributes

<br>Use case  <br>User sets project internal or global identifier  <br>[Optional] User sets isDeleted field value  <br>User runs method execution  <br>System search project  <br>[Optional] If User sets isDeleted field value as true, System search all deleted attributes related to project  <br>[Optional] If User sets isDeleted field value as false, System search all attributes related to project which are not deleted  <br>[Optional] If User did not set isDeleted field value, System search all attributes related to project  <br>System returns array of found attributes (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_model import CustomAttributeModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    is_deleted = DeletionState("Any") # DeletionState |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get project attributes
        api_response = api_instance.get_attributes_by_project_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_attributes_by_project_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get project attributes
        api_response = api_instance.get_attributes_by_project_id(id, is_deleted=is_deleted)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_attributes_by_project_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **is_deleted** | **DeletionState**|  | [optional]

### Return type

[**[CustomAttributeModel]**](CustomAttributeModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Read permission for test library is required |  -  |
**404** | Project with provided ID was not found |  -  |
**400** | Bad Request |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_tests_namespaces**
> [AutoTestNamespaceModel] get_auto_tests_namespaces(id)

Get namespaces of autotests in project

<br>Use case  <br>User sets project internal or global identifier and runs method execution  <br>System search project  <br>System search all autotest related to the project  <br>System returns array of autotest with namespaces and classnames (listed in response)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.auto_test_namespace_model import AutoTestNamespaceModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get namespaces of autotests in project
        api_response = api_instance.get_auto_tests_namespaces(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_auto_tests_namespaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**[AutoTestNamespaceModel]**](AutoTestNamespaceModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Project with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configurations_by_project_id**
> [ConfigurationModel] get_configurations_by_project_id(id)

Get project configurations

<br>Use case  <br>User sets project internal or global identifier  <br>User runs method execution  <br>System search project  <br>System search all configurations related to project  <br>System returns array of found configurations (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.configuration_model import ConfigurationModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get project configurations
        api_response = api_instance.get_configurations_by_project_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_configurations_by_project_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**[ConfigurationModel]**](ConfigurationModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Project with provided ID was not found |  -  |
**400** | Bad Request |  -  |
**403** | Read permission for configurations required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_attribute_test_plan_project_relations**
> [CustomAttributeModel] get_custom_attribute_test_plan_project_relations(id)

Get project's test plan attributes

<br>Use case  <br>User runs method execution  <br>System returns project for test plans attributes by project identifier

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get project's test plan attributes
        api_response = api_instance.get_custom_attribute_test_plan_project_relations(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_custom_attribute_test_plan_project_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**[CustomAttributeModel]**](CustomAttributeModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Read permission for project settings is required |  -  |
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_id**
> ProjectModel get_project_by_id(id)

Get project by ID

<br>Use case  <br>User sets project internal or global identifier and runs method execution  <br>System search project  <br>System returns project (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_model import ProjectModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Get project by ID
        api_response = api_instance.get_project_by_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_project_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

### Return type

[**ProjectModel**](ProjectModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Read permission for projects is required |  -  |
**404** | Project with provided ID was not found |  -  |
**200** | Success |  -  |
**400** | ID is invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sections_by_project_id**
> [SectionModel] get_sections_by_project_id(id)

Get project sections

<br>Use case  <br>User sets project internal or global identifier and runs method execution  <br>System search project  <br>System search all sections related to the project  <br>System returns array of sections (listed in response)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.section_model import SectionModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get project sections
        api_response = api_instance.get_sections_by_project_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_sections_by_project_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get project sections
        api_response = api_instance.get_sections_by_project_id(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_sections_by_project_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[SectionModel]**](SectionModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**400** | Bad Request |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Project with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_plans_by_project_id**
> [TestPlanModel] get_test_plans_by_project_id(id)

Get project test plans

<br>Use case  <br>User sets project internal or global identifier  <br>[Optional] User sets isDeleted field value  <br>User runs method execution  <br>System search project  <br>[Optional] If User sets isDeleted field value as true, System search all deleted test plans related to project  <br>[Optional] If User sets isDeleted field value as false, System search all test plans related to project which are not deleted  <br>[Optional] If User did not set isDeleted field value, System search all v related to project  <br>System returns array of found test plans (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.test_plan_model import TestPlanModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    is_deleted = True # bool | If result must consist of only actual/archived test plans (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get project test plans
        api_response = api_instance.get_test_plans_by_project_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_test_plans_by_project_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get project test plans
        api_response = api_instance.get_test_plans_by_project_id(id, is_deleted=is_deleted)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_test_plans_by_project_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **is_deleted** | **bool**| If result must consist of only actual/archived test plans | [optional]

### Return type

[**[TestPlanModel]**](TestPlanModel.md)

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
**404** | Project with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_test_runs_by_project_id**
> [TestRunV2GetModel] get_test_runs_by_project_id(id)

Get project test runs

<br>Use case  <br>User sets project internal or global identifier  <br>User runs method execution  <br>System search project  <br>System search all test runs related to project  <br>System returns array of found test runs (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.test_run_v2_get_model import TestRunV2GetModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    not_started = True # bool |  (optional)
    in_progress = True # bool |  (optional)
    stopped = True # bool |  (optional)
    completed = True # bool |  (optional)
    created_date_from = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    created_date_to = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime |  (optional)
    test_plan_id = "testPlanId_example" # str |  (optional)
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get project test runs
        api_response = api_instance.get_test_runs_by_project_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_test_runs_by_project_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get project test runs
        api_response = api_instance.get_test_runs_by_project_id(id, not_started=not_started, in_progress=in_progress, stopped=stopped, completed=completed, created_date_from=created_date_from, created_date_to=created_date_to, test_plan_id=test_plan_id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_test_runs_by_project_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **not_started** | **bool**|  | [optional]
 **in_progress** | **bool**|  | [optional]
 **stopped** | **bool**|  | [optional]
 **completed** | **bool**|  | [optional]
 **created_date_from** | **datetime**|  | [optional]
 **created_date_to** | **datetime**|  | [optional]
 **test_plan_id** | **str**|  | [optional]
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]

### Return type

[**[TestRunV2GetModel]**](TestRunV2GetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**404** | Project with provided ID was not found |  -  |
**403** | Read permission for test result is required |  -  |
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_items_by_project_id**
> [WorkItemShortModel] get_work_items_by_project_id(id)

Get project work items

<br>Use case  <br>User sets project internal or global identifier  <br>[Optional] User sets isDeleted field value  <br>User runs method execution  <br>System search project  <br>[Optional] If User sets isDeleted field value as true, System search all deleted workitems related to project  <br>[Optional] If User sets isDeleted field value as false, System search all workitems related to project which are not deleted  <br>If User did not set isDeleted field value, System search all  workitems related to project  <br>System returns array of found workitems (listed in response model)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    is_deleted = False # bool | If result must consist of only actual/deleted work items (optional) if omitted the server will use the default value of False
    tag_names = [
        "tagNames_example",
    ] # [str] | List of tags to filter by (optional)
    include_iterations = True # bool |  (optional) if omitted the server will use the default value of True
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get project work items
        api_response = api_instance.get_work_items_by_project_id(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_work_items_by_project_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get project work items
        api_response = api_instance.get_work_items_by_project_id(id, is_deleted=is_deleted, tag_names=tag_names, include_iterations=include_iterations, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->get_work_items_by_project_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **is_deleted** | **bool**| If result must consist of only actual/deleted work items | [optional] if omitted the server will use the default value of False
 **tag_names** | **[str]**| List of tags to filter by | [optional]
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
**400** | &lt;br&gt;- &#x60;orderBy&#x60; statement must have one &#x60;.&#x60; and no &#x60;,&#x60; characters  &lt;br&gt;- &#x60;orderBy&#x60; statement has invalid length  &lt;br&gt;- &#x60;orderBy&#x60; statement must have UUID as attribute key  &lt;br&gt;- Search field was not found |  -  |
**403** | Read permission for test library is required |  -  |
**404** | Project with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_to_existing_project**
> import_to_existing_project(id)

Import project from JSON file into existing project

<br>Use case  <br>User attaches project as json file taken from export or export-by-testPlans method  <br>User runs method execution  <br>System updates project  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    include_attachments = True # bool |  (optional)
    file = open('/path/to/file', 'rb') # file_type | Select file (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import project from JSON file into existing project
        api_instance.import_to_existing_project(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->import_to_existing_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import project from JSON file into existing project
        api_instance.import_to_existing_project(id, include_attachments=include_attachments, file=file)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->import_to_existing_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **include_attachments** | **bool**|  | [optional]
 **file** | **file_type**| Select file | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**413** | Multipart body length limit exceeded |  -  |
**204** | No Content |  -  |
**403** | Update permission for project settings required |  -  |
**409** | Entity with same id already imported in other project |  -  |
**404** | File not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_project**
> restore_project(id)

Restore project

<br>Use case  <br>User sets project internal or global identifier and runs method execution  <br>System search and restores deleted project  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier

    # example passing only required values which don't have defaults set
    try:
        # Restore project
        api_instance.restore_project(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->restore_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |

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
**403** | Update permission for projects is required |  -  |
**404** | Project with provided ID was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_attributes_in_project**
> [CustomAttributeGetModel] search_attributes_in_project(id)

Search for attributes used in the project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.custom_attribute_get_model import CustomAttributeGetModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_attributes_filter_model import ProjectAttributesFilterModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global project ID
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    project_attributes_filter_model = ProjectAttributesFilterModel(
        name="name_example",
        is_required=True,
        is_global=True,
        types=[
            CustomAttributeTypesEnum("string"),
        ],
        is_enabled=True,
    ) # ProjectAttributesFilterModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for attributes used in the project
        api_response = api_instance.search_attributes_in_project(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->search_attributes_in_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for attributes used in the project
        api_response = api_instance.search_attributes_in_project(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, project_attributes_filter_model=project_attributes_filter_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->search_attributes_in_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global project ID |
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **project_attributes_filter_model** | [**ProjectAttributesFilterModel**](ProjectAttributesFilterModel.md)|  | [optional]

### Return type

[**[CustomAttributeGetModel]**](CustomAttributeGetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**403** | Read permission for project is required |  -  |
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_test_plan_attributes_in_project**
> [CustomAttributeGetModel] search_test_plan_attributes_in_project(id)

Search for attributes used in the project test plans

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.custom_attribute_get_model import CustomAttributeGetModel
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.project_attributes_filter_model import ProjectAttributesFilterModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global project ID
    skip = 1 # int | Amount of items to be skipped (offset) (optional)
    take = 1 # int | Amount of items to be taken (limit) (optional)
    order_by = "OrderBy_example" # str | SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) (optional)
    search_field = "SearchField_example" # str | Property name for searching (optional)
    search_value = "SearchValue_example" # str | Value for searching (optional)
    project_attributes_filter_model = ProjectAttributesFilterModel(
        name="name_example",
        is_required=True,
        is_global=True,
        types=[
            CustomAttributeTypesEnum("string"),
        ],
        is_enabled=True,
    ) # ProjectAttributesFilterModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search for attributes used in the project test plans
        api_response = api_instance.search_test_plan_attributes_in_project(id)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->search_test_plan_attributes_in_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search for attributes used in the project test plans
        api_response = api_instance.search_test_plan_attributes_in_project(id, skip=skip, take=take, order_by=order_by, search_field=search_field, search_value=search_value, project_attributes_filter_model=project_attributes_filter_model)
        pprint(api_response)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->search_test_plan_attributes_in_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global project ID |
 **skip** | **int**| Amount of items to be skipped (offset) | [optional]
 **take** | **int**| Amount of items to be taken (limit) | [optional]
 **order_by** | **str**| SQL-like  ORDER BY statement (column1 ASC|DESC , column2 ASC|DESC) | [optional]
 **search_field** | **str**| Property name for searching | [optional]
 **search_value** | **str**| Value for searching | [optional]
 **project_attributes_filter_model** | [**ProjectAttributesFilterModel**](ProjectAttributesFilterModel.md)|  | [optional]

### Return type

[**[CustomAttributeGetModel]**](CustomAttributeGetModel.md)

### Authorization

[Bearer or PrivateToken](../README.md#Bearer or PrivateToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * Pagination-Skip - Skipped amount of items <br>  * Pagination-Take - Taken items <br>  * Pagination-Pages - Expected number of pages <br>  * Pagination-Total-Items - Total count of items <br>  |
**403** | Read permission for project is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_attribute_test_plan_project_relations**
> update_custom_attribute_test_plan_project_relations(id)

Update attribute of project's test plans

<br>Use case  <br>User sets project internal or global identifier and attribute model  <br>User runs method execution  <br>System updates project and project attribute for test plan  <br>System returns no content response

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.custom_attribute_test_plan_project_relation_put_model import CustomAttributeTestPlanProjectRelationPutModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Project internal (UUID) or global (integer) identifier
    custom_attribute_test_plan_project_relation_put_model = CustomAttributeTestPlanProjectRelationPutModel(
        id="id_example",
        is_enabled=True,
        is_required=True,
    ) # CustomAttributeTestPlanProjectRelationPutModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update attribute of project's test plans
        api_instance.update_custom_attribute_test_plan_project_relations(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->update_custom_attribute_test_plan_project_relations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update attribute of project's test plans
        api_instance.update_custom_attribute_test_plan_project_relations(id, custom_attribute_test_plan_project_relation_put_model=custom_attribute_test_plan_project_relation_put_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->update_custom_attribute_test_plan_project_relations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Project internal (UUID) or global (integer) identifier |
 **custom_attribute_test_plan_project_relation_put_model** | [**CustomAttributeTestPlanProjectRelationPutModel**](CustomAttributeTestPlanProjectRelationPutModel.md)|  | [optional]

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
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> update_project()

Update project

<br>Use case  <br>User sets project parameters (listed in request example) and runs method execution  <br>System updates project  <br>System returns updated project model (example listed in response parameters)

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.project_put_model import ProjectPutModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    project_put_model = ProjectPutModel(
        id="id_example",
        description="description_example",
        name="name_example",
        is_favorite=True,
    ) # ProjectPutModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update project
        api_instance.update_project(project_put_model=project_put_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_put_model** | [**ProjectPutModel**](ProjectPutModel.md)|  | [optional]

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
**400** | &lt;br&gt;- ID is invalid  &lt;br&gt;- Field is required |  -  |
**403** | Update permission for projects is required |  -  |
**404** | Project with provided ID was not found |  -  |
**409** | Project with the same name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_projects_attribute**
> update_projects_attribute(id)

Edit attribute of the project

### Example

* Api Key Authentication (Bearer or PrivateToken):

```python
import time
import testit_api_client
from testit_api_client.api import projects_api
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.custom_attribute_put_model import CustomAttributePutModel
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
    api_instance = projects_api.ProjectsApi(api_client)
    id = "id_example" # str | Unique or global project ID
    custom_attribute_put_model = CustomAttributePutModel(
        id="id_example",
        options=[
            CustomAttributeOptionModel(
                id="id_example",
                is_deleted=True,
                value="value_example",
                is_default=True,
            ),
        ],
        type=CustomAttributeTypesEnum("string"),
        is_deleted=True,
        name="name_example",
        is_enabled=True,
        is_required=True,
        is_global=True,
    ) # CustomAttributePutModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit attribute of the project
        api_instance.update_projects_attribute(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->update_projects_attribute: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit attribute of the project
        api_instance.update_projects_attribute(id, custom_attribute_put_model=custom_attribute_put_model)
    except testit_api_client.ApiException as e:
        print("Exception when calling ProjectsApi->update_projects_attribute: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Unique or global project ID |
 **custom_attribute_put_model** | [**CustomAttributePutModel**](CustomAttributePutModel.md)|  | [optional]

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
**403** | Update permission for project settings is required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

