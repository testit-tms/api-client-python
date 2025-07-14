# TestRunExtractionApiModel

Rules for different level entities inclusion/exclusion

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for test runs | [optional] 

## Example

```python
from testit_api_client.models.test_run_extraction_api_model import TestRunExtractionApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunExtractionApiModel from a JSON string
test_run_extraction_api_model_instance = TestRunExtractionApiModel.from_json(json)
# print the JSON string representation of the object
print TestRunExtractionApiModel.to_json()

# convert the object into a dict
test_run_extraction_api_model_dict = test_run_extraction_api_model_instance.to_dict()
# create an instance of TestRunExtractionApiModel from a dict
test_run_extraction_api_model_from_dict = TestRunExtractionApiModel.from_dict(test_run_extraction_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


