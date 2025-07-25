# UpdateTestPlanRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Test plan unique internal identifier | 
**name** | **str** | Test plan name | 
**project_id** | **str** | Project unique identifier | 
**locked_by_id** | **str, none_type** | User who locked test plan modification internal identifier | [optional] 
**start_date** | **datetime, none_type** | Date and time of test plan start | [optional] 
**end_date** | **datetime, none_type** | Date and time of test plan end | [optional] 
**description** | **str, none_type** | Test plan description | [optional] 
**build** | **str, none_type** | Build of the application on which test plan is executed | [optional] 
**product_name** | **str, none_type** | Name of the testing product | [optional] 
**has_automatic_duration_timer** | **bool, none_type** | Boolean flag defines if test plan has automatic duration timer | [optional] 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Key value pair of test plan custom attributes | [optional] 
**tags** | [**[TagApiModel], none_type**](TagApiModel.md) | Test plan tag names collection | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


