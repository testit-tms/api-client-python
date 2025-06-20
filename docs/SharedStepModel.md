# SharedStepModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** |  | 
**global_id** | **int** |  | 
**name** | **str** |  | 
**steps** | [**List[StepModel]**](StepModel.md) |  | 
**is_deleted** | **bool** |  | 

## Example

```python
from testit_api_client.models.shared_step_model import SharedStepModel

# TODO update the JSON string below
json = "{}"
# create an instance of SharedStepModel from a JSON string
shared_step_model_instance = SharedStepModel.from_json(json)
# print the JSON string representation of the object
print(SharedStepModel.to_json())

# convert the object into a dict
shared_step_model_dict = shared_step_model_instance.to_dict()
# create an instance of SharedStepModel from a dict
shared_step_model_from_dict = SharedStepModel.from_dict(shared_step_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


