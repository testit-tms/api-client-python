# TestPlanApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**started_on** | **datetime** |  | [optional] 
**completed_on** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**build** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**status** | [**TestPlanStatus**](TestPlanStatus.md) |  | 
**tags** | [**List[TestPlanTagApiResult]**](TestPlanTagApiResult.md) |  | 
**global_id** | **int** |  | 
**has_automatic_duration_timer** | **bool** |  | [optional] 
**locked_by_id** | **str** |  | [optional] 
**locked_date** | **datetime** |  | [optional] 
**attributes** | **Dict[str, object]** |  | 
**created_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**is_deleted** | **bool** |  | 

## Example

```python
from testit_api_client.models.test_plan_api_result import TestPlanApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanApiResult from a JSON string
test_plan_api_result_instance = TestPlanApiResult.from_json(json)
# print the JSON string representation of the object
print TestPlanApiResult.to_json()

# convert the object into a dict
test_plan_api_result_dict = test_plan_api_result_instance.to_dict()
# create an instance of TestPlanApiResult from a dict
test_plan_api_result_from_dict = TestPlanApiResult.from_dict(test_plan_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


