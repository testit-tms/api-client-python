# TestResultExtractionModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**test_result_ids** | [**GuidExtractionModel**](GuidExtractionModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_result_extraction_model import TestResultExtractionModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultExtractionModel from a JSON string
test_result_extraction_model_instance = TestResultExtractionModel.from_json(json)
# print the JSON string representation of the object
print(TestResultExtractionModel.to_json())

# convert the object into a dict
test_result_extraction_model_dict = test_result_extraction_model_instance.to_dict()
# create an instance of TestResultExtractionModel from a dict
test_result_extraction_model_from_dict = TestResultExtractionModel.from_dict(test_result_extraction_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


