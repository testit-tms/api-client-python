# ParameterFilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_deleted** | **bool** | Specifies a parameter deleted status to search for | [optional] 
**name** | **str** | Specifies a parameter key name to search for | [optional] 

## Example

```python
from testit_api_client.models.parameter_filter_model import ParameterFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of ParameterFilterModel from a JSON string
parameter_filter_model_instance = ParameterFilterModel.from_json(json)
# print the JSON string representation of the object
print(ParameterFilterModel.to_json())

# convert the object into a dict
parameter_filter_model_dict = parameter_filter_model_instance.to_dict()
# create an instance of ParameterFilterModel from a dict
parameter_filter_model_from_dict = ParameterFilterModel.from_dict(parameter_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


