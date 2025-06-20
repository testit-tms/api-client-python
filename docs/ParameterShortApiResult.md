# ParameterShortApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**parameter_key_id** | **str** |  | 
**value** | **str** | Value of the parameter | 
**name** | **str** | Key of the parameter | 

## Example

```python
from testit_api_client.models.parameter_short_api_result import ParameterShortApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterShortApiResult from a JSON string
parameter_short_api_result_instance = ParameterShortApiResult.from_json(json)
# print the JSON string representation of the object
print(ParameterShortApiResult.to_json())

# convert the object into a dict
parameter_short_api_result_dict = parameter_short_api_result_instance.to_dict()
# create an instance of ParameterShortApiResult from a dict
parameter_short_api_result_from_dict = ParameterShortApiResult.from_dict(parameter_short_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


