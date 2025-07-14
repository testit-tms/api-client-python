# TestRunApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 
**started_date** | **datetime** |  | [optional] 
**completed_date** | **datetime** |  | [optional] 
**build** | **str** |  | 
**description** | **str** |  | [optional] 
**state_name** | [**TestRunState**](TestRunState.md) |  | 
**status** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | 
**project_id** | **str** |  | 
**test_plan_id** | **str** |  | [optional] 
**run_by_user_id** | **str** |  | [optional] 
**stopped_by_user_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**launch_source** | **str** |  | [optional] 
**auto_tests** | [**List[AutoTestApiResult]**](AutoTestApiResult.md) |  | 
**auto_tests_count** | **int** |  | 
**test_suite_ids** | **List[str]** |  | 
**is_automated** | **bool** |  | 
**analytic** | [**TestRunAnalyticApiResult**](TestRunAnalyticApiResult.md) |  | 
**test_results** | [**List[TestResultApiResult]**](TestResultApiResult.md) |  | 
**test_plan** | [**TestPlanApiResult**](TestPlanApiResult.md) |  | [optional] 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | [optional] 
**created_by_id** | **str** |  | 
**modified_by_id** | **str** |  | [optional] 
**created_by_user_name** | **str** |  | [optional] 

## Example

```python
from testit_api_client.models.test_run_api_result import TestRunApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TestRunApiResult from a JSON string
test_run_api_result_instance = TestRunApiResult.from_json(json)
# print the JSON string representation of the object
print TestRunApiResult.to_json()

# convert the object into a dict
test_run_api_result_dict = test_run_api_result_instance.to_dict()
# create an instance of TestRunApiResult from a dict
test_run_api_result_from_dict = TestRunApiResult.from_dict(test_run_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


