# TestPointAnalyticResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_group_by_status** | [**List[TestPlanGroupByStatus]**](TestPlanGroupByStatus.md) |  | 
**sum_group_by_tester** | [**List[TestPlanGroupByTester]**](TestPlanGroupByTester.md) |  | 
**count_group_by_tester** | [**List[TestPlanGroupByTester]**](TestPlanGroupByTester.md) |  | 
**count_group_by_test_suite** | [**List[TestPlanGroupByTestSuite]**](TestPlanGroupByTestSuite.md) |  | 
**count_group_by_tester_and_status** | [**List[TestPlanGroupByTesterAndStatus]**](TestPlanGroupByTesterAndStatus.md) |  | 
**count_group_by_status_code** | [**List[TestPlanGroupByStatusCode]**](TestPlanGroupByStatusCode.md) |  | 
**count_group_by_tester_and_status_code** | [**List[TestPlanGroupByTesterAndStatusCode]**](TestPlanGroupByTesterAndStatusCode.md) |  | 

## Example

```python
from testit_api_client.models.test_point_analytic_result import TestPointAnalyticResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPointAnalyticResult from a JSON string
test_point_analytic_result_instance = TestPointAnalyticResult.from_json(json)
# print the JSON string representation of the object
print TestPointAnalyticResult.to_json()

# convert the object into a dict
test_point_analytic_result_dict = test_point_analytic_result_instance.to_dict()
# create an instance of TestPointAnalyticResult from a dict
test_point_analytic_result_from_dict = TestPointAnalyticResult.from_dict(test_point_analytic_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


