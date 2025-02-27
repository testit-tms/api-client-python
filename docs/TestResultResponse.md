# TestResultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**step_comments** | [**List[StepCommentApiModel]**](StepCommentApiModel.md) |  | [optional] 
**failure_class_ids** | **List[str]** |  | 
**outcome** | [**TestResultOutcome**](TestResultOutcome.md) |  | [optional] 
**status** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**step_results** | [**List[StepResultApiModel]**](StepResultApiModel.md) |  | [optional] 
**attachments** | [**List[AttachmentApiResult]**](AttachmentApiResult.md) |  | [optional] 
**auto_test_id** | **str** |  | [optional] 
**configuration_id** | **str** |  | 
**started_on** | **datetime** |  | [optional] 
**completed_on** | **datetime** |  | [optional] 
**duration_in_ms** | **int** |  | [optional] 
**traces** | **str** |  | [optional] 
**failure_type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**run_by_user_id** | **str** |  | [optional] 
**stopped_by_user_id** | **str** |  | [optional] 
**test_point_id** | **str** |  | 
**test_run_id** | **str** |  | 
**test_point** | [**TestPoint**](TestPoint.md) |  | [optional] 
**auto_test** | [**AutoTest**](AutoTest.md) |  | [optional] 
**auto_test_step_results** | [**List[AutoTestStepResult]**](AutoTestStepResult.md) |  | [optional] 
**setup_results** | [**List[AutoTestStepResult]**](AutoTestStepResult.md) |  | [optional] 
**teardown_results** | [**List[AutoTestStepResult]**](AutoTestStepResult.md) |  | [optional] 
**work_item_version_id** | **str** |  | 
**work_item_version_number** | **int** |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 

## Example

```python
from testit_api_client.models.test_result_response import TestResultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultResponse from a JSON string
test_result_response_instance = TestResultResponse.from_json(json)
# print the JSON string representation of the object
print(TestResultResponse.to_json())

# convert the object into a dict
test_result_response_dict = test_result_response_instance.to_dict()
# create an instance of TestResultResponse from a dict
test_result_response_from_dict = TestResultResponse.from_dict(test_result_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


