# TestRunModelTestPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | 
**id** | **str** |  | 
**name** | **str** |  | 
**project_id** | **str** |  | 
**started_on** | **datetime, none_type** | Set when test plan is starter (status changed to: In Progress) | [optional] 
**completed_on** | **datetime, none_type** | set when test plan status is completed (status changed to: Completed) | [optional] 
**created_date** | **datetime, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**global_id** | **int** | Used for search Test plan | [optional] 
**is_deleted** | **bool** |  | [optional] 
**locked_date** | **datetime, none_type** |  | [optional] 
**locked_by_id** | **str, none_type** |  | [optional] 
**tags** | [**[TagShortModel], none_type**](TagShortModel.md) |  | [optional] 
**start_date** | **datetime, none_type** | Used for analytics | [optional] 
**end_date** | **datetime, none_type** | Used for analytics | [optional] 
**description** | **str, none_type** |  | [optional] 
**build** | **str, none_type** |  | [optional] 
**product_name** | **str, none_type** |  | [optional] 
**has_automatic_duration_timer** | **bool, none_type** |  | [optional] 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


