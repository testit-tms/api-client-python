# TestResultModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_id** | **str** |  | 
**test_point_id** | **str** |  | 
**test_run_id** | **str** |  | 
**work_item_version_id** | **str** |  | 
**id** | **str** |  | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**failure_class_ids** | **[str]** |  | 
**auto_test_id** | **str, none_type** |  | [optional] 
**started_on** | **datetime, none_type** |  | [optional] 
**completed_on** | **datetime, none_type** |  | [optional] 
**duration_in_ms** | **int, none_type** |  | [optional] 
**traces** | **str, none_type** |  | [optional] 
**failure_type** | **str, none_type** |  | [optional] 
**message** | **str, none_type** |  | [optional] 
**run_by_user_id** | **str, none_type** |  | [optional] 
**stopped_by_user_id** | **str, none_type** |  | [optional] 
**test_point** | [**TestPointPutModel**](TestPointPutModel.md) |  | [optional] 
**auto_test** | [**AutoTestModel**](AutoTestModel.md) |  | [optional] 
**auto_test_step_results** | [**[AttachmentModelAutoTestStepResultsModel], none_type**](AttachmentModelAutoTestStepResultsModel.md) |  | [optional] 
**setup_results** | [**[AttachmentModelAutoTestStepResultsModel], none_type**](AttachmentModelAutoTestStepResultsModel.md) |  | [optional] 
**teardown_results** | [**[AttachmentModelAutoTestStepResultsModel], none_type**](AttachmentModelAutoTestStepResultsModel.md) |  | [optional] 
**work_item_version_number** | **int, none_type** |  | [optional] 
**parameters** | **{str: (str,)}, none_type** |  | [optional] 
**properties** | **{str: (str,)}, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**step_comments** | [**[StepCommentModel], none_type**](StepCommentModel.md) |  | [optional] 
**outcome** | [**TestResultOutcome**](TestResultOutcome.md) |  | [optional] 
**comment** | **str, none_type** |  | [optional] 
**links** | [**[LinkModel], none_type**](LinkModel.md) |  | [optional] 
**step_results** | [**[StepResultModel], none_type**](StepResultModel.md) |  | [optional] 
**attachments** | [**[AttachmentModel], none_type**](AttachmentModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


