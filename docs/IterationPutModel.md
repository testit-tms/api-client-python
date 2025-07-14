# IterationPutModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**List[ParameterIterationModel]**](ParameterIterationModel.md) |  | 
**id** | **str** |  | 

## Example

```python
from testit_api_client.models.iteration_put_model import IterationPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of IterationPutModel from a JSON string
iteration_put_model_instance = IterationPutModel.from_json(json)
# print the JSON string representation of the object
print IterationPutModel.to_json()

# convert the object into a dict
iteration_put_model_dict = iteration_put_model_instance.to_dict()
# create an instance of IterationPutModel from a dict
iteration_put_model_from_dict = IterationPutModel.from_dict(iteration_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


