# CreateAndFillByConfigurationsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | Specifies the GUID of the project, in which a test run will be created. | 
**test_plan_id** | **str** | Specifies the GUID of the test plan, within which the test run will be created. | 
**test_point_selectors** | [**[TestPointSelector]**](TestPointSelector.md) | Specifies an array of work items and configuration to create a test run for. | 
**name** | **str, none_type** | Specifies the name of the test run. | [optional] 
**description** | **str, none_type** | Specifies the test run description. | [optional] 
**launch_source** | **str, none_type** | Specifies the test run launch source. | [optional] 
**attachments** | [**[AssignAttachmentApiModel], none_type**](AssignAttachmentApiModel.md) | Collection of attachment ids to relate to the test run | [optional] 
**links** | [**[CreateLinkApiModel], none_type**](CreateLinkApiModel.md) | Collection of links to relate to the test run | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


