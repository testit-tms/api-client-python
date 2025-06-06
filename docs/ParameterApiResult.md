# ParameterApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**parameter_key_id** | **str** |  | 
**name** | **str** |  | 
**value** | **str** |  | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**modified_date** | **datetime** |  | [optional] 
**modified_by_id** | **str** |  | [optional] 
**is_deleted** | **bool** |  | 

## Example

```python
from testit_api_client.models.parameter_api_result import ParameterApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterApiResult from a JSON string
parameter_api_result_instance = ParameterApiResult.from_json(json)
# print the JSON string representation of the object
print(ParameterApiResult.to_json())

# convert the object into a dict
parameter_api_result_dict = parameter_api_result_instance.to_dict()
# create an instance of ParameterApiResult from a dict
parameter_api_result_from_dict = ParameterApiResult.from_dict(parameter_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


