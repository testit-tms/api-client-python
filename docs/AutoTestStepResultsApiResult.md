# AutoTestStepResultsApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**info** | **str** |  | [optional] 
**started_on** | **datetime** |  | [optional] 
**completed_on** | **datetime** |  | [optional] 
**duration** | **int** |  | [optional] 
**outcome** | [**AutoTestOutcome**](AutoTestOutcome.md) |  | [optional] 
**step_results** | [**List[AutoTestStepResultsApiResult]**](AutoTestStepResultsApiResult.md) |  | [optional] 
**attachments** | [**List[AttachmentApiResult]**](AttachmentApiResult.md) |  | [optional] 
**parameters** | **Dict[str, str]** |  | [optional] 

## Example

```python
from testit_api_client.models.auto_test_step_results_api_result import AutoTestStepResultsApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestStepResultsApiResult from a JSON string
auto_test_step_results_api_result_instance = AutoTestStepResultsApiResult.from_json(json)
# print the JSON string representation of the object
print(AutoTestStepResultsApiResult.to_json())

# convert the object into a dict
auto_test_step_results_api_result_dict = auto_test_step_results_api_result_instance.to_dict()
# create an instance of AutoTestStepResultsApiResult from a dict
auto_test_step_results_api_result_from_dict = AutoTestStepResultsApiResult.from_dict(auto_test_step_results_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


