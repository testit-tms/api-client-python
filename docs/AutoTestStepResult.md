# AutoTestStepResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str, none_type** | The name of the step. | [optional] 
**description** | **str, none_type** | Description of the step result. | [optional] 
**info** | **str, none_type** | Extended description of the step result. | [optional] 
**started_on** | **datetime, none_type** | Step start date. | [optional] 
**completed_on** | **datetime, none_type** | Step end date. | [optional] 
**duration** | **int, none_type** | Expected or actual duration of the test run execution in milliseconds. | [optional] 
**outcome** | [**AvailableTestResultOutcome**](AvailableTestResultOutcome.md) |  | [optional] 
**step_results** | [**[AutoTestStepResult], none_type**](AutoTestStepResult.md) | Nested step results. The maximum nesting level is 15. | [optional] 
**attachments** | [**[AttachmentApiResult], none_type**](AttachmentApiResult.md) | /// &lt;summary&gt;  Specifies an attachment GUID. Multiple values can be sent.  &lt;/summary&gt; | [optional] 
**parameters** | **{str: (str,)}, none_type** | \&quot;&lt;b&gt;parameter&lt;/b&gt;\&quot;: \&quot;&lt;b&gt;value&lt;/b&gt;\&quot; pair with arbitrary custom parameters. Multiple parameters can be sent. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


