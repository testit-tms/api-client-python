# TestResultsStatisticsStatuses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**in_progress** | **int** | Number of test results which is running currently | 
**passed** | **int** | Number of test results which successfully passed | 
**failed** | **int** | Number of test results which failed with an error | 
**skipped** | **int** | Number of test results which did not run and were skipped | 
**blocked** | **int** | Number of test results which cannot be launched | 

## Example

```python
from testit_api_client.models.test_results_statistics_statuses import TestResultsStatisticsStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsStatisticsStatuses from a JSON string
test_results_statistics_statuses_instance = TestResultsStatisticsStatuses.from_json(json)
# print the JSON string representation of the object
print(TestResultsStatisticsStatuses.to_json())

# convert the object into a dict
test_results_statistics_statuses_dict = test_results_statistics_statuses_instance.to_dict()
# create an instance of TestResultsStatisticsStatuses from a dict
test_results_statistics_statuses_from_dict = TestResultsStatisticsStatuses.from_dict(test_results_statistics_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


