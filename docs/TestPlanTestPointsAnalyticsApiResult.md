# TestPlanTestPointsAnalyticsApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_group_by_status** | [**List[TestPlanTestPointsStatusGroupApiResult]**](TestPlanTestPointsStatusGroupApiResult.md) |  | 
**sum_group_by_tester** | [**List[TestPlanTestPointsTesterGroupApiResult]**](TestPlanTestPointsTesterGroupApiResult.md) |  | 
**count_group_by_tester** | [**List[TestPlanTestPointsTesterGroupApiResult]**](TestPlanTestPointsTesterGroupApiResult.md) |  | 
**count_group_by_tester_and_status** | [**List[TestPlanTestPointsTesterAndStatusGroupApiResult]**](TestPlanTestPointsTesterAndStatusGroupApiResult.md) |  | 

## Example

```python
from testit_api_client.models.test_plan_test_points_analytics_api_result import TestPlanTestPointsAnalyticsApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsAnalyticsApiResult from a JSON string
test_plan_test_points_analytics_api_result_instance = TestPlanTestPointsAnalyticsApiResult.from_json(json)
# print the JSON string representation of the object
print(TestPlanTestPointsAnalyticsApiResult.to_json())

# convert the object into a dict
test_plan_test_points_analytics_api_result_dict = test_plan_test_points_analytics_api_result_instance.to_dict()
# create an instance of TestPlanTestPointsAnalyticsApiResult from a dict
test_plan_test_points_analytics_api_result_from_dict = TestPlanTestPointsAnalyticsApiResult.from_dict(test_plan_test_points_analytics_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


