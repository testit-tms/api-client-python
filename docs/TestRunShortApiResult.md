# TestRunShortApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test run | 
**name** | **str** | Name of the test run | 
**state** | [**TestRunState**](TestRunState.md) | Current state of the test run | 
**status** | [**TestStatusApiResult**](TestStatusApiResult.md) | Current status of the test run | 
**created_date** | **datetime** | Date when the test run was created | 
**started_date** | **datetime** | Date when the test run was started | [optional] 
**completed_date** | **datetime** | Completion date of the test run | [optional] 
**created_by_id** | **str** | Unique ID of user who created the test run | 
**modified_by_id** | **str** | Unique ID of user who modified the test run last time | [optional] 
**is_deleted** | **bool** | Is the test run is deleted | 
**auto_tests_count** | **int** | Number of AutoTests run in the test run | 
**statistics** | [**TestResultsStatisticsApiResult**](TestResultsStatisticsApiResult.md) | Statistics of the test run | 
**test_results_configurations** | [**List[ConfigurationShortApiResult]**](ConfigurationShortApiResult.md) | Test results configurations | 

## Example

```python
from testit_api_client.models.test_run_short_api_result import TestRunShortApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunShortApiResult from a JSON string
test_run_short_api_result_instance = TestRunShortApiResult.from_json(json)
# print the JSON string representation of the object
print(TestRunShortApiResult.to_json())

# convert the object into a dict
test_run_short_api_result_dict = test_run_short_api_result_instance.to_dict()
# create an instance of TestRunShortApiResult from a dict
test_run_short_api_result_from_dict = TestRunShortApiResult.from_dict(test_run_short_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


