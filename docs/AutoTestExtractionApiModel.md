# AutoTestExtractionApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for autotests | [optional] 

## Example

```python
from testit_api_client.models.auto_test_extraction_api_model import AutoTestExtractionApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestExtractionApiModel from a JSON string
auto_test_extraction_api_model_instance = AutoTestExtractionApiModel.from_json(json)
# print the JSON string representation of the object
print AutoTestExtractionApiModel.to_json()

# convert the object into a dict
auto_test_extraction_api_model_dict = auto_test_extraction_api_model_instance.to_dict()
# create an instance of AutoTestExtractionApiModel from a dict
auto_test_extraction_api_model_from_dict = AutoTestExtractionApiModel.from_dict(auto_test_extraction_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


