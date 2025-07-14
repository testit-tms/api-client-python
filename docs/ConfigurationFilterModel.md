# ConfigurationFilterModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **List[str]** | Collection of identifiers of projects from which configurations will be taken | [optional] 
**name** | **str** | Filter to search by name (case-insensitive, partial match) | [optional] 
**is_deleted** | **bool** | Is configurations deleted or existing | [optional] 
**global_ids** | **List[int]** | Collection of global (integer) identifiers to filter configurations | [optional] 

## Example

```python
from testit_api_client.models.configuration_filter_model import ConfigurationFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationFilterModel from a JSON string
configuration_filter_model_instance = ConfigurationFilterModel.from_json(json)
# print the JSON string representation of the object
print ConfigurationFilterModel.to_json()

# convert the object into a dict
configuration_filter_model_dict = configuration_filter_model_instance.to_dict()
# create an instance of ConfigurationFilterModel from a dict
configuration_filter_model_from_dict = ConfigurationFilterModel.from_dict(configuration_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


