# ParameterShortModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**parameter_key_id** | **str** |  | 
**value** | **str** | Value of the parameter | 
**name** | **str** | Key of the parameter | 
**project_ids** | **List[str]** |  | 

## Example

```python
from testit_api_client.models.parameter_short_model import ParameterShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterShortModel from a JSON string
parameter_short_model_instance = ParameterShortModel.from_json(json)
# print the JSON string representation of the object
print ParameterShortModel.to_json()

# convert the object into a dict
parameter_short_model_dict = parameter_short_model_instance.to_dict()
# create an instance of ParameterShortModel from a dict
parameter_short_model_from_dict = ParameterShortModel.from_dict(parameter_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


