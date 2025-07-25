# AutoTestApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**project_id** | **str** |  | 
**name** | **str** |  | 
**is_flaky** | **bool** |  | 
**global_id** | **int** |  | 
**is_deleted** | **bool** |  | 
**must_be_approved** | **bool** |  | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**external_id** | **str, none_type** |  | [optional] 
**namespace** | **str, none_type** |  | [optional] 
**classname** | **str, none_type** |  | [optional] 
**steps** | [**[AutoTestStepApiResult], none_type**](AutoTestStepApiResult.md) |  | [optional] 
**setup** | [**[AutoTestStepApiResult], none_type**](AutoTestStepApiResult.md) |  | [optional] 
**teardown** | [**[AutoTestStepApiResult], none_type**](AutoTestStepApiResult.md) |  | [optional] 
**title** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**external_key** | **str, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**last_test_run_id** | **str, none_type** |  | [optional] 
**last_test_run_name** | **str, none_type** |  | [optional] 
**last_test_result_id** | **str, none_type** |  | [optional] 
**last_test_result_configuration** | [**ConfigurationShortApiResult**](ConfigurationShortApiResult.md) |  | [optional] 
**last_test_result_outcome** | **str, none_type** |  | [optional] 
**last_test_result_status** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | [optional] 
**stability_percentage** | **int, none_type** |  | [optional] 
**links** | [**[LinkApiResult], none_type**](LinkApiResult.md) |  | [optional] 
**labels** | [**[LabelApiResult], none_type**](LabelApiResult.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


