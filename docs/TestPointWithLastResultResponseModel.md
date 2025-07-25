# TestPointWithLastResultResponseModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_automated** | **bool** |  | 
**work_item_id** | **str** |  | 
**test_suite_id** | **str** |  | 
**section_id** | **str** |  | 
**created_by_id** | **str** |  | 
**duration** | **int** |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**work_item_name** | **str, none_type** |  | [optional] 
**tester_id** | **str, none_type** |  | [optional] 
**configuration_id** | **str, none_type** |  | [optional] 
**last_test_result** | [**LastTestResultModel**](LastTestResultModel.md) |  | [optional] 
**status** | **str, none_type** |  | [optional] 
**status_model** | [**TestStatusApiResult**](TestStatusApiResult.md) |  | [optional] 
**work_item_global_id** | **int, none_type** |  | [optional] 
**work_item_entity_type_name** | **str, none_type** |  | [optional] 
**section_name** | **str, none_type** |  | [optional] 
**created_date** | **datetime, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 
**tag_names** | **[str], none_type** |  | [optional] 
**test_suite_name_bread_crumbs** | **[str], none_type** |  | [optional] 
**group_count** | **int, none_type** |  | [optional] 
**iteration** | [**IterationModel**](IterationModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


