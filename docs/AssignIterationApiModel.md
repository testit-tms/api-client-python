# AssignIterationApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**List[ParameterIterationModel]**](ParameterIterationModel.md) |  | 
**id** | **str** | Iteration identifier, must be empty for new or changed iteration | 

## Example

```python
from testit_api_client.models.assign_iteration_api_model import AssignIterationApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of AssignIterationApiModel from a JSON string
assign_iteration_api_model_instance = AssignIterationApiModel.from_json(json)
# print the JSON string representation of the object
print AssignIterationApiModel.to_json()

# convert the object into a dict
assign_iteration_api_model_dict = assign_iteration_api_model_instance.to_dict()
# create an instance of AssignIterationApiModel from a dict
assign_iteration_api_model_from_dict = AssignIterationApiModel.from_dict(assign_iteration_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


