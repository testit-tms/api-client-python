# WorkItemModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** | used for versioning changes in workitem | 
**median_duration** | **int** | used for getting a median duration of all autotests related to this workitem | 
**is_deleted** | **bool** |  | 
**project_id** | **str** |  | 
**entity_type_name** | [**WorkItemEntityTypes**](WorkItemEntityTypes.md) |  | 
**is_automated** | **bool** |  | 
**version_number** | **int** | used for define chronology of workitem state in each version | 
**created_date** | **datetime** |  | 
**created_by_id** | **str** |  | 
**global_id** | **int** |  | 
**id** | **str** |  | 
**section_id** | **str** |  | 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**steps** | [**[StepModel]**](StepModel.md) |  | 
**precondition_steps** | [**[StepModel]**](StepModel.md) |  | 
**postcondition_steps** | [**[StepModel]**](StepModel.md) |  | 
**duration** | **int** |  | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**tags** | [**[TagPutModel]**](TagPutModel.md) |  | 
**links** | [**[LinkModel]**](LinkModel.md) |  | 
**name** | **str** |  | 
**auto_tests** | [**[AutoTestModel], none_type**](AutoTestModel.md) |  | [optional] 
**attachments** | [**[AttachmentModel], none_type**](AttachmentModel.md) |  | [optional] 
**section_precondition_steps** | [**[StepModel], none_type**](StepModel.md) |  | [optional] 
**section_postcondition_steps** | [**[StepModel], none_type**](StepModel.md) |  | [optional] 
**iterations** | [**[IterationModel], none_type**](IterationModel.md) |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**description** | **str, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


