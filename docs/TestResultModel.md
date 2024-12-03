# TestResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**test_point** | [**TestPointPutModel**](TestPointPutModel.md) |  | [optional] 
**auto_test** | [**AutoTestModel**](AutoTestModel.md) |  | [optional] 
**auto_test_step_results** | [**List[AttachmentModelAutoTestStepResultsModel]**](AttachmentModelAutoTestStepResultsModel.md) |  | [optional] 
**setup_results** | [**List[AttachmentModelAutoTestStepResultsModel]**](AttachmentModelAutoTestStepResultsModel.md) |  | [optional] 
**teardown_results** | [**List[AttachmentModelAutoTestStepResultsModel]**](AttachmentModelAutoTestStepResultsModel.md) |  | [optional] 
**work_item_version_id** | **str** |  | 
**work_item_version_number** | **int** |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 
**properties** | **Dict[str, str]** |  | [optional] 
**id** | **str** |  | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**step_comments** | [**List[StepCommentModel]**](StepCommentModel.md) |  | [optional] 
**failure_class_ids** | **List[str]** |  | 
**outcome** | [**TestResultOutcome**](TestResultOutcome.md) |  | [optional] 
**status** | [**TestStatusModel**](TestStatusModel.md) |  | [optional] 
**comment** | **str** |  | [optional] 
**links** | [**List[LinkModel]**](LinkModel.md) |  | [optional] 
**step_results** | [**List[StepResultModel]**](StepResultModel.md) |  | [optional] 
**attachments** | [**List[AttachmentModel]**](AttachmentModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_result_model import TestResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultModel from a JSON string
test_result_model_instance = TestResultModel.from_json(json)
# print the JSON string representation of the object
print(TestResultModel.to_json())

# convert the object into a dict
test_result_model_dict = test_result_model_instance.to_dict()
# create an instance of TestResultModel from a dict
test_result_model_from_dict = TestResultModel.from_dict(test_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


