# TestRunAnalyticResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_group_by_status** | [**List[TestRunGroupByStatusModel]**](TestRunGroupByStatusModel.md) |  | [optional] 
**count_group_by_failure_class** | [**List[TestRunGroupByFailureClassModel]**](TestRunGroupByFailureClassModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_run_analytic_result_model import TestRunAnalyticResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunAnalyticResultModel from a JSON string
test_run_analytic_result_model_instance = TestRunAnalyticResultModel.from_json(json)
# print the JSON string representation of the object
print(TestRunAnalyticResultModel.to_json())

# convert the object into a dict
test_run_analytic_result_model_dict = test_run_analytic_result_model_instance.to_dict()
# create an instance of TestRunAnalyticResultModel from a dict
test_run_analytic_result_model_from_dict = TestRunAnalyticResultModel.from_dict(test_run_analytic_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


