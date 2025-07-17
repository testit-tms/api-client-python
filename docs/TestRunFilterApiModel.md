# TestRunFilterApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_ids** | **List[str]** | Specifies a test run project IDs to search for | [optional] 
**name** | **str** | Specifies test run name | [optional] 
**states** | [**List[TestRunState]**](TestRunState.md) | Specifies a test run states to search for | [optional] 
**status_codes** | **List[str]** | Specifies a test run status codes to search for | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test run range of created date to search for | [optional] 
**started_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test run range of started date to search for | [optional] 
**created_by_ids** | **List[str]** | Specifies a test run creator IDs to search for | [optional] 
**modified_by_ids** | **List[str]** | Specifies a test run last editor IDs to search for | [optional] 
**is_deleted** | **bool** | Specifies a test run deleted status to search for | [optional] 
**auto_tests_count** | [**Int32RangeSelectorModel**](Int32RangeSelectorModel.md) | Number of autoTests run in the test run | [optional] 
**test_results_outcome** | [**List[TestResultOutcome]**](TestResultOutcome.md) | Specifies test results outcomes | [optional] 
**test_results_status_codes** | **List[str]** | Specifies test results status codes | [optional] 
**failure_category** | [**List[FailureCategory]**](FailureCategory.md) | Specifies failure categories | [optional] 
**completed_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test run range of completed date to search for | [optional] 
**test_results_configuration_ids** | **List[str]** | Specifies a test result configuration IDs to search for | [optional] 

## Example

```python
from testit_api_client.models.test_run_filter_api_model import TestRunFilterApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunFilterApiModel from a JSON string
test_run_filter_api_model_instance = TestRunFilterApiModel.from_json(json)
# print the JSON string representation of the object
print TestRunFilterApiModel.to_json()

# convert the object into a dict
test_run_filter_api_model_dict = test_run_filter_api_model_instance.to_dict()
# create an instance of TestRunFilterApiModel from a dict
test_run_filter_api_model_from_dict = TestRunFilterApiModel.from_dict(test_run_filter_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


