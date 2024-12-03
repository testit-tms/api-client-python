# StepResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **str** |  | 
**outcome** | **str** |  | 
**shared_step_version_id** | **str** |  | [optional] 
**shared_step_results** | [**List[SharedStepResult]**](SharedStepResult.md) |  | [optional] 
**comment** | [**StepComment**](StepComment.md) |  | [optional] 

## Example

```python
from testit_api_client.models.step_result import StepResult

# TODO update the JSON string below
json = "{}"
# create an instance of StepResult from a JSON string
step_result_instance = StepResult.from_json(json)
# print the JSON string representation of the object
print(StepResult.to_json())

# convert the object into a dict
step_result_dict = step_result_instance.to_dict()
# create an instance of StepResult from a dict
step_result_from_dict = StepResult.from_dict(step_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


