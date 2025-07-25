# TestResultApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**outcome** | **str** |  | 
**test_run_id** | **str** |  | 
**configuration_id** | **str** |  | 
**status** | [**AutoTestResultHistoryApiResultStatus**](AutoTestResultHistoryApiResultStatus.md) |  | 
**attachments** | [**[AttachmentApiResult]**](AttachmentApiResult.md) |  | 
**links** | [**[LinkApiResult]**](LinkApiResult.md) |  | 
**failure_classes** | [**[TestResultFailureClassApiResult]**](TestResultFailureClassApiResult.md) |  | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**is_deleted** | **bool** |  | 
**started_on** | **datetime, none_type** |  | [optional] 
**completed_on** | **datetime, none_type** |  | [optional] 
**duration_in_ms** | **int, none_type** |  | [optional] 
**traces** | **str, none_type** |  | [optional] 
**failure_type** | **str, none_type** |  | [optional] 
**message** | **str, none_type** |  | [optional] 
**run_by_user_id** | **str, none_type** |  | [optional] 
**stopped_by_user_id** | **str, none_type** |  | [optional] 
**auto_test_id** | **str, none_type** |  | [optional] 
**test_point_id** | **str, none_type** |  | [optional] 
**test_point** | [**TestPointShortApiResult**](TestPointShortApiResult.md) |  | [optional] 
**auto_test** | [**AutoTestApiResult**](AutoTestApiResult.md) |  | [optional] 
**auto_test_step_results** | [**[AutoTestStepResultsApiResult], none_type**](AutoTestStepResultsApiResult.md) |  | [optional] 
**setup_results** | [**[AutoTestStepResultsApiResult], none_type**](AutoTestStepResultsApiResult.md) |  | [optional] 
**teardown_results** | [**[AutoTestStepResultsApiResult], none_type**](AutoTestStepResultsApiResult.md) |  | [optional] 
**work_item_version_id** | **str, none_type** |  | [optional] 
**work_item_version_number** | **int, none_type** |  | [optional] 
**step_comments** | [**[StepCommentApiModel], none_type**](StepCommentApiModel.md) |  | [optional] 
**parameters** | **{str: (str,)}, none_type** |  | [optional] 
**properties** | **{str: (str,)}, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


