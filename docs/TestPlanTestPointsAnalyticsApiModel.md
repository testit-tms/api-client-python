# TestPlanTestPointsAnalyticsApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**TestPlanTestPointsSearchApiModel**](TestPlanTestPointsSearchApiModel.md) |  | [optional] 
**extraction_model** | [**TestPlanTestPointsExtractionApiModel**](TestPlanTestPointsExtractionApiModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_test_points_analytics_api_model import TestPlanTestPointsAnalyticsApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsAnalyticsApiModel from a JSON string
test_plan_test_points_analytics_api_model_instance = TestPlanTestPointsAnalyticsApiModel.from_json(json)
# print the JSON string representation of the object
print(TestPlanTestPointsAnalyticsApiModel.to_json())

# convert the object into a dict
test_plan_test_points_analytics_api_model_dict = test_plan_test_points_analytics_api_model_instance.to_dict()
# create an instance of TestPlanTestPointsAnalyticsApiModel from a dict
test_plan_test_points_analytics_api_model_from_dict = TestPlanTestPointsAnalyticsApiModel.from_dict(test_plan_test_points_analytics_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


