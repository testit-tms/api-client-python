# Api client for Test IT TMS
![Test IT](https://raw.githubusercontent.com/testit-tms/api-client-python/master/images/banner.png)

[![Release Status](https://img.shields.io/pypi/v/testit-api-client?style=plastic)](https://pypi.python.org/pypi/testit-api-client)
[![Downloads](https://img.shields.io/pypi/dm/testit-api-client?style=plastic)](https://pypi.python.org/pypi/testit-api-client)
[![GitHub contributors](https://img.shields.io/github/contributors/testit-tms/api-client-python?style=plastic)](https://github.com/testit-tms/api-client-python)

## Getting Started

### Compatibility

| Test IT | API Client    |
|---------|---------------|
| 3.5     | 2.0.4         |
| 4.0     | 3.0.0         |
| 4.2     | 3.1.0         |
| 4.3     | 3.2.0         |
| 4.4     | 3.3.0         |
| 4.5     | 3.4.0         |
| 4.6     | 3.5.0         |
| 5.0     | 4.0.0         |
| 5.1     | 4.1.0         |
| 5.2     | 4.2.0         |
| 5.2.2   | 5.1.2.post522 |
| 5.3.0   | 6.0.1.post530 |
| 5.4.0   | 6.3.1.post540 |
| 5.4.1   | 7.0.3.post541 |
| 5.5.0   | 7.2.0.post550 |
| 5.6.0   | 7.4.0.post560 |
| Cloud   | 7.5.0 +       |

1. For current versions, see the releases tab. 
2. Starting with 5.2, we have added a TMS postscript, which means that the utility is compatible with a specific enterprise version. 
3. If you are in doubt about which version to use, check with the support staff. support@yoonion.ru

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
from testit_api_client.models.attachment_model import AttachmentModel
from testit_api_client.models.image_resize_type import ImageResizeType
from testit_api_client.models.problem_details import ProblemDetails
from testit_api_client.models.validation_problem_details import ValidationProblemDetails

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
*AttachmentsApi* | [**api_v2_attachments_id_metadata_get**](docs/AttachmentsApi.md#api_v2_attachments_id_metadata_get) | **GET** /api/v2/attachments/{id}/metadata | Get attachment metadata
*AttachmentsApi* | [**api_v2_attachments_occupied_file_storage_size_get**](docs/AttachmentsApi.md#api_v2_attachments_occupied_file_storage_size_get) | **GET** /api/v2/attachments/occupiedFileStorageSize | Get size of attachments storage in bytes
*AttachmentsApi* | [**api_v2_attachments_post**](docs/AttachmentsApi.md#api_v2_attachments_post) | **POST** /api/v2/attachments | Upload new attachment file
*AutoTestsApi* | [**api_v2_auto_tests_delete**](docs/AutoTestsApi.md#api_v2_auto_tests_delete) | **DELETE** /api/v2/autoTests | Delete autotests
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
*AutoTestsApi* | [**get_work_items_linked_to_auto_test**](docs/AutoTestsApi.md#get_work_items_linked_to_auto_test) | **GET** /api/v2/autoTests/{id}/workItems | Get work items linked to autotest
*AutoTestsApi* | [**link_auto_test_to_work_item**](docs/AutoTestsApi.md#link_auto_test_to_work_item) | **POST** /api/v2/autoTests/{id}/workItems | Link autotest with work items
*AutoTestsApi* | [**update_auto_test**](docs/AutoTestsApi.md#update_auto_test) | **PUT** /api/v2/autoTests | Update autotest
*AutoTestsApi* | [**update_multiple**](docs/AutoTestsApi.md#update_multiple) | **PUT** /api/v2/autoTests/bulk | Update multiple autotests
*BackgroundJobsApi* | [**api_v2_background_jobs_completed_delete**](docs/BackgroundJobsApi.md#api_v2_background_jobs_completed_delete) | **DELETE** /api/v2/backgroundJobs/completed | Delete all completed background jobs
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
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_exists_get**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_exists_get) | **GET** /api/v2/customAttributes/templates/exists | 
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_custom_attributes_exclude_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_custom_attributes_exclude_post) | **POST** /api/v2/customAttributes/templates/{id}/customAttributes/exclude | Exclude CustomAttributes from CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_custom_attributes_include_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_custom_attributes_include_post) | **POST** /api/v2/customAttributes/templates/{id}/customAttributes/include | Include CustomAttributes to CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_delete**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_delete) | **DELETE** /api/v2/customAttributes/templates/{id} | Delete CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_get**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_get) | **GET** /api/v2/customAttributes/templates/{id} | Get CustomAttributeTemplate by ID
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_name_get**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_name_get) | **GET** /api/v2/customAttributes/templates/{name} | Get CustomAttributeTemplate by name
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_post) | **POST** /api/v2/customAttributes/templates | Create CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_put**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_put) | **PUT** /api/v2/customAttributes/templates | Update custom attributes template
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_search_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_search_post) | **POST** /api/v2/customAttributes/templates/search | Search CustomAttributeTemplates
*CustomAttributesApi* | [**api_v2_custom_attributes_exists_get**](docs/CustomAttributesApi.md#api_v2_custom_attributes_exists_get) | **GET** /api/v2/customAttributes/exists | 
*CustomAttributesApi* | [**api_v2_custom_attributes_global_id_delete**](docs/CustomAttributesApi.md#api_v2_custom_attributes_global_id_delete) | **DELETE** /api/v2/customAttributes/global/{id} | Delete global attribute
*CustomAttributesApi* | [**api_v2_custom_attributes_global_id_put**](docs/CustomAttributesApi.md#api_v2_custom_attributes_global_id_put) | **PUT** /api/v2/customAttributes/global/{id} | Edit global attribute
*CustomAttributesApi* | [**api_v2_custom_attributes_global_post**](docs/CustomAttributesApi.md#api_v2_custom_attributes_global_post) | **POST** /api/v2/customAttributes/global | Create global attribute
*CustomAttributesApi* | [**api_v2_custom_attributes_id_get**](docs/CustomAttributesApi.md#api_v2_custom_attributes_id_get) | **GET** /api/v2/customAttributes/{id} | Get attribute
*CustomAttributesApi* | [**api_v2_custom_attributes_search_post**](docs/CustomAttributesApi.md#api_v2_custom_attributes_search_post) | **POST** /api/v2/customAttributes/search | Search for attributes
*ExternalIssuesApi* | [**api_v2_external_issues_suggestions_post**](docs/ExternalIssuesApi.md#api_v2_external_issues_suggestions_post) | **POST** /api/v2/external-issues/suggestions | Returns list of suggestions from available external issues
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
*ProjectSectionsApi* | [**get_sections_by_project_id**](docs/ProjectSectionsApi.md#get_sections_by_project_id) | **GET** /api/v2/projects/{projectId}/sections | Get project sections
*ProjectSettingsApi* | [**api_v2_projects_project_id_settings_autotests_post**](docs/ProjectSettingsApi.md#api_v2_projects_project_id_settings_autotests_post) | **POST** /api/v2/projects/{projectId}/settings/autotests | Set autotest project settings.
*ProjectSettingsApi* | [**get_autotest_project_settings**](docs/ProjectSettingsApi.md#get_autotest_project_settings) | **GET** /api/v2/projects/{projectId}/settings/autotests | Get autotest project settings.
*ProjectTestPlanAttributesApi* | [**create_custom_attribute_test_plan_project_relations**](docs/ProjectTestPlanAttributesApi.md#create_custom_attribute_test_plan_project_relations) | **POST** /api/v2/projects/{projectId}/testPlans/attributes | Add attributes to project&#39;s test plans
*ProjectTestPlanAttributesApi* | [**delete_custom_attribute_test_plan_project_relations**](docs/ProjectTestPlanAttributesApi.md#delete_custom_attribute_test_plan_project_relations) | **DELETE** /api/v2/projects/{projectId}/testPlans/attributes/{attributeId} | Delete attribute from project&#39;s test plans
*ProjectTestPlanAttributesApi* | [**get_custom_attribute_test_plan_project_relations**](docs/ProjectTestPlanAttributesApi.md#get_custom_attribute_test_plan_project_relations) | **GET** /api/v2/projects/{projectId}/testPlans/attributes | Get project&#39;s test plan attributes
*ProjectTestPlanAttributesApi* | [**search_test_plan_attributes_in_project**](docs/ProjectTestPlanAttributesApi.md#search_test_plan_attributes_in_project) | **POST** /api/v2/projects/{projectId}/testPlans/attributes/search | Search for attributes used in the project test plans
*ProjectTestPlanAttributesApi* | [**update_custom_attribute_test_plan_project_relations**](docs/ProjectTestPlanAttributesApi.md#update_custom_attribute_test_plan_project_relations) | **PUT** /api/v2/projects/{projectId}/testPlans/attributes | Update attribute of project&#39;s test plans
*ProjectTestPlanTestPointsApi* | [**api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post**](docs/ProjectTestPlanTestPointsApi.md#api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_rerun_post) | **POST** /api/v2/projects/{projectId}/test-plans/{testPlanId}/test-points/autotests/rerun | Rerun autotests.
*ProjectTestPlanTestPointsApi* | [**api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post**](docs/ProjectTestPlanTestPointsApi.md#api_v2_projects_project_id_test_plans_test_plan_id_test_points_autotests_run_post) | **POST** /api/v2/projects/{projectId}/test-plans/{testPlanId}/test-points/autotests/run | Run autotests.
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_analytics_get**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_analytics_get) | **GET** /api/v2/projects/{projectId}/testPlans/analytics | Get TestPlans analytics
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_delete_bulk_post**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_delete_bulk_post) | **POST** /api/v2/projects/{projectId}/testPlans/delete/bulk | Delete multiple test plans
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_name_exists_get**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_name_exists_get) | **GET** /api/v2/projects/{projectId}/testPlans/{name}/exists | Checks if TestPlan exists with the specified name exists for the project
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_purge_bulk_post**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_purge_bulk_post) | **POST** /api/v2/projects/{projectId}/testPlans/purge/bulk | Permanently delete multiple archived test plans
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_restore_bulk_post**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_restore_bulk_post) | **POST** /api/v2/projects/{projectId}/testPlans/restore/bulk | Restore multiple test plans
*ProjectTestPlansApi* | [**api_v2_projects_project_id_test_plans_search_post**](docs/ProjectTestPlansApi.md#api_v2_projects_project_id_test_plans_search_post) | **POST** /api/v2/projects/{projectId}/testPlans/search | Get Project TestPlans with analytics
*ProjectWorkItemsApi* | [**api_v2_projects_project_id_work_items_search_grouped_post**](docs/ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_search_grouped_post) | **POST** /api/v2/projects/{projectId}/workItems/search/grouped | Search for work items and group results by attribute
*ProjectWorkItemsApi* | [**api_v2_projects_project_id_work_items_search_id_post**](docs/ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_search_id_post) | **POST** /api/v2/projects/{projectId}/workItems/search/id | Search for work items and extract IDs only
*ProjectWorkItemsApi* | [**api_v2_projects_project_id_work_items_search_post**](docs/ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_search_post) | **POST** /api/v2/projects/{projectId}/workItems/search | Search for work items
*ProjectWorkItemsApi* | [**api_v2_projects_project_id_work_items_search_work_item_id_index_post**](docs/ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_search_work_item_id_index_post) | **POST** /api/v2/projects/{projectId}/workItems/search/{workItemId}/index | Get work item index (position) in a collection by its id.
*ProjectWorkItemsApi* | [**api_v2_projects_project_id_work_items_tags_get**](docs/ProjectWorkItemsApi.md#api_v2_projects_project_id_work_items_tags_get) | **GET** /api/v2/projects/{projectId}/workItems/tags | Get WorkItems Tags
*ProjectWorkItemsApi* | [**get_work_items_by_project_id**](docs/ProjectWorkItemsApi.md#get_work_items_by_project_id) | **GET** /api/v2/projects/{projectId}/workItems | Get project work items
*ProjectsApi* | [**add_global_attributes_to_project**](docs/ProjectsApi.md#add_global_attributes_to_project) | **POST** /api/v2/projects/{id}/globalAttributes | Add global attributes to project
*ProjectsApi* | [**api_v2_projects_demo_post**](docs/ProjectsApi.md#api_v2_projects_demo_post) | **POST** /api/v2/projects/demo | 
*ProjectsApi* | [**api_v2_projects_id_delete**](docs/ProjectsApi.md#api_v2_projects_id_delete) | **DELETE** /api/v2/projects/{id} | Archive project
*ProjectsApi* | [**api_v2_projects_id_failure_classes_get**](docs/ProjectsApi.md#api_v2_projects_id_failure_classes_get) | **GET** /api/v2/projects/{id}/failureClasses | Get failure classes
*ProjectsApi* | [**api_v2_projects_id_favorite_put**](docs/ProjectsApi.md#api_v2_projects_id_favorite_put) | **PUT** /api/v2/projects/{id}/favorite | Mark Project as favorite
*ProjectsApi* | [**api_v2_projects_id_filters_get**](docs/ProjectsApi.md#api_v2_projects_id_filters_get) | **GET** /api/v2/projects/{id}/filters | Get Project filters
*ProjectsApi* | [**api_v2_projects_id_patch**](docs/ProjectsApi.md#api_v2_projects_id_patch) | **PATCH** /api/v2/projects/{id} | Patch project
*ProjectsApi* | [**api_v2_projects_id_purge_post**](docs/ProjectsApi.md#api_v2_projects_id_purge_post) | **POST** /api/v2/projects/{id}/purge | Purge the project
*ProjectsApi* | [**api_v2_projects_id_restore_post**](docs/ProjectsApi.md#api_v2_projects_id_restore_post) | **POST** /api/v2/projects/{id}/restore | Restore archived project
*ProjectsApi* | [**api_v2_projects_id_test_plans_attribute_attribute_id_delete**](docs/ProjectsApi.md#api_v2_projects_id_test_plans_attribute_attribute_id_delete) | **DELETE** /api/v2/projects/{id}/testPlans/attribute/{attributeId} | Delete attribute from project&#39;s test plans
*ProjectsApi* | [**api_v2_projects_id_test_plans_attribute_put**](docs/ProjectsApi.md#api_v2_projects_id_test_plans_attribute_put) | **PUT** /api/v2/projects/{id}/testPlans/attribute | Update attribute of project&#39;s test plans
*ProjectsApi* | [**api_v2_projects_id_test_runs_full_get**](docs/ProjectsApi.md#api_v2_projects_id_test_runs_full_get) | **GET** /api/v2/projects/{id}/testRuns/full | Get Project TestRuns full models
*ProjectsApi* | [**api_v2_projects_name_name_exists_get**](docs/ProjectsApi.md#api_v2_projects_name_name_exists_get) | **GET** /api/v2/projects/name/{name}/exists | 
*ProjectsApi* | [**api_v2_projects_purge_bulk_post**](docs/ProjectsApi.md#api_v2_projects_purge_bulk_post) | **POST** /api/v2/projects/purge/bulk | Purge multiple projects
*ProjectsApi* | [**api_v2_projects_restore_bulk_post**](docs/ProjectsApi.md#api_v2_projects_restore_bulk_post) | **POST** /api/v2/projects/restore/bulk | Restore multiple projects
*ProjectsApi* | [**api_v2_projects_search_post**](docs/ProjectsApi.md#api_v2_projects_search_post) | **POST** /api/v2/projects/search | Search for projects
*ProjectsApi* | [**api_v2_projects_shorts_post**](docs/ProjectsApi.md#api_v2_projects_shorts_post) | **POST** /api/v2/projects/shorts | Get projects short models
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /api/v2/projects | Create project
*ProjectsApi* | [**delete_project_auto_tests**](docs/ProjectsApi.md#delete_project_auto_tests) | **DELETE** /api/v2/projects/{id}/autoTests | Delete all autotests from project
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
*TestPlansApi* | [**api_v2_test_plans_id_summaries_get**](docs/TestPlansApi.md#api_v2_test_plans_id_summaries_get) | **GET** /api/v2/testPlans/{id}/summaries | Get summary by TestPlan
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
*TestResultsApi* | [**api_v2_test_results_external_projects_external_project_id_defects_external_forms_post**](docs/TestResultsApi.md#api_v2_test_results_external_projects_external_project_id_defects_external_forms_post) | **POST** /api/v2/testResults/external-projects/{externalProjectId}/defects/external-forms | 
*TestResultsApi* | [**api_v2_test_results_external_projects_external_project_id_defects_post**](docs/TestResultsApi.md#api_v2_test_results_external_projects_external_project_id_defects_post) | **POST** /api/v2/testResults/external-projects/{externalProjectId}/defects | 
*TestResultsApi* | [**api_v2_test_results_id_aggregated_get**](docs/TestResultsApi.md#api_v2_test_results_id_aggregated_get) | **GET** /api/v2/testResults/{id}/aggregated | Get test result by ID aggregated with previous results
*TestResultsApi* | [**api_v2_test_results_id_attachments_attachment_id_put**](docs/TestResultsApi.md#api_v2_test_results_id_attachments_attachment_id_put) | **PUT** /api/v2/testResults/{id}/attachments/{attachmentId} | Attach file to the test result
*TestResultsApi* | [**api_v2_test_results_id_attachments_info_get**](docs/TestResultsApi.md#api_v2_test_results_id_attachments_info_get) | **GET** /api/v2/testResults/{id}/attachments/info | Get test result attachments meta-information
*TestResultsApi* | [**api_v2_test_results_id_get**](docs/TestResultsApi.md#api_v2_test_results_id_get) | **GET** /api/v2/testResults/{id} | Get test result by ID
*TestResultsApi* | [**api_v2_test_results_id_put**](docs/TestResultsApi.md#api_v2_test_results_id_put) | **PUT** /api/v2/testResults/{id} | Edit test result by ID
*TestResultsApi* | [**api_v2_test_results_id_reruns_get**](docs/TestResultsApi.md#api_v2_test_results_id_reruns_get) | **GET** /api/v2/testResults/{id}/reruns | Get reruns
*TestResultsApi* | [**api_v2_test_results_search_post**](docs/TestResultsApi.md#api_v2_test_results_search_post) | **POST** /api/v2/testResults/search | Search for test results
*TestResultsApi* | [**api_v2_test_results_statistics_filter_post**](docs/TestResultsApi.md#api_v2_test_results_statistics_filter_post) | **POST** /api/v2/testResults/statistics/filter | Search for test results and extract statistics
*TestResultsApi* | [**create_attachment**](docs/TestResultsApi.md#create_attachment) | **POST** /api/v2/testResults/{id}/attachments | Upload and link attachment to TestResult
*TestResultsApi* | [**delete_attachment**](docs/TestResultsApi.md#delete_attachment) | **DELETE** /api/v2/testResults/{id}/attachments/{attachmentId} | Remove attachment and unlink from TestResult
*TestResultsApi* | [**download_attachment**](docs/TestResultsApi.md#download_attachment) | **GET** /api/v2/testResults/{id}/attachments/{attachmentId} | Get attachment of TestResult
*TestResultsApi* | [**get_attachment**](docs/TestResultsApi.md#get_attachment) | **GET** /api/v2/testResults/{id}/attachments/{attachmentId}/info | Get Metadata of TestResult&#39;s attachment
*TestResultsApi* | [**get_attachments**](docs/TestResultsApi.md#get_attachments) | **GET** /api/v2/testResults/{id}/attachments | Get all attachments of TestResult
*TestRunsApi* | [**api_v2_test_runs_delete**](docs/TestRunsApi.md#api_v2_test_runs_delete) | **DELETE** /api/v2/testRuns | Delete multiple test runs
*TestRunsApi* | [**api_v2_test_runs_id_auto_tests_namespaces_get**](docs/TestRunsApi.md#api_v2_test_runs_id_auto_tests_namespaces_get) | **GET** /api/v2/testRuns/{id}/autoTestsNamespaces | Get autotest classes and namespaces in test run
*TestRunsApi* | [**api_v2_test_runs_id_delete**](docs/TestRunsApi.md#api_v2_test_runs_id_delete) | **DELETE** /api/v2/testRuns/{id} | Delete test run
*TestRunsApi* | [**api_v2_test_runs_id_purge_post**](docs/TestRunsApi.md#api_v2_test_runs_id_purge_post) | **POST** /api/v2/testRuns/{id}/purge | Permanently delete test run from archive
*TestRunsApi* | [**api_v2_test_runs_id_reruns_post**](docs/TestRunsApi.md#api_v2_test_runs_id_reruns_post) | **POST** /api/v2/testRuns/{id}/reruns | Manual autotests rerun in test run
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
*TestStatusesApi* | [**api_v2_test_statuses_code_code_exists_get**](docs/TestStatusesApi.md#api_v2_test_statuses_code_code_exists_get) | **GET** /api/v2/testStatuses/code/{code}/exists | 
*TestStatusesApi* | [**api_v2_test_statuses_id_delete**](docs/TestStatusesApi.md#api_v2_test_statuses_id_delete) | **DELETE** /api/v2/testStatuses/{id} | 
*TestStatusesApi* | [**api_v2_test_statuses_id_get**](docs/TestStatusesApi.md#api_v2_test_statuses_id_get) | **GET** /api/v2/testStatuses/{id} | 
*TestStatusesApi* | [**api_v2_test_statuses_id_put**](docs/TestStatusesApi.md#api_v2_test_statuses_id_put) | **PUT** /api/v2/testStatuses/{id} | 
*TestStatusesApi* | [**api_v2_test_statuses_name_name_exists_get**](docs/TestStatusesApi.md#api_v2_test_statuses_name_name_exists_get) | **GET** /api/v2/testStatuses/name/{name}/exists | 
*TestStatusesApi* | [**api_v2_test_statuses_post**](docs/TestStatusesApi.md#api_v2_test_statuses_post) | **POST** /api/v2/testStatuses | 
*TestStatusesApi* | [**api_v2_test_statuses_search_post**](docs/TestStatusesApi.md#api_v2_test_statuses_search_post) | **POST** /api/v2/testStatuses/search | 
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
*UsersApi* | [**api_v2_users_exists_get**](docs/UsersApi.md#api_v2_users_exists_get) | **GET** /api/v2/users/exists | 
*WebhooksApi* | [**api_v2_webhooks_delete**](docs/WebhooksApi.md#api_v2_webhooks_delete) | **DELETE** /api/v2/webhooks | 
*WebhooksApi* | [**api_v2_webhooks_get**](docs/WebhooksApi.md#api_v2_webhooks_get) | **GET** /api/v2/webhooks | Get all webhooks
*WebhooksApi* | [**api_v2_webhooks_id_delete**](docs/WebhooksApi.md#api_v2_webhooks_id_delete) | **DELETE** /api/v2/webhooks/{id} | Delete webhook by ID
*WebhooksApi* | [**api_v2_webhooks_id_get**](docs/WebhooksApi.md#api_v2_webhooks_id_get) | **GET** /api/v2/webhooks/{id} | Get webhook by ID
*WebhooksApi* | [**api_v2_webhooks_id_put**](docs/WebhooksApi.md#api_v2_webhooks_id_put) | **PUT** /api/v2/webhooks/{id} | Edit webhook by ID
*WebhooksApi* | [**api_v2_webhooks_post**](docs/WebhooksApi.md#api_v2_webhooks_post) | **POST** /api/v2/webhooks | Create webhook
*WebhooksApi* | [**api_v2_webhooks_put**](docs/WebhooksApi.md#api_v2_webhooks_put) | **PUT** /api/v2/webhooks | 
*WebhooksApi* | [**api_v2_webhooks_search_post**](docs/WebhooksApi.md#api_v2_webhooks_search_post) | **POST** /api/v2/webhooks/search | Search for webhooks
*WebhooksApi* | [**api_v2_webhooks_special_variables_get**](docs/WebhooksApi.md#api_v2_webhooks_special_variables_get) | **GET** /api/v2/webhooks/specialVariables | Get special variables for webhook event type
*WebhooksApi* | [**api_v2_webhooks_test_post**](docs/WebhooksApi.md#api_v2_webhooks_test_post) | **POST** /api/v2/webhooks/test | Test webhook&#39;s url
*WebhooksLogsApi* | [**api_v2_webhooks_logs_get**](docs/WebhooksLogsApi.md#api_v2_webhooks_logs_get) | **GET** /api/v2/webhooks/logs | Get last webhook logs
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
*WorkItemsApi* | [**api_v2_work_items_links_urls_search_post**](docs/WorkItemsApi.md#api_v2_work_items_links_urls_search_post) | **POST** /api/v2/workItems/links/urls/search | 
*WorkItemsApi* | [**api_v2_work_items_move_post**](docs/WorkItemsApi.md#api_v2_work_items_move_post) | **POST** /api/v2/workItems/move | Move WorkItem to another section
*WorkItemsApi* | [**api_v2_work_items_post**](docs/WorkItemsApi.md#api_v2_work_items_post) | **POST** /api/v2/workItems | Creates work item
*WorkItemsApi* | [**api_v2_work_items_search_post**](docs/WorkItemsApi.md#api_v2_work_items_search_post) | **POST** /api/v2/workItems/search | Search for work items
*WorkItemsApi* | [**api_v2_work_items_shared_step_id_references_sections_post**](docs/WorkItemsApi.md#api_v2_work_items_shared_step_id_references_sections_post) | **POST** /api/v2/workItems/{sharedStepId}/references/sections | Get SharedStep references in sections
*WorkItemsApi* | [**api_v2_work_items_shared_step_id_references_work_items_post**](docs/WorkItemsApi.md#api_v2_work_items_shared_step_id_references_work_items_post) | **POST** /api/v2/workItems/{sharedStepId}/references/workItems | Get SharedStep references in work items
*WorkItemsApi* | [**api_v2_work_items_shared_steps_shared_step_id_references_get**](docs/WorkItemsApi.md#api_v2_work_items_shared_steps_shared_step_id_references_get) | **GET** /api/v2/workItems/sharedSteps/{sharedStepId}/references | Get SharedStep references
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
*WorkItemsCommentsApi* | [**api_v2_work_items_id_comments_count_get**](docs/WorkItemsCommentsApi.md#api_v2_work_items_id_comments_count_get) | **GET** /api/v2/workItems/{id}/comments/count | Get work item comments count
*WorkItemsCommentsApi* | [**api_v2_work_items_id_comments_get**](docs/WorkItemsCommentsApi.md#api_v2_work_items_id_comments_get) | **GET** /api/v2/workItems/{id}/comments | Get work item comments
*WorkflowsApi* | [**api_v2_workflows_id_delete**](docs/WorkflowsApi.md#api_v2_workflows_id_delete) | **DELETE** /api/v2/workflows/{id} | 
*WorkflowsApi* | [**api_v2_workflows_id_get**](docs/WorkflowsApi.md#api_v2_workflows_id_get) | **GET** /api/v2/workflows/{id} | 
*WorkflowsApi* | [**api_v2_workflows_id_patch**](docs/WorkflowsApi.md#api_v2_workflows_id_patch) | **PATCH** /api/v2/workflows/{id} | 
*WorkflowsApi* | [**api_v2_workflows_id_projects_search_post**](docs/WorkflowsApi.md#api_v2_workflows_id_projects_search_post) | **POST** /api/v2/workflows/{id}/projects/search | 
*WorkflowsApi* | [**api_v2_workflows_id_put**](docs/WorkflowsApi.md#api_v2_workflows_id_put) | **PUT** /api/v2/workflows/{id} | 
*WorkflowsApi* | [**api_v2_workflows_name_name_exists_get**](docs/WorkflowsApi.md#api_v2_workflows_name_name_exists_get) | **GET** /api/v2/workflows/name/{name}/exists | 
*WorkflowsApi* | [**api_v2_workflows_post**](docs/WorkflowsApi.md#api_v2_workflows_post) | **POST** /api/v2/workflows | 
*WorkflowsApi* | [**api_v2_workflows_search_post**](docs/WorkflowsApi.md#api_v2_workflows_search_post) | **POST** /api/v2/workflows/search | 


## Documentation For Models

 - [AIServiceModelApiResult](docs/AIServiceModelApiResult.md)
 - [AIServiceModelApiResultReply](docs/AIServiceModelApiResultReply.md)
 - [ActionUpdate](docs/ActionUpdate.md)
 - [ApiExternalServiceCategory](docs/ApiExternalServiceCategory.md)
 - [ApiV2AutoTestsDeleteRequest](docs/ApiV2AutoTestsDeleteRequest.md)
 - [ApiV2AutoTestsFlakyBulkPostRequest](docs/ApiV2AutoTestsFlakyBulkPostRequest.md)
 - [ApiV2AutoTestsIdTestResultsSearchPostRequest](docs/ApiV2AutoTestsIdTestResultsSearchPostRequest.md)
 - [ApiV2AutoTestsSearchPostRequest](docs/ApiV2AutoTestsSearchPostRequest.md)
 - [ApiV2BackgroundJobsSearchPostRequest](docs/ApiV2BackgroundJobsSearchPostRequest.md)
 - [ApiV2ConfigurationsCreateByParametersPostRequest](docs/ApiV2ConfigurationsCreateByParametersPostRequest.md)
 - [ApiV2ConfigurationsDeleteBulkPostRequest](docs/ApiV2ConfigurationsDeleteBulkPostRequest.md)
 - [ApiV2ConfigurationsPurgeBulkPostRequest](docs/ApiV2ConfigurationsPurgeBulkPostRequest.md)
 - [ApiV2ConfigurationsPutRequest](docs/ApiV2ConfigurationsPutRequest.md)
 - [ApiV2ConfigurationsSearchPostRequest](docs/ApiV2ConfigurationsSearchPostRequest.md)
 - [ApiV2CustomAttributesGlobalIdPutRequest](docs/ApiV2CustomAttributesGlobalIdPutRequest.md)
 - [ApiV2CustomAttributesGlobalPostRequest](docs/ApiV2CustomAttributesGlobalPostRequest.md)
 - [ApiV2CustomAttributesSearchPostRequest](docs/ApiV2CustomAttributesSearchPostRequest.md)
 - [ApiV2CustomAttributesTemplatesPostRequest](docs/ApiV2CustomAttributesTemplatesPostRequest.md)
 - [ApiV2CustomAttributesTemplatesPutRequest](docs/ApiV2CustomAttributesTemplatesPutRequest.md)
 - [ApiV2CustomAttributesTemplatesSearchPostRequest](docs/ApiV2CustomAttributesTemplatesSearchPostRequest.md)
 - [ApiV2ExternalIssuesSuggestionsPostRequest](docs/ApiV2ExternalIssuesSuggestionsPostRequest.md)
 - [ApiV2NotificationsSearchPostRequest](docs/ApiV2NotificationsSearchPostRequest.md)
 - [ApiV2ParametersSearchGroupsPostRequest](docs/ApiV2ParametersSearchGroupsPostRequest.md)
 - [ApiV2ParametersSearchPostRequest](docs/ApiV2ParametersSearchPostRequest.md)
 - [ApiV2ProjectsProjectIdAttributesTemplatesSearchPostRequest](docs/ApiV2ProjectsProjectIdAttributesTemplatesSearchPostRequest.md)
 - [ApiV2ProjectsProjectIdSettingsAutotestsPostRequest](docs/ApiV2ProjectsProjectIdSettingsAutotestsPostRequest.md)
 - [ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest](docs/ApiV2ProjectsProjectIdTestPlansDeleteBulkPostRequest.md)
 - [ApiV2ProjectsProjectIdTestPlansSearchPostRequest](docs/ApiV2ProjectsProjectIdTestPlansSearchPostRequest.md)
 - [ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRerunPostRequest](docs/ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRerunPostRequest.md)
 - [ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRunPostRequest](docs/ApiV2ProjectsProjectIdTestPlansTestPlanIdTestPointsAutotestsRunPostRequest.md)
 - [ApiV2ProjectsProjectIdWorkItemsSearchGroupedPostRequest](docs/ApiV2ProjectsProjectIdWorkItemsSearchGroupedPostRequest.md)
 - [ApiV2ProjectsProjectIdWorkItemsSearchIdPostRequest](docs/ApiV2ProjectsProjectIdWorkItemsSearchIdPostRequest.md)
 - [ApiV2ProjectsProjectIdWorkItemsSearchPostRequest](docs/ApiV2ProjectsProjectIdWorkItemsSearchPostRequest.md)
 - [ApiV2ProjectsRestoreBulkPostRequest](docs/ApiV2ProjectsRestoreBulkPostRequest.md)
 - [ApiV2ProjectsSearchPostRequest](docs/ApiV2ProjectsSearchPostRequest.md)
 - [ApiV2ProjectsShortsPostRequest](docs/ApiV2ProjectsShortsPostRequest.md)
 - [ApiV2SearchGlobalSearchPostRequest](docs/ApiV2SearchGlobalSearchPostRequest.md)
 - [ApiV2TagsDeleteRequest](docs/ApiV2TagsDeleteRequest.md)
 - [ApiV2TagsPostRequest](docs/ApiV2TagsPostRequest.md)
 - [ApiV2TagsPutRequest](docs/ApiV2TagsPutRequest.md)
 - [ApiV2TestPlansIdExportTestPointsXlsxPostRequest](docs/ApiV2TestPlansIdExportTestPointsXlsxPostRequest.md)
 - [ApiV2TestPlansIdTestPointsTesterUserIdPostRequest](docs/ApiV2TestPlansIdTestPointsTesterUserIdPostRequest.md)
 - [ApiV2TestPlansIdTestRunsSearchPostRequest](docs/ApiV2TestPlansIdTestRunsSearchPostRequest.md)
 - [ApiV2TestPointsSearchPostRequest](docs/ApiV2TestPointsSearchPostRequest.md)
 - [ApiV2TestResultsExternalProjectsExternalProjectIdDefectsExternalFormsPostRequest](docs/ApiV2TestResultsExternalProjectsExternalProjectIdDefectsExternalFormsPostRequest.md)
 - [ApiV2TestResultsExternalProjectsExternalProjectIdDefectsPostRequest](docs/ApiV2TestResultsExternalProjectsExternalProjectIdDefectsPostRequest.md)
 - [ApiV2TestResultsIdPutRequest](docs/ApiV2TestResultsIdPutRequest.md)
 - [ApiV2TestResultsSearchPostRequest](docs/ApiV2TestResultsSearchPostRequest.md)
 - [ApiV2TestRunsDeleteRequest](docs/ApiV2TestRunsDeleteRequest.md)
 - [ApiV2TestRunsIdRerunsPostRequest](docs/ApiV2TestRunsIdRerunsPostRequest.md)
 - [ApiV2TestRunsIdStatisticsFilterPostRequest](docs/ApiV2TestRunsIdStatisticsFilterPostRequest.md)
 - [ApiV2TestRunsIdTestResultsBulkPutRequest](docs/ApiV2TestRunsIdTestResultsBulkPutRequest.md)
 - [ApiV2TestRunsSearchPostRequest](docs/ApiV2TestRunsSearchPostRequest.md)
 - [ApiV2TestRunsUpdateMultiplePostRequest](docs/ApiV2TestRunsUpdateMultiplePostRequest.md)
 - [ApiV2TestStatusesIdPutRequest](docs/ApiV2TestStatusesIdPutRequest.md)
 - [ApiV2TestStatusesPostRequest](docs/ApiV2TestStatusesPostRequest.md)
 - [ApiV2TestStatusesSearchPostRequest](docs/ApiV2TestStatusesSearchPostRequest.md)
 - [ApiV2TestSuitesPostRequest](docs/ApiV2TestSuitesPostRequest.md)
 - [ApiV2TestSuitesPutRequest](docs/ApiV2TestSuitesPutRequest.md)
 - [ApiV2WebhooksDeleteRequest](docs/ApiV2WebhooksDeleteRequest.md)
 - [ApiV2WebhooksPostRequest](docs/ApiV2WebhooksPostRequest.md)
 - [ApiV2WebhooksPutRequest](docs/ApiV2WebhooksPutRequest.md)
 - [ApiV2WebhooksSearchPostRequest](docs/ApiV2WebhooksSearchPostRequest.md)
 - [ApiV2WebhooksTestPostRequest](docs/ApiV2WebhooksTestPostRequest.md)
 - [ApiV2WorkItemsCommentsPostRequest](docs/ApiV2WorkItemsCommentsPostRequest.md)
 - [ApiV2WorkItemsCommentsPutRequest](docs/ApiV2WorkItemsCommentsPutRequest.md)
 - [ApiV2WorkItemsLinksUrlsSearchPostRequest](docs/ApiV2WorkItemsLinksUrlsSearchPostRequest.md)
 - [ApiV2WorkItemsMovePostRequest](docs/ApiV2WorkItemsMovePostRequest.md)
 - [ApiV2WorkItemsPostRequest](docs/ApiV2WorkItemsPostRequest.md)
 - [ApiV2WorkItemsSharedStepIdReferencesSectionsPostRequest](docs/ApiV2WorkItemsSharedStepIdReferencesSectionsPostRequest.md)
 - [ApiV2WorkItemsSharedStepIdReferencesWorkItemsPostRequest](docs/ApiV2WorkItemsSharedStepIdReferencesWorkItemsPostRequest.md)
 - [ApiV2WorkflowsIdProjectsSearchPostRequest](docs/ApiV2WorkflowsIdProjectsSearchPostRequest.md)
 - [ApiV2WorkflowsIdPutRequest](docs/ApiV2WorkflowsIdPutRequest.md)
 - [ApiV2WorkflowsPostRequest](docs/ApiV2WorkflowsPostRequest.md)
 - [ApiV2WorkflowsSearchPostRequest](docs/ApiV2WorkflowsSearchPostRequest.md)
 - [AssignAttachmentApiModel](docs/AssignAttachmentApiModel.md)
 - [AssignIterationApiModel](docs/AssignIterationApiModel.md)
 - [AttachmentApiResult](docs/AttachmentApiResult.md)
 - [AttachmentChangeViewModel](docs/AttachmentChangeViewModel.md)
 - [AttachmentChangeViewModelArrayChangedFieldViewModel](docs/AttachmentChangeViewModelArrayChangedFieldViewModel.md)
 - [AttachmentModel](docs/AttachmentModel.md)
 - [AttachmentPutModel](docs/AttachmentPutModel.md)
 - [AttachmentPutModelAutoTestStepResultsModel](docs/AttachmentPutModelAutoTestStepResultsModel.md)
 - [AttachmentUpdateRequest](docs/AttachmentUpdateRequest.md)
 - [AuditApiResult](docs/AuditApiResult.md)
 - [AutoTest](docs/AutoTest.md)
 - [AutoTestApiResult](docs/AutoTestApiResult.md)
 - [AutoTestAverageDurationApiResult](docs/AutoTestAverageDurationApiResult.md)
 - [AutoTestBulkDeleteApiModel](docs/AutoTestBulkDeleteApiModel.md)
 - [AutoTestBulkDeleteApiModelAutoTestSelect](docs/AutoTestBulkDeleteApiModelAutoTestSelect.md)
 - [AutoTestBulkDeleteApiResult](docs/AutoTestBulkDeleteApiResult.md)
 - [AutoTestChangeViewModel](docs/AutoTestChangeViewModel.md)
 - [AutoTestChangeViewModelArrayChangedFieldViewModel](docs/AutoTestChangeViewModelArrayChangedFieldViewModel.md)
 - [AutoTestClassCountApiModel](docs/AutoTestClassCountApiModel.md)
 - [AutoTestCreateApiModel](docs/AutoTestCreateApiModel.md)
 - [AutoTestExtractionApiModel](docs/AutoTestExtractionApiModel.md)
 - [AutoTestExtractionApiModelIds](docs/AutoTestExtractionApiModelIds.md)
 - [AutoTestFilterApiModel](docs/AutoTestFilterApiModel.md)
 - [AutoTestFilterApiModelCreatedDate](docs/AutoTestFilterApiModelCreatedDate.md)
 - [AutoTestFilterApiModelModifiedDate](docs/AutoTestFilterApiModelModifiedDate.md)
 - [AutoTestFilterApiModelStabilityPercentage](docs/AutoTestFilterApiModelStabilityPercentage.md)
 - [AutoTestFilterModel](docs/AutoTestFilterModel.md)
 - [AutoTestFlakyBulkApiModel](docs/AutoTestFlakyBulkApiModel.md)
 - [AutoTestFlakyBulkApiModelAutoTestSelect](docs/AutoTestFlakyBulkApiModelAutoTestSelect.md)
 - [AutoTestIdModel](docs/AutoTestIdModel.md)
 - [AutoTestLastTestResultConfiguration](docs/AutoTestLastTestResultConfiguration.md)
 - [AutoTestModel](docs/AutoTestModel.md)
 - [AutoTestModelLastTestResultConfiguration](docs/AutoTestModelLastTestResultConfiguration.md)
 - [AutoTestModelLastTestResultStatus](docs/AutoTestModelLastTestResultStatus.md)
 - [AutoTestModelV2GetModel](docs/AutoTestModelV2GetModel.md)
 - [AutoTestNamespaceApiResult](docs/AutoTestNamespaceApiResult.md)
 - [AutoTestNamespaceCountApiModel](docs/AutoTestNamespaceCountApiModel.md)
 - [AutoTestNamespacesCountResponse](docs/AutoTestNamespacesCountResponse.md)
 - [AutoTestOutcome](docs/AutoTestOutcome.md)
 - [AutoTestProjectSettingsApiModel](docs/AutoTestProjectSettingsApiModel.md)
 - [AutoTestProjectSettingsApiModelWorkItemUpdatingFields](docs/AutoTestProjectSettingsApiModelWorkItemUpdatingFields.md)
 - [AutoTestProjectSettingsApiResult](docs/AutoTestProjectSettingsApiResult.md)
 - [AutoTestProjectSettingsApiResultWorkItemUpdatingFields](docs/AutoTestProjectSettingsApiResultWorkItemUpdatingFields.md)
 - [AutoTestRelatedToTestResult](docs/AutoTestRelatedToTestResult.md)
 - [AutoTestResultHistoryApiResult](docs/AutoTestResultHistoryApiResult.md)
 - [AutoTestResultHistoryApiResultStatus](docs/AutoTestResultHistoryApiResultStatus.md)
 - [AutoTestResultHistorySelectApiModel](docs/AutoTestResultHistorySelectApiModel.md)
 - [AutoTestResultReasonShort](docs/AutoTestResultReasonShort.md)
 - [AutoTestResultReasonsCountItemModel](docs/AutoTestResultReasonsCountItemModel.md)
 - [AutoTestResultReasonsCountModel](docs/AutoTestResultReasonsCountModel.md)
 - [AutoTestResultsForTestRunModel](docs/AutoTestResultsForTestRunModel.md)
 - [AutoTestSearchApiModel](docs/AutoTestSearchApiModel.md)
 - [AutoTestSearchApiModelFilter](docs/AutoTestSearchApiModelFilter.md)
 - [AutoTestSearchApiModelIncludes](docs/AutoTestSearchApiModelIncludes.md)
 - [AutoTestSearchIncludeApiModel](docs/AutoTestSearchIncludeApiModel.md)
 - [AutoTestSelectApiModel](docs/AutoTestSelectApiModel.md)
 - [AutoTestSelectModel](docs/AutoTestSelectModel.md)
 - [AutoTestSelectModelFilter](docs/AutoTestSelectModelFilter.md)
 - [AutoTestShortApiResult](docs/AutoTestShortApiResult.md)
 - [AutoTestStep](docs/AutoTestStep.md)
 - [AutoTestStepApiModel](docs/AutoTestStepApiModel.md)
 - [AutoTestStepApiResult](docs/AutoTestStepApiResult.md)
 - [AutoTestStepModel](docs/AutoTestStepModel.md)
 - [AutoTestStepResult](docs/AutoTestStepResult.md)
 - [AutoTestStepResultUpdateRequest](docs/AutoTestStepResultUpdateRequest.md)
 - [AutoTestStepResultsApiResult](docs/AutoTestStepResultsApiResult.md)
 - [AutoTestUpdateApiModel](docs/AutoTestUpdateApiModel.md)
 - [AutoTestWorkItemIdentifierApiResult](docs/AutoTestWorkItemIdentifierApiResult.md)
 - [AutoTestsExtractionModel](docs/AutoTestsExtractionModel.md)
 - [AutotestResultOutcome](docs/AutotestResultOutcome.md)
 - [AutotestResultReasonFilterModel](docs/AutotestResultReasonFilterModel.md)
 - [AutotestResultReasonShortGetModel](docs/AutotestResultReasonShortGetModel.md)
 - [AvailableFailureCategory](docs/AvailableFailureCategory.md)
 - [AvailableTestResultOutcome](docs/AvailableTestResultOutcome.md)
 - [BackgroundJobAttachmentModel](docs/BackgroundJobAttachmentModel.md)
 - [BackgroundJobFilterModel](docs/BackgroundJobFilterModel.md)
 - [BackgroundJobGetModel](docs/BackgroundJobGetModel.md)
 - [BackgroundJobState](docs/BackgroundJobState.md)
 - [BackgroundJobType](docs/BackgroundJobType.md)
 - [BooleanChangedFieldViewModel](docs/BooleanChangedFieldViewModel.md)
 - [BooleanNullableChangedFieldViewModel](docs/BooleanNullableChangedFieldViewModel.md)
 - [CollectionFilter](docs/CollectionFilter.md)
 - [CollectionFilterFilter](docs/CollectionFilterFilter.md)
 - [CollectionOperator](docs/CollectionOperator.md)
 - [CompositeFilter](docs/CompositeFilter.md)
 - [ConfigurationByParametersModel](docs/ConfigurationByParametersModel.md)
 - [ConfigurationExtractionApiModel](docs/ConfigurationExtractionApiModel.md)
 - [ConfigurationExtractionApiModelIds](docs/ConfigurationExtractionApiModelIds.md)
 - [ConfigurationExtractionApiModelProjectIds](docs/ConfigurationExtractionApiModelProjectIds.md)
 - [ConfigurationExtractionModel](docs/ConfigurationExtractionModel.md)
 - [ConfigurationFilterApiModel](docs/ConfigurationFilterApiModel.md)
 - [ConfigurationFilterModel](docs/ConfigurationFilterModel.md)
 - [ConfigurationModel](docs/ConfigurationModel.md)
 - [ConfigurationPostModel](docs/ConfigurationPostModel.md)
 - [ConfigurationPutModel](docs/ConfigurationPutModel.md)
 - [ConfigurationSelectApiModel](docs/ConfigurationSelectApiModel.md)
 - [ConfigurationSelectApiModelExtractionModel](docs/ConfigurationSelectApiModelExtractionModel.md)
 - [ConfigurationSelectApiModelFilter](docs/ConfigurationSelectApiModelFilter.md)
 - [ConfigurationSelectModel](docs/ConfigurationSelectModel.md)
 - [ConfigurationSelectModelExtractionModel](docs/ConfigurationSelectModelExtractionModel.md)
 - [ConfigurationSelectModelFilter](docs/ConfigurationSelectModelFilter.md)
 - [ConfigurationShort](docs/ConfigurationShort.md)
 - [ConfigurationShortApiResult](docs/ConfigurationShortApiResult.md)
 - [ConfigurationShortModel](docs/ConfigurationShortModel.md)
 - [CreateAndFillByAutoTestsRequest](docs/CreateAndFillByAutoTestsRequest.md)
 - [CreateAndFillByConfigurationsRequest](docs/CreateAndFillByConfigurationsRequest.md)
 - [CreateAndFillByWorkItemsRequest](docs/CreateAndFillByWorkItemsRequest.md)
 - [CreateAutoTestRequest](docs/CreateAutoTestRequest.md)
 - [CreateConfigurationRequest](docs/CreateConfigurationRequest.md)
 - [CreateDefectApiModel](docs/CreateDefectApiModel.md)
 - [CreateDefectApiModelForm](docs/CreateDefectApiModelForm.md)
 - [CreateEmptyRequest](docs/CreateEmptyRequest.md)
 - [CreateEmptyTestRunApiModel](docs/CreateEmptyTestRunApiModel.md)
 - [CreateFailureCategoryApiModel](docs/CreateFailureCategoryApiModel.md)
 - [CreateFailureClassRegexApiModel](docs/CreateFailureClassRegexApiModel.md)
 - [CreateLinkApiModel](docs/CreateLinkApiModel.md)
 - [CreateParameterApiModel](docs/CreateParameterApiModel.md)
 - [CreateParameterRequest](docs/CreateParameterRequest.md)
 - [CreateProjectApiModel](docs/CreateProjectApiModel.md)
 - [CreateProjectFailureCategoryApiModel](docs/CreateProjectFailureCategoryApiModel.md)
 - [CreateProjectRequest](docs/CreateProjectRequest.md)
 - [CreateProjectsAttributeRequest](docs/CreateProjectsAttributeRequest.md)
 - [CreateSectionRequest](docs/CreateSectionRequest.md)
 - [CreateStepApiModel](docs/CreateStepApiModel.md)
 - [CreateTagApiModel](docs/CreateTagApiModel.md)
 - [CreateTestPlanApiModel](docs/CreateTestPlanApiModel.md)
 - [CreateTestPlanRequest](docs/CreateTestPlanRequest.md)
 - [CreateTestRunAndFillByAutoTestsApiModel](docs/CreateTestRunAndFillByAutoTestsApiModel.md)
 - [CreateTestRunAndFillByConfigurationsApiModel](docs/CreateTestRunAndFillByConfigurationsApiModel.md)
 - [CreateTestRunAndFillByWorkItemsApiModel](docs/CreateTestRunAndFillByWorkItemsApiModel.md)
 - [CreateTestStatusApiModel](docs/CreateTestStatusApiModel.md)
 - [CreateWorkItemApiModel](docs/CreateWorkItemApiModel.md)
 - [CreateWorkItemCommentApiModel](docs/CreateWorkItemCommentApiModel.md)
 - [CreateWorkItemPreviewsApiModel](docs/CreateWorkItemPreviewsApiModel.md)
 - [CreateWorkflowApiModel](docs/CreateWorkflowApiModel.md)
 - [CustomAttributeApiResult](docs/CustomAttributeApiResult.md)
 - [CustomAttributeChangeModel](docs/CustomAttributeChangeModel.md)
 - [CustomAttributeGetModel](docs/CustomAttributeGetModel.md)
 - [CustomAttributeModel](docs/CustomAttributeModel.md)
 - [CustomAttributeOptionApiResult](docs/CustomAttributeOptionApiResult.md)
 - [CustomAttributeOptionModel](docs/CustomAttributeOptionModel.md)
 - [CustomAttributeOptionPostModel](docs/CustomAttributeOptionPostModel.md)
 - [CustomAttributePostModel](docs/CustomAttributePostModel.md)
 - [CustomAttributePutModel](docs/CustomAttributePutModel.md)
 - [CustomAttributeSearchQueryModel](docs/CustomAttributeSearchQueryModel.md)
 - [CustomAttributeSearchResponseModel](docs/CustomAttributeSearchResponseModel.md)
 - [CustomAttributeTemplateModel](docs/CustomAttributeTemplateModel.md)
 - [CustomAttributeTemplatePostModel](docs/CustomAttributeTemplatePostModel.md)
 - [CustomAttributeTemplatePutModel](docs/CustomAttributeTemplatePutModel.md)
 - [CustomAttributeTemplateSearchQueryModel](docs/CustomAttributeTemplateSearchQueryModel.md)
 - [CustomAttributeTemplateValidationResult](docs/CustomAttributeTemplateValidationResult.md)
 - [CustomAttributeTestPlanProjectRelationPutModel](docs/CustomAttributeTestPlanProjectRelationPutModel.md)
 - [CustomAttributeType](docs/CustomAttributeType.md)
 - [CustomAttributeTypesEnum](docs/CustomAttributeTypesEnum.md)
 - [CustomAttributeValidationResult](docs/CustomAttributeValidationResult.md)
 - [DateTimeRangeSelectorModel](docs/DateTimeRangeSelectorModel.md)
 - [DefectApiModel](docs/DefectApiModel.md)
 - [DeletionState](docs/DeletionState.md)
 - [DemoProjectApiResult](docs/DemoProjectApiResult.md)
 - [EnableProjectExternalServiceApiModel](docs/EnableProjectExternalServiceApiModel.md)
 - [ExternalFormAllowedValueModel](docs/ExternalFormAllowedValueModel.md)
 - [ExternalFormCreateModel](docs/ExternalFormCreateModel.md)
 - [ExternalFormFieldModel](docs/ExternalFormFieldModel.md)
 - [ExternalFormLinkModel](docs/ExternalFormLinkModel.md)
 - [ExternalFormModel](docs/ExternalFormModel.md)
 - [ExternalIssueApiField](docs/ExternalIssueApiField.md)
 - [ExternalIssueApiFieldSuggestion](docs/ExternalIssueApiFieldSuggestion.md)
 - [ExternalIssueApiFieldSuggestionExternalService](docs/ExternalIssueApiFieldSuggestionExternalService.md)
 - [ExternalIssueApiFieldSuggestionReply](docs/ExternalIssueApiFieldSuggestionReply.md)
 - [ExternalIssueApiMetadata](docs/ExternalIssueApiMetadata.md)
 - [ExternalIssueApiMetadataPriority](docs/ExternalIssueApiMetadataPriority.md)
 - [ExternalIssueApiMetadataType](docs/ExternalIssueApiMetadataType.md)
 - [ExternalIssueApiPriority](docs/ExternalIssueApiPriority.md)
 - [ExternalIssueApiResult](docs/ExternalIssueApiResult.md)
 - [ExternalIssueApiResultMetadata](docs/ExternalIssueApiResultMetadata.md)
 - [ExternalIssueApiType](docs/ExternalIssueApiType.md)
 - [ExternalIssueExternalServiceApiResult](docs/ExternalIssueExternalServiceApiResult.md)
 - [ExternalIssueMetadataModel](docs/ExternalIssueMetadataModel.md)
 - [ExternalIssueModel](docs/ExternalIssueModel.md)
 - [ExternalIssueModelMetadata](docs/ExternalIssueModelMetadata.md)
 - [ExternalIssuePriorityModel](docs/ExternalIssuePriorityModel.md)
 - [ExternalIssueTypeModel](docs/ExternalIssueTypeModel.md)
 - [ExternalLinkModel](docs/ExternalLinkModel.md)
 - [ExternalServiceMetadataApiResult](docs/ExternalServiceMetadataApiResult.md)
 - [ExternalServicesMetadataApiResult](docs/ExternalServicesMetadataApiResult.md)
 - [FailureCategory](docs/FailureCategory.md)
 - [FailureCategoryApiResult](docs/FailureCategoryApiResult.md)
 - [FailureCategoryGroupApiModel](docs/FailureCategoryGroupApiModel.md)
 - [FailureCategoryGroupApiResult](docs/FailureCategoryGroupApiResult.md)
 - [FailureCategoryGroupItemApiResult](docs/FailureCategoryGroupItemApiResult.md)
 - [FailureCategoryGroupItemApiResultGroup](docs/FailureCategoryGroupItemApiResultGroup.md)
 - [FailureCategoryGroupItemApiResultReply](docs/FailureCategoryGroupItemApiResultReply.md)
 - [FailureCategoryGroupSearchApiModel](docs/FailureCategoryGroupSearchApiModel.md)
 - [FailureCategoryGroupSearchApiModelGroup](docs/FailureCategoryGroupSearchApiModelGroup.md)
 - [FailureCategoryGroupSearchApiModelInquiry](docs/FailureCategoryGroupSearchApiModelInquiry.md)
 - [FailureCategoryItemApiResult](docs/FailureCategoryItemApiResult.md)
 - [FailureCategoryModel](docs/FailureCategoryModel.md)
 - [FailureClassRegexApiResult](docs/FailureClassRegexApiResult.md)
 - [Filter](docs/Filter.md)
 - [FilterModel](docs/FilterModel.md)
 - [FilterOperator](docs/FilterOperator.md)
 - [GenerateWorkItemPreviewsApiModel](docs/GenerateWorkItemPreviewsApiModel.md)
 - [GenerateWorkItemPreviewsApiResult](docs/GenerateWorkItemPreviewsApiResult.md)
 - [GetAIServiceModelsApiModel](docs/GetAIServiceModelsApiModel.md)
 - [GetExternalFormApiResult](docs/GetExternalFormApiResult.md)
 - [GetExternalFormApiResultForm](docs/GetExternalFormApiResultForm.md)
 - [GetExternalIssueSuggestionsApiModel](docs/GetExternalIssueSuggestionsApiModel.md)
 - [GetExternalIssueSuggestionsApiModelInquiry](docs/GetExternalIssueSuggestionsApiModelInquiry.md)
 - [GetShortProjectsApiModel](docs/GetShortProjectsApiModel.md)
 - [GetXlsxTestPointsByTestPlanModel](docs/GetXlsxTestPointsByTestPlanModel.md)
 - [GlobalCustomAttributePostModel](docs/GlobalCustomAttributePostModel.md)
 - [GlobalCustomAttributeUpdateModel](docs/GlobalCustomAttributeUpdateModel.md)
 - [GlobalSearchItemResult](docs/GlobalSearchItemResult.md)
 - [GlobalSearchRequest](docs/GlobalSearchRequest.md)
 - [GlobalSearchResponse](docs/GlobalSearchResponse.md)
 - [GuidChangedFieldViewModel](docs/GuidChangedFieldViewModel.md)
 - [GuidExtractionModel](docs/GuidExtractionModel.md)
 - [IFilter](docs/IFilter.md)
 - [ImageResizeType](docs/ImageResizeType.md)
 - [Inquiry](docs/Inquiry.md)
 - [Int32ChangedFieldViewModel](docs/Int32ChangedFieldViewModel.md)
 - [Int32RangeSelectorModel](docs/Int32RangeSelectorModel.md)
 - [Int64ChangedFieldViewModel](docs/Int64ChangedFieldViewModel.md)
 - [Int64RangeSelectorModel](docs/Int64RangeSelectorModel.md)
 - [IterationApiResult](docs/IterationApiResult.md)
 - [IterationModel](docs/IterationModel.md)
 - [Label](docs/Label.md)
 - [LabelApiModel](docs/LabelApiModel.md)
 - [LabelApiResult](docs/LabelApiResult.md)
 - [LabelShortModel](docs/LabelShortModel.md)
 - [LastTestResultApiResult](docs/LastTestResultApiResult.md)
 - [LastTestResultModel](docs/LastTestResultModel.md)
 - [Link](docs/Link.md)
 - [LinkApiResult](docs/LinkApiResult.md)
 - [LinkAutoTestToWorkItemRequest](docs/LinkAutoTestToWorkItemRequest.md)
 - [LinkCreateApiModel](docs/LinkCreateApiModel.md)
 - [LinkModel](docs/LinkModel.md)
 - [LinkPostModel](docs/LinkPostModel.md)
 - [LinkPutModel](docs/LinkPutModel.md)
 - [LinkShort](docs/LinkShort.md)
 - [LinkShortApiResult](docs/LinkShortApiResult.md)
 - [LinkShortModel](docs/LinkShortModel.md)
 - [LinkType](docs/LinkType.md)
 - [LinkUpdateApiModel](docs/LinkUpdateApiModel.md)
 - [ListSortDirection](docs/ListSortDirection.md)
 - [LogicalOperator](docs/LogicalOperator.md)
 - [ManualRerunApiResult](docs/ManualRerunApiResult.md)
 - [ManualRerunSelectTestResultsApiModel](docs/ManualRerunSelectTestResultsApiModel.md)
 - [ManualRerunSelectTestResultsApiModelExtractionModel](docs/ManualRerunSelectTestResultsApiModelExtractionModel.md)
 - [ManualRerunSelectTestResultsApiModelFilter](docs/ManualRerunSelectTestResultsApiModelFilter.md)
 - [ManualRerunTestResultApiModel](docs/ManualRerunTestResultApiModel.md)
 - [ManualRerunTestResultApiModelTestResultIds](docs/ManualRerunTestResultApiModelTestResultIds.md)
 - [MoveRequest](docs/MoveRequest.md)
 - [NamedEntityApiModel](docs/NamedEntityApiModel.md)
 - [NotificationModel](docs/NotificationModel.md)
 - [NotificationQueryFilterModel](docs/NotificationQueryFilterModel.md)
 - [NotificationTypeModel](docs/NotificationTypeModel.md)
 - [Operation](docs/Operation.md)
 - [Order](docs/Order.md)
 - [Page](docs/Page.md)
 - [ParameterApiResult](docs/ParameterApiResult.md)
 - [ParameterGroupApiResult](docs/ParameterGroupApiResult.md)
 - [ParameterGroupsFilterApiModel](docs/ParameterGroupsFilterApiModel.md)
 - [ParameterIterationModel](docs/ParameterIterationModel.md)
 - [ParameterShortApiResult](docs/ParameterShortApiResult.md)
 - [ParameterShortModel](docs/ParameterShortModel.md)
 - [ParametersFilterApiModel](docs/ParametersFilterApiModel.md)
 - [PeriodViewModel](docs/PeriodViewModel.md)
 - [PeriodViewModelChangedFieldViewModel](docs/PeriodViewModelChangedFieldViewModel.md)
 - [PreviewsIssueLinkApiModel](docs/PreviewsIssueLinkApiModel.md)
 - [PreviewsIssueLinkApiResult](docs/PreviewsIssueLinkApiResult.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [ProjectApiResult](docs/ProjectApiResult.md)
 - [ProjectAttributesFilterModel](docs/ProjectAttributesFilterModel.md)
 - [ProjectCustomAttributeTemplateGetModel](docs/ProjectCustomAttributeTemplateGetModel.md)
 - [ProjectCustomAttributesTemplatesFilterModel](docs/ProjectCustomAttributesTemplatesFilterModel.md)
 - [ProjectDetailedFailureCategoryApiResult](docs/ProjectDetailedFailureCategoryApiResult.md)
 - [ProjectExternalServiceApiResult](docs/ProjectExternalServiceApiResult.md)
 - [ProjectExternalServiceApiResultMetadata](docs/ProjectExternalServiceApiResultMetadata.md)
 - [ProjectExternalServiceSettingsApiResult](docs/ProjectExternalServiceSettingsApiResult.md)
 - [ProjectExternalServicesApiResult](docs/ProjectExternalServicesApiResult.md)
 - [ProjectExtractionModel](docs/ProjectExtractionModel.md)
 - [ProjectFailureCategoryApiResult](docs/ProjectFailureCategoryApiResult.md)
 - [ProjectFailureCategoryGroupItemApiResult](docs/ProjectFailureCategoryGroupItemApiResult.md)
 - [ProjectFailureCategoryGroupItemApiResultReply](docs/ProjectFailureCategoryGroupItemApiResultReply.md)
 - [ProjectModel](docs/ProjectModel.md)
 - [ProjectNameApiResult](docs/ProjectNameApiResult.md)
 - [ProjectSelectModel](docs/ProjectSelectModel.md)
 - [ProjectShortApiResult](docs/ProjectShortApiResult.md)
 - [ProjectShortApiResultReply](docs/ProjectShortApiResultReply.md)
 - [ProjectShortModel](docs/ProjectShortModel.md)
 - [ProjectShortestModel](docs/ProjectShortestModel.md)
 - [ProjectTestPlansFilterModel](docs/ProjectTestPlansFilterModel.md)
 - [ProjectType](docs/ProjectType.md)
 - [ProjectTypeModel](docs/ProjectTypeModel.md)
 - [ProjectsFilterModel](docs/ProjectsFilterModel.md)
 - [ProjectsFilterModelAutotestsCount](docs/ProjectsFilterModelAutotestsCount.md)
 - [ProjectsFilterModelChecklistsCount](docs/ProjectsFilterModelChecklistsCount.md)
 - [ProjectsFilterModelCreatedDate](docs/ProjectsFilterModelCreatedDate.md)
 - [ProjectsFilterModelSharedStepsCount](docs/ProjectsFilterModelSharedStepsCount.md)
 - [ProjectsFilterModelTestCasesCount](docs/ProjectsFilterModelTestCasesCount.md)
 - [RenameRequest](docs/RenameRequest.md)
 - [ReplaceProjectExternalServiceApiModel](docs/ReplaceProjectExternalServiceApiModel.md)
 - [RequestType](docs/RequestType.md)
 - [RequestTypeApiModel](docs/RequestTypeApiModel.md)
 - [RequestTypeModel](docs/RequestTypeModel.md)
 - [RerunTestResultApiResult](docs/RerunTestResultApiResult.md)
 - [RerunsApiResult](docs/RerunsApiResult.md)
 - [SearchAttributesInProjectRequest](docs/SearchAttributesInProjectRequest.md)
 - [SearchCustomAttributeTemplateGetModel](docs/SearchCustomAttributeTemplateGetModel.md)
 - [SearchExternalIssuesApiModel](docs/SearchExternalIssuesApiModel.md)
 - [SearchTestRunsApiModel](docs/SearchTestRunsApiModel.md)
 - [SearchTestStatusesApiModel](docs/SearchTestStatusesApiModel.md)
 - [SearchWebhooksQueryModel](docs/SearchWebhooksQueryModel.md)
 - [SearchWorkItemLinkUrlsApiResult](docs/SearchWorkItemLinkUrlsApiResult.md)
 - [SearchWorkItemsRequest](docs/SearchWorkItemsRequest.md)
 - [SearchWorkflowProjectsApiModel](docs/SearchWorkflowProjectsApiModel.md)
 - [SearchWorkflowsApiModel](docs/SearchWorkflowsApiModel.md)
 - [SectionModel](docs/SectionModel.md)
 - [SectionMoveModel](docs/SectionMoveModel.md)
 - [SectionPostModel](docs/SectionPostModel.md)
 - [SectionPutModel](docs/SectionPutModel.md)
 - [SectionRenameModel](docs/SectionRenameModel.md)
 - [SectionSharedStep](docs/SectionSharedStep.md)
 - [SectionWithStepsModel](docs/SectionWithStepsModel.md)
 - [SelectTagsApiModel](docs/SelectTagsApiModel.md)
 - [SelectTagsApiModelExtractionModel](docs/SelectTagsApiModelExtractionModel.md)
 - [SelectTagsApiModelFilter](docs/SelectTagsApiModelFilter.md)
 - [SharedStepChangeViewModel](docs/SharedStepChangeViewModel.md)
 - [SharedStepModel](docs/SharedStepModel.md)
 - [SharedStepReferenceModel](docs/SharedStepReferenceModel.md)
 - [SharedStepReferenceSectionModel](docs/SharedStepReferenceSectionModel.md)
 - [SharedStepReferenceSectionsQueryFilterModel](docs/SharedStepReferenceSectionsQueryFilterModel.md)
 - [SharedStepReferenceSectionsQueryFilterModelCreatedDate](docs/SharedStepReferenceSectionsQueryFilterModelCreatedDate.md)
 - [SharedStepReferenceSectionsQueryFilterModelModifiedDate](docs/SharedStepReferenceSectionsQueryFilterModelModifiedDate.md)
 - [SharedStepReferencesQueryFilterModel](docs/SharedStepReferencesQueryFilterModel.md)
 - [SharedStepResultApiModel](docs/SharedStepResultApiModel.md)
 - [ShortConfiguration](docs/ShortConfiguration.md)
 - [StepCommentApiModel](docs/StepCommentApiModel.md)
 - [StepModel](docs/StepModel.md)
 - [StepPostModel](docs/StepPostModel.md)
 - [StepPutModel](docs/StepPutModel.md)
 - [StepResultApiModel](docs/StepResultApiModel.md)
 - [StringArrayChangedFieldViewModel](docs/StringArrayChangedFieldViewModel.md)
 - [StringChangedFieldViewModel](docs/StringChangedFieldViewModel.md)
 - [StringChangedFieldWithDiffsViewModel](docs/StringChangedFieldWithDiffsViewModel.md)
 - [StringExtractionModel](docs/StringExtractionModel.md)
 - [TagApiModel](docs/TagApiModel.md)
 - [TagApiResult](docs/TagApiResult.md)
 - [TagModel](docs/TagModel.md)
 - [TagShortApiResult](docs/TagShortApiResult.md)
 - [TagsExtractionApiModel](docs/TagsExtractionApiModel.md)
 - [TagsExtractionApiModelIds](docs/TagsExtractionApiModelIds.md)
 - [TagsFilterApiModel](docs/TagsFilterApiModel.md)
 - [TagsFilterApiModelCreatedDate](docs/TagsFilterApiModelCreatedDate.md)
 - [TestPlanApiResult](docs/TestPlanApiResult.md)
 - [TestPlanChangeModel](docs/TestPlanChangeModel.md)
 - [TestPlanChangeModelTestPlanChangedFields](docs/TestPlanChangeModelTestPlanChangedFields.md)
 - [TestPlanChangedFieldsViewModel](docs/TestPlanChangedFieldsViewModel.md)
 - [TestPlanExtractionModel](docs/TestPlanExtractionModel.md)
 - [TestPlanGroupByStatus](docs/TestPlanGroupByStatus.md)
 - [TestPlanGroupByStatusCode](docs/TestPlanGroupByStatusCode.md)
 - [TestPlanGroupByStatusType](docs/TestPlanGroupByStatusType.md)
 - [TestPlanGroupByTester](docs/TestPlanGroupByTester.md)
 - [TestPlanGroupByTesterAndStatus](docs/TestPlanGroupByTesterAndStatus.md)
 - [TestPlanGroupByTesterAndStatusCode](docs/TestPlanGroupByTesterAndStatusCode.md)
 - [TestPlanLink](docs/TestPlanLink.md)
 - [TestPlanModel](docs/TestPlanModel.md)
 - [TestPlanSelectModel](docs/TestPlanSelectModel.md)
 - [TestPlanShortModel](docs/TestPlanShortModel.md)
 - [TestPlanStatus](docs/TestPlanStatus.md)
 - [TestPlanStatusModel](docs/TestPlanStatusModel.md)
 - [TestPlanSummaryModel](docs/TestPlanSummaryModel.md)
 - [TestPlanTagApiResult](docs/TestPlanTagApiResult.md)
 - [TestPlanTestPointsAnalyticsApiModel](docs/TestPlanTestPointsAnalyticsApiModel.md)
 - [TestPlanTestPointsAnalyticsApiResult](docs/TestPlanTestPointsAnalyticsApiResult.md)
 - [TestPlanTestPointsApiModel](docs/TestPlanTestPointsApiModel.md)
 - [TestPlanTestPointsAutoTestsRerunApiModel](docs/TestPlanTestPointsAutoTestsRerunApiModel.md)
 - [TestPlanTestPointsAutoTestsRerunApiModelExtractionModel](docs/TestPlanTestPointsAutoTestsRerunApiModelExtractionModel.md)
 - [TestPlanTestPointsAutoTestsRerunApiModelFilter](docs/TestPlanTestPointsAutoTestsRerunApiModelFilter.md)
 - [TestPlanTestPointsAutoTestsRunApiModel](docs/TestPlanTestPointsAutoTestsRunApiModel.md)
 - [TestPlanTestPointsExtractionApiModel](docs/TestPlanTestPointsExtractionApiModel.md)
 - [TestPlanTestPointsExtractionApiModelIds](docs/TestPlanTestPointsExtractionApiModelIds.md)
 - [TestPlanTestPointsGroupApiModel](docs/TestPlanTestPointsGroupApiModel.md)
 - [TestPlanTestPointsGroupApiResult](docs/TestPlanTestPointsGroupApiResult.md)
 - [TestPlanTestPointsGroupSearchApiResult](docs/TestPlanTestPointsGroupSearchApiResult.md)
 - [TestPlanTestPointsGroupSearchApiResultStatusCounters](docs/TestPlanTestPointsGroupSearchApiResultStatusCounters.md)
 - [TestPlanTestPointsGroupSearchItemApiResult](docs/TestPlanTestPointsGroupSearchItemApiResult.md)
 - [TestPlanTestPointsInquiryApiModel](docs/TestPlanTestPointsInquiryApiModel.md)
 - [TestPlanTestPointsSearchApiModel](docs/TestPlanTestPointsSearchApiModel.md)
 - [TestPlanTestPointsSearchApiModelCreatedDate](docs/TestPlanTestPointsSearchApiModelCreatedDate.md)
 - [TestPlanTestPointsSearchApiModelDuration](docs/TestPlanTestPointsSearchApiModelDuration.md)
 - [TestPlanTestPointsSearchApiModelModifiedDate](docs/TestPlanTestPointsSearchApiModelModifiedDate.md)
 - [TestPlanTestPointsSearchApiModelWorkItemCreatedDate](docs/TestPlanTestPointsSearchApiModelWorkItemCreatedDate.md)
 - [TestPlanTestPointsSearchApiModelWorkItemMedianDuration](docs/TestPlanTestPointsSearchApiModelWorkItemMedianDuration.md)
 - [TestPlanTestPointsSearchApiModelWorkItemModifiedDate](docs/TestPlanTestPointsSearchApiModelWorkItemModifiedDate.md)
 - [TestPlanTestPointsSearchApiResult](docs/TestPlanTestPointsSearchApiResult.md)
 - [TestPlanTestPointsSearchApiResultConfiguration](docs/TestPlanTestPointsSearchApiResultConfiguration.md)
 - [TestPlanTestPointsSearchApiResultCreated](docs/TestPlanTestPointsSearchApiResultCreated.md)
 - [TestPlanTestPointsSearchApiResultStatusModel](docs/TestPlanTestPointsSearchApiResultStatusModel.md)
 - [TestPlanTestPointsSearchApiResultTestSuite](docs/TestPlanTestPointsSearchApiResultTestSuite.md)
 - [TestPlanTestPointsSearchApiResultWorkItem](docs/TestPlanTestPointsSearchApiResultWorkItem.md)
 - [TestPlanTestPointsSearchStatusCountersApiResult](docs/TestPlanTestPointsSearchStatusCountersApiResult.md)
 - [TestPlanTestPointsSectionSearchApiResult](docs/TestPlanTestPointsSectionSearchApiResult.md)
 - [TestPlanTestPointsSetTestersApiModel](docs/TestPlanTestPointsSetTestersApiModel.md)
 - [TestPlanTestPointsStatusCodeGroupApiResult](docs/TestPlanTestPointsStatusCodeGroupApiResult.md)
 - [TestPlanTestPointsStatusGroupApiResult](docs/TestPlanTestPointsStatusGroupApiResult.md)
 - [TestPlanTestPointsStatusTypeGroupApiResult](docs/TestPlanTestPointsStatusTypeGroupApiResult.md)
 - [TestPlanTestPointsTestSuiteSearchApiResult](docs/TestPlanTestPointsTestSuiteSearchApiResult.md)
 - [TestPlanTestPointsTesterAndStatusGroupApiResult](docs/TestPlanTestPointsTesterAndStatusGroupApiResult.md)
 - [TestPlanTestPointsTesterAndStatusTypeGroupApiResult](docs/TestPlanTestPointsTesterAndStatusTypeGroupApiResult.md)
 - [TestPlanTestPointsTesterGroupApiResult](docs/TestPlanTestPointsTesterGroupApiResult.md)
 - [TestPlanTestPointsWorkItemSearchApiResult](docs/TestPlanTestPointsWorkItemSearchApiResult.md)
 - [TestPlanTestPointsWorkItemSearchApiResultSection](docs/TestPlanTestPointsWorkItemSearchApiResultSection.md)
 - [TestPlanWithAnalyticModel](docs/TestPlanWithAnalyticModel.md)
 - [TestPlanWithAnalyticModelAnalytic](docs/TestPlanWithAnalyticModelAnalytic.md)
 - [TestPlanWithTestSuiteTreeModel](docs/TestPlanWithTestSuiteTreeModel.md)
 - [TestPoint](docs/TestPoint.md)
 - [TestPointAnalyticResult](docs/TestPointAnalyticResult.md)
 - [TestPointByTestSuiteModel](docs/TestPointByTestSuiteModel.md)
 - [TestPointChangeViewModel](docs/TestPointChangeViewModel.md)
 - [TestPointChangeViewModelChangedFieldViewModel](docs/TestPointChangeViewModelChangedFieldViewModel.md)
 - [TestPointFilterModel](docs/TestPointFilterModel.md)
 - [TestPointFilterRequestModel](docs/TestPointFilterRequestModel.md)
 - [TestPointRelatedToTestResult](docs/TestPointRelatedToTestResult.md)
 - [TestPointResultApiResult](docs/TestPointResultApiResult.md)
 - [TestPointSelectModel](docs/TestPointSelectModel.md)
 - [TestPointSelector](docs/TestPointSelector.md)
 - [TestPointShortApiResult](docs/TestPointShortApiResult.md)
 - [TestPointShortApiResultStatusModel](docs/TestPointShortApiResultStatusModel.md)
 - [TestPointShortModel](docs/TestPointShortModel.md)
 - [TestPointShortResponseModel](docs/TestPointShortResponseModel.md)
 - [TestPointShortResponseModelLastTestResult](docs/TestPointShortResponseModelLastTestResult.md)
 - [TestPointShortResponseModelStatusModel](docs/TestPointShortResponseModelStatusModel.md)
 - [TestPointStatus](docs/TestPointStatus.md)
 - [TestPointWithLastResultResponseModel](docs/TestPointWithLastResultResponseModel.md)
 - [TestPointsExtractionModel](docs/TestPointsExtractionModel.md)
 - [TestResultApiResult](docs/TestResultApiResult.md)
 - [TestResultChangeViewModel](docs/TestResultChangeViewModel.md)
 - [TestResultChangeViewModelChangedFieldViewModel](docs/TestResultChangeViewModelChangedFieldViewModel.md)
 - [TestResultChronologyModel](docs/TestResultChronologyModel.md)
 - [TestResultConfiguration](docs/TestResultConfiguration.md)
 - [TestResultFailureClassApiResult](docs/TestResultFailureClassApiResult.md)
 - [TestResultHistoryReportApiResult](docs/TestResultHistoryReportApiResult.md)
 - [TestResultHistoryReportApiResultStatus](docs/TestResultHistoryReportApiResultStatus.md)
 - [TestResultOutcome](docs/TestResultOutcome.md)
 - [TestResultResponse](docs/TestResultResponse.md)
 - [TestResultShortApiResult](docs/TestResultShortApiResult.md)
 - [TestResultShortResponse](docs/TestResultShortResponse.md)
 - [TestResultStepCommentUpdateRequest](docs/TestResultStepCommentUpdateRequest.md)
 - [TestResultUpdateV2Request](docs/TestResultUpdateV2Request.md)
 - [TestResultV2GetModel](docs/TestResultV2GetModel.md)
 - [TestResultV2ShortModel](docs/TestResultV2ShortModel.md)
 - [TestResultsExtractionApiModel](docs/TestResultsExtractionApiModel.md)
 - [TestResultsFilterApiModel](docs/TestResultsFilterApiModel.md)
 - [TestResultsFilterApiModelCompletedOn](docs/TestResultsFilterApiModelCompletedOn.md)
 - [TestResultsFilterApiModelCreatedDate](docs/TestResultsFilterApiModelCreatedDate.md)
 - [TestResultsFilterApiModelDuration](docs/TestResultsFilterApiModelDuration.md)
 - [TestResultsFilterApiModelModifiedDate](docs/TestResultsFilterApiModelModifiedDate.md)
 - [TestResultsFilterApiModelStartedOn](docs/TestResultsFilterApiModelStartedOn.md)
 - [TestResultsLocalFilterModel](docs/TestResultsLocalFilterModel.md)
 - [TestResultsSelectApiModel](docs/TestResultsSelectApiModel.md)
 - [TestResultsSelectApiModelExtractionModel](docs/TestResultsSelectApiModelExtractionModel.md)
 - [TestResultsSelectApiModelFilter](docs/TestResultsSelectApiModelFilter.md)
 - [TestResultsStatisticsApiResult](docs/TestResultsStatisticsApiResult.md)
 - [TestResultsStatisticsApiResultFailureCategories](docs/TestResultsStatisticsApiResultFailureCategories.md)
 - [TestResultsStatisticsApiResultStatuses](docs/TestResultsStatisticsApiResultStatuses.md)
 - [TestResultsStatisticsFailureCategoriesApiResult](docs/TestResultsStatisticsFailureCategoriesApiResult.md)
 - [TestResultsStatisticsStatusesApiResult](docs/TestResultsStatisticsStatusesApiResult.md)
 - [TestRunAnalyticApiResult](docs/TestRunAnalyticApiResult.md)
 - [TestRunApiResult](docs/TestRunApiResult.md)
 - [TestRunApiResultAnalytic](docs/TestRunApiResultAnalytic.md)
 - [TestRunByAutoTestApiResult](docs/TestRunByAutoTestApiResult.md)
 - [TestRunByAutoTestApiResultStatus](docs/TestRunByAutoTestApiResultStatus.md)
 - [TestRunExtractionApiModel](docs/TestRunExtractionApiModel.md)
 - [TestRunExtractionApiModelIds](docs/TestRunExtractionApiModelIds.md)
 - [TestRunFilterApiModel](docs/TestRunFilterApiModel.md)
 - [TestRunFilterApiModelAutoTestsCount](docs/TestRunFilterApiModelAutoTestsCount.md)
 - [TestRunFilterApiModelCompletedDate](docs/TestRunFilterApiModelCompletedDate.md)
 - [TestRunFilterApiModelCreatedDate](docs/TestRunFilterApiModelCreatedDate.md)
 - [TestRunFilterApiModelStartedDate](docs/TestRunFilterApiModelStartedDate.md)
 - [TestRunGroupByFailureClassApiResult](docs/TestRunGroupByFailureClassApiResult.md)
 - [TestRunGroupByStatusApiResult](docs/TestRunGroupByStatusApiResult.md)
 - [TestRunGroupByStatusTypeApiResult](docs/TestRunGroupByStatusTypeApiResult.md)
 - [TestRunNameApiResult](docs/TestRunNameApiResult.md)
 - [TestRunSelectApiModel](docs/TestRunSelectApiModel.md)
 - [TestRunSelectApiModelExtractionModel](docs/TestRunSelectApiModelExtractionModel.md)
 - [TestRunShortApiResult](docs/TestRunShortApiResult.md)
 - [TestRunShortApiResultStatistics](docs/TestRunShortApiResultStatistics.md)
 - [TestRunShortApiResultStatus](docs/TestRunShortApiResultStatus.md)
 - [TestRunState](docs/TestRunState.md)
 - [TestRunStatisticsFilterApiModel](docs/TestRunStatisticsFilterApiModel.md)
 - [TestRunTestResultsPartialBulkSetModel](docs/TestRunTestResultsPartialBulkSetModel.md)
 - [TestRunTestResultsPartialBulkSetModelSelector](docs/TestRunTestResultsPartialBulkSetModelSelector.md)
 - [TestRunTestResultsSelectModel](docs/TestRunTestResultsSelectModel.md)
 - [TestRunTestResultsSelectModelFilter](docs/TestRunTestResultsSelectModelFilter.md)
 - [TestRunTestResultsSelectModelTestResultIdsExtractionModel](docs/TestRunTestResultsSelectModelTestResultIdsExtractionModel.md)
 - [TestRunV2ApiResult](docs/TestRunV2ApiResult.md)
 - [TestStatusApiResult](docs/TestStatusApiResult.md)
 - [TestStatusApiResultReply](docs/TestStatusApiResultReply.md)
 - [TestStatusApiType](docs/TestStatusApiType.md)
 - [TestStatusModel](docs/TestStatusModel.md)
 - [TestStatusShortApiResult](docs/TestStatusShortApiResult.md)
 - [TestStatusType](docs/TestStatusType.md)
 - [TestSuiteApiResult](docs/TestSuiteApiResult.md)
 - [TestSuiteChangeViewModel](docs/TestSuiteChangeViewModel.md)
 - [TestSuiteChangeViewModelChangedFieldViewModel](docs/TestSuiteChangeViewModelChangedFieldViewModel.md)
 - [TestSuiteHierarchyApiResult](docs/TestSuiteHierarchyApiResult.md)
 - [TestSuiteTestPlanApiModel](docs/TestSuiteTestPlanApiModel.md)
 - [TestSuiteType](docs/TestSuiteType.md)
 - [TestSuiteTypeApiResult](docs/TestSuiteTypeApiResult.md)
 - [TestSuiteV2GetModel](docs/TestSuiteV2GetModel.md)
 - [TestSuiteV2PostModel](docs/TestSuiteV2PostModel.md)
 - [TestSuiteV2PutModel](docs/TestSuiteV2PutModel.md)
 - [TestSuiteWithChildrenModel](docs/TestSuiteWithChildrenModel.md)
 - [TestSuiteWorkItemsSearchModel](docs/TestSuiteWorkItemsSearchModel.md)
 - [TestSuiteWorkItemsSearchModelDuration](docs/TestSuiteWorkItemsSearchModelDuration.md)
 - [TestSuiteWorkItemsSearchModelExternalMetadata](docs/TestSuiteWorkItemsSearchModelExternalMetadata.md)
 - [TestSuiteWorkItemsSearchModelLinks](docs/TestSuiteWorkItemsSearchModelLinks.md)
 - [TestSuiteWorkItemsSearchModelMedianDuration](docs/TestSuiteWorkItemsSearchModelMedianDuration.md)
 - [UpdateAutoTestRequest](docs/UpdateAutoTestRequest.md)
 - [UpdateCustomAttributeTestPlanProjectRelationsRequest](docs/UpdateCustomAttributeTestPlanProjectRelationsRequest.md)
 - [UpdateEmptyRequest](docs/UpdateEmptyRequest.md)
 - [UpdateEmptyTestRunApiModel](docs/UpdateEmptyTestRunApiModel.md)
 - [UpdateFailureCategoryApiModel](docs/UpdateFailureCategoryApiModel.md)
 - [UpdateFailureCategoryProjectApiModel](docs/UpdateFailureCategoryProjectApiModel.md)
 - [UpdateFailureClassRegexApiModel](docs/UpdateFailureClassRegexApiModel.md)
 - [UpdateLinkApiModel](docs/UpdateLinkApiModel.md)
 - [UpdateMultipleAttachmentsApiModel](docs/UpdateMultipleAttachmentsApiModel.md)
 - [UpdateMultipleLinksApiModel](docs/UpdateMultipleLinksApiModel.md)
 - [UpdateMultipleTestRunsApiModel](docs/UpdateMultipleTestRunsApiModel.md)
 - [UpdateMultipleTestRunsApiModelAttachmentUpdateScheme](docs/UpdateMultipleTestRunsApiModelAttachmentUpdateScheme.md)
 - [UpdateMultipleTestRunsApiModelLinkUpdateScheme](docs/UpdateMultipleTestRunsApiModelLinkUpdateScheme.md)
 - [UpdateMultipleTestRunsApiModelSelectModel](docs/UpdateMultipleTestRunsApiModelSelectModel.md)
 - [UpdateParameterApiModel](docs/UpdateParameterApiModel.md)
 - [UpdateParameterRequest](docs/UpdateParameterRequest.md)
 - [UpdateProjectApiModel](docs/UpdateProjectApiModel.md)
 - [UpdateProjectRequest](docs/UpdateProjectRequest.md)
 - [UpdateProjectsAttributeRequest](docs/UpdateProjectsAttributeRequest.md)
 - [UpdateSectionRequest](docs/UpdateSectionRequest.md)
 - [UpdateStepApiModel](docs/UpdateStepApiModel.md)
 - [UpdateTagApiModel](docs/UpdateTagApiModel.md)
 - [UpdateTestPlanApiModel](docs/UpdateTestPlanApiModel.md)
 - [UpdateTestPlanRequest](docs/UpdateTestPlanRequest.md)
 - [UpdateTestStatusApiModel](docs/UpdateTestStatusApiModel.md)
 - [UpdateWorkItemApiModel](docs/UpdateWorkItemApiModel.md)
 - [UpdateWorkItemCommentApiModel](docs/UpdateWorkItemCommentApiModel.md)
 - [UpdateWorkItemRequest](docs/UpdateWorkItemRequest.md)
 - [UpdateWorkflowApiModel](docs/UpdateWorkflowApiModel.md)
 - [UserCustomNameValidationResponse](docs/UserCustomNameValidationResponse.md)
 - [UserNameApiResult](docs/UserNameApiResult.md)
 - [ValidationProblemDetails](docs/ValidationProblemDetails.md)
 - [WebHookEventType](docs/WebHookEventType.md)
 - [WebHookEventTypeModel](docs/WebHookEventTypeModel.md)
 - [WebHookEventTypeRequest](docs/WebHookEventTypeRequest.md)
 - [WebHookModel](docs/WebHookModel.md)
 - [WebHookPostModel](docs/WebHookPostModel.md)
 - [WebHookTestModel](docs/WebHookTestModel.md)
 - [WebhookBulkUpdateApiModel](docs/WebhookBulkUpdateApiModel.md)
 - [WebhookLogApiResult](docs/WebhookLogApiResult.md)
 - [WebhookResponse](docs/WebhookResponse.md)
 - [WebhookVariablesType](docs/WebhookVariablesType.md)
 - [WebhooksDeleteApiModel](docs/WebhooksDeleteApiModel.md)
 - [WebhooksDeleteApiModelExtractor](docs/WebhooksDeleteApiModelExtractor.md)
 - [WebhooksDeleteApiModelFilter](docs/WebhooksDeleteApiModelFilter.md)
 - [WebhooksDeleteFilterApiModel](docs/WebhooksDeleteFilterApiModel.md)
 - [WebhooksExtractionApiModel](docs/WebhooksExtractionApiModel.md)
 - [WebhooksFilterApiModel](docs/WebhooksFilterApiModel.md)
 - [WebhooksUpdateApiModel](docs/WebhooksUpdateApiModel.md)
 - [WebhooksUpdateApiModelFilter](docs/WebhooksUpdateApiModelFilter.md)
 - [WebhooksUpdateApiModelModel](docs/WebhooksUpdateApiModelModel.md)
 - [WebhooksUpdateApiResult](docs/WebhooksUpdateApiResult.md)
 - [WorkItemApiResult](docs/WorkItemApiResult.md)
 - [WorkItemChangeModel](docs/WorkItemChangeModel.md)
 - [WorkItemChangeModelWorkItemChangedFields](docs/WorkItemChangeModelWorkItemChangedFields.md)
 - [WorkItemChangedAttributeViewModel](docs/WorkItemChangedAttributeViewModel.md)
 - [WorkItemChangedFieldsViewModel](docs/WorkItemChangedFieldsViewModel.md)
 - [WorkItemChangedFieldsViewModelAttachments](docs/WorkItemChangedFieldsViewModelAttachments.md)
 - [WorkItemChangedFieldsViewModelAutoTests](docs/WorkItemChangedFieldsViewModelAutoTests.md)
 - [WorkItemChangedFieldsViewModelDuration](docs/WorkItemChangedFieldsViewModelDuration.md)
 - [WorkItemChangedFieldsViewModelGlobalId](docs/WorkItemChangedFieldsViewModelGlobalId.md)
 - [WorkItemChangedFieldsViewModelIsDeleted](docs/WorkItemChangedFieldsViewModelIsDeleted.md)
 - [WorkItemChangedFieldsViewModelLinks](docs/WorkItemChangedFieldsViewModelLinks.md)
 - [WorkItemChangedFieldsViewModelProjectId](docs/WorkItemChangedFieldsViewModelProjectId.md)
 - [WorkItemChangedFieldsViewModelState](docs/WorkItemChangedFieldsViewModelState.md)
 - [WorkItemChangedFieldsViewModelSteps](docs/WorkItemChangedFieldsViewModelSteps.md)
 - [WorkItemChangedFieldsViewModelTags](docs/WorkItemChangedFieldsViewModelTags.md)
 - [WorkItemCommentApiResult](docs/WorkItemCommentApiResult.md)
 - [WorkItemEntityTypeApiModel](docs/WorkItemEntityTypeApiModel.md)
 - [WorkItemEntityTypes](docs/WorkItemEntityTypes.md)
 - [WorkItemExternalMetadataFieldFilterApiModel](docs/WorkItemExternalMetadataFieldFilterApiModel.md)
 - [WorkItemExternalMetadataFieldFilterModel](docs/WorkItemExternalMetadataFieldFilterModel.md)
 - [WorkItemExternalMetadataFilterApiModel](docs/WorkItemExternalMetadataFilterApiModel.md)
 - [WorkItemExternalMetadataFilterModel](docs/WorkItemExternalMetadataFilterModel.md)
 - [WorkItemExtractionApiModel](docs/WorkItemExtractionApiModel.md)
 - [WorkItemExtractionApiModelIds](docs/WorkItemExtractionApiModelIds.md)
 - [WorkItemExtractionApiModelSectionIds](docs/WorkItemExtractionApiModelSectionIds.md)
 - [WorkItemExtractionModel](docs/WorkItemExtractionModel.md)
 - [WorkItemFilterApiModel](docs/WorkItemFilterApiModel.md)
 - [WorkItemFilterApiModelExternalMetadata](docs/WorkItemFilterApiModelExternalMetadata.md)
 - [WorkItemFilterApiModelLinks](docs/WorkItemFilterApiModelLinks.md)
 - [WorkItemFilterModel](docs/WorkItemFilterModel.md)
 - [WorkItemGroupGetModel](docs/WorkItemGroupGetModel.md)
 - [WorkItemGroupGetModelSelectModel](docs/WorkItemGroupGetModelSelectModel.md)
 - [WorkItemGroupModel](docs/WorkItemGroupModel.md)
 - [WorkItemGroupType](docs/WorkItemGroupType.md)
 - [WorkItemIdApiModel](docs/WorkItemIdApiModel.md)
 - [WorkItemIndexApiResult](docs/WorkItemIndexApiResult.md)
 - [WorkItemLikeModel](docs/WorkItemLikeModel.md)
 - [WorkItemLinkChangeViewModel](docs/WorkItemLinkChangeViewModel.md)
 - [WorkItemLinkChangeViewModelArrayChangedFieldViewModel](docs/WorkItemLinkChangeViewModelArrayChangedFieldViewModel.md)
 - [WorkItemLinkExtractionApiModel](docs/WorkItemLinkExtractionApiModel.md)
 - [WorkItemLinkFilterApiModel](docs/WorkItemLinkFilterApiModel.md)
 - [WorkItemLinkFilterModel](docs/WorkItemLinkFilterModel.md)
 - [WorkItemLinkUrlApiModel](docs/WorkItemLinkUrlApiModel.md)
 - [WorkItemLinkUrlApiModelExtractionModel](docs/WorkItemLinkUrlApiModelExtractionModel.md)
 - [WorkItemLinkUrlApiModelFilter](docs/WorkItemLinkUrlApiModelFilter.md)
 - [WorkItemLinkUrlApiResult](docs/WorkItemLinkUrlApiResult.md)
 - [WorkItemLinkUrlFilterApiModel](docs/WorkItemLinkUrlFilterApiModel.md)
 - [WorkItemLocalFilterModel](docs/WorkItemLocalFilterModel.md)
 - [WorkItemLocalSelectModel](docs/WorkItemLocalSelectModel.md)
 - [WorkItemLocalSelectModelExtractionModel](docs/WorkItemLocalSelectModelExtractionModel.md)
 - [WorkItemLocalSelectModelFilter](docs/WorkItemLocalSelectModelFilter.md)
 - [WorkItemModel](docs/WorkItemModel.md)
 - [WorkItemMovePostModel](docs/WorkItemMovePostModel.md)
 - [WorkItemPreviewApiModel](docs/WorkItemPreviewApiModel.md)
 - [WorkItemPreviewStepApiModel](docs/WorkItemPreviewStepApiModel.md)
 - [WorkItemPriority](docs/WorkItemPriority.md)
 - [WorkItemPriorityApiModel](docs/WorkItemPriorityApiModel.md)
 - [WorkItemPriorityModel](docs/WorkItemPriorityModel.md)
 - [WorkItemSearchQueryModel](docs/WorkItemSearchQueryModel.md)
 - [WorkItemSelectApiModel](docs/WorkItemSelectApiModel.md)
 - [WorkItemSelectApiModelFilter](docs/WorkItemSelectApiModelFilter.md)
 - [WorkItemSelectModel](docs/WorkItemSelectModel.md)
 - [WorkItemSelectModelFilter](docs/WorkItemSelectModelFilter.md)
 - [WorkItemShortApiResult](docs/WorkItemShortApiResult.md)
 - [WorkItemShortModel](docs/WorkItemShortModel.md)
 - [WorkItemSourceTypeApiModel](docs/WorkItemSourceTypeApiModel.md)
 - [WorkItemSourceTypeModel](docs/WorkItemSourceTypeModel.md)
 - [WorkItemState](docs/WorkItemState.md)
 - [WorkItemStateApiModel](docs/WorkItemStateApiModel.md)
 - [WorkItemStates](docs/WorkItemStates.md)
 - [WorkItemStepChangeViewModel](docs/WorkItemStepChangeViewModel.md)
 - [WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel](docs/WorkItemStepChangeViewModelArrayChangedFieldWithDiffsViewModel.md)
 - [WorkItemStepChangeViewModelWorkItem](docs/WorkItemStepChangeViewModelWorkItem.md)
 - [WorkItemUpdatingFieldsApiModel](docs/WorkItemUpdatingFieldsApiModel.md)
 - [WorkItemUpdatingFieldsApiResult](docs/WorkItemUpdatingFieldsApiResult.md)
 - [WorkItemVersionModel](docs/WorkItemVersionModel.md)
 - [WorkflowApiResult](docs/WorkflowApiResult.md)
 - [WorkflowExistsByNameApiResult](docs/WorkflowExistsByNameApiResult.md)
 - [WorkflowProjectApiResult](docs/WorkflowProjectApiResult.md)
 - [WorkflowProjectApiResultApiCollectionPreview](docs/WorkflowProjectApiResultApiCollectionPreview.md)
 - [WorkflowProjectApiResultReply](docs/WorkflowProjectApiResultReply.md)
 - [WorkflowShortApiResult](docs/WorkflowShortApiResult.md)
 - [WorkflowShortApiResultProjects](docs/WorkflowShortApiResultProjects.md)
 - [WorkflowShortApiResultReply](docs/WorkflowShortApiResultReply.md)
 - [WorkflowStatusApiModel](docs/WorkflowStatusApiModel.md)
 - [WorkflowStatusApiResult](docs/WorkflowStatusApiResult.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Bearer or PrivateToken"></a>
### Bearer or PrivateToken

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in testit_api_client.apis and testit_api_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from testit_api_client.api.default_api import DefaultApi`
- `from testit_api_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import testit_api_client
from testit_api_client.apis import *
from testit_api_client.models import *
```

