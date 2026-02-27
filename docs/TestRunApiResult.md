# TestRunApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 
**build** | **str** |  | 
**state_name** | [**TestRunState**](TestRunState.md) |  | 
**status** | [**AutoTestResultHistoryApiResultStatus**](AutoTestResultHistoryApiResultStatus.md) |  | 
**project_id** | **str** |  | 
**auto_tests** | [**[AutoTestApiResult]**](AutoTestApiResult.md) |  | 
**auto_tests_count** | **int** |  | 
**test_suite_ids** | **[str]** |  | 
**is_automated** | **bool** |  | 
**analytic** | [**TestRunApiResultAnalytic**](TestRunApiResultAnalytic.md) |  | 
**test_results** | [**[TestResultApiResult]**](TestResultApiResult.md) |  | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**tags** | **[str]** |  | 
**started_date** | **datetime, none_type** |  | [optional] 
**completed_date** | **datetime, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**test_plan_id** | **str, none_type** |  | [optional] 
**run_by_user_id** | **str, none_type** |  | [optional] 
**stopped_by_user_id** | **str, none_type** |  | [optional] 
**name** | **str, none_type** |  | [optional] 
**launch_source** | **str, none_type** |  | [optional] 
**test_plan** | [**TestPlanApiResult**](TestPlanApiResult.md) |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**created_by_user_name** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


