# TestRunTestResultsPartialBulkSetModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | [**TestRunTestResultsSelectModel**](TestRunTestResultsSelectModel.md) | Object with filters and extraction parameters | [optional] 
**result_reason_ids** | **List[str]** | Unique IDs of result reasons to be assigned to test results | [optional] 
**links** | [**List[LinkPostModel]**](LinkPostModel.md) | Collection of links to be assigned to test results | [optional] 
**comment** | **str** | Comment to be added to test results | [optional] 
**attachment_ids** | **List[str]** | Unique IDs of files to be attached to test results | [optional] 

## Example

```python
from testit_api_client.models.test_run_test_results_partial_bulk_set_model import TestRunTestResultsPartialBulkSetModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunTestResultsPartialBulkSetModel from a JSON string
test_run_test_results_partial_bulk_set_model_instance = TestRunTestResultsPartialBulkSetModel.from_json(json)
# print the JSON string representation of the object
print(TestRunTestResultsPartialBulkSetModel.to_json())

# convert the object into a dict
test_run_test_results_partial_bulk_set_model_dict = test_run_test_results_partial_bulk_set_model_instance.to_dict()
# create an instance of TestRunTestResultsPartialBulkSetModel from a dict
test_run_test_results_partial_bulk_set_model_from_dict = TestRunTestResultsPartialBulkSetModel.from_dict(test_run_test_results_partial_bulk_set_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


