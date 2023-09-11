# TestRunModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_tests_count** | **int** |  | 
**is_automated** | **bool** |  | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**state_name** | [**TestRunState**](TestRunState.md) |  | 
**project_id** | **str** |  | 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 
**auto_tests** | [**[AutoTestModel], none_type**](AutoTestModel.md) |  | [optional] 
**test_suite_ids** | **[str], none_type** |  | [optional] 
**analytic** | [**TestRunAnalyticResultModel**](TestRunAnalyticResultModel.md) |  | [optional] 
**test_results** | [**[TestResultModel], none_type**](TestResultModel.md) |  | [optional] 
**test_plan** | [**TestPlanModel**](TestPlanModel.md) |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**created_by_user_name** | **str, none_type** |  | [optional] 
**started_date** | **datetime, none_type** |  | [optional] 
**completed_date** | **datetime, none_type** |  | [optional] 
**build** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**test_plan_id** | **str, none_type** |  | [optional] 
**run_by_user_id** | **str, none_type** |  | [optional] 
**stopped_by_user_id** | **str, none_type** |  | [optional] 
**name** | **str, none_type** |  | [optional] 
**launch_source** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


