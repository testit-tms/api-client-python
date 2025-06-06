# TestPlanTestPointsExtractionApiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**GuidExtractionModel**](GuidExtractionModel.md) | Extraction parameters for test points | [optional] 

## Example

```python
from testit_api_client.models.test_plan_test_points_extraction_api_model import TestPlanTestPointsExtractionApiModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanTestPointsExtractionApiModel from a JSON string
test_plan_test_points_extraction_api_model_instance = TestPlanTestPointsExtractionApiModel.from_json(json)
# print the JSON string representation of the object
print(TestPlanTestPointsExtractionApiModel.to_json())

# convert the object into a dict
test_plan_test_points_extraction_api_model_dict = test_plan_test_points_extraction_api_model_instance.to_dict()
# create an instance of TestPlanTestPointsExtractionApiModel from a dict
test_plan_test_points_extraction_api_model_from_dict = TestPlanTestPointsExtractionApiModel.from_dict(test_plan_test_points_extraction_api_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


