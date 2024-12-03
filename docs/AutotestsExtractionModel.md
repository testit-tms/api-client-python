# AutotestsExtractionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for autotests | [optional] 

## Example

```python
from testit_api_client.models.autotests_extraction_model import AutotestsExtractionModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutotestsExtractionModel from a JSON string
autotests_extraction_model_instance = AutotestsExtractionModel.from_json(json)
# print the JSON string representation of the object
print(AutotestsExtractionModel.to_json())

# convert the object into a dict
autotests_extraction_model_dict = autotests_extraction_model_instance.to_dict()
# create an instance of AutotestsExtractionModel from a dict
autotests_extraction_model_from_dict = AutotestsExtractionModel.from_dict(autotests_extraction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


