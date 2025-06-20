# TestResultsStatisticsFailureCategoriesApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infrastructure_defect** | **int** | Number of test results which outcomes were caused by some infrastructure defect | 
**product_defect** | **int** | Number of test results which outcomes were caused by some tested product defect | 
**test_defect** | **int** | Number of test results which outcomes were caused by test itself | 

## Example

```python
from testit_api_client.models.test_results_statistics_failure_categories_api_result import TestResultsStatisticsFailureCategoriesApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsStatisticsFailureCategoriesApiResult from a JSON string
test_results_statistics_failure_categories_api_result_instance = TestResultsStatisticsFailureCategoriesApiResult.from_json(json)
# print the JSON string representation of the object
print(TestResultsStatisticsFailureCategoriesApiResult.to_json())

# convert the object into a dict
test_results_statistics_failure_categories_api_result_dict = test_results_statistics_failure_categories_api_result_instance.to_dict()
# create an instance of TestResultsStatisticsFailureCategoriesApiResult from a dict
test_results_statistics_failure_categories_api_result_from_dict = TestResultsStatisticsFailureCategoriesApiResult.from_dict(test_results_statistics_failure_categories_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


