# TestResultsFilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_ids** | **List[str]** |  | [optional] 
**outcomes** | [**List[TestResultOutcome]**](TestResultOutcome.md) |  | [optional] 
**status_codes** | **List[str]** |  | [optional] 
**failure_categories** | [**List[FailureCategoryModel]**](FailureCategoryModel.md) |  | [optional] 
**namespace** | **str** |  | [optional] 
**class_name** | **str** |  | [optional] 
**auto_test_global_ids** | **List[int]** |  | [optional] 
**name** | **str** |  | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**modified_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**started_on** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**completed_on** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**duration** | [**Int64RangeSelectorModel**](Int64RangeSelectorModel.md) |  | [optional] 
**result_reasons** | **List[str]** |  | [optional] 
**test_run_ids** | **List[str]** |  | [optional] 

## Example

```python
from testit_api_client.models.test_results_filter_model import TestResultsFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsFilterModel from a JSON string
test_results_filter_model_instance = TestResultsFilterModel.from_json(json)
# print the JSON string representation of the object
print(TestResultsFilterModel.to_json())

# convert the object into a dict
test_results_filter_model_dict = test_results_filter_model_instance.to_dict()
# create an instance of TestResultsFilterModel from a dict
test_results_filter_model_from_dict = TestResultsFilterModel.from_dict(test_results_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


