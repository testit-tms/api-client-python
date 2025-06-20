# TestPlanTestPointsGroupSearchApiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TestPlanTestPointsGroupSearchItemApiResult]**](TestPlanTestPointsGroupSearchItemApiResult.md) |  | 
**total_count** | **int** |  | 
**status_counters** | [**TestPlanTestPointsSearchStatusCountersApiResult**](TestPlanTestPointsSearchStatusCountersApiResult.md) |  | 

## Example

```python
from testit_api_client.models.test_plan_test_points_group_search_api_result import TestPlanTestPointsGroupSearchApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsGroupSearchApiResult from a JSON string
test_plan_test_points_group_search_api_result_instance = TestPlanTestPointsGroupSearchApiResult.from_json(json)
# print the JSON string representation of the object
print(TestPlanTestPointsGroupSearchApiResult.to_json())

# convert the object into a dict
test_plan_test_points_group_search_api_result_dict = test_plan_test_points_group_search_api_result_instance.to_dict()
# create an instance of TestPlanTestPointsGroupSearchApiResult from a dict
test_plan_test_points_group_search_api_result_from_dict = TestPlanTestPointsGroupSearchApiResult.from_dict(test_plan_test_points_group_search_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


