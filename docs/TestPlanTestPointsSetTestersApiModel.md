# TestPlanTestPointsSetTestersApiModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TestPlanTestPointsSearchApiModel**](TestPlanTestPointsSearchApiModel.md) |  | [optional] 
**extraction_model** | [**TestPlanTestPointsExtractionApiModel**](TestPlanTestPointsExtractionApiModel.md) |  | [optional] 
**tester_ids** | **List[str]** |  | 

## Example

```python
from testit_api_client.models.test_plan_test_points_set_testers_api_model import TestPlanTestPointsSetTestersApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsSetTestersApiModel from a JSON string
test_plan_test_points_set_testers_api_model_instance = TestPlanTestPointsSetTestersApiModel.from_json(json)
# print the JSON string representation of the object
print TestPlanTestPointsSetTestersApiModel.to_json()

# convert the object into a dict
test_plan_test_points_set_testers_api_model_dict = test_plan_test_points_set_testers_api_model_instance.to_dict()
# create an instance of TestPlanTestPointsSetTestersApiModel from a dict
test_plan_test_points_set_testers_api_model_from_dict = TestPlanTestPointsSetTestersApiModel.from_dict(test_plan_test_points_set_testers_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


