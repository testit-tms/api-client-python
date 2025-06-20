# TestPlanShortModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project_id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from testit_api_client.models.test_plan_short_model import TestPlanShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanShortModel from a JSON string
test_plan_short_model_instance = TestPlanShortModel.from_json(json)
# print the JSON string representation of the object
print TestPlanShortModel.to_json()

# convert the object into a dict
test_plan_short_model_dict = test_plan_short_model_instance.to_dict()
# create an instance of TestPlanShortModel from a dict
test_plan_short_model_from_dict = TestPlanShortModel.from_dict(test_plan_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


