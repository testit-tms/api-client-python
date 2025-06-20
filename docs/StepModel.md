# StepModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**work_item** | [**SharedStepModel**](SharedStepModel.md) | Nested shared steps are allowed | [optional] 
**id** | **str** |  | 
**action** | **str** |  | [optional] 
**expected** | **str** |  | [optional] 
**test_data** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**work_item_id** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.step_model import StepModel

# TODO update the JSON string below
json = "{}"
# create an instance of StepModel from a JSON string
step_model_instance = StepModel.from_json(json)
# print the JSON string representation of the object
print(StepModel.to_json())

# convert the object into a dict
step_model_dict = step_model_instance.to_dict()
# create an instance of StepModel from a dict
step_model_from_dict = StepModel.from_dict(step_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


