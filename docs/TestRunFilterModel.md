# TestRunFilterModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **List[str]** | Specifies a test run project IDs to search for | [optional] 
**name** | **str** | Specifies test run name | [optional] 
**states** | [**List[TestRunState]**](TestRunState.md) | Specifies a test run states to search for | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test run range of created date to search for | [optional] 
**started_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test run range of started date to search for | [optional] 
**created_by_ids** | **List[str]** | Specifies a test run creator IDs to search for | [optional] 
**modified_by_ids** | **List[str]** | Specifies a test run last editor IDs to search for | [optional] 
**is_deleted** | **bool** | Specifies a test run deleted status to search for | [optional] 
**auto_tests_count** | [**Int32RangeSelectorModel**](Int32RangeSelectorModel.md) | Number of autoTests run in the test run | [optional] 
**test_results_outcome** | [**List[TestResultOutcome]**](TestResultOutcome.md) | Specifies test results outcomes | [optional] 
**failure_category** | [**List[FailureCategoryModel]**](FailureCategoryModel.md) | Specifies failure categories | [optional] 
**completed_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test run range of completed date to search for | [optional] 
**test_results_configuration_ids** | **List[str]** | Specifies a test result configuration IDs to search for | [optional] 

## Example

```python
from testit_api_client.models.test_run_filter_model import TestRunFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunFilterModel from a JSON string
test_run_filter_model_instance = TestRunFilterModel.from_json(json)
# print the JSON string representation of the object
print(TestRunFilterModel.to_json())

# convert the object into a dict
test_run_filter_model_dict = test_run_filter_model_instance.to_dict()
# create an instance of TestRunFilterModel from a dict
test_run_filter_model_from_dict = TestRunFilterModel.from_dict(test_run_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


