# TestRunV2GetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**started_on** | **datetime, none_type** |  | [optional] 
**completed_on** | **datetime, none_type** |  | [optional] 
**state_name** | [**TestRunStateTypeModel**](TestRunStateTypeModel.md) |  | [optional] 
**project_id** | **str** | This property is used to link test run with project | [optional] 
**test_plan_id** | **str, none_type** | This property is used to link test run with test plan | [optional] 
**test_results** | [**[TestResultV2GetModel], none_type**](TestResultV2GetModel.md) |  | [optional] 
**created_date** | **datetime, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**created_by_user_name** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**launch_source** | **str, none_type** | Once launch source is specified it cannot be updated | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


