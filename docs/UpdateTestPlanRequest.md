# UpdateTestPlanRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**project_id** | **str** |  | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**locked_by_id** | **str, none_type** |  | [optional] 
**tags** | [**[TagPostModel], none_type**](TagPostModel.md) |  | [optional] 
**start_date** | **datetime, none_type** | Used for analytics | [optional] 
**end_date** | **datetime, none_type** | Used for analytics | [optional] 
**description** | **str, none_type** |  | [optional] 
**build** | **str, none_type** |  | [optional] 
**product_name** | **str, none_type** |  | [optional] 
**has_automatic_duration_timer** | **bool, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


