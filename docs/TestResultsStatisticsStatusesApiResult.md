# TestResultsStatisticsStatusesApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_progress** | **int** | Number of test results which is running currently | 
**passed** | **int** | Number of test results which successfully passed | 
**failed** | **int** | Number of test results which failed with an error | 
**skipped** | **int** | Number of test results which did not run and were skipped | 
**blocked** | **int** | Number of test results which cannot be launched | 
**incomplete** | **int** | Number of test results which are incomplete | 

## Example

```python
from testit_api_client.models.test_results_statistics_statuses_api_result import TestResultsStatisticsStatusesApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsStatisticsStatusesApiResult from a JSON string
test_results_statistics_statuses_api_result_instance = TestResultsStatisticsStatusesApiResult.from_json(json)
# print the JSON string representation of the object
print TestResultsStatisticsStatusesApiResult.to_json()

# convert the object into a dict
test_results_statistics_statuses_api_result_dict = test_results_statistics_statuses_api_result_instance.to_dict()
# create an instance of TestResultsStatisticsStatusesApiResult from a dict
test_results_statistics_statuses_api_result_from_dict = TestResultsStatisticsStatusesApiResult.from_dict(test_results_statistics_statuses_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


