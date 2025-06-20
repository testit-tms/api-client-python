# ParameterGroupsFilterApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_key_ids** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 

## Example

```python
from testit_api_client.models.parameter_groups_filter_api_model import ParameterGroupsFilterApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterGroupsFilterApiModel from a JSON string
parameter_groups_filter_api_model_instance = ParameterGroupsFilterApiModel.from_json(json)
# print the JSON string representation of the object
print(ParameterGroupsFilterApiModel.to_json())

# convert the object into a dict
parameter_groups_filter_api_model_dict = parameter_groups_filter_api_model_instance.to_dict()
# create an instance of ParameterGroupsFilterApiModel from a dict
parameter_groups_filter_api_model_from_dict = ParameterGroupsFilterApiModel.from_dict(parameter_groups_filter_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


