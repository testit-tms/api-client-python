# TestResultsFilterRequest


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
from testit_api_client.models.test_results_filter_request import TestResultsFilterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsFilterRequest from a JSON string
test_results_filter_request_instance = TestResultsFilterRequest.from_json(json)
# print the JSON string representation of the object
print(TestResultsFilterRequest.to_json())

# convert the object into a dict
test_results_filter_request_dict = test_results_filter_request_instance.to_dict()
# create an instance of TestResultsFilterRequest from a dict
test_results_filter_request_from_dict = TestResultsFilterRequest.from_dict(test_results_filter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


