# AutoTestModelV2GetModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** | This property is used to link autotest with project | 
**global_id** | **int** |  | 
**created_by_id** | **str** |  | 
**id** | **str** | Unique ID of the entity | 
**is_deleted** | **bool** | Indicates if the entity is deleted | 
**external_id** | **str, none_type** | This property is used to set autotest identifier from client system | [optional] 
**links** | [**[LinkModel], none_type**](LinkModel.md) |  | [optional] 
**name** | **str, none_type** |  | [optional] 
**namespace** | **str, none_type** |  | [optional] 
**classname** | **str, none_type** |  | [optional] 
**steps** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) |  | [optional] 
**setup** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) |  | [optional] 
**teardown** | [**[AutoTestStepModel], none_type**](AutoTestStepModel.md) |  | [optional] 
**created_date** | **datetime, none_type** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**labels** | [**[LabelShortModel], none_type**](LabelShortModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


