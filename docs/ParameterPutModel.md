# ParameterPutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**value** | **str** | Value of the parameter | 
**name** | **str** | Key of the parameter | 

## Example

```python
from testit_api_client.models.parameter_put_model import ParameterPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterPutModel from a JSON string
parameter_put_model_instance = ParameterPutModel.from_json(json)
# print the JSON string representation of the object
print(ParameterPutModel.to_json())

# convert the object into a dict
parameter_put_model_dict = parameter_put_model_instance.to_dict()
# create an instance of ParameterPutModel from a dict
parameter_put_model_from_dict = ParameterPutModel.from_dict(parameter_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


