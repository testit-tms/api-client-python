# ProjectShortModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID of the project | 
**name** | **str** | Name of the project | 
**is_favorite** | **bool** | Indicates if the project is marked as favorite | 
**is_deleted** | **bool** | Indicates if the project is deleted | 
**created_date** | **datetime** | Creation date of the project | 
**created_by_id** | **str** | Unique ID of the project creator | 
**global_id** | **int** | Global ID of the project | 
**type** | [**ProjectTypeModel**](ProjectTypeModel.md) |  | 
**workflow_id** | **str** |  | 
**description** | **str, none_type** | Description of the project | [optional] 
**test_cases_count** | **int, none_type** | Number of test cases in the project | [optional] 
**shared_steps_count** | **int, none_type** | Number of shared steps in the project | [optional] 
**check_lists_count** | **int, none_type** | Number of checklists in the project | [optional] 
**auto_tests_count** | **int, none_type** | Number of autotests in the project | [optional] 
**modified_date** | **datetime, none_type** | Last modification date of the project | [optional] 
**modified_by_id** | **str, none_type** | Unique ID of the project last editor | [optional] 
**is_flaky_auto** | **bool, none_type** | Indicates if the status \&quot;Flaky/Stable\&quot; sets automatically | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


