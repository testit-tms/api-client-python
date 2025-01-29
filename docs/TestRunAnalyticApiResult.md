# TestRunAnalyticApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_group_by_status** | [**List[TestRunGroupByStatusApiResult]**](TestRunGroupByStatusApiResult.md) |  | 
**count_group_by_status_type** | [**List[TestRunGroupByStatusTypeApiResult]**](TestRunGroupByStatusTypeApiResult.md) |  | 
**count_group_by_failure_class** | [**List[TestRunGroupByFailureClassApiResult]**](TestRunGroupByFailureClassApiResult.md) |  | 

## Example

```python
from testit_api_client.models.test_run_analytic_api_result import TestRunAnalyticApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunAnalyticApiResult from a JSON string
test_run_analytic_api_result_instance = TestRunAnalyticApiResult.from_json(json)
# print the JSON string representation of the object
print(TestRunAnalyticApiResult.to_json())

# convert the object into a dict
test_run_analytic_api_result_dict = test_run_analytic_api_result_instance.to_dict()
# create an instance of TestRunAnalyticApiResult from a dict
test_run_analytic_api_result_from_dict = TestRunAnalyticApiResult.from_dict(test_run_analytic_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


