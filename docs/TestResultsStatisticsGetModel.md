# TestResultsStatisticsGetModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**statuses** | [**TestRunStatisticsStatusesGetModel**](TestRunStatisticsStatusesGetModel.md) | Test results counts aggregated by outcome | [readonly] 
**failure_categories** | [**TestRunStatisticsErrorCategoriesGetModel**](TestRunStatisticsErrorCategoriesGetModel.md) | Test results counts aggregated by result failure categories | [readonly] 

## Example

```python
from testit_api_client.models.test_results_statistics_get_model import TestResultsStatisticsGetModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestResultsStatisticsGetModel from a JSON string
test_results_statistics_get_model_instance = TestResultsStatisticsGetModel.from_json(json)
# print the JSON string representation of the object
print(TestResultsStatisticsGetModel.to_json())

# convert the object into a dict
test_results_statistics_get_model_dict = test_results_statistics_get_model_instance.to_dict()
# create an instance of TestResultsStatisticsGetModel from a dict
test_results_statistics_get_model_from_dict = TestResultsStatisticsGetModel.from_dict(test_results_statistics_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


