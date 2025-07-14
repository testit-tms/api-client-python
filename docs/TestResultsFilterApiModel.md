# TestResultsFilterApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration_ids** | **List[str]** | Specifies a test result configuration IDs to search for | [optional] 
**outcomes** | [**List[TestResultOutcome]**](TestResultOutcome.md) | Specifies a test result outcomes to search for | [optional] 
**status_codes** | **List[str]** | Specifies a test result status codes to search for | [optional] 
**failure_categories** | [**List[FailureCategoryModel]**](FailureCategoryModel.md) | Specifies a test result failure categories to search for | [optional] 
**namespace** | **str** | Specifies a test result namespace to search for | [optional] 
**class_name** | **str** | Specifies a test result class name to search for | [optional] 
**auto_test_global_ids** | **List[int]** | Specifies an autotest global IDs to search results for | [optional] 
**name** | **str** | Specifies an autotest name to search results for | [optional] 
**created_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test result creation date and time range to search for | [optional] 
**modified_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test result modified date and time range to search for | [optional] 
**started_on** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test result started on date and time range to search for | [optional] 
**completed_on** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) | Specifies a test result completed on date and time range to search for | [optional] 
**duration** | [**Int64RangeSelectorModel**](Int64RangeSelectorModel.md) | Specifies a test result duration range to search for | [optional] 
**result_reasons** | **List[str]** | Specifies result reasons for searching test results | [optional] 
**test_run_ids** | **List[str]** | Specifies a test result test run IDs to search for | [optional] 

## Example

```python
from testit_api_client.models.test_results_filter_api_model import TestResultsFilterApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsFilterApiModel from a JSON string
test_results_filter_api_model_instance = TestResultsFilterApiModel.from_json(json)
# print the JSON string representation of the object
print TestResultsFilterApiModel.to_json()

# convert the object into a dict
test_results_filter_api_model_dict = test_results_filter_api_model_instance.to_dict()
# create an instance of TestResultsFilterApiModel from a dict
test_results_filter_api_model_from_dict = TestResultsFilterApiModel.from_dict(test_results_filter_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


