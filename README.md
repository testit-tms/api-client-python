# Api client for Test IT TMS
![Test IT](https://raw.githubusercontent.com/testit-tms/api-client-python/master/images/banner.png)

## Getting Started

### Compatibility

| Test IT | API Client |
|---------|------------|
| 3.5     | 2.0.1      |

## Installation & Usage
### pip install

```sh
pip install testit-api-client
```

Then import the package:

```python
import testit_api_client
```

## Getting Started

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
*AttachmentsApi* | [**api_v2_attachments_occupied_file_storage_size_get**](docs/AttachmentsApi.md#api_v2_attachments_occupied_file_storage_size_get) | **GET** /api/v2/attachments/occupiedFileStorageSize | 
*AttachmentsApi* | [**api_v2_attachments_post**](docs/AttachmentsApi.md#api_v2_attachments_post) | **POST** /api/v2/attachments | Upload new attachment file
*AutoTestsApi* | [**api_v2_auto_tests_flaky_bulk_post**](docs/AutoTestsApi.md#api_v2_auto_tests_flaky_bulk_post) | **POST** /api/v2/autoTests/flaky/bulk | Set \&quot;Flaky\&quot; status for multiple autotests
*AutoTestsApi* | [**api_v2_auto_tests_id_work_items_changed_id_get**](docs/AutoTestsApi.md#api_v2_auto_tests_id_work_items_changed_id_get) | **GET** /api/v2/autoTests/{id}/workItems/changed/id | Get identifiers of changed linked work items
*AutoTestsApi* | [**api_v2_auto_tests_id_work_items_changed_work_item_id_approve_post**](docs/AutoTestsApi.md#api_v2_auto_tests_id_work_items_changed_work_item_id_approve_post) | **POST** /api/v2/autoTests/{id}/workItems/changed/{workItemId}/approve | Approve changes to work items linked to autotest
*AutoTestsApi* | [**create_auto_test**](docs/AutoTestsApi.md#create_auto_test) | **POST** /api/v2/autoTests | Create autotest
*AutoTestsApi* | [**create_multiple**](docs/AutoTestsApi.md#create_multiple) | **POST** /api/v2/autoTests/bulk | Create multiple autotests
*AutoTestsApi* | [**delete_auto_test**](docs/AutoTestsApi.md#delete_auto_test) | **DELETE** /api/v2/autoTests/{id} | Delete autotest
*AutoTestsApi* | [**delete_auto_test_link_from_work_item**](docs/AutoTestsApi.md#delete_auto_test_link_from_work_item) | **DELETE** /api/v2/autoTests/{id}/workItems | Unlink autotest from work item
*AutoTestsApi* | [**get_all_auto_tests**](docs/AutoTestsApi.md#get_all_auto_tests) | **GET** /api/v2/autoTests | Get all autotests
*AutoTestsApi* | [**get_auto_test_average_duration**](docs/AutoTestsApi.md#get_auto_test_average_duration) | **GET** /api/v2/autoTests/{id}/averageDuration | Get average autotest duration
*AutoTestsApi* | [**get_auto_test_by_id**](docs/AutoTestsApi.md#get_auto_test_by_id) | **GET** /api/v2/autoTests/{id} | Get autotest by internal or global ID
*AutoTestsApi* | [**get_auto_test_chronology**](docs/AutoTestsApi.md#get_auto_test_chronology) | **GET** /api/v2/autoTests/{id}/chronology | Get autotest chronology
*AutoTestsApi* | [**get_test_runs**](docs/AutoTestsApi.md#get_test_runs) | **GET** /api/v2/autoTests/{id}/testRuns | Get completed tests runs for autotests
*AutoTestsApi* | [**get_work_item_results**](docs/AutoTestsApi.md#get_work_item_results) | **GET** /api/v2/autoTests/{id}/testResultHistory | Get test results history for autotest
*AutoTestsApi* | [**get_work_items_linked_to_auto_test**](docs/AutoTestsApi.md#get_work_items_linked_to_auto_test) | **GET** /api/v2/autoTests/{id}/workItems | Get work items linked to autotest
*AutoTestsApi* | [**link_auto_test_to_work_item**](docs/AutoTestsApi.md#link_auto_test_to_work_item) | **POST** /api/v2/autoTests/{id}/workItems | Link autotest with work items
*AutoTestsApi* | [**update_auto_test**](docs/AutoTestsApi.md#update_auto_test) | **PUT** /api/v2/autoTests | Update autotest
*AutoTestsApi* | [**update_multiple**](docs/AutoTestsApi.md#update_multiple) | **PUT** /api/v2/autoTests/bulk | Update multiple autotests
*ConfigurationsApi* | [**api_v2_configurations_create_by_parameters_post**](docs/ConfigurationsApi.md#api_v2_configurations_create_by_parameters_post) | **POST** /api/v2/configurations/createByParameters | Create Configurations by parameters
*ConfigurationsApi* | [**api_v2_configurations_search_post**](docs/ConfigurationsApi.md#api_v2_configurations_search_post) | **POST** /api/v2/configurations/search | Search for configurations
*ConfigurationsApi* | [**create_configuration**](docs/ConfigurationsApi.md#create_configuration) | **POST** /api/v2/configurations | Create Configuration
*ConfigurationsApi* | [**get_configuration_by_id**](docs/ConfigurationsApi.md#get_configuration_by_id) | **GET** /api/v2/configurations/{id} | Get configuration by internal or global ID
*ConfigurationsApi* | [**update_configuration**](docs/ConfigurationsApi.md#update_configuration) | **PUT** /api/v2/configurations | Update Configuration
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_custom_attributes_exclude_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_custom_attributes_exclude_post) | **POST** /api/v2/customAttributes/templates/{id}/customAttributes/exclude | Exclude CustomAttributes from CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_custom_attributes_include_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_custom_attributes_include_post) | **POST** /api/v2/customAttributes/templates/{id}/customAttributes/include | Include CustomAttributes to CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_delete**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_delete) | **DELETE** /api/v2/customAttributes/templates/{id} | Delete CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_id_get**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_id_get) | **GET** /api/v2/customAttributes/templates/{id} | Get CustomAttributeTemplate by ID
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_name_get**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_name_get) | **GET** /api/v2/customAttributes/templates/{name} | Get CustomAttributeTemplate by name
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_post) | **POST** /api/v2/customAttributes/templates | Create CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_put**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_put) | **PUT** /api/v2/customAttributes/templates | Update CustomAttributeTemplate
*CustomAttributeTemplatesApi* | [**api_v2_custom_attributes_templates_search_post**](docs/CustomAttributeTemplatesApi.md#api_v2_custom_attributes_templates_search_post) | **POST** /api/v2/customAttributes/templates/search | Search CustomAttributeTemplates
*CustomAttributesApi* | [**api_v2_custom_attributes_id_delete**](docs/CustomAttributesApi.md#api_v2_custom_attributes_id_delete) | **DELETE** /api/v2/customAttributes/{id} | 
*CustomAttributesApi* | [**api_v2_custom_attributes_id_get**](docs/CustomAttributesApi.md#api_v2_custom_attributes_id_get) | **GET** /api/v2/customAttributes/{id} | 
*CustomAttributesApi* | [**api_v2_custom_attributes_id_make_global_post**](docs/CustomAttributesApi.md#api_v2_custom_attributes_id_make_global_post) | **POST** /api/v2/customAttributes/{id}/makeGlobal | 
*CustomAttributesApi* | [**api_v2_custom_attributes_id_projects_get**](docs/CustomAttributesApi.md#api_v2_custom_attributes_id_projects_get) | **GET** /api/v2/customAttributes/{id}/projects | 
*CustomAttributesApi* | [**api_v2_custom_attributes_id_put**](docs/CustomAttributesApi.md#api_v2_custom_attributes_id_put) | **PUT** /api/v2/customAttributes/{id} | 
*CustomAttributesApi* | [**api_v2_custom_attributes_merge_post**](docs/CustomAttributesApi.md#api_v2_custom_attributes_merge_post) | **POST** /api/v2/customAttributes/merge | 
*CustomAttributesApi* | [**api_v2_custom_attributes_order_post**](docs/CustomAttributesApi.md#api_v2_custom_attributes_order_post) | **POST** /api/v2/customAttributes/order | 
*CustomAttributesApi* | [**api_v2_custom_attributes_post**](docs/CustomAttributesApi.md#api_v2_custom_attributes_post) | **POST** /api/v2/customAttributes | 
*CustomAttributesApi* | [**api_v2_custom_attributes_replace_post**](docs/CustomAttributesApi.md#api_v2_custom_attributes_replace_post) | **POST** /api/v2/customAttributes/replace | 
*CustomAttributesApi* | [**api_v2_custom_attributes_search_post**](docs/CustomAttributesApi.md#api_v2_custom_attributes_search_post) | **POST** /api/v2/customAttributes/search | 
*NotificationsApi* | [**api_v2_notifications_count_get**](docs/NotificationsApi.md#api_v2_notifications_count_get) | **GET** /api/v2/notifications/count | Get unread Notifications total in last 7 days
*NotificationsApi* | [**api_v2_notifications_get**](docs/NotificationsApi.md#api_v2_notifications_get) | **GET** /api/v2/notifications | Get all Notifications for current User
*NotificationsApi* | [**api_v2_notifications_id_read_post**](docs/NotificationsApi.md#api_v2_notifications_id_read_post) | **POST** /api/v2/notifications/{id}/read | Set Notification as read
*NotificationsApi* | [**api_v2_notifications_read_post**](docs/NotificationsApi.md#api_v2_notifications_read_post) | **POST** /api/v2/notifications/read | Set all Notifications as read
*ParametersApi* | [**api_v2_parameters_bulk_post**](docs/ParametersApi.md#api_v2_parameters_bulk_post) | **POST** /api/v2/parameters/bulk | Create multiple parameters
*ParametersApi* | [**api_v2_parameters_bulk_put**](docs/ParametersApi.md#api_v2_parameters_bulk_put) | **PUT** /api/v2/parameters/bulk | Update multiple parameters
*ParametersApi* | [**api_v2_parameters_groups_get**](docs/ParametersApi.md#api_v2_parameters_groups_get) | **GET** /api/v2/parameters/groups | Get parameters as group
*ParametersApi* | [**api_v2_parameters_key_name_name_exists_get**](docs/ParametersApi.md#api_v2_parameters_key_name_name_exists_get) | **GET** /api/v2/parameters/key/name/{name}/exists | Check existence parameter key in system
*ParametersApi* | [**api_v2_parameters_key_values_get**](docs/ParametersApi.md#api_v2_parameters_key_values_get) | **GET** /api/v2/parameters/{key}/values | Get all parameter key values
*ParametersApi* | [**api_v2_parameters_keys_get**](docs/ParametersApi.md#api_v2_parameters_keys_get) | **GET** /api/v2/parameters/keys | Get all parameter keys
*ParametersApi* | [**create_parameter**](docs/ParametersApi.md#create_parameter) | **POST** /api/v2/parameters | Create parameter
*ParametersApi* | [**delete_by_name**](docs/ParametersApi.md#delete_by_name) | **DELETE** /api/v2/parameters/name/{name} | Delete parameter by name
*ParametersApi* | [**delete_by_parameter_key_id**](docs/ParametersApi.md#delete_by_parameter_key_id) | **DELETE** /api/v2/parameters/keyId/{keyId} | Delete parameters by parameter key identifier
*ParametersApi* | [**delete_parameter**](docs/ParametersApi.md#delete_parameter) | **DELETE** /api/v2/parameters/{id} | Delete parameter
*ParametersApi* | [**get_all_parameters**](docs/ParametersApi.md#get_all_parameters) | **GET** /api/v2/parameters | Get all parameters
*ParametersApi* | [**get_parameter_by_id**](docs/ParametersApi.md#get_parameter_by_id) | **GET** /api/v2/parameters/{id} | Get parameter by ID
*ParametersApi* | [**obsolete_delete_by_name**](docs/ParametersApi.md#obsolete_delete_by_name) | **POST** /api/v2/parameters/deleteByName | 
*ParametersApi* | [**update_parameter**](docs/ParametersApi.md#update_parameter) | **PUT** /api/v2/parameters | Update parameter
*ProjectsApi* | [**api_v2_projects_id_custom_attribute_templates_template_id_delete**](docs/ProjectsApi.md#api_v2_projects_id_custom_attribute_templates_template_id_delete) | **DELETE** /api/v2/projects/{id}/customAttributeTemplates/{templateId} | Delete CustomAttributeTemplate from Project
*ProjectsApi* | [**api_v2_projects_id_custom_attribute_templates_template_id_post**](docs/ProjectsApi.md#api_v2_projects_id_custom_attribute_templates_template_id_post) | **POST** /api/v2/projects/{id}/customAttributeTemplates/{templateId} | Add CustomAttributeTemplate to Project
*ProjectsApi* | [**api_v2_projects_id_failure_classes_get**](docs/ProjectsApi.md#api_v2_projects_id_failure_classes_get) | **GET** /api/v2/projects/{id}/failureClasses | Get Project FailureClasses
*ProjectsApi* | [**api_v2_projects_id_favorite_put**](docs/ProjectsApi.md#api_v2_projects_id_favorite_put) | **PUT** /api/v2/projects/{id}/favorite | Mark Project as favorite
*ProjectsApi* | [**api_v2_projects_id_filters_get**](docs/ProjectsApi.md#api_v2_projects_id_filters_get) | **GET** /api/v2/projects/{id}/filters | Get Project filters
*ProjectsApi* | [**api_v2_projects_id_test_plans_analytics_get**](docs/ProjectsApi.md#api_v2_projects_id_test_plans_analytics_get) | **GET** /api/v2/projects/{id}/testPlans/analytics | Get TestPlans analytics
*ProjectsApi* | [**api_v2_projects_id_test_plans_search_post**](docs/ProjectsApi.md#api_v2_projects_id_test_plans_search_post) | **POST** /api/v2/projects/{id}/testPlans/search | Get Project TestPlans with analytics
*ProjectsApi* | [**api_v2_projects_id_test_runs_active_get**](docs/ProjectsApi.md#api_v2_projects_id_test_runs_active_get) | **GET** /api/v2/projects/{id}/testRuns/active | Get active Project TestRuns
*ProjectsApi* | [**api_v2_projects_id_test_runs_full_get**](docs/ProjectsApi.md#api_v2_projects_id_test_runs_full_get) | **GET** /api/v2/projects/{id}/testRuns/full | Get Project TestRuns full models
*ProjectsApi* | [**api_v2_projects_id_work_items_tags_get**](docs/ProjectsApi.md#api_v2_projects_id_work_items_tags_get) | **GET** /api/v2/projects/{id}/workItems/tags | Get WorkItems Tags
*ProjectsApi* | [**api_v2_projects_search_post**](docs/ProjectsApi.md#api_v2_projects_search_post) | **POST** /api/v2/projects/search | 
*ProjectsApi* | [**call_import**](docs/ProjectsApi.md#call_import) | **POST** /api/v2/projects/import | Import project from JSON file
*ProjectsApi* | [**create_custom_attribute_test_plan_project_relations**](docs/ProjectsApi.md#create_custom_attribute_test_plan_project_relations) | **POST** /api/v2/projects/{id}/testPlans/attributes | Add attributes to project&#39;s test plans
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /api/v2/projects | Create project
*ProjectsApi* | [**create_projects_attribute**](docs/ProjectsApi.md#create_projects_attribute) | **POST** /api/v2/projects/{id}/attributes | Create project attribute
*ProjectsApi* | [**delete_custom_attribute_test_plan_project_relations**](docs/ProjectsApi.md#delete_custom_attribute_test_plan_project_relations) | **DELETE** /api/v2/projects/{id}/testPlans/attribute/{attributeId} | Delete attribute from project&#39;s test plans
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /api/v2/projects/{id} | Delete project
*ProjectsApi* | [**delete_project_auto_tests**](docs/ProjectsApi.md#delete_project_auto_tests) | **DELETE** /api/v2/projects/{id}/autoTests | Delete project
*ProjectsApi* | [**delete_projects_attribute**](docs/ProjectsApi.md#delete_projects_attribute) | **DELETE** /api/v2/projects/{id}/attributes/{attributeId} | Delete project attribute
*ProjectsApi* | [**export**](docs/ProjectsApi.md#export) | **POST** /api/v2/projects/{id}/export | Export project as JSON file
*ProjectsApi* | [**export_with_test_plans_and_configurations**](docs/ProjectsApi.md#export_with_test_plans_and_configurations) | **POST** /api/v2/projects/{id}/export-by-testPlans | Export project with test plans, test suites and test points as JSON file
*ProjectsApi* | [**get_all_projects**](docs/ProjectsApi.md#get_all_projects) | **GET** /api/v2/projects | Get all projects
*ProjectsApi* | [**get_attribute_by_project_id**](docs/ProjectsApi.md#get_attribute_by_project_id) | **GET** /api/v2/projects/{id}/attributes/{attributeId} | Get project attribute
*ProjectsApi* | [**get_attributes_by_project_id**](docs/ProjectsApi.md#get_attributes_by_project_id) | **GET** /api/v2/projects/{id}/attributes | Get project attributes
*ProjectsApi* | [**get_auto_tests_namespaces**](docs/ProjectsApi.md#get_auto_tests_namespaces) | **GET** /api/v2/projects/{id}/autoTestsNamespaces | Get namespaces of autotests in project
*ProjectsApi* | [**get_configurations_by_project_id**](docs/ProjectsApi.md#get_configurations_by_project_id) | **GET** /api/v2/projects/{id}/configurations | Get project configurations
*ProjectsApi* | [**get_custom_attribute_test_plan_project_relations**](docs/ProjectsApi.md#get_custom_attribute_test_plan_project_relations) | **GET** /api/v2/projects/{id}/testPlans/attributes | Get project&#39;s test plan attributes
*ProjectsApi* | [**get_project_by_id**](docs/ProjectsApi.md#get_project_by_id) | **GET** /api/v2/projects/{id} | Get project by ID
*ProjectsApi* | [**get_sections_by_project_id**](docs/ProjectsApi.md#get_sections_by_project_id) | **GET** /api/v2/projects/{id}/sections | Get project sections
*ProjectsApi* | [**get_test_plans_by_project_id**](docs/ProjectsApi.md#get_test_plans_by_project_id) | **GET** /api/v2/projects/{id}/testPlans | Get project test plans
*ProjectsApi* | [**get_test_runs_by_project_id**](docs/ProjectsApi.md#get_test_runs_by_project_id) | **GET** /api/v2/projects/{id}/testRuns | Get project test runs
*ProjectsApi* | [**get_work_items_by_project_id**](docs/ProjectsApi.md#get_work_items_by_project_id) | **GET** /api/v2/projects/{id}/workItems | Get project work items
*ProjectsApi* | [**import_to_existing_project**](docs/ProjectsApi.md#import_to_existing_project) | **POST** /api/v2/projects/{id}/import | Import project from JSON file into existing project
*ProjectsApi* | [**restore_project**](docs/ProjectsApi.md#restore_project) | **POST** /api/v2/projects/{id}/restore | Restore project
*ProjectsApi* | [**update_custom_attribute_test_plan_project_relations**](docs/ProjectsApi.md#update_custom_attribute_test_plan_project_relations) | **PUT** /api/v2/projects/{id}/testPlans/attribute | Update attribute of project&#39;s test plans
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /api/v2/projects | Update project
*ProjectsApi* | [**update_projects_attribute**](docs/ProjectsApi.md#update_projects_attribute) | **PUT** /api/v2/projects/{id}/attributes | Update project attribute
*SectionsApi* | [**create_section**](docs/SectionsApi.md#create_section) | **POST** /api/v2/sections | Create section
*SectionsApi* | [**delete_section**](docs/SectionsApi.md#delete_section) | **DELETE** /api/v2/sections/{id} | Delete section
*SectionsApi* | [**get_section_by_id**](docs/SectionsApi.md#get_section_by_id) | **GET** /api/v2/sections/{id} | Get section
*SectionsApi* | [**get_work_items_by_section_id**](docs/SectionsApi.md#get_work_items_by_section_id) | **GET** /api/v2/sections/{id}/workItems | Get section work items
*SectionsApi* | [**move**](docs/SectionsApi.md#move) | **POST** /api/v2/sections/move | Move section
*SectionsApi* | [**rename**](docs/SectionsApi.md#rename) | **POST** /api/v2/sections/rename | Rename section
*SectionsApi* | [**update_section**](docs/SectionsApi.md#update_section) | **PUT** /api/v2/sections | Update section
*StepCommentsApi* | [**api_v2_step_comments_id_get**](docs/StepCommentsApi.md#api_v2_step_comments_id_get) | **GET** /api/v2/stepComments/{id} | Get StepComment by internal ID
*TagsApi* | [**api_v2_tags_get**](docs/TagsApi.md#api_v2_tags_get) | **GET** /api/v2/tags | Get all Tags
*TagsApi* | [**api_v2_tags_test_plans_tags_get**](docs/TagsApi.md#api_v2_tags_test_plans_tags_get) | **GET** /api/v2/tags/testPlansTags | Get all Tags that are used in TestPlans
*TestPlansApi* | [**add_test_points_with_sections**](docs/TestPlansApi.md#add_test_points_with_sections) | **POST** /api/v2/testPlans/{id}/test-points/withSections | Add test-points to test suite with sections
*TestPlansApi* | [**add_work_items_with_sections**](docs/TestPlansApi.md#add_work_items_with_sections) | **POST** /api/v2/testPlans/{id}/workItems/withSections | Add WorkItems to TestPlan with Sections as TestSuites
*TestPlansApi* | [**api_v2_test_plans_id_analytics_get**](docs/TestPlansApi.md#api_v2_test_plans_id_analytics_get) | **GET** /api/v2/testPlans/{id}/analytics | Get analytics by TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_autobalance_post**](docs/TestPlansApi.md#api_v2_test_plans_id_autobalance_post) | **POST** /api/v2/testPlans/{id}/autobalance | Auto-balance for TestPlan with testers
*TestPlansApi* | [**api_v2_test_plans_id_configurations_get**](docs/TestPlansApi.md#api_v2_test_plans_id_configurations_get) | **GET** /api/v2/testPlans/{id}/configurations | Get TestPlan configurations
*TestPlansApi* | [**api_v2_test_plans_id_export_test_points_xlsx_post**](docs/TestPlansApi.md#api_v2_test_plans_id_export_test_points_xlsx_post) | **POST** /api/v2/testPlans/{id}/export/testPoints/xlsx | Export TestPoints from TestPlan in xls format
*TestPlansApi* | [**api_v2_test_plans_id_export_test_result_history_xlsx_post**](docs/TestPlansApi.md#api_v2_test_plans_id_export_test_result_history_xlsx_post) | **POST** /api/v2/testPlans/{id}/export/testResultHistory/xlsx | Export TestResults history from TestPlan in xls format
*TestPlansApi* | [**api_v2_test_plans_id_history_get**](docs/TestPlansApi.md#api_v2_test_plans_id_history_get) | **GET** /api/v2/testPlans/{id}/history | Get TestPlan history
*TestPlansApi* | [**api_v2_test_plans_id_links_get**](docs/TestPlansApi.md#api_v2_test_plans_id_links_get) | **GET** /api/v2/testPlans/{id}/links | Get Links of TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_test_points_last_results_get**](docs/TestPlansApi.md#api_v2_test_plans_id_test_points_last_results_get) | **GET** /api/v2/testPlans/{id}/testPoints/lastResults | Get TestPoints with last result from TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_test_points_reset_post**](docs/TestPlansApi.md#api_v2_test_plans_id_test_points_reset_post) | **POST** /api/v2/testPlans/{id}/testPoints/reset | Reset TestPoints status of TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_test_runs_get**](docs/TestPlansApi.md#api_v2_test_plans_id_test_runs_get) | **GET** /api/v2/testPlans/{id}/testRuns | Get TestRuns of TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_test_runs_search_post**](docs/TestPlansApi.md#api_v2_test_plans_id_test_runs_search_post) | **POST** /api/v2/testPlans/{id}/testRuns/search | Search TestRuns of TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get**](docs/TestPlansApi.md#api_v2_test_plans_id_test_runs_test_results_last_modified_modified_date_get) | **GET** /api/v2/testPlans/{id}/testRuns/testResults/lastModified/modifiedDate | Get max modified date in TestRun for TestPlan
*TestPlansApi* | [**api_v2_test_plans_id_unlock_request_post**](docs/TestPlansApi.md#api_v2_test_plans_id_unlock_request_post) | **POST** /api/v2/testPlans/{id}/unlock/request | Send unlock TestPlan notification
*TestPlansApi* | [**api_v2_test_plans_shorts_post**](docs/TestPlansApi.md#api_v2_test_plans_shorts_post) | **POST** /api/v2/testPlans/shorts | Get TestPlans short models by Project identifiers
*TestPlansApi* | [**clone**](docs/TestPlansApi.md#clone) | **POST** /api/v2/testPlans/{id}/clone | Clone TestPlan
*TestPlansApi* | [**complete**](docs/TestPlansApi.md#complete) | **POST** /api/v2/testPlans/{id}/complete | Complete TestPlan
*TestPlansApi* | [**create_test_plan**](docs/TestPlansApi.md#create_test_plan) | **POST** /api/v2/testPlans | Create TestPlan
*TestPlansApi* | [**delete_test_plan**](docs/TestPlansApi.md#delete_test_plan) | **DELETE** /api/v2/testPlans/{id} | Delete TestPlan
*TestPlansApi* | [**get_test_plan_by_id**](docs/TestPlansApi.md#get_test_plan_by_id) | **GET** /api/v2/testPlans/{id} | Get TestPlan by Id
*TestPlansApi* | [**get_test_suites_by_id**](docs/TestPlansApi.md#get_test_suites_by_id) | **GET** /api/v2/testPlans/{id}/testSuites | Get TestSuites Tree By Id
*TestPlansApi* | [**pause**](docs/TestPlansApi.md#pause) | **POST** /api/v2/testPlans/{id}/pause | Pause TestPlan
*TestPlansApi* | [**restore_test_plan**](docs/TestPlansApi.md#restore_test_plan) | **POST** /api/v2/testPlans/{id}/restore | Restore TestPlan
*TestPlansApi* | [**start**](docs/TestPlansApi.md#start) | **POST** /api/v2/testPlans/{id}/start | Start TestPlan
*TestPlansApi* | [**update_test_plan**](docs/TestPlansApi.md#update_test_plan) | **PUT** /api/v2/testPlans | Update TestPlan
*TestPointsApi* | [**api_v2_test_points_id_test_runs_get**](docs/TestPointsApi.md#api_v2_test_points_id_test_runs_get) | **GET** /api/v2/testPoints/{id}/testRuns | 
*TestPointsApi* | [**api_v2_test_points_id_work_item_get**](docs/TestPointsApi.md#api_v2_test_points_id_work_item_get) | **GET** /api/v2/testPoints/{id}/workItem | 
*TestPointsApi* | [**api_v2_test_points_search_post**](docs/TestPointsApi.md#api_v2_test_points_search_post) | **POST** /api/v2/testPoints/search | 
*TestResultsApi* | [**api_v2_test_results_id_aggregated_get**](docs/TestResultsApi.md#api_v2_test_results_id_aggregated_get) | **GET** /api/v2/testResults/{id}/aggregated | 
*TestResultsApi* | [**api_v2_test_results_id_attachments_attachment_id_put**](docs/TestResultsApi.md#api_v2_test_results_id_attachments_attachment_id_put) | **PUT** /api/v2/testResults/{id}/attachments/{attachmentId} | 
*TestResultsApi* | [**api_v2_test_results_id_attachments_info_get**](docs/TestResultsApi.md#api_v2_test_results_id_attachments_info_get) | **GET** /api/v2/testResults/{id}/attachments/info | 
*TestResultsApi* | [**api_v2_test_results_id_external_projects_external_project_id_defect_post**](docs/TestResultsApi.md#api_v2_test_results_id_external_projects_external_project_id_defect_post) | **POST** /api/v2/testResults/{id}/externalProjects/{externalProjectId}/defect | 
*TestResultsApi* | [**api_v2_test_results_id_external_projects_external_project_id_form_get**](docs/TestResultsApi.md#api_v2_test_results_id_external_projects_external_project_id_form_get) | **GET** /api/v2/testResults/{id}/externalProjects/{externalProjectId}/form | 
*TestResultsApi* | [**api_v2_test_results_id_get**](docs/TestResultsApi.md#api_v2_test_results_id_get) | **GET** /api/v2/testResults/{id} | 
*TestResultsApi* | [**api_v2_test_results_id_link_requests_post**](docs/TestResultsApi.md#api_v2_test_results_id_link_requests_post) | **POST** /api/v2/testResults/{id}/linkRequests | 
*TestResultsApi* | [**api_v2_test_results_id_put**](docs/TestResultsApi.md#api_v2_test_results_id_put) | **PUT** /api/v2/testResults/{id} | 
*TestResultsApi* | [**api_v2_test_results_link_requests_link_request_id_use_post**](docs/TestResultsApi.md#api_v2_test_results_link_requests_link_request_id_use_post) | **POST** /api/v2/testResults/linkRequests/{linkRequestId}/use | 
*TestResultsApi* | [**create_attachment**](docs/TestResultsApi.md#create_attachment) | **POST** /api/v2/testResults/{id}/attachments | Upload and link attachment to TestResult
*TestResultsApi* | [**delete_attachment**](docs/TestResultsApi.md#delete_attachment) | **DELETE** /api/v2/testResults/{id}/attachments/{attachmentId} | Remove attachment and unlink from TestResult
*TestResultsApi* | [**download_attachment**](docs/TestResultsApi.md#download_attachment) | **GET** /api/v2/testResults/{id}/attachments/{attachmentId} | Get attachment of TestResult
*TestResultsApi* | [**get_attachment**](docs/TestResultsApi.md#get_attachment) | **GET** /api/v2/testResults/{id}/attachments/{attachmentId}/info | Get Metadata of TestResult&#39;s attachment
*TestResultsApi* | [**get_attachments**](docs/TestResultsApi.md#get_attachments) | **GET** /api/v2/testResults/{id}/attachments | Get all attachments of TestResult
*TestRunsApi* | [**api_v2_test_runs_id_test_points_results_get**](docs/TestRunsApi.md#api_v2_test_runs_id_test_points_results_get) | **GET** /api/v2/testRuns/{id}/testPoints/results | 
*TestRunsApi* | [**api_v2_test_runs_id_test_results_last_modified_modification_date_get**](docs/TestRunsApi.md#api_v2_test_runs_id_test_results_last_modified_modification_date_get) | **GET** /api/v2/testRuns/{id}/testResults/lastModified/modificationDate | 
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
*TestSuitesApi* | [**create_test_suite**](docs/TestSuitesApi.md#create_test_suite) | **POST** /api/v2/testSuites | Create TestSuite
*TestSuitesApi* | [**delete_test_suite**](docs/TestSuitesApi.md#delete_test_suite) | **DELETE** /api/v2/testSuites/{id} | Delete TestSuite
*TestSuitesApi* | [**get_configurations_by_test_suite_id**](docs/TestSuitesApi.md#get_configurations_by_test_suite_id) | **GET** /api/v2/testSuites/{id}/configurations | Get Configurations By Id
*TestSuitesApi* | [**get_test_points_by_id**](docs/TestSuitesApi.md#get_test_points_by_id) | **GET** /api/v2/testSuites/{id}/testPoints | Get TestPoints By Id
*TestSuitesApi* | [**get_test_results_by_id**](docs/TestSuitesApi.md#get_test_results_by_id) | **GET** /api/v2/testSuites/{id}/testResults | Get TestResults By Id
*TestSuitesApi* | [**get_test_suite_by_id**](docs/TestSuitesApi.md#get_test_suite_by_id) | **GET** /api/v2/testSuites/{id} | Get TestSuite by Id
*TestSuitesApi* | [**get_work_items_by_id**](docs/TestSuitesApi.md#get_work_items_by_id) | **GET** /api/v2/testSuites/{id}/workItems | 
*TestSuitesApi* | [**search_work_items**](docs/TestSuitesApi.md#search_work_items) | **POST** /api/v2/testSuites/{id}/workItems/search | Search WorkItems
*TestSuitesApi* | [**set_configurations_by_test_suite_id**](docs/TestSuitesApi.md#set_configurations_by_test_suite_id) | **POST** /api/v2/testSuites/{id}/configurations | Set Configurations By TestSuite Id
*TestSuitesApi* | [**set_work_items_by_test_suite_id**](docs/TestSuitesApi.md#set_work_items_by_test_suite_id) | **POST** /api/v2/testSuites/{id}/workItems | Set WorkItems By TestSuite Id
*TestSuitesApi* | [**update_test_suite**](docs/TestSuitesApi.md#update_test_suite) | **PUT** /api/v2/testSuites | Update TestSuite
*WebhooksApi* | [**api_v2_webhooks_get**](docs/WebhooksApi.md#api_v2_webhooks_get) | **GET** /api/v2/webhooks | 
*WebhooksApi* | [**api_v2_webhooks_id_delete**](docs/WebhooksApi.md#api_v2_webhooks_id_delete) | **DELETE** /api/v2/webhooks/{id} | 
*WebhooksApi* | [**api_v2_webhooks_id_get**](docs/WebhooksApi.md#api_v2_webhooks_id_get) | **GET** /api/v2/webhooks/{id} | 
*WebhooksApi* | [**api_v2_webhooks_id_put**](docs/WebhooksApi.md#api_v2_webhooks_id_put) | **PUT** /api/v2/webhooks/{id} | 
*WebhooksApi* | [**api_v2_webhooks_post**](docs/WebhooksApi.md#api_v2_webhooks_post) | **POST** /api/v2/webhooks | 
*WebhooksApi* | [**api_v2_webhooks_special_variables_get**](docs/WebhooksApi.md#api_v2_webhooks_special_variables_get) | **GET** /api/v2/webhooks/specialVariables | 
*WebhooksLogsApi* | [**api_v2_webhooks_logs_get**](docs/WebhooksLogsApi.md#api_v2_webhooks_logs_get) | **GET** /api/v2/webhooks/logs | 
*WebhooksLogsApi* | [**api_v2_webhooks_logs_id_delete**](docs/WebhooksLogsApi.md#api_v2_webhooks_logs_id_delete) | **DELETE** /api/v2/webhooks/logs/{id} | 
*WebhooksLogsApi* | [**api_v2_webhooks_logs_id_get**](docs/WebhooksLogsApi.md#api_v2_webhooks_logs_id_get) | **GET** /api/v2/webhooks/logs/{id} | 
*WorkItemsApi* | [**api_v2_work_items_id_actual_post**](docs/WorkItemsApi.md#api_v2_work_items_id_actual_post) | **POST** /api/v2/workItems/{id}/actual | Set WorkItem as actual
*WorkItemsApi* | [**api_v2_work_items_id_check_list_transform_to_test_case_post**](docs/WorkItemsApi.md#api_v2_work_items_id_check_list_transform_to_test_case_post) | **POST** /api/v2/workItems/{id}/checkList/transformTo/testCase | Transform CheckList to TestCase
*WorkItemsApi* | [**api_v2_work_items_id_history_get**](docs/WorkItemsApi.md#api_v2_work_items_id_history_get) | **GET** /api/v2/workItems/{id}/history | Get change history of WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_like_delete**](docs/WorkItemsApi.md#api_v2_work_items_id_like_delete) | **DELETE** /api/v2/workItems/{id}/like | Delete like from WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_like_post**](docs/WorkItemsApi.md#api_v2_work_items_id_like_post) | **POST** /api/v2/workItems/{id}/like | Set like to WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_likes_count_get**](docs/WorkItemsApi.md#api_v2_work_items_id_likes_count_get) | **GET** /api/v2/workItems/{id}/likes/count | Get likes count of WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_likes_get**](docs/WorkItemsApi.md#api_v2_work_items_id_likes_get) | **GET** /api/v2/workItems/{id}/likes | Get likes of WorkItem
*WorkItemsApi* | [**api_v2_work_items_id_test_results_history_get**](docs/WorkItemsApi.md#api_v2_work_items_id_test_results_history_get) | **GET** /api/v2/workItems/{id}/testResults/history | Get test results history of WorkItem
*WorkItemsApi* | [**api_v2_work_items_move_post**](docs/WorkItemsApi.md#api_v2_work_items_move_post) | **POST** /api/v2/workItems/move | Move WorkItem to another section
*WorkItemsApi* | [**api_v2_work_items_shared_steps_shared_step_id_references_get**](docs/WorkItemsApi.md#api_v2_work_items_shared_steps_shared_step_id_references_get) | **GET** /api/v2/workItems/sharedSteps/{sharedStepId}/references | Get SharedStep references
*WorkItemsApi* | [**create_work_item**](docs/WorkItemsApi.md#create_work_item) | **POST** /api/v2/workItems | Create Test Case, Checklist or Shared Step
*WorkItemsApi* | [**delete_all_work_items_from_auto_test**](docs/WorkItemsApi.md#delete_all_work_items_from_auto_test) | **DELETE** /api/v2/workItems/{id}/autoTests | Delete all links AutoTests from WorkItem by Id or GlobalId
*WorkItemsApi* | [**delete_work_item**](docs/WorkItemsApi.md#delete_work_item) | **DELETE** /api/v2/workItems/{id} | Delete Test Case, Checklist or Shared Step by Id or GlobalId
*WorkItemsApi* | [**get_auto_tests_for_work_item**](docs/WorkItemsApi.md#get_auto_tests_for_work_item) | **GET** /api/v2/workItems/{id}/autoTests | Get all AutoTests linked to WorkItem by Id or GlobalId
*WorkItemsApi* | [**get_iterations**](docs/WorkItemsApi.md#get_iterations) | **GET** /api/v2/workItems/{id}/iterations | Get iterations by workitem Id or GlobalId
*WorkItemsApi* | [**get_work_item_by_id**](docs/WorkItemsApi.md#get_work_item_by_id) | **GET** /api/v2/workItems/{id} | Get Test Case, Checklist or Shared Step by Id or GlobalId
*WorkItemsApi* | [**get_work_item_chronology**](docs/WorkItemsApi.md#get_work_item_chronology) | **GET** /api/v2/workItems/{id}/chronology | Get WorkItem chronology by Id or GlobalId
*WorkItemsApi* | [**get_work_item_versions**](docs/WorkItemsApi.md#get_work_item_versions) | **GET** /api/v2/workItems/{id}/versions | Get WorkItem versions
*WorkItemsApi* | [**update_work_item**](docs/WorkItemsApi.md#update_work_item) | **PUT** /api/v2/workItems | Update Test Case, Checklist or Shared Step
*WorkItemsCommentsApi* | [**api_v2_work_items_comments_comment_id_delete**](docs/WorkItemsCommentsApi.md#api_v2_work_items_comments_comment_id_delete) | **DELETE** /api/v2/workItems/comments/{commentId} | Delete WorkItem comment
*WorkItemsCommentsApi* | [**api_v2_work_items_comments_post**](docs/WorkItemsCommentsApi.md#api_v2_work_items_comments_post) | **POST** /api/v2/workItems/comments | Create WorkItem comment
*WorkItemsCommentsApi* | [**api_v2_work_items_comments_put**](docs/WorkItemsCommentsApi.md#api_v2_work_items_comments_put) | **PUT** /api/v2/workItems/comments | Update WorkItem comment
*WorkItemsCommentsApi* | [**api_v2_work_items_id_comments_get**](docs/WorkItemsCommentsApi.md#api_v2_work_items_id_comments_get) | **GET** /api/v2/workItems/{id}/comments | Get WorkItem comments by Id or GlobalId


## Documentation For Models

 - You can see the documentation [here](docs/README.md).


# Contributing

You can help to develop the project. Any contributions are **greatly appreciated**.

* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/testit-tms/api-client-python/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/testit-tms/api-client-python/blob/master/CODE_OF_CONDUCT.md) before posting your first idea as well.


# License

Distributed under the Apache-2.0 License. See [LICENSE](https://github.com/testit-tms/api-client-python/blob/master/LICENSE.md) for more information.

