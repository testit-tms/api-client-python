# TestPlanTestPointsSearchStatusCountersApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automated_test_points_count** | **int** |  | 
**automated_test_points_in_progress_count** | **int** |  | 
**automated_test_points_failed_count** | **int** |  | 
**manual_test_points_count** | **int** |  | 

## Example

```python
from testit_api_client.models.test_plan_test_points_search_status_counters_api_result import TestPlanTestPointsSearchStatusCountersApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsSearchStatusCountersApiResult from a JSON string
test_plan_test_points_search_status_counters_api_result_instance = TestPlanTestPointsSearchStatusCountersApiResult.from_json(json)
# print the JSON string representation of the object
print(TestPlanTestPointsSearchStatusCountersApiResult.to_json())

# convert the object into a dict
test_plan_test_points_search_status_counters_api_result_dict = test_plan_test_points_search_status_counters_api_result_instance.to_dict()
# create an instance of TestPlanTestPointsSearchStatusCountersApiResult from a dict
test_plan_test_points_search_status_counters_api_result_from_dict = TestPlanTestPointsSearchStatusCountersApiResult.from_dict(test_plan_test_points_search_status_counters_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


