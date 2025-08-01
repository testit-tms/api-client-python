# AutoTestResultHistoryApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**test_run_id** | **str** |  | 
**configuration_id** | **str** |  | 
**configuration_name** | **str** |  | 
**outcome** | [**AutotestResultOutcome**](AutotestResultOutcome.md) |  | 
**status** | [**AutoTestResultHistoryApiResultStatus**](AutoTestResultHistoryApiResultStatus.md) |  | 
**rerun_count** | **int** |  | 
**rerun_test_results** | [**[RerunTestResultApiResult]**](RerunTestResultApiResult.md) |  | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**test_plan_id** | **str, none_type** |  | [optional] 
**test_plan_global_id** | **int, none_type** |  | [optional] 
**test_plan_name** | **str, none_type** |  | [optional] 
**duration** | **int, none_type** |  | [optional] 
**test_run_name** | **str, none_type** |  | [optional] 
**launch_source** | **str, none_type** |  | [optional] 
**created_by_name** | **str, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


