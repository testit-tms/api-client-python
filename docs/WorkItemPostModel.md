# WorkItemPostModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type_name** | [**WorkItemEntityTypes**](WorkItemEntityTypes.md) |  | 
**state** | [**WorkItemStates**](WorkItemStates.md) |  | 
**priority** | [**WorkItemPriorityModel**](WorkItemPriorityModel.md) |  | 
**steps** | [**[StepPutModel]**](StepPutModel.md) |  | 
**precondition_steps** | [**[StepPutModel]**](StepPutModel.md) |  | 
**postcondition_steps** | [**[StepPutModel]**](StepPutModel.md) |  | 
**duration** | **int** | Must be 0 for shared steps and greater than 0 for the other types of work items | 
**attributes** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** |  | 
**tags** | [**[TagShortModel]**](TagShortModel.md) |  | 
**links** | [**[LinkPostModel]**](LinkPostModel.md) |  | 
**name** | **str** |  | 
**project_id** | **str** | This property is used to link workitem with project | 
**section_id** | **str** |  | 
**description** | **str, none_type** |  | [optional] 
**attachments** | [**[AttachmentPutModel], none_type**](AttachmentPutModel.md) |  | [optional] 
**iterations** | [**[IterationPutModel], none_type**](IterationPutModel.md) |  | [optional] 
**auto_tests** | [**[AutoTestIdModel], none_type**](AutoTestIdModel.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


