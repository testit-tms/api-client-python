# TestPlanWithAnalyticModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytic** | [**TestPointAnalyticResult**](TestPointAnalyticResult.md) |  | 
**status** | [**TestPlanStatusModel**](TestPlanStatusModel.md) |  | 
**started_on** | **datetime** | Set when test plan is starter (status changed to: In Progress) | [optional] 
**completed_on** | **datetime** | set when test plan status is completed (status changed to: Completed) | [optional] 
**created_date** | **datetime** |  | [optional] 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**global_id** | **int** | Used for search Test plan | 
**is_deleted** | **bool** |  | 
**locked_date** | **datetime** |  | [optional] 
**id** | **str** |  | 
**locked_by_id** | **str** |  | [optional] 
**tags** | [**List[TagPostModel]**](TagPostModel.md) |  | [optional] 
**name** | **str** |  | 
**start_date** | **datetime** | Used for analytics | [optional] 
**end_date** | **datetime** | Used for analytics | [optional] 
**description** | **str** |  | [optional] 
**build** | **str** |  | [optional] 
**project_id** | **str** |  | 
**product_name** | **str** |  | [optional] 
**has_automatic_duration_timer** | **bool** |  | [optional] 
**attributes** | **Dict[str, Optional[object]]** |  | 

## Example

```python
from testit_api_client.models.test_plan_with_analytic_model import TestPlanWithAnalyticModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanWithAnalyticModel from a JSON string
test_plan_with_analytic_model_instance = TestPlanWithAnalyticModel.from_json(json)
# print the JSON string representation of the object
print(TestPlanWithAnalyticModel.to_json())

# convert the object into a dict
test_plan_with_analytic_model_dict = test_plan_with_analytic_model_instance.to_dict()
# create an instance of TestPlanWithAnalyticModel from a dict
test_plan_with_analytic_model_from_dict = TestPlanWithAnalyticModel.from_dict(test_plan_with_analytic_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


