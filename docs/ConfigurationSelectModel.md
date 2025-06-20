# ConfigurationSelectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ConfigurationFilterModel**](ConfigurationFilterModel.md) | Configuration filters collection | [optional] 
**extraction_model** | [**ConfigurationExtractionModel**](ConfigurationExtractionModel.md) | Rules for configurations extraction | [optional] 

## Example

```python
from testit_api_client.models.configuration_select_model import ConfigurationSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationSelectModel from a JSON string
configuration_select_model_instance = ConfigurationSelectModel.from_json(json)
# print the JSON string representation of the object
print(ConfigurationSelectModel.to_json())

# convert the object into a dict
configuration_select_model_dict = configuration_select_model_instance.to_dict()
# create an instance of ConfigurationSelectModel from a dict
configuration_select_model_from_dict = ConfigurationSelectModel.from_dict(configuration_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


