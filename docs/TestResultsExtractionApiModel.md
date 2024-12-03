# TestResultsExtractionApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Set of extracted test result IDs | [optional] 

## Example

```python
from testit_api_client.models.test_results_extraction_api_model import TestResultsExtractionApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsExtractionApiModel from a JSON string
test_results_extraction_api_model_instance = TestResultsExtractionApiModel.from_json(json)
# print the JSON string representation of the object
print(TestResultsExtractionApiModel.to_json())

# convert the object into a dict
test_results_extraction_api_model_dict = test_results_extraction_api_model_instance.to_dict()
# create an instance of TestResultsExtractionApiModel from a dict
test_results_extraction_api_model_from_dict = TestResultsExtractionApiModel.from_dict(test_results_extraction_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


