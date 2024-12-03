# TestRunExtractionModel

Rules for different level entities inclusion/exclusion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for test runs | [optional] 

## Example

```python
from testit_api_client.models.test_run_extraction_model import TestRunExtractionModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunExtractionModel from a JSON string
test_run_extraction_model_instance = TestRunExtractionModel.from_json(json)
# print the JSON string representation of the object
print(TestRunExtractionModel.to_json())

# convert the object into a dict
test_run_extraction_model_dict = test_run_extraction_model_instance.to_dict()
# create an instance of TestRunExtractionModel from a dict
test_run_extraction_model_from_dict = TestRunExtractionModel.from_dict(test_run_extraction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


