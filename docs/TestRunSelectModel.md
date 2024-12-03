# TestRunSelectModel

Model containing options to filter test runs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TestRunFilterModel**](TestRunFilterModel.md) |  | 
**extraction_model** | [**TestRunExtractionModel**](TestRunExtractionModel.md) | Rules for different level entities inclusion/exclusion | 

## Example

```python
from testit_api_client.models.test_run_select_model import TestRunSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunSelectModel from a JSON string
test_run_select_model_instance = TestRunSelectModel.from_json(json)
# print the JSON string representation of the object
print(TestRunSelectModel.to_json())

# convert the object into a dict
test_run_select_model_dict = test_run_select_model_instance.to_dict()
# create an instance of TestRunSelectModel from a dict
test_run_select_model_from_dict = TestRunSelectModel.from_dict(test_run_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


