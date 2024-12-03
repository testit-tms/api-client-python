# IterationModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**parameters** | [**List[ParameterShortModel]**](ParameterShortModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.iteration_model import IterationModel

# TODO update the JSON string below
json = "{}"
# create an instance of IterationModel from a JSON string
iteration_model_instance = IterationModel.from_json(json)
# print the JSON string representation of the object
print(IterationModel.to_json())

# convert the object into a dict
iteration_model_dict = iteration_model_instance.to_dict()
# create an instance of IterationModel from a dict
iteration_model_from_dict = IterationModel.from_dict(iteration_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


