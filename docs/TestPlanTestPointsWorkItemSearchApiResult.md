# TestPlanTestPointsWorkItemSearchApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**global_id** | **int** |  | 
**version_id** | **str** |  | 
**version_number** | **int** |  | 
**median_duration** | **int** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**duration** | **int** |  | 
**state** | [**WorkItemState**](WorkItemState.md) |  | 
**tags** | **List[str]** |  | 
**attributes** | **Dict[str, object]** |  | 
**order_rank** | **str** |  | [optional] 
**is_automated** | **bool** |  | 
**name** | **str** |  | 
**priority** | [**WorkItemPriority**](WorkItemPriority.md) |  | 
**section** | [**TestPlanTestPointsSectionSearchApiResult**](TestPlanTestPointsSectionSearchApiResult.md) |  | 
**created** | [**AuditApiResult**](AuditApiResult.md) |  | 
**modified** | [**AuditApiResult**](AuditApiResult.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_test_points_work_item_search_api_result import TestPlanTestPointsWorkItemSearchApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsWorkItemSearchApiResult from a JSON string
test_plan_test_points_work_item_search_api_result_instance = TestPlanTestPointsWorkItemSearchApiResult.from_json(json)
# print the JSON string representation of the object
print TestPlanTestPointsWorkItemSearchApiResult.to_json()

# convert the object into a dict
test_plan_test_points_work_item_search_api_result_dict = test_plan_test_points_work_item_search_api_result_instance.to_dict()
# create an instance of TestPlanTestPointsWorkItemSearchApiResult from a dict
test_plan_test_points_work_item_search_api_result_from_dict = TestPlanTestPointsWorkItemSearchApiResult.from_dict(test_plan_test_points_work_item_search_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


