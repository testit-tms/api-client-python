# ParametersFilterApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**project_ids** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.parameters_filter_api_model import ParametersFilterApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of ParametersFilterApiModel from a JSON string
parameters_filter_api_model_instance = ParametersFilterApiModel.from_json(json)
# print the JSON string representation of the object
print ParametersFilterApiModel.to_json()

# convert the object into a dict
parameters_filter_api_model_dict = parameters_filter_api_model_instance.to_dict()
# create an instance of ParametersFilterApiModel from a dict
parameters_filter_api_model_from_dict = ParametersFilterApiModel.from_dict(parameters_filter_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


