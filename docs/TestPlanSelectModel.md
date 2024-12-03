# TestPlanSelectModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**ProjectTestPlansFilterModel**](ProjectTestPlansFilterModel.md) |  | 
**extraction_model** | [**TestPlanExtractionModel**](TestPlanExtractionModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_select_model import TestPlanSelectModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanSelectModel from a JSON string
test_plan_select_model_instance = TestPlanSelectModel.from_json(json)
# print the JSON string representation of the object
print(TestPlanSelectModel.to_json())

# convert the object into a dict
test_plan_select_model_dict = test_plan_select_model_instance.to_dict()
# create an instance of TestPlanSelectModel from a dict
test_plan_select_model_from_dict = TestPlanSelectModel.from_dict(test_plan_select_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


