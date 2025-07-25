# CreateTestPlanRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Test plan name | 
**project_id** | **str** | Project unique identifier | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Key value pair of test plan custom attributes | 
**tags** | [**[TagApiModel], none_type**](TagApiModel.md) | Test plan tag names collection | [optional] 
**start_date** | **datetime, none_type** | Date and time of test plan start | [optional] 
**end_date** | **datetime, none_type** | Date and time of test plan end | [optional] 
**description** | **str, none_type** | Test plan description | [optional] 
**build** | **str, none_type** | Build of the application on which test plan is executed | [optional] 
**product_name** | **str, none_type** | Name of the testing product | [optional] 
**has_automatic_duration_timer** | **bool, none_type** | Boolean flag defines if test plan has automatic duration timer | [optional] 
**test_suite** | [**TestSuiteTestPlanApiModel**](TestSuiteTestPlanApiModel.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


