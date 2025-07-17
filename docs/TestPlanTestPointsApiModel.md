# TestPlanTestPointsApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TestPlanTestPointsSearchApiModel**](TestPlanTestPointsSearchApiModel.md) |  | [optional] 
**group** | [**TestPlanTestPointsGroupApiModel**](TestPlanTestPointsGroupApiModel.md) |  | [optional] 
**inquiry** | [**TestPlanTestPointsInquiryApiModel**](TestPlanTestPointsInquiryApiModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_test_points_api_model import TestPlanTestPointsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsApiModel from a JSON string
test_plan_test_points_api_model_instance = TestPlanTestPointsApiModel.from_json(json)
# print the JSON string representation of the object
print TestPlanTestPointsApiModel.to_json()

# convert the object into a dict
test_plan_test_points_api_model_dict = test_plan_test_points_api_model_instance.to_dict()
# create an instance of TestPlanTestPointsApiModel from a dict
test_plan_test_points_api_model_from_dict = TestPlanTestPointsApiModel.from_dict(test_plan_test_points_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


