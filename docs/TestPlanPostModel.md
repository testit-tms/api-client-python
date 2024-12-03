# TestPlanPostModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from testit_api_client.models.test_plan_post_model import TestPlanPostModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanPostModel from a JSON string
test_plan_post_model_instance = TestPlanPostModel.from_json(json)
# print the JSON string representation of the object
print(TestPlanPostModel.to_json())

# convert the object into a dict
test_plan_post_model_dict = test_plan_post_model_instance.to_dict()
# create an instance of TestPlanPostModel from a dict
test_plan_post_model_from_dict = TestPlanPostModel.from_dict(test_plan_post_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


