# TestRunV2GetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_name** | [**TestRunState**](TestRunState.md) |  | 
**project_id** | **str** | This property is used to link test run with project | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**started_on** | **datetime, none_type** |  | [optional] 
**completed_on** | **datetime, none_type** |  | [optional] 
**test_plan_id** | **str, none_type** | This property is used to link test run with test plan | [optional] 
**test_results** | [**[TestResultV2GetModel], none_type**](TestResultV2GetModel.md) |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**created_by_user_name** | **str, none_type** |  | [optional] 
**attachments** | [**[AttachmentModel], none_type**](AttachmentModel.md) |  | [optional] 
**links** | [**[LinkModel], none_type**](LinkModel.md) |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**launch_source** | **str, none_type** | Once launch source is specified it cannot be updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


