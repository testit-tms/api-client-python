# StepResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **str** |  | 
**outcome** | **str** |  | 
**shared_step_version_id** | **str** |  | [optional] 
**shared_step_results** | [**List[SharedStepResultModel]**](SharedStepResultModel.md) |  | [optional] 
**comment** | [**StepCommentModel**](StepCommentModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.step_result_model import StepResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of StepResultModel from a JSON string
step_result_model_instance = StepResultModel.from_json(json)
# print the JSON string representation of the object
print(StepResultModel.to_json())

# convert the object into a dict
step_result_model_dict = step_result_model_instance.to_dict()
# create an instance of StepResultModel from a dict
step_result_model_from_dict = StepResultModel.from_dict(step_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


