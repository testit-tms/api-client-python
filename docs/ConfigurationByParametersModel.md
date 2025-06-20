# ConfigurationByParametersModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | This property is used to link configuration with project | 
**parameter_ids** | **List[str]** |  | 

## Example

```python
from testit_api_client.models.configuration_by_parameters_model import ConfigurationByParametersModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationByParametersModel from a JSON string
configuration_by_parameters_model_instance = ConfigurationByParametersModel.from_json(json)
# print the JSON string representation of the object
print(ConfigurationByParametersModel.to_json())

# convert the object into a dict
configuration_by_parameters_model_dict = configuration_by_parameters_model_instance.to_dict()
# create an instance of ConfigurationByParametersModel from a dict
configuration_by_parameters_model_from_dict = ConfigurationByParametersModel.from_dict(configuration_by_parameters_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


