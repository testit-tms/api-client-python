# StepPutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**action** | **str** |  | [optional] 
**expected** | **str** |  | [optional] 
**test_data** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**work_item_id** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.step_put_model import StepPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of StepPutModel from a JSON string
step_put_model_instance = StepPutModel.from_json(json)
# print the JSON string representation of the object
print(StepPutModel.to_json())

# convert the object into a dict
step_put_model_dict = step_put_model_instance.to_dict()
# create an instance of StepPutModel from a dict
step_put_model_from_dict = StepPutModel.from_dict(step_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


