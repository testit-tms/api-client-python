# TestResultsStatisticsFailureCategories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**infrastructure_defect** | **int** | Number of test results which outcomes were caused by some infrastructure defect | 
**product_defect** | **int** | Number of test results which outcomes were caused by some tested product defect | 
**test_defect** | **int** | Number of test results which outcomes were caused by test itself | 

## Example

```python
from testit_api_client.models.test_results_statistics_failure_categories import TestResultsStatisticsFailureCategories

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsStatisticsFailureCategories from a JSON string
test_results_statistics_failure_categories_instance = TestResultsStatisticsFailureCategories.from_json(json)
# print the JSON string representation of the object
print(TestResultsStatisticsFailureCategories.to_json())

# convert the object into a dict
test_results_statistics_failure_categories_dict = test_results_statistics_failure_categories_instance.to_dict()
# create an instance of TestResultsStatisticsFailureCategories from a dict
test_results_statistics_failure_categories_from_dict = TestResultsStatisticsFailureCategories.from_dict(test_results_statistics_failure_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


