# TestPlanTestPointsAutoTestsRerunApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TestPlanTestPointsSearchApiModel**](TestPlanTestPointsSearchApiModel.md) |  | [optional] 
**extraction_model** | [**TestPlanTestPointsExtractionApiModel**](TestPlanTestPointsExtractionApiModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_test_points_auto_tests_rerun_api_model import TestPlanTestPointsAutoTestsRerunApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsAutoTestsRerunApiModel from a JSON string
test_plan_test_points_auto_tests_rerun_api_model_instance = TestPlanTestPointsAutoTestsRerunApiModel.from_json(json)
# print the JSON string representation of the object
print(TestPlanTestPointsAutoTestsRerunApiModel.to_json())

# convert the object into a dict
test_plan_test_points_auto_tests_rerun_api_model_dict = test_plan_test_points_auto_tests_rerun_api_model_instance.to_dict()
# create an instance of TestPlanTestPointsAutoTestsRerunApiModel from a dict
test_plan_test_points_auto_tests_rerun_api_model_from_dict = TestPlanTestPointsAutoTestsRerunApiModel.from_dict(test_plan_test_points_auto_tests_rerun_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


