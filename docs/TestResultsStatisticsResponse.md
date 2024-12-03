# TestResultsStatisticsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**TestResultsStatisticsStatuses**](TestResultsStatisticsStatuses.md) | Test results counts aggregated by outcome | [readonly] 
**failure_categories** | [**TestResultsStatisticsFailureCategories**](TestResultsStatisticsFailureCategories.md) | Test results counts aggregated by result failure categories | [readonly] 

## Example

```python
from testit_api_client.models.test_results_statistics_response import TestResultsStatisticsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsStatisticsResponse from a JSON string
test_results_statistics_response_instance = TestResultsStatisticsResponse.from_json(json)
# print the JSON string representation of the object
print(TestResultsStatisticsResponse.to_json())

# convert the object into a dict
test_results_statistics_response_dict = test_results_statistics_response_instance.to_dict()
# create an instance of TestResultsStatisticsResponse from a dict
test_results_statistics_response_from_dict = TestResultsStatisticsResponse.from_dict(test_results_statistics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


