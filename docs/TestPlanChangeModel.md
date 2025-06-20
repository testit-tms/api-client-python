# TestPlanChangeModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**test_plan_id** | **str** |  | 
**test_plan_changed_fields** | [**TestPlanChangedFieldsViewModel**](TestPlanChangedFieldsViewModel.md) |  | 
**created_by_id** | **str** |  | 
**created_date** | **datetime** |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_change_model import TestPlanChangeModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanChangeModel from a JSON string
test_plan_change_model_instance = TestPlanChangeModel.from_json(json)
# print the JSON string representation of the object
print TestPlanChangeModel.to_json()

# convert the object into a dict
test_plan_change_model_dict = test_plan_change_model_instance.to_dict()
# create an instance of TestPlanChangeModel from a dict
test_plan_change_model_from_dict = TestPlanChangeModel.from_dict(test_plan_change_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


