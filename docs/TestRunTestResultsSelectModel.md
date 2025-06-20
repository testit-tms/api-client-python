# TestRunTestResultsSelectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TestResultsLocalFilterModel**](TestResultsLocalFilterModel.md) | Collection of filters to apply to search | [optional] 
**test_result_ids_extraction_model** | [**GuidExtractionModel**](GuidExtractionModel.md) | Rules to include and exclude certain entities in result | [optional] 

## Example

```python
from testit_api_client.models.test_run_test_results_select_model import TestRunTestResultsSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunTestResultsSelectModel from a JSON string
test_run_test_results_select_model_instance = TestRunTestResultsSelectModel.from_json(json)
# print the JSON string representation of the object
print(TestRunTestResultsSelectModel.to_json())

# convert the object into a dict
test_run_test_results_select_model_dict = test_run_test_results_select_model_instance.to_dict()
# create an instance of TestRunTestResultsSelectModel from a dict
test_run_test_results_select_model_from_dict = TestRunTestResultsSelectModel.from_dict(test_run_test_results_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


