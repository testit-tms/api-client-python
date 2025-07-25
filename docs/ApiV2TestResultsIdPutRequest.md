# ApiV2TestResultsIdPutRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure_class_ids** | **[str], none_type** |  | [optional] 
**outcome** | [**TestResultOutcome**](TestResultOutcome.md) |  | [optional] 
**status_code** | **str, none_type** |  | [optional] 
**comment** | **str, none_type** |  | [optional] 
**links** | [**[Link], none_type**](Link.md) |  | [optional] 
**step_results** | [**[StepResultApiModel], none_type**](StepResultApiModel.md) |  | [optional] 
**attachments** | [**[AttachmentUpdateRequest], none_type**](AttachmentUpdateRequest.md) |  | [optional] 
**duration_in_ms** | **int, none_type** |  | [optional] 
**duration** | **int, none_type** |  | [optional] 
**step_comments** | [**[TestResultStepCommentUpdateRequest], none_type**](TestResultStepCommentUpdateRequest.md) |  | [optional] 
**setup_results** | [**[AutoTestStepResultUpdateRequest], none_type**](AutoTestStepResultUpdateRequest.md) |  | [optional] 
**teardown_results** | [**[AutoTestStepResultUpdateRequest], none_type**](AutoTestStepResultUpdateRequest.md) |  | [optional] 
**message** | **str, none_type** |  | [optional] 
**trace** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


