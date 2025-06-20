# TestResultChronologyModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outcome** | **str** |  | [optional] 
**count** | **int** |  | 

## Example

```python
from testit_api_client.models.test_result_chronology_model import TestResultChronologyModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultChronologyModel from a JSON string
test_result_chronology_model_instance = TestResultChronologyModel.from_json(json)
# print the JSON string representation of the object
print(TestResultChronologyModel.to_json())

# convert the object into a dict
test_result_chronology_model_dict = test_result_chronology_model_instance.to_dict()
# create an instance of TestResultChronologyModel from a dict
test_result_chronology_model_from_dict = TestResultChronologyModel.from_dict(test_result_chronology_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


