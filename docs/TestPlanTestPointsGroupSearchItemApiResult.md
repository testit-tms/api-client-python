# TestPlanTestPointsGroupSearchItemApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | [**TestPlanTestPointsGroupApiResult**](TestPlanTestPointsGroupApiResult.md) |  | 
**items** | [**List[TestPlanTestPointsSearchApiResult]**](TestPlanTestPointsSearchApiResult.md) |  | 

## Example

```python
from testit_api_client.models.test_plan_test_points_group_search_item_api_result import TestPlanTestPointsGroupSearchItemApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsGroupSearchItemApiResult from a JSON string
test_plan_test_points_group_search_item_api_result_instance = TestPlanTestPointsGroupSearchItemApiResult.from_json(json)
# print the JSON string representation of the object
print TestPlanTestPointsGroupSearchItemApiResult.to_json()

# convert the object into a dict
test_plan_test_points_group_search_item_api_result_dict = test_plan_test_points_group_search_item_api_result_instance.to_dict()
# create an instance of TestPlanTestPointsGroupSearchItemApiResult from a dict
test_plan_test_points_group_search_item_api_result_from_dict = TestPlanTestPointsGroupSearchItemApiResult.from_dict(test_plan_test_points_group_search_item_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


