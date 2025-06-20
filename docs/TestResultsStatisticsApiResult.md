# TestResultsStatisticsApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**TestResultsStatisticsStatusesApiResult**](TestResultsStatisticsStatusesApiResult.md) | Test results counts aggregated by outcome | [readonly] 
**failure_categories** | [**TestResultsStatisticsFailureCategoriesApiResult**](TestResultsStatisticsFailureCategoriesApiResult.md) | Test results counts aggregated by result failure categories | [readonly] 

## Example

```python
from testit_api_client.models.test_results_statistics_api_result import TestResultsStatisticsApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsStatisticsApiResult from a JSON string
test_results_statistics_api_result_instance = TestResultsStatisticsApiResult.from_json(json)
# print the JSON string representation of the object
print TestResultsStatisticsApiResult.to_json()

# convert the object into a dict
test_results_statistics_api_result_dict = test_results_statistics_api_result_instance.to_dict()
# create an instance of TestResultsStatisticsApiResult from a dict
test_results_statistics_api_result_from_dict = TestResultsStatisticsApiResult.from_dict(test_results_statistics_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


