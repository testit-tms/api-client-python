# TestPlanPutModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from testit_api_client.models.test_plan_put_model import TestPlanPutModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanPutModel from a JSON string
test_plan_put_model_instance = TestPlanPutModel.from_json(json)
# print the JSON string representation of the object
print(TestPlanPutModel.to_json())

# convert the object into a dict
test_plan_put_model_dict = test_plan_put_model_instance.to_dict()
# create an instance of TestPlanPutModel from a dict
test_plan_put_model_from_dict = TestPlanPutModel.from_dict(test_plan_put_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


