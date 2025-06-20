# ConfigurationExtractionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for configurations | [optional] 
**project_ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for projects | [optional] 

## Example

```python
from testit_api_client.models.configuration_extraction_model import ConfigurationExtractionModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationExtractionModel from a JSON string
configuration_extraction_model_instance = ConfigurationExtractionModel.from_json(json)
# print the JSON string representation of the object
print(ConfigurationExtractionModel.to_json())

# convert the object into a dict
configuration_extraction_model_dict = configuration_extraction_model_instance.to_dict()
# create an instance of ConfigurationExtractionModel from a dict
configuration_extraction_model_from_dict = ConfigurationExtractionModel.from_dict(configuration_extraction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


