# ParameterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**is_deleted** | **bool** |  | 
**parameter_key_id** | **str** |  | 
**id** | **str** |  | 
**value** | **str** | Value of the parameter | 
**name** | **str** | Key of the parameter | 

## Example

```python
from testit_api_client.models.parameter_model import ParameterModel

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterModel from a JSON string
parameter_model_instance = ParameterModel.from_json(json)
# print the JSON string representation of the object
print(ParameterModel.to_json())

# convert the object into a dict
parameter_model_dict = parameter_model_instance.to_dict()
# create an instance of ParameterModel from a dict
parameter_model_from_dict = ParameterModel.from_dict(parameter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


