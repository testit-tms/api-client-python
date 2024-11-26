# TestResultResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**failure_class_ids** | **[str]** |  | 
**configuration_id** | **str** |  | 
**test_point_id** | **str** |  | 
**test_run_id** | **str** |  | 
**work_item_version_id** | **str** |  | 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**step_comments** | [**[StepComment], none_type**](StepComment.md) |  | [optional] 
**outcome** | [**TestResultOutcome**](TestResultOutcome.md) |  | [optional] 
**status** | [**TestStatus**](TestStatus.md) |  | [optional] 
**comment** | **str, none_type** |  | [optional] 
**links** | [**[Link], none_type**](Link.md) |  | [optional] 
**step_results** | [**[StepResult], none_type**](StepResult.md) |  | [optional] 
**attachments** | [**[Attachment], none_type**](Attachment.md) |  | [optional] 
**auto_test_id** | **str, none_type** |  | [optional] 
**started_on** | **datetime, none_type** |  | [optional] 
**completed_on** | **datetime, none_type** |  | [optional] 
**duration_in_ms** | **int, none_type** |  | [optional] 
**traces** | **str, none_type** |  | [optional] 
**failure_type** | **str, none_type** |  | [optional] 
**message** | **str, none_type** |  | [optional] 
**run_by_user_id** | **str, none_type** |  | [optional] 
**stopped_by_user_id** | **str, none_type** |  | [optional] 
**test_point** | [**TestPoint**](TestPoint.md) |  | [optional] 
**auto_test** | [**AutoTest**](AutoTest.md) |  | [optional] 
**auto_test_step_results** | [**[AutoTestStepResult], none_type**](AutoTestStepResult.md) |  | [optional] 
**setup_results** | [**[AutoTestStepResult], none_type**](AutoTestStepResult.md) |  | [optional] 
**teardown_results** | [**[AutoTestStepResult], none_type**](AutoTestStepResult.md) |  | [optional] 
**work_item_version_number** | **int, none_type** |  | [optional] 
**parameters** | **{str: (str,)}, none_type** |  | [optional] 
**properties** | **{str: (str,)}, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


