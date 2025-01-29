# TestResultApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**started_on** | **datetime** |  | [optional] 
**completed_on** | **datetime** |  | [optional] 
**duration_in_ms** | **int** |  | [optional] 
**traces** | **str** |  | [optional] 
**failure_type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**run_by_user_id** | **str** |  | [optional] 
**stopped_by_user_id** | **str** |  | [optional] 
**outcome** | **str** |  | 
**auto_test_id** | **str** |  | [optional] 
**test_point_id** | **str** |  | [optional] 
**test_run_id** | **str** |  | 
**configuration_id** | **str** |  | 
**status** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | 
**test_point** | [**TestPointShortApiResult**](TestPointShortApiResult.md) |  | [optional] 
**auto_test** | [**AutoTestModel**](AutoTestModel.md) |  | [optional] 
**auto_test_step_results** | [**List[AutoTestStepResultsApiResult]**](AutoTestStepResultsApiResult.md) |  | [optional] 
**setup_results** | [**List[AutoTestStepResultsApiResult]**](AutoTestStepResultsApiResult.md) |  | [optional] 
**teardown_results** | [**List[AutoTestStepResultsApiResult]**](AutoTestStepResultsApiResult.md) |  | [optional] 
**work_item_version_id** | **str** |  | [optional] 
**work_item_version_number** | **int** |  | [optional] 
**attachments** | [**List[AttachmentApiResult]**](AttachmentApiResult.md) |  | 
**links** | [**List[LinkApiResult]**](LinkApiResult.md) |  | 
**failure_classes** | [**List[TestResultFailureClassApiResult]**](TestResultFailureClassApiResult.md) |  | 
**step_comments** | [**List[StepCommentApiResult]**](StepCommentApiResult.md) |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**is_deleted** | **bool** |  | 

## Example

```python
from testit_api_client.models.test_result_api_result import TestResultApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultApiResult from a JSON string
test_result_api_result_instance = TestResultApiResult.from_json(json)
# print the JSON string representation of the object
print(TestResultApiResult.to_json())

# convert the object into a dict
test_result_api_result_dict = test_result_api_result_instance.to_dict()
# create an instance of TestResultApiResult from a dict
test_result_api_result_from_dict = TestResultApiResult.from_dict(test_result_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


