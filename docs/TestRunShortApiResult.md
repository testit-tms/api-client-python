# TestRunShortApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the test run | 
**name** | **str** | Name of the test run | 
**state** | [**TestRunState**](TestRunState.md) |  | 
**status** | [**TestRunShortApiResultStatus**](TestRunShortApiResultStatus.md) |  | 
**created_date** | **datetime** | Date when the test run was created | 
**created_by_id** | **str** | Unique ID of user who created the test run | 
**is_deleted** | **bool** | Is the test run is deleted | 
**auto_tests_count** | **int** | Number of AutoTests run in the test run | 
**statistics** | [**TestRunShortApiResultStatistics**](TestRunShortApiResultStatistics.md) |  | 
**test_results_configurations** | [**[ConfigurationShortApiResult]**](ConfigurationShortApiResult.md) | Test results configurations | 
**started_date** | **datetime, none_type** | Date when the test run was started | [optional] 
**completed_date** | **datetime, none_type** | Completion date of the test run | [optional] 
**modified_by_id** | **str, none_type** | Unique ID of user who modified the test run last time | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


