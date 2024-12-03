# TestRunModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_tests** | [**List[AutoTestModel]**](AutoTestModel.md) |  | [optional] 
**auto_tests_count** | **int** |  | 
**test_suite_ids** | **List[str]** |  | [optional] 
**is_automated** | **bool** |  | 
**analytic** | [**TestRunAnalyticResultModel**](TestRunAnalyticResultModel.md) |  | 
**test_results** | [**List[TestResultModel]**](TestResultModel.md) |  | [optional] 
**test_plan** | [**TestPlanModel**](TestPlanModel.md) |  | [optional] 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**created_by_user_name** | **str** |  | [optional] 
**started_date** | **datetime** |  | [optional] 
**completed_date** | **datetime** |  | [optional] 
**build** | **str** |  | 
**description** | **str** |  | 
**state_name** | [**TestRunState**](TestRunState.md) |  | 
**project_id** | **str** |  | 
**test_plan_id** | **str** |  | [optional] 
**run_by_user_id** | **str** |  | [optional] 
**stopped_by_user_id** | **str** |  | [optional] 
**name** | **str** |  | 
**launch_source** | **str** |  | 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 

## Example

```python
from testit_api_client.models.test_run_model import TestRunModel

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunModel from a JSON string
test_run_model_instance = TestRunModel.from_json(json)
# print the JSON string representation of the object
print(TestRunModel.to_json())

# convert the object into a dict
test_run_model_dict = test_run_model_instance.to_dict()
# create an instance of TestRunModel from a dict
test_run_model_from_dict = TestRunModel.from_dict(test_run_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


