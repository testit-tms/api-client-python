# ParameterGroupApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_key_id** | **str** |  | 
**name** | **str** |  | 
**values** | **Dict[str, str]** |  | 
**project_ids** | **List[str]** |  | 

## Example

```python
from testit_api_client.models.parameter_group_api_result import ParameterGroupApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterGroupApiResult from a JSON string
parameter_group_api_result_instance = ParameterGroupApiResult.from_json(json)
# print the JSON string representation of the object
print ParameterGroupApiResult.to_json()

# convert the object into a dict
parameter_group_api_result_dict = parameter_group_api_result_instance.to_dict()
# create an instance of ParameterGroupApiResult from a dict
parameter_group_api_result_from_dict = ParameterGroupApiResult.from_dict(parameter_group_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


