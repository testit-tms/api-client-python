# ParameterGroupModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**values** | **Dict[str, str]** |  | 
**parameter_key_id** | **str** |  | 

## Example

```python
from testit_api_client.models.parameter_group_model import ParameterGroupModel

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterGroupModel from a JSON string
parameter_group_model_instance = ParameterGroupModel.from_json(json)
# print the JSON string representation of the object
print ParameterGroupModel.to_json()

# convert the object into a dict
parameter_group_model_dict = parameter_group_model_instance.to_dict()
# create an instance of ParameterGroupModel from a dict
parameter_group_model_from_dict = ParameterGroupModel.from_dict(parameter_group_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


