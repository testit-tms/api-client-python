# TestRunStatisticsStatusesGetModel


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
from testit_api_client.models.test_run_statistics_statuses_get_model import TestRunStatisticsStatusesGetModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunStatisticsStatusesGetModel from a JSON string
test_run_statistics_statuses_get_model_instance = TestRunStatisticsStatusesGetModel.from_json(json)
# print the JSON string representation of the object
print(TestRunStatisticsStatusesGetModel.to_json())

# convert the object into a dict
test_run_statistics_statuses_get_model_dict = test_run_statistics_statuses_get_model_instance.to_dict()
# create an instance of TestRunStatisticsStatusesGetModel from a dict
test_run_statistics_statuses_get_model_from_dict = TestRunStatisticsStatusesGetModel.from_dict(test_run_statistics_statuses_get_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


