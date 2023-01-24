# TestResultV2GetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ConfigurationModel**](ConfigurationModel.md) |  | [optional] 
**auto_test** | [**AutoTestModelV2GetModel**](AutoTestModelV2GetModel.md) |  | [optional] 
**id** | **str** |  | [optional] 
**configuration_id** | **str** |  | [optional] 
**work_item_version_id** | **str** |  | [optional] 
**auto_test_id** | **str, none_type** |  | [optional] 
**message** | **str, none_type** |  | [optional] 
**traces** | **str, none_type** |  | [optional] 
**started_on** | **datetime, none_type** |  | [optional] 
**completed_on** | **datetime, none_type** |  | [optional] 
**run_by_user_id** | **str, none_type** |  | [optional] 
**stopped_by_user_id** | **str, none_type** |  | [optional] 
**test_point_id** | **str, none_type** |  | [optional] 
**test_point** | [**TestPointShortModel**](TestPointShortModel.md) |  | [optional] 
**test_run_id** | **str** |  | [optional] 
**outcome** | **str, none_type** | Property can contain one of these values: Passed, Failed, InProgress, Blocked, Skipped | [optional] 
**comment** | **str, none_type** |  | [optional] 
**links** | [**[LinkModel], none_type**](LinkModel.md) |  | [optional] 
**attachments** | [**[AttachmentModel], none_type**](AttachmentModel.md) |  | [optional] 
**parameters** | **{str: (str, none_type)}, none_type** |  | [optional] 
**properties** | **{str: (str, none_type)}, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


