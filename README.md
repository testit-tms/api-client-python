# Api client for Test IT TMS
![Test IT](https://raw.githubusercontent.com/testit-tms/api-client-python/master/images/banner.png)

[![Release
Status](https://img.shields.io/pypi/v/testit-api-client?style=plastic)](https://pypi.python.org/pypi/testit-api-client)
[![Downloads](https://img.shields.io/pypi/dm/testit-api-client?style=plastic)](https://pypi.python.org/pypi/testit-api-client)
[![GitHub contributors](https://img.shields.io/github/contributors/testit-tms/api-client-python?style=plastic)](https://github.com/testit-tms/api-client-python)

## Getting Started

### Compatibility

| Test IT | API Client |
|---------|------------|
| 3.5     | 2.0.4      |
| 4.0     | 3.0.0      |
| 4.2     | 3.1.0      |
| 4.3     | 3.2.0      |
| 4.4     | 3.3.0      |
| 4.5     | 3.4.0      |
| 4.6     | 3.5.0      |
| 5.0     | 4.0.0      |

## Installation & Usage
### pip install

```sh
pip install testit-api-client
```

Then import the package:

```python
import testit_api_client
```

## Examples

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import testit_api_client
from testit_api_client.api import attachments_api
from testit_api_client.model.attachment_model import AttachmentModel
from testit_api_client.model.image_resize_type import ImageResizeType
from testit_api_client.model.problem_details import ProblemDetails
from testit_api_client.model.validation_problem_details import ValidationProblemDetails

configuration = testit_api_client.Configuration(
    host = "Your TMS address"
)

with testit_api_client.ApiClient(
        configuration,
        header_name='Authorization',
        header_value='PrivateToken ' + 'Your private token') as api_client:
    api_instance = attachments_api.AttachmentsApi(api_client)
    id = "Attachment's guid in the TMS"

    try:
        api_instance.api_v2_attachments_id_delete(id)
    except testit_api_client.ApiException as e:
        print("Exception when calling AttachmentsApi->api_v2_attachments_id_delete: %s\n" % e)
```


## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AttachmentsApi* | [**api_v2_attachments_id_delete**](docs/AttachmentsApi.md#api_v2_attachments_id_delete) | **DELETE** /api/v2/attachments/{id} | Delete attachment file
*AttachmentsApi* | [**api_v2_attachments_id_get**](docs/AttachmentsApi.md#api_v2_attachments_id_get) | **GET** /api/v2/attachments/{id} | Download attachment file
*AttachmentsApi* | [**api_v2_attachments_occupied_file_storage_size_get**](docs/AttachmentsApi.md#api_v2_attachments_occupied_file_storage_size_get) | **GET** /api/v2/attachments/occupiedFileStorageSize | Get size of attachments storage in bytes
*AttachmentsApi* | [**api_v2_attachments_post**](docs/AttachmentsApi.md#api_v2_attachments_post) | **POST** /api/v2/attachments | Upload new attachment file
*AutoTestsApi* | [**api_v2_auto_tests_flaky_bulk_post**](docs/AutoTestsApi.md#api_v2_auto_tests_flaky_bulk_post) | **POST** /api/v2/autoTests/flaky/bulk | Set \&quot;Flaky\&quot; status for multiple autotests
*AutoTestsApi* | [**api_v2_auto_tests_id_patch**](docs/AutoTestsApi.md#api_v2_auto_tests_id_patch) | **PATCH** /api/v2/autoTests/{id} | Patch auto test
*AutoTestsApi* | [**api_v2_auto_tests_id_test_results_search_post**](docs/AutoTestsApi.md#api_v2_auto_tests_id_test_results_search_post) | **POST** /api/v2/autoTests/{id}/testResults/search | Get test results history for autotest
*AutoTestsApi* | [**api_v2_auto_tests_id_work_items_changed_id_get**](docs/AutoTestsApi.md#api_v2_auto_tests_id_work_items_changed_id_get) | **GET** /api/v2/autoTests/{id}/workItems/changed/id | Get identifiers of changed linked work items
*AutoTestsApi* | [**api_v2_auto_tests_id_work_items_changed_work_item_id_approve_post**](docs/AutoTestsApi.md#api_v2_auto_tests_id_work_items_changed_work_item_id_approve_post) | **POST** /api/v2/autoTests/{id}/workItems/changed/{workItemId}/approve | Approve changes to work items linked to autotest
*AutoTestsApi* | [**api_v2_auto_tests_search_post**](docs/AutoTestsApi.md#api_v2_auto_tests_search_post) | **POST** /api/v2/autoTests/search | Search for autotests
*AutoTestsApi* | [**create_auto_test**](docs/AutoTestsApi.md#create_auto_test) | **POST** /api/v2/autoTests | Create autotest
*AutoTestsApi* | [**create_multiple**](docs/AutoTestsApi.md#create_multiple) | **POST** /api/v2/autoTests/bulk | Create multiple autotests
*AutoTestsApi* | [**delete_auto_test**](docs/AutoTestsApi.md#delete_auto_test) | **DELETE** /api/v2/autoTests/{id} | Delete autotest
*AutoTestsApi* | [**delete_auto_test_link_from_work_item**](docs/AutoTestsApi.md#delete_auto_test_link_from_work_item) | **DELETE** /api/v2/autoTests/{id}/workItems | Unlink autotest from work item
*AutoTestsApi* | [**get_all_auto_tests**](docs/AutoTestsApi.md#get_all_auto_tests) | **GET** /api/v2/autoTests | 
*AutoTestsApi* | [**get_auto_test_average_duration**](docs/AutoTestsApi.md#get_auto_test_average_duration) | **GET** /api/v2/autoTests/{id}/averageDuration | Get average autotest duration
*AutoTestsApi* | [**get_auto_test_by_id**](docs/AutoTestsApi.md#get_auto_test_by_id) | **GET** /api/v2/autoTests/{id} | Get autotest by internal or global ID
*AutoTestsApi* | [**get_auto_test_chronology**](docs/AutoTestsApi.md#get_auto_test_chronology) | **GET** /api/v2/autoTests/{id}/chronology | Get autotest chronology
*AutoTestsApi* | [**get_test_runs**](docs/AutoTestsApi.md#get_test_runs) | **GET** /api/v2/autoTests/{id}/testRuns | Get completed tests runs for autotests
*AutoTestsApi* | [**get_work_item_results**](docs/AutoTestsApi.md#get_work_item_results) | **GET** /api/v2/autoTests/{id}/testResultHistory | 
*AutoTestsApi* | [**get_work_items_linked_to_auto_test**](docs/AutoTestsApi.md#get_work_items_linked_to_auto_test) | **GET** /api/v2/autoTests/{id}/workItems | Get work items linked to autotest
*AutoTestsApi* | [**link_auto_test_to_work_item**](docs/AutoTestsApi.md#link_auto_test_to_work_item) | **POST** /api/v2/autoTests/{id}/workItems | Link autotest with work items
*AutoTestsApi* | [**update_auto_test**](docs/AutoTestsApi.md#update_auto_test) | **PUT** /api/v2/autoTests | Update autotest
*AutoTestsApi* | [**update_multiple**](docs/AutoTestsApi.md#update_multiple) | **PUT** /api/v2/autoTests/bulk | Update multiple autotests
*BackgroundJobsApi* | [**api_v2_background_jobs_get**](docs/BackgroundJobsApi.md#api_v2_background_jobs_get) | **GET** /api/v2/backgroundJobs | 
*BackgroundJobsApi* | [**api_v2_background_jobs_id_cancel_post**](docs/BackgroundJobsApi.md#api_v2_background_jobs_id_cancel_post) | **POST** /api/v2/backgroundJobs/{id}/cancel | Cancel current user background job
*BackgroundJobsApi* | [**api_v2_background_jobs_id_get**](docs/BackgroundJobsApi.md#api_v2_background_jobs_id_get) | **GET** /api/v2/backgroundJobs/{id} | Get background job by ID
*BackgroundJobsApi* | [**api_v2_background_jobs_id_status_get**](docs/BackgroundJobsApi.md#api_v2_background_jobs_id_status_get) | **GET** /api/v2/backgroundJobs/{id}/status | Get background job status by job ID
*BackgroundJobsApi* | [**api_v2_background_jobs_search_post**](docs/BackgroundJobsApi.md#api_v2_background_jobs_search_post) | **POST** /api/v2/backgroundJobs/search | Search for user background jobs
*ConfigurationsApi* | [**api_v2_configurations_create_by_parameters_post**](docs/ConfigurationsApi.md#api_v2_configurations_create_by_parameters_post) | **POST** /api/v2/configurations/createByParameters | Create configurations by parameters
*ConfigurationsApi* | [**api_v2_configurations_delete_bulk_post**](docs/ConfigurationsApi.md#api_v2_configurations_delete_bulk_post) | **POST** /api/v2/configurations/delete/bulk | Delete multiple configurations
*ConfigurationsApi* | [**api_v2_configurations_id_delete**](docs/ConfigurationsApi.md#api_v2_configurations_id_delete) | **DELETE** /api/v2/configurations/{id} | Delete configuration
*ConfigurationsApi* | [**api_v2_configurations_id_patch**](docs/ConfigurationsApi.md#api_v2_configurations_id_patch) | **PATCH** /api/v2/configurations/{id} | Patch configuration
*ConfigurationsApi* | [**api_v2_configurations_id_purge_post**](docs/ConfigurationsApi.md#api_v2_configurations_id_purge_post) | **POST** /api/v2/configurations/{id}/purge | Permanently delete configuration from archive
*ConfigurationsApi* | [**api_v2_configurations_id_restore_post**](docs/ConfigurationsApi.md#api_v2_configurations_id_restore_post) | **POST** /api/v2/configurations/{id}/restore | Restore configuration from the archive
*ConfigurationsApi* | [**api_v2_configurations_purge_bulk_post**](docs/ConfigurationsApi.md#api_v2_configurations_purge_bulk_post) | **POST** /api/v2/configurations/purge/bulk | Permanently delete multiple archived configurations
*ConfigurationsApi* | [**api_v2_configurations_put**](docs/ConfigurationsApi.md#api_v2_configurations_put) | **PUT** /api/v2/configurations | Edit configuration
*ConfigurationsApi* | [**api_v2_configurations_restore_bulk_post**](docs/ConfigurationsApi.md#api_v2_configurations_restore_bulk_post) | **POST** /api/v2/configurations/restore/bulk | Restore multiple configurations from the archive
*ConfigurationsApi* | [**api_v2_configurations_search_post**](docs/ConfigurationsApi.md#api_v2_configurations_search_post) | **POST** /api/v2/configurations/search | Search for configurations
*ConfigurationsApi* | [**create_configuration**](docs/ConfigurationsApi.md#create_configuration) | **POST** /api/v2/configurations | Create Configuration
*ConfigurationsApi* | [**get_configuration_by_id**](docs/ConfigurationsApi.md#get_configuration_by_id) | **GET** /api/v2/configurations/{id} | Get configuration by internal or global ID
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_custom_attributes_exclude_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_custom_attributes_exclude_post) | **POST** /api/v2/customAttributes/templates/{id}/customAttributes/exclude | Exclude CustomAttributes from CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_custom_attributes_include_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_custom_attributes_include_post) | **POST** /api/v2/customAttributes/templates/{id}/customAttributes/include | Include CustomAttributes to CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_delete**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_delete) | **DELETE** /api/v2/customAttributes/templates/{id} | Delete CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_get**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_get) | **GET** /api/v2/customAttributes/templates/{id} | Get CustomAttributeTemplate by ID
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_name_get**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_name_get) | **GET** /api/v2/customAttributes/templates/{name} | Get CustomAttributeTemplate by name
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_post) | **POST** /api/v2/customAttributes/templates | Create CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_put**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_put) | **PUT** /api/v2/customAttributes/templates | Update custom attributes template
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_search_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_search_post) | **POST** /api/v2/customAttributes/templates/search | Search CustomAttributeTemplates
*CustomAttributesApi* | [**api_v2_custom_attributes_global_id_delete**](docs/CustomAttributesApi.md#api_v2_custom_attributes_global_id_delete) | **DELETE** /api/v2/customAttributes/global/{id} | Delete global attribute
*CustomAttributesApi* | [**api_v2_custom_attributes_global_id_put**](docs/CustomAttributesApi.md#api_v2_custom_attributes_global_id_put) | **PUT** /api/v2/customAttributes/global/{id} | Edit global attribute
*CustomAttributesApi* | [**api_v2_custom_attributes_global_post**](docs/CustomAttributesApi.md#api_v2_custom_attributes_global_post) | **POST** /api/v2/customAttributes/global | Create global attribute
*CustomAttributesApi* | [**api_v2_custom_attributes_id_get**](docs/CustomAttributesApi.md#api_v2_custom_attributes_id_get) | **GET** /api/v2/customAttributes/{id} | Get attribute
*CustomAttributesApi* | [**api_v2_custom_attributes_search_post**](docs/CustomAttributesApi.md#api_v2_custom_attributes_search_post) | **POST** /api/v2/customAttributes/search | Search for attributes
*NotificationsApi* | [**api_v2_notifications_count_get**](docs/NotificationsApi.md#api_v2_notifications_count_get) | **GET** /api/v2/notifications/count | Get unread Notifications total in last 7 days
*NotificationsApi* | [**api_v2_notifications_get**](docs/NotificationsApi.md#api_v2_notifications_get) | **GET** /api/v2/notifications | Get all Notifications for current User
*NotificationsApi* | [**api_v2_notifications_id_read_post**](docs/NotificationsApi.md#api_v2_notifications_id_read_post) | **POST** /api/v2/notifications/{id}/read | Set Notification as read
*NotificationsApi* | [**api_v2_notifications_read_post**](docs/NotificationsApi.md#api_v2_notifications_read_post) | **POST** /api/v2/notifications/read | Set all Notifications as read
*NotificationsApi* | [**api_v2_notifications_search_post**](docs/NotificationsApi.md#api_v2_notifications_search_post) | **POST** /api/v2/notifications/search | Search Notifications for current User
*ParametersApi* | [**api_v2_parameters_bulk_post**](docs/ParametersApi.md#api_v2_parameters_bulk_post) | **POST** /api/v2/parameters/bulk | Create multiple parameters
*ParametersApi* | [**api_v2_parameters_bulk_put**](docs/ParametersApi.md#api_v2_parameters_bulk_put) | **PUT** /api/v2/parameters/bulk | Update multiple parameters
*ParametersApi* | [**api_v2_parameters_groups_get**](docs/ParametersApi.md#api_v2_parameters_groups_get) | **GET** /api/v2/parameters/groups | Get parameters as group
*ParametersApi* | [**api_v2_parameters_key_name_name_exists_get**](docs/ParametersApi.md#api_v2_parameters_key_name_name_exists_get) | **GET** /api/v2/parameters/key/name/{name}/exists | Check existence parameter key in system
*ParametersApi* | [**api_v2_parameters_key_values_get**](docs/ParametersApi.md#api_v2_parameters_key_values_get) | **GET** /api/v2/parameters/{key}/values | Get all parameter key values
*ParametersApi* | [**api_v2_parameters_keys_get**](docs/ParametersApi.md#api_v2_parameters_keys_get) | **GET** /api/v2/parameters/keys | Get all parameter keys
*ParametersApi* | [**api_v2_parameters_search_groups_post**](docs/ParametersApi.md#api_v2_parameters_search_groups_post) | **POST** /api/v2/parameters/search/groups | Search for parameters as group
*ParametersApi* | [**api_v2_parameters_search_post**](docs/ParametersApi.md#api_v2_parameters_search_post) | **POST** /api/v2/parameters/search | Search for parameters
*ParametersApi* | [**create_parameter**](docs/ParametersApi.md#create_parameter) | **POST** /api/v2/parameters | Create parameter
*ParametersApi* | [**delete_by_name**](docs/ParametersApi.md#delete_by_name) | **DELETE** /api/v2/parameters/name/{name} | Delete parameter by name
*ParametersApi* | [**delete_by_parameter_key_id**](docs/ParametersApi.md#delete_by_parameter_key_id) | **DELETE** /api/v2/parameters/keyId/{keyId} | Delete parameters by parameter key identifier
*ParametersApi* | [**delete_parameter**](docs/ParametersApi.md#delete_parameter) | **DELETE** /api/v2/parameters/{id} | Delete parameter
*ParametersApi* | [**get_all_parameters**](docs/ParametersApi.md#get_all_parameters) | **GET** /api/v2/parameters | Get all parameters
*ParametersApi* | [**get_parameter_by_id**](docs/ParametersApi.md#get_parameter_by_id) | **GET** /api/v2/parameters/{id} | Get parameter by ID
*ParametersApi* | [**update_parameter**](docs/ParametersApi.md#update_parameter) | **PUT** /api/v2/parameters | Update parameter
*ProjectAttributeTemplatesApi* | [**api_v2_projects_project_id_attributes_templates_search_post**](docs/ProjectAttributeTemplatesApi.md#api_v2_projects_project_id_attributes_templates_search_post) | **POST** /api/v2/projects/{projectId}/attributes/templates/search | Search for custom attributes templates
*ProjectAttributeTemplatesApi* | [**api_v2_projects_project_id_attributes_templates_template_id_delete**](docs/ProjectAttributeTemplatesApi.md#api_v2_projects_project_id_attributes_templates_template_id_delete) | **DELETE** /api/v2/projects/{projectId}/attributes/templates/{templateId} | Delete CustomAttributeTemplate from Project
*ProjectAttributeTemplatesApi* | [**api_v2_projects_project_id_attributes_templates_template_id_post**](docs/ProjectAttributeTemplatesApi.md#api_v2_projects_project_id_attributes_templates_template_id_post) | **POST** /api/v2/projects/{projectId}/attributes/templates/{templateId} | Add CustomAttributeTemplate to Project
*ProjectAttributesApi* | [**create_projects_attribute**](docs/ProjectAttributesApi.md#create_projects_attribute) | **POST** /api/v2/projects/{projectId}/attributes | Create project attribute
*ProjectAttributesApi* | [**delete_projects_attribute**](docs/ProjectAttributesApi.md#delete_projects_attribute) | **DELETE** /api/v2/projects/{projectId}/attributes/{attributeId} | Delete project attribute
*ProjectAttributesApi* | [**get_attribute_by_project_id**](docs/ProjectAttributesApi.md#get_attribute_by_project_id) | **GET** /api/v2/projects/{projectId}/attributes/{attributeId} | Get project attribute
*ProjectAttributesApi* | [**get_attributes_by_project_id**](docs/ProjectAttributesApi.md#get_attributes_by_project_id) | **GET** /api/v2/projects/{projectId}/attributes | Get project attributes
*ProjectAttributesApi* | [**search_attributes_in_project**](docs/ProjectAttributesApi.md#search_attributes_in_project) | **POST** /api/v2/projects/{projectId}/attributes/search | Search for attributes used in the project
*ProjectAttributesApi* | [**update_projects_attribute**](docs/ProjectAttributesApi.md#update_projects_attribute) | **PUT** /api/v2/projects/{projectId}/attributes | Edit attribute of the project
*ProjectConfigurationsApi* | [**get_configurations_by_project_id**](docs/ProjectConfigurationsApi.md#get_configurations_by_project_id) | **GET** /api/v2/projects/{projectId}/configurations | Get project configurations
*ProjectExportApi* | [**export**](docs/ProjectExportApi.md#export) | **POST** /api/v2/projects/{projectId}/export | Export project as JSON file
*ProjectExportApi* | [**export_project_json**](docs/ProjectExportApi.md#export_project_json) | **POST** /api/v2/projects/{projectId}/export/json | Export project as JSON file in background job
*ProjectExportApi* | [**export_project_with_test_plans_json**](docs/ProjectExportApi.md#export_project_with_test_plans_json) | **POST** /api/v2/projects/{projectId}/export/testPlans/json | Export project as JSON file with test plans in background job
*ProjectExportApi* | [**export_project_with_test_plans_zip**](docs/ProjectExportApi.md#export_project_with_test_plans_zip) | **POST** /api/v2/projects/{projectId}/export/testPlans/zip | Export project as Zip file with test plans in background job
*ProjectExportApi* | [**export_project_zip**](docs/ProjectExportApi.md#export_project_zip) | **POST** /api/v2/projects/{projectId}/export/zip | Export project as Zip file in background job
*ProjectImportApi* | [**background_import_to_existing_project**](docs/ProjectImportApi.md#background_import_to_existing_project) | **POST** /api/v2/projects/{projectId}/import/json | Import project from JSON file into existing project in background job
*ProjectImportApi* | [**background_import_zip_to_existing_project**](docs/ProjectImportApi.md#background_import_zip_to_existing_project) | **POST** /api/v2/projects/{projectId}/import/zip | Import project from Zip file into existing project in background job
*ProjectImportApi* | [**import_to_existing_project**](docs/ProjectImportApi.md#import_to_existing_project) | **POST** /api/v2/projects/{projectId}/import | Import project from JSON file into existing project
*ProjectSectionsApi* | [**get_sections_by_project_id**](docs/ProjectSectionsApi.md#get_sections_by_project_id) | **GET** /api/v2/projects/{projectId}/sections | Get project sections
*ProjectTestPlanAttributesApi* | [**create_custom_attribute_test_plan_project_relations**](docs/ProjectTestPlanAttributesApi.md#create_custom_attribute_test_plan_project_relations) | **POST** /api/v2/projects/{projectId}/testPlans/attributes | Add attributes to project&#39;s test plans
*ProjectTestPlanAttributesApi* | [**delete_custom_attribute_test_plan_project_relations**](docs/ProjectTestPlanAttributesApi.md#delete_custom_attribute_test_plan_project_relations) | **DELETE** /api/v2/projects/{projectId}/testPlans/attributes/{attributeId} | Delete attribute from project&#39;s test plans
*ProjectTestPlanAttributesApi* | [**get_custom_attribute_test_plan_project_relations**](docs/ProjectTestPlanAttributesApi.md#get_custom_attribute_test_plan_project_relations) | **GET** /api/v2/projects/{projectId}/testPlans/attributes | Get project&#39;s test plan attributes
*ProjectTestPlanAttributesApi* | [**search_test_plan_attributes_in_project**](docs/ProjectTestPlanAttributesApi.md#search_test_plan_attributes_in_project) | **POST** /api/v2/projects/{projectId}/testPlans/attributes/search | Search for attributes used in the project test plans
*ProjectTestPlanAttributesApi* | [**update_custom_attribute_test_plan_project_relations**](docs/ProjectTestPlanAttributesApi.md#update_custom_attribute_test_plan_project_relations) | **PUT** /api/v2/projects/{projectId}/testPlans/attributes | Update attribute of project&#39;s test plans
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_analytics_get**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_analytics_get) | **GET** /api/v2/projects/{projectId}/testPlans/analytics | Get TestPlans analytics
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_delete_bulk_post**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_delete_bulk_post) | **POST** /api/v2/projects/{projectId}/testPlans/delete/bulk | Delete multiple test plans
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_name_exists_get**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_name_exists_get) | **GET** /api/v2/projects/{projectId}/testPlans/{name}/exists | Checks if TestPlan exists with the specified name exists for the project
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_purge_bulk_post**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_purge_bulk_post) | **POST** /api/v2/projects/{projectId}/testPlans/purge/bulk | Permanently delete multiple archived test plans
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_restore_bulk_post**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_restore_bulk_post) | **POST** /api/v2/projects/{projectId}/testPlans/restore/bulk | Restore multiple test plans
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_search_post**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_search_post) | **POST** /api/v2/projects/{projectId}/testPlans/search | Get Project TestPlans with analytics
*ProjectWorkItemsApi* | [**api_v2_projects_project_id_work_items_search_grouped_post**](docs/ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_search_grouped_post) | **POST** /api/v2/projects/{projectId}/workItems/search/grouped | Search for work items and group results by attribute
*ProjectWorkItemsApi* | [**api_v2_projects_project_id_work_items_search_id_post**](docs/ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_search_id_post) | **POST** /api/v2/projects/{projectId}/workItems/search/id | Search for work items and extract IDs only
*ProjectWorkItemsApi* | [**api_v2_projects_project_id_work_items_search_post**](docs/ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_search_post) | **POST** /api/v2/projects/{projectId}/workItems/search | Search for work items
*ProjectWorkItemsApi* | [**api_v2_projects_project_id_work_items_tags_get**](docs/ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_tags_get) | **GET** /api/v2/projects/{projectId}/workItems/tags | Get WorkItems Tags
*ProjectWorkItemsApi* | [**get_work_items_by_project_id**](docs/ProjectWorkItemsApi.md#get_work_items_by_project_id) | **GET** /api/v2/projects/{projectId}/workItems | Get project work items
*ProjectsApi* | [**add_globa_attributes_to_project**](docs/ProjectsApi.md#add_globa_attributes_to_project) | **POST** /api/v2/projects/{id}/globalAttributes | Add global attributes to project
*ProjectsApi* | [**api_v2_projects_demo_post**](docs/ProjectsApi.md#api_v2_projects_demo_post) | **POST** /api/v2/projects/demo | 
*ProjectsApi* | [**api_v2_projects_id_delete**](docs/ProjectsApi.md#api_v2_projects_id_delete) | **DELETE** /api/v2/projects/{id} | Archive project
*ProjectsApi* | [**api_v2_projects_id_failure_classes_get**](docs/ProjectsApi.md#api_v2_projects_id_failure_classes_get) | **GET** /api/v2/projects/{id}/failureClasses | Get failure classes
*ProjectsApi* | [**api_v2_projects_id_favorite_put**](docs/ProjectsApi.md#api_v2_projects_id_favorite_put) | **PUT** /api/v2/projects/{id}/favorite | Mark Project as favorite
*ProjectsApi* | [**api_v2_projects_id_filters_get**](docs/ProjectsApi.md#api_v2_projects_id_filters_get) | **GET** /api/v2/projects/{id}/filters | Get Project filters
*ProjectsApi* | [**api_v2_projects_id_patch**](docs/ProjectsApi.md#api_v2_projects_id_patch) | **PATCH** /api/v2/projects/{id} | Patch project
*ProjectsApi* | [**api_v2_projects_id_purge_post**](docs/ProjectsApi.md#api_v2_projects_id_purge_post) | **POST** /api/v2/projects/{id}/purge | Purge archived project
*ProjectsApi* | [**api_v2_projects_id_restore_post**](docs/ProjectsApi.md#api_v2_projects_id_restore_post) | **POST** /api/v2/projects/{id}/restore | Restore archived project
*ProjectsApi* | [**api_v2_projects_id_test_plans_attribute_attribute_id_delete**](docs/ProjectsApi.md#api_v2_projects_id_test_plans_attribute_attribute_id_delete) | **DELETE** /api/v2/projects/{id}/testPlans/attribute/{attributeId} | Delete attribute from project&#39;s test plans
*ProjectsApi* | [**api_v2_projects_id_test_plans_attribute_put**](docs/ProjectsApi.md#api_v2_projects_id_test_plans_attribute_put) | **PUT** /api/v2/projects/{id}/testPlans/attribute | Update attribute of project&#39;s test plans
*ProjectsApi* | [**api_v2_projects_id_test_runs_active_get**](docs/ProjectsApi.md#api_v2_projects_id_test_runs_active_get) | **GET** /api/v2/projects/{id}/testRuns/active | Get active Project TestRuns
*ProjectsApi* | [**api_v2_projects_id_test_runs_full_get**](docs/ProjectsApi.md#api_v2_projects_id_test_runs_full_get) | **GET** /api/v2/projects/{id}/testRuns/full | Get Project TestRuns full models
*ProjectsApi* | [**api_v2_projects_name_name_exists_get**](docs/ProjectsApi.md#api_v2_projects_name_name_exists_get) | **GET** /api/v2/projects/name/{name}/exists | 
*ProjectsApi* | [**api_v2_projects_purge_bulk_post**](docs/ProjectsApi.md#api_v2_projects_purge_bulk_post) | **POST** /api/v2/projects/purge/bulk | Purge multiple projects
*ProjectsApi* | [**api_v2_projects_restore_bulk_post**](docs/ProjectsApi.md#api_v2_projects_restore_bulk_post) | **POST** /api/v2/projects/restore/bulk | Restore multiple projects
*ProjectsApi* | [**api_v2_projects_search_post**](docs/ProjectsApi.md#api_v2_projects_search_post) | **POST** /api/v2/projects/search | Search for projects
*ProjectsApi* | [**background_import_project**](docs/ProjectsApi.md#background_import_project) | **POST** /api/v2/projects/import/json | Import project from JSON file in background job
*ProjectsApi* | [**background_import_zip_project**](docs/ProjectsApi.md#background_import_zip_project) | **POST** /api/v2/projects/import/zip | Import project from Zip file in background job
*ProjectsApi* | [**call_import**](docs/ProjectsApi.md#call_import) | **POST** /api/v2/projects/import | Import project from JSON file
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /api/v2/projects | Create project
*ProjectsApi* | [**delete_project_auto_tests**](docs/ProjectsApi.md#delete_project_auto_tests) | **DELETE** /api/v2/projects/{id}/autoTests | Delete all autotests from project
*ProjectsApi* | [**export_with_test_plans_and_configurations**](docs/ProjectsApi.md#export_with_test_plans_and_configurations) | **POST** /api/v2/projects/{id}/export-by-testPlans | Export project with test plans, test suites and test points as JSON file
*ProjectsApi* | [**get_all_projects**](docs/ProjectsApi.md#get_all_projects) | **GET** /api/v2/projects | Get all projects
*ProjectsApi* | [**get_auto_tests_namespaces**](docs/ProjectsApi.md#get_auto_tests_namespaces) | **GET** /api/v2/projects/{id}/autoTestsNamespaces | Get namespaces of autotests in project
*ProjectsApi* | [**get_project_by_id**](docs/ProjectsApi.md#get_project_by_id) | **GET** /api/v2/projects/{id} | Get project by ID
*ProjectsApi* | [**get_test_plans_by_project_id**](docs/ProjectsApi.md#get_test_plans_by_project_id) | **GET** /api/v2/projects/{id}/testPlans | Get project test plans
*ProjectsApi* | [**get_test_runs_by_project_id**](docs/ProjectsApi.md#get_test_runs_by_project_id) | **GET** /api/v2/projects/{id}/testRuns | Get project test runs
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /api/v2/projects | Update project
*SearchApi* | [**api_v2_search_global_search_post**](docs/SearchApi.md#api_v2_search_global_search_post) | **POST** /api/v2/search/globalSearch | 
*SectionsApi* | [**api_v2_sections_id_patch**](docs/SectionsApi.md#api_v2_sections_id_patch) | **PATCH** /api/v2/sections/{id} | Patch section
*SectionsApi* | [**create_section**](docs/SectionsApi.md#create_section) | **POST** /api/v2/sections | Create section
*SectionsApi* | [**delete_section**](docs/SectionsApi.md#delete_section) | **DELETE** /api/v2/sections/{id} | Delete section
*SectionsApi* | [**get_section_by_id**](docs/SectionsApi.md#get_section_by_id) | **GET** /api/v2/sections/{id} | Get section
*SectionsApi* | [**get_work_items_by_section_id**](docs/SectionsApi.md#get_work_items_by_section_id) | **GET** /api/v2/sections/{id}/workItems | Get section work items
*SectionsApi* | [**move**](docs/SectionsApi.md#move) | **POST** /api/v2/sections/move | Move section with all work items into another section
*SectionsApi* | [**rename**](docs/SectionsApi.md#rename) | **POST** /api/v2/sections/rename | Rename section
*SectionsApi* | [**update_section**](docs/SectionsApi.md#update_section) | **PUT** /api/v2/sections | Update section
*TagsApi* | [**api_v2_tags_delete**](docs/TagsApi.md#api_v2_tags_delete) | **DELETE** /api/v2/tags | Delete tags
*TagsApi* | [**api_v2_tags_get**](docs/TagsApi.md#api_v2_tags_get) | **GET** /api/v2/tags | Get all Tags
*TagsApi* | [**api_v2_tags_id_delete**](docs/TagsApi.md#api_v2_tags_id_delete) | **DELETE** /api/v2/tags/{id} | Delete tag
*TagsApi* | [**api_v2_tags_post**](docs/TagsApi.md#api_v2_tags_post) | **POST** /api/v2/tags | Create tag
*TagsApi* | [**api_v2_tags_put**](docs/TagsApi.md#api_v2_tags_put) | **PUT** /api/v2/tags | Update tag
*TagsApi* | [**api_v2_tags_search_get**](docs/TagsApi.md#api_v2_tags_search_get) | **GET** /api/v2/tags/search | Search tags
*TagsApi* | [**api_v2_tags_test_plans_tags_get**](docs/TagsApi.md#api_v2_tags_test_plans_tags_get) | **GET** /api/v2/tags/testPlansTags | Get all Tags that are used in TestPlans
*TestPlansApi* | [**add_test_points_with_sections**](docs/TestPlansApi.md#add_test_points_with_sections) | **POST** /api/v2/testPlans/{id}/test-points/withSections | Add test-points to TestPlan with sections
*TestPlansApi* | [**add_work_items_with_sections**](docs/TestPlansApi.md#add_work_items_with_sections) | **POST** /api/v2/testPlans/{id}/workItems/withSections | Add WorkItems to TestPlan with Sections as TestSuites
*TestPlansApi* | [**api_v2_test_plans_id_analytics_get**](docs/TestPlansApi.md#api_v2_test_plans_id_analytics_get) | **GET** /api/v2/testPlans/{id}/analytics | Get analytics by TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_autobalance_post**](docs/TestPlansApi.md#api_v2_test_plans_id_autobalance_post) | **POST** /api/v2/testPlans/{id}/autobalance | Distribute test points between the users
*TestPlansApi* | [**api_v2_test_plans_id_configurations_get**](docs/TestPlansApi.md#api_v2_test_plans_id_configurations_get) | **GET** /api/v2/testPlans/{id}/configurations | Get TestPlan configurations
*TestPlansApi* | [**api_v2_test_plans_id_export_test_points_xlsx_post**](docs/TestPlansApi.md#api_v2_test_plans_id_export_test_points_xlsx_post) | **POST** /api/v2/testPlans/{id}/export/testPoints/xlsx | Export TestPoints from TestPlan in xls format
*TestPlansApi* | [**api_v2_test_plans_id_export_test_result_history_xlsx_post**](docs/TestPlansApi.md#api_v2_test_plans_id_export_test_result_history_xlsx_post) | **POST** /api/v2/testPlans/{id}/export/testResultHistory/xlsx | Export TestResults history from TestPlan in xls format
*TestPlansApi* | [**api_v2_test_plans_id_history_get**](docs/TestPlansApi.md#api_v2_test_plans_id_history_get) | **GET** /api/v2/testPlans/{id}/history | Get TestPlan history
*TestPlansApi* | [**api_v2_test_plans_id_links_get**](docs/TestPlansApi.md#api_v2_test_plans_id_links_get) | **GET** /api/v2/testPlans/{id}/links | Get Links of TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_patch**](docs/TestPlansApi.md#api_v2_test_plans_id_patch) | **PATCH** /api/v2/testPlans/{id} | Patch test plan
*TestPlansApi* | [**api_v2_test_plans_id_test_points_last_results_get**](docs/TestPlansApi.md#api_v2_test_plans_id_test_points_last_results_get) | **GET** /api/v2/testPlans/{id}/testPoints/lastResults | Get TestPoints with last result from TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_test_points_reset_post**](docs/TestPlansApi.md#api_v2_test_plans_id_test_points_reset_post) | **POST** /api/v2/testPlans/{id}/testPoints/reset | Reset TestPoints status of TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_test_points_tester_delete**](docs/TestPlansApi.md#api_v2_test_plans_id_test_points_tester_delete) | **DELETE** /api/v2/testPlans/{id}/testPoints/tester | Unassign users from multiple test points
*TestPlansApi* | [**api_v2_test_plans_id_test_points_tester_user_id_post**](docs/TestPlansApi.md#api_v2_test_plans_id_test_points_tester_user_id_post) | **POST** /api/v2/testPlans/{id}/testPoints/tester/{userId} | Assign user as a tester to multiple test points
*TestPlansApi* | [**api_v2_test_plans_id_test_runs_get**](docs/TestPlansApi.md#api_v2_test_plans_id_test_runs_get) | **GET** /api/v2/testPlans/{id}/testRuns | Get TestRuns of TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_test_runs_search_post**](docs/TestPlansApi.md#api_v2_test_plans_id_test_runs_search_post) | **POST** /api/v2/testPlans/{id}/testRuns/search | Search TestRuns of TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get**](docs/TestPlansApi.md#api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get) | **GET** /api/v2/testPlans/{id}/testRuns/testResults/lastModified/modifiedDate | Get last modification date of test plan&#39;s test results
*TestPlansApi* | [**api_v2_test_plans_id_unlock_request_post**](docs/TestPlansApi.md#api_v2_test_plans_id_unlock_request_post) | **POST** /api/v2/testPlans/{id}/unlock/request | Send unlock TestPlan notification
*TestPlansApi* | [**api_v2_test_plans_shorts_post**](docs/TestPlansApi.md#api_v2_test_plans_shorts_post) | **POST** /api/v2/testPlans/shorts | Get TestPlans short models by Project identifiers
*TestPlansApi* | [**clone**](docs/TestPlansApi.md#clone) | **POST** /api/v2/testPlans/{id}/clone | Clone TestPlan
*TestPlansApi* | [**complete**](docs/TestPlansApi.md#complete) | **POST** /api/v2/testPlans/{id}/complete | Complete TestPlan
*TestPlansApi* | [**create_test_plan**](docs/TestPlansApi.md#create_test_plan) | **POST** /api/v2/testPlans | Create TestPlan
*TestPlansApi* | [**delete_test_plan**](docs/TestPlansApi.md#delete_test_plan) | **DELETE** /api/v2/testPlans/{id} | Delete TestPlan
*TestPlansApi* | [**get_test_plan_by_id**](docs/TestPlansApi.md#get_test_plan_by_id) | **GET** /api/v2/testPlans/{id} | Get TestPlan by Id
*TestPlansApi* | [**get_test_suites_by_id**](docs/TestPlansApi.md#get_test_suites_by_id) | **GET** /api/v2/testPlans/{id}/testSuites | Get TestSuites Tree By Id
*TestPlansApi* | [**pause**](docs/TestPlansApi.md#pause) | **POST** /api/v2/testPlans/{id}/pause | Pause TestPlan
*TestPlansApi* | [**purge_test_plan**](docs/TestPlansApi.md#purge_test_plan) | **POST** /api/v2/testPlans/{id}/purge | Permanently delete test plan from archive
*TestPlansApi* | [**restore_test_plan**](docs/TestPlansApi.md#restore_test_plan) | **POST** /api/v2/testPlans/{id}/restore | Restore TestPlan
*TestPlansApi* | [**start**](docs/TestPlansApi.md#start) | **POST** /api/v2/testPlans/{id}/start | Start TestPlan
*TestPlansApi* | [**update_test_plan**](docs/TestPlansApi.md#update_test_plan) | **PUT** /api/v2/testPlans | Update TestPlan
*TestPointsApi* | [**api_v2_test_points_id_test_runs_get**](docs/TestPointsApi.md#api_v2_test_points_id_test_runs_get) | **GET** /api/v2/testPoints/{id}/testRuns | Get all test runs which use test point
*TestPointsApi* | [**api_v2_test_points_id_work_item_get**](docs/TestPointsApi.md#api_v2_test_points_id_work_item_get) | **GET** /api/v2/testPoints/{id}/workItem | Get work item represented by test point
*TestPointsApi* | [**api_v2_test_points_search_id_post**](docs/TestPointsApi.md#api_v2_test_points_search_id_post) | **POST** /api/v2/testPoints/search/id | Search for test points and extract IDs only
*TestPointsApi* | [**api_v2_test_points_search_post**](docs/TestPointsApi.md#api_v2_test_points_search_post) | **POST** /api/v2/testPoints/search | Search for test points
*TestResultsApi* | [**api_v2_test_results_id_aggregated_get**](docs/TestResultsApi.md#api_v2_test_results_id_aggregated_get) | **GET** /api/v2/testResults/{id}/aggregated | Get test result by ID aggregated with previous results
*TestResultsApi* | [**api_v2_test_results_id_attachments_attachment_id_put**](docs/TestResultsApi.md#api_v2_test_results_id_attachments_attachment_id_put) | **PUT** /api/v2/testResults/{id}/attachments/{attachmentId} | Attach file to the test result
*TestResultsApi* | [**api_v2_test_results_id_attachments_info_get**](docs/TestResultsApi.md#api_v2_test_results_id_attachments_info_get) | **GET** /api/v2/testResults/{id}/attachments/info | Get test result attachments meta-information
*TestResultsApi* | [**api_v2_test_results_id_get**](docs/TestResultsApi.md#api_v2_test_results_id_get) | **GET** /api/v2/testResults/{id} | Get test result by ID
*TestResultsApi* | [**api_v2_test_results_id_put**](docs/TestResultsApi.md#api_v2_test_results_id_put) | **PUT** /api/v2/testResults/{id} | Edit test result by ID
*TestResultsApi* | [**api_v2_test_results_search_post**](docs/TestResultsApi.md#api_v2_test_results_search_post) | **POST** /api/v2/testResults/search | Search for test results
*TestResultsApi* | [**api_v2_test_results_statistics_filter_post**](docs/TestResultsApi.md#api_v2_test_results_statistics_filter_post) | **POST** /api/v2/testResults/statistics/filter | Search for test results and extract statistics
*TestResultsApi* | [**create_attachment**](docs/TestResultsApi.md#create_attachment) | **POST** /api/v2/testResults/{id}/attachments | Upload and link attachment to TestResult
*TestResultsApi* | [**delete_attachment**](docs/TestResultsApi.md#delete_attachment) | **DELETE** /api/v2/testResults/{id}/attachments/{attachmentId} | Remove attachment and unlink from TestResult
*TestResultsApi* | [**download_attachment**](docs/TestResultsApi.md#download_attachment) | **GET** /api/v2/testResults/{id}/attachments/{attachmentId} | Get attachment of TestResult
*TestResultsApi* | [**get_attachment**](docs/TestResultsApi.md#get_attachment) | **GET** /api/v2/testResults/{id}/attachments/{attachmentId}/info | Get Metadata of TestResult&#39;s attachment
*TestResultsApi* | [**get_attachments**](docs/TestResultsApi.md#get_attachments) | **GET** /api/v2/testResults/{id}/attachments | Get all attachments of TestResult
*TestRunsApi* | [**api_v2_test_runs_delete**](docs/TestRunsApi.md#api_v2_test_runs_delete) | **DELETE** /api/v2/testRuns | Delete multiple test runs
*TestRunsApi* | [**api_v2_test_runs_id_delete**](docs/TestRunsApi.md#api_v2_test_runs_id_delete) | **DELETE** /api/v2/testRuns/{id} | Delete test run
*TestRunsApi* | [**api_v2_test_runs_id_purge_post**](docs/TestRunsApi.md#api_v2_test_runs_id_purge_post) | **POST** /api/v2/testRuns/{id}/purge | Permanently delete test run from archive
*TestRunsApi* | [**api_v2_test_runs_id_restore_post**](docs/TestRunsApi.md#api_v2_test_runs_id_restore_post) | **POST** /api/v2/testRuns/{id}/restore | Restore test run from the archive
*TestRunsApi* | [**api_v2_test_runs_id_statistics_filter_post**](docs/TestRunsApi.md#api_v2_test_runs_id_statistics_filter_post) | **POST** /api/v2/testRuns/{id}/statistics/filter | Search for the test run test results and build statistics
*TestRunsApi* | [**api_v2_test_runs_id_test_points_results_get**](docs/TestRunsApi.md#api_v2_test_runs_id_test_points_results_get) | **GET** /api/v2/testRuns/{id}/testPoints/results | Get test results from the test run grouped by test points
*TestRunsApi* | [**api_v2_test_runs_id_test_results_bulk_put**](docs/TestRunsApi.md#api_v2_test_runs_id_test_results_bulk_put) | **PUT** /api/v2/testRuns/{id}/testResults/bulk | Partial edit of multiple test results in the test run
*TestRunsApi* | [**api_v2_test_runs_id_test_results_last_modified_modification_date_get**](docs/TestRunsApi.md#api_v2_test_runs_id_test_results_last_modified_modification_date_get) | **GET** /api/v2/testRuns/{id}/testResults/lastModified/modificationDate | Get modification date of last test result of the test run
*TestRunsApi* | [**api_v2_test_runs_purge_bulk_post**](docs/TestRunsApi.md#api_v2_test_runs_purge_bulk_post) | **POST** /api/v2/testRuns/purge/bulk | Permanently delete multiple test runs from archive
*TestRunsApi* | [**api_v2_test_runs_restore_bulk_post**](docs/TestRunsApi.md#api_v2_test_runs_restore_bulk_post) | **POST** /api/v2/testRuns/restore/bulk | Restore multiple test runs from the archive
*TestRunsApi* | [**api_v2_test_runs_search_post**](docs/TestRunsApi.md#api_v2_test_runs_search_post) | **POST** /api/v2/testRuns/search | Search for test runs
*TestRunsApi* | [**api_v2_test_runs_update_multiple_post**](docs/TestRunsApi.md#api_v2_test_runs_update_multiple_post) | **POST** /api/v2/testRuns/updateMultiple | Update multiple test runs
*TestRunsApi* | [**complete_test_run**](docs/TestRunsApi.md#complete_test_run) | **POST** /api/v2/testRuns/{id}/complete | Complete TestRun
*TestRunsApi* | [**create_and_fill_by_auto_tests**](docs/TestRunsApi.md#create_and_fill_by_auto_tests) | **POST** /api/v2/testRuns/byAutoTests | Create test runs based on autotests and configurations
*TestRunsApi* | [**create_and_fill_by_configurations**](docs/TestRunsApi.md#create_and_fill_by_configurations) | **POST** /api/v2/testRuns/byConfigurations | Create test runs picking the needed test points
*TestRunsApi* | [**create_and_fill_by_work_items**](docs/TestRunsApi.md#create_and_fill_by_work_items) | **POST** /api/v2/testRuns/byWorkItems | Create test run based on configurations and work items
*TestRunsApi* | [**create_empty**](docs/TestRunsApi.md#create_empty) | **POST** /api/v2/testRuns | Create empty TestRun
*TestRunsApi* | [**get_test_run_by_id**](docs/TestRunsApi.md#get_test_run_by_id) | **GET** /api/v2/testRuns/{id} | Get TestRun by Id
*TestRunsApi* | [**set_auto_test_results_for_test_run**](docs/TestRunsApi.md#set_auto_test_results_for_test_run) | **POST** /api/v2/testRuns/{id}/testResults | Send test results to the test runs in the system
*TestRunsApi* | [**start_test_run**](docs/TestRunsApi.md#start_test_run) | **POST** /api/v2/testRuns/{id}/start | Start TestRun
*TestRunsApi* | [**stop_test_run**](docs/TestRunsApi.md#stop_test_run) | **POST** /api/v2/testRuns/{id}/stop | Stop TestRun
*TestRunsApi* | [**update_empty**](docs/TestRunsApi.md#update_empty) | **PUT** /api/v2/testRuns | Update empty TestRun
*TestSuitesApi* | [**add_test_points_to_test_suite**](docs/TestSuitesApi.md#add_test_points_to_test_suite) | **POST** /api/v2/testSuites/{id}/test-points | Add test-points to test suite
*TestSuitesApi* | [**api_v2_test_suites_id_patch**](docs/TestSuitesApi.md#api_v2_test_suites_id_patch) | **PATCH** /api/v2/testSuites/{id} | Patch test suite
*TestSuitesApi* | [**api_v2_test_suites_id_refresh_post**](docs/TestSuitesApi.md#api_v2_test_suites_id_refresh_post) | **POST** /api/v2/testSuites/{id}/refresh | Refresh test suite. Only dynamic test suites are supported by this method
*TestSuitesApi* | [**api_v2_test_suites_id_work_items_post**](docs/TestSuitesApi.md#api_v2_test_suites_id_work_items_post) | **POST** /api/v2/testSuites/{id}/workItems | Set work items for test suite
*TestSuitesApi* | [**api_v2_test_suites_post**](docs/TestSuitesApi.md#api_v2_test_suites_post) | **POST** /api/v2/testSuites | Create test suite
*TestSuitesApi* | [**api_v2_test_suites_put**](docs/TestSuitesApi.md#api_v2_test_suites_put) | **PUT** /api/v2/testSuites | Edit test suite
*TestSuitesApi* | [**delete_test_suite**](docs/TestSuitesApi.md#delete_test_suite) | **DELETE** /api/v2/testSuites/{id} | Delete TestSuite
*TestSuitesApi* | [**get_configurations_by_test_suite_id**](docs/TestSuitesApi.md#get_configurations_by_test_suite_id) | **GET** /api/v2/testSuites/{id}/configurations | Get Configurations By Id
*TestSuitesApi* | [**get_test_points_by_id**](docs/TestSuitesApi.md#get_test_points_by_id) | **GET** /api/v2/testSuites/{id}/testPoints | Get TestPoints By Id
*TestSuitesApi* | [**get_test_results_by_id**](docs/TestSuitesApi.md#get_test_results_by_id) | **GET** /api/v2/testSuites/{id}/testResults | Get TestResults By Id
*TestSuitesApi* | [**get_test_suite_by_id**](docs/TestSuitesApi.md#get_test_suite_by_id) | **GET** /api/v2/testSuites/{id} | Get TestSuite by Id
*TestSuitesApi* | [**search_work_items**](docs/TestSuitesApi.md#search_work_items) | **POST** /api/v2/testSuites/{id}/workItems/search | Search WorkItems
*TestSuitesApi* | [**set_configurations_by_test_suite_id**](docs/TestSuitesApi.md#set_configurations_by_test_suite_id) | **POST** /api/v2/testSuites/{id}/configurations | Set Configurations By TestSuite Id
*WebhooksApi* | [**api_v2_webhooks_get**](docs/WebhooksApi.md#api_v2_webhooks_get) | **GET** /api/v2/webhooks | Get all webhooks
*WebhooksApi* | [**api_v2_webhooks_id_delete**](docs/WebhooksApi.md#api_v2_webhooks_id_delete) | **DELETE** /api/v2/webhooks/{id} | Delete webhook by ID
*WebhooksApi* | [**api_v2_webhooks_id_get**](docs/WebhooksApi.md#api_v2_webhooks_id_get) | **GET** /api/v2/webhooks/{id} | Get webhook by ID
*WebhooksApi* | [**api_v2_webhooks_id_put**](docs/WebhooksApi.md#api_v2_webhooks_id_put) | **PUT** /api/v2/webhooks/{id} | Edit webhook by ID
*WebhooksApi* | [**api_v2_webhooks_post**](docs/WebhooksApi.md#api_v2_webhooks_post) | **POST** /api/v2/webhooks | Create webhook
*WebhooksApi* | [**api_v2_webhooks_search_post**](docs/WebhooksApi.md#api_v2_webhooks_search_post) | **POST** /api/v2/webhooks/search | Search for webhooks
*WebhooksApi* | [**api_v2_webhooks_special_variables_get**](docs/WebhooksApi.md#api_v2_webhooks_special_variables_get) | **GET** /api/v2/webhooks/specialVariables | Get special variables for webhook event type
*WebhooksApi* | [**api_v2_webhooks_test_post**](docs/WebhooksApi.md#api_v2_webhooks_test_post) | **POST** /api/v2/webhooks/test | Test webhook&#39;s url
*WebhooksLogsApi* | [**api_v2_webhooks_logs_get**](docs/WebhooksLogsApi.md#api_v2_webhooks_logs_get) | **GET** /api/v2/webhooks/logs | Get all webhook logs
*WebhooksLogsApi* | [**api_v2_webhooks_logs_id_delete**](docs/WebhooksLogsApi.md#api_v2_webhooks_logs_id_delete) | **DELETE** /api/v2/webhooks/logs/{id} | Delete webhook log by ID
*WebhooksLogsApi* | [**api_v2_webhooks_logs_id_get**](docs/WebhooksLogsApi.md#api_v2_webhooks_logs_id_get) | **GET** /api/v2/webhooks/logs/{id} | Get webhook log by ID
*WorkItemsApi* | [**api_v2_work_items_id_attachments_post**](docs/WorkItemsApi.md#api_v2_work_items_id_attachments_post) | **POST** /api/v2/workItems/{id}/attachments | Upload and link attachment to WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_check_list_transform_to_test_case_post**](docs/WorkItemsApi.md#api_v2_work_items_id_check_list_transform_to_test_case_post) | **POST** /api/v2/workItems/{id}/checkList/transformTo/testCase | Transform CheckList to TestCase
*WorkItemsApi* | [**api_v2_work_items_id_history_get**](docs/WorkItemsApi.md#api_v2_work_items_id_history_get) | **GET** /api/v2/workItems/{id}/history | Get change history of WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_like_delete**](docs/WorkItemsApi.md#api_v2_work_items_id_like_delete) | **DELETE** /api/v2/workItems/{id}/like | Delete like from WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_like_post**](docs/WorkItemsApi.md#api_v2_work_items_id_like_post) | **POST** /api/v2/workItems/{id}/like | Set like to WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_likes_count_get**](docs/WorkItemsApi.md#api_v2_work_items_id_likes_count_get) | **GET** /api/v2/workItems/{id}/likes/count | Get likes count of WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_likes_get**](docs/WorkItemsApi.md#api_v2_work_items_id_likes_get) | **GET** /api/v2/workItems/{id}/likes | Get likes of WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_test_results_history_get**](docs/WorkItemsApi.md#api_v2_work_items_id_test_results_history_get) | **GET** /api/v2/workItems/{id}/testResults/history | Get test results history of WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_version_version_id_actual_post**](docs/WorkItemsApi.md#api_v2_work_items_id_version_version_id_actual_post) | **POST** /api/v2/workItems/{id}/version/{versionId}/actual | Set WorkItem as actual
*WorkItemsApi* | [**api_v2_work_items_move_post**](docs/WorkItemsApi.md#api_v2_work_items_move_post) | **POST** /api/v2/workItems/move | Move WorkItem to another section
*WorkItemsApi* | [**api_v2_work_items_search_post**](docs/WorkItemsApi.md#api_v2_work_items_search_post) | **POST** /api/v2/workItems/search | Search for work items
*WorkItemsApi* | [**api_v2_work_items_shared_step_id_references_sections_post**](docs/WorkItemsApi.md#api_v2_work_items_shared_step_id_references_sections_post) | **POST** /api/v2/workItems/{sharedStepId}/references/sections | Get SharedStep references in sections
*WorkItemsApi* | [**api_v2_work_items_shared_step_id_references_work_items_post**](docs/WorkItemsApi.md#api_v2_work_items_shared_step_id_references_work_items_post) | **POST** /api/v2/workItems/{sharedStepId}/references/workItems | Get SharedStep references in work items
*WorkItemsApi* | [**api_v2_work_items_shared_steps_shared_step_id_references_get**](docs/WorkItemsApi.md#api_v2_work_items_shared_steps_shared_step_id_references_get) | **GET** /api/v2/workItems/sharedSteps/{sharedStepId}/references | Get SharedStep references
*WorkItemsApi* | [**create_work_item**](docs/WorkItemsApi.md#create_work_item) | **POST** /api/v2/workItems | Create Test Case, Checklist or Shared Step
*WorkItemsApi* | [**delete_all_work_items_from_auto_test**](docs/WorkItemsApi.md#delete_all_work_items_from_auto_test) | **DELETE** /api/v2/workItems/{id}/autoTests | Delete all links AutoTests from WorkItem by Id or GlobalId
*WorkItemsApi* | [**delete_work_item**](docs/WorkItemsApi.md#delete_work_item) | **DELETE** /api/v2/workItems/{id} | Delete Test Case, Checklist or Shared Step by Id or GlobalId
*WorkItemsApi* | [**get_auto_tests_for_work_item**](docs/WorkItemsApi.md#get_auto_tests_for_work_item) | **GET** /api/v2/workItems/{id}/autoTests | Get all AutoTests linked to WorkItem by Id or GlobalId
*WorkItemsApi* | [**get_iterations**](docs/WorkItemsApi.md#get_iterations) | **GET** /api/v2/workItems/{id}/iterations | Get iterations by work item Id or GlobalId
*WorkItemsApi* | [**get_work_item_by_id**](docs/WorkItemsApi.md#get_work_item_by_id) | **GET** /api/v2/workItems/{id} | Get Test Case, Checklist or Shared Step by Id or GlobalId
*WorkItemsApi* | [**get_work_item_chronology**](docs/WorkItemsApi.md#get_work_item_chronology) | **GET** /api/v2/workItems/{id}/chronology | Get WorkItem chronology by Id or GlobalId
*WorkItemsApi* | [**get_work_item_versions**](docs/WorkItemsApi.md#get_work_item_versions) | **GET** /api/v2/workItems/{id}/versions | Get WorkItem versions
*WorkItemsApi* | [**purge_work_item**](docs/WorkItemsApi.md#purge_work_item) | **POST** /api/v2/workItems/{id}/purge | Permanently delete test case, checklist or shared steps from archive
*WorkItemsApi* | [**restore_work_item**](docs/WorkItemsApi.md#restore_work_item) | **POST** /api/v2/workItems/{id}/restore | Restore test case, checklist or shared steps from archive
*WorkItemsApi* | [**update_work_item**](docs/WorkItemsApi.md#update_work_item) | **PUT** /api/v2/workItems | Update Test Case, Checklist or Shared Step
*WorkItemsCommentsApi* | [**api_v2_work_items_comments_comment_id_delete**](docs/WorkItemsCommentsApi.md#api_v2_work_items_comments_comment_id_delete) | **DELETE** /api/v2/workItems/comments/{commentId} | Delete WorkItem comment
*WorkItemsCommentsApi* | [**api_v2_work_items_comments_post**](docs/WorkItemsCommentsApi.md#api_v2_work_items_comments_post) | **POST** /api/v2/workItems/comments | Create WorkItem comment
*WorkItemsCommentsApi* | [**api_v2_work_items_comments_put**](docs/WorkItemsCommentsApi.md#api_v2_work_items_comments_put) | **PUT** /api/v2/workItems/comments | Update work item comment
*WorkItemsCommentsApi* | [**api_v2_work_items_id_comments_get**](docs/WorkItemsCommentsApi.md#api_v2_work_items_id_comments_get) | **GET** /api/v2/workItems/{id}/comments | Get work item comments


## Documentation For Models

 - You can see the documentation [here](docs/Readme.md).


# Contributing

You can help to develop the project. Any contributions are **greatly appreciated**.

* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/testit-tms/api-client-python/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/testit-tms/api-client-python/blob/master/CODE_OF_CONDUCT.md) before posting your first idea as well.


# License

Distributed under the Apache-2.0 License. See [LICENSE](https://github.com/testit-tms/api-client-python/blob/master/LICENSE.md) for more information.

