# WorkItemModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_name** | [**WorkItemEntityTypes**](WorkItemEntityTypes.md) |  | 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**steps** | [**[StepModel]**](StepModel.md) |  | 
**precondition_steps** | [**[StepModel]**](StepModel.md) |  | 
**postcondition_steps** | [**[StepModel]**](StepModel.md) |  | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**tags** | [**[TagShortModel]**](TagShortModel.md) |  | 
**links** | [**[LinkModel]**](LinkModel.md) |  | 
**name** | **str** |  | 
**version_id** | **str** | used for versioning changes in workitem | [optional] 
**median_duration** | **int** | used for getting a median duration of all autotests related to this workitem | [optional] 
**is_deleted** | **bool** |  | [optional] 
**project_id** | **str** |  | [optional] 
**is_automated** | **bool** |  | [optional] 
**auto_tests** | [**[AutoTestModel], none_type**](AutoTestModel.md) |  | [optional] 
**attachments** | [**[AttachmentModel], none_type**](AttachmentModel.md) |  | [optional] 
**section_precondition_steps** | [**[StepModel], none_type**](StepModel.md) |  | [optional] 
**section_postcondition_steps** | [**[StepModel], none_type**](StepModel.md) |  | [optional] 
**version_number** | **int** | used for define chronology of workitem state in each version | [optional] 
**iterations** | [**[IterationModel], none_type**](IterationModel.md) |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**modified_date** | **datetime, none_type** |  | [optional] 
**created_by_id** | **str** |  | [optional] 
**modified_by_id** | **str, none_type** |  | [optional] 
**global_id** | **int** |  | [optional] 
**id** | **str** |  | [optional] 
**section_id** | **str** |  | [optional] 
**description** | **str, none_type** |  | [optional] 
**duration** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


