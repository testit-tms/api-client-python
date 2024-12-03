# TestPlanSummaryModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_test_points_count** | **int** |  | 
**manual_test_points_count** | **int** |  | 
**automated_test_points_count** | **int** |  | 
**completed_test_points_count** | **int** |  | 
**defects_count** | **int** |  | 
**planned_test_points_duration** | **int** |  | 
**spent_test_points_duration** | **int** |  | [optional] 

## Example

```python
from testit_api_client.models.test_plan_summary_model import TestPlanSummaryModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestPlanSummaryModel from a JSON string
test_plan_summary_model_instance = TestPlanSummaryModel.from_json(json)
# print the JSON string representation of the object
print(TestPlanSummaryModel.to_json())

# convert the object into a dict
test_plan_summary_model_dict = test_plan_summary_model_instance.to_dict()
# create an instance of TestPlanSummaryModel from a dict
test_plan_summary_model_from_dict = TestPlanSummaryModel.from_dict(test_plan_summary_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


